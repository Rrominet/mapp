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

# -*-coding:utf-8 -*

def move_up(pList, index) : 
	"""return : Move up the item at the index 'index' in the list pList"""

	try : 
		pList[index-1], pList[index] = pList[index], pList[index-1]
		return pList
	except : 
		return pList

def move_dwn(pList, index) : 
	"""return : Move up the item at the index 'index' in the list pList"""

	try : 
		pList[index+1], pList[index] = pList[index], pList[index+1]
		return pList
	except : 
		return pList

#if index is out of range, it return the last element of the list
def get(ls, index) : 
    if len(ls) == 0 : return None
    if len(ls)<= index : 
        return ls[-1]
    return ls[index]
