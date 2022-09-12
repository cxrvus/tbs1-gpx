from parser import parse_all_file_names
import db

GPXDIR = './testdata'
parsed_file_names = parse_all_file_names(GPXDIR)

for file in parsed_file_names:
	db.amend_record('fahrer', 'name', file['name'])
	db.amend_record('fahrzeig', 'polkz', file['polkz'])