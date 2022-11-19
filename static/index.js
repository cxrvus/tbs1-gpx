const init = () => {
	listTracks()
}

const listTracks = () => { 
	const fahrtSelect = document.getElementById('fahrtSelect')
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
			option.value = `track_${i}`
			option.innerText = summary
			fahrtSelect.appendChild(option)
		})
	;
}

const renderPath = () => {
	alert('Path wird gerendert ya seleme')
}