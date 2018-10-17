
from rw_xyz import *

def Z2m(xyzfile):
  # convert atomic numbers (Z) to mass for xyzfile

  AtomList,Coords,comment = read_xyz(xyzfile)
  m=[]
  # convert AtomList to MassList
  for i in range(len(AtomList)):
    a = AtomList[i]
    if a=='H' or a=='1':
      m.append(1.0079)
    elif a=='He' or a=='2':
      m.append(4.0026)
    elif a=='B' or a=='5':
      m.append(10.811)
    elif a=='C' or a=='6':
      m.append(12.0107)
    elif a=='N' or a=='7':
      m.append(14.0067)
    elif a=='O' or a=='8':
      m.append(15.9994)
    elif a=='F' or a=='9':
      m.append(18.9984)
    elif a=='S' or a=='16':
      m.append(32.065)
    elif a=='Fe' or a=='26':
      m.append(55.845)

  return m
