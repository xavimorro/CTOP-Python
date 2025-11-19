edad = int(input("introduce tu edad: "))

try:

    if edad < 18:
        print(f"Eres menor de edad, tienes {edad} años.")
    elif edad >= 18 & edad <= 64:
        print(f"Eres adulto, tienes {edad} años.")
    else:
        print(f"Eres mayor, tienes {edad} años.")
except ValueError as e:
    print("Error, " + e)