#!/usr/bin/python
# -*- coding: utf-8 -*-
# Execution example : python generate_zips.py "path/to/folder/to/zip"

import os, sys, zipfile, zlib

zip_folder_name = 'sp5-ol.zip'

def zipdir(path, ziph) :
	# ziph is zipfile handle
	for root, dirs, files in os.walk(path) :
		for file in files :
			ziph.write(os.path.join(root, file), os.path.join(root.replace(path, ''), file))

if __name__ == '__main__' :
	if len(sys.argv) != 2 :
		print ''
		print 'Arguments error'
		print 'Correct usage : python ' + sys.argv[0] + ' "path/to/folder/to/zip"'
		print 'The first argument is mandatory and is the path to the folder to zip'
	else :
		zf = zipfile.ZipFile(zip_folder_name, mode='w', compression=zipfile.ZIP_DEFLATED, allowZip64=1)
		print 'Adding archive folder'
		zipdir(sys.argv[1], zf)
		print 'Folder zipped into file : ' + zip_folder_name
		zf.close()