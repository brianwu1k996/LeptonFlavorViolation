#!/usr/bin/env python
print ("Loading Libraries")
import matplotlib
matplotlib.use('Agg')
import re
import os, sys
import pickle, cPickle
import pprint
from math import fabs, log, exp
from numpy import log10
from numpy import *

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
#from matplotlib.mlab import griddata
import numpy as np
from scipy.interpolate import griddata
from math import ceil, sqrt
from copy import deepcopy

from pylab import genfromtxt 
from matplotlib.pyplot import text

#This script needs to be executed in python2

def plot_logx_logy_logz(xvalues, xlabel, yvalues, ylabel, zvalues, zlabel, title, filename, linecolor, contourstyle, contourlevel, contourlinewidth, clabel_positions, clabelformat):
    print ("Plotting '"+title+"'")

    # remove invalid entries which have either x or z <= 0
    newxvalues, newyvalues, newzvalues = xvalues[:], yvalues[:], zvalues[:]
    npopped = 0
    newX, newY, newZ =  list(), list(), list()
    for i in range(len(xvalues)):
           newX.append(xvalues[i])
           newY.append(yvalues[i])
           if zvalues[i] == 0:
              newZ.append(1E-99)
           else:
              newZ.append(zvalues[i])
	   
    x = np.array(map(log10, newX))
    y = np.array(map(log10, newY))
    z = np.array(newZ)
    
    if len(x) == 0:
       return
    plt.xlabel(xlabel,fontsize = 16)
    plt.ylabel(ylabel,fontsize = 16)
    plt.title(title,fontsize = 16)
    plt.axis([1E-12, 1e-5, 1E-10, 1e-6])
    zmin, zmax =  1E-3, 1E3 #min([z[i] for i in range(len(z)) if x[i] >= -9 and x[i] <= -5 and y[i] >= -9 and y[i] <= -5 and z[i] != 0.])

    ax.set_xscale('log')
    ax.set_yscale('log')

    plt.xticks(fontsize = 12)
    plt.yticks(fontsize = 12)

    
    n=200
    xg = np.linspace(x.min(),x.max(),n)
    yg = np.linspace(y.min(),y.max(),n)
    X,Y = np.meshgrid(xg,yg)

    # interpolate Z values on defined grid
    Z = griddata(np.vstack((x.flatten(),y.flatten())).T, \
    np.vstack(z.flatten()),(X,Y),method='linear').reshape(X.shape)
    # mask nan values, so they will not appear on plot
    Zm = np.ma.masked_where(np.isnan(Z),Z)

    X = np.array(map(lambda k : 10.**k, X))    
    Y = np.array(map(lambda k : 10.**k, Y))
    
    colmap = mpl.cm.Greys_r
    colmap.set_bad('k',1)
    #ax.pcolormesh(X,Y,Zm,vmin=zmin,vmax=zmax,shading='gouraud', norm=mpl.colors.LogNorm(),cmap = colmap)



    cons2 = plt.contour(X, Y, Zm, [contourlevel] ,colors=linecolor,locator=mpl.ticker.LogLocator(), linewidths=contourlinewidth, linestyles = contourstyle)
#


    plt.scatter(map(lambda k: 10**k, x), map(lambda k: 10**k, y), s=-20, c=z, vmin=zmin, vmax=zmax, cmap = mpl.cm.Greys_r,norm=mpl.colors.LogNorm())


##############
#tau decay width limit 
sigmaBrtaupinu=0.057e-2
##############

########################################################################################################
########################################################################################################
########################################################################################################
print ("Reading in Data")

