import sys
input = int(sys.argv[1]);


print("## FizzBuzz ## ");

print(f"Input: {input}");

def fizzBuzz(n: int):
    for i in range(1,n+1):
        threeDivisible = i % 3 == 0; 
        fiveDivisible = i % 5 == 0; 

        if(threeDivisible and fiveDivisible):
            print("FizzBuzz")
        elif(threeDivisible):
            print("Fizz")
        elif(fiveDivisible):
            print("Buzz")
        else:
            print(str(i))

fizzBuzz(input);
