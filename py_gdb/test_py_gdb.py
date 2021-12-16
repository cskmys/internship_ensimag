#!/usr/bin/env python3
import os
import global_var as gv
import gdb_py as gp


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main():
    gp.init()
    gp.setBkpt(gv.STOP_FILE, gv.STOP_LIN_NO)
    # gp.brk_main()
    gp.setArgs('5 6')
    gp.run()
    print(bcolors.FAIL + 'Bonjour, Attention svp!' + bcolors.ENDC)
    print(bcolors.OKGREEN + 'This argc value is printed from python script:' + str(gp.get_var('argc')) + bcolors.ENDC)
    gp.deinit()
    gp.exit()


if __name__ == '__main__':
    main()
