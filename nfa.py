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
    start_state = []
    final_states = []
    counter = 0
    for line in nfa:
        line = line.strip()
        if counter == 2:
            start_state.append(line)
            # print(start_state)
        elif counter == 3:
            final_states = line.split(",")
        counter += 1

    return start_state, final_states


def rules(nfa):
    # return as list of transition rules
    transition_rules = []
    counter = 0
    for line in nfa:
        line = line.strip()
        if counter > 3:
            transition_rules.append(line.split(","))
        counter += 1
    return transition_rules


def process_list_check_empty(start_state_list, rules):
    # returns the new list need to be processed after checking empty string transition
    new_list = start_state_list
    for ele in start_state_list:
        for i in rules:
            if (i[0] == ele) and (i[1] == '@'):
                # print(i[0], i[1])
                new_list.append(i[2])
                # print("new list:", new_list)

    # remove duplicates in the list
    new_list = list(dict.fromkeys(new_list))
    return new_list


def dictionary_ivan(start, path, trans_rules):
    # custom dictionary look up because the duplicates in keys and values
    end_state = []
    for i in trans_rules:
        if (i[0] == start) and (i[1] == path):
            end_state.append(i[2])
    return end_state


def get_next_pro_list(pro_list, path, trans_rules):
    # given a element and initial processing list, returns the next list to be processed
    new_pro_list = []
    for i in pro_list:
        temp = dictionary_ivan(i, path, trans_rules)

        # if empty transition the original state also needs to be included in the processing list
        if path == "@":
            temp.append(i)
        for j in temp:
            new_pro_list.append(j)
    return new_pro_list


def get_final_state_list(path_list, trans_rules, initial_state):
    # given the initial state, returns the list of final states
    temp_state = initial_state
    temp_list = []
    # traverse each path
    for i in path_list:
        # check if empty strings are involved. If so, add the states after the empty string to the processing list
        print("temp list before:", temp_list)
        temp_list = process_list_check_empty(temp_state, trans_rules)
        print("temp list after:", temp_list)

        # find next processing state with the given path element
        temp_list = get_next_pro_list(temp_list, i, trans_rules)
        print("next process list:", temp_list, "\n")

        # the next processing state may also contain empty transitions. Check those
        temp_list = process_list_check_empty(temp_list, trans_rules)
        temp_state = temp_list
    return temp_list


def write_result(file, result_list, final_states):
    counter = 0
    for i in result_list:
        if i in final_states:
            counter += 1
    if counter >= 1:
        file.write("accept\n")
    else:
        file.write("reject\n")


def main():
    # opens the nfa.txt file
    nfa = open_file("nfa.txt")

    # set initial and final states
    start_state, final_states = fill_in_start_final(nfa)

    # set the transition rule
    transition_rules = rules(nfa)

    # read in the transition paths
    trans_path = open_file("input.txt")
    path = []
    for line in trans_path:
        line = line.strip()
        path.append(line)
    print("path:", path)

    # iterate through paths and find the state the given string is ending
    output = open("output.txt", "w+")
    for i in path:
        result_list = get_final_state_list(i, transition_rules, start_state)
        print(result_list)
        write_result(output, result_list, final_states)

    # print("star:", start_state)
    # print("final:", final_states)
    # print("rule:", transition_rules)


if __name__ == '__main__':
    main()

