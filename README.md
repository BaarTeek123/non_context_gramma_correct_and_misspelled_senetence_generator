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
- **Present Continuous**
  -  Correct sentence: I am + gerund or singular noun + is + gerund  or Plural noun + are + gerund
  -  Incorrect sentence: I is + gerund or singular noun + are + gerund or Plural noun + is + gerund
- **Present perfect**
  -  Correct sentence: Not 3rd singular subject + have + V3 or 3rd singular subject + has + V3
  -  Incorrect sentence: Not 3rd singular subject + has + V3 or 3rd singular subject + have + V3
- **Past Simple**
  -  Correct sentence: Subject + V2
  -  Incorrect sentence: Not included
- **Past Continuous**
  -  Correct sentence: Singular noun + was + gerund  or Plural noun + were + gerund
  -  Incorrect sentence: Singular noun + were + gerund or Plural noun + was + gerund
- **Past perfect**
  -  Correct sentence: Subject + had + V3
  -  Incorrect sentence: Subject + had + V1
- **Future Simple**
  -  Correct sentence: Subject + will + V1
  -  Incorrect sentence: Subject + will + Verb -s / -es / -ies 
- **Future Continuous**
  -  Correct sentence: Subject + will be + gerund
  -  Incorrect sentence: Subject + will be + Verb -s / -es / -ies 
- **Future Perfect**
  -  Correct sentence: Subject + will have + V3
  -  Incorrect sentence: Subject + will have + Verb -s / -es / -ies 
- **Passive Present Continuous**
  -  Correct sentence: Singular noun + is being + V3  or Plural noun + are being + V3
  -  Incorrect sentence: Singular noun + is being + V3 or Plural noun + is being + V3
- **Passive Present Perfect** 
  -  Correct sentence: Not 3rd singular subject + have been + V3 or 3rd singular subject + has been + V3
  -  Incorrect sentence: Not included
- **Passive Past Simple**
  -  Correct sentence: Singular subject + was + V3 or Plural subject + were + V3
  -  Incorrect sentence: Singular subject + were + V3 or Plural subject + was + V3
- **Passive Past Perfect**
  -  Correct sentence: Subject + had been + V3
  -  Incorrect sentence: Not included
- **Passive Future Simple**
  -  Correct sentence: Subject + will be + V3
  -  Incorrect sentence: Subject + will be + Verb -s / -es / -ies 
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

            

