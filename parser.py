import re
from os import listdir

def parse_all_file_names(dir):
	file_name_data = []
	file_names = listdir(dir)
	for file_name in file_names:
		file_name_data.append(_parse_file_name(file_name))
	return file_name_data

_gpx_file_pattern = re.compile(r'^(?P<name>[a-z]{1,32})_(?P<polkz>[a-z]{1,3}-?[a-z]{2}\d{1,4})_(?P<index>\d{3})\.gpx$', flags=re.I)

def _parse_file_name(fileName):
	match = _gpx_file_pattern.match(fileName)
	if match:
		return match.groupdict()
	else:
		raise Exception(f'invalid match at {fileName}')