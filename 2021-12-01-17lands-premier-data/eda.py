# lpa2a@virginia.edu
# exploration of vow draft data from 17 lands
# 2021-12-03
# fun!

# import ROOT # need to bring in pyroot https://root.cern/manual/python/
import pandas as pd
import datetime
#import matplotlib
import matplotlib.pyplot as plt

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

# convert time to pandas._libs.tslibs.timestamps.Timestamp
df3["draft_time_days"] = (pd.to_datetime(df3["draft_time"]).astype(int)/10**9/60/60/24)%7
df3["draft_time_hour"] = (pd.to_datetime(df3["draft_time"]).astype(int)/10**9/60/60)%24
print(df3.head)


# analysis

# histogram - wins
#binning = [x-0.5 for x in range(9)]
#df3["event_match_wins"].plot.hist(bins=binning)
#plt.show()


# histogram - day of the week
#binning = [x-0.5 for x in range(8)]
#df3["draft_time_days"].plot.hist(bins=binning)
#plt.show()

# histogram - hour of the day
binning = [x-0.5 for x in range(25)]
df3["draft_time_hour"].plot.hist(bins=binning)
plt.show()