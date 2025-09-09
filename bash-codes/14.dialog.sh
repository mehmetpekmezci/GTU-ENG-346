#!/bin/bash
echo ""
echo "#########################################################################"
echo "####################  DIALOG                     ########################"
echo "#########################################################################"
echo ""

value1=$(dialog  --stdout  --title "Dialog title" --inputbox "Enter your name:" 0 0 )
dialog --stdout --default-button "no" --no-label "I don't want to format" --yes-label "I want to format" --yesno "Do you really want to format the partition?" 0 0
value2=$?
value3=$(dialog --stdout --checklist "Select items:" 0 0 0 \
  1 "Choice number one" off \
  2 "Choice number two" on \
  3 "Choice number three" off)
value4=$(dialog --stdout --radiolist "Select items:" 0 0 0 \
  1 "Choice number one" Off \
  2 "Choice number two" on \
  3 "Choice number three" off) 
value5=$( dialog --stdout --insecure --passwordbox "Enter your password:" 0 0  )
echo ""
echo "#########################################################################"
echo ""
echo "value1=$value1"
echo "value2=$value2"
echo "value3=$value3"
echo "value4=$value4"
echo "value5=$value5"



