# Lab 6 Coverage Analysis

**Student:** PES2UG24CS593  
**Application:** Weather alert classifier  
**Repository:** [SELab6](https://github.com/vishnu-1107-cloud/SELab6)

## Code coverage

The code coverage suite exercises wind, rain, heat, and overall alert classification, including threshold values and invalid alert input. The test run passed all 4 tests. Coverage measured against `weather_alert.py` was **100% line coverage**: 38 statements, 0 missed.

Command:

```text
python -m coverage run --source=weather_alert -m pytest -q CodeCoverageTest_weather_alert.py
python -m coverage report -m weather_alert.py
```

## Branch coverage

The branch suite tests outcomes on both sides of each decision, including all alert thresholds, saturated and unsaturated rain cases, humidity adjustment, and valid and invalid overall alerts. The test run passed all 23 cases. Coverage measured against `weather_alert.py` was **100% branch coverage**: 28 branches, 0 partial branches, and 0 missed statements.

Command:

```text
python -m coverage run --branch --source=weather_alert -m pytest -q BranchCoverageTest_weather_alert.py
python -m coverage report -m weather_alert.py
```

## Evidence files

- `code_coverage_terminal.png` and `code_coverage_terminal.txt` show the line coverage run and report.
- `branch_coverage_terminal.png` and `branch_coverage_terminal.txt` show the branch coverage run and report.
- `CodeCoverageTest_weather_alert.py` and `BranchCoverageTest_weather_alert.py` contain the respective test suites.
