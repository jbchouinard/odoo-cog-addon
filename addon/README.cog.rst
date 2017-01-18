[[[cog
import cog
import cogconstants
cog.outl("=" * len(cogconstants.TITLE))
cog.outl(cogconstants.TITLE)
cog.outl("=" * len(cogconstants.TITLE))
]]]
[[[end]]]
[[[cog cog.outl(cogconstants.DESCRIPTION) ]]]
[[[end]]]

Contributors
------------
[[[cog
for c in cogconstants.CONTRIBUTORS:
    line = '* %s (%s)' % (c[0], c[1])
    cog.outl(line)
]]]
[[[end]]]

More information
----------------
[[[cog
cog.outl('* Module developed and tested with Odoo version %s' % cogconstants.ODOO_VERSION) 
]]]
[[[end]]]
* For questions, please contact our support services
(support@savoirfairelinux.com)
