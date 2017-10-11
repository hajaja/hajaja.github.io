import pandas as pd
import numpy as np
import datetime,re,os,sys
import matplotlib.pyplot as plt

strFileAddress = 'plot.xlsx'
df = pd.read_excel(strFileAddress, sheetname='Best')
df = df.set_index('dtEnd')

for strStrategy in ['TSM', 'XSM', 'TSC', 'XSC', 'Stock', 'Port', 'DualThrust', 'DynamicBreakOut', 'FD']:
    sV = (df[strStrategy]+1).cumprod()
    sDD = sV / sV.expanding().max() - 1
    
    # axis
    plt.xticks(rotation=90)
    ax1 = plt.subplot()
    ax1.grid()
    ax2 = ax1.twinx()
    ax1.set_ylabel('Value', color='b')
    ax2.set_ylabel('DrawDown', color='r')
    ax2.set_ylim((sDD.min(), 0))
    plt.title(strStrategy)
    
    # Value
    ax1.plot(sV.index, sV.values, color='b')

    # DD
    ax2.bar(sDD.index, sDD.values, color='r', edgecolor='r')

    strFileAddress = strStrategy + '.png'
    plt.savefig(strFileAddress, format='png') 
    plt.close('all')


