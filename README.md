# scons-dfu 📥
A SCons tool for creating DFU files.

## How to use

1) Add `dfu.py` into your SCons tools (i.e. `site_scons/site_tools/`).<br>or<br>Add this repo as a submodule to your repo and add its path to `toolpath` in your environment.
2) Include the tool in your environment and configure flags. See the tool files for construction variable names.
```python
env = Environment(tools = ['dfu', ...], DFUSUFFIXFLAGS = "-p <pid> -v <vid>", ...)
```
3) Build a DFU file!
```python
firmware_dfu = env.DfuPrefix("firmware.dfu", "firmware.bin")
# or
firmware_dfu = env.DfuSuffix("firmware.dfu", "firmware.bin")
```
