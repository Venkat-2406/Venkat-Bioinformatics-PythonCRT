'''
import pandas as pd
calories={"Day1":420,"Day2":380,"Day3":390,}
myvar=pd.Series(calories)
print(myvar)

'''


import pandas as pd
calories={"Day1":420,"Day2":380,"Day3":390,}
myvar=pd.Series(calories,index=['Day1','Day2','Day3'])
print(myvar)