## Vision-Box job Application Process

Display of short FE Automation project, for recruitment process purposes
(other than this, All rights reserved)

### Index
1. Requirements and Assumptions/Other thoughts
2. Demo Framework Specifications
3. Installation
4. Use
5. Notes

### 1. Requirements and Assumptions
#### 1.1 Requirements and Assumptions
- Test execution machine OS: Windows
- Power Shell (used for: creation of venv, activation of venv, triggering the installation of dependencies)
- Latest Python installed
- Python in PATH, as expected (installation step).
- git bash or equivalent is usable.

- This Demo was created assuming possibility to execute Powershell scripts, as described below in the Installation and Use sections
- IF working with VS Code, to view and run, careful that there have been some known issues with the PowerShell extension working with Python venvs! Also refer to the Installation section below.

### 2. Demo Framework Specifications

- Selenium 4
- running on Python,
- using Pytest
- Pytest-BDD for Cucumber TC parsing
- using venv for virtual environment (separation between host and execution environment)
- Multi-browser (Chrome and Firefox)
- Webdriver (remote Chrome and Fire) Selenoid (http://localhost:4444) with UI (http://localhost:8080) for realtime viewing of execution and video capture
- Execution videos downloaded from Selenoid to local machine. Video URL provided in console.
- currently, cucumber.json reporting
- Faker library integrated for some random test data as desired.

## 3. Installation

### Installation
In a Powershell CLI, inside the project folder, run the setup_framework.ps1 script.
This will automatically:
    - create the Python venv
    - install required dependencies
    - call the selenoid setup python script, which will
        . download arekube's content management tool (cm.exe)
        . run required commands for Selenoid setup , Selenoid-UI, Selenoid video capture and Selenoid remote browsers (as per browsers.json config file)

And you should be good to go inside a virtual environment, segregated from the host system.



## 4. Use

(default)
```python -m pytest```

will use local machine chrome headed.

Some switches/ flags have been included.

```--browser chrome``` 
aceepts: firefox or chrome

```--headless``` 
will trigger headless browser execution

```--remote```
will trigger remote execution, with video download

Example combining custom and out-of-the-box possibilities:

```python -m pytest --remote --browser firefox --cucumberjson= .\reports --gherkin-terminal-reporter .\features\report```

```python -m pytest tests/step_definitions/test_login.py::test_testing_login -v -s --remote --full-trace --exitfirst```

```python -m pytest tests/step_definitions/test_checkout_your_information.py -v -s --remote --browser chrome --json-report --json-report-file reports/report.json```

```python -m pytest tests/step_definitions/test_checkout_your_information.py -v -s --remote --full-trace --exitfirst --json-report --json-report-file reports/report.json```


## 5. Notes and other thoughts

***They don't theach this in Law School...*** :-)

Selenoid uses the _browsers.json_ to setup the available browser webdrivers. 
Currently: latest Chrome and latest Firefox.

Improval points:

- Friendlier video naming;
- possibility for remote + headless
- revisit locator strategy

Future explorations!

Jira/Xray integration through REST API.

    https://pypi.org/project/pytest-jira-xray/
    (testcases are marked as per JIRA XRAY test ID or list of IDs)

Visual Regression Testing

    https://pypi.org/project/pixelmatch/
    (establish a baseline and run against it. Update baseline as per sanctioned ui changes)
    
- I imagine assuming as target that one day installation triggered and dependencies installed via a Pipeline e.g. Jenkins. Hence Selenoid containerized. 
- Aditionally, a script could import the relevant Cucumber Test cases from Jira/Xray (or other...)
- A report file would be exported into Jira/Xray at the end of the execution. See Notes for possible library for this goal
- Possible next step also includes Visual Regression Testing.
