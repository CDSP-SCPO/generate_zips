# generate_zips


## What for ?

Add meta_documents.csv file into ol_folder/_meta folder.
Zip the ol_folder and the dl_folder


## How to use it ?

generate_zips can be used with any system compatible with python 2.7 by invoking the command :

`python generate_zips.py "path/to/folder/to/zip" "path/to/csv/inventory/file" "survey_name"`

* The first argument is mandatory and is the path to the folder to zip
* The second argument is mandatory and is the path to the CSV inventory file
* The third argument is not mandatory and is the name of the survey, this is used to name the archive folders


## What is the output ?

The output are 2 archive folders.

One is to upload for the website (_survey\_name_-ol.zip).

The other one is to be available on the website to let the user download the dataset (_survey\_name_-dl.zip).


## How are these folders generated ?

The _survey\_name_-ol.zip contains :
* The transcription file into XML
* The inventory file
* The classification tree file
* The "enquête sur l'enquête" files
* The meta files ('meta_documents.csv', 'meta_speakers.csv')
* Others files as setted into the inventory file

The _survey\_name_-dl.zip contains :
* The transcription files into ODT and PDF
* The inventory file
* The classification tree file
* The "enquête sur l'enquête" files
* Others files as setted into the inventory file


### Warning

Only the 22d and the 23d columns of the inventory file passed as second argument. So this file has to have at least 23 columns.


## Credits

[Sciences Po - CDSP](http://cdsp.sciences-po.fr/)