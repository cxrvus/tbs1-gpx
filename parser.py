import re
from os import listdir
from gpxpy import parse as parse_gpx

def parse_file(filename):
	with open(filename, 'r') as file:
		gpx = parse_gpx(file)
		points = gpx.get_points_data()
		return gpx

def parse_all_filenames(dir):
	filename_data = []
	filenames = listdir(dir)
	for filename in filenames:
		parsed_filename = _parse_filename(filename)
		parsed_filename['filename'] = filename
		filename_data.append(parsed_filename)
	return filename_data

_gpx_file_pattern = re.compile(r'^(?P<name>[a-z]{1,32})_(?P<polkz>[a-z]{1,3}-?[a-z]{2}\d{1,4})_(?P<index>\d{3})\.gpx$', flags=re.I)

def _parse_filename(fileName):
	match = _gpx_file_pattern.match(fileName)
	if match:
		return match.groupdict()
	else:
		raise Exception(f'invalid match at {fileName}')