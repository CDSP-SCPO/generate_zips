#!/usr/bin/python
# -*- coding: utf-8 -*-
# Execution example : python generate_zips.py "path/to/folder/to/zip"

import os, sys, zipfile

# def zipdir(path, ziph) :
# 	# ziph is zipfile handle
# 	# for root, dirs, files in os.walk(path):
# 		# for file in files:
# 			# ziph.write(os.path.join(root, file))
# 	assert os.path.isdir(path)
# 	with closing(ZipFile(archivename, "w", ZIP_DEFLATED)) as z:
# 		for root, dirs, files in os.walk(basedir):
# 			# NOTE: ignore empty directories
# 			for fn in files:
# 				absfn = os.path.join(root, fn)
# 				zfn = absfn[len(basedir)+len(os.sep):] #XXX: relative path
# 				z.write(absfn, zfn)

def zipdir(path, ziph):
	# ziph is zipfile handle
	for root, dirs, files in os.walk(path):
		for file in files:
			ziph.write(os.path.join(root, file))

if __name__ == '__main__' :
	if len(sys.argv) != 2 :
		print ''
		print 'Arguments error'
		print 'Correct usage : python ' + sys.argv[0] + ' "path/to/folder/to/zip"'
		print 'The first argument is mandatory and is the path to the folder to zip'
	else :
		zipf = zipfile.ZipFile('python.zip', 'w')
		zipdir(sys.argv[1], zipf)
		zipf.close()