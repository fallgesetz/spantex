#!/usr/bin/env python
import sys
import argparse
import os

import parser
import tokenizer

def make_html_output(output_dir, title, page):
    path = os.path.join(os.path.dirname('%s/%s' % (os.getcwd(), output_dir)), '%s.html' % title)
    print path
    print os.path.dirname(output_dir)
    print os.getcwd()
    with open(path, 'w') as fh:
        fh.write(page)

def main():
    argparser = argparse.ArgumentParser(description='Static web site generator with integrated latex support')
    argparser.add_argument('input', default='in')
    argparser.add_argument('output', default='out')
    argparser.add_argument('-e', '--extension', action='append', help='file types to parse', default=['.txt'])

    args = argparser.parse_args(sys.argv[1:])
    main_template = os.path.join(os.path.dirname(args.input), 'templates/main.html')
    try:
        main_template_html = open(main_template, 'r').read()
    except IOError as e:
        import html_templates
        main_template_html = html_templates.basic

    posts = os.path.join(os.path.dirname(args.input), 'posts/')
    for post in os.listdir(posts):
        if any([post.endswith(x) for x in args.extension]):
            post_path = os.path.join(os.path.dirname(posts), post)
            tokens = tokenizer.tokenize(open(post_path, 'r').read())
            for x in tokens:
                print 'new token'
                print x.content
            parsed_post = parser.parse(tokens)
            parsed_page = main_template_html.safe_substitute(title=post, body=parsed_post)
            make_html_output(args.output, post, parsed_page)

if __name__ == '__main__':
    main()

