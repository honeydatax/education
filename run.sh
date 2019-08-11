#!/bin/bash
printf "Content-type:text/txt\r\n\r\n"
d=$(date)
list2=($QUERY_STRING)
list3=${list2//%20/ }
list1=$($list3)
echo bash web server text
echo online shell bash
echo $d
echo "$list3"
echo "$list1"



