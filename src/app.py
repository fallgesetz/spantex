#!/usr/bin/env python
import sys
import argparse

import html_templates
import parser
import tokenizer



def main():
    parser = argparse.ArgumentParser(description='Static web site generator with integrated latex support')
    parser.add_argument('input', default='in/')
    parser.add_argument('output', default='out/')
    parser.add_argument('-e', '--extension', action='append', help='file types to parse')

    print parser.parse_args(sys.argv[1:])

if __name__ == '__main__':
    main()
    tokens = tokenizer.tokenize('hi how are you. $\epsilon$')
    print tokens
    print parser.parse(tokens)

