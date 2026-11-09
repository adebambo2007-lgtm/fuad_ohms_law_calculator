# Ohm's Law and Power Calculator

## What it does
A menu program that finds voltage, current, resistance or power from two known values and prints the answer with units. It repeats until the user chooses Quit.

## How to run it
Install Python 3, then run: `python ohms_law.py`

## Sample output
```
Choose 1-6: 4
Voltage in volts (V): 230
Current in amps (A): 2
Answer: P = 230.0 V x 2.0 A = 460 W
WARNING: 460.00 W is above 100 W. Check that your components can handle this power!
```

## My own twist
The program keeps a history of every answer in the session (menu option 5), and warns when the power is above 100 W.

## What I learned
Check input before using it: typing a letter or a zero used to crash the program, so I added input checks and a rule that resistance and current cannot be zero when dividing.

## Author
Faisal Ali-Adebambo, ND1 Mechatronics Engineering, YabaTech.
