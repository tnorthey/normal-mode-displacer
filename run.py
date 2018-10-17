
from rw_xyz import read_xyz,write_xyz
from displace_coords import displace_coords 
from variables import *
from random import random

AtomList,R0,comment = read_xyz('equilibrium.xyz')  # read starting coordinates

####################################################

for j in range(N):  # loop N times
  print('Step ' + str(j+1))
  D=R0  # Starting coordinates
  for i in range(len(Modes)):  # Loop over modes
    imode=Modes[i]  # Mode number
    value = random()  # random value between 0 and 1
    Factor = -a + ( value * 2 * a )  # random value in range [-a,a]
    D = displace_coords(D,imode,freqcm1[i],Factor)	# Displace coordinates along mode 'imode' by 'Factor'
  x=len(str(N))
  frmat="%0" + str(x) + "d"
  fname='xyz/' + str(frmat % (j+1))  + '.xyz'	# Output file name
  comment=' '  # comment on 2nd line of xyz file
  write_xyz(AtomList,D,fname,comment)  # write to xyz

####################################################

