# PlaylistManager v.1.2

The objective of this project is to manage files from a .m3u file (a playlist) and transfer them to a selected PATH. 

Note that to be able to do this, you must have the files saved on your system. Downloading a .m3u file without the files or with broken paths will make this program fail.

## Requirements

- (FFMPEG)[https://ffmpeg.org/download.html], as for the current version its not packaged in the program. 

## Usage

Playlist Manager works 2 ways, by a very simple CLI and also argument input on the python program. 

For using the CLI you only got to run the main.py and you'll be prompted for the paths, the program will finish by its own. To use the arguments paste the paths using the following syntax:

> python numark_converter.py /path/to/your/playlist /path/to/output/folder [Y/N]

## Changelog

#### 1.2
- Works only in terminal. Needs a couple of libraries that are not bundled to this repository
- If you have ffmpeg installed you can convert the files to mp3

