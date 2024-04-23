#!/usr/bin/env python3
import argparse
import os
import sys

def byte_count(file):
    return os.path.getsize(file)

def line_count(file):
    with open(file, 'r') as f:
        return len(f.readlines())

def word_count(file):
    with open(file,"r") as f:
        return len(f.read().split())

def char_count(file):
    with open(file, 'r') as f:
        return len(f.read())

def main():
    parser = argparse.ArgumentParser(description='CCWC: word count cli tool', prog='ccwc', usage='%(prog)s [file] [options]')
    
    parser.add_argument('file', type=str,nargs="?", help='The file to be processed')
    parser.add_argument('-c', action='store_true', help='The number of bytes in each input file is written to the standard output')
    parser.add_argument('-l', action='store_true', help='The number of lines in each input file is written to the standard output')
    parser.add_argument('-w', action='store_true', help='The number of words in each input file is written to the standard output')
    parser.add_argument('-m', action='store_true', help='The number of characters in each input file is written to the standard output')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    args = parser.parse_args()
    # if file is not provided then we check for stdin
    if not args.file:
        if sys.stdin.isatty():
            parser.print_help()
            sys.exit(1)
        else:
            # copy the stdin to a file
            with open("temp.txt", "w") as f:
                f.write(sys.stdin.read())
            args.file = "temp.txt"

    if args.c:
        print(byte_count(args.file), args.file)
    
    if args.l:
        print(line_count(args.file), args.file)
    
    if args.w:
        print(word_count(args.file), args.file)
    if args.m:
        print(char_count(args.file), args.file)
    if not any(value for key, value in vars(args).items() if key != 'file'):
        print(line_count(args.file), word_count(args.file), byte_count(args.file), args.file)

if __name__ == '__main__':
    main()
    