#!/usr/bin/env bash
set -e # halt script on error

if brew ls --versions exiftool > /dev/null; then
  echo "Exiftool Installed"
else
  echo "Installing Exiftool"
  brew install exiftool
fi

if brew ls --versions imagemagick > /dev/null; then
  echo "Image Magick Installed"
else
  echo "Installing Image Magick"
  brew install imagemagick
fi


#=================================#
# Generate Publication Thumbnails #
#=================================#

for pdf in `ls publications/*.pdf`; do
    p="`basename ${pdf}`"
    if [ ! -f publications/thumb_${p/pdf/png} ]; then
        echo "Generating thumbnail for ${p}"
        magick convert -density 300 -resize 150 ${pdf}[0] publications/thumb_${p/pdf/png}
    fi;
done;

#===============================#
# Fetch Publication Information #
#===============================#

echo "Fetching publication information"
python scripts/fetch_pubs.py

#========#
# Albums #
#========#

# Generate album pages
IFS=$(echo -en "\n\b")
echo "Generating albums"
for i in `ls -1 -d people/albums/*/`; do
    echo ${i};
    name="`basename ${i}`"
    fname=`echo $name | awk '{print tolower($0) ".md"}'`
    echo """---
album: ${name:11}
layout: gallery
category: album
menu: people
--- """ > _posts/photo_albums/${fname}
done;

# Generate image thumbnails
for img in `ls people/albums/*/* | grep -v 'thumb' | grep -v '.DS' `; do
    output_name="`basename ${img}`"
    directory="`dirname ${img}`"
    # Generate thumbnail
    if [ ! -f ${directory}/thumb_${output_name} ]; then
        echo "Generating Thumbnail [${img}]"
        magick convert -auto-orient -thumbnail 200 ${img} ${directory}/thumb_${output_name}
    fi
    # Resize if the image is really big
    image_width=`exiftool -s3 -ImageWidth ${img}`
    echo "${image_width} --> OK [${img}]"
    if [ ${image_width} -gt 1200 ]; then
        # Downsizing image
        echo "${image_width} --> 1200 [${img}]"
        magick convert -auto-orient -resize 1200 "${img}" "${img}_tmp"
        mv "${img}_tmp" "${img}"
    fi
done;
