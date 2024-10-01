install:
	poetry install
	poetry build
	python3 -m pip install --force-reinstall --user dist/*.whl
	poetry publish --dry-run

uninstall:
	python3 -m pip uninstall -y hexlet-code
	rm -rf ../python-project-49/

brain-games:
	poetry run brain-games

lint:
	poetry run flake8 brain_games
