## This is the Documentation for step_1
For this task, one needs a src and test directory. The src dir contains function definition and the test dir the corresponding test suite. For running the test, the following commands needs be prompted into the active micromamba environment:
- pytest --cov --cov-report=html tests

The test coverage will be saved under a 'htmlcov' directory, in which one can view the coverage by opening the index.html file. A possible command on MacOS could be:

- open htmlcov/index.html


