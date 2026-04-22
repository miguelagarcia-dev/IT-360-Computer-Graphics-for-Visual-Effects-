#!/usr/bin/python

# This is statement is required by the build system to query build info
if __name__ == '__build__':
    raise Exception

import sys
import math
from math import cos as cos
from math import sin as sin
from math import pi as PI
from math import sqrt as sqrt
import glfw 

try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
except BaseException:
    print('''
ERROR: PyOpenGL not installed properly.
        ''')
    sys.exit()


screen_dimx = 800
screen_dimy = 800
screen_leftx = 0
screen_rightx = 1
screen_topy = 0
screen_bottomy = 1
screen_world_width = screen_rightx-screen_leftx
screen_world_height = screen_bottomy-screen_topy

time_delta = 0.1
grid_size = 64
last_time = 0.0
mouse_down = False
prev_mouse_x = None
prev_mouse_y = None


class SmokeSimulator:
    def __init__(self, size=64, dt=0.1):
        self.N = size
        self.dt = dt
        self.diff = 0.0001  # diffusion rate
        self.visc = 0.0001  # viscosity
        
        # Velocity fields (u, v for 2D)
        self.u = [[0.0 for _ in range(self.N + 2)] for _ in range(self.N + 2)]
        self.v = [[0.0 for _ in range(self.N + 2)] for _ in range(self.N + 2)]
        self.u_prev = [[0.0 for _ in range(self.N + 2)] for _ in range(self.N + 2)]
        self.v_prev = [[0.0 for _ in range(self.N + 2)] for _ in range(self.N + 2)]
        
        # Density field (smoke)
        self.dens = [[0.0 for _ in range(self.N + 2)] for _ in range(self.N + 2)]
        self.dens_prev = [[0.0 for _ in range(self.N + 2)] for _ in range(self.N + 2)]
        
        # Temperature field for buoyancy
        self.temp = [[0.0 for _ in range(self.N + 2)] for _ in range(self.N + 2)]
        self.temp_prev = [[0.0 for _ in range(self.N + 2)] for _ in range(self.N + 2)]
        
    def add_source(self, x, s, dt):
        """Add source term"""
        for i in range(len(x)):
            for j in range(len(x[0])):
                x[i][j] += dt * s[i][j]
        
    def set_bounds(self, b, x):
        """Set boundary conditions"""
        N = self.N
        # Edges
        for i in range(1, N + 1):
            x[0][i] = -x[1][i] if b == 1 else x[1][i]
            x[N + 1][i] = -x[N][i] if b == 1 else x[N][i]
            x[i][0] = -x[i][1] if b == 2 else x[i][1]
            x[i][N + 1] = -x[i][N] if b == 2 else x[i][N]
        
        # Corners
        x[0][0] = 0.5 * (x[1][0] + x[0][1])
        x[0][N + 1] = 0.5 * (x[1][N + 1] + x[0][N])
        x[N + 1][0] = 0.5 * (x[N][0] + x[N + 1][1])
        x[N + 1][N + 1] = 0.5 * (x[N][N + 1] + x[N + 1][N])
    
    def lin_solve(self, b, x, x0, a, c):
        """Linear solver (Gauss-Seidel relaxation)"""
        N = self.N
        for k in range(20):  # iterations
            for i in range(1, N + 1):
                for j in range(1, N + 1):
                    x[i][j] = (x0[i][j] + a * (x[i-1][j] + x[i+1][j] + 
                                                x[i][j-1] + x[i][j+1])) / c
            self.set_bounds(b, x)
    
    def diffuse(self, b, x, x0, diff, dt):
        """Diffusion step using implicit method"""
        a = dt * diff * self.N * self.N
        self.lin_solve(b, x, x0, a, 1 + 4 * a)
    
    def advect(self, b, d, d0, u, v, dt):
        """Advection step using method of characteristics (backtracing)"""
        N = self.N
        dt0 = dt * N
        
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                # Backtrace
                x = i - dt0 * u[i][j]
                y = j - dt0 * v[i][j]
                
                # Clamp to grid boundaries
                if x < 0.5:
                    x = 0.5
                if x > N + 0.5:
                    x = N + 0.5
                if y < 0.5:
                    y = 0.5
                if y > N + 0.5:
                    y = N + 0.5
                
                # Bilinear interpolation
                i0 = int(x)
                i1 = i0 + 1
                j0 = int(y)
                j1 = j0 + 1
                
                s1 = x - i0
                s0 = 1.0 - s1
                t1 = y - j0
                t0 = 1.0 - t1
                
                d[i][j] = (s0 * (t0 * d0[i0][j0] + t1 * d0[i0][j1]) +
                          s1 * (t0 * d0[i1][j0] + t1 * d0[i1][j1]))
        
        self.set_bounds(b, d)
    
    def project(self, u, v, p, div):
        """Projection step to ensure incompressibility"""
        N = self.N
        h = 1.0 / N
        
        # Compute divergence
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                div[i][j] = -0.5 * h * (u[i+1][j] - u[i-1][j] + 
                                        v[i][j+1] - v[i][j-1])
                p[i][j] = 0.0
        
        self.set_bounds(0, div)
        self.set_bounds(0, p)
        
        # Solve Poisson equation
        self.lin_solve(0, p, div, 1.0, 4.0)
        
        # Subtract gradient
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                u[i][j] -= 0.5 * (p[i+1][j] - p[i-1][j]) / h
                v[i][j] -= 0.5 * (p[i][j+1] - p[i][j-1]) / h
        
        self.set_bounds(1, u)
        self.set_bounds(2, v)
    
    def vel_step(self):
        """Velocity step of the fluid solver"""
        # Add forces
        self.add_source(self.u, self.u_prev, self.dt)
        self.add_source(self.v, self.v_prev, self.dt)
        
        # Swap for diffusion
        self.u, self.u_prev = self.u_prev, self.u
        self.diffuse(1, self.u, self.u_prev, self.visc, self.dt)
        self.v, self.v_prev = self.v_prev, self.v
        self.diffuse(2, self.v, self.v_prev, self.visc, self.dt)
        
        # Project
        self.project(self.u, self.v, self.u_prev, self.v_prev)
        
        # Swap for advection
        self.u, self.u_prev = self.u_prev, self.u
        self.v, self.v_prev = self.v_prev, self.v
        self.advect(1, self.u, self.u_prev, self.u_prev, self.v_prev, self.dt)
        self.advect(2, self.v, self.v_prev, self.u_prev, self.v_prev, self.dt)
        
        # Project again
        self.project(self.u, self.v, self.u_prev, self.v_prev)
    
    def dens_step(self, x, x_prev):
        """Density step"""
        # Add source
        self.add_source(x, x_prev, self.dt)
        
        # Swap for diffusion
        temp = x
        x = x_prev
        x_prev = temp
        self.diffuse(0, x, x_prev, self.diff, self.dt)
        
        # Swap for advection
        temp = x
        x = x_prev
        x_prev = temp
        self.advect(0, x, x_prev, self.u, self.v, self.dt)
        
        # Dissipation (smoke fades)
        for i in range(len(x)):
            for j in range(len(x[0])):
                x[i][j] *= 0.995
        
        return x
    
    def add_buoyancy(self):
        """Add buoyancy force based on temperature"""
        buoyancy = 0.5  # buoyancy strength
        for i in range(1, self.N + 1):
            for j in range(1, self.N + 1):
                self.v[i][j] += self.dt * buoyancy * self.temp[i][j]
    
    def add_smoke(self, x, y, amount, temp_amount):
        """Add smoke at a specific location"""
        i = int(x * self.N)
        j = int(y * self.N)
        
        if 1 <= i <= self.N and 1 <= j <= self.N:
            self.dens_prev[i][j] += amount
            self.temp_prev[i][j] += temp_amount
    
    def add_velocity(self, x, y, vx, vy):
        """Add velocity at a specific location"""
        i = int(x * self.N)
        j = int(y * self.N)
        
        if 1 <= i <= self.N and 1 <= j <= self.N:
            self.u_prev[i][j] += vx
            self.v_prev[i][j] += vy
    
    def clear_prev(self):
        """Clear previous step data"""
        for i in range(self.N + 2):
            for j in range(self.N + 2):
                self.u_prev[i][j] = 0.0
                self.v_prev[i][j] = 0.0
                self.dens_prev[i][j] = 0.0
                self.temp_prev[i][j] = 0.0


