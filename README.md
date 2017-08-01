# odoo-cog-addon

Automatically generate Odoo addon boilerplate.

## Requirements

### Binaries

bash

### Python Packages

cogapp

## Usage

Edit module constants in `cogconstants.py`.

If you want, copy and modify the templates for models, wizards, tests, views.

For example, if your module has a new model Reference Number, copy template.cog.py
to reference_number.py. You can edit the MODEL_NAME variable; other model attributes
will be set automatically (the class name will be ReferenceNumber, the model name
will be reference.number).

Generate code by running

```./cogmake.sh```

`README.rst`, `__manifest__.py` (or `__openerp__.py`), and `__init__.py` files
will be automatically generated. Some parts of the manifest still need to be
written by hand.

You can erase all the cog template files and utilities by running

```./cogclean.sh```

(to ship the code without the code generators).

## Advanced Usage

See Cog documentation: http://nedbatchelder.com/code/cog/
