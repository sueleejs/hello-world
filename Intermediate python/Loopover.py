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

# for first try - In Pandas, need to mention explicitly that I want to interate over the rows
import pandas as pd
brics = pd.read_csv("brics.csv", index_col = 0)
for val in brics :
     print(val)

#iterrows
import pandas as pd
brics = pd.read_csv("brics.csv", index_col = 0)
for lab, row in brics.iterrows():
          print(lab)
          print(row)
# in the first iteration, lab is BR, and row is this entire pandas series

#selective print
import pandas as pd
brics = pd.read_csv("brics.csv", index_col = 0)
for lab, row in brics.iterrows():
          print(lab +": " + row["capital"])

#add column
import pandas as pd
brics = pd.read_csv("brics.csv", index_col = 0)
for lab, row in brics.iterrows() :
          brics.loc[lab, "name_length"] = len(row["country"])
print(brics)

#apply
import pandas as pd
brics = pd.read_csv("brics.csv", index_col = 0)
brics["name_length"] = brics["country"].apply(len)
print(brics)

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab)
    print(row)
          
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
print(cars)

# Adapt for loop
for lab, row in cars.iterrows() :
     cars.loc[lab, "COUNTRY"] = len(row["country"])

# Adapt for loop
for lab, row in cars.iterrows() :
     cars.loc[lab, "COUNTRY"] = row["country"].upper()

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

print(cars)
          
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
for lab, row in cars.iterrows() :
    cars["COUNTRY"] = cars["country"].apply(str.upper)

print(cars)
          
      
