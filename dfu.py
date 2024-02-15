# SCons tool for creating DFU files
#
# Builders
# - DfuPrefix: builds a dfu file with dfu-prefix
# - DfuSuffix: builds a dfu file with dfu-suffix

from SCons.Builder import Builder
from SCons.Action import Action

dfu_prefix_builder = None
dfu_suffix_builder = None
dfu_prefix_action = None
dfu_suffix_action = None

def generate(env):

    # Create actions and builders
    #

    global dfu_prefix_action
    if (dfu_prefix_action is None):
        dfu_prefix_action = Action(["cp $SOURCE $TARGET", "$DFUPREFIXCOM"], "$DFUPREFIXCOMSTR")

    global dfu_suffix_action
    if (dfu_suffix_action is None):
        dfu_suffix_action = Action(["cp $SOURCE $TARGET", "$DFUSUFFIXCOM"], "$DFUSUFFIXCOMSTR")

    global dfu_prefix_builder
    if (dfu_prefix_builder is None):
        dfu_prefix_builder = Builder(action = dfu_prefix_action,
                              prefix = "$DFUPREFIX",
                              suffix = "$DFUSUFFIX",
                              emitter = {},
                              source_ext_match = None,
                              single_source = True)

    global dfu_suffix_builder
    if (dfu_suffix_builder is None):
        dfu_suffix_builder = Builder(action = dfu_suffix_action,
                              prefix = "$DFUPREFIX",
                              suffix = "$DFUSUFFIX",
                              emitter = {},
                              source_ext_match = None,
                              single_source = True)

    # Prep environment
    #

    env["DFUPREFIX"] = ""
    env["DFUSUFFIX"] = ".dfu"

    # this is a bit confusing because there is a dfu-prefix and dfu-suffix program,
    # but this refers to the beggining of dfu commands
    env["DFUPREFIXPROG"] = "dfu-prefix"
    env["DFUSUFFIXPROG"] = "dfu-suffix"
    env["DFUPREFIXFLAGS"] = ""
    env["DFUSUFFIXFLAGS"] = ""
 
    env["DFUPREFIXCOM"] = "$DFUPREFIXPROG $DFUPREFIXFLAGS -a $TARGET"
    env["DFUSUFFIXCOM"] = "$DFUSUFFIXPROG $DFUSUFFIXFLAGS -a $TARGET"

    # Add builders
    #

    env["BUILDERS"]["DfuPrefix"] = dfu_prefix_builder
    env["BUILDERS"]["DfuSuffix"] = dfu_suffix_builder

def exists():
    return True
