#!/bin/bash
echo ""
echo "#########################################################################"
echo "#################### FIND BY DATE                ########################"
echo "#########################################################################"
echo ""

date > /var/tmp/eclipse/file123

find /var/tmp/eclipse -mmin -10

# -10  -> son 10 dakika icinde degisen
# +10  -> 10 dakika oncesine git, u tarihten once desigenleri getir
#         Yani -10 olarak yazilan arama ile gelen sonuclarin tam tersini getirir.
# 10   -> degisme tarihi tam 10. dakikada olanlari getir.
