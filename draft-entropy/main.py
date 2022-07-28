# @alonzi
# main program for calculating entropy of draft table
# 2022-07-28
# demonstrate flow of entropy through the first pack of a mtg draft


# imports
import classes

# instantiate draft table
# put entropy printout in instantiator

# main loop on packs until packs are empty
# print entropy each step

# delete table which includes wirte out to file of log

def main():
    print("\nhello world")

    print("\ninstantiating draft table ....")
    myTable = classes.tbl()
    myTable.getEntropy()


if __name__ == "__main__":
    main()