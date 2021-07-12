#### arlo camera extract info

- ffprobe script to print json output format works. Example below.

        ffprobe -show_format -print_format json <filePath> >> output_append.json
        
- Print only file name from a folder    
    ls -1 *.MP4