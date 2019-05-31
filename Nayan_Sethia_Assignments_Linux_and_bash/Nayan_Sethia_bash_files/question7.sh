echo enter the number whose factorial you want
read n

p=1
while [ $n -gt 0 ] 
do

  p=$(( $p * $n ))
  n=$(( $n - 1))
done
echo $p
