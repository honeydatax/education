#!/bin/bash
d=$(date)
list1=($QUERY_STRING)
printf "Content-type:text/txt\r\n\r\n"
echo bash web server text
echo QUERY
echo $d
echo "$list1"


