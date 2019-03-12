##################################################################
# Description:
# Code name: ./src/main.py
# Date of creation: 2019/03/12
# Date of last modification: 2019/03/12
# Contact information: Yann Chavaillaz, yann.chavaillaz@gmail.com
##################################################################

# Local packages required
import src.utils as fct

# Definition of paths
path_data   = './data/'     # where to find the dataset
path_fig    = './figures/'  # where to store the figures

# Opening of the dataset
file        = open(path_data+'data.csv', 'r')

# Reading or sorting the dataset by gender
list_data                   = fct.read_data(file)
age_F,size_F,age_M,size_M   = fct.sort_data(list_data)

# Plotting histograms of age and size distribution among both genders
fct.save_doublehistogram(age_F,age_M,"age","age [years]","#occurrences","Distribution of age among both genders",300,path_fig)
fct.save_doublehistogram(size_F,size_M,"size","size [meters]","#occurrences","Distribution of size among both genders",300,path_fig)
