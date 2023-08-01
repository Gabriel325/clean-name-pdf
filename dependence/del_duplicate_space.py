def del_duplicate_space(name):
    for x in enumerate(name):
                    index = x[0]
                    letter = x[1]

                    if index != len(name) -1:
                        next_letter = name[index+1]

                        if letter == next_letter and letter == "-":
                            del name[index]        
    return name