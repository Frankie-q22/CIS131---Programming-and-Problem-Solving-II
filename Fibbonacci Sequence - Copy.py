#Frankie Quintero
#CIS131
#3/16/21

def fibonacci_numbers(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        # printing fibonacci numbers
        return fibonacci_numbers(num-2)+fibonacci_numbers(num-1)
  
  
n = int(input("Enter a Number for the Fibbonacci Sequence: "))
for i in range(0, n):
    print(fibonacci_numbers(i), end=" ")
  