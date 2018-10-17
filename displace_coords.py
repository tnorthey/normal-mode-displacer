
from read_displacements import *
from Z2m import Z2m
from variables import *

def displace_coords(Coords,imode,freqcm1,Factor):
  ##################################################
  # displace_coords: Displace coords from xyz file 'equilibrium.xyz' along mode 'imode' (0<int<=Nmode) by 'Factor' (float)
  # Inputs:	Coords (float list), coordinates as column vector with the format X1,Y1,Z1,X2,Y2,Z2,...
  #		imode (int), the coordinates are displaced along mode number 'imode'
  #		freqcm1 (float), the frequency in cm-1 of the mode
  # 		Factor (float), the coordinates are displaced along the mode by 'Factor' atomic units  
  # Outputs:	D (float list), displaced coordinates with same formatting as 'Coords'
  ##################################################

  Nat=len(Coords)/3				# Number of atoms 
  Displc=read_displacements(Nat,imode)		# Read normal mode displacements (vector of length 3*Nat)
  mi = Z2m('equilibrium.xyz')
  D=[]
  for i in range( 3 * int(Nat) ):			# Loop over coordinates
    mass = mi[ int( (i - 1) / 3 ) ]  # int rounds down by default
    displacement_constant = (mass**.5 * 0.172*freqcm1**.5)**-1
    #extra_factor = 1e5*freqcm1**-3
    #D.append( Coords[i] + extra_factor * displacement_constant * Factor * Displc[i] ) 	# Displaced coordinates
    D.append( Coords[i] + displacement_constant * Factor * Displc[i] ) 	# Displaced coordinates
  ################################################## 
  return D
