sudo apt-get update
sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
sudo su - postgres
# After logging in enter these commands
# psql
# CREATE DATABASE library_buddy;
# CREATE USER op3ntrap WITH password 'a';
# ALTER ROLE op3ntrap SET client_encoding TO 'utf8';
# ALTER ROLE op3ntrap SET default_transaction_isolation TO 'read committed';
# ALTER ROLE op3ntrap SET timezone TO 'UTC+5:30';
# GRANT ALL PRIVILEGES ON DATABASE myproject TO op3ntrap;
# \q
# exit