# Initialize simulator
simulator = SmokeSimulator(size=grid_size, dt=time_delta)


def draw_smoke():
    """Render smoke density field"""
    global simulator
    
    N = simulator.N
    h = 1.0 / N
    
    # Draw smoke as colored quads
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            x = (i - 0.5) * h
            y = (j - 0.5) * h
            
            # Get density and temperature for color
            d = simulator.dens[i][j]
            if d > 1.0:
                d = 1.0
            t = simulator.temp[i][j]
            if t > 1.0:
                t = 1.0
            
            if d > 0.01:  # Only render visible smoke
                # Color: white/gray smoke with orange tint for hot areas
                r = d * 0.8 + t * 0.5
                g = d * 0.8 + t * 0.3
                b = d * 0.8
                a = d
                
                glColor4f(r, g, b, a)
                glBegin(GL_QUADS)
                glVertex2f(x, y)
                glVertex2f(x + h, y)
                glVertex2f(x + h, y + h)
                glVertex2f(x, y + h)
                glEnd()


def smoke_main_loop():
    global simulator
    
    # Add buoyancy - line 5
    simulator.add_buoyancy()
    
    # Velocity step - line 5 through line 11
    simulator.vel_step()
    
    # Density step - line 8 through line 11
    simulator.dens = simulator.dens_step(simulator.dens, simulator.dens_prev)
    
    # Temperature step (similar to density) - line 8 through line 11
    simulator.temp = simulator.dens_step(simulator.temp, simulator.temp_prev)
    
    # Clear previous step data - line 12
    simulator.clear_prev()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_smoke()
    glFlush()


