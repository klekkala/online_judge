import re
dummy = 'skdjffk394.45'
l = []
l = re.findall(r"[-+]?\d*\.\d+|\d+", dummy)
a = l[0]
b = l[0]
print a

