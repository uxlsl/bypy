# -*- coding:utf-8 -*-

import os
import sys
import time
import config


def iswindows():
	return os.name == 'nt'

# A little summary of Unicode in Python (ad warning):
# http://houtianze.github.io/python/unicode/2015/12/07/python-unicode.html

# https://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
# https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
# 0 - black, 1 - red, 2 - green, 3 - yellow
# 4 - blue, 5 - magenta, 6 - cyan 7 - white
class TermColor:
	NumOfColors = 8
	Black, Red, Green, Yellow, Blue, Magenta, Cyan, White = range(NumOfColors)
	Nil = -1

def colorstr(msg, fg, bg):
	CSI = '\x1b['
	fgs = ''
	bgs = ''
	if fg >=0 and fg <= 7:
		fgs = str(fg + 30)

	if bg >= 0 and bg <=7:
		bgs = str(bg + 40)

	cs = ';'.join([fgs, bgs]).strip(';')
	if cs:
		return CSI + cs + 'm' + msg + CSI + '0m'
	else:
		return msg

def prc(msg):
	print(msg)
	# we need to flush the output periodically to see the latest status
	config.last_stdout_flush
	now = time.time()
	if now - config.last_stdout_flush >= config.PrintFlushPeriodInSec:
		sys.stdout.flush()
		config.last_stdout_flush = now

pr = prc

def prcolorc(msg, fg, bg):
	if sys.stdout.isatty() and not iswindows():
		pr(colorstr(msg, fg, bg))
	else:
		pr(msg)

prcolor = prcolorc

def plog(tag, msg, showtime = True, showdate = False,
		prefix = '', suffix = '', fg = TermColor.Nil, bg = TermColor.Nil):
	if showtime or showdate:
		now = time.localtime()
		if showtime:
			tag += time.strftime("[%H:%M:%S] ", now)
		if showdate:
			tag += time.strftime("[%Y-%m-%d] ", now)

	if prefix:
		prcolor("{}{}".format(tag, prefix), fg, bg)

	prcolor("{}{}".format(tag, msg), fg, bg)

	if suffix:
		prcolor("{}{}".format(tag, suffix), fg, bg)

def perr(msg, showtime = True, showdate = False, prefix = '', suffix = ''):
	return plog('<E> ', msg, showtime, showdate, prefix, suffix, TermColor.Red)

def pwarn(msg, showtime = True, showdate = False, prefix = '', suffix = ''):
	return plog('<W> ', msg, showtime, showdate, prefix, suffix, TermColor.Yellow)

def pinfo(msg, showtime = True, showdate = False, prefix = '', suffix = ''):
	return plog('<I> ', msg, showtime, showdate, prefix, suffix, TermColor.Green)

def pdbg(msg, showtime = True, showdate = False, prefix = '', suffix = ''):
	return plog('<D> ', msg, showtime, showdate, prefix, suffix, TermColor.Cyan)


def bannerwarn(msg):
	print('!' * 160)
	print(msg)
	print('!' * 160)


def iswindows():
	return os.name == 'nt'


