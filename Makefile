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

# build:
# 	poetry build

# package-install:
# 	python3 -m pip install --force-reinstall --user dist/*.whl

# publish:
# 	poetry publish --dry-run

lint:
	poetry run flake8 brain_games
