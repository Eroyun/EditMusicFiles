import re
import os
import eyed3 as eye
from typing import Pattern

path = ""  # Write the path of the folder containing the music files between the quotation marks
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
