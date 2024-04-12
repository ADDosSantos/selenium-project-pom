# selenium-project-pom
Python + Selenium 4 exercising Page Object Model


using Faker for random test data.

usage example

(default)
python -m pytest --browser chrome .\tests\test_01_login.py 

###
python -m pytest --remote --browser firefox --cucumberjson= .\reports --gherkin-terminal-reporter .\features

python -m pytest --remote --browser chrome --headless .\tests\test_01_login.py

