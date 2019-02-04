coverage erase
pytest --cov=notipy --cov-report xml:coverage.xml ./tests/
coverage combine --append
coverage report
coverage xml
#coveralls