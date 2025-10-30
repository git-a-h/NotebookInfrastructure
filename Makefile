report-type=html

.PHONY: test 

test: 
	pytest --cov --cov-report=html tests

show-coverage:
	open htmlcov/index.html