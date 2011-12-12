import unittest
from src.tokenizer import tokenize, Token, LaTeXToken, ItalicsToken

class TestTokenizer(unittest.TestCase):
    def test_just_text(self):
        text = 'how are you'
        tokens = tokenize(text)
        for x in tokens:
            print x

    def test_some_latex(self):
        text = '$\epsilon$ is awesome!'
        tokens = tokenize(text)
        assert tokens[0].content == '$\epsilon$'

    def test_escapes(self):
        text = '$\$$'
        tokens = tokenize(text)
        for token in tokens:
            print token.content

class TestLaTeXTokens(unittest.TestCase):
    def test_compile(self):
        foo = LaTeXToken('$\epsilon$')
        foo.compile()




