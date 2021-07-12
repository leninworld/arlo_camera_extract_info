dir=/Users/leninmookiah/Downloads/iCloudPhotos/
# After running this, it produces .json file in the same folder as above.

echo $from_start
for filepath in $dir*
do
    filename=$(basename $filepath)
    fullpath=($dir$filename)
    if [ "$from_start" = "yes" ]; then
      ffprobe -show_format -print_format json $fullpath >> output_append.json
#      echo "ffprobe -show_format -print_format json $fullpath"  >> $fullpath.json
    else
      ffmpeg -i $fullpath -dump >> output.txt
      echo "------------------------------------------\n" > output.txt
    fi
done
