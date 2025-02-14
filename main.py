'''
	File: main.py
	Author: Dane Rainbird (hello@danerainbird.me)
	Last Edited: 2025-02-14
'''

import argparse
import os
import shutil

def main(args):
	"""
	Main function
	"""

	# Print a welcome message
	print('Welcome to the Hoyoverse Web Event folder processing script!')
	print('Processing / sorting files in the directory: {}\n\n'.format(args.path))

	# Check if the path exists
	if checkIfPathExists(args.path):
		processFiles(args.path)
	else:
		print('Provided path does not exist (or is not accessible to your user). Please try again!')
		exit(1)


def parseArgs():
	"""
	Parse the command line arguments.
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument('--path', type=str, help='Absolute path to the directory containing the files to be processed.', required=True)
	args = parser.parse_args()
	return args


def checkIfPathExists(path):
	"""
	Check if a given path exists.
	"""
	return os.path.exists(path)


def processFiles(path):
    """
    Process the files in the directory.
    More specifically, moves the files in the SPINE and other_resources folders to subdirectories based on their longest matching prefix.
    """
    
    # Get the list of files in the directory
    files = os.listdir(path)
    
    # Ensure that there is a SPINE folder and an "other_resources" folder
    if 'SPINE' not in files:
        print('SPINE folder not found in the provided directory. Please ensure that the SPINE folder is present.')
        exit(1)
    if 'other_resources' not in files:
        print('other_resources folder not found in the provided directory. Please ensure that the other_resources folder is present.')
        exit(1)

    # Get the list of files in the SPINE folder
    spine_files = os.listdir(os.path.join(path, 'SPINE'))

    # Create the parent directory for the files
    sorted_dir = os.path.join(path, 'sorted')
    if not checkIfPathExists(sorted_dir):
        os.makedirs(sorted_dir)
        print('Created new parent directory: {}'.format(sorted_dir))

    for file in spine_files:
        if file.endswith('.atlas') or file.endswith('.json'):
            base_name = os.path.splitext(file)[0]

            # Create a directory for the base name if it doesn't exist
            base_name_dir = os.path.join(sorted_dir, base_name)
            if not checkIfPathExists(base_name_dir):
                os.makedirs(base_name_dir)
                print('Created a new subdirectory: {}'.format(base_name_dir))

            # Move the file to the base name directory
            try:
                shutil.move(os.path.join(os.path.join(path, 'SPINE'), file), os.path.join(base_name_dir, file))
            except Exception as e:
                print(f'Error moving file {file}: {str(e)}')
                continue

    # Check if the spine folder is now empty
    if len(os.listdir(os.path.join(path, 'SPINE'))) == 0:
        os.rmdir(os.path.join(path, 'SPINE'))
        print('Removed the SPINE folder as it is now empty.')

    # Create a dictionary to store the longest matching prefix for each file
    file_matches = {}
    
    # Get list of all base directories in sorted
    base_directories = os.listdir(sorted_dir)
    
    # Process files in other_resources
    other_resources_files = os.listdir(os.path.join(path, 'other_resources'))
    
    # First pass: find the longest matching prefix for each file
    for file in other_resources_files:
        longest_match = ''
        for base_name in base_directories:
            if file.startswith(base_name) and len(base_name) > len(longest_match):
                longest_match = base_name
        if longest_match:  # Only store if we found a match
            file_matches[file] = longest_match

    # Second pass: move the files based on their longest matching prefix
    for file, matched_base in file_matches.items():
        source = os.path.join(path, 'other_resources', file)
        destination = os.path.join(sorted_dir, matched_base, file)
        
        try:
            if checkIfPathExists(source):  # Check if file still exists before moving
                shutil.move(source, destination)
                print('Moved file {} to subdirectory {}'.format(file, matched_base))
            else:
                print(f'Warning: Source file not found: {source}')
        except Exception as e:
            print(f'Error moving file {file}: {str(e)}')
            continue

    # Check if the other_resources folder is now empty
    if len(os.listdir(os.path.join(path, 'other_resources'))) == 0:
        os.rmdir(os.path.join(path, 'other_resources'))
        print('Removed the other_resources folder as it is now empty.')

    print('Processing complete! You can now use Spine to open the files in the sorted directories and put the images and animations together.')


if __name__ == '__main__':
	args = parseArgs()
	main(args)