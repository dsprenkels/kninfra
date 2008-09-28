#
# Executes a sync generated by gen-sync.py
#

import os
import sys
import os.path
import cStringIO
import subprocess


if __name__ == '__main__':
	p = os.path.dirname(sys.argv[0])
	if p != '': os.chdir(p)
	while True:
		l = sys.stdin.readline()
		if l == '': break
		l = l[:-1]
		l = l.split('#')[0]
		action, args = l.split(' ', 1)
		action = os.path.basename(action)
		if not os.path.exists('actions/%s' % action):
			print "Action %s doesn't exist" % action
			sys.exit(-1)
		subprocess.call(['actions/%s'%action,]+args.split(' '))
