import random
import re
import string


def transpose(word: str) -> str:
    """Function that transposes chars in the word."""
    if len(word) >= 3:
        x = random.randint(0, len(word) - 2)
        if word[x] == word[x + 1]:
            while word[x] != word[x + 1]:
                x = random.randint(0, len(word) - 2)
        word = list(word)
        word[x], word[x + 1] = word[x + 1], word[x]
        return "".join(word)


def deletion(word: str) -> str:
    """Function that deletes a char in the word."""
    if len(word) >= 3:
        x = random.randint(0, len(word) - 1)
        if x > 0:
            return word[:x - 1] + word[x:]
        else:
            return word[1:]


def replace(word: str) -> str:
    """Function that replaces a char in the word."""
    if len(word) >= 2:
        x = random.randint(0, len(word) - 1)
        word = list(word)
        word[x] = random.choice(re.sub(r'[\s]', '', string.printable))
        return ''.join(word)


def insert(word: str) -> str:
    """Function that inserts a char in the word."""
    x = random.randint(0, len(word))
    word = word[:x] + random.choice(re.sub(r'[\s]', '', string.printable)) + word[x:]
    return word


def misspell_sentence(sentence: str, amount_of_misspells: int = 1):
    """Function that misspells the sentence."""

    if len(sentence) > amount_of_misspells:
        operations = {'transpose': 0, 'replace': 0, 'deletion': 0, 'insert': 0}
        while amount_of_misspells > 0:
            operation_choice = random.randint(1, 4)
            if isinstance(sentence, str):
                sentence = sentence.split()
            word_choice = random.randint(0, len(sentence) - 1)
            if operation_choice == 0 and len(sentence[word_choice]) > 2:
                sentence[word_choice] = transpose(sentence[word_choice])
                amount_of_misspells -= 1
                operations['transpose'] += 1
            elif operation_choice == 1 and len(sentence[word_choice]) >= 2:
                sentence[word_choice] = replace(sentence[word_choice])
                amount_of_misspells -= 1
                operations['replace'] += 1

            elif operation_choice == 2 and len(sentence[word_choice]) > 2:
                sentence[word_choice] = deletion(sentence[word_choice])
                amount_of_misspells -= 1
                operations['deletion'] += 1

            elif operation_choice == 3:
                sentence[word_choice] = insert(sentence[word_choice])
                amount_of_misspells -= 1
                operations['insert'] += 1

        return ' '.join(sentence), operations

