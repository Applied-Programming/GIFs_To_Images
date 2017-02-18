from PIL import Image
import glob
import os,sys,shutil

def processImage(infile):
    try:
        im = Image.open(infile)
    except IOError:
        print "Cant load", infile
        sys.exit(1)
    i = 0
    mypalette = im.getpalette()

    try:
        while 1:
            im.putpalette(mypalette)
            new_im = Image.new("RGBA", im.size)
            new_im.paste(im)
            infilename = os.path.splitext(infile)[0]
            new_im.save('Converted_gifs/' +  infilename+str(i)+'.jpg')
            #new_im.save(infilename +str(i)+'.jpg')
            print 'Saved : ' + infilename + str(i)+'.jpg'
            i += 1
            im.seek(im.tell() + 1)

    except EOFError:
        pass # end of sequence

for single_gif in glob.glob('*.gif'):
    print single_gif
    processImage(single_gif)
    #shutil.move(single_gif,'Converted_gifs/'+single_gif)
