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

import bpy

def newCollection (name, parent = None) : 
	col = bpy.data.collections.new(name)
	if parent == None : 
		bpy.context.scene.collection.children.link(col)
		return col

	else : 
		parent.children.link(col)
		return col

def moveObjToCollection (object, collection) : 
	""" remove object from other collections """
	for col in object.users_collection : 
		col.objects.unlink(object)
	collection.objects.link(object)

def moveCollectionToCollection (collectionToMove, parent) : 
	for c in bpy.data.collections : 
		if c.children.find(collectionToMove.name) != -1 : 
			c.children.unlink(collectionToMove)

	parent.children.link(collectionToMove)

def contains(container, searchedName) : 
    res = False
    for c in container.children : 
        if c.name == searchedName : 
            res = True
            return res 
        else : 
            res = contains(c, searchedName)
    return res

def deepChildren(blObject) : 
    children = []
    for o in bpy.context.scene.objects : 
        if o.parent == blObject : 
            children.append(o)
            children += deepChildren(o)

    return children

#parent is a collection
def createIfItDoesNotExists(name, parent=None) : 
    for c in bpy.data.collections : 
        if c.name == name or c.name_full == name : 
            return c

    nc = bpy.data.collections.new(name)
    if not parent : 
        parent = bpy.context.scene.collection
    parent.children.link(nc)
    return nc

def visibleCollections(layerCollection) : 
    r = []
    if not layerCollection.exclude : 
        r.append(layerCollection)
    for c in layerCollection.children : 
        if not c.exclude : 
            r.append(c)
        r += visibleCollections(c)
    return r

def hiddenCollections(layerCollection) : 
    r = []
    if layerCollection.exclude : 
        r.append(layerCollection)
    for c in layerCollection.children : 
        if c.exclude : 
            r.append(c)
        r += hiddenCollections(c)
    return r

def hideCollections(layerCollection, names) : 
    for c in visibleCollections(layerCollection) : 
        if c.name in names : 
            c.exclude = True
