count=10

if [ $count -eq 10 ]

then

	echo "true"

else

	echo "false"

fi


value="guessme"

guess=$1

if [ "value" = "$guess" ]

then
	echo "they are equal"

else

	echo "they are not equal"
	
fi
