import glfw
from OpenGL.GL import *
import math

circles = [
    {'x': -1.5, 'y': -1.0, 'radius': 1.0},
    {'x': 1.5, 'y': 1.0, 'radius': 1.0}
]

dragged_circle = None

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

def window_to_gl_coords(window, mx, my):
    width, height = glfw.get_window_size(window)
    glx = (mx / width) * 8.0 - 4.0
    gly = 3.0 - (my / height) * 6.0
    return glx, gly

def is_point_in_circle(px, py, circle):
    distance_squared = (px - circle['x']) ** 2 + (py - circle['y']) ** 2
    return distance_squared <= circle['radius'] ** 2

# Callback for mouse button events
def mouse_button_callback(window, button, action, mods):
    global dragged_circle
    
    if button == glfw.MOUSE_BUTTON_LEFT:
        if action == glfw.PRESS:
            mx, my = glfw.get_cursor_pos(window)
            glx, gly = window_to_gl_coords(window, mx, my)
            
            for i, circle in enumerate(circles):
                if is_point_in_circle(glx, gly, circle):
                    dragged_circle = i
                    break
        elif action == glfw.RELEASE:
            dragged_circle = None

# Callback for cursor position
def cursor_position_callback(window, xpos, ypos):
    global dragged_circle
    
    if dragged_circle is not None:
        glx, gly = window_to_gl_coords(window, xpos, ypos)
        circles[dragged_circle]['x'] = glx
        circles[dragged_circle]['y'] = gly

# Callback for keyboard events
def key_callback(window, key, scancode, action, mods):
    if action == glfw.PRESS:
        if key == glfw.KEY_ESCAPE:
            glfw.set_window_should_close(window, True)

# Initialize the library
if not glfw.init():
    exit()

# Create a windowed mode window and its OpenGL context
window = glfw.create_window(640, 480, "Draggable Circles", None, None)
if not window:
    glfw.terminate()
    exit()

# Make the window's context current
glfw.make_context_current(window)

# Set callbacks
glfw.set_key_callback(window, key_callback)
glfw.set_mouse_button_callback(window, mouse_button_callback)
glfw.set_cursor_pos_callback(window, cursor_position_callback)

# Camera settings
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(-4.0, 4.0, -3.0, 3.0, -1.0, 1.0)
glMatrixMode(GL_MODELVIEW)

# Main loop
while not glfw.window_should_close(window):
    glClearColor(0.870, 0.905, 0.937, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    for circle in circles:
        glColor3f(0.807, 0.0, 0.0)
        draw_filled_circle(circle['x'], circle['y'], circle['radius'])
        glColor3f(0.0, 0.0, 0.0)
        glLineWidth(2.0)
        draw_circle_outline(circle['x'], circle['y'], circle['radius'])

    # Swap front and back buffers
    glfw.swap_buffers(window)

    # Poll for and process events
    glfw.poll_events()

# Terminate GLFW
glfw.terminate()