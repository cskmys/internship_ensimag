import pexpect

ch = pexpect.spawn('python3 child.py')
ch.sendline('test')
ch.expect('TEST')
ch.sendline('sest')
ch.expect('SEST')