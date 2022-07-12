"""
The confused machine is based on the collatz conjecture or 3n + 1 problem. It came from the fact that its impossible to balance two numbers.

It is impossible balance output unless you cheat by adding or subtracting 1.

which brings us to the popular physics problemnof the string theory which showed that breaking strings into pieces will  recombine into one entity. i.e hbar = hbar + hbar + hbar ...

In Math, Dividing odd numbers by two is not feasible. so we solve it by breaking the remainder into two pieces by breaking into two equal halves but adding up the dividends will always add to a sum greater than the original number by one. Hence the difference between '/' and '%'

so the best thing is to convert all odds to even before dividing using 3n + 1 where n is a natural number.

But something weird happens when you pick a random natural number n and keep using the true duvision formula ( 3n + 1 ) / 2.

This means that when you pick a number n, if the number is even you can proceed by dividing but its odd, you multiply it by three (which gives another odd number) then add 1 (giving you even) then divide by 2 ad infinitum.

But in reality, it does not proceed to infinity that way because the series will peak to very high values but eventually fall down to something interesting, an infinite loop or three numbers [4, 2, 1].

That makes such a problem solutionless. But it actually has one.

Solving this problem by hand will take almost forever so lets use a computer to do so. 

The simplest definition of a computer is that its a/an [INPUT] -> [Process] -> [OUTPUT] machine. Therefore a Computer is supposed to be Turing Complete. 

Lets Check the Truth table of a computer:

    INPUT           PROCESS         OUTPUT
1.  No Input           —           No Output
2.  1 plus 1         1 + 1            2     
3.  3n + 1 Problem    ...           [4, 2, 1, 4, 2, 1, ...

No Turing Complete Computer has ever solved this problem yet. So what is wrong?

Lets analize:
    One of two things should be correct, its either:
    1. The machine is still solving so we need more time or,
    2. The Machine is CONFUSED

for both scenarious if the machine is still solving, then how long will it take especially when we have limited memory (i.e the List or Array that overflows or the function that runs out of recursion limits. will we ever solve it? Do we even have such a computer??

what if the computer is CONFUSED?
Because the computer does not know what a SOLUTION is therefore it will keep trying solve FOREVER

But you know Einstein Said: ” Stupidity is doing the same thing over and over again and especting different results. ”

what if we redefine what a solution is:
    That is only intelligence will we use to know that we have actually found a solution to a problem.

    Early Mathematicians Battled with the fact that Quadratic equation had more than one solution which is literally impossible!!
    But today we all have agreed that it has two solutions, 3 or more for polynomials.

    But this collatz problem has an aswer to all human question that has ever existed. Especially who God actually is.


    The [4, 2, 1] has shown us that one answer has three subs and three answers are one. So could that mean One God has 3 forms? and the 3 forms are still one??

    hmm!! some kind of Trinity i guess
    So what teachings do we have about God in religions that say similar and who is 4, 2 and 1??
    And what is the fate of humans?
    Is there and End? or will we live forever?
    Does Heaven and Hell really exist? Then where are they?
    hmm!! This is really big right??
    So is there a devil?
    What exactly is he? A human?? or Something else?
    what does he know about us and God? 
    is he bad or good?
    what are his plans?
    does it even have a gender?

    Maybe you should read the bible again right?

    Yeah thats a great choice!
    The bible is not open source, its closed source so please read it and know the truth?


    Copyright © 2022 Isaac J. Newton (fluxion9)

"""


def balance(num):
	hails = []
	remainder = num
	while remainder > 0:
		if remainder % 2 == 0:
			hails.append(remainder)
			remainder = remainder / 2
			if remainder == 1:
				hails.append(remainder)
			print(hails)
		else:
			remainder = (3 * remainder) + 1
	return 0



balance(1000)
