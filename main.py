import PhraseGenerator
from SentenceGenerator import fill_verb_subject_rule, generate_sentences

if __name__=="__main__":
    try:
        for verb in PhraseGenerator.PhraseGenerator('VB').generate_phrase(10000):
            for key in fill_verb_subject_rule(verb):
                for sent in generate_sentences(fill_verb_subject_rule(verb)[key][0],
                                               fill_verb_subject_rule(verb)[key][1],
                                               fill_verb_subject_rule(verb)[key][2], 'RB'):
                    with open('grammar_incorrect\\' + str(key) + '.txt', 'a+') as f:
                        f.write(str(sent))
                        if sent != '\n':
                            f.write('\n')
                for sent in generate_sentences(fill_verb_subject_rule(verb)[key][0],
                                               fill_verb_subject_rule(verb)[key][1],
                                               fill_verb_subject_rule(verb)[key][2], 'JJ'):
                    with open('grammar_incorrect\\' + str(key) + '.txt', 'a+') as f:
                        f.write(str(sent))
                        if sent != '\n':
                            f.write('\n')
                for sent in generate_sentences(fill_verb_subject_rule(verb)[key][0],
                                               fill_verb_subject_rule(verb)[key][1],
                                               fill_verb_subject_rule(verb)[key][2], 'PP'):
                    with open('grammar_incorrect\\' + str(key) + '.txt', 'a+') as f:
                        f.write(str(sent))
                        if sent != '\n':
                            f.write('\n')
                for sent in generate_sentences(fill_verb_subject_rule(verb)[key][0],
                                               fill_verb_subject_rule(verb)[key][1],
                                               fill_verb_subject_rule(verb)[key][2], 'Det Adj NP'):
                    with open('grammar_incorrect\\' + str(key) + '.txt', 'a+') as f:
                        f.write(str(sent))
                        f.write('\n')
    except:
        pass




