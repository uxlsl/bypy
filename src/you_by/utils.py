# -*- coding:utf-8 -*-

import os
import sys
import time
import shutil
import config
import traceback
from constants import (
        ENoError,
        EFailToCreateLocalFile,
        EFailToDeleteFile,
        EFailToDeleteDir,
)
from human import (
        human_size,
        human_time_short,
        human_speed,
)


# http://stackoverflow.com/questions/9403986/python-3-traceback-fails-when-no-exception-is-active
def formatex(ex):
	s = ''
	if ex and isinstance(ex, Exception):
		s = "Exception:\n{} - {}\nStack:\n{}".format(
			type(ex), ex, ''.join(traceback.format_stack()))

	return s


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


def askc(msg, enter = True):
	pr(msg)
	if enter:
		pr('Press [Enter] when you are done')
	return raw_input()

ask = askc

# print progress
# https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
def pprgrc(finish, total, start_time = None, existing = 0,
		prefix = '', suffix = '', seg = 20):
	# we don't want this goes to the log, so we use stderr
	if total > 0:
		segth = seg * finish // total
		percent = 100 * finish // total
		current_batch_percent = 100 * (finish - existing) // total
	else:
		segth = seg
		percent = 100
	eta = ''
	now = time.time()
	if start_time is not None and current_batch_percent > 5 and finish > 0:
		finishf = float(finish) - float(existing)
		totalf = float(total)
		remainf = totalf - float(finish)
		elapsed = now - start_time
		speed = human_speed(finishf / elapsed)
		eta = 'ETA: ' + human_time_short(elapsed * remainf / finishf) + \
				' (' + speed + ', ' + \
				human_time_short(elapsed) + ' gone)'
	msg = '\r' + prefix + '[' + segth * '=' + (seg - segth) * '_' + ']' + \
		" {}% ({}/{})".format(percent, human_size(finish, 1), human_size(total, 1)) + \
		' ' + eta + suffix
	#msg = '\r' + prefix + '[' + segth * '=' + (seg - segth) * '_' + ']' + \
	#	" {}% ({}/{})".format(percent, human_size(finish), human_size(total)) + \
	#	' ' + eta + suffix
	sys.stderr.write(msg + ' ') # space is used as a clearer
	sys.stderr.flush()

pprgr = pprgrc

# guarantee no-exception
def copyfile(src, dst):
	result = ENoError
	try:
		shutil.copyfile(src, dst)
	except (shutil.Error, IOError) as ex:
		perr("Fail to copy '{}' to '{}'.\n{}".format(
			src, dst, formatex(ex)))
		result = EFailToCreateLocalFile

	return result

def movefile(src, dst):
	result = ENoError
	try:
		shutil.move(src, dst)
	except (shutil.Error, OSError) as ex:
		perr("Fail to move '{}' to '{}'.\n{}".format(
			src, dst, formatex(ex)))
		result = EFailToCreateLocalFile

	return result

def removefile(path, verbose = False):
	result = ENoError
	try:
		if verbose:
			pr("Removing local file '{}'".format(path))
		if path:
			os.remove(path)
	except Exception as ex:
		perr("Fail to remove local fle '{}'.\n{}".format(
			path, formatex(ex)))
		result = EFailToDeleteFile

	return result

def removedir(path, verbose = False):
	result = ENoError
	try:
		if verbose:
			pr("Removing local directory '{}'".format(path))
		if path:
			shutil.rmtree(path)
	except Exception as ex:
		perr("Fail to remove local directory '{}'.\n{}".format(
			path, formatex(ex)))
		result = EFailToDeleteDir

	return result

def makedir(path, mode = 0o777, verbose = False):
	result = ENoError

	if verbose:
		pr("Creating local directory '{}'".format(path))

	if path and not os.path.exists(path):
		try:
			os.makedirs(path, mode)
		except os.error as ex:
			perr("Failed at creating local dir '{}'.\n{}".format(
				path, formatex(ex)))
			result = EFailToCreateLocalDir

	return result

# guarantee no-exception
def getfilesize(path):
	size = -1
	try:
		size = os.path.getsize(path)
	except os.error as ex:
		perr("Exception occured while getting size of '{}'.\n{}".format(
			path, formatex(ex)))

	return size

# guarantee no-exception
def getfilemtime(path):
	mtime = -1
	try:
		mtime = os.path.getmtime(path)
	except os.error as ex:
		perr("Exception occured while getting modification time of '{}'.\n{}".format(
			path, formatex(ex)))

	return mtime

