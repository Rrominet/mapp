import bpy
import os

#if frame is -1, it will take the current frame
def availableChannel(frame=-1) : 
    if frame == -1 :
        frame = bpy.context.scene.frame_current

    r_channel = 1
    channels = []
    for seq in sequences() : 
        if frameIn(seq, frame) :
            channels.append(seq.channel)
        
    while r_channel in channels : 
        r_channel += 1
        
    return r_channel

# return True if the frame is between frame_final_start and frame_final_end
def frameIn(strip, frame) : 
    if not strip : 
        return False

    return (frame >= strip.frame_final_start) and (frame < strip.frame_final_end)

def sequences() : 
    if not bpy.context.scene.sequence_editor : 
        bpy.context.scene.sequence_editor_create()
    return bpy.context.scene.sequence_editor.sequences

def sequences_all() : 
    if not bpy.context.scene.sequence_editor : 
        bpy.context.scene.sequence_editor_create()
    return bpy.context.scene.sequence_editor.sequences_all

def sequencesFromPath(path, type="MOVIE") : 
    seqs = []
    for seq in sequences_all() : 
        if seq.type == type and type == "MOVIE" : 
            if seq.filepath == path or bpy.path.abspath(seq.filepath) == path : 
                seqs.append(seq)
        elif seq.type == type and type == "SOUND" : 
            if seq.sound.filepath == path or bpy.path.abspath(seq.sound.filepath) == path : 
                seqs.append(seq)
    return seqs

#if deep, it will take in to account the selection in the Meta Sequences
def selected(deep=False) : 
    selected = []
    seqs = []
    if deep : 
        seqs = sequences_all()
    else : 
        seqs = sequences()
    for seq in seqs : 
        if seq.select : 
            selected.append(seq)

    return selected

def unselectAll() : 
    for s in sequences() : 
        s.select = False

def active() : 
    if not bpy.context.scene.sequence_editor : 
        return None
    return bpy.context.scene.sequence_editor.active_strip

def setActive(seq) :
    if not bpy.context.scene.sequence_editor : 
        raise Exception("Sequence editor is not created")
    bpy.context.scene.sequence_editor.active_strip = seq

def selectAll() : 
    for s in sequences() : 
        s.select = True
        s.select_left_handle = False
        s.select_right_handle = False

def deselecteAll() : 
    for s in sequences_all() : 
        s.select = False
        s.select_left_handle = False
        s.select_right_handle = False

def erase(path, _in, _out, sound=False) : 
    print("Erase " + path)
    print("in frame : " + str(_in))
    print("out frame : " + str(_out))
    sequencer = bpy.context.scene.sequence_editor
    if not sound : 
        seq = sequencer.sequences.new_movie(
                name=path.split(os.sep)[-1], 
                filepath = path, 
                channel=2, 
                frame_start=bpy.context.scene.frame_current
                )
    seq2 = sequencer.sequences.new_sound(
            name=path.split(os.sep)[-1], 
            filepath = path, 
            channel=1, 
            frame_start=bpy.context.scene.frame_current
            )
    if not sound : 
        seqs = (seq, seq2)
    else : 
        seqs = (seq2, )
    for s in seqs : 
        s.frame_offset_start = _in
        s.frame_offset_end = s.frame_duration - _out
        s.frame_start = -_in + bpy.context.scene.frame_current
        if s.type == "MOVIE" : 
            ratio = bpy.context.scene.render.resolution_x/s.elements[0].orig_width
            s.transform.scale_x = ratio
            s.transform.scale_y = ratio

    bpy.context.scene.frame_current = seqs[0].frame_final_end

def setStartNEndFromSelectedStripes() : 
    selection = selected()
    if len(selection) == 0 : 
        selection = sequences()

    setStartNEndFromStripes(selection)

