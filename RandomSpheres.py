bl_info = {
    "name": "Custom addon",
    "author": "Tahiti",
    "version": (1, 0),
    "blender": (4, 3, 2),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Adds randomly placed spheres",
    "warning": "",
    "doc_url": "",
    "category": "",
}


import bpy
from random import randint
from bpy.types import (Panel, Operator)


class ButtonOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "random.1"
    bl_label = "Simple Random Operator"


    def execute(self, context):
        for i in range(500):
            randomScale = randint(0,3)
            x = randint(-40,40)
            y = randint(-40,40)
            z = randint(-40,40)
            bpy.ops.mesh.primitive_uv_sphere_add(radius=randomScale, enter_editmode=False, align='WORLD', location=(x, y, z))
            bpy.ops.object.shade_smooth()

        return {'FINISHED'}

class CustomPanel(bpy.types.Panel):
    bl_label = "Random Panel"
    bl_idname = "OBJECT_PT_random"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Random Spheres"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.operator(ButtonOperator.bl_idname, text="Generate", icon='MESH_UVSPHERE')

from bpy.utils import register_class, unregister_class

_classes = [
    ButtonOperator,
    CustomPanel
]


def register():
    for cls in _classes:
            register_class(cls)

def unregister():
    for cls in _classes:
            unregister_class(cls)


if __name__ == "__main__":
    register()
