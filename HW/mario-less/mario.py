while True:
    n = input("Enter a size 1-8: ")
    n = int(n)
    if 1 <= n <= 8:
        print(f"Height:{n}")
        for i in range(1, 1+n):
            print(" "*(n-i)+"#"*i)
        break
    else:
        print("Please input a number between 1-8")