def setStartNEndFromStripes(stripes) : 
    if (len(stripes) == 0) : 
        return
    minFrame = stripes[0].frame_final_start
    maxFrame = stripes[0].frame_final_end

    for seq in stripes : 
        if seq.frame_final_start < minFrame : 
            minFrame = seq.frame_final_start 

        if seq.frame_final_end > maxFrame : 
            maxFrame = seq.frame_final_end 

    bpy.context.scene.frame_start = minFrame
    bpy.context.scene.frame_end = maxFrame - 1

def mute(stripes=[], mute=True) : 
    if (len(stripes) == 0) : 
        stripes = selected()

    for s in stripes : 
        s.mute = mute

def unmute(stripes=[]) : 
    mute(stripes, False)

def isUnderTheCursor(strip) : 
    return (bpy.context.scene.frame_current >= strip.frame_final_start) and (bpy.context.scene.frame_current < strip.frame_final_end)

def serialized(seq) : 
    data = {}
    data["blend_alpha"] = seq.blend_alpha
    data["blend_type"] = seq.blend_type
    data["channel"] = seq.channel
    data["color_tag"] = seq.color_tag
    data["effect_fader"] = seq.effect_fader
    data["frame_duration"] = seq.frame_duration
    data["frame_final_duration"] = seq.frame_final_duration
    data["frame_final_end"] = seq.frame_final_end
    data["frame_final_start"] = seq.frame_final_start
    data["frame_offset_end"] = seq.frame_offset_end
    data["frame_offset_start"] = seq.frame_offset_start
    data["frame_start"] = seq.frame_start
    data["lock"] = seq.lock
    data["mute"] = seq.mute
    data["name"] = seq.name
    data["override_cache_settings"] = seq.override_cache_settings
    data["show_retiming_keys"] = seq.show_retiming_keys
    data["use_cache_composite"] = seq.use_cache_composite
    data["use_cache_preprocessed"] = seq.use_cache_preprocessed
    data["use_cache_raw"] = seq.use_cache_raw
    data["use_default_fade"] = seq.use_default_fade
    data["use_linear_modifiers"] = seq.use_linear_modifiers
    data["type"] = seq.type

    if seq.type == "IMAGE" : 
        data = serializedImageSequence(seq, data)

    elif seq.type == "MOVIE" : 
        data = serializedMovieSequence(seq, data)

    elif seq.type == "SOUND" : 
        data = serializedSoundSequence(seq, data)

    elif seq.type == "MOVIECLIP" : 
        data = serializedMovieClipSequence(seq, data)

    #need to do the other types likes the metas, effects, and modifiers applied to the strips.

    return data

def serializedEffectSequence(seq, data) : 
    #TODO
    return data

def serializedImageSequence(seq, data) : 
    data["alpha_mode"] = seq.alpha_mode
    data["animation_offset_end"] = seq.animation_offset_end
    data["animation_offset_start"] = seq.animation_offset_start
    data["color_multiply"] = seq.color_multiply
    data["color_saturation"] = seq.color_saturation
    data["directory"] = seq.directory
    data["multiply_alpha"] = seq.multiply_alpha
    data["strobe"] = seq.strobe
    data["use_deinterlace"] = seq.use_deinterlace
    data["use_flip_x"] = seq.use_flip_x
    data["use_flip_y"] = seq.use_flip_y
    data["use_float"] = seq.use_float
    data["use_multiview"] = seq.use_multiview
    data["use_proxy"] = seq.use_proxy
    data["use_reverse_frames"] = seq.use_reverse_frames

    data["elements"] = []
    for el in seq.elements :
        datael = {}
        datael["filename"] = el.filename
        datael["orig_fps"] = el.orig_fps
        data["elements"].append(datael)

    return data

def serializedMovieClipSequence(seq, data) : 
    data["alpha_mode"] = seq.alpha_mode
    data["animation_offset_end"] = seq.animation_offset_end
    data["animation_offset_start"] = seq.animation_offset_start
    data["color_multiply"] = seq.color_multiply
    data["color_saturation"] = seq.color_saturation
    data["fps"] = seq.fps
    data["multiply_alpha"] = seq.multiply_alpha
    data["stabilize2d"] = seq.stabilize2d
    data["strobe"] = seq.strobe
    data["undistort"] = seq.undistort
    data["use_deinterlace"] = seq.use_deinterlace
    data["use_flip_x"] = seq.use_flip_x
    data["use_flip_y"] = seq.use_flip_y
    data["use_float"] = seq.use_float
    data["use_reverse_frames"] = seq.use_reverse_frames
    return data

