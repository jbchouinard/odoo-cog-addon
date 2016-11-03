====================
[[[cog import cog; import cogutils; cog.outl(cogutils.TITLE) ]]]
[[[end]]]
====================
[[[cog cog.outl(cogutils.DESCRIPTION) ]]]
[[[end]]]

Contributors
------------
[[[cog
for c in cogutils.CONTRIBUTORS:
    line = '* %s (%s)' % (c[0], c[1])
    cog.outl(line)
]]]
[[[end]]]

More information
----------------
[[[cog
cog.outl('* Module developed and tested with Odoo version %s' % cogutils.ODOO_VERSION) 
]]]
[[[end]]]
* For questions, please contact our support services
(support@savoirfairelinux.com)
