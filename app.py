import re
import os
import eyed3 as eye
from typing import Pattern

# Write the path of the folder containing the music files between the quotation marks
path = ""
path = path.replace("\\", "/")
if path[-1] != "/":
    path += "/"
filenamelist = os.listdir(path)

for file in filenamelist:
    x = re.search(r"([\w\W]*)(\s-\s)([\w\W]*)", file)
    if x:
        path2 = os.path.join(path, file)
        audiofile = eye.load(path2)
        audiofile.tag.artist = x.group(1)
        audiofile.tag.save()
        print(audiofile.tag.artist)
        os.rename(path2, os.path.join(path, x.group(3)))
