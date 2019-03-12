##################################################################
# Description:
# Code name: ./src/utils.py
# Date of creation: 2019/03/12
# Date of last modification: 2019/03/12
# Contact information: Yann Chavaillaz, yann.chavaillaz@gmail.com
##################################################################

# Non-local packages required
import numpy as np
import matplotlib.pyplot as plt

def get_split_line(line):
    return line.replace('\n', '').split(',')

def read_data(file):
    ListOfAllLines = []
    for line in file:
        ListOfAllLines.append(line)
    return ListOfAllLines

def sort_data(ListOfAllLines):
    x = []
    y = []
    z = []
    w = []
    for line in ListOfAllLines:
        if line[0] == 'M':
            split_line = get_split_line(line)
            x.append(float(split_line[1]))
            y.append(float(split_line[2]))
        elif line[0] == 'F':
            split_line = get_split_line(line)
            z.append(float(split_line[1]))
            w.append(float(split_line[2]))
    return x,y,z,w

def plot_histogram(list,label):
    counts_list, bin_edges_list = np.histogram(list, bins=100)
    column_width = np.min(bin_edges_list[1:] - bin_edges_list[:-1])
    plt.bar(0.5*(bin_edges_list[1:] +bin_edges_list[:-1]),  counts_list, label=label, alpha=0.5, width=column_width)

def save_doublehistogram(list_F,list_M,var,xlabel,ylabel,title,res,path):
    plot_histogram(list_F,"women's "+var)
    plot_histogram(list_M,"men's "+var)
    plt.legend(loc=0)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.savefig(path+var+'_distribution.png',dpi=res)
    plt.close()
