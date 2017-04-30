# DonorsChoose_Visualization
# Completed as initial data vizualization project for The Data Incubator week 5.

# Visit the interactive dashboard here: https://donorschoosedashboard.herokuapp.com/

## Getting started

The dependencies for the project can be installed (in your virtual environment, venv) using

    $ pip install -r requirements.txt

You can use ``Vagrant`` to start a machine with a MongoDB instance running

    $ vagrant up

To initialize the database you need to download the data

    $ wget http://s3.amazonaws.com/open_data/opendata_projects000.gz


and import it after gunzip

    $ mongoimport -d donorschoose -c projects --type csv --file /vagrant/opendata_projects.csv -headerline
