# Scalar Theory
I am writing this article to directly respond to the constant refrain of "but Game in Hand Win Rate doesn't tell the whole story". I absolutely agree that it doesn't tell the whole story. My objective is to provide some of the data science behind that number and equip the reader to understand numbers like it. I am calling this principle Scalar Theory. We will need to dip into a little jargon, namely the idea of a scalar. So we will start by defining a scalar and the core principle of scalar theory. Then get into examples. Let's go!

## What is Game in Hand Win Rate (GIH WR)?
Game in Hand Win Rate is defined by 17 Lands as: 

`The win rate of games where an instance of this card appeared in the hand, either in the opening hand or later. Each instance of a card is counted, so a game having a copy of a card in the opening hand and then two more copies drawn later has three times as much weight as an opening hand with only one copy.`

But for our purposes here we will call it a `scalar`.

Our working definition of `scalar` will be: A scalar is a number.

Here are a few examples of scalars:
* Game in Hand Win Rate - eg: 57.5% [1]
* Frank Karsten's Pick Order - eg: 97 [2]
* LSV's rating for a card - eg: 3.5 [3]
* The number of Stuffed Bear's I have played in MID premier draft - eg: 0 [4]

All of these examples are numbers, they are all scalars. Understanding how to use them requires context. Contex is the key, when people say "but Game in Hand Win Rate doesn't tell the whole story" what they are saying is "that number doesn't have all the information you need". It lacks context.

## Core principle of Scalar Theory
When you use a scalar, make sure you apply it in context.

## Let's get some context
Time to get practical. Let's consider two scalars:
1. Frank Karsten's pick order
2. 17 Lands Game in Hand Win Rate

### Context 1
You have just started a draft, it is pack 1 pick 1. Which scalar would you rather have for each card in the pack?
1. Frank Karsten's pick order
2. 17 Lands Game in Hand Win Rate

I am going to trust Frank because this is the exact context for which he created that scalar. Using it here is a perfect context match. [5]

### Context 2
You are about halfway through a draft, you know you are playing White Blue (aka WU), and are choosing between Lunarch Veteran and Flip the Switch. Which scalar would you rather have for each card?
1. Frank Karsten's pick order
2. 17 Lands Game in Had Win Rate

I am going to consider the 17 Lands GIH WR. I've shifted my choice because of the context. But, there are some caveats, and that's the rub. When context isn't a perfect match we have caveats.

### So what is the context for Game in Hand Win Rate?
I've stated that we need to know the context to apply a scalar. But what exactly is the context of "Game in Hand Win Rate"? When we think about Frank's pick orders it was straight forward, he said, 'for the purpose of the first-pack, first-pick (P1P1) decision in draft, answering the question “which card would you first-pick?” for every conceivable booster pack. ' That is some pretty clear context. He chose a particular game state and made the scalar for that state. However we do not have that clear game state definition for GIH WR.

The challenge with Game in Hand Win Rate is that its context is not a game state of a Magic game. When Frank publishes his pick orders he presents that scalar in the exact context of a Magic game, namely pack 1 pick 1. However there is never a moment in a Magic game where you have the context of a Game in Hand Win Rate.

### So is it usesless to consider Game in Hand Win Rate?
Not at all. Let's look at the definition again:

`The win rate of games where an instance of this card appeared in the hand, either in the opening hand or later. Each instance of a card is counted, so a game having a copy of a card in the opening hand and then two more copies drawn later has three times as much weight as an opening hand with only one copy.`

Here we can see that this scalar contains information about the effectiveness of a card for achieving our goal of winning a game. That is valuable. But let's look again at our sample contexts: pack 1 pick 1, and mid draft after we have decided on a color pair. In these contexts we are trying to find pieces for our deck. What we would really like to have is:

`The probability that drafting this card will improve our win rate in the current draft event.`

Then we could simply compare the value of this scalar for all the cards and make the correct selection. Of course this requires the collective knowledge of the universe, past, present, and future (CKotUPPaF). Which is something we will never have. So let's look at the difference between these two definitions and find some overlap.

GIH WR contains information about how a card impacts your win rate and our imaginary scalar also contains information about how a card impacts our win rate. Some kernel of the information we are after is contained in GIH WR. And GIH WR is a knowable value. I can look it up. The question is ...

## Core question of Scalar Theory
Is this context close enough to the context of the scalar?

Answering this question for GIH WR is very tricky. The context is not defined the basis of Magic game states.





### Footnotes
1. https://www.17lands.com/card_ratings
2. https://strategy.channelfireball.com/all-strategy/cfb-pro-content/pick-order-for-innistrad-midnight-hunt-limited/
3. https://strategy.channelfireball.com/all-strategy/cfb-pro-content/lsvs-innistrad-midnight-hunt-limited-set-re-review/
4. https://media.wizards.com/2021/mid/en_9KarCuKRcO.png
5. Which is not to say Frank has the idea pick order, but I can assure you at any point in time he is very likely to have the better pick order than me.
