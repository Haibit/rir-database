Room Impulse Response (RIR) Database
====================================
Some Python scripts to download and organize RIRs from various online sources. This repository does not provide RIRs. If you use the scripts to obtain RIRs make sure to follow the licenses for the individual collection and be nice by citing there papers ;)

Currently RIRs are collected from:

- [Acoustic Characterisation of Environments (ACE) Corpus](http://www.ee.ic.ac.uk/naylor/ACEweb/index.html)
- [Aachen Impulse Response (AIR) Databas](http://www.iks.rwth-aachen.de/de/forschung/tools-downloads/aachen-impulse-response-database/)
- [Multichannel Acoustic Reverberation Database at York (MARDY) Database](http://www.commsp.ee.ic.ac.uk/~sap/resources/mardy-multichannel-acoustic-reverberation-database-at-york-database/)
- [Database of Omnidirectional and B-Format Impulse Responses](http://isophonics.net/content/room-impulse-response-data-set)
- [RWCP Sound Scene Database](http://www.openslr.org/13/)

## Usage

```
# This will download all the collections above and copy RIRs to the `wav.imported` folder while putting some infos into `db.json`
python3 scripts/createDb.py --sources=all

# Resample RIRs to 16 kHz, normalize the amplitude and cut silence at the beginning. Results are saved to `wav.normalized`
python3 scripts/normalize.py -fs 16000

# to save some disk space you can delete the downloaded archives
rm -rf download
```

## Installation

The scripts require the following Python modules: `numpy` `scipy` `soundfile` `patool` `scikits.samplerate`

`scikits.samplerate` does not officially support Python3 but you can install a dev version using
```
pip install git+https://github.com/gregorias/samplerate.git
```

Full example installation (MacOS):

```
$ brew install libsamplerate unrar
Warning: libsamplerate 0.1.9 is already installed
Warning: unrar 5.5.8 is already installed
$ virtualenv rir-db-env
Using base prefix '/usr/local/Cellar/python3/3.5.2_3/Frameworks/Python.framework/Versions/3.5'
New python executable in /Users/marvin/Downloads/rir-database/rir-db-env/bin/python3.5
Also creating executable in /Users/marvin/Downloads/rir-database/rir-db-env/bin/python
Installing setuptools, pip, wheel...done.
$ source rir-db-env/bin/activate
$ pip install numpy scipy soundfile patool
Collecting numpy
  Using cached numpy-1.14.0-cp35-cp35m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl
Collecting scipy
  Using cached scipy-1.0.0-cp35-cp35m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl
Collecting soundfile
  Using cached SoundFile-0.9.0.post1-py2.py3.cp26.cp27.cp32.cp33.cp34.cp35.cp36.pp27.pp32.pp33-none-macosx_10_5_x86_64.macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.whl
Collecting patool
  Using cached patool-1.12-py2.py3-none-any.whl
Collecting cffi>=0.6 (from soundfile)
  Using cached cffi-1.11.3-cp35-cp35m-macosx_10_6_intel.whl
Collecting pycparser (from cffi>=0.6->soundfile)
Installing collected packages: numpy, scipy, pycparser, cffi, soundfile, patool
Successfully installed cffi-1.11.3 numpy-1.14.0 patool-1.12 pycparser-2.18 scipy-1.0.0 soundfile-0.9.0.post1
$ pip install git+https://github.com/gregorias/samplerate.git
Collecting git+https://github.com/gregorias/samplerate.git
  Cloning https://github.com/gregorias/samplerate.git to /private/var/folders/41/yg43zvdx59n8qvs278kh6cgh0000gn/T/pip-5z6otgy5-build
Requirement already satisfied: numpy in ./rir-db-env/lib/python3.5/site-packages (from scikits.samplerate==0.4.0.dev0)
Installing collected packages: scikits.samplerate
  Running setup.py install for scikits.samplerate ... done
Successfully installed scikits.samplerate-0.4.0.dev0
```

