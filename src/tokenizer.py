import re

""" -- Data -- """
class AbstractToken(object):
    def __init__(self, content):
        self.content = content

    def compile(self):
        return self.content

class Token(AbstractToken):
    pass

class LaTeXToken(AbstractToken):
    """
    returns an image tag with inlined png.

    inlined png
    pro:
    easier to manage.
    con: 
    take up more space
    """
    def compile(self):
        latex_to_compile = """
\documentclass[12pt]{amsart}
\usepackage{amsmath}
\usepackage{amssymb}
\begin{document}
%s
\end{document}
""" % self.content
        return "<img src='data:image/png;base64,%s' />" % encoded_image


class ItalicsToken(AbstractToken):
    pass

TOKEN_TYPES = {0: LaTeXToken, 
               1: ItalicsToken,
               2: Token}

tokenizer_regex = r"""
(\$.*?\$) | 
(_\w+_) |   
(\w+)      
"""

tokenizer_matcher = re.compile(tokenizer_regex, re.VERBOSE)


""" -- Actions -- """

def tuple_to_token(re_tuple):
    for index, content in enumerate(re_tuple):
        if not re_tuple[index] == '':
            return TOKEN_TYPES[index](content)

def tokenize(text):
    token_list = tokenizer_matcher.findall(text)
    tokens = []
    for x in token_list:
        tokens.append(tuple_to_token(x))

    return tokens









