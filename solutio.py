
import pandas as pd
import numpy as np
from pprint import pprint

ltable = pd.read_csv( "ltable.csv")
rtable = pd.read_csv("rtable.csv")
train = pd.read_csv("train.csv")

match = []
final = []
rmodel =  rtable["modelno"].tolist()
lmodel = ltable["modelno"].tolist()
for modelnum in lmodel:
    if modelnum in rmodel:
        match.append(modelnum)
match = np.array(match)
finalmatch = [x for x in match if pd.isnull(x) == False]
for s in finalmatch:
    if s != 'nan':
        final.append(s)

expor = []

lindex = pd.Index(lmodel)
rindex = pd.Index(rmodel)
for itemnum in final:
    left = lindex.get_loc(itemnum)
    right = rindex.get_loc(itemnum)
    tup = [left,right]
    expor.append(tup)

export = []

for stuff in expor:
    if type(stuff[1]) == int:
        export.append(stuff)

finalexport = []

compare= train[train['label'] == 1]
comparer = compare['rtable_id'].tolist()
comparel = compare['ltable_id'].tolist()



for tup in export:

    if tup[0] not in comparel:
        if tup[1] not in comparer:
            finalexport.append(tup)
pprint(finalexport)

l = [x[0] for x in finalexport]
r = [x[1] for x in finalexport]
d = {'ltable_id': l, 'rtable_id': r}
df = pd.DataFrame(data = d)
df.to_csv("myoutput.csv", index=False)



