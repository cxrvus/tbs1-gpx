const fs = require('fs');
const GPXDIR = './testdata'

const gpxFilePattern = /^(?<name>[a-z]{1,32})_(?<polkz>[a-z]{1,3}-[a-z]{2}[- ]?\d{1,4})_(?<index>\d{3})\.gpx$/i

const fileMatches = fs.readdirSync(GPXDIR)
	.map(x => x.match(gpxFilePattern))
	.filter(x => x)
	.map(x => x.groups)
;

console.log(fileMatches)
