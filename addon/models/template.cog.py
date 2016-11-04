# -*- coding: utf-8 -*-
# [[[cog
# import cog
# import cogutils
# cog.outl(cogutils.LICENSE_HEADER)
# ]]]
# [[[end]]]

from openerp import api, fields, models, _
from openerp.addons import decimal_precision as dp


# [[[cog
# MODEL_NAME = "My Model"
#
# cog.outl('class %s(models.Models):' % MODEL_NAME.replace(' ', ''))
# cog.outl('    """%s"""' % MODEL_NAME)
# cog.outl("    _name = '%s'" % MODEL_NAME.lower().replace(' ', '.'))
# ]]]
# [[[end]]]
