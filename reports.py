# Reports
Safe_low = 60
Safe_high = 100
def report(times, rates, analysis):
    print("Heart Rate Analysis Report")
    print("Readings:")
    for t, r in zip(times, rates):
        print(f"Time: {t} | Heart Rate: {r} bpm")

    print("\nSummary:")
    print(f"Minimum heart rate: {analysis['min']:.1f} bpm")
    print(f"Maximum heart rate: {analysis['max']:.1f} bpm")
    print(f"Average heart rate: {analysis['average']:.1f} bpm")
    print(f"Safe range: {Safe_low}-{Safe_high} bpm")

    if analysis["is_safe"]:
        print("Status: Safe")
        print("Your average heart rate is in the normal range.")
        print("Good for you")
    else:
        print("Your average Heart rate is out of normal range")
        print("Status:Unsafe. Consult A Doctor ")