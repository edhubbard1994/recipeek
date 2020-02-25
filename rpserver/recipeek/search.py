

def search(keywords):
    query_accumulator = []
    for word in keywords:
        context = resolve_keyword(word)
        results = lookup(word,context)
        if results:
            query_accumulator.append(results)
    return query_accumulator


def resolve_keyword(word):
    #TODO: database queries to find the word context
    pass

def lookup(word,context):
    #perform database lookup
    pass