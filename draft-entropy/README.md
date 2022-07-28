# Draft Entropy Study
The goal of this study is to understand how much information a player gets at the draft table. This can possibly lead to insights about signaling when taken in concert with Sierkovitz's analysis from: [Magic Numbers #35: Reading The Signals](https://www.youtube.com/watch?v=GeZFlfWx_J0&t=5017s)


# Questions
1. what is the entropy of an SNC pack -- 61 bits (upper bound) - assuming all p1p1 are rare/mythic and no color/gimick constraints
2. what is the entropy of an SNC table -- 484 bits (upper bound) - just multiply by 8 seats
   2a. once you open your first pack -- 484 - 61 bits
   2b. once you 
3. does the rare slot contain any information, if so how much? 5.7 bits or log(20)/(8 log(2)) + (7 log(60))/(8 log(2)) to be exact (maximum) but reality of rare drafters means it must be lower


4. Entropy of the packs (0-7) as a function of pick number
4. Entropy of the players (0-7) as a function of pick number

5. What is the entropy of each other seats pool as a function of pick
6. The objective is color information, in a sense we can reduce all the numbers by 5

8. how much information can you pick up at what point (graph, information gained v pick# and cumulative) 


## Useful Links:
* rarity explanation: https://draftsim.com/mtg-rarity/
* booster composition SNC: https://magic.wizards.com/en/articles/archive/feature/streets-of-new-capenna-product-overview-2022-04-07
* wolfram alpha: https://www.wolframalpha.com/

## Assumptions
* like arena - no foils
* too hard to enforce color/gimick selection - extra credit


## Strategy
* conduct analysis assuming p1p1 is a rare? just look at pack 1?



# Definitions
Entropy is missing information aka how much info you need to determine a system
==> in this case the entropy of a pack is how much information you need to know every card



## Constants
| Variable | Value | Notes |
|----------|-------|-------|
|Nup       | 1578502390319254400 | number of unique packs|
|Pup  | 1./Nup = 6.3x10^-19 | probability of a given unique pack|
|NU   | 80 | number of uncommons|
|NUpp | 3 | number of uncommons per pack|
|NC   | 101 | number of commons|
|NCpp | 10 | number of commons per pack|

## Derived Quantities
Entropy of a pack = log2(Nup) = log(2, binomial(80, 3) binomial(101, 10)) = 60.453262153291854508268550281981164583609486916645009310957956923... bits
  * nb: some of these combinations aren't possible because of color/gimick rules so this is actually an upper bound
  * nb: this is under the no rares assumption since there are 80 potential cards for the rare slot you are looking at roughly and additonal 6 bits of information

## Findings
1. As the draft proceeds the entropy flows from the table to the other drafter's pools
