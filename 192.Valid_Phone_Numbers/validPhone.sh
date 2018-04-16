#!/bin/bash

#Read from the file file.txt and output all valid phone numbers to stdout.

cat $1|gawk --re-interval '/^\(?[0-9]{3}\)?(| |-|)[0-9]{3}-[0-9]{4}$/{print $0}'


