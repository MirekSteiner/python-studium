from random import randrange

start = 0
print("Tvoje body: ", start)
odpoved = input("Chcanoeš pokračovat? ")
if odpoved == "ne":
    print("KONEC HRY")
elif odpoved == "ano":
    a = print("Další karta je: ", randrange(2,10))
    body = start + a
    print("Tvoje nové body jsou: ", body)
else:
    print("KONEC HRY")



