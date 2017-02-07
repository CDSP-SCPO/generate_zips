#!/usr/bin/python
# -*- coding: utf-8 -*-
# Execution example : python script.py "path/to/folder/to/convert" "path/to/conf/file"

#
# Libs
#

import json
import logging
import os
import shutil
import sys


#
# Config
#

log_folder = 'log'
log_level = logging.DEBUG


#
# Functions
#

def convertFolder() :
	# Generate log file path
	log_file = os.path.join(log_folder, sys.argv[0].replace('.py', '.log'))
	# Init logs
	logging.basicConfig(filename=log_file, filemode='a+', format='%(asctime)s  |  %(levelname)s  |  %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=log_level)
	logging.info('Start script')
	# Load conf file
	with open(sys.argv[2]) as conf_file :
		conf = json.load(conf_file)
	# Create CINES folder
	cines_folder = 'CINES'
	# Create remote folder
	if not os.path.exists(cines_folder) :
		os.makedirs(cines_folder)
	for root, dirs, files in os.walk(sys.argv[1]) :
		# If file extension is
		if root.replace(sys.argv[1], '') in conf.keys() :
			for file in files :
				if file.split('.')[-1] in conf[root.replace(sys.argv[1], '')] :
					distdir = os.path.join(cines_folder, root.replace(sys.argv[1], ''))
					if not os.path.exists(distdir) :
						logging.info('Create folder : ' + distdir)
						os.makedirs(distdir)
					logging.info('Copy file : ' + file)
					shutil.copy(os.path.join(root, file), distdir)


#
# Main
#

if __name__ == '__main__' :
	# Check args
	if len(sys.argv) != 3 or not sys.argv[2].lower().endswith('.json') :
		print ''
		print 'Arguments error'
		print 'Correct usage : python ' + sys.argv[0] + ' "path/to/folder/to/convert" "path/to/conf/file"'
		print 'The first argument is mandatory and is the path to the folder to convert'
		print 'The second argument is mandatory and is the path to the JSON config file'
	else :
		convertFolder()