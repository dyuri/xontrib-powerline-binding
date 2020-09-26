from .segments import exec_time
from powerline import Powerline


class PowerlineArgs(dict):
    def __getattr__(self, attr):
        return self.get(attr, "")


class XonshPowerline(Powerline):
    def __init__(self, args, part="", **kwargs):
        self.args = args
        self.part = "xonsh" + part
        self.valid = True
        super().__init__(self.part, "shell", **kwargs)

    def exception(self, *args, **kwargs):
        self.valid = False
