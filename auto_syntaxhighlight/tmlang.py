# import xml.etree.cElementTree as et
#
# root = et.Element('plist', version='1.0')
# dict = et.SubElement(root, 'dict')
# key_file_type = et.SubElement(dict, 'key').text = 'fileTypes'
#
# tree = et.ElementTree(root)
# tree.write('trial.xml')


def _get_keyword_lst_str(keyword_lst):
    keyword_lst_str = str()
    for keyword in keyword_lst:
        keyword_lst_str += keyword + '|'
    keyword_lst_str = keyword_lst_str[:-1]
    return keyword_lst_str


def mk_tmlang_file(tmlang_file_nam, file_ext, ext_id, keyword_lst):
    keyword_lst_str = _get_keyword_lst_str(keyword_lst)

    tmlang_str = """<?xml  version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN"   "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0" >
<!-- Generated via Iro -->
<dict>
  <key>fileTypes</key>
  <array>
    <string>{file_ext}</string>
   </array>
  <key>name</key>
  <string>{ext_id}</string>
  <key>patterns</key>
  <array>
    <dict>
      <key>include</key>
      <string>#main</string>
    </dict>
   </array>
  <key>scopeName</key>
  <string>source.{ext_id}</string>
  <key>uuid</key>
  <string></string>
  <key>repository</key>
  <dict>
    <key>main</key>
    <dict>
      <key>patterns</key>
      <array>
        <dict>
          <key>match</key>
          <string>({keyword_lst_str})</string>
          <key>name</key>
          <string>keyword.{ext_id}</string>
        </dict>
       </array>
    </dict>
  </dict>
</dict>
</plist>
""".format(file_ext=file_ext, ext_id=ext_id, keyword_lst_str=keyword_lst_str)
    tmlang_fil = open(tmlang_file_nam, 'wt')
    tmlang_fil.write(tmlang_str)
    tmlang_fil.close()
