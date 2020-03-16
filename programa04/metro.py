# !/usr/bin/env python3
# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import re
import sys

def populate(graph, lines):
	for line in lines:
		if not line or line.startswith('#'):
			prev = None
			continue
		if not line in graph:
			graph[line] = []
		if prev and not prev in graph[line]:
			graph[line].append(prev)
		prev = line

graph = {}
with open('metro.txt', 'r') as fp:
	lines = fp.read().splitlines()

# print(lines)
populate(graph, lines)
lines[::-1]
populate(graph, lines)

for key in graph:
	for connection in graph[key]:
		if not key in graph[connection]:
			graph[connection].append(key)


with open('metro.graph', 'w') as fp:
	for key in graph:
		fp.write('{} = {}\n'.format(key, ', '.join(graph[key])))
