install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:	
	find ./codes -type f -name "*.py" -exec black {} \;
	find ./codes -type f -name "*.ipynb" -exec nbqa black {} \;
		 
lint:
	find ./codes -type f -name "*.py" -exec ruff check {} \;
	find ./codes -type f -name "*.ipynb" -exec nbqa ruff {} \;

test:
	python -m pytest -vv --cov=codes/project_codes codes/test_codes/*.py
	python -m pytest --nbval codes/project_codes/*.ipynb 

all : install test format lint 
