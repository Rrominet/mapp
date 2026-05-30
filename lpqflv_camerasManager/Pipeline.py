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

from lpqflv_camerasManager import config as cfg
from lpqflv_camerasManager import PipelineNodeTree as pnt

import bpy
import os 
import shutil
import sys

class Pipeline : 
    def __init__(self, projectPath="", sceneContent="", sceneType="", characterType="modeling", seq = 0) : 
        
        if projectPath == "" : 
            return
        
        self.projectPath = projectPath.replace("\\","/")
        if self.projectPath[-1] == "/" : 
            self.projectPath = self.projectPath[:-1]
            
        self.sceneContent = sceneContent.replace("_", "-")
        self.sceneType = sceneType
        self.seq = seq
        
        if seq == 0 : 
            self.isAnimation = False 
        else :
            self.isAnimation = True
        
        self.characterType = characterType

    
    def createFolders(self, pFolderName, create=True) : #creer les dossier qu'il faut
        scenePath = self.projectPath + "/" + pFolderName
        if os.path.isdir(self.projectPath + "/" + pFolderName)==False : #si le dossier n'existe pas, le creer 
            if create : os.mkdir(scenePath)
        
        # Gestion des dossiers 'modeling' et 'rig' si on travaille un perso
        
        if (pFolderName == "characters") and (self.characterType=="modeling"): 
            
            scenePath += "/modeling"
            if os.path.isdir(scenePath) == False : 
                if create : os.mkdir(scenePath)
            
        elif (pFolderName == "characters") and (self.characterType=="rig") : 
            
            scenePath += "/rig"
            if os.path.isdir(scenePath) == False :
                if create : os.mkdir(scenePath)
                
        # END modeling et RIG # 
        
        #Gestion NOm de l'objet si asset ou char #
        
        if pFolderName=="assets" or pFolderName=="characters" : 
            scenePath+= "/" + self.sceneContent
            
            if os.path.isdir(scenePath) == False : 
                if create : os.mkdir(scenePath)
        
        ## GESTION DE L'ANIMATION ## 
        
        if (self.isAnimation) : 
            
            scenePath += "/seq" + str(self.seq) + "_" + self.sceneContent
            self.sceneContent += "_seq" + str(self.seq)
            
            if os.path.isdir(scenePath) == False :
                if create : os.mkdir(scenePath)
                
        return scenePath

    #### SAVE SCENE #####
    
    def saveIncrementScene (self) : 
        if bpy.context.scene.reloadGlobalLibraries == True : 
            try : 
                bpy.ops.libraries.relocate_refs()
            except : 
                pass
        
        # creation du dossier correspondant au type de scene # 
        path = self.createFolders(self.sceneType)

        sceneName = self.sceneType + "_" + self.sceneContent + "."
        # print ("scene name : " + sceneName)

        #print ('FOLDER PATH : ' + path)
        
        fileList = os.listdir(path)
        
        #print (fileList)
        
        try : 
        
            currentSceneNameList = bpy.data.filepath.split("\\")
            currentSceneName = ""
            
            if len(currentSceneNameList) == 1 : 
                currentSceneNameList = bpy.data.filepath.split("/")
                currentSceneName = currentSceneNameList[len(currentSceneNameList) -1 ]
            else :
                currentSceneName = currentSceneNameList[len(currentSceneNameList) -1 ]
        except : 
            currentSceneName = ""
        
        
        ### INCREMENTATION ###
        if currentSceneName in fileList : 
            
            i=0
            while currentSceneName in fileList : 
                
                fileNumberList = fileList[i].split(".")
                
                fileNumber = fileNumberList[len(fileNumberList) -2]
                
                #print ("File number : " + str(fileNumber))
                
                try : 
                    fileNumber = int(fileNumber) 
                except : 
                    fileNumber = i
                
                
                ## RENOMMER LE NOM DE LA SCENE EN FONCTION DES AUTRES SCENES DANS LE DOSSIER, ## 
                currentSceneName = self.sceneType + "_" + self.sceneContent + "." + str(fileNumber + 1) + ".blend"
                i += 1

            # SAVE THE SCENE # 
            sceneName = currentSceneName
            bpy.ops.wm.save_as_mainfile(filepath=path + "/" + sceneName)
            scenePath = filepath=path + "/" + sceneName

            Pipeline.onSceneTypeChange ("", bpy.context)

            return scenePath
        
        else : 
            
            # print ("scene name 2 : " + sceneName)

            scenePath = filepath=path + "/" + sceneName + "1.blend"
            bpy.ops.wm.save_as_mainfile(filepath = scenePath) # save the Scene
            Pipeline.onSceneTypeChange ("", bpy.context)

            return scenePath
        
    def getScenePath(self) : 
        # creation du dossier correspondant au type de scene # 
        path = self.createFolders(self.sceneType, False)
        return path   

    ### END SAVE SCENE ###
            
    def saveMasterScene (self) : 
        bpy.ops.wm.save_as_mainfile()
        if bpy.context.scene.reloadGlobalLibraries == True : 
            try : 
                bpy.ops.libraries.relocate_refs()
            except : 
                pass
        
        sceneName = self.sceneType + "_" + self.sceneContent
        sceneName = self.masterName(sceneName)
        path = self.createFolders(self.sceneType)
        masterPath = path + os.sep + sceneName
        if os.path.exists(masterPath):
            os.remove(masterPath)
        shutil.copy(bpy.data.filepath, masterPath)
        self.copyMasterToSmartLinks(path, sceneName)
        self.makePoto(masterPath) # make the photo
        Pipeline.onSceneTypeChange ("", bpy.context)
        return masterPath


    def masterName(self, sceneName, dotBlend=True) : 
        if self.isAnimation : 
            sceneName += "_seq" + str(self.seq)
        sceneName += ".MASTER"
        if dotBlend : 
            sceneName += ".blend"

        return sceneName

    def smartLinks (self, pdir) : 
        r = []
        for f in os.listdir(pdir) : 
            if ".MASTER_smart-link" in f : 
                r.append(pdir + os.sep + f)
        return r

    def copyMasterToSmartLinks(self, pdir, masterName) : 
        for s in self.smartLinks(pdir) : 
            os.remove(s)
            os.symlink(pdir + os.sep + masterName, s)
        
    def makePoto (self, pScenePath) : 
        ##Render OpenGL##
        
        ## Save the variables ##
        
        defaultRenderOutput = bpy.context.scene.render.filepath
        defaultWidth = bpy.context.scene.render.resolution_x
        defaultHeight = bpy.context.scene.render.resolution_y
        defaultPourcentage = bpy.context.scene.render.resolution_percentage
        defaultFormat = bpy.context.scene.render.image_settings.file_format

        
        ### END VARIABLES ###
        
        ### FILE_NEW PARAMETERS ###
        
        imgPath = pScenePath.replace (".blend", "")
        imgPath += "_img"
        if bpy.context.scene.render.use_file_extension == False : 
            imgPath += ".jpg"
        
        bpy.context.scene.render.image_settings.file_format = "JPEG"
        bpy.context.scene.render.filepath = imgPath
        bpy.context.scene.render.resolution_x = 200
        bpy.context.scene.render.resolution_y = 200
        bpy.context.scene.render.resolution_percentage = 100
        
        ### END PARAMETERS ###
        
        ## RENDER OPEN GL ##
        is3DView = False
        for a in bpy.context.screen.areas : 
            if a.type == "VIEW_3D" : 
                is3DView = True 
                break
            
        currentType = bpy.context.area.type
        if not is3DView : 
            bpy.context.area.type = "VIEW_3D"
            bpy.ops.render.opengl(write_still = True, view_context = True)
            bpy.context.area.type = currentType
        
        else : 
            bpy.ops.render.opengl(write_still = True, view_context = True)

        ## RESET VARIABLES ##
        
        bpy.context.scene.render.filepath = defaultRenderOutput
        bpy.context.scene.render.resolution_x = defaultWidth
        bpy.context.scene.render.resolution_y = defaultHeight
        bpy.context.scene.render.resolution_percentage = defaultPourcentage
        bpy.context.scene.render.image_settings.file_format = defaultFormat
        
    @staticmethod    
    def setExistingSeqs (self, context) : 
        cfg.EXISTING_SEQS = []
        
        dir = bpy.context.scene.projectPath + "/" + bpy.context.scene.sceneType
        if (os.path.exists(dir)) : 
            dirs = os.listdir(dir)
            
            i = 0
            for d in dirs : 
                cfg.EXISTING_SEQS.append ((d,d,d,"",i))
                i+=1
                
                bpy.types.Scene.existingScenes = bpy.props.EnumProperty(items=cfg.EXISTING_SEQS,  name="Existing strips")
                
        else : 
            bpy.types.Scene.existingScenes = bpy.props.EnumProperty(items=cfg.EXISTING_SEQS,  name="Existing strips")

        ## DONE ##
        
        ## set previous projects ## 
        Pipeline.writePreviousProjects(context)
        Pipeline.readPreviousProjects()

    @staticmethod
    def readPreviousProjects () : 
        cfg.PREVIOUS_PROJECTS = []

        #read the file
        
        path = cfg.PREVIOUS_PROJECTS_FILE
        
        if os.path.isfile(path) : 
        
            previousFile = open (path, 'r')
            projectsStr = previousFile.read() 
            projectsList = projectsStr.split (";;")
            projectsList.reverse()
            projectsList = projectsList[:9]
            
            for p in projectsList : 
                cfg.PREVIOUS_PROJECTS.append ((p, p, p))
            
            bpy.types.Scene.previousProject = bpy.props.EnumProperty(items=cfg.PREVIOUS_PROJECTS,
  name="Previous projects ", update=Pipeline.onPreviousProjectChange)
  
            previousFile.close()
            
        else : 
            print ("File project does not exists - ")
            print ("path : " + cfg.PREVIOUS_PROJECTS_FILE)
            return
            
    @staticmethod
    def writePreviousProjects (context) : 
        path = cfg.PREVIOUS_PROJECTS_FILE
        
        str = ""
        
        if os.path.isfile(path) : 
            previousFileR = open (path, 'r')
            str = previousFileR.read()
            previousFileR.close()

        projectPath = context.scene.projectPath
        
        if projectPath in str : 
            return
        
        previousFile = open (path, 'a')
        previousFile.write (context.scene.projectPath + ";;")
        previousFile.close()
        
    @staticmethod
    def onSceneTypeChange (self, context) : 
        if context.scene.sceneType == "characters" or context.scene.sceneType == "assets" : 
            context.scene.seq = 0
        else : 

            if context.scene.seq == 0 : 
                context.scene.seq = 1
            Pipeline.setExistingSeqs(self, context)
            
    @staticmethod
    def onPreviousProjectChange(self, context) : 
        context.scene.projectPath = context.scene.previousProject

    @staticmethod
    def duplicate(newName) : 
        bpy.ops.wm.save_as_mainfile()
        if bpy.context.scene.reloadGlobalLibraries == True : 
            try : 
                bpy.ops.libraries.relocate_refs()
            except : 
                pass

        bpy.context.scene.sceneContent = newName
        bpy.ops.lpqflv_pipeline.save_increment()

def project(path = "") : 
    if path == "" : 
        path = bpy.context.scene.projectPath
    _r = path.replace("\\","/")
    if _r[-1] == "/" : 
        _r = _r[:-1]
    return _r
        
def trash() : 
    sc = bpy.context.scene
    _trash = sc.projectPath + "__trash__"
        
    if not os.path.isdir(_trash) : 
        os.mkdir(_trash)
        
    return _trash
