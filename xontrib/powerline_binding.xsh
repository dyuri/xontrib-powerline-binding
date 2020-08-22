"""Initialize prompts with `powerline`
"""
import builtins
import shutil
from powerline.shell import ShellPowerline


__all__ = ()


class FakeArgs(dict):
    def __getattr__(self, attr):
        return self.get(attr, "")


powerline_args = FakeArgs({
    "ext": ["shell"],
    "renderer_module": "shell",
    "jobnum": 0,  # TODO
    "last_pipe_status": 0,
    "last_exit_code": 0,
    "execution_time": 0
})
segment_info = {
    "args": powerline_args,
    "environ": builtins.__xonsh__.env,
    "client_id": 1,  # TODO ?
    "local_theme": None,  # TODO
}

xpl = ShellPowerline(powerline_args)


@events.on_postcommand
def update_args(cmd, rtn, out, ts):
    powerline_args["last_pipe_status"] = rtn
    powerline_args["last_exit_code"] = rtn
    powerline_args["execution_time"] = ts[1] - ts[0] if ts else 0


def powerline_prompt():
    width = shutil.get_terminal_size(80)[0]
    ps = ""
    for line in xpl.render_above_lines(width=width, segment_info=segment_info):
        ps += line + "\n"
    ps += xpl.render(width=width, side="left", segment_info=segment_info)

    return ps


def powerline_right_prompt():
    width = shutil.get_terminal_size(80)[0]
    return xpl.render(width=width, side="right", segment_info=segment_info)


def powerline_init():
    builtins.__xonsh__.env["PROMPT"] = powerline_prompt
    builtins.__xonsh__.env["RIGHT_PROMPT"] = powerline_right_prompt
    # TODO
    # - TOOLBAR
    # - MULTILINE_PROMPT
    # - TITLE


builtins.aliases["powerline_init"] = powerline_init
powerline_init()
