# Readings from user
def readings(num=5):
    times = []
    rates = []

    print(f"Enter {num} heart rate readings with the time.")
    for i in range(1, num + 1):
        print(f"Reading {i}")
        time = input("Enter time: ")
        while True:
            try:
                hr = float(input("Enter heart rate: "))
                if hr <= 0:
                    print("Heart rate should be positive.")
                    continue
                break
            except ValueError:
                print("Invalid")
        times.append(time)
        rates.append(hr)
        print()
    return times, rates