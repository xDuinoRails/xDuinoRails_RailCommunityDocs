# Configuration file for the Sphinx documentation builder.
#
# Full list of options can be found in the Sphinx reference manual:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = 'Your Project Name'  # Replace with your project name
copyright = '2023, Your Name' # Replace with your name and year
author = 'Your Name' # Replace with your name

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',  # For automatic documentation from docstrings
    'sphinx.ext.napoleon', # For parsing NumPy and Google style docstrings
    'sphinx.ext.todo', # If you want to include todo's in your docs
    'sphinx.ext.mathjax', # For rendering math equations
    'sphinx.ext.ifconfig', # For conditional content based on config values
    'sphinx.ext.viewcode', # To add links to the source code
    'sphinx.ext.githubpages', # For deploying to Github pages
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme' # Use the Read the Docs theme (popular and good-looking)

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Extension settings -----------------------------------------------------

# Napoleon settings (if using NumPy or Google style docstrings)
napoleon_google_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_returns = True
napoleon_use_rtype = True
napoleon_preprocess_types = True
napoleon_type_aliases = None
napoleon_attr_annotations = True

# -- Autodoc settings -----------------------------------------------------
autodoc_member_order = 'bysource' # Order members by source code order
#autodoc_default_options = {
#    'members': True,
#    'undoc-members': True,  # Include undocumented members
#    'show-inheritance': True,
#}


# -- Options for EPUB output
epub_show_urls = 'no'

# -- Options for LaTeX output ---------------------------------------------
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',

    # Latex figure (float) alignment
    # 'figure_align': 'htbp',
}


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, target name, title, author, options).
man_pages = [
    (master_doc, 'yourproject', 'Your Project Name Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author, dir menu entry, description, category)
texinfo_documents = [
  (master_doc, 'YourProject', 'Your Project Name Documentation',
   author, 'YourProject', 'One line description of project.', 'Miscellaneous'),
]


# -- Options for linkcheck builder ------------------------------------
#  You can set the linkcheck_ignore list to domains that may be unavailable,
#  that you don't want to check, or that have unreliable DNS.
#
#  Example:
#  linkcheck_ignore = [
#      r'http\:\/\/example\.com\/?'
#  ]
#  linkcheck_timeout = 600
