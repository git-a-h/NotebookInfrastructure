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
 - [ ] Create a GitHub workflow
 - [ ] Create a task in the workflow that ...
  - [ ] is triggered on push and pull requests
  - [ ] initializes a virtual environment with micromamba, replicating your local environment
  - [ ] runs the pytest unit tests
  - [ ] creates an artifact with a coverage report

## Task 3: Familiarize yourself with notebooks
 - [ ] Look for alternatives to Jupyter notebooks for interactive testing. Have a look at the Firedrake repository. What are pros and cons of various approaches? Do this before committing to notebooks. Subsequently, "notebook" will refer to whatever proved to be best.
 - [ ] Write a tutorial for your toy code in a notebook

## Task 4: Write local tests for notebooks
 - [ ] Find a framework for automating tests in notebooks. Ideally, a pytest plugin or an alternative to pytest.
 - [ ] Write an automatable smoke test for the tutorial.
 - [ ] Create a coverage report for the tutorial notebook
 - [ ] Merge the coverage reports of the tutorial tests and the unit tests

## Task 5: Implement the notebook tests in the GitHub CI
 - [ ] Add a task running the notebook tests in parallel to the unit tests
 - [ ] Create an artifact with the merged coverage report

## Task 6: Add MPI parallelism
 - [ ] Add a parallel module to your toy code. E.g. parallel sum
 - [ ] Test locally using multiple MPI ranks
 - [ ] Implement parallel unit test in GitHub CI 
 - [ ] Figure out a way to run the notebook tests in parallel
 - [ ] Write parallel smoke test for the notebook
 - [ ] Implement parallel notebook tests in GitHub CI
 - [ ] Merge all coverage reports (Serial and parallel unit and notebook tests) into a single artifact
