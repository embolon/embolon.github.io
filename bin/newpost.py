#!/usr/bin/env python

import time
import datetime
import argparse

parser = argparse.ArgumentParser(description='Arguments')
parser.add_argument('-t', '--title', help='the title of this post',
                    default='This is a test post')
parser.add_argument('-c', '--categories', help='the categories of this post',
                    default='default')
parser.add_argument('-tg', '--tags', help='tags of this post',
                    default='default')
parser.add_argument('-cm', '--comments', help='enable comments',
                    action='store_true', default=False)
parser.add_argument('-i', '--identifier', help='page identifier',
                    default='false')
parser.add_argument('-p', '--print', help='print the newly created post file name', 
                    action='store_true', default=False)
parser.add_argument('-l', '--language', help='the language of this post: english/chinese',
                    default='english')
args = parser.parse_args()
args_var = vars(args)

if __name__ == '__main__':

    # post name
    today = time.strftime("%Y-%m-%d")
    title = '-'.join(args_var['title'].lower().split())
    post_name = today + '-' + title

    # prepare post content
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S %z") # utc_now
    #now = time.strftime("%Y-%m-%d %H:%M:%S %z")
    identifier = args_var['identifier']
    title = args_var['title']
    categories = '-'.join(args_var['categories'].lower().split()) # all lowercase connect with '-'
    tags = ''
    for tag in args_var['tags'].split(','): # use ',' to separate tags
        tags += '\n- {0}'.format('-'.join(tag.lower().split()))
    comments = 'true' if args_var['comments'] else 'false'
    language = args_var['language']
    post_content = '''---
layout: post
title:  "{0}"
date:   {1}
categories: {2}
tags: {3}
comments: {4}
identifier: {5}
language: {6}
---
'''.format(title, now, categories, tags, comments, identifier, language)

    # create new post file
    with open('_posts/{0}.md'.format(post_name), 'w') as fh:
       fh.write(post_content)

    # print post file name
    if args_var['print']:
        print('_posts/{0}.md'.format(post_name))
