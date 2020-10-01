# Xontrib-powerline-binding

[Powerline](https://github.com/powerline/powerline) binding for [xonsh](https://xon.sh), so you can use your existing `powerline` prompt in `xonsh`.

![Example image](xonsh_powerline_binding_example.png)

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

### Configuration

Add `xonsh` (and optionally `xonshtoolbar`) section to your `powerline` `config.json`:

```
{
  "ext": {
    "xonsh": {
      "theme": "mytheme"
    },
    "xonshtoolbar": {
      "theme": "mytheme"
    }
  }
}
```

Then create `themes/xonsh/mytheme.json` (and `themes/xonshtoolbar/mytheme.json`) with your theme configuration (see [Powerline documentation](https://powerline.readthedocs.io/en/master/configuration/reference.html#themes)).
You can find my example powerline configuration in the `example-powerline-config` folder.

## Extra segments

Currently includes the following xonsh specific powerline segments:

### `powerline_xonsh.exec_time`

Execution time of the last command.

Highlight group used: `exec_time`
