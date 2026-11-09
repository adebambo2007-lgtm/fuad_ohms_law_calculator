# Ohm's Law and Power Calculator
# Finds voltage, current, resistance or power from two known values.
# My own twist: the program keeps a history of every answer in the session,
# shows it on request, and warns when the power is dangerously high.

POWER_WARNING_LIMIT = 100  # watts; above this we print a safety warning

history = []  # list that stores every calculation done in this session


def get_number(prompt):
    """Keep asking until the user types a valid number (float)."""
    while True:
        text = input(prompt)
        try:
            return float(text)  # convert the typed text to a decimal number
        except ValueError:
            print("That is not a number. Please type digits only, e.g. 12 or 0.5")


def get_positive(prompt):
    """Keep asking until the user types a number greater than zero."""
    while True:
        value = get_number(prompt)
        if value > 0:
            return value
        print("The value must be greater than zero (this also avoids dividing by zero).")


def save_result(text):
    """Print a result and store it in the history list."""
    print("Answer:", text)
    history.append(text)


def check_power(power):
    """Twist: warn the user if the power is above the safe limit."""
    if power > POWER_WARNING_LIMIT:
        print(f"WARNING: {power:.2f} W is above {POWER_WARNING_LIMIT} W. "
              "Check that your components can handle this power!")


def show_menu():
    print("\n--- Ohm's Law and Power Calculator ---")
    print("1. Find voltage (V = I x R)")
    print("2. Find current (I = V / R)")
    print("3. Find resistance (R = V / I)")
    print("4. Find power (P = V x I)")
    print("5. Show history")
    print("6. Quit")


def main():
    running = True
    while running:  # the program repeats until the user quits
        show_menu()
        choice = input("Choose 1-6: ").strip()

        if choice == "1":
            current = get_number("Current in amps (A): ")
            resistance = get_number("Resistance in ohms (ohm): ")
            voltage = current * resistance
            save_result(f"V = {current} A x {resistance} ohm = {voltage:.4g} V")
        elif choice == "2":
            voltage = get_number("Voltage in volts (V): ")
            resistance = get_positive("Resistance in ohms (ohm): ")  # cannot be 0
            current = voltage / resistance
            save_result(f"I = {voltage} V / {resistance} ohm = {current:.4g} A")
        elif choice == "3":
            voltage = get_number("Voltage in volts (V): ")
            current = get_positive("Current in amps (A): ")  # cannot be 0
            resistance = voltage / current
            save_result(f"R = {voltage} V / {current} A = {resistance:.4g} ohm")
        elif choice == "4":
            voltage = get_number("Voltage in volts (V): ")
            current = get_number("Current in amps (A): ")
            power = voltage * current
            save_result(f"P = {voltage} V x {current} A = {power:.4g} W")
            check_power(abs(power))
        elif choice == "5":
            if len(history) == 0:
                print("No calculations yet.")
            else:
                for number, line in enumerate(history, start=1):
                    print(f"{number}. {line}")
        elif choice == "6":
            print("Goodbye!")
            running = False
        else:
            print("Invalid choice. Please type a number from 1 to 6.")


main()
