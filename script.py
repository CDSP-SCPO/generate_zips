#!/usr/bin/python
# -*- coding: utf-8 -*-
# Execution example : python script.py "path/to/folder/to/convert" "path/to/conf/file"

#
# Libs
#

import json
import logging
import os
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
	if not os.path.exists(cines_folder) :
		os.makedirs(cines_folder)
	for root, dirs, files in os.walk(sys.argv[1]) :
		print ''
		print root
		print dirs
		print files
		# TODO : Check if one of conf.keys() in contains in root.replace(sys.argv[1], '') and the extension file is in conf["SOMETHING"]
	sys.exit()


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