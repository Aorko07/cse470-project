def fibonacci(n):
    #nterms = int(input("How many terms? "))
    nterms = int(n)
    f=0

    # first two terms
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    else:
        print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        f+=n1
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
    return f