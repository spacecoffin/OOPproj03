from spellCheck import SpellChecker

def main():
    sc = SpellChecker()
    sc.statistics()
    query = 'Name of the document to be spell-checked: '
    sc.spellcheck(input(query))

main()