# @alonzi
# main program for calculating entropy of draft table
# 2022-08-11
# demonstrate flow of entropy through the first pack of a mtg draft


# imports
import pandas as pd

# main function
def main():
    print("\nhello world")

    df = pd.read_csv('hbg-eda/data/data.csv')
    print(df)

if __name__ == "__main__":
    main()