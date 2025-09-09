#/bin/bash

SCRIPT_NAME="$0"

function print_usage_and_exit {
   tput setaf 1 ## RED
   tput bold
   echo "$1"
   echo "Usage:  ${SCRIPT_NAME} <dir> <expression> [a|d|f|l] <depth>"
   tput sgr0
   exit 1
}

if [ $# -lt 2 ]
then
	print_usage_and_exit "Wrong number of parameters :"
fi

DIR="$1"
EXPRESSION="$2"
TYPE="$3"
DEPTH="$4"

if [ ! -d $DIR ]; then print_usage_and_exit "Directory $DIR does not exist"; fi

if [ "$TYPE" != "" -a "$TYPE" != "a" -a "$TYPE" != "d"  -a "$TYPE" != "f"  -a "$TYPE" != "l" ]
then
	print_usage_and_exit "Type can only be one of the a,d,f,l or no-parameter "
fi

DEPTH_FIND_ARGUMENT=""
if [ "$DEPTH" != "" ]; then DEPTH_FIND_ARGUMENT="-maxdepth $DEPTH"; fi

TYPE_FIND_ARGUMENT=""
if [ "$TYPE" != "" ]; then TYPE_FIND_ARGUMENT=" -type $TYPE"; fi

echo "find $DIR $DEPTH_FIND_ARGUMENT $TYPE_FIND_ARGUMENT -name $EXPRESSION"
find $DIR $DEPTH_FIND_ARGUMENT $TYPE_FIND_ARGUMENT -name "$EXPRESSION" 
