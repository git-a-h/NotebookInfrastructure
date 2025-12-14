# TODOs

This is the outline for the Winter of Code project for setting up notebook tutorial infrastructure for pySDC.
This is not set in stone and there is no need to do these steps in this order. This should serve as a guideline that can be updated during the project.

For the first two tasks, the pySDC repository can serve as a reference. Ultimately, the goal is to implement what is developed here into pySDC. Copying from there is not a bad idea, but make sure to understand what you copy.


## Task 1: Familiarize yourself with the local testing environment
 - [x] Set up an empty virtual environment with micromamba. Add all dependencies you subsequently need to an environment file to make future setup seamless.
 - [x] Set up a toy code that needs testing and a tutorial. This should be simple. For instance, just a basic add function.
 - [x] Set up a unit test for the code using pytest. E.g. does 1+1=2? 
 - [x] Generate a coverage report for the toy code

## Task 2: Familiarize yourself with GitHub Continuous Integration (CI)
 - [x] Create a GitHub workflow
 - [x] Create a task in the workflow that ...
  - [x] is triggered on push and pull requests
  - [x] initializes a virtual environment with micromamba, replicating your local environment
  - [x] runs the pytest unit tests
  - [x] creates an artifact with a coverage report

## Task 3: Familiarize yourself with notebooks
 - [x] Look for alternatives to Jupyter notebooks for interactive testing. Have a look at the Firedrake repository. What are pros and cons of various approaches? Do this before committing to notebooks. Subsequently, "notebook" will refer to whatever proved to be best. **Winner (preliminary): [Jupytext](https://github.com/mwouts/jupytext)**
 - [x] Write a tutorial for your toy code in a python file that includes an equation, some code, and a plot
 - [x] Generate a jupyter notebook from the python file using Jupytext which shows the output of the code. Do not check the notebook into git. We only want the plain text python file in version control.

## Task 4: Write local tests for notebooks
 - [x] Write an automatable smoke test for the tutorial. Try simply importing the tutorial python file, which should run all code in that file, in a test.

## Task 5: Implement the notebook tests in the GitHub CI
 - [x] Add a task running the tutorial tests in parallel to the unit tests
 - [x] Create an artifact with the merged coverage report
 - [x] Write a script / command that scans a directory for .py files with prefix notebook*.py 
 - [x] Generate the notebooks in CI and output them as an artifact

## Task 6: Add MPI parallelism
 - [ ] Add a parallel module to your toy code. E.g. parallel sum
 - [ ] Test locally using multiple MPI ranks
 - [ ] Implement parallel unit test in GitHub CI 
 - [ ] Figure out a way to run the notebook tests in parallel
 - [ ] Write parallel smoke test for the notebook
 - [ ] Implement parallel notebook tests in GitHub CI
 - [ ] Merge all coverage reports (Serial and parallel unit and notebook tests) into a single artifact
