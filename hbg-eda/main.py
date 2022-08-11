# @alonzi
# main program for calculating entropy of draft table
# 2022-08-11
# demonstrate flow of entropy through the first pack of a mtg draft


# imports
import pandas as pd
import matplotlib.pyplot as plt

# main function
def main():
    print("\nhello world")

    df = pd.read_csv('hbg-eda/data/data.csv')
    
    # begin cleaning
    df.dropna(inplace=True)
    df.GIHWR = df.GIHWR.str.rstrip('%').astype('float') / 100.0

    df.GIHWR.hist()

    plt.show()




if __name__ == "__main__":
    main()