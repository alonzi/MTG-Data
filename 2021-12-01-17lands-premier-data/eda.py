# lpa2a@virginia.edu
# exploration of vow draft data from 17 lands
# 2021-12-03
# fun!

# import ROOT # need to bring in pyroot https://root.cern/manual/python/

import pandas as pd

filepath = "./2021-12-01-17lands-premier-data/"
filename = "draft_data_public.VOW.PremierDraft.csv"
filenamekurtz = "kurtz.csv"

df = pd.read_csv(filepath+filenamekurtz)

print(df.head)
