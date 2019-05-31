
echo enter the length of first side
read a

echo enter the length of second side
read b

echo enter the length of third side
read c

if [ $a -eq $b  -a  $b -eq $c ]
then
   echo Equilateral
elif [  $a -ne $b  -a   $b -ne $c ] 
then
   echo Scalene
else
   echo Isoceles

fi

