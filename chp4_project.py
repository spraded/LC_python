date = "Monday 2019-03-18"
time = "10:05:34 AM"
average_astronaut_mass_kg = 80.7
fuel_mass_kg = 760000
ship_mass_kg = 74842.31
fuel_level = "100%"
dashes = ("-" * 20)

# Prompt the user for the number of astronauts and the crew status:
number_of_astronauts = float(input("Enter the number of astronauts in the crew between 1 and 7. "))
crew_status = input("Enter the crew status: Ready or Not Ready. ")

# Code your mass calculations here:
total_crew_mass = (number_of_astronauts * average_astronaut_mass_kg)
total_ship_mass = (total_crew_mass + ship_mass_kg + fuel_mass_kg)

# Display the checklist:
print(dashes)
print("> LAUNCH CHECKLIST")
print(dashes)
print("Date:", date)
print("Time:", time, "\n")
print(dashes)
print("> SHIP INFO")
print(dashes)
print("* Crew:", int(number_of_astronauts))
print("* Crew Status:", crew_status)
print("* Fuel Level:", fuel_level, "\n")
print(dashes)
print("> MASS DATA")
print(dashes)
print("* Crew:", total_crew_mass)
print("* Fuel", fuel_mass_kg)
print("* Spaceship:", ship_mass_kg)
print("* Total mass:", total_ship_mass)
