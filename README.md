# non_context_gramma_correct_and_misspelled_senetence_generator

Python module that allows to generate sentences using non-context grammar.The main goal of this module is to generate gramarly corrected and incorrected sentences in a control way. 
Module MisspellGenerator is created to randomly add typing errors that base on Damerau–Levenshtein distance error types: 
- transpose;
- deletion;
- replace;
- insert.
The _misspell_sentence_ function adds typing errors to the provided as an argument string (the amount of the errors is the second argument of this function). 

The function _generate_sentences_ from SentenceGenerator.py is core one to generate sentence - as the arguments it takes: subject,  
correct and incorrect (optionally) verb phrase and the rest of sentences. The project mainly focuses on simple grammatical constructions: 
— Subject - Verb - Object;
— Subject - Verb - Adjective;
— Subject - Verb - Adverb;
— Subject - Verb - Noun.

The rules that are included in the _fill_verb_subject_rule_ function from SentenceGenerator.py module allows to generate sentences using following structures:
- Present Simple 
  -  Correct sentence: Not 3rd Singular subject + V1 or 3rd Singular subject + V -s / -es / -ies 
  -  Incorrect sentence:  Not 3rd Singular subject + Verb -s / -es / -ies   or  3rd Singular subject + V1
- Present continuous
  -  Correct sentence: I am + gerund or Singular noun + is + gerund  or Plural noun + are + gerund
  -  Incorrect sentence: I is + gerund or Singular noun + are + gerund or Plural noun + is + gerund
- Present perfect 
  -  Correct sentence: Subject (Not 3rd Singular) + V1 or Subject (3rd Singular) + V -s / -es / -ies 
  -  Incorrect sentence: 
- Past simple
- Past continuous 
- Past perfect
- Future simple
- Future continuous
- Future perfect
- Passive present continuous 
- Passive present perfect 
- Passive past simple 
- Passive past perfect
- Passive future simple
- Can
- Could
- Will
- Must
- Would
- Should
- Ought to
- Used to
- Going to

            

