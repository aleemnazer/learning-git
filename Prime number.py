def checkPrime(X):
  if X > 1:
    for i in range(2, int(X/2) + 1):
      if(X % i) == 0:
        print(X, " is not a prime number\n")
        print("The factors of", X, "are: ")
        for j in range(1, X + 1):
          if(X % j) == 0:
            print(j," ")
        break
    else:
      print(X, " is a prime number")
  else:
    print(X, " is 1 or less than one and it's not prime")

X = int(input("Enter a positive Number: "))
checkPrime(X)
