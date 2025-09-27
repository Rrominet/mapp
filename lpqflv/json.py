import json
import base64

def dictToClass(cls, dictionary) : 
    inst = cls()
    for k in dictionary.keys() : 
        setattr(inst, k, dictionary[k])

    return inst

def jsonToClass (cls, jsonStr) : 
    dic = json.loads(jsonStr)
    return dictToClass(cls, dic)

def classToDict(inst) : 
    tmp = dir(inst)
    keys = []
    for k in tmp : 
        if "__" not in k and (type(getattr(inst, k)) == int or type(getattr(inst, k)) == float or type(getattr(inst, k)) == bool or type(getattr(inst, k)) == tuple or type(getattr(inst, k)) == list or type(getattr(inst, k)) == str) :
            keys.append(k)

    dic = {}
    for k in keys : 
        dic[k] = getattr(inst, k)

    return dic

# the key is the key for the mage data in the dict
def addImageData(pdict, key, imageData) : 
    pdict[key] = base64.b64encode(imageData).decode("utf-8")


def addImage(pdict, key, filepath) : 
    f = open(filepath, "rb")
    data = f.read()
    f.close()
    addImageData(pdict, key, data)
