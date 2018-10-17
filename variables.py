
# Number of random geometries to generate
N = 1000

# random number between -x and x to displace along each mode
a = 3

# frequencies (cm-1) of selected modes
freqcm1 = [ 1722.4496, 3799.4476, 3925.0128] 

# selected modes
#Modes = [1,2,3]
Modes = list(range(1, len(freqcm1) + 1 ))  # all modes

