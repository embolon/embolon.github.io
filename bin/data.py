#!/usr/bin/env python

import json
import argparse
import os.path

parser = argparse.ArgumentParser(description='Argument')
parser.add_argument('-i', '--identifier', help='return page identifier',
                    action='store_true', default=False)
parser.add_argument('-f', '--file', help='input Json File', default='default.json')
args = parser.parse_args()
args_var = vars(args)

def initData():
    newdata = {}
    newdata['identifier'] = 0
    return newdata

if __name__ == '__main__':
    
    # read in the data
    filepath = 'bin/{0}'.format(args_var['file'])
    if not os.path.isfile(filepath):
        data = initData()
    else:
        with open(filepath, 'r') as fh:
            data = json.load(fh)
    
    # output the required data
    if args_var['identifier']:
        print('{0:012d}'.format(data['identifier']))
        data['identifier'] += 1

    # write back the data
    with open(filepath, 'w') as fh:
        json.dump(data, fh)
