import re
from os import listdir

def parseAllFileNames(dir):
	fileNameData = []
	fileNames = listdir(dir)
	for fileName in fileNames:
		fileNameData.append(_parseFileName(fileName))
	return fileNameData

_gpxFilePattern = re.compile(r'^(?P<name>[a-z]{1,32})_(?P<polkz>[a-z]{1,3}-?[a-z]{2}\d{1,4})_(?P<index>\d{3})\.gpx$', flags=re.I)

def _parseFileName(fileName):
	match = _gpxFilePattern.match(fileName)
	if match:
		return match.groupdict()
	else:
		raise Exception(f'invalid match at {fileName}')