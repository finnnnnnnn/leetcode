#!/bin/bash

#Read from the file words.txt and output the word frequency list to stdout.

gawk '
{
    for(i=1;i<=NF;i++){
        ++var[$i];
    }
}
END{
for(i in var){
    print i,var[i];
}
}' $1
