#!/bin/bash
d=$(date)
list1=$(df)
printf "Content-type:text/txt\r\n\r\n"
echo bash web server text
echo disk free
echo $d
echo "$list1"


