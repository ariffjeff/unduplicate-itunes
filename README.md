
# unduplicate-itunes
[![Upload Python Package](https://github.com/ariffjeff/unduplicate-itunes/actions/workflows/python-publish.yml/badge.svg)](https://github.com/ariffjeff/unduplicate-itunes/actions/workflows/python-publish.yml)

Moves duplicate song files from your iTunes music directory to the trash.

Given that iTunes doesn't automatically remove missing songs (that you have deleted because they are duplicates), you will still need to manually remove the missing song entries from iTunes itself.

Depending on the structure of your iTunes music directory, it's possible that some duplicate files will be untouched while their original counterparts will be deleted instead (e.g. song.mp4 is removed, song 1.mp4 survives). Although, duplicates and originals look identical in iTunes regardless so this problem only matters if you care about the file names.

## Behavior
* You are prompted to make a backup of your iTunes music directory before executing. Even if you don't, you can still restore your files from the trash after the script is finished.
* You are prompted with the number of duplicates to be removed before executing.
* Directories (usually albums folders) that only contain duplicate files will be moved to the trash.
* A log file of all actions is output once the script finishes. It is created in whatever `cd` you have your terminal set to.

## Install ([PyPi](https://pypi.org/project/unduplicate-itunes/))
```
pip install unduplicate-itunes
```
## Usage
### Using [remove_by_artist_and_title.py](/unduplicate_itunes/remove_by_artist_and_title.py)
```
from unduplicate_itunes import remove_by_artist_and_title as undup
undup.main()
```
When you are prompted to enter the iTunes music directory, you can find the path by right clicking on any song in iTunes and select `Show in Windows Explorer` or `Show in Finder` (macOS). Grab the root folder that contains all the artist folders.

There are other scripts included that try to find duplicates by other methods but they are unfinished and aren't as effective at finding all duplicates.
