#!/usr/bin/env python
from pygments import lex,format
from pygments.lexers import SqlLexer
from pygments.formatters import TerminalFormatter
from sys import stdin,stdout
line = stdin.readline()
while(line):
	stdout.write(format(lex(line,SqlLexer()),TerminalFormatter()))
	line=stdin.readline()

