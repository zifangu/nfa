# nfa

The structure of nfa.txt will be as follows:

 Line 1: the states of the NFA (separated by commas, if there is more than one state)
 
 Line 2: the alphabet of the NFA (separated by commas, if there is more than one symbol)
 
 Line 3: the starting state of the NFA
 
 Line 4: the final/accept states of the NFA (separated by commas, if there is more than one accept state)
 
 Line 5 and onward: the transition rules, where each rule takes the form a,b,c (where being in state a and reading symbol b transitions to new state c)
In addition to the given alphabet, all NFAs may also contain empty-string transitions (the character "@" is used to represent an empty string).


input.txt contains strings on each line that will run on the NFA.

nfa.py will read in a text file called nfa.txt and construct a NFA. Then it reads in input.txt to determine whether each input strings can be accepted or not by the NFA. The result is reflected in output.txt as each line contains the result "acctpt" or "reject" for every line in input.txt.