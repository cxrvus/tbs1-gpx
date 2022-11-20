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
			'start_time': None,
			'points': []
		}

		with open(f"{GPXDIR}/{fileinfo['filename']}", 'r') as file:
			gpx_data = parse(file)
			track['start_time'] = gpx_data.time
			progress = f"{str(i+1).rjust(2,'0')} / {len(parsed_filenames)} - "

			if(len(gpx_data.tracks) > 0 and len(gpx_data.tracks[0].segments) > 0):
				points = gpx_data.tracks[0].segments[0].points
				if(not track['start_time']):
					track['start_time'] = points[0].time
			else:
				print(f"{progress}failiure - {fileinfo['filename']}")
				points = []
				continue

		for point in points:
			track['points'].append({
				'lat': point.latitude,
				'lon': point.longitude,
				'ele': point.elevation,
				'time': point.time
			})

		tracks.append(track)
		print(f"{progress}success - {len(points)} points parsed")

	with open('static/tracks.js', 'w') as target_json:
		json_tracks = json.dumps(tracks, indent=4, sort_keys=True, default=str)
		json_script = f"const tracks = {json_tracks}"
		target_json.write(json_script)

sync_tracks()
