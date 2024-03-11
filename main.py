import shutil
import os
import glob
import subprocess
import argparse

def main(input_playlist, output_folder, mp3_or_not):
    file_list = []

    with open(input_playlist, 'r') as fhand:
        for line in fhand:
            if line.startswith('/'):
                route = line.rstrip()
                file_list.append(route)

    print(f'We ve found {len(file_list)} files')

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    for item in file_list:
        remaining_files = len(file_list) - len(glob.glob(os.path.join(output_folder, '*')))
        print(f"{remaining_files}/{len(file_list)} files left")
        if mp3_or_not == 'N':
            shutil.copy2(item, output_folder)
        elif mp3_or_not == 'Y':
            filename = os.path.splitext(os.path.basename(item))[0]
            mp3_file = os.path.join(output_folder, f'{filename}.mp3')
            subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-i', item, '-codec:a', 'libmp3lame', '-qscale:a', '2', mp3_file], check=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='NUMARK MIXDECK USB CLI (V1)')
    parser.add_argument('--input_playlist', help='Path of your playlist')
    parser.add_argument('--output_folder', help='Path to where you want your files')
    parser.add_argument('--mp3_or_not', choices=['Y', 'N'], help='Do you want to convert the files to mp3? Y/N')
    args = parser.parse_args()

    if args.input_playlist and args.output_folder and args.mp3_or_not:
        input_playlist = args.input_playlist
        output_folder = args.output_folder
        mp3_or_not = args.mp3_or_not
    else:
        input_playlist = input("Enter the path of your playlist: ")
        output_folder = input("Enter the path to where you want your files: ")
        mp3_or_not = input("Do you want to convert the files to mp3? Y/N: ")

        while mp3_or_not not in ['Y', 'N']:
            print("Invalid input. Please enter Y or N.")
            mp3_or_not = input("Do you want to convert the files to mp3? Y/N: ")

    main(input_playlist, output_folder, mp3_or_not)