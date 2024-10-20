is_year_leap = int (input("Ведите год:"))

if is_year_leap % 4 != 0:
    print ("Год обычный!")

elif is_year_leap % 100 == 0:
    if is_year_leap % 400 == 0:
        print("Год Високосный!")
    else:
        print ("Год обычный!")
else:
    print("Год Високосный!")

