# _import.py
#   sets up the mailman environment for sync
#


import os
import sys
import imp
import os.path

def setup_virtual_package(name, path=os.curdir):
	""" Sets up a package at the given path with a given
	    name """
	modulePath = os.path.abspath(path)
	f, fn, suffix = imp.find_module('__init__',
		 [modulePath])
	imp.load_module(name, f, fn, suffix)
	sys.modules[name].__path__ = [modulePath]

if '_import' in sys.modules:
	setup_virtual_package('Mailman', os.path.expanduser('~mailman/Mailman'))
