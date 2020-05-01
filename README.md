# nfa

nfa.py will read in a text file called nfa.txt and construct a NFA. Then it reads in input.txt to determine whether each input strings can be accepted or not by the NFA. The result is reflected in output.txt as each line contains the result "accetpt" or "reject" for every line in input.txt.

nfa.txt and input.txt files are grouped together.

input.txt contains strings on each line that will run on the NFA.


nfa.txt: an NFA schema recognizing when users are using commenting functions in programming languages (similar to C++ multi-line comment). 
nfa_2.txt: example provided by the professor.

Files "nfa.txt" and "nfa_2.txt" are different test files for nfa.py. Both test cases produced consisent answers identical to the results from manually contructed DFAs.

The structure of nfa.txt will be as follows:

 Line 1: the states of the NFA (separated by commas, if there is more than one state)
 
 Line 2: the alphabet of the NFA (separated by commas, if there is more than one symbol)
 
 Line 3: the starting state of the NFA
 
 Line 4: the final/accept states of the NFA (separated by commas, if there is more than one accept state)
 
 Line 5 and onward: the transition rules, where each rule takes the form a,b,c (where being in state a and reading symbol b transitions to new state c)
In addition to the given alphabet, all NFAs may also contain empty-string transitions (the character "@" is used to represent an empty string).


