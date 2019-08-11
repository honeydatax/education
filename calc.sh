#!/bin/bash
printf "Content-type:text/txt\r\n\r\n"
d=$(date)
list2=($QUERY_STRING)
printf "$list2 \n" > calc.dat
printf "quit\n" >> calc.dat
bc calc.dat > shell.dat
list1=$(cat shell.dat)
echo bash web server text
echo online calculator
echo $d
echo "$list2 = $list1"



