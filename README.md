# selenium-project-pom
Python + Selenium 4 exercising Page Object Model


using Faker for random test data.

usage example

(default)
python -m pytest --browser chrome .\tests\test_01_login.py 

###
python -m pytest --remote --browser firefox --cucumberjson= .\reports --gherkin-terminal-reporter .\features

python -m pytest --remote --browser chrome --headless .\tests\test_01_login.py

pytest tests/step_definitions/test_login.py -v -s

pytest tests/step_definitions/test_login.py::test_testing_login -v -s --headless --full-trace --exitfirst

pytest tests/step_definitions/test_checkout_your_information.py -v -s --remote --full-trace --exitfirst

pytest tests/step_definitions/test_checkout_your_information.py -v -s --remote --full-trace --exitfirst --json-report --json-report-file reports/report.json