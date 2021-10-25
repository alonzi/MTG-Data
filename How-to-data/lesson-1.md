# Lesson 1: Scalars and Vectors and Tensors, oh my!
Hello and welcome to the first lesson in "How to Data". In this series we will look at how to use data. For the first lesson we will start a the very beginning. When you think about data you must start with thinking of data as a collection of information containers. We will break down the building blocks and apply them to decision making.

## Step 1: Identify your goal
For this lesson we will focus on two decisions a player makes during a limited game of magic.
1. Which card to draft?
2. Which card to play on turn 5?
Throughout the lesson we will refer to these two questions. Along the way we will me our friends, the scalar, the vector, and the tensor.[1]

## Step 2: Definitions
These are the definitions we are going to use for this lesson.
1. A scalar is a number.
2. A vector is a group of scalars.
3. A tensor is a group of vectors. [2]

## Step 3: Let's get into it, answering question #1 Which card to draft?
Now things are going to get fun. Let's run out a little thought experiment and apply our new thinking. Imagine you are in a draft, it is pack 1 pick 1, you crack the pack and have to make a choice. What do you pick? and How much information do you need? Do you need a scalar? a vector? or something more complex?

I would argue there are two answers:
1. a vector
2. the collective knowledge of the universe, past, present, and future (CKotUPPaF).

For the sake of our work here today. Let's focus on the answer being #1 a vector. And to understand that first we need to dig into what a scalar is.

### Our friend, the scalar
A scalar contains a number, a single piece of information. For example LSV would call Lunarch Veteran a '3.5'.
![](https://media.wizards.com/2021/mid/en_uB38jn7tMk.png)
LSV would also call Flip the Switch a '3.5'.
![](https://media.wizards.com/2021/mid/en_VhfxQodv2N.png)
And finally he would say that '3.5' means "Top-tier common or solid uncommon." [3]

And here we have the crux of the challenge when working with scalars. All three of those things "Lunarch Veteran", "Flip the Switch", and "Top-tier common or solid uncommon" are equivalent. They are all the same as 3.5. Let that sink in.

#### When we talk in terms of scalars we take lots of information and compress it into a number.
#### Lunarch Veteran = Flip the Switch

Now ask youself the question, would you have a hard time deciding between these two cards in pack 1 pick 1? (ignore the rest of the pack, in fact you can pretend these are the only two cards in the pack)

For me the answer is no. In that context I don't think it is a hard decision. We need something more. We need a vector.

### Our friend, the vector.
Let's dig into Lunarch Veteran a bit more. Let's make a vector out of it. For this we will look to the popular scalar "GP WR" aka Games Played Win Rate. [4]
* 58.1%
What a beautiful scalar we have. If you play a copy or more in your deck and hit the 17 lands average you have a 58.1% win rate. Now as we saw above this single number compresses a lot of information down into one point. So let's unpack it. Let's use deck color pair:
* 58.1%
  * WU --> 60.0%
  * WB --> 57.7%
  * RW --> 55.0%
  * GW --> 57.7%

And now we have our first vector. The GP WR for Lunarch Veteran by deck color. We have four scalars, one for each deck color pair, and when we combine them we get a vector.

But we don't have the CKotUPPaF, so we don't know what color pair we will wind up in, or if we will even have a deck that can play a white card, let alone, Lunarch Veteran. For the moment let's not add that complexuity, keep it simple.

### Let's bring in another vector
Let's step back from Lunarch Veteran for a moment and look at the four components of that vector, the deck color pairs and their sucess. Here we have another vector.
* WU = 59.1%
* WB = 56.7%
* RW = 55.3%
* GW = 57.6%

If we look at this vector and you had to choose which color pair to play, which would you choose? [5]

### Put the vectors together!
Now when we look at these two vectors simultaneously we can really see something. White Blue (WU) is tops on both lists. This is really telling us something. [6]

### But don't I need to worry about the average win rate of a 17 lands user?
Well, I'm glad you brought that up. The percentages we are looking at are based on data from 17 lands users. So in order to understand them in an absolute context we do need to know the typical winrate for a 17 lands user. However, what we are doing here is comparing two vectors pulled from the same dataset. And the beauty of a comparison like this is that any systematic bias present cancels out [7].

In this case both rates are pulled from 17 lands so whatever base win rate we experience from 17 lands is the same in both instances and therefore cancels out.

### But Pete, you said we only needed a scalar?
I did say we only needed a scalar. But I know you thinking, let's take a look at the vectors for Flip the Switch. I got you.

* Flip the Switch (GP WR)
  * WU = 59.3%
  * UB = 58.8%
  * UR = 53.7%
  * UG = 57.1%

* Blue color pair win rates
  * WU = 59.1%
  * UB = 58.1%
  * UR = 53.7%
  * UG = 57.6%

Taking a look here we see the standout is again White Blue (WU) but the gap is not as big. WU is still the highest on both lists but the next highest pair is not as far behind.

So what are we to make of this and why is Pete insiting a scalar can get the job done?

## Remeber when we learned scalars are distilled information?
So here is where we return to the scalar. It turns out that pack 1 pick 1 decisions are so important that the pros have gone to great lengths to figure out all of this high level analysis and distill it down to a scalar. That would be a pick order. You can look up the rank for every card in the format and find out what order you are reccomended to take it, pack 1 pick 1. You can find an example on Channel Fireball from Frank Karsten [here](https://strategy.channelfireball.com/all-strategy/cfb-pro-content/pick-order-for-innistrad-midnight-hunt-limited/).

If we consult this list we see that Lunarch Veteran ranks #4 in the C- tier and Flip the Switch ranks #7 in the D tier. So based on Frank's ratings from September 15, 2021 I would easily select Lunarch Veteran over Flip the Switch.


### Let's talk a little more about scalars
When you make a scalar you do so for a purpose. In the case of Frank's pick orders it was speicfically for "answering the question 'which card would you first-pick?' ". He went to the trouble of working out that scalar for this case because pack 1 pick 1 is just that important. Taking a look at LSV rating them both 3.5 we see his purpose was that "the grade can help show you where it lands when all is said and done". LSV is shooting for a more general scalar whereas Frank is targeting pack 1 pick 1.


## Part 2: Which card to play?
So you may be wondering when I was going to come around to talking about using this approach for deciding which card to play on turn 5. Well I hope you can see by now that the answer is, "You need a lot more than a scalar". And that is what we are going to get into next time. Simply playing the card with the highest GP WR isn't going to get the job done.

### Bonus Note
A lot of you may be thinking, "What is relevance of pick orders form the beginning of the format?" This is a great question!

Answer:
1. You're right. More recent pick orders would probably be more helpful because they have been updated with newer information.
2. The point was to demonstrate the scalar and it's purpose, not to actually say what the right pick is.
3. Reflect on the point about bias canceling out when comparing. Do you think Lunarch Veteran is a better pick than Flip the Switch?








### Footnotes for the nerds
1. I totally hear you that scalars and vectors are tensors. Believe me I want to go there. But for now please chill and don't @ me. We have a foundation to build first.
2. Again, nerds. Chill out. Don't @ me.
3. https://strategy.channelfireball.com/all-strategy/cfb-pro-content/lsvs-innistrad-midnight-hunt-limited-set-re-review/
4. Data courtesy of https://www.17lands.com/
5. Spikes only! https://magic.wizards.com/en/articles/archive/making-magic/timmy-johnny-and-spike-2013-12-03
6. In math form if you prefer: 
7. Yeah yeah yeah, I know, I know, I'm talking leading order, which is enough to get us there.