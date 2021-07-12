
dir = "/Users/leninmookiah/Downloads/iCloudPhotos/"


# Python3 program to illustrate
# accessing of video metadata
# using tinytag library

# Import Tinytag method from
# tinytag library
from tinytag import TinyTag

# Pass the filename into the
# Tinytag.get() method and store
# the result in audio variable
video = TinyTag.get(dir+"1623479350992.MP4")

print(video)
# Use the attributes
# and display
print("Title:" + str(video.title))
print("Artist: " + str(video.artist))
print("Genre:" + str(video.genre))
print("Year Released: " + str(video.year))
print("Bitrate:" + str(video.bitrate) + " kBits/s")
print("Composer: " + video.composer)
print("Filesize: " + str(video.filesize) + " bytes")
print("AlbumArtist: " + str(video.albumartist))
print("Duration: " + str(video.duration) + " seconds")
print("TrackTotal: " + str(video.track_total))
print("TrackTotal: " + str(video.))