fig = plt.figure(num=None, figsize=(5,4), dpi=300, facecolor='w', edgecolor='k')
ax = fig.add_subplot(1, 1, 1) 
massstring = 'test'
for i in range(len(sys.argv))[1:]:
  resdircollection = sys.argv[i]
  print ("")
  for resdir in resdircollection.split(":"):
    #os.chdir(resdir)
        data=np.zeros((1,20))
        print (" - "+resdir)
        #counter = 0
        for filename in os.listdir(resdir):
            newdata=np.zeros((1,20))
            #print(filename)
            #counter = counter + 1
            #print(counter)
            #print (resdir+"/"+filename)
            with open(resdir+"/"+filename,'r') as f: 
                 line = next((l for l in f if "mX:" in l), None)
                 newdata[0,0]=line[line.find("mX:")+len("mX:"):]
            with open(resdir+"/"+filename,'r') as f: 
                 line = next((l for l in f if "g_CC_Lamb:" in l), None)
                 newdata[0,1]=line[line.find("g_CC_Lamb:")+len("g_CC_Lamb:"):]
            with open(resdir+"/"+filename,'r') as f: 
                 line = next((l for l in f if "g_AB_Lamb:" in l), None)
                 newdata[0,2]=line[line.find("g_AB_Lamb:")+len("g_AB_Lamb:"):]
            with open(resdir+"/"+filename,'r') as f: 
                 line = next((l for l in f if "BRtau2xmu:" in l), None)
                 newdata[0,3]=line[line.find("BRtau2xmu:")+len("BRtau2xmu:"):]
            with open(resdir+"/"+filename,'r') as f: 
                 line = next((l for l in f if "BRtau2xe:" in l), None)
                 newdata[0,4]=line[line.find("BRtau2xe:")+len("BRtau2xe:"):]
            with open(resdir+"/"+filename,'r') as f: 
                 line = next((l for l in f if "produced tau excluding those daughters are also tau lepton:" in l), None)
                 newdata[0,5]=line[line.find("produced tau excluding those daughters are also tau lepton:")+len("produced tau excluding those daughters are also tau lepton:"):]
            with open(resdir+"/"+filename,'r') as f: 
                 line = next((l for l in f if "produced X:" in l), None)
                 newdata[0,6]=line[line.find("produced X:")+len("produced X:"):]
            with open(resdir+"/"+filename,'r') as f: 
                 line = next((l for l in f if "Total Gamma [GeV]:" in l), None)
                 newdata[0,7]=line[line.find("Total Gamma [GeV]:")+len("Total Gamma [GeV]:"):]
            with open(resdir+"/"+filename,'r') as f: 
                 line = next((l for l in f if "ctau [m]:" in l), None)
                 newdata[0,8]=line[line.find("ctau [m]:")+len("ctau [m]:"):]
            with open(resdir+"/"+filename,'r') as f: 
                 line = next((l for l in f if "BRx2tautau:" in l), None)
                 newdata[0,9]=line[line.find("BRx2tautau:")+len("BRx2tautau:"):]
            with open(resdir+"/"+filename,'r') as f: 
                 line = next((l for l in f if "BRx2mumu:" in l), None)
                 newdata[0,10]=line[line.find("BRx2mumu:")+len("BRx2mumu:"):]
            with open(resdir+"/"+filename,'r') as f: 
                 line = next((l for l in f if "BRx2ee:" in l), None)
                 newdata[0,11]=line[line.find("BRx2ee:")+len("BRx2ee:"):]
            with open(resdir+"/"+filename,'r') as f: 
                 line = next((l for l in f if "BRx2gmgm:" in l), None)
                 newdata[0,12]=line[line.find("BRx2gmgm:")+len("BRx2gmgm:"):]
            with open(resdir+"/"+filename,'r') as f: 
                 line = next((l for l in f if "observedX:" in l), None)
                 newdata[0,13]=line[line.find("observedX:")+len("observedX:"):]
            with open(resdir+"/"+filename,'r') as f: 
                 line = next((l for l in f if "visibleX:" in l), None)
                 newdata[0,14]=line[line.find("visibleX:")+len("visibleX:"):]
            with open(resdir+"/"+filename,'r') as f: 
                 line = next((l for l in f if "X Observed Fiducial efficiency:" in l), None)
                 newdata[0,15]=line[line.find("X Observed Fiducial efficiency:")+len("X Observed Fiducial efficiency:"):]
            with open(resdir+"/"+filename,'r') as f: 
                 line = next((l for l in f if "X Visible Fiducial efficiency:" in l), None)
                 newdata[0,16]=line[line.find("X Visible Fiducial efficiency:")+len("X Visible Fiducial efficiency:"):]
            with open(resdir+"/"+filename,'r') as f: 
                 line = next((l for l in f if "reallyProducedX:" in l), None)
                 newdata[0,17]=line[line.find("reallyProducedX:")+len("reallyProducedX:"):]
            with open(resdir+"/"+filename,'r') as f: 
                 line = next((l for l in f if "reallyobservedX:" in l), None)
                 newdata[0,18]=line[line.find("reallyobservedX:")+len("reallyobservedX:"):]
            with open(resdir+"/"+filename,'r') as f: 
                 line = next((l for l in f if "reallyvisibleX:" in l), None)
                 newdata[0,19]=line[line.find("reallyvisibleX:")+len("reallyvisibleX:"):]
            data=np.vstack((data,newdata))
    #os.chdir(resdir)
        data=np.delete(data,0,0)

