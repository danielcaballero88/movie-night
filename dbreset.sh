#!/usr/bin/env bash

rm -rf ./migrations/
rm ./movie_night/movie_night_dev.sqlite3

flask db init 
flask db migrate 
flask db upgrade

