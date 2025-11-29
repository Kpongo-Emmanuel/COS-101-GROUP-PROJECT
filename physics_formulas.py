print("Welcome to the Physics Calculator, Please select your choice of formula from a to e")
print('a -- force\nb -- work done\nc -- velocity\nd -- density\ne -- power')
while True:
    y = input("what formula would you like to use?")

    if y == "a" :
        print('you have chosen Force')
        mass = float(input("what is your mass in Kg?"))
        acceleration: float = float(input("what is your acceleration in m/s^2?"))
        print(mass * acceleration, "m/s^2")

    elif y == "b" :
        print('you have chosen work done')
        force = float(input("what is your force in Newton?"))
        distance = float(input("what is your distance in m"))
        print(force * distance, "m")


    elif y == "c" :
        print('you have chosen velocity')
        v = float(input("what is your displacement in m?"))
        g = float(input("what is your time in seconds?"))
        print(v / g, "m/s")

    elif y == "d" :
        print('you have chosen density')
        mass = float(input("what is your mass in kg?"))
        volume = float(input("what is your volume in m^3?"))
        print(mass * volume, "m^3")

    elif y == "e" :
        print('you have chosen power')
        work_done = float(input("what is your work done in Joules?"))
        time = float(input("what is your time in seconds?"))
        print(work_done / time, "W")

    else :
        print('please select a correct choice')














