# This folder contains exploratory plots for HBG
* Data set 1 - hbg-cards-orig.csv : HBG data starting from 3 weeks into the format until the Alchemy change 
* Data set 2 - hbg-cards-alch.csv : HBG data starting from alchmeny rebalance to date

## Installation/Building
`git clone https://github.com/alonzi/MTG-Data.git`

## Data
source: https://www.17lands.com/public_datasets
dictionary: https://www.17lands.com/metrics_definitions
license: these data sets are licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/)

* Raw data - `data/raw-data.tsv` : initial data from 17lands - scrape of win rate data no temporal cuts or any other cuts
* Data set 1 - `data/data.tsv` : unclean file
* Data set 2 - `data/data.csv` : clean file

## Usage
`$ cd hbg-eda`
`$ python main.py <datafile>.csv`

## Notes
To Do:
* create datasets
* create main.py
* create plots
