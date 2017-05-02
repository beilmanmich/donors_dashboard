# Donors Choose Visualization - Interactive Dashboard

# Visit the interactive dashboard here: https://donorschoosedashboard.herokuapp.com/

![visualization
demo](https://github.com/beilmanmich/donors_dashboard/blob/master/viz_demo.gif)

## Background

This repository contains a clone of the repo used to create the example data dashboard linked above.

The motivation of this project was to create an interactive data visualization, hosted on Heroku (or similar) as a weekly assignment for the Data Incubator Fellowship. This project showcases interactive data visualization with D3.js, DC.js, Python, MongoDB, hosted on Heroku. MongoDB for storing and querying the data, Python for building a web server that interacts with MongoDB and serving html pages, Javascript libraries d3.js, dc.js and crossfilter.js for building interactive charts.

The data dashboard allows a user to stratify a subset of donations across time period, campaign resource type, campaign recipient poverty level, and state geography. The current dashboard supports 164k records from the data linked below (the full dataset contains 900k records, 164k was the limit I optimized under Heroku and mLab free subscription limits). Data licensed with thanks from DonorsChoose.org (CC_NY_BC 3.0).

This is my first attempt at deploying d3.js visualizations to Heroku. In my past life, I used R Shiny for all interactive data needs.

## Getting started

The dependencies for the project can be installed (in your virtual environment, venv) using

    $ pip install -r requirements.txt

You can use ``Vagrant`` to start a machine with a MongoDB instance running

    $ vagrant up

To initialize the database you need to download the data, other datasets available: https://research.donorschoose.org/t/download-opendata/33

    $ wget http://s3.amazonaws.com/open_data/opendata_projects000.gz


and import it after gunzip

    $ mongoimport -d donorschoose -c projects --type csv --file /vagrant/opendata_projects.csv -headerline

## Using this Git

Please! Help yourself. Much of this project was built off open data sources and existing Git Repos from the previous Hack4Education Challenges.

One tip, when deploying to Heroku...remember to scale up a dyno after pushing any incremental changes! (This cause a lot of frustration as this was a beginner project).

![dyno
up](https://github.com/beilmanmich/donors_dashboard/blob/master/viz_demo.gif)