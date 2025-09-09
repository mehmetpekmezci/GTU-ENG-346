#!/bin/bash
echo ""
echo "#########################################################################"
echo "#################### GREP                      ##########################"
echo "#########################################################################"
echo ""

grep equinox /var/tmp/eclipse/org.eclipse.equinox.p2.rcp.feature_1.4.900.v20200813-0739/{*.properties,*.html} | head -2
echo ""
echo "#########################################################################"
echo ""

grep -A2 equinox /var/tmp/eclipse/org.eclipse.equinox.p2.rcp.feature_1.4.900.v20200813-0739/*.xml| tail -4
echo ""
echo "#########################################################################"
echo ""

grep -R equinox /var/tmp/eclipse/ | head -2
echo ""
echo "#########################################################################"
echo ""

grep -R equinox /var/tmp/eclipse/ | tail -2
echo ""
echo "#########################################################################"
echo ""

grep -R equinox /var/tmp/eclipse/ | grep -v xml| tail -2
echo ""
echo "#########################################################################"
echo ""

grep -R 'id="warranty"\|featureName=.*support' /var/tmp/eclipse/| head -3
echo ""
echo "#########################################################################"
echo ""


