from parser import parse_all_filenames
from gpxpy import parse
import json
# import db

GPXDIR = './testdata'
parsed_filenames = parse_all_filenames(GPXDIR)

def sync_tracks():
	tracks = []
	for i, fileinfo in enumerate(parsed_filenames):
		track = {
			'fahrer_name': fileinfo['name'],
			'fahrtzeug_polkz': fileinfo['polkz'],
			'points': []
		}

		with open(f"{GPXDIR}/{fileinfo['filename']}", 'r') as file:
			gpx_data = parse(file)
			track['start_time'] = gpx_data.time
			progress = f"{str(i+1).rjust(2,'0')} / {len(parsed_filenames)} - "

			if(len(gpx_data.tracks) > 0 and len(gpx_data.tracks[0].segments) > 0):
				points = gpx_data.tracks[0].segments[0].points
			else:
				print(progress + 'failiure - ' + fileinfo['filename'])
				continue

		for point in points:
			track['points'].append({
				'lat': point.latitude,
				'lon': point.longitude,
				'ele': point.elevation,
				'time': point.time
			})

		tracks.append(track)

	with open('static/tracks.json', 'w') as target_json:
		target_json.write(json.dumps(tracks, indent=4, sort_keys=True, default=str))

	print(progress + 'success')


sync_tracks()
exit()

"""
for fileinfo in parsed_filenames:
	db.amend_record('fahrer', 'name', fileinfo['name'])
	db.amend_record('fahrzeug', 'polkz', fileinfo['polkz'])
	# if not db.read_record('fahrt', 'dateiname', file['filename']):
	if not False:
		fid = db.amend_record('fahrer', 'name', fileinfo['name'])['fid']
		fzid = db.amend_record('fahrzeug', 'polkz', fileinfo['polkz'])['fzid']
		fahrt_record = {
			'fid': fid,
			'fzid': fzid,
			'dateiname': fileinfo['filename']
		}
		fahrt_record = db.create_record('fahrt', fahrt_record)
		fahrt_id = fahrt_record['ftid']
"""