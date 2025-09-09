#!/bin/bash
echo ""
echo "#########################################################################"
echo "#################### FIND AND REPLACE          ##########################"
echo "#########################################################################"
echo ""

find /var/tmp/eclipse/ -type f -name 'license.*' 
echo ""
echo "#########################################################################"
echo ""
find /var/tmp/eclipse/ -type f -name 'license.*' | xargs  grep equinox 
echo ""
echo "#########################################################################"
echo ""
find /var/tmp/eclipse/ -type f -name 'license.*' | xargs  grep equinox | cut -d: -f1| sort|uniq
echo ""
echo "#########################################################################"
echo ""
file=$(find /var/tmp/eclipse/ -type f -name 'license.*' | xargs  grep equinox | cut -d: -f1| sort|uniq| head -1)
grep equinox $file
echo ""
echo "#########################################################################"
echo ""
i=0
for file in $(find /var/tmp/eclipse/ -type f -name 'license.*' | xargs  grep equinox | cut -d: -f1| sort|uniq)
do
    perl -pi -e "s/equinox/equinox$i/" $file
    ((i=i+1))
    grep equinox $file
done


