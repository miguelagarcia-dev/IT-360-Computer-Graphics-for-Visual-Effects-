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
import random

try:
    from OpenGL.GLUT import *
    from OpenGL.GLUT import GLUT_BITMAP_TIMES_ROMAN_24
    from OpenGL.GL import *
    from OpenGL.GLU import *
except BaseException:
    print('''
ERROR: PyOpenGL not installed properly.
        ''')
    sys.exit()


# Screen setup - reused from rope.py/point.py
screen_dimx = 800
screen_dimy = 800
screen_leftx = 0
screen_rightx = 1
screen_topy = 0
screen_bottomy = 1
screen_world_width = screen_rightx - screen_leftx
screen_world_height = screen_bottomy - screen_topy

time_delta = 1 / 60.
mouse_down = False


# Simulation parameters - adjustable with keyboard
class SimParams:
    def __init__(self):
        # Default values
        self.default_fade_rate = 0.01
        self.default_growth_rate = 0.0002
        self.default_upward_vel_min = 0.3
        self.default_upward_vel_max = 0.5
        self.default_horizontal_drift = 0.05
        self.default_turbulence = 0.01
        self.default_vel_damping = 0.995
        self.default_spawn_rate = 0.3
        self.default_max_particles = 200
        self.default_mouse_particles = 3
        self.default_initial_size_min = 0.02
        self.default_initial_size_max = 0.04
        
        # Initialize to defaults
        self.reset()
    
    def reset(self):
        """Reset all parameters to default values"""
        self.fade_rate = self.default_fade_rate              # How fast smoke fades (Q/W)
        self.growth_rate = self.default_growth_rate          # How fast particles grow (A/S)
        self.upward_vel_min = self.default_upward_vel_min    # Min upward velocity (Z/X)
        self.upward_vel_max = self.default_upward_vel_max    # Max upward velocity (C/V)
        self.horizontal_drift = self.default_horizontal_drift # Horizontal drift range (E/R)
        self.turbulence = self.default_turbulence            # Random turbulence strength (D/F)
        self.vel_damping = self.default_vel_damping          # Velocity dampening (T/Y)
        self.spawn_rate = self.default_spawn_rate            # Auto-spawn probability (G/H)
        self.max_particles = self.default_max_particles      # Max particle count (U/I)
        self.mouse_particles = self.default_mouse_particles  # Particles per mouse click (J/K)
        self.initial_size_min = self.default_initial_size_min # Min initial size (N/M)
        self.initial_size_max = self.default_initial_size_max # Max initial size (,/.)

params = SimParams()


# Smoke particle class - simplified from Particle in rope.py
class SmokeParticle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-params.horizontal_drift, params.horizontal_drift)
        self.vy = random.uniform(params.upward_vel_min, params.upward_vel_max)
        self.life = 1.0                          # opacity/life
        self.size = random.uniform(params.initial_size_min, params.initial_size_max)
        self.age = 0.0


smoke_particles = []


# Drawing functions - adapted from point.py
def draw_smoke_particle(particle):
    """Draw a smoke particle as a semi-transparent circle"""
    x, y = particle.x, particle.y
    r = particle.size
    
    # Color: white smoke that fades
    alpha = particle.life
    glColor4f(0.9, 0.9, 0.9, alpha)
    
    i = 0.0
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    while i <= 360.0:
        glVertex2f(r * cos(PI * i / 180.0) + x,
                   r * sin(PI * i / 180.0) + y)
        i += 360.0 / 12.0  # fewer segments for speed
    glEnd()


def draw_smoke():
    """Draw all smoke particles"""
    for particle in smoke_particles:
        draw_smoke_particle(particle)


def draw_text(x, y, text):
    """Draw text at screen position"""
    glColor3f(0.0, 1.0, 0.0)  # Green text
    glRasterPos2f(x, y)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))


