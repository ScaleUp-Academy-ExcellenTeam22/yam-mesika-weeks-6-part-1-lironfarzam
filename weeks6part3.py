import re
from itertools import product


def words_length(Sentence: str) -> []:
    """
    Function that receives a sentence and returns a list of all word lengths.
    :param Sentence: string of words.
    :return:List of all word lengths.
    """
    return list(map(lambda word: len(word), Sentence.split(" ")))


def get_letters() -> []:
    """
    :return: Returns a list of all characters between a and z and between A and Z.
    """
    return [chr(i) for i in range(ord('a'), ord('z') + 1)] + [chr(i) for i in range(ord('A'), ord('Z') + 1)]


def remove_non_alpha(string: str):
    """
    function to remove non alpha characters from a string
    :param string: the string.
    :return: string after the remove
    """
    return re.sub('[^a-zA-Z\s]', '', string)


def count_words(text: str) -> {}:
    """
    Function accepts a text parameter, and returns a dictionary of its word lengths.
    First clear the text of non-letter characters.
    Next, use dictionary comprehension to find out the length of each word in the sentence.
    :param text: string
    :return: dictionary { KEY = word : VAL = len(word)}
    """
    text_whit_only_letters = remove_non_alpha(text)
    words_length_dictionary = {word: len(word) for word in text_whit_only_letters.split()}

    return words_length_dictionary


def full_names(first_names: [], last_names: [], min_length: int = 0) -> []:
    """
    Function which will get as a parameter a list of first names and a list of last names,
    and compile full names from them.
    For each first name, the function will attach all the family names received.

    :param first_names: List of first names.
    :param last_names : List of last names,
    :param min_length : If the parameter is passed, full names whose number of characters is less than the
                        specified length will not be returned from the function.

    :return: List of all full names.
    """

    full_names = list(map(lambda name: name[0]+" "+name[1], product(map(lambda name: name.title(), first_names),
                                                                    map(lambda name: name.title(), last_names))))

    return list(filter(lambda name: len(name) >= min_length, full_names))


if __name__ == '__main__':

    # [5, 4, 1, 7, 5, 3, 2, 6, 7]
    print(words_length("Toto, I've a feeling we're not in Kansas anymore"))

    print(get_letters())

    text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """
    # expected_result = {'you': 3, 'see': 3, 'wire': 4, 'telegraph': 9, 'is': 2, 'a': 1, 'kind': 4, 'of': 2, 'very': 4,
    #                   'long': 4, 'cat': 3, 'pull': 4, 'his': 3, 'tail': 4, 'in': 2, 'new': 3, 'york': 4, 'and': 3,
    #                   'head': 4, 'meowing': 7, 'los': 3, 'angeles': 7, 'do': 2, 'understand': 10, 'this': 4,
    #                   'radio': 5, 'operates': 8, 'exactly': 7, 'the': 3, 'same': 4, 'way': 3, 'send': 4, 'signals': 7,
    #                   'here': 4, 'they': 4, 'receive': 7, 'them': 4, 'there': 5, 'only': 4, 'difference': 10,
    #                   'that': 4, 'no': 2}

    print(count_words(text))

    first_names = ['avi', 'moshe', 'yaakov']
    last_names = ['cohen', 'levi', 'mizrahi']

    print(full_names(first_names, last_names, 10))

    # ['Avi Mizrahi', 'Moshe Cohen', 'Moshe Levi', 'Moshe Mizrahi',
    # 'Yaakov Cohen', 'Yaakov Levi', 'Yaakov Mizrahi']
