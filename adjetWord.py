import coffeeBrain as cf
import wtf
with open('odm.neural', 'r', encoding='utf-8') as wordsFile:
    allwords = wordsFile.readlines()

word = 'pesymistyczne'
word_1 = []
cc = 0
for w in allwords:
    ww = w.strip().split(', ')
    word_finded = ww[0]
    if ww[0].endswith('owy') and ww[0].startswith('p'): # len(ww)
        word_1.append([ww[0], len(ww)])

        cc += 1
    # if cc == 40:
    #     break

print(word_1)


# wordBase = cf.coffeePls()[2]
# meaningWords = cf.coffeePls()[3]
# for w in allwords:
#     ishere = w.count(f' {word}')
    # if ishere == 0:
    #     ishere = w.count(f'{word}, ')
#     if ishere:
#         ww = w.strip().split(', ')
#         word_finded = ww[0]
#         try:
#             print(wordBase[word_finded])
#         except:
#             print(f'brak znaczenia {word_finded}')
#             answer = wtf.whatIsThat(word_finded)
#             print(answer)
#         try:
#             print(meaningWords[word_finded])
#         except:
#             print(f'brak cz. mowy {word_finded}')
        



            # written = INDEX_WORD + str(q) + SEP_PART + str(faze) + '\n'
            # wtf.addQuestionAnswer(written)

                # try: knowWord = wordBase[q]
                # except: knowWord = False
                # if knowWord == False:
                #     answer = wtf.whatIsThat(q)
                #     for ans in answer:
                #         for an in ans.keys():
                #             CategoryOfWord = SEP_TITLE + an + SEP_TITLE
                #             wordListTmp.append(CategoryOfWord)
                #         for anV in ans.values():
                #             for a in anV:
                #                 a = str(a)
                #                 a = a
                #                 wordListTmp.append(a + SEP_SPLIT)

                #     wordBase[q] = wordListTmp
                #     faze = ''
                #     for f in wordListTmp:
                #         f = str(f)
                #         faze += f.strip()
                #     written = INDEX_WORD + str(q) + SEP_PART + str(faze) + '\n'
                #     wtf.addQuestionAnswer(written)