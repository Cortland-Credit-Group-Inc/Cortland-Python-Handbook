# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Cortland-Python-Handbook'
copyright = '2023, Bokun Huang'
author = 'Bokun Huang'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']


extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode'
]


# 使用插件支持markdowm
extensions.append('recommonmark')
# extensions.append('myst_parser')
extensions.append('sphinx_markdown_tables')

# 不进行编译的文件/文件夹
exclude_patterns = ['_build', 'Thumbs.db', 
                    '.DS_Store']


# 设置不同后缀的文件使用不同解析器(这个需要后加)
source_suffix = {
    '.rst': 'restructuredtext'
}

# 针对`.md`为后缀的文件做markdown渲染
source_suffix[".md"] = 'markdown'


# todo插件的设置
todo_include_todos = True

# 主题
extensions.append('sphinx_rtd_theme')
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    'logo_only': False,
    'navigation_depth': 5,}



def setup(app):
    # github_doc_root = 'https://localhost:5000'
    app.add_config_value('recommonmark_config', {
        # 'url_resolver': lambda url: github_doc_root + url,
        "enable_auto_toc_tree": True,
        "auto_toc_tree_section": "Contents",
        'auto_toc_maxdepth': 3,
        "enable_math": True,
        'enable_eval_rst': True
    }, True)
    
    #to adjust the max width of the page
    #the dependency file is in _static
    #reference: https://stackoverflow.com/questions/23211695/modifying-content-width-of-the-sphinx-theme-read-the-docs
    app.add_css_file('my_theme.css')
