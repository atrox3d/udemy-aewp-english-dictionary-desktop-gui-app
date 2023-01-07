import json


def list_words():
    with open('data.json') as file:
        terms = json.load(file)
    for word in sorted(terms.keys()):
        print(word)


def get_definition(term):
    print('loading data.json...')
    with open('data.json') as file:
        terms = json.load(file)
    definition = terms.get(term, [])
    print(f'{definition=}')
    return definition


if __name__ == '__main__':
    # list_words()
    print(get_definition('moon'))
