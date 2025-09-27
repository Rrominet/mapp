import bpy

class UIList(bpy.types.UIList):
    def drawItem(self, context, layout, item) : 
        pass

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        self.drawItem(context, layout, item)

def draw(clsname, layout, bl_prop_collection_parent, bl_prop_collection_name, activeIdxPropName) : 
    bl_prop_collection = getattr(bl_prop_collection_parent, bl_prop_collection_name)

    layout.template_list(clsname, "", bl_prop_collection_parent, bl_prop_collection_name, bl_prop_collection_parent, activeIdxPropName)
