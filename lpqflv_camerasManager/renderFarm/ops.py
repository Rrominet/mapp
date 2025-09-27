import bpy 
from lpqflv import bl_ops
from lpqflv_camerasManager.renderFarm.RenderFarm import Computer
from lpqflv_camerasManager.renderFarm.RenderFarm import Camera
from lpqflv_camerasManager import config as cf

class AddComputer (bl_ops.Operator) : 
    bl_idname = "lpqflv_render_farm.add_new_computer"
    bl_label = "Add/Modify a Computer"
    bl_description = "Add/Modify/Remove a new computer for the render"

    name : bpy.props.StringProperty(name="Name")
    ip : bpy.props.StringProperty(name="IP")
    power : bpy.props.IntProperty(name="Power", min=1, max=100, default=10)
    master : bpy.props.BoolProperty(name="Master", description="If the computer is the Master, the frames will be rendered on his HDD")
    action : bpy.props.IntProperty(default=1)

    CREATE = 1
    MODIFY = 2
    REMOVE = 3

    def __init__(self) : 
        self.computer = None

    def overInvoke(self, ctx, e) : 
        if self.action == AddComputer.MODIFY : 
            self.computer = cf.MCR.renderFarm.computerFromIp(self.ip)
            self.name = self.computer.name
            self.ip = self.computer.ip 
            self.power = self.computer.power
            self.master = self.computer.master
        elif self.action == AddComputer.REMOVE : 
            cf.MCR.renderFarm.removeComputer(cf.MCR.renderFarm.computerFromIp(self.ip))

    @classmethod
    def poll(cls, ctx) : 
        return True

    def draw(self, ctx) : 
        l = self.layout 
        if self.action == AddComputer.REMOVE : 
            l.label(text="Computer removed.")
        else : 
            c = l.column() 
            c.prop(self, "name")
            c.prop(self, "ip")
            c.prop(self, "power", slider=True)
            c.prop(self, "master")

    def execute(self, ctx) : 
        if (self.action == AddComputer.CREATE) : 
            c = Computer(self.name, self.ip, self.power, self.master) 
            cf.MCR.renderFarm.computers.append(c)
        elif self.action == AddComputer.MODIFY : 
            self.computer.name = self.name
            self.computer.ip = self.ip 
            self.computer.power = self.power
            self.computer.master = self.master
        return {'FINISHED'}

def AddCamera_update(self, ctx) : 
    camera = None
    find = bpy.data.objects.find(self.name)
    if find != -1 : 
        camera = bpy.data.objects[find]
    else : 
        return

    if camera.type != "CAMERA" : 
        self.name = ""
        return

    self.start = camera.data.cm.start
    self.end = camera.data.cm.end

class AddCamera (bl_ops.Operator) : 
    bl_idname = "lpqflv_render_farm.add_new_camera"
    bl_label = "Add Camera"
    bl_description = "Add a new Camera to render"

    computerIp : bpy.props.StringProperty(name="IP")
    name : bpy.props.StringProperty(name="Name", description="Camera name (from object) to render", update=AddCamera_update)
    start : bpy.props.IntProperty(name="Start Frame")
    end : bpy.props.IntProperty(name="End Frame")

    @classmethod
    def poll(cls, ctx) : 
        return True 

    def draw(self, ctx) : 
        l = self.layout
        l.prop_search(self, "name", bpy.data, "objects")
        l.prop(self, "start")
        l.prop(self, "end")

    def execute(self, ctx) : 
        c = cf.MCR.renderFarm.computerFromIp(self.computerIp)
        c.files[0].cameras.append(Camera(self.name, self.start, self.end))
        return {'FINISHED'}

class UpdateCamerasFromFile (bl_ops.Operator) : 
    bl_idname = "lpqflv_render_farm.update_cameras_from_file"
    bl_label = "Update"
    bl_description = "Create the cameras to render from the current file"

    def execute(self, ctx) : 
        cf.MCR.renderFarm.createCamerasFromScene()
        return {'FINISHED'}

class LaunchRender (bl_ops.Operator) : 
    bl_idname = "lpqflv_render_farm.launch_render"
    bl_label = "Launch"
    bl_description = "Launch the Render on all the computers"

    @classmethod
    def poll(cls, ctx) : 
        return True

    def execute(self, ctx) : 
        cf.MCR.renderFarm.startRender()
        return {'FINISHED'}


cls = (AddComputer, AddCamera, UpdateCamerasFromFile, LaunchRender)

register, unregister = bpy.utils.register_classes_factory(cls)
