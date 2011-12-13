import unittest
from src.tokenizer import tokenize, Token, LaTeXToken, ItalicsToken, LineBreak

class TestTokenizer(unittest.TestCase):
    def _print_tokens(self, tokens):
        for x in tokens:
            print x.content
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
        print tokens
        assert tokens[0].content == '$\$$'

    def test_display_math(self):
        text = '$$\sigma$$'
        tokens = tokenize(text)
        print tokens
        self._print_tokens(tokens)

    def test_new_lines(self):
        text = "\n\n"
        tokens = tokenize(text)
        assert len(tokens) == 1
        assert isinstance(tokens[0], Spacing)

class TestLaTeXTokens(unittest.TestCase):
    def test_compile(self):
        foo = LaTeXToken('$\epsilon$')
        foo.compile()




