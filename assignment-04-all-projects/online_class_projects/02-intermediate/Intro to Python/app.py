
gravity_of_all_planets = {
    "Mercury": 37.6,
    "Venus": 88.9,
    "Mars": 37.8,
    "Jupiter": 236.0,
    "Saturn": 108.1,
    "Uranus": 81.5,
    "Neptune": 114.0,
}

gravity=None

def planetary_weight_calculator():

    # Weight On Earth
    try:
        earth_weight = int(input("Enter a weight on earth"))
    except ValueError:
        print("Please enter a valid number ")

    # Planet Name
    planet = input("Enter a planet").capitalize()
    print(planet)

    # Planets Gravity
    if planet == "Mercury":
        gravity = gravity_of_all_planets["Mercury"]
    elif planet == "Venus":
        gravity = gravity_of_all_planets["Venus"]
    elif planet == "Mars":
        gravity = gravity_of_all_planets["Mars"]
    elif planet == "Jupiter":
        gravity = gravity_of_all_planets["Jupiter"]
    elif planet == "Saturn":
        gravity = gravity_of_all_planets["Saturn"]
    elif planet == "Uranus":
        gravity = gravity_of_all_planets["Uranus"]
    elif planet == "Neptune":
        gravity =  gravity_of_all_planets["Neptune"]
    else:
        print("Invalid planet name. Please enter a valid planet.")

    
    # Calculation 
    planetary_weight = earth_weight * gravity / 100
    rounded_planetary_weight = round(planetary_weight, 2)
    print(f"The equivalent weight on {planet}: {rounded_planetary_weight}")


planetary_weight_calculator()