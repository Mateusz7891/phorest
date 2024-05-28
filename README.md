In order to run the tests, you need to have:
a) Python 3.10 (or later)
b) Playwright
c) Pytest
d) PIP
e) Virtual environment

Some of these dependencies can be installed through the requirements file:

pip install -r requirements.txt
This way, everyone will have the same versions.

To run tests:
1) You can do it via PyCharm (or other IDE)
2) You can do it from command line example:
    "pytest tests/send_to_someone_else_test.py" will run "send_to_someone_else_test"