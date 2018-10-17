def read_xyz(fname):
  ##################################################
  # read_xyz:	Reads xyz file 'fname'
  # Inputs:	fname, the file name of the xyz file to read
  # Outputs: 	AtomList (string list), list of atomic labels; 
  # 		Coords (float list), coordinates as column vector with the format X1,Y1,Z1,X2,Y2,Z2,...
  ##################################################
  with open(fname,'r') as f:			# open file   
    AtomList=[]; Coords=[]
    c=0
    for line in f:
      c+=1				
      if c==1:
        pass
      elif c==2:
        comment = line
      else:
        AtomList.append(line.split()[0]) 	# List of atomic labels
        for i in range(1,4):
          Coords.append(float(line.split()[i]))
  ##################################################dd
  return AtomList,Coords,comment

def write_xyz(AtomList,Coords,fname,comment):
  ##################################################
  # write_xyz: Write xyz file 'fname' using atom list 'AtomList' and Cartesian coordinates 'Coords'
  # Inputs:	AtomList (string list), list of atomic labels
  # 		Coords (float list), coordinates as column vector with the format X1,Y1,Z1,X2,Y2,Z2,... 
  # 		fname (str), output xyz file name  
  #		comment (str), comment line in the xyz file
  # Outputs:	'fname' (file), xyz file
  ##################################################
  Nat=len(AtomList)					# Number of atoms
  with open(fname,'w') as f:				# Open file for writing
    f.write(str(Nat)+'\n')				# The first line of an xyz file contains only the number of atoms
    f.write(comment + '\n')				# The second line is blank or contains a title string (convention)
    for i in range(3*Nat):				# Loop over vectors of lentgh 3*Nat
      if i%3==0:					# Indices 0,3,6,...
        Atom=AtomList[int(i/3)]				# Read atom labels (at indices 0,1,2,... every i=0,3,6,...)
        x = Coords[i]				# x coordinate
      elif (i-1)%3==0:				# Indices 1,4,7,...
        y = Coords[i]				# y coordinate
      elif (i-2)%3==0:				# Indices 2,5,8,...
        z = Coords[i]				# z coordinate
        #f.write( Atom + '  ' + str(x) + '  ' + str(y) + '  ' + str(z) + '\n')	# Write out Lines containing atom labels and x,y,z coordinates
        f.write( "%2s %12.8f %12.8f %12.8f \n" % (Atom,x,y,z) )	# Write out Lines containing atom labels and x,y,z coordinates
  ################################################## 
  return

