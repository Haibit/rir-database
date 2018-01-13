"""
Name: Multichannel Acoustic Reverberation Database at York (MARDY) Database

Website: http://www.commsp.ee.ic.ac.uk/~sap/resources/mardy-multichannel-acoustic-reverberation-database-at-york-database/

License: ?

Paper: Jimi YC Wen, Nikolay D Gaubitch, Emanuël AP Habets, Tony Myatt, and Patrick A Naylor. "Evaluation of speech dereverberation algorithms using the MARDY database", 2006
"""

import glob
import os
import re
import util

Positions = {
	'L': 'left',
	'C': 'center',
	'R': 'right',
}

def importRirs(downloadDir, insertIntoDbF):
	url = 'http://www.commsp.ee.ic.ac.uk/~sap/uploads/data/MARDY.rar'
	filename = os.path.join(downloadDir, 'mardy.rar')
	unpackDir = os.path.join(downloadDir, 'mardy')
	
	dl = util.FileDownloader(url, filename)
	dl.download()
	dl.unpackTo(unpackDir)

	fileSelector = os.path.join(unpackDir, '*.wav')
	files = list(glob.glob(fileSelector))

	bar = util.ConsoleProgressBar()
	bar.start('Import MARDY')
	for i, file in enumerate(sorted(files)): # we sort to get same identifiers cross-platform
		filename = os.path.basename(file)
		m = re.search(r'ir_(\d)_([LCR])_(\d).wav', filename)
		assert m, 'Could not parse rir info from filename {}'.format(filename)
		assert m.group(2) in Positions, 'invalid position {}'.format(m.groups(2))
		distanceInMeter = int(m.group(1))
		position = Positions[m.group(2)]
		microphoneIndexInArray = int(m.group(3))
		if microphoneIndexInArray == 4:
			identifier = '{:04d}_{}_{}'.format(i, distanceInMeter, position[0])
			insertIntoDbF(file, identifier, {
				'source': 'MARDY',
				'distanceInMeter': distanceInMeter,
				'position': position,
			})
		bar.progress(i / len(files))
	bar.end()

