#!/bin/bash
echo "#########################################################################"
echo "#################### EXPORT                     ########################"
echo "#########################################################################"
echo ""

MYVAR="VALUE1"
echo '
echo "MYVAR variable in export.release.sh : -- $MYVAR --"
MYVAR="VALUE2"
export MYVAR
' > export.release.sh

chmod +x ./export.release.sh
./export.release.sh
echo "MYVAR variable in main script : $MYVAR"

echo "#########################################################################"

export MYVAR
echo "Now exporting MYVAR in main script"
./export.release.sh
echo "#########################################################################"

source ./export.release.sh
echo "MYVAR variable in main script : $MYVAR after sourcing  export.release.sh"

echo ""
echo "#########################################################################"
echo "#################### BASH_SOURCE                 ########################"
echo "#########################################################################"
echo ""

echo '
CURRENT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
export CURRENT_DIR
' > bash_source.release.sh

. ./bash_source.release.sh

echo "CURRENT_DIR variable in main script : $CURRENT_DIR after sourcing  bash_source.release.sh"





