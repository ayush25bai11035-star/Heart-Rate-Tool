# Graphical Representation
import matplotlib.pyplot as plt

def graph(times, rates):
    plt.figure()
    plt.plot(times, rates, marker="o")
    plt.title("Heart Rate vs Time")
    plt.xlabel("Time of Measurement")
    plt.ylabel("Heart Rate (bpm)")
    plt.show()
