import pandas as pd
import numpy as np
import datetime,re,os,sys
import matplotlib.pyplot as plt

strFileAddress = 'TSM_Review_CR.xlsx'
df = pd.read_excel(strFileAddress, sheetname='Port')

for strStrategy in ['TSM', 'XSM', 'TSC', 'XSC', 'Stock', 'Port']:
    sV = (df[strStrategy]+1).cumprod()
    sDD = sV / sV.expanding().max() - 1
    dfPlot = pd.concat([sV, sDD], axis=1)
    dfPlot.columns = ['Value', 'DD']
    dfPlot.plot(secondary_y='DD')
    strFileAddress = strStrategy + '.png'
    plt.savefig(strFileAddress, format='png') 
    plt.close('all')


