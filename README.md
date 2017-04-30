# Donors Choose Visualization - Interactive Dashboard

# Visit the interactive dashboard here: https://donorschoosedashboard.herokuapp.com/

## Background

This repository contains a clone of the repo used to create the example data dashboard linked above.

The motivation of this project was to create an interactive data vizualization, hosted on Heroku (or similar) as a weekly assignment for the Data Incubator Fellowship. This project showcases interactive data visualization with D3.js, DC.js, Python, MongoDB, hosted on Heroku. MongoDB for storing and querying the data, Python for building a web server that interacts with MongoDB and serving html pages, Javascript libraries d3.js, dc.js and crossfilter.js for building interactive charts.

## Getting started

The dependencies for the project can be installed (in your virtual environment, venv) using

    $ pip install -r requirements.txt

You can use ``Vagrant`` to start a machine with a MongoDB instance running

    $ vagrant up

To initialize the database you need to download the data, other datasets available: https://research.donorschoose.org/t/download-opendata/33

    $ wget http://s3.amazonaws.com/open_data/opendata_projects000.gz


and import it after gunzip

    $ mongoimport -d donorschoose -c projects --type csv --file /vagrant/opendata_projects.csv -headerline
