import file2
from file2 import a
import sys
print(sys.path)

"""Importing vars from files"""  # NOT SUGGESTED
print(a)

"""Importing other files"""  # SUGGESTED
print(file2.a)
file2.fn("Ohoooo")

"""Hence you can group fns which you often use in a file and thn import that file and use those fns"""

"""Giving same name to file as that of module will give an error as compiler will search for that module in curr directory so it'll consider file created by you wch doesn't has required fns"""
