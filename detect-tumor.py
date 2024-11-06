import cv2 as cv
import os
from contrast import contrast


tumor_ratio = 0.45 #the higher the number, the less sensetive the program. Range: 0-1


folder = "src_path/" #add source folder here, ending in backslash
filelist = os.listdir(folder)
for filename in filelist:
    if filename.endswith("png") or filename.endswith("jpg") or filename.endswith("jpeg"):  
        contrast_filename = contrast(folder+filename, 1.7, folder+"contrastBrain/"+filename)
        img= cv.imread(contrast_filename,  cv.IMREAD_GRAYSCALE)
        h,w = img.shape[:2]
        wmult = int(w/8)
        hmult = int(h/5)
        pieces = []
        for i in range(5):
            for j in range(8):
                pieces.append((i, j, (img[i*hmult:(i+1)*hmult ,j*wmult:(j+1)* wmult])))
        for piece in pieces:
            wcnt = 0
            bcnt = 0
            for i in range(piece[2].shape[0]):
                for j in range(piece[2].shape[1]):
                    if piece[2][i][j]>220:
                        wcnt+=1
                    else:
                        bcnt+=1
            if wcnt/bcnt>tumor_ratio:
               for x in range(wmult):
                   for y in range(hmult):
                        img[piece[0]*hmult:(piece[0]+1)*hmult, piece[1]*wmult:piece[1]*wmult+5]=0
                        img[piece[0]*hmult:piece[0]*hmult+5 ,piece[1]*wmult:(piece[1]+1)*wmult] = 0
                        img[piece[0]*hmult:(piece[0]+1)*hmult ,(piece[1]+1)*wmult:(piece[1]+1)*wmult+5] = 0
                        img[(piece[0]+1)*hmult:(piece[0]+1)*hmult+5 ,(piece[1])*wmult:(piece[1]+1)*wmult+5] = 0
        cv.imwrite("folder_path/"+filename, img) #add target folder path here. followed by backslash
               

