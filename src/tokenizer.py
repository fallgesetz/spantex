import base64
import os
import re
import tempfile
import subprocess # got to call latex

class AbstractToken(object):
    def __init__(self, content):
        self.content = content

    def compile(self):
        return self.content

class Token(AbstractToken):
    # TODO: do things like separate out paragraphs
    pass

class LaTeXToken(AbstractToken):
    """
        returns an image tag with inlined png.
    """
    def compile(self):
        latex_to_compile = r"""
\documentclass[20pt]{article}
\usepackage{amsmath}
\usepackage{amssymb}
\begin{document}
\pagestyle{empty}
%s
\end{document}
""" % self.content

        compilation_dir = tempfile.mkdtemp()
        tex_path = "%s/t.tex" % compilation_dir

        tex_file = open(tex_path, 'w')
        tex_file.write(latex_to_compile)
        tex_file.close()

        current_dir = os.getcwd()
        os.chdir(compilation_dir)

        subprocess.call(['latex', 't.tex'])
        subprocess.call(['dvips', '-E', 't.dvi', '-o', 't.ps'])
        subprocess.call(['convert', '-density', '200x200', 't.ps', 't.png'])

        png_path = "%s/t.png" % compilation_dir

        png_file = open(png_path, 'rb')
        png_data = png_file.read()
        encoded_png_data = base64.b64encode(png_data)

        os.chdir(current_dir)

        return "<img src='data:image/png;base64,%s' />" % encoded_png_data

class LaTeXDisplayToken(LaTeXToken):
    def compile(self):
        png = super(LaTeXDisplayToken, self).compile()
        return "<div class='display_math'>%s</div>" % png

class ItalicsToken(AbstractToken):
    def compile(self):
        return '<i>%s</i>' % self.content[1:-1]

class LineBreak(AbstractToken):
    pass

TOKEN_TYPES = {0: LaTeXDisplayToken,
               1: LaTeXToken,
               2: ItalicsToken,
               3: Token,
               4: LineBreak}

tokenizer_regex = r"""
(\$\$.+?(?<!\\)\$\$) |
(\$.+?(?<!\\)\$) |
(_\S+_) |
(\S+) |
(\n{1,})
"""

tokenizer_matcher = re.compile(tokenizer_regex, re.VERBOSE)


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
