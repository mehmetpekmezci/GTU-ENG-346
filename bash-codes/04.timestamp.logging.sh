#!/bin/bash
echo ""
echo "#########################################################################"
echo "############################# TIMESTAMP AND LOGGING USAGE ###############"
echo "#########################################################################"
echo ""

TIMESTAMP=$(date '+%Y%m%d%H%M%S')
echo $TIMESTAMP
(
 hostname
) >& /var/tmp/mylog.$TIMESTAMP

(
 hostname
) 1> /var/tmp/stdout.log.$TIMESTAMP

(
 hostname1
) 2> /var/tmp/stderr.log.$TIMESTAMP

for i in  /var/tmp/*.$TIMESTAMP; do    echo ""; echo ""; echo "File :$i";echo "Content:";    cat $i; done
