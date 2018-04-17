#!/bin/bash

mysql=`which mysql`

$mysql -uroot -p Test -e 'select name,population,area from World where area>=3000000 or population>=25000000'
