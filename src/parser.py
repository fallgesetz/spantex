def parse(tokens):
    output = []
    for tok in tokens:
        output.append(tok.compile())
    return ' '.join(output)


