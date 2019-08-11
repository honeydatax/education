#!/bin/bash
d=$(date)
list1=$(ls -l)
printf "Content-type:text/txt\r\n\r\n"
echo bash web server text
echo file list
echo $d
echo "$list1"


