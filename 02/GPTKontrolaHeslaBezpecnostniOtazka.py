user = input("Zadej uživatelské jméno:")
passwd = input("Zadej heslo:")
if user == "kralkralu" and passwd == "heslo123":
    keyword = input("Znáš tajné slovo? (ano/ne)")
    if keyword == "ano":
        print("Vítej, králi!")
    else:
        print("Přístup zamítnut.")
else:
    print("Neplatné přihlašovací údaje.")
