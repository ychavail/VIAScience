##################################################################
# Description: Defintion of all the functions/modules useful to plot statistics from the database ./data/data.csv. The modules are used in ./src/main.py.
# Code name: ./src/utils.py
# Date of creation: 2019/03/12
# Date of last modification: 2019/03/14
# Contact information: Yann Chavaillaz, yann.chavaillaz@gmail.com
##################################################################

# Non-local packages required
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def read_data(file):
    """ Read the content of a .csv file and putting it in the dataframe (using pandas). Headers are considered. """
    data = pd.read_csv(file)
    return data

def sort_data(df,gender):
    """ Sort a dataframe of statistics of men and women. The output is a sub-dataframe containing only men or only women statistics. """
    sorted_df = df[df['gender'].isin([gender])]
    return sorted_df

def choose_bins(df,var,step):
    """ Selection of bins consistent with the statistics of the dataframe. For age statitics: getting the previous integer of the minimum value as a lower limit and the next integer of the maximum value as an upper limit. For height statistics: similar, but with a 10^-1 precision. One bin per year for age, one bin every 2cm for height. """
    if step == 1.:
        bin_1   = round(np.min(df[var].values))
        bin_n   = round(np.max(df[var].values))+1
        bins    = int(bin_n-bin_1)
    elif step == 0.1:
        bin_1   = round(np.min(df[var].values),1)
        bin_n   = round(np.max(df[var].values),1)+0.1
        bins    = int((bin_n-bin_1)*50.)
    return bin_1,bin_n,bins

def plot_histogram(list,bin_1,bin_n,bins,side,label):
    """ Plot histogram for statistics of one gender in particular. Use the left/right part of each bin if women/men statistics are plotted. """
    counts_list, bin_edges_list = np.histogram(list, bins=bins,range=(bin_1,bin_n))
    column_width = np.min(bin_edges_list[1:] - bin_edges_list[:-1])/3.
    if side == 'left':
        column_spot = 0.5*(bin_edges_list[1:]+bin_edges_list[:-1])+column_width
    elif side == 'right':
        column_spot = 0.5*(bin_edges_list[1:]+bin_edges_list[:-1])-column_width
    plt.bar(column_spot,counts_list,label=label,alpha=0.5, width=column_width)
    return column_spot,column_width

def doublehistogram(df,var,step,res,path):
    """ Construction and saving of the figure illustrating statistics of both men and women. Figure is saved in the folder 'path'. """
    df_F = sort_data(df,'F')
    df_M = sort_data(df,'M')
    bin_1,bin_n,bins = choose_bins(df,var,step)
    spot1,width1 = plot_histogram(df_F[var].values,bin_1,bin_n,bins,'left','women')
    spot2,width2 = plot_histogram(df_M[var].values,bin_1,bin_n,bins,'right','men')
    plt.legend(loc=0)
    plt.xlabel(var)
    plt.ylabel('#occurrences')
    plt.title('Distribution of '+var+' among both genders')
    plt.savefig(path+var+'_distribution.png',dpi=res)
    plt.close()
    return spot1,spot2,width1,width2
