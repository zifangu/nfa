"""
1. read in dfa.txt
2. put states, alphabets, start states, final states into separate lists
3. rules: a list of list of transition rules:[[start_state, elements, reached_state], ...]
4. read in input.txt, start collecting paths
5. create a list of states need to be processed for the next element in the path.
5.5 the result of the process list is the new process list to operate with the next element
6. loop until the last char on the line is reached
7. compare the returned result to the list of final states
"""


def open_file(filename):
    file = open(filename, "r")
    content = file.readlines()
    file.close()
    return content


def fill_in_start_final(nfa):
    start_state = ""
    final_states = []
    dictionary = {}
    counter = 0
    for line in nfa:
        line = line.strip()
        if counter == 2:
            start_state = line
            # print(start_state)
        elif counter == 3:
            final_states = line.split(",")
        counter += 1

    return start_state, final_states


def rules(nfa):
    transition_rules = []
    counter = 0
    for line in nfa:
        line = line.strip()
        if counter > 3:
            transition_rules.append(line.split(","))
        counter += 1
    return transition_rules


def process_list_check_empty(start_state, rules):
    # returns the new list need to be processed after checking empty string transition
    new_list = [start_state]
    for i in rules:
        if (i[0] == start_state) and (i[1] == '@'):
            new_list.append(i[2])
    return new_list


def dictionary_ivan(start, path, trans_rules):
    end_state = []
    for i in trans_rules:
        if (i[0] == start) and (i[1] == path):
            end_state.append(i[2])
    return end_state



def main():
    # opens the dfa.txt file and creates dictionary connecting the tuples and key
    nfa = open_file("nfa.txt")

    start_state, final_states = fill_in_start_final(nfa)
    transition_rules = rules(nfa)
    # print(process_list_check_empty('s1', transition_rules))

    # read in the transition paths
    trans_path = open_file("input.txt")
    path = []
    for line in trans_path:
        line = line.strip()
        path.append(line)

    pro_list = process_list_check_empty(start_state, transition_rules)






    print("start:", start_state)
    print("final:", final_states)
    print("rule:", transition_rules)



if __name__ == '__main__':
    main()