#!/usr/bin/env python
# coding: utf-8

# In[10]:


import matplotlib.pyplot as plt
import numpy as np


# * 横轴为渔场水体体积 V(m3)=A(m2)*d(m)
# 
# * 纵轴为渔业产量 P(kg)

# In[11]:


#x = np.arange(370000, 42000000, 100000)
#y = np.arange(50000, 2800000, 10000)
x = np.arange(370000, 41400000, 100000)
y = np.arange(61500, 2742900, 10000)
xx, yy = np.meshgrid(x, y, sparse=True)
z = yy / xx
# h = plt.contourf(x, y, z)
# plt.show()


# In[12]:


# fig = plt.figure(figsize=(8,16))
# ax = fig.add_subplot(2,1,1)

# h= ax.contourf(x, y, z)

#ax.set_yscale('log')
# ax.set_xscale('log')

# plt.show()


# In[13]:


xxx = [7820000,1911000,41400000,28000000,2100000,1350000,370000,960000,3900000,3060000,740000,720000,1070000,3972000,996000,2780000,5340000,7488000,11583000,1000000,7035000,7130000,10025000,5050000,2210000,2510000]


# In[14]:


yyy = [236775,489150,413280,464940,369000,467400,568200,221400,861000,102336,61500,61500,504300,1205400,233700,258300,2742900,2533800,2398500,319800,861000,1389900,393600,2091000,1119300,184500]


# In[15]:


#h = plt.contourf(x, y, z)
# hh = plt.scatter(xxx,yyy)
# plt.show()


# In[16]:


# fig = plt.figure(figsize=(8,16))
# ax = fig.add_subplot(2,1,1)

#h= ax.contourf(x, y, z, [10,20],colors='k')
#h= ax.contour(x, y, z, [1,3,10,30], colors='k')
# hh = plt.scatter(xxx,yyy)

# ax.set_yscale('log')
# ax.set_xscale('log')

# plt.clabel(h,fontsize=10,colors=('k','r'))

# ax.set_xlabel('time ()')
# ax.set_ylabel('volts ()')

# plt.show()


# In[17]:


# fig = plt.figure(figsize=(8,16))
# ax = fig.add_subplot(2,1,1)

#h= ax.contourf(x, y, z, [10,20],colors='k')
# h= ax.contour(x, y, z, [1,3,10,30], colors='k')
#hh = plt.scatter(xxx,yyy)

# ax.set_yscale('log')
# ax.set_xscale('log')

# plt.clabel(h,fontsize=10,colors=('k','r'))

# ax.set_xlabel('time ()')
# ax.set_ylabel('volts ()')

# plt.show()


# In[18]:


plt.clf()

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(1,1,1)

h= ax.contourf(x, y, z, cmap='GnBu')
cb=plt.colorbar(h)
cb.ax.tick_params(labelsize=18)
cb.set_label('Aquaculture Intensity Index' r'$(I, Unit:kg \cdot m^{-3})$',size=18)
#cb.set_ticks([0.005,3.5])

# h=ax.contour(x, y, z, [0.01,0.03,0.1,0.3,1,3], colors='k', norm=norm)
h=ax.contour(x, y, z, [0.01,0.03,0.1,0.3,1,3], colors='k')

#h=ax.imshow(z, cmap='RdBu', vmin=0, vmax=2, interpolation='none')
#cbar = fig.colorbar(h, ax=ax)
#cbar.minorticks_on()

hh = plt.scatter(xxx,yyy)

ax.set_yscale('log')
ax.set_xscale('log')

plt.clabel(h,fontsize=18,colors=('k'), fmt='%.2f',inline=True,rightside_up=False)

ax.set_xlim(min(xxx)*0.9,max(xxx)*1.1)
ax.set_ylim(min(yyy)*0.9,max(yyy)*1.1)

font = {'family':'Times New Roman','weight':'normal','size':20}

ax.set_xlabel('Farm water volume 'r'$(A \times \bar{H}, Unit:m^{3})$',font)
ax.set_ylabel('Farm annual production 'r'$(p, Unit:kg)$ ',font)

plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

plt.savefig('index_map_high.png', dpi=600)

plt.show()


# In[ ]:




