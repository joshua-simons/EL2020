#!/bin/bash
# This script will be about making sure I don't spend more than $10 since I am broke.

declare -a List=( );
x=0
while [[ $x -lt 5 ]]
do
	echo "Enter in an item (5 item limit): "
	read item
	List=("${List[@]}" $item)
	((x++))
done


echo -n "Would you like to view your list of items(0=no, 1=yes)? "
read ans
if [[ $ans -eq 0 ]]
then
	echo "Have a great day!"

elif [[ $ans -eq 1 ]]
then
	echo ${List[@]}
else
	echo "Wrong input, please try again."
fi


echo -n "How much are the items you want to buy? $"
read price
if [[ $price -gt 10 ]]
then
	echo "Too much money, you are broke!!"
elif [[ $price -eq 10 ]]
then
	echo "Ask yourself: Do you really need all these items?"
else
	echo "Ok, just watch yourself."
fi



