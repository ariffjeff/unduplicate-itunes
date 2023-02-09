import os
from pathlib import Path

from tinytag import TinyTag


def main():

  # ITUNES_MEDIA_PATH = input_validate_path("Enter path to the folder of iTunes music: ")
  ITUNES_MEDIA_PATH = Path("C:\\Users\\ariff\\Desktop\\Music - Copy")

  audio_types = [
     "m4a",
     "m4p", # iTunes DRM
     "mp3",
     "wav",
     "aac",
     "aiff"
  ]

  songs = get_files(ITUNES_MEDIA_PATH, audio_types)

  # group songs by artist
  songs_by_artist = {}
  for song in songs:
    artist = get_artist(ITUNES_MEDIA_PATH, song)
    songs_by_artist[artist] = []
  for song in songs:
    artist = get_artist(ITUNES_MEDIA_PATH, song)
    # name = song.name
    songs_by_artist[artist].append({
      "song": song,
      "track": TinyTag.get(song).track
    })


  # select which songs are duplicates per artist
  duplicate_songs = []
  track_count = []
  for artist in songs_by_artist:
    songs_by_artist[artist].sort(key=lambda x: x['song'], reverse=True) # easiest way to order correctly by song name
    for song in songs_by_artist[artist]:
      if(song['track'] in track_count):
        duplicate_songs.append(song)
      else:
        track_count.append(song['track'])
    track_count = []



def get_song(path: str, part: int) -> str:
  '''
  Get song name from path.
  path :
    string path to file, or just the filename itself
  part :
    0: song name without file extension
    1: file extension
  '''
  return os.path.splitext(path)[part]

def get_artist(path_exclusion: Path, song_path: Path) -> str:
  '''
  Get the name of the artist of a song.
  Strips path_exclusion from the song path to determine the artist since
  the artist name is always the folder immediately following the main path.
  '''
  artist = str(song_path).replace(str(path_exclusion)+("\\"), "")
  artist = artist.split("\\")[0]
  return artist

def get_files(path: list, extensions: list) -> list:
  all_files = []
  for ext in extensions:
      all_files.extend(path.glob('**/*.'+ext))
  return all_files


def input_validate_path(message_and_user_input: str, prefix="", postfix="", no_cwd=False) -> Path:
  '''
  Take user input and validates if it's a valid path.
  prefix and postfix surround message_and_user_input. This is useful for modifying the user input on the fly.
  Keep asking for input if it's an invalid path.
  Return a Path object of a valid string.
  '''
  input_path = input(message_and_user_input)
  try:
      custom_plugin_path = Path(os.path.join(prefix, input_path, postfix))
  except:
      print("Invalid path!")
      return input_validate_path(message_and_user_input, prefix, postfix, no_cwd)

  if(no_cwd and (str(input_path) == '.' or str(input_path) == "")):
    print("Invalid relative path to current directory!")
    return input_validate_path(message_and_user_input, prefix, postfix, no_cwd)
  
  if(not custom_plugin_path.exists()):
    print("Invalid path: {}".format(custom_plugin_path))
    return input_validate_path(message_and_user_input, prefix, postfix, no_cwd)
  return custom_plugin_path


if(__name__ == "__main__"):
  main()
