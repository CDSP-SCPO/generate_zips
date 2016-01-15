#!/usr/bin/python
# -*- coding: utf-8 -*-
# Execution example : python generate_zips.py "path/to/folder/to/zip"

#
# Libs
#
import logging, os, sys, zipfile, zlib

#
# Config
#
path_separator = '/'
zip_folder_name = 'sp5-ol.zip'
log_folder = 'log'
log_level = logging.DEBUG

#
# Functions
#
def zipdir(path, ziph) :
	# ziph is zipfile handle
	for root, dirs, files in os.walk(path) :
		for file in files :
			ziph.write(os.path.join(root, file), os.path.join(root.replace(path, ''), file))

#
# Main
#
if __name__ == '__main__' :
	if len(sys.argv) != 2 :
		print ''
		print 'Arguments error'
		print 'Correct usage : python ' + sys.argv[0] + ' "path/to/folder/to/zip"'
		print 'The first argument is mandatory and is the path to the folder to zip'
	else :
		# Check that log folder exists, else create it
		if not os.path.exists(log_folder) :
			os.makedirs(log_folder)
		# Create log file
		log_file = log_folder + path_separator + sys.argv[0].replace('.py', '.log')
		logging.basicConfig(filename = log_file, filemode = 'w', format = '%(asctime)s  |  %(levelname)s  |  %(message)s', datefmt = '%m/%d/%Y %I:%M:%S %p', level = log_level)
		logging.info('Start')
		# Create archive folder
		zf = zipfile.ZipFile(zip_folder_name, mode='w', compression=zipfile.ZIP_DEFLATED, allowZip64=1)
		logging.info('Create archive folder')
		# Add files into archive folder
		zipdir(sys.argv[1], zf)
		logging.info('Folder zipped into file : ' + zip_folder_name)
		zf.close()