# Analysis
Safe_low = 60
Safe_high = 100

def heart_rate(rates):
    average_heart_rate = sum(rates) / len(rates)
    minimum = min(rates)
    maximum = max(rates)

    is_safe = Safe_low <= average_heart_rate <= Safe_high

    return {
        "average": average_heart_rate,
        "min": minimum,
        "max": maximum,
        "is_safe": is_safe,
    }
