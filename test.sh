coverage erase
pytest --cov=notipy_me --cov-report xml:coverage.xml ./tests/
coverage combine --append
coverage report
coverage xml
#coveralls