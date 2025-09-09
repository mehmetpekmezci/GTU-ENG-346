#!/bin/bash
echo "#########################################################################"
echo "##### ASSIGN OUTPUT OF A COMMAND TO A VARIABLE ##########################"
echo "#########################################################################"
echo ""
hostname
HOSTTYPE=$(hostname| cut -d- -f1)
if [ "$HOSTTYPE" == "dev" ]
then
	echo "This is a development host"
fi

echo ""
echo "#########################################################################"
echo "############################# TR COMMAND USAGE ##########################"
echo "#########################################################################"
echo ""

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/eclipse/lib:/opt/havelsan/lib
echo $LD_LIBRARY_PATH | tr ':' '\n'| grep havelsan

echo ""
echo "#########################################################################"
echo "############################# IFS VARIABLE USAGE ##########################"
echo "#########################################################################"
echo ""

echo " word1 word1.1 word1.2
word2.1 word2.2 word2.3" > /var/tmp/file1.txt

for i in $(cat /var/tmp/file1.txt); do echo $i; done
OLDIFS=$IFS
IFS="
"
for i in $(cat /var/tmp/file1.txt); do echo $i; done
IFS=$OLDIFS

