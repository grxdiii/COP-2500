# Gradi Tshielekeja Mbuyi
# COP 2500C
# Sep 26 2021
# Assignment #3: Line Plotter

# inputs for plotter
delay = int(input("Enter the per delay: "))
time = int(input("Enter the time off work: "))
process = int(input("Enter the number of delays in our table: "))

# looping "process" amount of time
for i in range(process):
    print("Delay #", i, ", Time = ", time, sep="")
    time = time + delay
