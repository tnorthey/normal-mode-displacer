# normal\_mode\_displacer

## Description
Displace atomic coordinates along molecular normal modes. Works for any molecule with g09 freq=hpmodes and equilibrium.xyz starting geometry. Water is shown as an example below.

![watermodes](watermodes.gif)

## Requirements

- Gaussian quantum chemistry package
- python2.7 or python3

## How to use

### Files

1. equilibrium.xyz, the starting geometry.

2. normalmodes.txt, contains the normal modes from a Gaussian (g09) calculation with freq=hpmodes option enabled.

3. variables.py, contains user defined variables.

4. run.py, run this to start generating randomly displaced geometries (xyz files).

### Functions

No need to edit these:

- displace\_coords.py, displace equilibrium.xyz coordinates along the normal modes 

- read\_displacements.py, read displacement factors from normalmodes.txt

- rw\_xyz.py, read or write xyz files 

- Z2m.py, converts between atom name (H,C,N,O, etc.) or atomic number to atomic mass

### Usage

First run a Gaussian (g09) calculation with "freq=hpmodes". Then manually extract the file 'normalmodes.txt' from the frequencies section of the .log file. Make sure 'equilibrium.xyz' is the starting geometry you want (probably the optimised geometry from the same .log file, but it doesn't have to be). 

Define the variables in `variables.py':

```python
# Number of random geometries to generate
N = 100

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
```

``N`` is the number of geometries that will be outputted, ``a`` defines the range of random displacement ``[-a,a]`` along each normal mode, ``freqcm1`` is a list of the frequencies of the normal modes in units cm-1, and ``nmodes`` is the number of normal modes to include, or you can specify which modes to include by the ``Modes`` list. The displacements are defined as,

```math 
xᵢ= x₀ + aΔxᵢ
```
for ``x₀`` the equilibrium geometry (from equilibrium.xyz), ``xᵢ`` the displaced geometry, and ``Δxᵢ`` the normal mode coordinate for mode ``i`` out of a total of ``nmodes``. 

Running the script,
```python
python run.py
```

produces ``N`` .xyz files in the xyz directory.

### Examples

Here, the water molecule is used as an example. The Gaussian files for water (input file and resulting log file) are in the g09 directory.
Water has 3 normal modes as shown in the image. They are "symmetric stretch", "bending", and "anti-symmetric stretch". Here are some examples of moving along each normal mode and creating ``N`` output files, either by a defined amount or by random amounts in a defined range ``[-a,a]``.

#### Displace water molecule by 1 normal mode unit along mode 1

Here, we will move along only the lowest energy mode, mode 1: the "bending" mode which has frequency 1722.4496 cm-1.
Edit variables.py to look like, 

```python
N = 1
randm = 0
a = 1
freqcm1 = [1722.4496, 3799.4476, 3925.0128] 
Modes = 1
nmodes = 1
```
Then run,

```python
python run.py
```
and 1 xyz file will be created in the xyz directory, which is the displaced coordinates. Set ``a = -1`` to move in the opposite direction along the mode.

#### Bend and stretch

To diplace simultaneously along the bending and stretching modes, edit variables.py as follows, 

```python
N = 1
randm = 0
a = [3.0,-1.5]
freqcm1 = [1722.4496, 3799.4476, 3925.0128] 
Modes = [1,2]
nmodes = len(Modes)
```
Then run,

```python
python run.py
```
again creating 1 xyz file in the xyz directory. Although, this time the  water molecule has "bent" by 3.0 normal mode units, and "stretched" by -1.5 units. Note, the difference here is ``a`` and ``Modes`` are now lists.

#### Create N random geometries

Let's move a random distance in the range ``[-a,a]`` along each of the 3 normal modes. Then do this ``N`` times to produce many different geometries.

```python
N = 100
randm = 1
a = 3
freqcm1 = [1722.4496, 3799.4476, 3925.0128] 
Modes = [1,2,3]
nmodes = len(Modes)
```

```python
python run.py
```

This moves along each mode by a random factor in the range ``[-a,a]``. 

For the factor to be mode dependent, simply make ``a`` a list:

```python
N = 100
randm = 1
a = [3.5,2.0,1.8]
freqcm1 = [1722.4496, 3799.4476, 3925.0128]
Modes = [1,2,3]
nmodes = len(Modes)
```

```python
python run.py
```
