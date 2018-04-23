#!/bin/bash

mysql=`which mysql`
file='class.sql'
$mysql -uroot -p<<EOF
use Test
source $file
EOF

