#!/usr/bin/env bash
set -e # halt script on error

# Generate album pages
IFS=$(echo -en "\n\b")
for i in `ls -1 -d people/albums/*/`; do
    echo ${i};
    name="`basename ${i}`"
    fname="`echo $name | awk '{print tolower($0) ".md"}'`"
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
        convert -thumbnail 200 ${img} ${directory}/thumb_${output_name}
    fi
    # Resize if the image is really big
    image_width=`exiftool -s3 -ImageWidth ${img}`

    if [ ${image_width} -gt 1200 ]; then
        # Downsizing image
        echo "${image_width} --> 1200 [${img}]"
        convert -resize 1200 "${img}" "${img}_tmp"
        mv "${img}_tmp" "${img}"
    fi
done;
