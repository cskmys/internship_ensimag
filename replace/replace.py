import yaml
import os
from distutils.dir_util import copy_tree


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


def copy_dir(src, dest):
    copy_tree(src, dest)


def replace_file_contents(ipdir, opdir, replace_file_lst, replace_dict):
    copy_dir(ipdir, opdir)

    for replace_file in replace_file_lst:
        replace_file_path = os.path.join(opdir, replace_file['file'])
        fil_dat = rd_fil(replace_file_path)

        for word in replace_file['words']:
            fil_dat = fil_dat.replace(get_search_tag(word), replace_dict[word])

        replaced_file_path = replace_file_path
        wr_fil(replaced_file_path, fil_dat)


def main():
    replace_dict = get_dict_from_yaml('replace.yaml')
    replace_file_lst = get_dict_from_yaml('replacefiles.yaml')
    replace_file_contents(replace_file_lst['ipdir'], replace_file_lst['opdir'], replace_file_lst['list'], replace_dict)


if __name__ == '__main__':
    main()
