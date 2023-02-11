# Non-context grammar correct and misspelled senetence generator

Python module that allows to generate sentences using non-context grammar.The main goal of this module is to generate gramarly corrected and incorrected sentences in a control way. 
Module MisspellGenerator is created to randomly add typing errors that base on Damerau–Levenshtein distance error types: 
- transpose;
- deletion;
- replace; 
- insert.
The _misspell_sentence_ function adds typing errors to the provided as an argument string (the amount of the errors is the second argument of this function). 

The function _generate_sentences_ from SentenceGenerator.py is core one to generate sentence - as the arguments it takes: subject,  
correct and incorrect (optionally) verb phrase and the rest of sentences. The project mainly focuses on simple grammatical constructions: 
- Subject - Verb - Object;
- Subject - Verb - Adjective;
- Subject - Verb - Adverb;
- Subject - Verb - Noun.

The rules that are included in the _fill_verb_subject_rule_ function from SentenceGenerator.py module allows to generate sentences using following structures:
- **Present Simple**
  -  Correct sentence: Not 3rd singular subject + V1 or 3rd singular subject + Verb -s / -es / -ies 
  -  Incorrect sentence:  Not 3rd singular subject + Verb -s / -es / -ies   or  3rd singular subject + V1
- **Present continuous**
  -  Correct sentence: I am + gerund or singular noun + is + gerund  or Plural noun + are + gerund
  -  Incorrect sentence: I is + gerund or singular noun + are + gerund or Plural noun + is + gerund
- **Present perfect**
  -  Correct sentence: Not 3rd singular subject + have + V3 or 3rd singular subject + has + V3
  -  Incorrect sentence: Not 3rd singular subject + has + V3 or 3rd singular subject + have + V3
- **Past simple**
  -  Correct sentence: 
  -  Incorrect sentence: 
- **Past continuous**
  -  Correct sentence: 
  -  Incorrect sentence: 
- **Past perfect**
  -  Correct sentence: 
  -  Incorrect sentence: 
- **Future simple**
  -  Correct sentence: 
  -  Incorrect sentence: 
- **Future continuous**
  -  Correct sentence: 
  -  Incorrect sentence: 
- **Future perfect**
  -  Correct sentence: 
  -  Incorrect sentence: 
- **Passive present continuous**
  -  Correct sentence: 
  -  Incorrect sentence: 
- **Passive present perfect** 
  -  Correct sentence: 
  -  Incorrect sentence: 
- **Passive past simple**
  -  Correct sentence: 
  -  Incorrect sentence: 
- **Passive past perfect**
  -  Correct sentence: 
  -  Incorrect sentence: 
- **Passive future simple**
  -  Correct sentence: 
  -  Incorrect sentence: 
- **Can**
  -  Correct sentence: Subject + can + V1
  -  Incorrect sentence: Subject + can + Verb -s / -es / -ies 
- **Could**
  -  Correct sentence: Subject + could + V1
  -  Incorrect sentence: Subject + could + Verb -s / -es / -ies 
- **Will**
  -  Correct sentence: Subject + will + V1
  -  Incorrect sentence: Subject + will + Verb -s / -es / -ies 
- **Must**
  -  Correct sentence: Subject + must + V1
  -  Incorrect sentence: Subject + must + Verb -s / -es / -ies 
- **Would**
  -  Correct sentence: Subject + would + V1
  -  Incorrect sentence: Subject + would + Verb -s / -es / -ies 
- **Should**
  -  Correct sentence: Subject + should + V1
  -  Incorrect sentence: Subject + should + Verb -s / -es / -ies 
- **Ought to**
  -  Correct sentence: Subject + ought to + V1
  -  Incorrect sentence: Subject + ought to + Verb -s / -es / -ies 
- **Used to**
  -  Correct sentence: Subject + used to + V1
  -  Incorrect sentence: Subject + used to + Verb -s / -es / -ies 
- **Going to**
  -  Correct sentence: I am going to + V1 or singular noun + is going to + V1  or Plural noun + are going to + V1
  -  Incorrect sentence:  Singular noun + are going to + V1 or Plural noun + is going to + V1 or  Singular noun + are going to + Verb -s / -es / -ies  or  Plural noun + is going to + Verb -s / -es / -ies 

            

