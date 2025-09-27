#a lib that parse srt files

#time format is hh:mm:ss,ms or hh:mm:ss.ms
def framesFromTime(time, fps) :
    time = time.replace(",", ".")
    time = time.split(".")
    tmp = time[0].split(":")
    h, m, s = float(tmp[0]), float(tmp[1]), float(tmp[2])
    ms = float(time[1])

    frames = s * fps + m * fps * 60 + h * fps * 60 * 60 + ms * fps / 1000.0
    return frames

class Subtitle : 
    def __init__(self, textblock, fps) : 
        self.fps = fps
        self.textblock = textblock
        self.index = -1
        self.start = -1
        self.end = -1
        self.text = ""
        self.parse()

    def parse(self) : 
        ls = self.textblock.split("\n")
        self.index = int(ls[0])
        lstime = ls[1].split(" --> ")
        self.start = framesFromTime(lstime[0], self.fps)
        self.end = framesFromTime(lstime[1], self.fps)
        self.text = "\n".join(ls[2:])

    def print(self) : 
        print(self.index)
        print(self.start)
        print(self.end)
        print(self.text)
        print("--")

def parse(srttext, fps=24) : 
    ls = srttext.split("\n\n")
    subtitles = []
    for l in ls : 
        if len(l) == 0 : 
            continue
        subtitles.append(Subtitle(l, fps))
    return subtitles
