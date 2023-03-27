def similar_string(WORD_check, WORD_orginal):
    # WORD_check = 'czerwony' 
    # WORD_orginal = 'czerwoni'
    C_word = WORD_check 
    O_word = WORD_orginal 
    leters_O = set()
    counter_to = 0
    for c, o in zip(C_word, O_word):
        leters_O.add(c)
        if o == c:        
            counter_to += 1
    res_1 = counter_to / len(WORD_orginal)
    WORD_check_back = ''
    indexCounter_check = len(WORD_check) - 1
    for i in range(len(WORD_check)):
        WORD_check_back += WORD_check[indexCounter_check]
        indexCounter_check -= 1
    WORD_orginal_back = ''
    indexCounter_orginal = len(WORD_orginal) - 1
    for i in range(len(WORD_orginal)):
        WORD_orginal_back += WORD_orginal[indexCounter_orginal]
        indexCounter_orginal -= 1
    C_word_back = WORD_check_back
    O_word_back = WORD_orginal_back
    counter_back = 0
    for c, o in zip(C_word_back, O_word_back):
        if o == c:
            counter_back += 1
    res_2 = counter_back / len(O_word_back)
    counter_letters = 0
    for l in leters_O:
        for o in O_word:
            if l == o:
                counter_letters += 1
    res_3 = counter_letters / len(O_word_back)
    counter_letters_3 = 1
    WORD_check_3 = []
    exp_w_3 = ''
    for lc in WORD_check:
        exp_w_3 += lc
        if counter_letters_3 == 3:
            WORD_check_3.append(exp_w_3)
            counter_letters_3 = 0
            exp_w_3 = ''
        counter_letters_3 += 1
    if len(exp_w_3) != 3:
        WORD_check_3.append(exp_w_3)
    counter_letters_3 = 1
    WORD_orginal_3 = []
    exp_w_3 = ''
    for lo in WORD_orginal:
        exp_w_3 += lo
        if counter_letters_3 == 3:
            WORD_orginal_3.append(exp_w_3)
            counter_letters_3 = 0
            exp_w_3 = ''
        counter_letters_3 += 1
    if len(exp_w_3) != 3:
        WORD_orginal_3.append(exp_w_3)
    counter_to_3 = 0
    for c, o in zip(WORD_check_3, WORD_orginal_3):
        if o == c:
            counter_to_3 += 1
    res_4 = counter_to_3 / len(WORD_orginal_3)
    final = int(((res_1 + res_2 + res_3 + res_4) / 4) * 100)
    return final
if __name__ == "__main__":
    res = similar_string('mam', 'masz')
    print(str(int(res)) + ' %')