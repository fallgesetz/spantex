#!/usr/bin/env python
import sys
import yaml
import os

import parser
import tokenizer

def make_html_output(output_dir, title, page):
    path = os.path.join(output_dir, '%s.html' % title)
    with open(path, 'w') as fh:
        fh.write(page)

def main():

    try:
        settings = open('settings.cfg', 'r').read()
    except IOError as e:
        print "Do you have your settings entered correctly?"
        exit(1)

    settings_obj = yaml.load(settings)

    input_path = os.path.abspath(settings_obj['in'])
    output_path = os.path.abspath(settings_obj['out'])
    extensions = settings_obj['extensions']


    main_template = os.path.join(input_path, 'templates/main.html')
    try:
        main_template_html = open(main_template, 'r').read()
    except IOError as e:
        import html_templates
        main_template_html = html_templates.basic

    posts = os.path.join(input_path, 'posts/')
    for post in os.listdir(posts):
        if any([post.endswith(x) for x in extensions]):
            post_path = os.path.join(os.path.dirname(posts), post)
            tokens = tokenizer.tokenize(open(post_path, 'r').read())
            parsed_post = parser.parse(tokens)
            parsed_page = main_template_html.safe_substitute(title=post, body=parsed_post)
            make_html_output(output_path, post, parsed_page)

if __name__ == '__main__':
    main()