def translate_to_world_coords(screenx, screeny):
    x = screenx / screen_dimx
    y = 1.0 - screeny / screen_dimy
    return (x, y)


def mouse_button_callback(window, button, action, mods):
    global mouse_down, prev_mouse_x, prev_mouse_y
    
    x, y = glfw.get_cursor_pos(window)
    worldx, worldy = translate_to_world_coords(x, y)
    
    if button == 0:  # Left mouse button
        if action == glfw.PRESS:
            mouse_down = True
            prev_mouse_x = x
            prev_mouse_y = y
        elif action == glfw.RELEASE:
            mouse_down = False
            prev_mouse_x = None
            prev_mouse_y = None


def cursor_position_callback(window, x, y):
    global simulator, mouse_down, prev_mouse_x, prev_mouse_y
    
    if x >= 0 and x < screen_dimx and y >= 0 and y < screen_dimy:
        worldx, worldy = translate_to_world_coords(x, y)
        
        if mouse_down:
            # Add smoke at mouse position
            simulator.add_smoke(worldx, worldy, 100.0, 10.0)
            
            # Add velocity based on mouse movement
            if prev_mouse_x is not None and prev_mouse_y is not None:
                dx = (x - prev_mouse_x) / screen_dimx
                dy = -(y - prev_mouse_y) / screen_dimy
                simulator.add_velocity(worldx, worldy, dx * 50.0, dy * 50.0)
            
            prev_mouse_x = x
            prev_mouse_y = y


# Initialize the library
if not glfw.init():
    exit()

# Create a windowed mode window and its OpenGL context
window = glfw.create_window(screen_dimx, screen_dimy, "Smoke Simulation", None, None)
if not window:
    glfw.terminate()
    exit()

# Make the window's context current
glfw.make_context_current(window)

# Set callbacks
glfw.set_mouse_button_callback(window, mouse_button_callback)
glfw.set_cursor_pos_callback(window, cursor_position_callback)

# Setup OpenGL
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glClearColor(0.0, 0.0, 0.0, 1.0)

gluOrtho2D(screen_leftx,
            screen_rightx,
            screen_bottomy,
            screen_topy)

# Main loop
frame_count = 0
while not glfw.window_should_close(window):
    # Add continuous smoke source at bottom center
    if frame_count % 3 == 0:
        simulator.add_smoke(0.5, 0.1, 50.0, 5.0)
    
    # Run simulation step
    smoke_main_loop()
    
    # Render
    display()
    
    # Swap front and back buffers
    glfw.swap_buffers(window)

    # Poll for and process events
    glfw.poll_events()
    
    frame_count += 1

# Terminate GLFW
glfw.terminate()