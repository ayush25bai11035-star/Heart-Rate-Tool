# Importing data from different python files
from readings import readings
from analysis import heart_rate, Safe_low, Safe_high
from reports import report
from graph import graph

def main():
    print("Heart Rate Analyzing Tool")
    times, rates = readings(num=5)
    analysis = heart_rate(rates)
    report(times, rates, analysis)
    graph(times, rates)

if __name__ == "__main__":
    main()