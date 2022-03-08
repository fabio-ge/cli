#!/usr/bin/env python

import argparse


def get_args():
    """recupero gli argomenti"""
    parser = argparse.ArgumentParser(description="say hello")
    parser.add_argument('-n', '--name', metavar="name", default="World",
                        help="name to greet")
    return parser.parse_args()


def main():
	args = get_args()
	print(f"Hello, {args.name}!")

if __name__ == '__main__':
	main()


