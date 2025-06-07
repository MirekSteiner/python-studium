vek = int(input("Kolik Ti je let? "))
vip = input("Máš VIP kartu? (ano/ne) ")
host = input("Jsi v seznamu čestných hostů? (ano/ne) ")
if (vek >= 21 and vip == "ano") or host == "ano":
    print("Vítej ve VIP klubu!")
else:
    print("Nemáš přístup do VIP klubu.")
