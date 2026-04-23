users=$(cat notlar.csv | cut -d, -f1| sort|uniq)
assignments=$(cat notlar.csv | cut -d, -f2| sort|uniq)
echo -n " ,"; for assignment in $assignments;    do  echo -n $assignment, ;done; echo;

for user in $users
do    
	echo -n "$user," 
	for assignment in $assignments
	do     
		not=$(grep "$user,$assignment," notlar.csv| cut -d, -f3); 
		echo -n "$not,"; 
	done;
	echo;  
done

