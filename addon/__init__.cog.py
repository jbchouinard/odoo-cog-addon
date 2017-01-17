# -*- coding: utf-8 -*-
# [[[cog
# import cog
# import cogconstants
# cog.outl(cogconstants.LICENSE_HEADER)
# ]]]
# [[[end]]]
# [[[cog
# import os
# usual_folders = ('model', 'models', 'wizard', 'wizards')
# folders = [f for f in usual_folders if os.path.exists('./%s' % f)]
# if folders:
#     cog.outl('from . import (')
#     for f in folders:
#         cog.outl('    ' + f + ',')
#     cog.outl(')')
# ]]]
# [[[end]]]
