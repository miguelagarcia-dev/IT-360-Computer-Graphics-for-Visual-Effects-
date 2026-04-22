import glfw
from OpenGL.GL import *
import math

def draw_filled_circle(cx, cy, r, segments=100):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(cx, cy)  
    for i in range(segments + 1):
        angle = 2.0 * math.pi * i / segments
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        glVertex2f(x, y)
    glEnd()

def draw_circle_outline(cx, cy, r, segments=100):
    glBegin(GL_LINE_LOOP)
    for i in range(segments):
        angle = 2.0 * math.pi * i / segments
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        glVertex2f(x, y)
    glEnd()

# Callback for keyboard events
def key_callback(window, key, scancode, action, mods):
    if action == glfw.PRESS:
        if key == glfw.KEY_ESCAPE:
            glfw.set_window_should_close(window, True)

# Initialize the library
if not glfw.init():
    exit()

# Create a windowed mode window and its OpenGL context
window = glfw.create_window(640, 480, "Red Circles", None, None)
if not window:
    glfw.terminate()
    exit()

# Make the window's context current
glfw.make_context_current(window)

# Set callbacks
glfw.set_key_callback(window, key_callback)

# Camera settings
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(-4.0, 4.0, -3.0, 3.0, -1.0, 1.0)
glMatrixMode(GL_MODELVIEW)

# Main loop
while not glfw.window_should_close(window):
    glClearColor(0.870, 0.905, 0.937, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0.807, 0.0, 0.0)
    draw_filled_circle(-1.5, -1.0, 1.0)
    glColor3f(0.0, 0.0, 0.0)
    glLineWidth(2.0)
    draw_circle_outline(-1.5, -1.0, 1.0)
    
    glColor3f(0.807, 0.0, 0.0)
    draw_filled_circle(1.5, 1.0, 1.0)
    glColor3f(0.0, 0.0, 0.0)
    glLineWidth(2.0)
    draw_circle_outline(1.5, 1.0, 1.0)

    # Swap front and back buffers
    glfw.swap_buffers(window)

    # Poll for and process events
    glfw.poll_events()

# Terminate GLFW
glfw.terminate()