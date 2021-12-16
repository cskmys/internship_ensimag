import jsonrpyc
from subprocess import Popen, PIPE

p = Popen(["python3", "server.py"], stdin=PIPE, stdout=PIPE)
rpc = jsonrpyc.RPC(stdout=p.stdin, stdin=p.stdout)

#
# sync usage
#

print(rpc("greet", args=("John",), block=0.1))
# => "Hi, John!"


#
# async usage
#

def cb(err, res=None):
    if err:
        raise err
    print("callback got: " + res)


rpc("greet", args=("John",), callback=cb)

# cb is called asynchronously which prints
# => "callback got: Hi, John!"
