```python
import pyglet
from pywavefront import visualization, Wavefront

class Avatar3D:
    def __init__(self, obj_path, texture_path):
        self.obj = Wavefront(obj_path)
        self.texture = pyglet.image.load(texture_path).get_texture()

    def draw(self):
        pyglet.gl.glEnable(pyglet.gl.GL_TEXTURE_2D)
        pyglet.gl.glBindTexture(pyglet.gl.GL_TEXTURE_2D, self.texture.id)
        visualization.draw(self.obj)

class AvatarWindow(pyglet.window.Window):
    def __init__(self, avatar, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.avatar = avatar

    def on_draw(self):
        self.clear()
        self.avatar.draw()

def create_avatar(obj_path, texture_path):
    avatar = Avatar3D(obj_path, texture_path)
    window = AvatarWindow(avatar, width=800, height=600, caption='3D Avatar')
    pyglet.app.run()

# Example usage:
# create_avatar('path_to_obj_file.obj', 'path_to_texture_file.png')
```