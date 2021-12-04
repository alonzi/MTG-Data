# lpa2a@virginia.edu
# exploration of vow draft data from 17 lands
# 2021-12-03
# fun!

# import ROOT # need to bring in pyroot https://root.cern/manual/python/

import pandas as pd


# read in data
filepath = "./2021-12-01-17lands-premier-data/"
filename = "draft_data_public.VOW.PremierDraft.csv"
filenamekurtz = "kurtz.csv"
df = pd.read_csv(filepath+filenamekurtz)

# select features of interest
features = ["user_match_win_rate_bucket","user_n_matches_bucket","draft_id","draft_time","user_rank","event_match_wins","event_match_losses"]
df2 = df[df.columns.intersection(features)]
print(df2.head)

# select final result of each draft
df3 = df2.groupby("draft_id").max()
print(df3.head)


# analysis
# histogram - draft time by hour of day and day of week 2d
# histogram - event_match_wins

df3["event_match_wins"].plot.hist()