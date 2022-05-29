# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for k, v in europe.items():
    print("the capital of " + str(k) + " is " +str(v))

# Import numpy as np
import numpy as np

# For loop over np_height
for x in np_height:
    print(str(x) + " inches")
# For loop over np_baseball
for x in np.nditer(np_baseball) :
    print(x)
