import re
import os
import eyed3 as eye
from typing import Pattern

path = ""  # enter the path of your music files directory between the qutoes
path = path.replace("\\", "/")

filenamelist = os.listdir(path)

for file in filenamelist:
    x = re.search("([\w\W]*)(\s-\s)([\w\W]*)", file)
    if x:
        audiofile = eye.load(file)
        audiofile.tag.artist = x.group(1)
        audiofile.tag.save()
        print(audiofile.tag.artist)
        os.rename(file, x.group(3))
