#!/bin/bash
echo ""
echo "#########################################################################"
echo "####################  ARRAY MENU                ########################"
echo "#########################################################################"
echo ""


echo "red green blue" > colors.txt
for i in $(cat colors.txt); do    echo $i; done
color_array=($(cat colors.txt))
for((i=0;i<${#color_array[@]};i=i+1)); do   echo "$i. ${color_array[$i]}"; done
read -p "Select a color (0-2) : " selection
echo "You selected ${color_array[$selection]}"
