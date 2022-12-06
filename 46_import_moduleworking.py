import pandas as pd
import sys   #sys module is used to check for how and from where(path) module is importing.
import file46


print(pd.__version__)
print(sys.path)               #check all the directory that where the module is available to use
print(file46.a)
print(file46.modfun(':Is working'))
