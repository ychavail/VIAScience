# README #

This package contains the AI software developer assignment.

content:
- `environment.yml` defines the conda environment
- `data/data.csv` contains randomly generated data about the heights and ages of individuals.
- `src/main.py` contains code that reads the data and generates simple histogram plots
- `src/utils.py` contains a function called in `src/main.py`. 

The quality of the code is purposefully very poor.

Your task is to refactor the code to improve its overall quality and to write unit tests using the pytest framework. 

To do so:
- use whatever python module you choose
- feel free to use a linter / pep8
- create whatever file/function/folder/class you see fit
- improve the quality of the plots in which ever way you see fit, while keeping the original intent of the plots
- commit your work regularly in git with meaningful commit messages.


Spend no more than 2 hours on this assignment. To keep the scope small, here is what we do not expect:

 - *do not* create new analyses, extra plots or a machine learning model: the data is random and trivial
 - *do not* create a browser app or html report or anything like that
 - *do not* put the data in a database, do continuous integration or do anything on the cloud 


The goal of this assignment is to show how you think about code. Please submit your work
as a tar ball of your updated git repo along with a brief document describing your thoughts on what was wrong with 
the initial code, what you did to make it better, etc.