#converting nan to zero
where_are_NaNs = isnan(data)
data[where_are_NaNs] = 0


#export data
#np.savetxt("plots/data/data_311.dat", data, fmt="%s")



# os.chdir("..")	   
print ("Plotting")

font = {'size'   : 18}
mpl.rc('font', family='serif')
plt.rc("text", usetex=True)
fig = plt.figure(num=None, figsize=(5,4), dpi=300, facecolor='w', edgecolor='k')
ax = fig.add_subplot(1, 1, 1) 
plt.rc("text", usetex=True)
         
#title = r'$\epsilon_{\textrm{det.}}=8.4\%$' 
title = r'$g_{\alpha \beta}$ vs. $g_{\alpha \alpha}$'
xlabel = r'$g_{\alpha \alpha}$ [GeV$^{-1}$]'
ylabel = r'$g_{\alpha \beta}$ [GeV$^{-1}$]'
zlabel = r'$three_event$'
filename = "0_mX1.5_gAB_gCC"

#plot signal
plot_logx_logy_logz(data[:,1], xlabel, data[:,2], ylabel, data[:,19], zlabel, title, filename, 'k', 'solid', 3 , 1 ,[(0.8,5e-8)],'3signal')


#use data files expoted by Mathematica where MovingAverage was used:
#signal311NoBG = genfromtxt("plots/data/signal_311_NoBG.dat");
#signal311NoBG1InvAb = genfromtxt("plots/data/signal_311_NoBG_1InvAb.dat");

#plt.plot(signal311NoBG[:,0], signal311NoBG[:,1],  color='blue',linewidth=1,linestyle='solid' ,label=r"$N_S = ~ \,$3, 50 ab$^{-1}$ (Belle II)" );
#plt.plot(signal311NoBG1InvAb[:,0], signal311NoBG1InvAb[:,1],  color='darkturquoise',linewidth=1,linestyle='solid' ,label=r"$N_S = ~ \,$3, 1 ab$^{-1}$ (Belle)" );

plt.legend(loc='upper right',prop={'size': 9})

#plot ctau
#for exponent in range(-7,5,2):
#	plot_logx_logy_logz(data[:,0], xlabel, data[:,1], ylabel, data[:,4], zlabel, title, filename, 'darkorange', 'dashed', 10**exponent,0.5,[(1.4,2e-4)],'log')
#for exponent in range(5,6):
#	plot_logx_logy_logz(data[:,0], xlabel, data[:,1], ylabel, data[:,4], zlabel, title, filename, 'darkorange', 'dashed', 10**exponent,0.5,[(0.5,2e-9)],'log')


#plot tau decay BR constraint   removed because it is always for ctau < 1 m
#plot_logx_logy_logz(data[:,0], xlabel, data[:,1], ylabel, data[:,8], zlabel, title, filename, 'red', 'dashdot', 2*sigmaBrtaupinu , 0.5, [(1.35,8e-6)],'tauBR')   


#plot LQD coupling constraint
#msfermion=[1e3,5e3]
#for mass in msfermion:
#	limit = 0.20/(1e3*mass)+0.046/(mass**2)
#	plt.plot([0,2],[limit,limit],linestyle='dashed',color='red',linewidth=0.5)
#	plt.text(0.59, limit*0.92, r"$m_{\tilde{d}_{R}}=" + str(int(mass/1000))  + "$ TeV", color='red',ha='left',va='top', fontsize = '8')


#ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(0.1))
#ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.05))
#ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter())

plt.grid(which='major',axis='x',alpha=0.5,linestyle='--',linewidth=0.5)
plt.grid(which='major',axis='y',alpha=0.5,linestyle='--',linewidth=0.5)

plt.savefig("plots/"+filename+".png",bbox_inches='tight')


#br vs ctau plot
plt.clf()#clear the current figure
#plt.cla()#clear the current axes

fig = plt.figure(num=None, figsize=(5,4), dpi=300, facecolor='w', edgecolor='k')
ax = fig.add_subplot(1, 1, 1)
