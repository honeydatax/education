#!/bin/bash
printf "Content-type:text/txt\r\n\r\n"
file1=counter.dat
d=$(date)
if test -f "$file1"; then
printf "\n"
else
echo "0" > counter.dat
fi
list1=$(cat counter.dat)
printf "$list1 + 1\n" > counter.dat
printf "quit\n" >> counter.dat
bc counter.dat > shell.dat
list1=$(cat shell.dat)
echo "$list1"  > counter.dat
echo bash web server text
echo file counter visit counter web site
echo $d
echo "$list1"


