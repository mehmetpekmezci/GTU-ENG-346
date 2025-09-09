#!/bin/bash
echo ""
echo "#########################################################################"
echo "#################### PERL MUTLILINE REPLACEMENT  ########################"
echo "#########################################################################"
echo ""

echo "deneme1
deneme2
deneme3
deneme4
deneme5" >/var/tmp/test.replace.txt
cat /var/tmp/test.replace.txt
echo ""
echo "#########################################################################"
echo ""
perl -0pi -e 's/deneme2\ndeneme3/DENEME/imsg' /var/tmp/test.replace.txt
cat /var/tmp/test.replace.txt

