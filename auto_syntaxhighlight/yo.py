import pexpect
import tmlang as tm

fil_nam = 'txt_syntax.tmLanguage'
ext_name = 'txt syntax highlight'
ext_id = 'txt'  # make sure there's no whitespace
descrip = 'boh'
file_ext = 'txt'  # make sure there's no whitespace
lang_nam = 'modified txt'
keyword_lst = ['TypeScript', 'JavaScript']
tm.mk_tmlang_file(tmlang_file_nam=fil_nam, file_ext=file_ext, ext_id=ext_id, keyword_lst=keyword_lst)

yo = pexpect.spawn('/home/csk/.npm-global/bin/yo code --extensionType=language')  # full path of yo as per your system

yo.expect('URL or file to import, or none for new')
yo.sendline(fil_nam)

yo.expect("What's the name of your extension")
yo.sendline(ext_name)

yo.expect("What's the identifier of your extension")
yo.sendline(ext_id)

yo.expect("What's the description of your extension")
yo.sendline(descrip)

lang_id = file_ext
yo.expect('Language id')
yo.sendline(lang_id)

yo.expect('Language name')
yo.sendline(lang_nam)

yo.expect('File extensions')
yo.sendline('.' + file_ext)

scope_nam = 'source.' + ext_id
yo.expect('Scope names')
yo.sendline(scope_nam)

yo.wait()
