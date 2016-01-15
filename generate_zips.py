#!/usr/bin/python
# -*- coding: utf-8 -*-
# Execution example : python generate_zips.py "path/to/folder/to/zip" "path/to/inventory/file"

#
# Libs
#
import logging, os, sys, zipfile, zlib

#
# Config
#
path_separator = '/'
zip_online_folder_name = 'sp5-ol.zip'
zip_download_folder_name = 'sp5-dl.zip'
log_folder = 'log'
log_level = logging.DEBUG
jp2_extensions = ['jp2', 'j2k', 'jpf', 'jpx', 'jpm', 'mj2']

#
# Functions
#
def zipdir(path, zf_ol, zf_dl) :
	# zf_ol and zf_dl are zipfile handle
	for root, dirs, files in os.walk(path) :
		for file in files :
			logging.info('Add file into archive folder : ' + os.path.join(root, file))
			extension = file.split('.')[-1]
			# Ignore all the JPEG2000 files
			if not extension in jp2_extensions :
				# Add TEI files into "online" archive folder only (not into "download" archive folder)
				# A file is a TEI if its extension is "xml" and the file name contains "_transcr_"
				if extension == 'xml' and '_transcr_' in file :
					zf_ol.write(os.path.join(root, file), os.path.join(root.replace(path, ''), file))
				# For other files, check into the inventory file
				else :
					# TODO : Pass inventory file as execution argument as CSV file (cdsp_bequali_sp6_add_archives_inventiry.xls)
					# TODO : Check into inventory file
					zf_ol.write(os.path.join(root, file), os.path.join(root.replace(path, ''), file))
					zf_dl.write(os.path.join(root, file), os.path.join(root.replace(path, ''), file))

#
# Main
#
if __name__ == '__main__' :
	if len(sys.argv) != 2 :
		print ''
		print 'Arguments error'
		print 'Correct usage : python ' + sys.argv[0] + ' "path/to/folder/to/zip" "path/to/inventory/file"'
		print 'The first argument is mandatory and is the path to the folder to zip'
		print 'The second argument is mandatory and is the path to the inventory'
	else :
		# Check that log folder exists, else create it
		if not os.path.exists(log_folder) :
			os.makedirs(log_folder)
		# Create log file
		log_file = log_folder + path_separator + sys.argv[0].replace('.py', '.log')
		logging.basicConfig(filename = log_file, filemode = 'w', format = '%(asctime)s  |  %(levelname)s  |  %(message)s', datefmt = '%m/%d/%Y %I:%M:%S %p', level = log_level)
		logging.info('Start')
		# Create archive folder
		zf_ol = zipfile.ZipFile(zip_online_folder_name, mode='w', compression=zipfile.ZIP_DEFLATED, allowZip64=1)
		zf_dl = zipfile.ZipFile(zip_download_folder_name, mode='w', compression=zipfile.ZIP_DEFLATED, allowZip64=1)
		logging.info('Create archive folders')
		# Add files into archive folder
		zipdir(sys.argv[1], zf_ol, zf_dl)
		logging.info('Online folder zipped into file : ' + zip_online_folder_name)
		logging.info('Download folder zipped into file : ' + zip_download_folder_name)
		print ''
		print 'Online folder zipped into file : ' + zip_online_folder_name
		print 'Download folder zipped into file : ' + zip_download_folder_name
		zf_ol.close()
		zf_dl.close()