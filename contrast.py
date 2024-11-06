from setup import set_all, val
import numpy as np
from PIL import Image


def contrast(filepath, factor, target ,RGB=0):
    gvals, matrix, height, width = set_all(filepath)
    median = np.median(gvals)
    img = Image.open(filepath)
    RGBimg = Image.open(filepath)
    pixels = img.load()
    coloredpixels = RGBimg.load()
    for i in range(width):
        for j in range(height):
            for k in range(3):
                if RGB>1:
                    coloredpixels[i,j] = (int(median + factor*(coloredpixels[i,j][0]-median)),
                                      int(median + factor*(coloredpixels[i,j][1]-median)),
                                      int(median + factor*(coloredpixels[i,j][2]-median)))
            try:
                v = int(median + factor*(val(*pixels[i,j])-median))
                pixels[i,j] =(v,v,v)
            except:
                v = int(median+factor*(pixels[i,j]-median))
                pixels[i,j] = v
    if RGB!=1:
        img.save(target)
    if RGB!=0:
        newname = target.split(".")
        RGBimg.save(newname[0]+"-RGB."+newname[1])
    return target
    