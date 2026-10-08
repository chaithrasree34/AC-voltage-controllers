# AC-voltage-controllers
print("Single-Phase AC Voltage Controller")

Vs = float(input("Enter supply RMS voltage (V): "))
alpha = float(input("Enter firing angle α (degrees): "))

if Vs <= 0:
    print("Supply voltage must be greater than zero.")

elif alpha < 0 or alpha > 180:
    print("Firing angle must be between 0 and 180 degrees.")

else:
    # Convert firing angle to radians
    a = math.radians(alpha)

    # Calculate RMS output voltage
    Vo = Vs * math.sqrt(
        (1 / math.pi) *
        (math.pi - a + (math.sin(2 * a) / 2))
    )

    print("\n--- AC Voltage Controller Results ---")
    print("Supply Voltage =", Vs, "V")
    print("Firing Angle =", alpha, "degrees")
    print("Output RMS Voltage =", round(Vo, 2), "V")

    if alpha == 0:
        print("Controller Status: Maximum output voltage")
    elif alpha < 90:
        print("Controller Status: Partial voltage control")
    else:
        print("Controller Status: Low output voltage")
