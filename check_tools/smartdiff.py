import sys

def format_map(black_list):
    docs  = black_list.split(':')[1::2]
    words = black_list.split(':')[0::2][1:]

    index = 0
    _map = {}
    for doc in docs:
        _map[doc] = words[index].split(';')
        index += 1

    return _map

def main():
    pr_list   = open('pr_black_list.log', 'r').read()
    head_list = open('head_black_list.log', 'r').read()

    pr_dict   = format_map(pr_list)
    head_dict = format_map(head_list)

    result = 0

    for doc,words in pr_dict.iteritems():
        # Split the line number and trailing newlines from the list of found prohibited words
        # Check for move in file location as the path is included in the key. Catch on try failure
        try:
            stripped_pr_words = [word.split(',')[1].replace("\n","") for word in words]
            stripped_head_words = [word.split(',')[1].replace("\n","") for word in head_dict[doc]]
        except KeyError as E:
            print "File name or location change, skipping file: %s" % E
            result += 1

        # Do not want to trigger failure on removed prohibited words from existing docs.
        # Subtracting the set of PR words from the head revision list works as this filter
        diff = list(set(stripped_pr_words) - set(stripped_head_words))

        if diff:
            print "Found added words from the prohibited list in file %s..." % doc
            result += 2
            for word in diff:
                # Find word in unstripped set to pull in line number
                line = words[diff.index(word)].split(',')[0]
                print "\t- Line: %s, Word: %s" % (line, word)

    sys.exit(result)

if __name__ == "__main__":
    main()
