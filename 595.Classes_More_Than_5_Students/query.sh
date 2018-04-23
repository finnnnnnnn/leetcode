#!/bin/bash

mysql=`which mysql`
$mysql -uroot -p Test -e "select class from courses group by class having count(distinct student)>=5"