def draw_ui():
    """Draw UI showing current parameter values"""
    y = 0.95
    line_height = 0.05  # Increased for larger font
    
    draw_text(0.02, y, "CONTROLS - Press keys to adjust:")
    y -= line_height
    draw_text(0.02, y, f"Q/W: Fade Rate = {params.fade_rate:.4f}")
    y -= line_height
    draw_text(0.02, y, f"A/S: Growth Rate = {params.growth_rate:.5f}")
    y -= line_height
    draw_text(0.02, y, f"Z/X: Upward Vel Min = {params.upward_vel_min:.2f}")
    y -= line_height
    draw_text(0.02, y, f"C/V: Upward Vel Max = {params.upward_vel_max:.2f}")
    y -= line_height
    draw_text(0.02, y, f"E/R: Horiz Drift = {params.horizontal_drift:.3f}")
    y -= line_height
    draw_text(0.02, y, f"D/F: Turbulence = {params.turbulence:.4f}")
    y -= line_height
    draw_text(0.02, y, f"T/Y: Vel Damping = {params.vel_damping:.4f}")
    y -= line_height
    draw_text(0.02, y, f"G/H: Spawn Rate = {params.spawn_rate:.3f}")
    y -= line_height
    draw_text(0.02, y, f"U/I: Max Particles = {int(params.max_particles)}")
    y -= line_height
    draw_text(0.02, y, f"J/K: Mouse Particles = {int(params.mouse_particles)}")
    y -= line_height
    draw_text(0.02, y, f"N/M: Init Size Min = {params.initial_size_min:.3f}")
    y -= line_height
    draw_text(0.02, y, f",/.: Init Size Max = {params.initial_size_max:.3f}")
    y -= line_height * 1.5
    draw_text(0.02, y, f"Particles: {len(smoke_particles)}")
    y -= line_height
    draw_text(0.02, y, "Press SPACE to clear smoke")
    y -= line_height
    draw_text(0.02, y, "Press BACKSPACE to reset all parameters")


# Simplified simulation - no constraints needed!
def smoke_main_loop():
    global smoke_particles, params
    
    # Update each particle
    for particle in smoke_particles:
        # Apply slight wind/turbulence
        particle.vx += random.uniform(-params.turbulence, params.turbulence)
        
        # Move particle
        particle.x += particle.vx * time_delta
        particle.y += particle.vy * time_delta
        
        # Fade out over time
        particle.life -= params.fade_rate
        particle.age += time_delta
        
        # Grow slightly as it rises (smoke expands)
        particle.size += params.growth_rate
        
        # Slow down vertically over time
        particle.vy *= params.vel_damping
        particle.vx *= 0.99
    
    # Remove dead particles
    smoke_particles[:] = [p for p in smoke_particles if p.life > 0]
    
    # Add continuous smoke source at bottom
    if len(smoke_particles) < params.max_particles:
        if random.random() < params.spawn_rate:
            smoke_particles.append(SmokeParticle(0.5, 0.05))


def add_smoke_at(x, y):
    """Add smoke particles at mouse position"""
    for _ in range(int(params.mouse_particles)):
        smoke_particles.append(SmokeParticle(x, y))


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_smoke()
    draw_ui()
    glFlush()


# Mouse functions - adapted from rope.py/point.py
def translate_to_world_coords(screenx, screeny):
    x = screenx / screen_dimx
    y = 1.0 - screeny / screen_dimy
    return (x, y)


def mouse_button_callback(window, button, action, mods):
    global mouse_down
    if button == 0:  # Left mouse button
        if action == glfw.PRESS:
            mouse_down = True
        elif action == glfw.RELEASE:
            mouse_down = False


def cursor_position_callback(window, x, y):
    global mouse_down
    if x >= 0 and x < screen_dimx and y >= 0 and y < screen_dimy:
        if mouse_down:
            worldx, worldy = translate_to_world_coords(x, y)
            add_smoke_at(worldx, worldy)


