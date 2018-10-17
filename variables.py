
# Number of random geometries to generate
N = 1000

# switch on (1) or off (0) random displacements
randm = 1

# if randm is on the random displacement will be in range [-a,a], if randm is off it will displace by exactly a
a = 3

# frequencies (cm-1) of selected modes
freqcm1 = [1722.4496, 3799.4476, 3925.0128] 

# selected modes
#Modes = [1,2,3]
nmodes = len(freqcm1)
Modes = list(range(1, nmodes + 1 ))  # all modes

