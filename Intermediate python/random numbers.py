import numpy as np
np.random.rand()
np.random.seed(123)

#coin toss
np.random.seed(123)
coin = np.random.radint(0,2)
print(coin)

import numpy as np
np.random.seed(123)
coin = np.random.randint(0,2) #randomly generate 0 or 1
print(coin)
if coin == 0:
  print("heads")
else:
  print("tails")
  
