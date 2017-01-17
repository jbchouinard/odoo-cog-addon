# -*- coding: utf-8 -*-
# [[[cog
# import cog
# import cogconstants
# cog.outl(cogconstants.LICENSE_HEADER)
# ]]]
# [[[end]]]
# [[[cog
# import os
# from glob import glob
# fns = [f.split('/')[1][:-3] for f in glob('tests/*.py')]
# fns = [f for f in fns if f.startswith('test_') and not f.endswith('.cog')]
# if fns:
#    cog.outl('\nfrom . import (')
#    for f in fns:
#        cog.outl('    ' + f + ',')
#    cog.outl(')')
# ]]]
# [[[end]]]
