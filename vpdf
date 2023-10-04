#!/bin/bash

valid=`ls $1`

if [ "$valid" == "$1" ]; then

	path=`pwd`/$1  #saved the file path and concat with $1
  echo $path
  python3 main.py $path

	else
		echo " ======================== WARNING ================================= "
		echo "                       File Not Found!!!"
		echo " ================================================================== "
fi