import soundfile
import os

'''
This is a small script that will convert all the wav files 
in a directory (including subdirectories) to 16 bit depth.

Samples generally come in 8-bit, 16-bit, and 24-bit depth.

I'm using this script to easily import files for use in 
Little GP Tracker (LGPT), a sample player that only accepts
8 and 16 depth samples.
'''

tree_root = "/Volumes/RETROFW/apps/lgpt/samplelib"

for dirpath, dirnames, filenames in os.walk(tree_root):
    print(dirpath, dirnames, filenames)
    for index, name in enumerate(filenames):
        path = dirpath + "/" + name
        if name.split(".")[1].lower() in ["wav", "wave"]: # if wav file
            data, samplerate = soundfile.read(path)
            soundfile.write(path, data, samplerate, subtype="PCM_16")
