# Pytest full-featured example

Install and run:

```
pip install pytest pytest-instafail pytest-cov pytest-html

pytest -s --cov-report html:reports/coverage --cov=mymath --instafail --html=reports/main/report.html .
```

Explanation:

`-s` - output print() results

`--cov-report html:reports/coverage --cov=mymath` - analyze coverage of `mymath` module and outpur html report to `reports/coverage` dir

`--html=reports/main/report.html` - output test run HTML report to `reports/main/report.html`

`--instafail` - if test fails, output it immediately, dont wait until test ends


