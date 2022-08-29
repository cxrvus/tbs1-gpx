import re
from os import listdir

GPXDIR = './testdata'

gpxFilePattern = r'^(?P<name>[a-z]{1,32})_(?P<polkz>[a-z]{1,3}-[a-z]{2}[- ]?P\d{1,4})_(?P<index>\d{3})\.gpx$'

files = listdir(GPXDIR)
fileMatches = map(lambda x: re.match(gpxFilePattern, x, flags=re.I), files)
validFileMatches = filter(lambda x: x, fileMatches)

print(str(list(files)))