# -----------------------------------------------------------------------------
# Python, OpenGL & Scientific Visualization
# www.labri.fr/perso/nrougier/python+opengl
# Copyright (c) 2017, Nicolas P. Rougier
# Distributed under the 2-Clause BSD License.
# -----------------------------------------------------------------------------
from glumpy import app, gloo, gl

vertex = """
    uniform float theta;
    attribute vec4 color;
    attribute vec2 position;
    varying vec4 v_color;
    void main()
    {
        float ct = cos(theta);
        float st = sin(theta);
        float x = 0.65* (position.x*ct - position.y*st);
        float y = 0.65* (position.x*st + position.y*ct);
        gl_Position = vec4(x, y, 0.0, 1.0);
        v_color = color;
    } """


fragment = """
  varying vec4 v_color;
  void main()
  {
      gl_FragColor = v_color;
  } """

# Build the program and corresponding buffers (with 4 vertices)
quad = gloo.Program(vertex, fragment, count=4)

# Upload data into GPU
quad['color'] = [ (1,0,0,1), (0,1,0,1), (0,0,1,1), (1,1,0,1) ]
quad['position'] = [ (-1,-1),   (-1,+1),   (+1,-1),   (+1,+1)   ]
quad['theta'] = 0

# Create a window with a valid GL context
window = app.Window()

counter = 0

# Tell glumpy what needs to be done at each redraw
@window.event
def on_draw(dt):
    global counter
    window.clear()
    quad['theta'] += dt
    quad.draw(gl.GL_TRIANGLE_STRIP)
#     print(counter, dt, quad['theta'])
#     counter += 1

# Run the app
app.run()