def serializedMovieSequence(seq, data) : 
    data["alpha_mode"] = seq.alpha_mode
    data["animation_offset_end"] = seq.animation_offset_end
    data["animation_offset_start"] = seq.animation_offset_start
    data["color_multiply"] = seq.color_multiply
    data["color_saturation"] = seq.color_saturation
    data["filepath"] = seq.filepath
    data["fps"] = seq.fps
    data["multiply_alpha"] = seq.multiply_alpha
    data["stream_index"] = seq.stream_index
    data["strobe"] = seq.strobe
    data["use_deinterlace"] = seq.use_deinterlace
    data["use_flip_x"] = seq.use_flip_x
    data["use_flip_y"] = seq.use_flip_y
    data["use_float"] = seq.use_float
    data["use_multiview"] = seq.use_multiview
    data["use_proxy"] = seq.use_proxy
    data["use_reverse_frames"] = seq.use_reverse_frames

    data["elements"] = []
    for el in seq.elements :
        datael = {}
        datael["filename"] = el.filename
        datael["orig_fps"] = el.orig_fps
        data["elements"].append(datael)

    return data

def serializedSoundSequence(seq, data) : 
    data["animation_offset_end"] = seq.animation_offset_end
    data["animation_offset_start"] = seq.animation_offset_start
    data["pan"] = seq.pan
    data["show_waveform"] = seq.show_waveform
    data["volume"] = seq.volume

    data["sound"] = {}
    data["sound"]["channels"] = seq.sound.channels
    data["sound"]["filepath"] = seq.sound.filepath
    data["sound"]["samplerate"] = seq.sound.samplerate
    data["sound"]["use_memory_cache"] = seq.sound.use_memory_cache
    data["sound"]["use_mono"] = seq.sound.use_mono

    return data

def deserialized(data) : 
    seq = None
    if data["type"] == "IMAGE" : 
        seq = bpy.context.scene.sequence_editor.sequences.new_image(data["name"], data["directory"] + os.sep + data["elements"][0]["filename"], data["channel"], int(data["frame_start"]))
    elif data["type"] == "MOVIE" : 
        seq = bpy.context.scene.sequence_editor.sequences.new_movie(data["name"], data["filepath"], data["channel"], int(data["frame_start"]))
    elif data["type"] == "SOUND" : 
        seq = bpy.context.scene.sequence_editor.sequences.new_sound(data["name"], data["sound"]["filepath"], data["channel"], int(data["frame_start"]))
    if seq == None : 
        print ("Sequence type " + data["type"] + " deserialized is not implemented yet.")
        return
    seq.blend_alpha=data["blend_alpha"]
    seq.blend_type=data["blend_type"]
    seq.channel=data["channel"]
    seq.color_tag=data["color_tag"]
    seq.effect_fader=data["effect_fader"]
    try : 
        seq.frame_duration=data["frame_duration"]
    except : pass
    try : 
        seq.frame_final_duration=data["frame_final_duration"]
    except : pass
    try : 
        seq.frame_final_end=data["frame_final_end"]
    except : pass
    try : 
        seq.frame_final_start=data["frame_final_start"]
    except : pass
    try : 
        seq.frame_offset_end=data["frame_offset_end"]
    except : pass
    try : 
        seq.frame_offset_start=data["frame_offset_start"]
    except : pass
    try : 
        seq.frame_start=data["frame_start"]
    except : pass
    seq.lock=data["lock"]
    seq.mute=data["mute"]
    seq.name=data["name"]
    seq.override_cache_settings=data["override_cache_settings"]
    seq.show_retiming_keys=data["show_retiming_keys"]
    seq.use_cache_composite=data["use_cache_composite"]
    seq.use_cache_preprocessed=data["use_cache_preprocessed"]
    seq.use_cache_raw=data["use_cache_raw"]
    seq.use_default_fade=data["use_default_fade"]
    seq.use_linear_modifiers=data["use_linear_modifiers"]

    if data["type"] == "IMAGE" : 
        data = serializedImageSequence(seq, data)

    elif data["type"] == "MOVIE" : 
        data = serializedMovieSequence(seq, data)

    elif data["type"] == "SOUND" : 
        data = serializedSoundSequence(seq, data)

    elif data["type"] == "MOVIECLIP" : 
        data = serializedMovieClipSequence(seq, data)

    return seq

