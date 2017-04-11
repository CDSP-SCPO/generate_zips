#!/usr/bin/python
# -*- coding: utf-8 -*-
# Execution example : python generate_zips.py "path/to/folder/to/zip" "path/to/csv/inventory/file" "survey_name"

#
# Libs
#
import csv, logging, os, sys, zipfile, zlib

#
# Config
#
log_folder = 'log'
log_level = logging.DEBUG
ignored_extensions = ['jp2', 'j2k', 'jpf', 'jpx', 'jpm', 'mj2']
ignored_files = ['.DS_Store']


#
# Functions
#

# A file is a classification plan file if its name is "planclassement.pdf"
def is_classification_file(file) :
	return file == 'planclassement.pdf'

# A file is a transcription file if its name contains "_transcr_"
def is_transcr_file(file) :
	return any(x in file for x in ['_transcr_', '_trans_'])

# A file is an inventory if its file name contains "_add_archives_inventaire"
def is_inventory_file(file) :
	return '_add_archives_inventaire' in file

# A file is an "enquête sur l'enquête" file if it is into folder "add/ese" and its extension is ".mp3", ".xml" or ".pdf"
def is_ese_file(root, extension) :
	return os.path.join('add', 'ese') in root and extension.lower() in ['mp3', 'xml', 'pdf']

# A file is a meta file if its name is "meta_documents.csv" or "meta_speakers.csv"
def is_meta_file(file) :
	return file in ['meta_documents.csv', 'meta_speakers.csv']

def add_file_to_archive(zf, root, path, file) :
	zf.write(os.path.join(root, file), os.path.join(root.replace(path, ''), file))

def zipdir(path, zf_ol, zf_dl) :
	# zf_ol and zf_dl are zipfile handle
	for root, dirs, files in os.walk(path) :
		for file in files :
			logging.info('Add file into archive folder : ' + os.path.join(root, file))
			extension = file.split('.')[-1]
			file_without_extension = file.split('.')[0]
			# Ignore all the JPEG2000 files
			if not extension in ignored_extensions and not file in ignored_files :
				# Transcription file
				if is_transcr_file(file) :
					# Add ODT and PDF transcription files into "download" archive folder
					if extension.lower() in ['odt', 'pdf'] :
						add_file_to_archive(zf_dl, root, path, file)
					# Add XML transcription files into "online" archive folder
					elif extension.lower() in ['xml'] :
						add_file_to_archive(zf_ol, root, path, file)
				# If file is an inventory, classification or "enquête sur l'enquête", add it to "donwload" and "online" archive folder
				elif is_inventory_file(file) or is_classification_file(file) or is_ese_file(root, extension) :
					add_file_to_archive(zf_dl, root, path, file)
					add_file_to_archive(zf_ol, root, path, file)
				# If file is a meta file, add it to "online" archive folder
				elif is_meta_file(file) :
					add_file_to_archive(zf_ol, root, path, file)
				# For other files, check into the inventory file
				elif file_without_extension in recordsbyid.keys() :
					if recordsbyid[file_without_extension][21] != '' :
						add_file_to_archive(zf_dl, root, path, file)
					if recordsbyid[file_without_extension][22] != '' :
						add_file_to_archive(zf_ol, root, path, file)
				# Else do nothing
				else :
					logging.info('#ignored : file not added into "online" archive folder neither into "download" archive folder : ' + file)

#
# Main
#
if __name__ == '__main__' :
	if len(sys.argv) <= 3 :
		print ''
		print 'Arguments error'
		print 'Correct usage : python ' + sys.argv[0] + ' "path/to/folder/to/zip" "path/to/csv/inventory/file" "survey_name"'
		print 'The first argument is mandatory and is the path to the folder to zip'
		print 'The second argument is mandatory and is the path to the CSV inventory file'
		print 'The third argument is not mandatory and is the name of the survey, this is used to name the archive folders'
	else :
		# Check that log folder exists, else create it
		if not os.path.exists(log_folder) :
			os.makedirs(log_folder)
		# Create the archive folders names
		survey_name = sys.argv[3] if len(sys.argv) == 4 else 'survey'
		zip_online_folder_name = survey_name + '-ol.zip'
		zip_download_folder_name = survey_name + '-dl.zip'
		# Create log file
		# log_file = log_folder + path_separator + sys.argv[0].replace('.py', '.log')
		log_file = os.path.join(log_folder, sys.argv[0].replace('.py', '.log'))
		logging.basicConfig(filename = log_file, filemode = 'w', format = '%(asctime)s  |  %(levelname)s  |  %(message)s', datefmt = '%m/%d/%Y %I:%M:%S %p', level = log_level)
		logging.info('Start')
		# Parse inventory file
		logging.info('Parse inventory file')
		inventory_file = sys.argv[2]
		recordsbyid = {}
		with open(inventory_file, 'rb') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
			for x in spamreader :
				if len(x) == 23 :
					recordsbyid[x[1]] = x
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