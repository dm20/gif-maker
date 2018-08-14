import imageio
import os

path = '/Users/danielmcgrath/Desktop/Pics/' # on Mac: right click on a folder, hold down option, and click "copy as pathname"

image_folder = os.fsencode(path)

images = []

for file in os.listdir(image_folder):
	filename = os.fsdecode(file)
	if filename.endswith( ('.jpeg','.png') ):
        	images.append(imageio.imread(filename))

imageio.mimsave(os.path.join('movie.gif', images)
