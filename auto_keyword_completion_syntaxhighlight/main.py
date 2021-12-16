#!/usr/bin/env python3

import os
import replace as rep
import pexpect as pex

langcfg_dict = rep.get_dict_from_yaml('langcfg.yaml')
replace_file_lst = rep.get_dict_from_yaml('replacefiles.yaml')

keyword_lst = []
for keyword in langcfg_dict['keywords']:
    keyword_lst.append(keyword['name'])

langcfg_dict['keyword_lst_regex'] = rep.get_keyword_regex_str(keyword_lst)

rep.replace_file_contents(replace_file_lst['ipdir'], replace_file_lst['opdir'], replace_file_lst['list'], langcfg_dict)

json_fil = os.path.join(replace_file_lst['opdir'], 'lsp/server/src/langcfg.json')
rep.json_fil_from_dict(json_fil, langcfg_dict)

op_lsp_dir = os.path.join(replace_file_lst['opdir'], 'lsp')
os.chdir(op_lsp_dir)
lsp_cmd = pex.spawn('npm install')
lsp_cmd.wait()
lsp_cmd = pex.spawn('npm config get prefix')
lsp_cmd.wait()
npm_path = lsp_cmd.readline().decode("utf-8").rstrip()
vsce_path = os.path.join(npm_path, 'bin/vsce')
lsp_cmd = pex.spawn(vsce_path + ' package')
while True:
    try:
        lsp_cmd.read_nonblocking()
    except Exception:
        break
if lsp_cmd.isalive():
    lsp_cmd.wait()

rep.move_fil('*.vsix', '../')
os.chdir('../')
op_lsp_dir = os.path.join(os.getcwd(), 'lsp')
rep.del_dir_if_exist(op_lsp_dir)
