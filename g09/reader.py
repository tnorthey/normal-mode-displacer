import re

c=0
with open('freq2.log','r') as f:
  with open('normalmodes.txt','w+') as g:
    for line in f:
      c+=1
      if re.match( r'\s+Frequencies\s*---\s*\d*', line ):
        g.write(line)
      elif re.match( r' ^\s+ [1-3] \s+ (\d*\s+){2} ( (-|\s) \d*\.\d{5}\s+ ){2,5}$', line ):
        g.write(line)

