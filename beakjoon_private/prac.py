# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 16:30:28 2022

@author: 형준
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# First create some toy data:
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

# Create just a figure and only one subplot
fig, ax = plt.subplots()
fig.figsize = (20,10)
ax.scatter(x, y)
ax.set_title('Simple plot')

'''
# Create two subplots and unpack the output array immediately
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(x, y)
ax1.set_title('Sharing Y axis')
ax2.scatter(x, y)
'''
# Create four polar axes and access them through the returned array
#fig, axs = plt.subplots(2, 2, subplot_kw=dict(projection="polar"))
#axs[0, 0].plot(x, y)
#axs[1, 1].scatter(x, y)

# Share a X axis with each column of subplots
# plt.subplots(2, 2, sharex='col')

# Share a Y axis with each row of subplots
# plt.subplots(2, 2, sharey='row')

# Share both X and Y axes with all subplots
# plt.subplots(2, 2, sharex='all', sharey='all')

# Note that this is the same as
# plt.subplots(2, 2, sharex=True, sharey=True)

# Create figure number 10 with a single subplot
# and clears it if it already exists.
# fig, ax = plt.subplots(num=10, clear=True)