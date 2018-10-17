# random_displacer

## Description
Displace atomic coordinates along molecular normal modes.

![watermodes](watermodes.gif)

## How to use

### Files

1. equilibrium.xyz, The equilibrium geometry (lowest energy geometry from an opt calculation).

2. variables.py, Contains user defined variables.

3. run.py, Run this to start generating randomly displaced geometries (xyz files).

### Functions

No need to edit these:

- displace\_coords.py 

- read\_displacements.py  

- rw\_xyz.py  

- Z2m.py

### Usage

Open `variables.py' which contains values:

```python
N = 100

a = 3

nmodes = 153
```

``N`` is the number of geometries that will be outputted. ``a`` defines the range of random displacement ``[-a,a]`` along each normal mode, in other words,

```math 
xᵢ= x₀ + aΔxᵢ
```
for ``x₀`` the equilibrium geometry (from equilibrium.xyz), ``xᵢ`` the displaced geometry, and ``Δxᵢ`` the normal mode coordinate for mode ``i`` out of a total of ``nmodes``. 

If you run the script,
```python
python2.7 run.py
```

N files will be created in the xyz directory.
