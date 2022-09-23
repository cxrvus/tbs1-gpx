from fileinput import filename
from parser import parse_all_filenames
import db

GPXDIR = './testdata'
parsed_filenames = parse_all_filenames(GPXDIR)
print(parsed_filenames)

for file in parsed_filenames:
	db.amend_record('fahrer', 'name', file['name'])
	db.amend_record('fahrzeug', 'polkz', file['polkz'])
	# if not db.read_record('fahrt', 'dateiname', file['filename']):
	if not False:
		fid = db.amend_record('fahrer', 'name', file['name'])['fid']
		fzid = db.amend_record('fahrzeug', 'polkz', file['polkz'])['fzid']
		fahrt_record = {
			'fid': fid,
			'fzid': fzid,
			'dateiname': file['filename']
		}
		fahrt_record = db.create_record('fahrt', fahrt_record)
		fahrt_id = fahrt_record['ftid']