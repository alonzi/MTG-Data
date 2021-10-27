# Scalar Theory
I am writing this article to directly respond to the constant refrain of "but Game in Hand Win Rate doesn't tell the whole story". I absolutely agree that it doesn't tell the whole story. My objectives are to:
1. Provide some of the data science behind Game in Had Win Rate (GIH WR)
2. Equip the reader to understand numbers like GIH WR
3. Help the reader put this understanding into practical use. 

I am calling this framework Scalar Theory [1]. We will need to dip into a little jargon, namely the idea of a scalar and the broader area of information theory, so brace yourself. We will start by defining a scalar, and then discuss the fundamental principles of Scalar Theory with examples. Let's go!

## What is Game in Hand Win Rate (GIH WR)?
Game in Hand Win Rate is defined by 17 Lands as: 

`The win rate of games where an instance of this card appeared in the hand, either in the opening hand or later. Each instance of a card is counted, so a game having a copy of a card in the opening hand and then two more copies drawn later has three times as much weight as an opening hand with only one copy.`

But for our purposes here we will call it a `scalar`.

Our working definition of `scalar` will be: A scalar is a number.

Here are a few examples of scalars:
* Game in Hand Win Rate - eg: 57.5% [2]
* Frank Karsten's Pick Order - eg: 97 [3]
* LSV's rating for a card - eg: 3.5 [4]
* The number of Stuffed Bear's I have played in MID premier draft - eg: 0 [5]

All of these examples are numbers, they are all scalars. Understanding how to use them requires context. Contex is the key, when people say "but Game in Hand Win Rate doesn't tell the whole story" what they are saying is "that number doesn't have all the information you need". It lacks context.

For example, GIH WR doesn't tell you how a card was used in a game, it doesn't tell you the quality of the opponents, or even how many games are in the sample used to calculate GIH WR. All of these features are part of the context and you have to bring those yourself, a scalar isn't going to do that for you.

## The first fundamental principle of Scalar Theory
When you use a scalar, make sure you apply it in context.

## Let's get some context
Time to get practical. Let's consider two scalars:
1. Frank Karsten's pick order
2. 17 Lands Game in Hand Win Rate

### Context 1
You have just started a draft, it is pack 1 pick 1. Which scalar would you rather have for each card in the pack?
1. Frank Karsten's pick order
2. 17 Lands Game in Hand Win Rate

I am going to trust Frank because this is the exact context for which he created that scalar. Using it here is a perfect context match. [6]

### Context 2
You are most of the way through a draft, you know you are playing White Blue (aka WU), and are choosing between Lunarch Veteran and Flip the Switch. Which scalar would you rather have for each card?
1. Frank Karsten's pick order
2. 17 Lands Game in Had Win Rate

I am going to consider the 17 Lands GIH WR. I've made a different choice because the context is different. But there are some caveats, and that's the rub. When context isn't a perfect match we have caveats.

### So what is the context for Game in Hand Win Rate?
I've stated that we need to know the context to apply a scalar. But what exactly is the context of "Game in Hand Win Rate"? 

First let's reflect on Frank's pick order. The context was explicity stated as, "for the purpose of the first-pack, first-pick (P1P1) decision in draft, answering the question “which card would you first-pick?” for every conceivable booster pack. ' He chose a particular game state and made a scalar just for that state. We have a perfect context match. If it is pack 1 pick 1 we know exactly how to interpret Frank's pick order. Now play the tape forward. As every additional pack comes in we move further from the context of Frank's pick order and start adding more and more caveats.


The challenge with Game in Hand Win Rate is that its context is not a game state of a Magic game. You will never be in the exact context of GIH WR. So what do we do given the fundamental principle of Scalar Theory? How can we use GIH WR if we are never in its context and caveats abound. [7]

## The second fundamental principle of Scalar Theory
If the contex is not a perfect match there are caveats.

## Is it usesless to consider Game in Hand Win Rate?
Not at all. Let's look at the definition again:

`The win rate of games where an instance of this card appeared in the hand, either in the opening hand or later. Each instance of a card is counted, so a game having a copy of a card in the opening hand and then two more copies drawn later has three times as much weight as an opening hand with only one copy.`

Here we can see that this scalar contains information about the effectiveness of a card for achieving our goal of winning a game. That is valuable. But let's look again at our sample contexts: pack 1 pick 1, and mid draft after we have decided on a color pair. In these contexts we are trying to find pieces for our deck. What we would really like to have is:

`The probability that drafting this card will improve our win rate in the current draft event.`

Then we could simply compare the value of this scalar for all the cards and make the correct selection. Of course this requires the collective knowledge of the universe, past, present, and future (CKotUPPaF). Which is something we will never have. So let's look at the difference between these two definitions and find some overlap.

GIH WR contains information about how a card impacts your win rate and our imaginary scalar also contains information about how a card impacts our win rate. Some kernel of the information we are after is contained in GIH WR. And GIH WR is a knowable value! I can look it up.

### Context 2 revisited
You are most of the way through a draft, you know you are playing White Blue (aka WU), and are choosing between Lunarch Veteran and Flip the Switch.They have the following GIH WR:
* Lunarch Veteran - 60.6%
* Flip the Switch - 60.1%

But let's add a little more context. We know we are playing White Blue (WU) so now let's look at GIH WR for WU decks:
* Lunarch Veteran - 62.3%
* Flip the Switch - 60.5% 

Both cards look better but Lunarch Veteran looks even better. Given this information I am leaning Lunarch Veteran base on this information.

But remember the second fundamental principle of Scalar Theory. We are not in a perfect context match. Our context is drafting, but our scalar (GIH WR) is about cards being in a player's hand. So there caveats. For example, what are the other cards I have drafted?

## Core question of Scalar Theory
Is my context close enough to the context of the scalar?

If not what caveats must I consider before using the scalar.

Answering this question for GIH WR is very tricky. The context of GIH WR is not defined in the basis of Magic game states.


# Summary
* Fundamental Principle #1: When you use a scalar, make sure you apply it in context.
* Fundamental Principle #2: If the contex is not a perfect match there are caveats.
* Core question to ask: Is my context close enough to the context of the scalar?


Thanks for reading. I hope you enjoyed this piece. [About the author](https://github.com/alonzi/MTG-Data/blob/b4c21adc50da5804015552fe2445cea5df8c4c60/about-the-author.md)

### Footnotes
1. The term Scalar Theory is an homage to Quadrant Theory from Brian Wong on Limited Resources: https://lrcast.com/limited-resources-184-card-evaluation-with-brian-wong/
2. https://www.17lands.com/card_ratings
3. https://strategy.channelfireball.com/all-strategy/cfb-pro-content/pick-order-for-innistrad-midnight-hunt-limited/
4. https://strategy.channelfireball.com/all-strategy/cfb-pro-content/lsvs-innistrad-midnight-hunt-limited-set-re-review/
5. https://media.wizards.com/2021/mid/en_9KarCuKRcO.png
6. Which is not to say Frank has the ideal pick order, but I can assure you at any point in time he is very likely to have the better pick order than me.
7. In case you are wondering it is this never ending parade of caveats that make data anlysis hard and also what separate pro magic players from people like me.
