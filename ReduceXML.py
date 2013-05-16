import xml.etree.ElementTree as ET

def convertToDict(xml):
    children = list(map(convertToDict, iter(xml)))
    if not children:
        children = [xml.text.strip()]
    return {xml.tag:children}


def reduceDict(parse):
    parse = reduceEmpty(parse)
    parse = reduceWords(parse)
    #parse = reduceNesting(parse)
    return parse


def flatten(word):
    if type(word) == str:
        return word
    else:
        return ''.join(map(flatten, 
            word if type(word) == list else word.values()))

def reduceWords(parse):
    if type(parse) == str:
        return parse
    else:
        return dict(map(lambda e: reduceWordsL(*e), parse.items()))

def reduceWordsL(key, inner):
    if not list(filter(lambda c: not c in 'ABCDEFGhIJKLMNOPRSTUVXYZ', key)):
        return (key, flatten(inner))
    else:
        return (key, list(map(reduceWords, inner)))

def reduceEmpty(parse):
    if type(parse) == str:
        return parse
    else:
        return dict(filter(lambda e: not e[1] in [[''],[{}],[]], 
            map(lambda e: (e[0], list(filter(lambda i: i != {},
                map(reduceEmpty, e[1])))), parse.items())))
