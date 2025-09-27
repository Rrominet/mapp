import bpy
import os
from bpy.app.handlers import persistent
import json
from lpqflv import bl_sequencer as bs
from lpqflv_camerasManager import pipelineFiles

def shotsFromSelection() : 
    shots = []
    sl = bs.selected()
    for s in sl : 
        if s.mapp.type == "shot" : 
            shots.append(s)

    return shots

def seqsFromSelection() : 
    seqs = []
    sl = bs.selected()
    for s in sl : 
        if s.mapp.type == "seq" : 
            seqs.append(s)

    return seqs

#if shots are a list of strings, its works to
def scaleSeqFromShots(seq, shots) : 
    if not shots : 
        return

    gshots = []
    for s in shots :
        if type(s) == str : 
            s = bs.sequences_all()[s]
            gshots.append(s)
        else : 
            gshots.append(s)

    fs = gshots[0].frame_final_start
    fe = gshots[0].frame_final_end

    for s in gshots : 
        if s.frame_final_start < fs : 
            fs = s.frame_final_start
        if s.frame_final_end > fe : 
            fe = s.frame_final_end

    seq.frame_final_start = fs
    seq.frame_final_end = fe

#if shots are a list of strings, its works to
def setSeqChannelFromShots(seq, shots) : 
    if not shots : 
        return
    gshots = []
    for s in shots :
        if type(s) == str : 
            s = bs.sequences_all()[s]
            gshots.append(s)
        else : 
            gshots.append(s)
    ch = 1
    for s in gshots :
        if s.channel > ch : 
            ch = s.channel
    seq.channel = ch + 1

def children(seq) : 
    try : 
        chs = json.loads(seq.mapp.children)
        _r = []
        for c in chs : 
            if c in bs.sequences_all() : 
                _r.append(bs.sequences_all()[c])
        return _r
    except : return []

def updateSeq(seq) :
    setSeqChannelFromShots(seq, children(seq))
    scaleSeqFromShots(seq, children(seq))

@persistent
def updateAllSeqs(dum=None, dum2=None) :
    for s in allSeqs() : 
        updateSeq(s)

def removeShotFromSeq(seq, shot, updateUi=True) : 
    if (not seq) or (not shot) : 
        return
    if type(shot) == str : 
        shot = bs.sequences_all()[shot]
    if (type(seq) == str) : 
        seq = bs.sequences_all()[seq]
    shot.mapp.seq = ""
    chs = children(seq)

    if shot.name in chs : 
        chs.remove(shot.name)
        seq.mapp.children = json.dumps(chs)
        if updateUi : 
            scaleSeqFromShots(seq, chs)
            setSeqChannelFromShots(seq, chs)

def allShots() : 
    shots = []
    for s in bs.sequences_all() : 
        if s.mapp.type == "shot" : 
            shots.append(s)
    return shots

def shots() : 
    shots = []
    for s in bs.sequences() : 
        if s.mapp.type == "shot" : 
            shots.append(s)
    return shots

def allSeqs() :
    seqs = []
    for s in bs.sequences_all() : 
        if s.mapp.type == "seq" : 
            seqs.append(s)
    return seqs

def seqs() :
    seqs = []
    for s in bs.sequences() : 
        if s.mapp.type == "seq" : 
            seqs.append(s)
    return seqs

def removeShotFromAllSeq(shot) : 
    if (type(shot) == str) : 
        shot = bs.sequences_all()[shot]
    for s in allSeqs() : 
        removeShotFromSeq(s, shot)

def shotUnderTheCursor() : 
    shs = shots()
    keep = []
    for s in shs :
        if bs.isUnderTheCursor(s) : 
            keep.append(s)

    _r = None
    ch = 0
    for s in keep : 
        if s.channel > ch : 
            ch = s.channel
            _r = s
    return _r

def setStripTextFromProps(strip) : 
    if (strip.mapp.type == "shot" or strip.mapp.type == "none") : 
        return
     
    text = "seq_" + str(strip.mapp.seq_number) + "_" + strip.mapp.seq_name
    strip.text = text
    strip.name = text

    chs = json.loads(strip.mapp.children)
    for c in chs : 
        bs.sequences_all()[c].mapp.seq = text

def seq(s) : 
    if s.mapp.type == "none" : 
        raise Exception("The Strip is not a Shot/Seq")
    
    elif s.mapp.type == "shot" : 
        s = bs.sequences_all()[s.map.seq]

    return s

def cleanType(strip) :
    strip = seq(strip)
    scType = strip.mapp.seq_type.lower().replace(" ", "-").replace("/", "-")
    if scType == "animation" : 
        scType += "s"
        
    return scType 


def folderName(strip) : 
    strip = seq(strip)
    return "seq" + str(strip.mapp.seq_number) + "_" + strip.mapp.seq_name

def filename(strip) : 
    strip = seq(strip)

    return cleanType(strip) + "_" + strip.mapp.seq_name + "_seq" + str(strip.mapp.seq_number)

def filepath (strip) : 
    path = bpy.context.scene.projectPath + os.sep + cleanType(strip) + os.sep + folderName(strip)
    _r = pipelineFiles.lastIncrement(path, True)
    if _r == None : 
        _r = path + os.sep + filename(strip) + ".1.blend"
    return _r
