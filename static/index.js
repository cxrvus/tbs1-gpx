const drawTrack = track => {
    const coordinates = track.points.map(p => [p.lat.toFixed(5), p.lon.toFixed(5)]);
    const polyline = L.polyline(coordinates,
		{
			weight: 6,
			color: 'darkred'
		}
		).addTo(window.mymap);
    mymap.fitBounds(polyline.getBounds());
}

const init = () => {
	window.mymap = L.map('map');

	L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
		attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
		maxZoom: 50
	}).addTo(window.mymap);

	window.fahrtSelect = document.getElementById('fahrtSelect')
	listTracks()
}

const listTracks = () => { 
	fahrtSelect.innerHTML = '<option value="" selected disabled hidden>--- Bitte Fahrt auswählen ---</option>'
	
	tracks
		.map(track =>
			[
				track.fahrer_name,
				track.fahrtzeug_polkz,
				track.start_time && new Date(track.start_time).toLocaleDateString()
			]
			.join(' - ')
		)
		.forEach((summary,i) => {
			const option = document.createElement('option')
			option.value = i
			option.innerText = summary
			fahrtSelect.appendChild(option)
		})
	;
}

const renderPath = () => {
	const chosenTrack = tracks[parseInt(fahrtSelect.value)]
	drawTrack(chosenTrack)
}