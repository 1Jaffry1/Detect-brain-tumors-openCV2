from PIL import Image


def val(R,G,B):
    return int(R*0.299+ G*0.587+ B*0.114)

def index(i, j):
    return i*width+j

filename = None

def set_all(filepath):
    global filename
    if filename!=filepath:
        with Image.open(filepath) as image:
            global gvals, matrix, height, width
            height = image.height
            width = image.width
            pixels = image.load()
            gvals = []
            matrix = []
            for i in range(width):
                for j in range(height):
                    try:
                        R = pixels[i,j][0]
                        G = pixels[i,j][1]
                        B = pixels[i,j][2]
                    except:
                        R=G=B = pixels[i,j]    
                        
                    gvals.append(val(R,G,B))
                    matrix.append((R,G,B))
        filename=filepath
    return gvals, matrix, height, width

def main():
    pass

if __name__=="__main__":
    main()