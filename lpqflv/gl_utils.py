# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import blf
import bgl
import bpy
import gpu
import gpu_extras.presets
import gpu_extras.batch
import mathutils
    
class Drawer : 
    
    # enum in [‘EMPTY’, ‘VIEW_3D’, ‘IMAGE_EDITOR’, ‘NODE_EDITOR’, ‘SEQUENCE_EDITOR’, ‘CLIP_EDITOR’, ‘DOPESHEET_EDITOR’, ‘GRAPH_EDITOR’, ‘NLA_EDITOR’, ‘TEXT_EDITOR’, ‘CONSOLE’, ‘INFO’, ‘TOPBAR’, ‘STATUSBAR’, ‘OUTLINER’, ‘PROPERTIES’, ‘FILE_BROWSER’, ‘PREFERENCES’], default 'EMPTY'
    _3D = "POST_VIEW"
    _2D = "POST_PIXEL"

    def __init__(self, drawFunc, args=(), space=None, type="POST_PIXEL") : 
        self.drawFunc = drawFunc
        self.args = args
        if not space : 
            self.space = bpy.context.area.spaces.active
        else : 
            self.space = space
        self.type = type
        self.region_type = "WINDOW"
        self.handler = None
        self.addHandler()
        
    def addHandler(self) : 
        if self.handler : 
            return 
        self.handler = self.space.draw_handler_add(self.drawFunc, 
                                                                  self.args, 
                                                                  self.region_type,
                                                                  self.type)
    def removeHandler(self) : 
        if not self.handler : 
            return 
        self.space.draw_handler_remove(self.handler, self.region_type)
        self.handler = None
            
    def toogleHandler(self) : 
        if self.handler : 
            self.removeHandler()
        elif not self.handler : 
            self.addHandler()

    def stop(self) : 
        self.removeHandler();

    def start(self) : 
        self.addHandler();

    def toggle(self) :
        self.toogleHandler();

class ImageBase : 
    quality = bgl.GL_LINEAR
    def __init__(self, path, coord=(5, 5), space=None) : 
        self._path = path
        self._coord = [coord[0], coord[1]]
        self._space = space
        self._w = 0;
        self._h = 0;
        self._rot = 0.0
        self._drawer = None
        self._image = None
        self._shader = None
        self._batch = None
        self._handler = None

        self.loaded = False
        self.startDrawer()

    def loadImg(self) : 
        if self.loaded : 
            return
        self._image = bpy.data.images.load(self._path, check_existing=True)
        self._image.gl_load()
        self._w = self._image.size[0]
        self._h = self._image.size[1]
        self.loaded = True

    def startDrawer(self) : 
        if self._drawer : 
            self._drawer.stop()
            self._drawer = None
        self.loadImg()

    def scale(self, w, h) : 
        self._w = w
        self._h = h

    def remove(self) : 
        self._drawer.stop()

class _2DImage(ImageBase) : 
    def __init__ (self, path, coord=[5, 5], space=None) : 
        ImageBase.__init__(self, path, coord, space)

    def setPosition(self, x, y) : 
        self._coord[0] = x
        self._coord[1] = y

    def move(self, x, y) : 
        self._coord[0] += x
        self._coord[1] += y
    
    def loadImg(self) : 
        super().loadImg()
        self._shader = gpu.shader.from_builtin("2D_IMAGE")

    def startDrawer(self) : 
        super().startDrawer()
        def handler() : 
            self._batch = gpu_extras.batch.batch_for_shader(
                self._shader, "TRI_FAN", 
                {
                    "pos": ((self._coord[0], self._coord[1]), (self._coord[0] + self._w, self._coord[1]), (self._coord[0] + self._w, self._coord[1] + self._h), (self._coord[0], self._coord[1] + self._h)),
                    "texCoord" : ((0, 0), (1, 0), (1 ,1), (0, 1)),
                })
            bgl.glEnable(bgl.GL_BLEND)
            bgl.glActiveTexture(bgl.GL_TEXTURE0)
            bgl.glBindTexture(bgl.GL_TEXTURE_2D, self._image.bindcode)

            bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MIN_FILTER, ImageBase.quality)
            bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MAG_FILTER, ImageBase.quality)

            self._shader.bind()
            self._shader.uniform_int("image", 0);
            self._batch.draw(self._shader)
            bgl.glDisable(bgl.GL_BLEND)
        self._drawer = Drawer(handler, (), self._space)
        self._drawer.start()

class _3DImage(ImageBase) : 
    def __init__(self, path, coord=[0, 0, 0], space=None) : 
        ImageBase.__init__(self, path, coord, space)
        self.parent = None
        self.parentInverseMatrix = None
        self._rot = (0.0, 0.0, 0.0)

    def loadImg(self) : 
        super().loadImg()
        self.setShader()

    def setPosition(self, x, y, z) : 
        self._coord[0] = xfrom 
        self._coord[1] = y
        self._coord[1] = z

    def move(self, x, y, z) : 
        self._coord[0] += x
        self._coord[1] += y
        self._coord[2] += z

    def startDrawer(self) : 
        super().startDrawer()
        c = self._coord
        self.setShader()
        def handler() : 
            data = None
            data = {
                        "pos" : self.transformMatrix(), # need to convert it to double
                        "texCoord" : ((0, 0), (1, 0), (1 ,1), (0, 1)),
                        }
            self._batch = gpu_extras.batch.batch_for_shader(
                self._shader, "TRI_FAN", data
                )
            bgl.glEnable(bgl.GL_DEPTH_TEST)
            bgl.glEnable(bgl.GL_BLEND)
            bgl.glActiveTexture(bgl.GL_TEXTURE0)
            bgl.glBindTexture(bgl.GL_TEXTURE_2D, self._image.bindcode)

            self._shader.bind()
            self._shader.uniform_int("image", 0);
            self._batch.draw(self._shader)
            bgl.glDisable(bgl.GL_BLEND)
            bgl.glDisable(bgl.GL_DEPTH_TEST)
        self._drawer = Drawer(handler, (), self._space, Drawer._3D)
        self._drawer.start()

    def transformMatrix(self) : 
        c = self._coord
        m_loc = mathutils.Matrix.Translation((c[0], c[1], c[2]))
        m_sca = mathutils.Matrix.Scale(1, 4, (self._w, self._h, 1.0))
        m_rot = mathutils.Matrix().to_3x3()
        m_rot.rotate(mathutils.Euler(self._rot))
        m_rot = m_rot.to_4x4()
        m = m_loc @ m_rot @ m_sca
        if self.parent : 
            m = m@self.parentInverseMatrix
        return m


    def setParent(self, blObject) : 
        #careful : could cause memory problem
        self.parent = blObject
        self.parentInverseMatrix = self.parent.matrix_world.inverted()

    def setShader(self) : 
        vs = ''' 
uniform mat4 ModelViewProjectionMatrix;

in mat4 pos;
in vec2 texCoord;
out vec2 texCoord_interp;

void main()
{
    gl_Position = ModelViewProjectionMatrix * pos * vec4(0.0f, 0.0f, 0.0f, 1.0f);
    texCoord_interp = texCoord;
}
        '''
        fs = '''
in vec2 texCoord_interp;
out vec4 fragColor;

uniform sampler2D image;

void main()
{
  fragColor = texture(image, texCoord_interp);
}
        '''
        self._shader = gpu.types.GPUShader(vs, fs)
