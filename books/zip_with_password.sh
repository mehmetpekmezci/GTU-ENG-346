PASSWD=$(cat .password)
for i in *.pdf
do
	if [ -f $i ]
	then
	    echo $i
	    rm -f $i.zip
            zip --password $PASSWD $i.zip $i
	fi
done
