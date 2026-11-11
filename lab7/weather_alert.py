"""Parse and classify weather readings with defensive input validation."""

import math
import re


def parse_reading(text):
    """Return ``(temperature, humidity)`` or None for an invalid reading.

    Readings use the form ``temperature/humidity``. Temperature must be a
    finite number and humidity must be an integer percentage from 0 to 100.
    """
    if not isinstance(text, str) or text.count("/") != 1:
        return None

    temp_text, humidity_text = (part.strip() for part in text.split("/"))
    if not temp_text or not re.fullmatch(r"[+-]?\d+", humidity_text):
        return None

    try:
        temperature = float(temp_text)
        humidity = int(humidity_text)
    except (ValueError, OverflowError):
        return None

    if not math.isfinite(temperature) or not 0 <= humidity <= 100:
        return None
    return temperature, humidity

def wind_category(speed_text):
    """Classify a nonnegative integer wind speed; invalid values mean none."""
    if isinstance(speed_text, bool):
        return 'none'
    if isinstance(speed_text, int):
        speed = speed_text
    elif isinstance(speed_text, str) and re.fullmatch(r"\+?\d+", speed_text.strip()):
        try:
            speed = int(speed_text.strip())
        except (ValueError, OverflowError):
            return 'none'
    else:
        return 'none'

    if speed < 0:
        return 'none'
    if speed >= 89:
        return 'warning'
    if speed >= 39:
        return 'advisory'
    return 'none'

def rainfall_spread(readings_csv):
    """Return max minus min for nonnegative finite CSV readings, else None."""
    if not isinstance(readings_csv, str) or not readings_csv.strip():
        return None

    parts = [part.strip() for part in readings_csv.split(',')]
    if any(not part for part in parts):
        return None
    try:
        readings = [float(part) for part in parts]
    except (ValueError, OverflowError):
        return None
    if any(not math.isfinite(reading) or reading < 0 for reading in readings):
        return None
    return max(readings) - min(readings)

def main():
    print("==== Running parse_reading ====")
    user_input = input("Enter temperature/humidity (e.g. 35.5/80): ")
    result = parse_reading(user_input)
    print("Temperature and Humidity:", result if result is not None else "Invalid reading")

    print("\n==== Running wind_category ====")
    user_input = input("Enter a wind speed in km/h (e.g. 45): ")
    result = wind_category(user_input)
    print("Wind Category:", result)

    print("\n==== Running rainfall_spread ====")
    user_input = input("Enter hourly rainfall in mm as CSV (e.g. 2,5.5,10): ")
    result = rainfall_spread(user_input)
    print("Rainfall Spread:", result if result is not None else "Invalid rainfall readings")

if __name__ == "__main__":
    main()
