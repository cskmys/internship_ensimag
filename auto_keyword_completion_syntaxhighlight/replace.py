#!/usr/bin/env python3

import yaml
import json
import os
import glob
import shutil
from distutils.dir_util import copy_tree
from pathlib import Path


def rd_fil(fil_nam):
    with open(fil_nam, 'r') as rd_fil:
        file_dat = rd_fil.read()
    return file_dat


def wr_fil(fil_nam, fil_dat):
    with open(fil_nam, 'w') as wr_fil:
        wr_fil.write(fil_dat)


def get_search_tag(word):
    tag = '#$' + word + '$#'
    return tag


def get_dict_from_yaml(yaml_fil_nam):
    with open(yaml_fil_nam) as yaml_fil:
        yaml_dict = yaml.load(yaml_fil, Loader=yaml.FullLoader)
    return yaml_dict


def del_dir_if_exist(dirpath):
    dirpath = Path(dirpath)
    if dirpath.exists() and dirpath.is_dir():
        shutil.rmtree(dirpath)


def copy_dir(src, dest):
    copy_tree(src, dest)


def move_fil(fil, path):
    for file in glob.glob(fil):
        shutil.move(file, path)


def replace_file_contents(ipdir, opdir, replace_file_lst, replace_dict):
    del_dir_if_exist(opdir)

    copy_dir(ipdir, opdir)

    for replace_file in replace_file_lst:
        replace_file_path = os.path.join(opdir, replace_file['file'])
        fil_dat = rd_fil(replace_file_path)

        for word in replace_file['words']:
            fil_dat = fil_dat.replace(get_search_tag(word), replace_dict[word])

        replaced_file_path = replace_file_path
        wr_fil(replaced_file_path, fil_dat)


def get_keyword_regex_str(keyword_lst):
    keyword_lst_str = '('
    for keyword in keyword_lst:
        keyword_lst_str += keyword + '|'
    keyword_lst_str = keyword_lst_str[:-1]
    keyword_lst_str += ')'
    return keyword_lst_str


def json_fil_from_dict(json_fil, conv_dict):
    with open(json_fil, 'w', encoding='utf-8') as dump_file:
        json.dump(conv_dict, dump_file, ensure_ascii=False, indent=4)
        dump_file.write('\n')
