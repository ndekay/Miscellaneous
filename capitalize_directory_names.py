#!/usr/bin/env python


"""capitalize_directory_names.py: Title-case capitalizes the names of subdirectories in a specified directory list."""


import os
import sys


__author__ = "Nickolaus Dekay"
__version__ = "1.0"
__email__ = "nickolaus.dekay@gmail.com"


def main():
    args = sys.argv[1:]
    if len(args) > 0:
        for arg in args:
            dest = os.path.abspath(arg)
            if os.path.exists(dest):
                os.chdir(dest)
                subdirs = os.listdir(dest)
                for subdir in subdirs:
                    try:
                        print("Renaming '{}\\{}' to '{}'".format(dest, subdir, subdir.title()))
                        os.rename(subdir, subdir.title())
                    except PermissionError as e:
                        print("Unable to rename '{}\\{}' to '{}' due to {}".format(dest, subdir, subdir.title(), e))
    else:
        print("Nothing done; no parameters provided.")


if __name__ == "__main__":
    main()
