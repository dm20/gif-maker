import imageio
import os

path = '/Users/danielmcgrath/Desktop/Pics/'

image_folder = os.fsencode(path)

images = []

for file in os.listdir(image_folder):
	filename = os.fsdecode(file)
	if filename.endswith( ('.jpeg','.png') ):
        	images.append(imageio.imread(filename))

imageio.mimsave('/Users/danielmcgrath/Desktop/Pics/movie.gif', images)
