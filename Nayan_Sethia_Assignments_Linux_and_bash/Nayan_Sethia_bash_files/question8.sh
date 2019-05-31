echo enter the number you want to check for prime number
read n

i=2
k=1
while [ $i -lt $n ]
do
 q=$(( $n / $i ))
 if [ $q -eq 0 ]
 then
  k=0
  break
 fi
 i=$(( $i + 1 ))
done

if [ $k -eq 1 ]
then 
  echo prime
else
  echo not a prime
fi
