#!/bin/bash

# loop & print a folder recusively,
print_folder_recurse() {
    for i in "$1"/*;do  #before: "$1"
        if [ -d "$i" ];then
            #if the file being looked at is a directory, recursion go brrr
            #echo "dir: $outputpath$(basename $1)/$(basename $i)"
            #echo $i
            print_folder_recurse "$i"
        elif [ -f "$i" ] && [ -d "$outputpath${1#$path}" ] && [[ $(basename $i) == *.csv ]]; then 
            
            #echo $outputpath${1#$path}


            #mkdir -p $outputpath${1#$path}
            #echo "starting video $i"
            #./bin/OpenPoseDemo.exe --video $i --hand --write_json $outputpath${1#$path} && continue
            #echo "finished video $i"

            echo $i
            cp $i $outputpath${1#$path}
            #echo $1
            #echo $outputpath${1#$path}
            #python3 ./featureExtraction/convertDirectoryOfJsonToCsv.py $1 $outputpath${1#$path} && return
            #python3 ./featureExtraction/addingFacetouchToCsv.py $i && return

            #echo "dir: $outputpath$(basename $1)/$(basename $i)"
            #echo " "

        fi
    done
}


# try get path from param
path=""
if [ -d "$1" ]; then
    path=$1;
else
    path="/tmp"
fi
#path = "/home/vero/Dropbox/wellbeingdataset"
outputpath="$2"
#outputpath = "/home/vero/coding/masters/mastersProject/src/csvOut"
echo "base path: $path"
echo "destination path: $outputpath"
print_folder_recurse $path


