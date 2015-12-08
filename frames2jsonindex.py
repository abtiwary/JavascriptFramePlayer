import os
import sys
import json

from glob import glob

frames_dict = {}

lstpngs = glob("*.png")
print lstpngs

for i, pngfl in enumerate(lstpngs):
    frames_dict[i] = pngfl

print frames_dict

with open("frames_index.json", "w+") as fjson:
    json.dump(frames_dict, fjson)

print

