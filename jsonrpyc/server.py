import jsonrpyc


class MyTarget(object):

    def greet(self, name):
        return "Hi, %s!" % name


jsonrpyc.RPC(MyTarget())
