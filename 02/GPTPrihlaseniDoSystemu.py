user = input("Zadej uživatelské jméno: ")
if user == "":
    print("Toto pole musíš vyplnit!")
elif user != "admin":
    print("Neznámý uživatel.")
else:
    user == "admin"
    passwd = input("Zadej heslo: ")
    if passwd == "tajne123":
        print("Vítej, administrátore.")
    else:
        print("Nesprávné heslo.")
