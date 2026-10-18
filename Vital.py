print("Vital Signs Checker (adult, for learning only)")

heart_rate = int(input("Heart rate (beats per minute): "))
temperature = float(input("Temperature (C): "))
oxygen = int(input("Oxygen level (%): "))

print()

# Heart rate
if heart_rate < 60:
    print("Heart rate: LOW")
elif heart_rate <= 100:
    print("Heart rate: normal")
else:
    print("Heart rate: HIGH")

# Temperature
if temperature < 36.1:
    print("Temperature: LOW")
elif temperature < 38:
    print("Temperature: normal")
else:
    print("Temperature: FEVER")

# Oxygen
if oxygen >= 95:
    print("Oxygen: normal")
elif oxygen >= 90:
    print("Oxygen: LOW")
else:
    print("Oxygen: VERY LOW, get medical help")
