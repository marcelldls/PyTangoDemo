'''Exploring PyTango'''

import tango
print(tango.__version__)
print(tango.ApiUtil.get_env_var("TANGO_HOST"))
