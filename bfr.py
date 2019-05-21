import exifread

with open('DSC_1399.NEF', 'rb') as image_file:
	tags = exifread.process_file(image_file)

for tag in tags:
    if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
        print("Key: %s, value %s" % (tag, tags[tag]))
