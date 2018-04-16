#!/bin/bash

#Read from the file file.txt and print its transposed content to stdout

gawk '
{
    for (i=1;i<=NF;i++){
        if(var[i]==""){
            var[i]=$i;
        }
        else{
            var[i]=var[i] " " $i;
        }
    }
}
END {
    for(i=1;i<=NF;i++){
        print var[i];
    }
}' $1

