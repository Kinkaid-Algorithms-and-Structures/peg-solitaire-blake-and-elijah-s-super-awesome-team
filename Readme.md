CLA&S	August, 2024

First Project: Peg Solitaire

This first project is going to be mostly about getting comfortable with Python, including some features I want you to acclimate to, as well as revisiting Github. You are going to be making a text-based version of "Peg Solitaire" (a.k.a., "[The Cracker Barrel puzzle](https://blog.crackerbarrel.com/2021/08/13/how-to-beat-the-cracker-barrel-peg-game/)"). This consists of a triangular-shaped board with 15 small holes (`o`) in it:


```
                    1
                    o
                  2/ \3
                  o — o
                4/ \5/ \6
                o — o — o
              7/ \8/ \9/ \10
              o — o — o — o
            11/ \12/ \13/ \14/ \15
            o — o — o — o — o
```


(This is one way of displaying it… feel free to come up with your own. You might choose to use emoji or colors, for example. Or you might omit the hexadecimal numbers and just show row numbers on the left side and ask for a cell within the row afterwards.)

The board starts with all but one of the holes filled in. (I suggest a visually dense character like "@" if you are just using a plain text version.) The goal is to ask the player to select a peg and "jump" it over a neighboring peg to an empty hole on the far side, removing the "jumped" peg. (Like checkers.) For example, consider the following, where the user has selected to move the peg in hole 4 to the one in hole 1, removing the peg in hole 2:


```
                1	                1
                o	                @
              2/ \3	              2/ \3
              @ — @	              o — @
            4/ \5/ \6	            4/ \5/ \6
            @ — @ — @	            o — @ — @
          7/ \8/ \9/ \A	          7/ \8/ \9/ \A
          @ — @ — @ — @	          @ — @ — @ — @
        B/ \C/ \D/ \E/ \F        B/ \C/ \D/ \E/ \F
        @ — @ — @ — @ — @        @ — @ — @ — @ — @
```


	Before	After

_Note that hole 1 was empty but now is filled, and both holes 2 and 4 were filled but now are empty._

_Note 2: Now you could move 6 → 4 or B → 4 or D → 4 or 9 → 2, but there is nowhere you can move 8 yet._

… and the goal is to remove all the pegs you can, while there are still legal moves.



How you choose to represent this in memory is up to you, and you should spend a bit of time thinking about this. Here are a few possibilities:



* A 1-D array:

    ```
    1 2 3 4 5 6 7 8 9 A B C D E F
    ```


* A list of lists of varying lengths:

    ```
    	1

    		2 3
    		4 5 6
    		7 8 9 A
    		B C D E F

    ```



* A 2-D array, with unused (out of bounds) spots:

    ```
    	1 _ _ _ _	_ _ _ _ 1 _ _ _ _
    	2 3 _ _ _ 	_ _ _ 2 _ 3 _ _ _
    	4 5 6 _ _   or	_ _ 4 _ 5 _ 6 _ _
    	7 8 9 A _	_ 7 _ 8 _ 9 _ A _
    	B C D E F	B _ C _ D _ E _ F

    ```


There may be other ways out there, too.


## The project

You are going to write this in teams of 2 people, in python. The teams are:

(TBA - see Canvas)


And here is the link to the (generally empty) starter code: (If you go here, you've already found the link.)

Along the way, there are some things I want you to make sure you are using, so that you come to understand them:



* Your printing should be using "f-strings" (unless you aren't printing any variables, of course).
* You should have at least one method that returns two values (and the method that calls it should read both values).
* You should use type hints for your method parameters and return values.
* You should use classes in separate files, particularly since you'll want to have two people programming! I suggest you separate the logic of the game from the user interface.
* Avoid using tons of "if" statements to establish the relationships between adjacent holes. Try to find generalizable connections between them. (e.g., math)



I STRONGLY ADVISE you and your partner do some planning before you launch into coding. Here are some questions you might include in your thinking:


**Project structure**



* What data structure _should_ we use for the board? What are we storing?
* What are the possible mathematical relationships between a starting hole, a "jumped" hole and a destination hole?
* How _do_ we want to display the board?

**User interactions / game flow**

* How do we ask the user which move to make?
* How do we check the user is making legal requests?
* What do we do if the user tries to make an illegal move?
* What do we do if the user has picked a peg that has no options?
* How do we decide whether the game is over?
* When we ask the user to pick a peg, do we then ask for a destination, or do we offer possible moves and let the user pick one?

**Your organization**

* How are we going to decide who does what?
* How do we communicate with each other about the parts of the program we'll need? (e.g., UML diagram, program "bible," mind meld, lots of texts, wishful thinking, …)
* How often do we want to check in with each other? How much do we want to work independently?
* How will we test that the portions of the code we write are working properly early on, so we don't have to debug five million errors when we are trying to integrate the parts?
* How can we support each other if one of us gets stuck?


## Extensions

I'm not really expecting that you will have a lot of extra time for this one, but a few ideas I have for taking this the next step forward are: snazzing up the appearance of the board, making a thoughtful user interface that makes the game easy to understand and play, or building an "undo" stack.


## Academic Integrity

This is a group project, and it's also a project that is the first of the year in a language that is either new or rusty for most of you. Naturally, you're going to talk to your partner, and you're going to need to look up how to do some things, either from class notes or online (e.g., Stack Overflow, Geeks for Geeks). Here are the things that might cause Academic Integrity issues:

**_Online resources:_** You are welcome to search online for ways to use language features, like lists, f-strings, loops, conditional statements, type hints, etc., but you should NOT be taking large swaths of code from such sites. (One or two lines, like what you might get if you asked "how to print 'n' spaces in Python" are ok.) Furthermore, you should not be asking "how do I write the Cracker Barrel puzzle in Python?"

**_Artificial Intelligence_**: Please do not use AI to write your code for you on this project. Yes, when you do a google search these days, the first thing that pops up is often an AI summary of the search results. That's fine. But don't go to Flint/ChatGPT and ask it to write you an out-of-bounds method for a triangular board or to debug a method that isn't working.[^1]

**_People_**: By all means you should talk with your partner. You might also have conversations with members of other groups, but I would set the same guidelines as the Online resources. Asking a neighbor the difference between a Tuple and a List, or how to do type hints is fine. But you shouldn't be talking about how you are answering the starred questions above during the planning phase or exchanging code chunks. Later, you are welcome (and encouraged) to playtest other groups' programs.

If in doubt, ask Mr. Howe!


<!-- Footnotes themselves at the bottom. -->
## Notes

[^1]:
     I mention Flint here because we are moving school-wide to say that any AI use should be done through Flint's ChatGPT access, not a stand-alone ChatGPT, for instance. But in this case, I don't want you using Flint, either.











<!-- watermark --><div style="background-color:#FFFFFF"><p style="color:#FFFFFF; font-size: 1px">gd2md-html: xyzzy Mon Aug 12 2024</p></div>

