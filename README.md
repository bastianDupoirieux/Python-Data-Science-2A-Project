## Python-Data-Science-2A-Project
A repository containing our project for the "Python for Data Science" course at the ENSAE.


This project is carried out by @efflam581, @bastianDupoirieux and @Aharon21

The entire project's source code is available on github, at [linked text](https://github.com/bastianDupoirieux/Python-Data-Science-2A-Project)

# What is this project?

This project will focus primarlily on studying rail connections between major European cities, using selected open-source data, and datasets we created from scratch.

The aim of our work is, first of all, to improve our Python skills, particularly with regard to the use of databases and widely used Python packages.

In particular, we use folium to create a few interactive maps, on which we try to show some (more or less) interesting information, with regard to train lines and train stations in certain European countries.

All the packages we use are listed under the requirements.md file

# How to work on this project?

We have one main visualisation file, aptly named `Visualisation.ipynb`. This file uses other files we have created, but is really the final work file where all the results will be shown.

# What are the different files?

There are four working files in this project, each serves a specific purpose.
We've got a perfect balance of two notebooks, and two regular .py files.

Both regular .py files work as modules, that are imported into both notebooks, in order to gather a bit of information using webscraping techniques

The notebooks is where the real magic takes place. The unifiedDatabase.ipynb notebook is a look into creating the useful database out of our accessible data.
The Visualisation.ipynb notebook creates maps based on our data. Due to technical limitations, the maps can be a bit slow to load, unfortunately. 

Furthermore, the data.zip zipped folder summarises every database we have used throughout the project, perfectly organised by country.

Lastly, we have got regular github files, README.md (which you are reading right now), setup.md, requirements.md and .gitignore

Hopefully you enjoy our little project, and who knows, you may even develop an interest in train transport in Europe :)
