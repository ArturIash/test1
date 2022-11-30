#!/usr/bin/env python3


from capitalize import capitalize


if capitalize('hello') != 'Hello':
    raise Exception('works incorrectly')


if capitalize('') != '':
    raise Exception('works incorrectly')


print('Test passed!')
