"""Property-based tests for the weather alert input validators."""

import math

from hypothesis import given, strategies as st

from weather_alert import parse_reading, rainfall_spread, wind_category


@given(st.one_of(st.text(), st.none()))
def test_parse_reading_handles_arbitrary_input(value):
    """Malformed readings are rejected with None, never an exception."""
    result = parse_reading(value)
    assert result is None or (
        isinstance(result, tuple)
        and len(result) == 2
        and math.isfinite(result[0])
        and isinstance(result[1], int)
        and 0 <= result[1] <= 100
    )


@given(
    st.floats(allow_nan=False, allow_infinity=False, width=32),
    st.integers(min_value=0, max_value=100),
)
def test_parse_reading_preserves_valid_values(temperature, humidity):
    result = parse_reading(f"{temperature}/{humidity}")
    assert result is not None
    assert math.isclose(result[0], temperature, rel_tol=1e-6, abs_tol=1e-6)
    assert result[1] == humidity


@given(st.one_of(st.text(), st.none()))
def test_wind_category_handles_arbitrary_input(value):
    result = wind_category(value)
    assert result in {"none", "advisory", "warning"}


@given(st.integers(min_value=0, max_value=100_000))
def test_wind_category_uses_documented_thresholds(speed):
    expected = "warning" if speed >= 89 else "advisory" if speed >= 39 else "none"
    assert wind_category(str(speed)) == expected


def test_wind_category_rejects_extremely_long_integer_text():
    assert wind_category("9" * 5000) == "none"


@given(st.one_of(st.text(), st.none()))
def test_rainfall_spread_handles_arbitrary_input(value):
    result = rainfall_spread(value)
    assert result is None or (math.isfinite(result) and result >= 0)


@given(
    st.lists(
        st.floats(min_value=0, allow_nan=False, allow_infinity=False, width=32),
        min_size=1,
    ),
)
def test_rainfall_spread_matches_range(readings):
    result = rainfall_spread(",".join(map(str, readings)))
    assert result is not None
    assert math.isclose(result, max(readings) - min(readings), rel_tol=1e-6, abs_tol=1e-6)
