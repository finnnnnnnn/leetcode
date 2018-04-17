#!/bin/bash

#use shell to insert mysql.

mysql=`which mysql`
file='world.sql'
$mysql -u root -p <<EOF
use Test;
source $file;
EOF
