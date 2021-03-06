#
# This file is part of Web Land Trajectory Service.
# Copyright (C) 2019-2020 INPE.
#
# Web Land Trajectory Service is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Configuration file for the Sphinx documentation builder system."""
import os

# -- Project information -----------------------------------------------------

project = 'Web Land Trajectory Service'
copyright = '2020, INPE'
author = 'INPE'

g = {}

with open(os.path.join('..', '..', 'wlts', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

# The full version, including alpha/beta/rc tags.
release = version

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

def setup(app):
    app.add_stylesheet('wlts.css')

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

todo_emit_warnings = True

doctest_global_setup = '''
import os

WLTS_EXAMPLE_URL = os.getenv('WLTS_EXAMPLE_URL', None)
'''

master_doc = 'index'