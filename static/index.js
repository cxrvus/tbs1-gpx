const init = () => {
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
	console.log(chosenTrack)
}