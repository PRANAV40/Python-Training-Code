''' Problem1:
Create a function that takes damage and speed (attacks per second) and returns the amount of damage after a given time.
Examples
damage(40, 5, "second") ➞ 200
damage(100, 1, "minute") ➞ 6000
damage(2, 100, "hour") ➞ 720000
'''
def calculate_total_damages(damage, speed, time_unit):
    time_conversion = {"second": 1, "minute": 60, "hour": 3600}

    if time_unit not in time_conversion:
        return "Invalid Time Unit! Please enter right time_uit"
    times = time_conversion[time_unit]
    total_damages = damage * speed * times

    return total_damages


damages = int(input("Enter the damage: "))
speeds = int(input("Enter the speed: "))
time_units = str(input("Enter the time units: "))
print("damage(", damages, ",", speeds, ",", '"', time_units, '"'  ")->",
      calculate_total_damages(damages, speeds, time_units), end="")
