#syeda khunza fatima
#22nd oct,2024

#this program help us in iterates the integers
for num in range (1, 51):
    if num %3 == 0 and num %5 == 0:
        print ("divisible by both")
    elif num % 3 == 0:
        print ("divisible by three")
    elif num % 5 ==0:
        print ("divisible by five")

    else:
        print(num)