def key_callback(window, key, scancode, action, mods):
    global smoke_particles, params
    
    if action == glfw.PRESS or action == glfw.REPEAT:
        # Fade rate (Q/W)
        if key == glfw.KEY_Q:
            params.fade_rate = max(0.001, params.fade_rate - 0.001)
        elif key == glfw.KEY_W:
            params.fade_rate = min(0.1, params.fade_rate + 0.001)
        
        # Growth rate (A/S)
        elif key == glfw.KEY_A:
            params.growth_rate = max(0.0, params.growth_rate - 0.0001)
        elif key == glfw.KEY_S:
            params.growth_rate = min(0.01, params.growth_rate + 0.0001)
        
        # Upward velocity min (Z/X)
        elif key == glfw.KEY_Z:
            params.upward_vel_min = max(0.0, params.upward_vel_min - 0.05)
        elif key == glfw.KEY_X:
            params.upward_vel_min = min(params.upward_vel_max, params.upward_vel_min + 0.05)
        
        # Upward velocity max (C/V)
        elif key == glfw.KEY_C:
            params.upward_vel_max = max(params.upward_vel_min, params.upward_vel_max - 0.05)
        elif key == glfw.KEY_V:
            params.upward_vel_max = min(2.0, params.upward_vel_max + 0.05)
        
        # Horizontal drift (E/R)
        elif key == glfw.KEY_E:
            params.horizontal_drift = max(0.0, params.horizontal_drift - 0.01)
        elif key == glfw.KEY_R:
            params.horizontal_drift = min(0.5, params.horizontal_drift + 0.01)
        
        # Turbulence (D/F)
        elif key == glfw.KEY_D:
            params.turbulence = max(0.0, params.turbulence - 0.001)
        elif key == glfw.KEY_F:
            params.turbulence = min(0.1, params.turbulence + 0.001)
        
        # Velocity damping (T/Y)
        elif key == glfw.KEY_T:
            params.vel_damping = max(0.9, params.vel_damping - 0.005)
        elif key == glfw.KEY_Y:
            params.vel_damping = min(0.999, params.vel_damping + 0.005)
        
        # Spawn rate (G/H)
        elif key == glfw.KEY_G:
            params.spawn_rate = max(0.0, params.spawn_rate - 0.05)
        elif key == glfw.KEY_H:
            params.spawn_rate = min(1.0, params.spawn_rate + 0.05)
        
        # Max particles (U/I)
        elif key == glfw.KEY_U:
            params.max_particles = max(10, params.max_particles - 10)
        elif key == glfw.KEY_I:
            params.max_particles = min(1000, params.max_particles + 10)
        
        # Mouse particles (J/K)
        elif key == glfw.KEY_J:
            params.mouse_particles = max(1, params.mouse_particles - 1)
        elif key == glfw.KEY_K:
            params.mouse_particles = min(20, params.mouse_particles + 1)
        
        # Initial size min (N/M)
        elif key == glfw.KEY_N:
            params.initial_size_min = max(0.005, params.initial_size_min - 0.005)
        elif key == glfw.KEY_M:
            params.initial_size_min = min(params.initial_size_max, params.initial_size_min + 0.005)
        
        # Initial size max (,/.)
        elif key == glfw.KEY_COMMA:
            params.initial_size_max = max(params.initial_size_min, params.initial_size_max - 0.005)
        elif key == glfw.KEY_PERIOD:
            params.initial_size_max = min(0.2, params.initial_size_max + 0.005)
        
        # Clear all smoke (SPACE)
        elif key == glfw.KEY_SPACE:
            smoke_particles = []
        
        # Reset all parameters (BACKSPACE)
        elif key == glfw.KEY_BACKSPACE:
            params.reset()


# Initialize GLUT for text rendering
glutInit(sys.argv)

# Initialize GLFW - same as rope.py/point.py
if not glfw.init():
    exit()

window = glfw.create_window(screen_dimx, screen_dimy, "Simple Smoke Simulation", None, None)
if not window:
    glfw.terminate()
    exit()

glfw.make_context_current(window)

# Set callbacks
glfw.set_mouse_button_callback(window, mouse_button_callback)
glfw.set_cursor_pos_callback(window, cursor_position_callback)
glfw.set_key_callback(window, key_callback)

# OpenGL setup with transparency
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glClearColor(0.0, 0.0, 0.0, 1.0)

gluOrtho2D(screen_leftx,
            screen_rightx,
            screen_bottomy,
            screen_topy)

# Main loop - same structure as rope.py/point.py
while not glfw.window_should_close(window):
    smoke_main_loop()
    display()
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()

