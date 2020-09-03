# Xontrib-powerline-binding

[Powerline](https://github.com/powerline/powerline) binding for [xonsh](https://xon.sh), so you can use your existing `powerline` prompt in `xonsh`.

## Install

Install using pip

```
pip install xontrib-powerline-binding
```

Add to your `.xonshrc`:

```
xontrib load powerline_binding
```

## Usage

Uses `powerline` to setup you `$PROMPT` and `$RIGHT_PROMPT`.

## Extra segments

Currently includes the following xonsh specific powerline segments:

### `powerline_xonsh.exec_time`

Execution time of the last command.

Highlight group used: `exec_time`

