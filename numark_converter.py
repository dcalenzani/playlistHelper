# NUMARK MIXDECK USB CLI (V1)
'''
This project was done for copying files from a playlist in your system and convert them into mp3 by infering the format by reading the file extension (.mp3, .flac. aiff.) so they can be read by an Old Numark Mixdeck. It mixes the script in m3u.py and extends its utilities.
Note that you need to use some linux utilities (FFMPEG mostly) for its correct working, ill list the requirements in the README.txt
'''
# Libraries
import shutil
import os
import glob

# Variables
list = []
input_folder = ''
output_folder = ''

# User Input
input_playlist = input('Copy the path of your playlist: ')
output_folder = input('Copy the path to where you want your files: ')
mp3_or_not = input('Do you want to convert the files to mp3? Y/N:')

while mp3_or_not != 'Y' and mp3_or_not != 'N':
    mp3_or_not = input('Please enter Y or N')
    continue

# Program

# Open the playlist and create a log of the files to copy
fhand = open(input_playlist, 'r')
for line in fhand:
    if not line.startswith('/home/carlos/DDrive/Musica/'):
        continue
    with open('log.txt', 'a') as file:
        route = line.rstrip()
        list.append(route)
fhand.close()

# Sanity printing
print(f'We ve found {len(list)} files')

for item in list:
    remaining_files = len(list) - len(glob.glob(os.path.join(output_folder, '*')))
    # Check if user mp3_or_not selection
    print(f"{remaining_files}/{len(list)} files left")
    if mp3_or_not == 'N':
        shutil.copy2(item, output_folder)
    # Convert files in the list to mp3 (using ffmpeg)
    if mp3_or_not == 'Y':
        filename = os.path.splitext(os.path.basename(item))[0]
        mp3_file = os.path.join(output_folder, f'{filename}.mp3')
        os.system(f'ffmpeg -hide_banner -loglevel error -i "{item}" -codec:a libmp3lame -qscale:a 2 "{mp3_file}"')
