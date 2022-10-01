import random, time

orders = 0
operations = 0

#check with echo $TERM for control statements
UP = "\x1B[5A" ##match this to print statements (only called once here)
CLR = "\x1B[0K"
print("\n\n")  # set up blank lines so cursor moves work
while True:
   orders += random.randrange(1, 3)
   operations += random.randrange(2, 10)

   print(f"{UP}Orders: {orders}{CLR}\nOperations: {operations}{CLR}\nNewOrders: {orders}{CLR}\nMoreOps: {orders}{CLR}")
   print(f"{CLR}asdfOrders: {orders}")
   time.sleep(random.uniform(0.5, 2))
