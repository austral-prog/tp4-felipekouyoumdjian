def leap_year():

    YEAR = int(input("Ingrese un año: "))
    
    if YEAR % 4 == 0 and YEAR % 100 != 0 or YEAR % 400 == 0:
        print(f"El año {YEAR} es bisiesto")
    else:
        print(f"El año {YEAR} no es bisiesto")