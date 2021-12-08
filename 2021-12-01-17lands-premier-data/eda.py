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
df3["day_name"] = pd.to_datetime(df3["draft_time"]).dt.day_name()
df4 = df3.groupby(df3["day_name"]).size()
#df3["day_name"] = pd.to_datetime(df3["draft_time"]).dt.day
df3["day_hour"] = pd.to_datetime(df3["draft_time"]).dt.hour
#print(df3["day_name"].head())
# analysis




fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
fig.suptitle('plots')

# histogram - wins
plt.sca(ax1)
ax1.set_xlabel('wins') 
binning = [x-0.5 for x in range(9)]
df3["event_match_wins"].plot.hist(bins=binning)
#plt.show()


# histogram - day of the week
plt.sca(ax2) 
df4.plot.bar()
#plt.show()

# histogram - hour of the day
plt.sca(ax3)
ax3.set_xlabel('hour (UTC±00:00 aka ET+5:00)') 
binning = [x-0.5 for x in range(25)]
df3["day_hour"].plot.hist(bins=binning)
plt.show()