# Example configuration

This is an example `powerline` configuration that I'm using at the moment. To use it, copy all of its content under `~/.config/powerline` (or `$XDG_CONFIG_HOME/powerline`).

## Detailed steps

```
$ pip install powerline-status xontrib-powerline-binding powerline-gitstatus git+https://github.com/shimtom/powerline-exitstatus
$ mkdir -p ~/.config/powerline
# standing in the root of the cloned repository
$ cp example-powerline-config/* ~/.config/powerline/
$ echo 'xontrib load powerline_binding' >> ~/.xonshrc
```

## Orange underline issue

By default `powerline` uses non-breaking-spaces, but some terminals mark them (with orange underline for example). You can turn that off in your main powerline configuration by setting `use_non_breaking_spaces` to `false`. See the `powerline` documentation for reference: https://powerline.readthedocs.io/en/master/configuration/reference.html
