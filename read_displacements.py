def read_displacements(Nat,imode):
  ##################################################
  # read_displacements: Reads displacement coordinates for mode 'imode' from 'normalmodes.txt'
  # Inputs: 	Nat (int), total number of atoms
  #		imode (int), the displacements are taken from mode number 'imode'
  # Outputs:	D (float list), single column of displacement coordinates (length 3*Nat)
  ##################################################
  # Definitions
  N = 3*Nat  # Number of coordinates
  # Error checks
  if Nat==2:
    Nmode=2
  elif Nat>2:
    Nmode=N-6
  else:
    print("ERROR: Something wrong with number of atoms")
    print("Are there <2 atoms?")
    return
 
  if imode>=1 and imode<=Nmode:
    pass
    #print "Reading displacements for mode " + str(imode)
  else:
    print('ERROR: imode out of range (1,Nmode).')
    return
  # Known pattern of g09 frequencies output file...
  row = int((imode-1)/5)
  a = (row+1)*7 + row*N
  b = (row+1)*(7 + N)
  d = row*5
  # Append displacements from file to column vector 'Displc'
  c=0
  Displc=[]
  with open('normalmodes.txt','r') as f:
    for line in f:
      c+=1
      if c>a and c<=b:
        Displc.append(float(line.split()[imode+2-d]))
  ##################################################
  return Displc

