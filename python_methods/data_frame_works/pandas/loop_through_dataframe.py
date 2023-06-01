#We can hold of a every column & row of the data frame using pandas DataFrame

import pandas as pd

dict = {
    "students" :  ["Suresh", "Ramesh", "Sunil"],
    "score" : [56, 78, 90]
}


data = pd.DataFrame(dict)
print(data)

##loops through the rows of the dataframe

for (index,row) in data.iterrows():
    print(row.students)
    print(row.score)
    if row.students == "Suresh":
        print(row.score)
Results:
========
  students  score
0   Suresh     56
1   Ramesh     78
2    Sunil     90
Suresh
56
56
Ramesh
78
Sunil
90
