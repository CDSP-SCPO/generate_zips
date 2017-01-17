#!/usr/bin/python
# -*- coding: utf-8 -*-
# Execution example : python script.py "path/to/folder/to/convert" "path/to/matching/file"

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
# Main
#

if __name__ == '__main__' :
	# Generate log file path
	log_file = os.path.join(log_folder, sys.argv[0].replace('.py', '.log'))
	# Init logs
	logging.basicConfig(filename=log_file, filemode='a+', format='%(asctime)s  |  %(levelname)s  |  %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=log_level)
	logging.info('Start script')
	sys.exit()