def deserializeImageSequence(seq, data) : 
    seq.alpha_mode=data["alpha_mode"]
    seq.animation_offset_end=data["animation_offset_end"]
    seq.animation_offset_start=data["animation_offset_start"]
    seq.color_multiply=data["color_multiply"]
    seq.color_saturation=data["color_saturation"]
    seq.directory=data["directory"]
    seq.multiply_alpha=data["multiply_alpha"]
    seq.strobe=data["strobe"]
    seq.use_deinterlace=data["use_deinterlace"]
    seq.use_flip_x=data["use_flip_x"]
    seq.use_flip_y=data["use_flip_y"]
    seq.use_float=data["use_float"]
    seq.use_multiview=data["use_multiview"]
    seq.use_proxy=data["use_proxy"]
    seq.use_reverse_frames=data["use_reverse_frames"]

    for el in data["elements"] :
        seq.elements.append(ImageSequenceElement(el["filename"]))

def deserializeMovieClipSequence(seq, data) : 
    seq.alpha_mode=data["alpha_mode"]
    seq.animation_offset_end=data["animation_offset_end"]
    seq.animation_offset_start=data["animation_offset_start"]
    seq.color_multiply=data["color_multiply"]
    seq.color_saturation=data["color_saturation"]
    seq.fps=data["fps"]
    seq.multiply_alpha=data["multiply_alpha"]
    seq.stabilize2d=data["stabilize2d"]
    seq.strobe=data["strobe"]
    seq.undistort=data["undistort"]
    seq.use_deinterlace=data["use_deinterlace"]
    seq.use_flip_x=data["use_flip_x"]
    seq.use_flip_y=data["use_flip_y"]
    seq.use_float=data["use_float"]
    seq.use_reverse_frames=data["use_reverse_frames"]

def deserializeMovieSequence(seq, data) : 
    seq.alpha_mode=data["alpha_mode"]
    seq.animation_offset_end=data["animation_offset_end"]
    seq.animation_offset_start=data["animation_offset_start"]
    seq.color_multiply=data["color_multiply"]
    seq.color_saturation=data["color_saturation"]
    seq.filepath=data["filepath"]
    seq.fps=data["fps"]
    seq.multiply_alpha=data["multiply_alpha"]
    seq.stream_index=data["stream_index"]
    seq.strobe=data["strobe"]
    seq.use_deinterlace=data["use_deinterlace"]
    seq.use_flip_x=data["use_flip_x"]
    seq.use_flip_y=data["use_flip_y"]
    seq.use_float=data["use_float"]
    seq.use_multiview=data["use_multiview"]
    seq.use_proxy=data["use_proxy"]
    seq.use_reverse_frames=data["use_reverse_frames"]

def deserializeSoundSequence(seq, data) : 
    seq.animation_offset_end=data["animation_offset_end"]
    seq.animation_offset_start=data["animation_offset_start"]
    seq.pan=data["pan"]
    seq.show_waveform=data["show_waveform"]
    seq.volume=data["volume"]

    seq.sound.channels=data["sound"]["channels"]
    seq.sound.filepath=data["sound"]["filepath"]
    seq.sound.samplerate=data["sound"]["samplerate"]
    seq.sound.use_memory_cache=data["sound"]["use_memory_cache"]
    seq.sound.use_mono=data["sound"]["use_mono"]
