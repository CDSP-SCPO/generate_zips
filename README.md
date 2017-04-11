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

One is to upload for the website (_survey\_name_-on.zip).

The other one is to be available on the website to let the user download the dataset (_survey\_name_-dl.zip).


## Credits

[Sciences Po - CDSP](http://cdsp.sciences-po.fr/)