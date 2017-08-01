# -*- coding: utf-8 -*-
# [[[cog
# import cog
# import cogconstants
# cog.outl(cogconstants.LICENSE_HEADER)
# ]]]
# [[[end]]]

{
    # [[[cog
    # cog.outl("'name': '%s'," % cogconstants.TITLE)
    # cog.outl("'version': '%s.1.0.0'," % cogconstants.ODOO_VERSION)
    # ]]]
    # [[[end]]]
    'author': 'Savoir-faire Linux',
    'maintainer': 'Savoir-faire Linux',
    'website': 'http://www.savoirfairelinux.com',
    # [[[cog
    # cog.outl("'license': '%s'," % cogconstants.LICENSE)
    # cog.outl("'category': '%s'," % cogconstants.CATEGORY)
    # cog.outl("'summary': '%s'," % cogconstants.SUMMARY)
    # ]]]
    # [[[end]]]
    'depends': [
    ],
    'data': [
        'security/ir.model.access.csv',
        # [[[cog
        # import os
        # from glob import glob
        # views = [f.split('/')[1][:-3] for f in glob('views/*.xml')]
        # fns = [f for f in views if not f.endswith('.cog')]
        # for f in fns:
        #     cog.outl("'views/" + f + "xml" + "',")
        # wizviews = [f.split('/')[1][:-3] for f in glob('wizards/*.xml')]
        # fns = [f for f in wizviews if not f.endswith('.cog')]
        # for f in fns:
        #     cog.outl("'wizards/" + f + "xml" + "',")
        # ]]]
        # [[[end]]]
    ],
    'installable': True,
    'application': False,
}
