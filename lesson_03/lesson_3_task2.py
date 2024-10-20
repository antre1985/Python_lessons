from lesson_03.Smartphone import Smartphone

catalog = []
phone1 = Smartphone("One_plus" , "Pro_11" , "+79393475639")
phone2 = Smartphone("Apple" , "Iphone_11" , "+79273294542")
phone3 = Smartphone("Xiaomi" , "Mi_9" , "+79234034858")
phone4 = Smartphone("Samsung" , "S_23" , "+79996999999")
phone5 = Smartphone("Vivo" , "S_9" , "+79212112345")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand}  {phone.model}  {phone.number_phone}")