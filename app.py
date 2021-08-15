import re
import os
import eyed3 as eye

# Write the path of the folder containing the music files between the quotation marks
PATH = ""
PATH = PATH.replace("\\", "/")
if PATH[-1] != "/":
    PATH += "/"
filenamelist = os.listdir(PATH)

for file in filenamelist:
    x = re.search(r"([\w\W]*)(\s-\s)([\w\W]*)", file)
    if x:
        PATH2 = os.path.join(PATH, file)
        audiofile = eye.load(PATH2)
        audiofile.tag.artist = x.group(1)
        audiofile.tag.save()
        print(audiofile.tag.artist)
        os.rename(PATH2, os.path.join(PATH, x.group(3)))
