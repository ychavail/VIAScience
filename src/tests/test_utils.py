##################################################################
# Description: This .py executable allows to test all the functions defined in ./src/utils.py.
# Code name: ./src/test/test_utils.py
# Date of creation: 2019/03/14
# Date of last modification: 2019/03/14
# Contact information: Yann Chavaillaz, yann.chavaillaz@gmail.com
##################################################################

# Package in which functions to be tested are defined
import src.utils as fct

# Non-local packages required
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

# Definition of the dataset to test
path_data   = './data/'                         # where to find the dataset
file        = (path_data+'data_to_test.csv')    # where data is stored

# Testing the functions of ./src/utils.py
class TestClass:
    def test_read_data(self):
        """ test of the read_data function """
        data_to_test = fct.read_data(file)
        assert np.size(data_to_test) == 12
        assert round(np.mean(data_to_test['age'].values),2) == 33.25
        assert round(np.sum(data_to_test['height'].values),2) == 6.79

    def test_sort_data(self):
        """ test of the sort_data function """
        data_to_test = fct.read_data(file)
        dataM = fct.sort_data(data_to_test,'M')
        assert np.size(np.where(dataM['gender'].values=='F')) == 0

    def test_choose_bins(self):
        """ test of the choose_bins function """
        data_to_test = fct.read_data(file)
        bin_1,bin_n,bins = fct.choose_bins(data_to_test,'height',0.1)
        assert round(bin_1,1) == 1.6
        assert round(bin_n,1) == 1.9
        assert round(bins,1) == 15.

    def test_plot_histogram(self):
        """ test of the plot_histogram function """
        data_to_test = fct.read_data(file)
        data_F = fct.sort_data(data_to_test,'F')
        bin_1,bin_n,bins = fct.choose_bins(data_F,'age',1.)
        spot1,width1 = fct.plot_histogram(data_F['age'].values,bin_1,bin_n,bins,'left','women')
        assert round(spot1[-1]-spot1[0],1) == 1.0

    def test_doublehistogram(self):
        """ test of the doublehistogram function """
        data_to_test = fct.read_data(file)
        spot1,spot2,width1,width2 = fct.doublehistogram(data_to_test,list(data_to_test)[1],1.,300,'./figures/')
        assert round(width1,2) == round(width2,2)
        assert round(spot1[0]+width1,2) == round(spot2[0]-width1,2)
