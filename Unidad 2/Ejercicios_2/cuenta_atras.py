import time

try:
    n = int(input("introduce un numero"))
except ValueError as e:
    print ("Error" , e)
    exit(1)


if n >= 5 & n <= 50:
        for i in range(n, 0, -1):
            print(i, "...")
            time.sleep(0.5)
else:
        print("el num tiene que estar entre 5 y 50")
        exit(0)