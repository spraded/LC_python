engine_indicator_light = "not red blinking"
space_suits_on = True
shuttle_cabin_ready = True
crew_status = space_suits_on and shuttle_cabin_ready
computer_status_code = 200
fuel_level = 25000
engine_temperature = 2500
command_override = False
spacecraft_speed = int(input("Enter the spacecraft speed: "))

#Part B: Safety checks
if crew_status:
   print("Crew Ready")
else: 
   print("Crew Not Ready")

if computer_status_code == 200:
   print("Please stand by. Computer is rebooting.")
elif computer_status_code == 400:
   print("Success! Computer online.")
else:
   print("ALERT: Computer offline!")

if spacecraft_speed > 17500:
   print("ALERT: Escape velocity reached!")
elif spacecraft_speed < 8000:
   print("ALERT: Cannot maintain orbit!")
else:
   print("Stable speed.")

# Part C: Fuel status
if fuel_level < 1000 or engine_temperature > 3500 or engine_indicator_light == "red blinking":
   print("ENGINE FAILURE IMMINENT!")
elif fuel_level <= 5000 or engine_temperature > 2500:
   print("ALERT: Check fuel level and engine temperature.")
elif fuel_level > 20000 and engine_temperature <= 2500:
   print("Full tank. Engines good.")
elif fuel_level > 10000 and engine_temperature <= 2500:
   print("Fuel level above 50%. Engines good.")
elif fuel_level > 5000 and engine_temperature <= 2500:
   print("Fuel level above 25%. Engines good.")
else:
   print("Fuel and engine status pending...")

#Extra: Command override

if command_override:
   print("Command override enabled. Cleared to launch.")
else:
   if fuel_level > 20000 and engine_temperature != "red blinking":
      print("Cleared to launch!")
   else:
      print("Launch scrubbed!")