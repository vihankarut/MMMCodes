print("mathwork.py")
problem = input("Enter a math problem,Or 'q'to quit ")
while (problem != "q"):
    print("The answer to ",problem,"is ",eval(problem))
    problem = input("Enter another math problem,Or 'q'to quit")
    
