#!/usr/bin/env python3

import yaml
import json
from pprint import pprint as print

with open('langcfg.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data, sort_dicts=False)

with open('langcfg.json', 'w', encoding='utf-8') as dump_file:
    json.dump(data, dump_file, ensure_ascii=False, indent=4)
    dump_file.write('\n')
