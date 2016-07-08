import os, sys
from PIL import Image

directory = os.listdir(sys.argv[1])
size = (128,128)
with open(sys.argv[2], 'r+') as yaml_file:
	content = yaml_file.read()
	yaml_file.seek(0,0)

	album_title = str(sys.argv[1].split("/")[1:][0]) + ":\n"
	print album_title
	yaml_file.write(album_title)

	for infile in directory:
		if not infile.startswith("thumb"):
			photo = "- "+infile + "\n"
			yaml_file.write(photo)
		filename = os.path.join(sys.argv[1], infile)
		outfile = "thumb_" + infile
		thumb = os.path.join(sys.argv[1], outfile)
		if filename != thumb:
			im = Image.open(os.path.abspath(filename))
			im.thumbnail(size)
			im.save(thumb,"JPEG")

	yaml_file.write(content)


