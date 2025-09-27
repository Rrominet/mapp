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

import sys 
import bpy

from lpqflv import bl_addons
from lpqflv_camerasManager import Pipeline



#globals # 
CM = None 
PIPE = None
PipelineTree = None
MCR = None
global EXISTING_SEQS
EXISTING_SEQS = []
icons = None

global PREVIOUS_PROJECTS
PREVIOUS_PROJECTS = []
ROOT = bl_addons.addonsPath() + "/lpqflv_camerasManager"
SAVE_PATH = ROOT + "/saves"
PREVIOUS_PROJECTS_FILE = SAVE_PATH + "/previousProjects"

def pipelineFile () : 
    return Pipeline.project() + "/lpqflv_pipeline"

panelDirs = []
