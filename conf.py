import sys, os

extensions = [
    'sphinx.ext.autodoc',
    'myst_parser'
]

source_suffix = '.md'
master_doc = 'README'
exclude_patterns = []
add_function_parentheses = True

project = u'COMPAS-Surrogate'
copyright = u'2024, Avi V'

version = ''
release = ''

html_theme = "pydata_sphinx_theme"
html_title = "COMPAS-Surrogate"
# html_short_title = None
# html_logo = None
# html_favicon = None
html_static_path = ['_static']
html_domain_indices = False
html_use_index = False
html_show_sphinx = False
html_show_sourcelink = False


html_theme_options = {
  "external_links": [
      {"name": "LnL-Computer", "url": " https://compas-surrogate.github.io/lnl_computer/"},
      {"name": "LnL-Surrogate", "url": " https://compas-surrogate.github.io/lnl_surrogate/"}
  ]
}