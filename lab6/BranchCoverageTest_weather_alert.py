import pytest
from weather_alert import wind_alert, rain_alert, heat_alert, overall_alert


@pytest.mark.parametrize(("speed", "expected"), [
    (38.99, "none"), (39, "advisory"), (61.99, "advisory"),
    (62, "watch"), (88.99, "watch"), (89, "warning"),
])
def test_wind_branches(speed, expected):
    assert wind_alert(speed) == expected


@pytest.mark.parametrize(("rain", "saturated", "expected"), [
    (9.99, False, "none"), (10, False, "advisory"), (10, True, "watch"),
    (49.99, False, "advisory"), (49.99, True, "watch"),
    (50, False, "watch"), (50, True, "warning"),
])
def test_rain_branches(rain, saturated, expected):
    assert rain_alert(rain, saturated) == expected


@pytest.mark.parametrize(("temp", "humidity", "expected"), [
    (34.9, 40, "none"), (35, 40, "advisory"), (39.9, 40, "advisory"),
    (40, 40, "watch"), (44.9, 40, "watch"), (45, 40, "warning"),
    (39, 50, "watch"), (34, 60, "advisory"), (34, 49, "none"),
])
def test_heat_branches(temp, humidity, expected):
    assert heat_alert(temp, humidity) == expected


def test_overall_branches_and_unknown():
    assert overall_alert([]) == "none"
    assert overall_alert(["none"]) == "none"
    assert overall_alert(["advisory", "watch"]) == "watch"
    assert overall_alert(["watch", "advisory"]) == "watch"
    assert overall_alert(["warning", "none"]) == "warning"
    with pytest.raises(ValueError, match="unknown alert"):
        overall_alert(["storm"])
