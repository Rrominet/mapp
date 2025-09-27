import os
import bpy

def execFile(filepath) : 
    exec(compile(open(filepath).read(), filepath, 'exec'))

def execString(s, src="<string>") : 
    exec(compile(s, src, 'exec'))

def execDirContent(dirpath) : 
    for file in os.listdir(dirpath) : 
        if file.endswith(".py") : 
            execFile(dirpath + os.sep + file)


trackedFiles = {}
def trackupdate(filepath) : 
    def on_timer() : 
        try : 
            if filepath not in trackedFiles :
                trackedFiles[filepath] = os.stat(filepath).st_size
                execFile(filepath)
            else : 
                if os.stat(filepath).st_size != trackedFiles[filepath] :
                    trackedFiles[filepath] = os.stat(filepath).st_size
                    execFile(filepath)
        except Exception as e : 
            print ("Error during execution of the py file : " + filepath)
            print (type(e))
            print (e)
            print ("--")
        return 1.0

    bpy.app.timers.register(on_timer, first_interval=1.0)
