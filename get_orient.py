from itertools import zip_longest
import maya.cmds as mc

# Select root joint, then run 'select -hi', then run script
selection = mc.ls(sl=True,type="joint")

# Grab rotation attributes with getAttr
get_orientX = mc.getAttr(selection,".rotateX")
get_orientY = mc.getAttr(selection,".rotateY")
get_orientZ = mc.getAttr(selection,".rotateZ")

#Loop through each attribute based on selection
for sel, x, y, z in zip_longest(selection, get_orientX, get_orientY, get_orientZ):
    print(sel, x, y, z)
