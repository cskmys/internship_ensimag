#!/usr/bin/env python3
import os
import gdb


def gc(cmd):
	return gdb.execute(cmd, to_string=True)


def setBkpt(file_name, lin_no):
	gc('b {}:{}'.format(file_name, lin_no))


def brk_main():
	gc('break main')


def run():
	gc('r')


def resume():
	gc('continue')


import sys


def init(log_file=''):
	gc('set pagination off')
	global f
	if log_file != '':
		f = open(log_file, 'w')
	else:
		f = sys.stdout


def log(msg):
	print(msg, file=f)


def deinit():
	if f != sys.stdout:
		f.close()


def exit():
	gc('q')


def read_mem(addr, siz):
	return gdb.inferiors()[0].read_memory(addr, siz)


def log_mem(addr, siz):
	byte_str = read_mem(addr, siz)
	make_str = str()
	lastIdx = 0
	for i,byte in enumerate(byte_str):
		make_str = make_str + format(int.from_bytes(byte, 'big'), '02x') + ' '
		if (i + 1) % 16 == 0:
			log(format(int(addr) - 16 + i + 1, '12x') + ': ' + make_str)
			make_str = ''
		lastIdx = i
	mod_lidx = (lastIdx + 1) % 16
	if mod_lidx != 0:
		log(format(int(addr) - 16 + (lastIdx + 1 + mod_lidx), '12x') + ': ' + make_str)
	make_str = ''
	log(make_str)


def get_var(var):
	return gdb.parse_and_eval(var)


def set_var_to_gdb_var(var, gdb_var):
	return gc(str('set ${} = {}'.format(gdb_var, var)))


def run_func(func):
	return gdb.parse_and_eval(func)


def setArgs(args):
	return gc('set args ' + args)