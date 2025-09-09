#!/bin/bash
echo ""
echo "#########################################################################"
echo "############################# FOR USAGE 1 ##########################"
echo "#########################################################################"
echo ""

MAX=4
for((i=0;i<$MAX;i=i+1)); do echo $i; done

echo ""
echo "#########################################################################"
echo "############################# FOR USAGE 2 ##########################"
echo "#########################################################################"
echo ""
touch /var/tmp/testfile1.txt  /var/tmp/testfile2.txt
for myfile in /var/tmp/*.txt
do
   echo "Txt file name is $myfile"
done

echo "#########################################################################"
echo "############################# FOR USAGE 3 ##########################"
echo "#########################################################################"
echo ""

echo "machine1:type1
machine2:type2 
machine3:type1" >  nodes.txt
for line in $(cat nodes.txt)
do
	machine=$(echo $line | cut -d\# -f1) 
	mtype=$(echo $line | cut -d\# -f2) 
	echo "Machine name is $machine which is of type $mtype "
done
