# This Python file uses the following encoding: utf-8
import os, sys
from collections import OrderedDict

def words(string):

  # my_string = string.split()
  my_string = [int (word) if word.isdigit() else word for word in string.split()]
  # my_dict = OrderedDict()
  my_dict  = {}
  for item in my_string:
    my_dict[item] = my_string.count(item)
  print (my_dict)
  return my_dict


words("testing 1 2 testing")