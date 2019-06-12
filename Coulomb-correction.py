#Phys. Status Solidi B248, No. 5, 1067-1076 (2011)
import numpy as np
from math import sqrt, exp, pi
import sys
Ecut = input('input cutoff energy in eV')         #input cutoff energy
epsilon = input ('input dielectric constant')
omega = input('input cell volume')
q = input('input model charge')
Hatree = 27.21138602                   
Gcut = sqrt(2*Ecut/Hatree)                              #calculate cutoff G vector (modulus)
x, y, z = 0, 0, 0
i=0                                           
f = np.zeros((300,3))
while x**2+y**2+z**2<=Gcut**2:
    while x**2+y**2+z**2<=Gcut**2:
         while x**2+y**2+z**2<=Gcut**2:
               f[i,0] = x
               f[i,1] = y
               f[i,2] = z                         #store allowed G vectors in to the array
               z = z+1
               i = i+1
         else:
              z = 0
              y=y+1
    else:
         z = 0
         y=0
         x=x+1
#print(f)
E,E1,E2=0,0,0
while f[i,0]!=0 or f[i,1]!=0 or f[i,2]!=0:
       E1+=2*pi/epsilon/omega*q**2/(f[i,0]**2+f[i,1]**2+f[i,2]**2)
       i=i+1
E2=-1/pi/epsilon*q**2*Gcut
E=E1+E2
print(E)
#calculate coulomb correction energy
