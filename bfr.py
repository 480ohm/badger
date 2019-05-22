import os
import exifread

# image_types could also take into account .jpeg/.JPEG but it would require file_extension to be something like
# file_extension = current_file[-4:] and then read if file_extention[0] == '.'

image_types = ["jpg", "JPG", "nef", "NEF", "dng", "DNG"]

current_file = "DSC_1399.NEF"

file_extension = current_file[-3:]

# the block below needs to be broken up into functions or modules, it's getting a bit convoluted

with os.scandir(path=".") as files:
    for f in files:
        if f.is_dir() is False:
            file_extension = f.name[-3:]

            if file_extension in image_types:
                print(f.name)
                with open(f.name, 'rb') as image_file:
	                tags = exifread.process_file(image_file)

                for tag in tags:
                    # could this next if block be taken out? probs not really relevant for my use
                    if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename',
                        'EXIF MakerNote'):
                        if tag == "Image DateTimeOriginal":
                            print("Key: %s, value %s" % (tag, tags[tag]))

                            # store value of Image DateTimeOriginal in a variable for processing
                            # remove time from variable, break up remainder into DD MM YYYY
                            # rename image file to YYYY-MM-YY-00000.EXTENSION
