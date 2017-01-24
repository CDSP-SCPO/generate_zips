#!/usr/bin/python
# -*- coding: utf-8 -*-
# Execution example : python script.py "path/to/folder/to/convert" "path/to/conf/file"

#
# Libs
#

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
	# TODO load conf file
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