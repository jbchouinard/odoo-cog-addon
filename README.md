# odoo-cog-addon

Automatically generate Odoo addon boilerplate.

## Requirements

```
pip install cogapp
```

## Usage

Edit module constants in `cogconstants.py`.

If you want, copy and modify the .cog.py templates for models, wizards, tests, views.

Generate code by running `cogmake.sh`. `README.rst`, `__manifest__.py` (or `__openerp__.py`), and `__init__.py` files will be automatically generated. Some parts of the manifest still need to be written by hand.

You can erase all the cog template files and utilities by running cogclean.sh (to ship the code without the code generators).
