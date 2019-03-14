##################################################################
# Description:
# Code name: ./src/main.py
# Date of creation: 2019/03/12
# Date of last modification: 2019/03/14
# Contact information: Yann Chavaillaz, yann.chavaillaz@gmail.com
##################################################################

# Local packages required
import src.utils as fct

# Definition of paths
path_data   = './data/'     # where to find the dataset
path_fig    = './figures/'  # where to store the figures

# Definition and reading of the dataset
file        = (path_data+'data.csv') # where data is stored
data        = fct.read_data(file)

# Definition of parameters
resolution  = 300 # resolution of the figure in dpi
step1       = 1.  # increment of histogram for the 1st variable
step2       = 0.1 # increment of histogram for the 2nd variable

# Plotting and saving histograms of age and size distribution among both genders
fct.doublehistogram(data,list(data)[1],step1,resolution,path_fig) # age
fct.doublehistogram(data,list(data)[2],step2,resolution,path_fig) # size
