import nbformat
import glob
import os
import re
from traitlets.config import Config
from nbconvert import HTMLExporter
from shutil import copyfile

from custom_configs import *

# Setup html exporter template/configs
html_exporter = HTMLExporter()
html_exporter.template_file = 'basic'


def get_body(nb_node):
    """ Get HTML body from notebook """
    (body, resources) = html_exporter.from_notebook_node(nb_node)
    fixed_body = fix_links(body)
    return fixed_body


def fix_links(body):
    """ Find all local asset links and correct """
    #TODO: Fix to handle no folder case: src="python_xkcd.svg"
    #TODO: Fix to use relative urls to get rid of hardcoded ipynb_template_site...
    # href="{{ '/assets/minima-social-icons.svg#dribbble' | relative_url }}"

    NB_ASSET_DIRS = ['figures', 'images', 'img']
    correct_asset_dir = 'src="/ipynb_template_site/assets/images/'
    s = '|'.join(NB_ASSET_DIRS)
    regex = re.compile(r'(?:source|src)=\"\/?(?:%s)\/' % s, re.IGNORECASE)

    fixed_body = re.sub(regex, correct_asset_dir, body)
    
    return fixed_body


def get_nb_info(nb_node):
    """ Return nb info from configs or nothing"""
    return NB_INFO or False


def get_nb_title(nb_node):
    """ Get notebook title give a nb_node (json) """
    for cell in nb_node.cells:
        if cell.source.startswith('#'):
            return cell.source[1:].splitlines()[0].strip()


def get_nb_topics(nb_node):
    """ Get notebook topics give a nb_node (json) """
    txt_src = nb_node.cells[0].source
    m = re.search(REGEX_TOPICS, txt_src)
    topics = m.group(0).replace("**Topics Covered**\n* ", "").split("\n* ") 
    return str(topics)


def get_front_matter(nb_node):
    """ Get front matter for Jekyll """
    layout = "notebook"
    title = get_nb_title(nb_node)
    # TODO HARDEN - check for special chars in title
    permalink = title.lower().replace(" ", "-")
    topics = str(get_nb_topics(nb_node))
    return "---\nlayout: {}\ntitle: {}\npermalink: /{}/\ntopics: {}\n---\n".format(layout, title, permalink, topics)


def get_nb_nav():
    """ Get html for notebook navigation """
    #TODO implement prev/next nb links
    prev_nb = '&lt; <a href="#">Next NB Title</a> | '
    contents = '<a href="/ipynb_template_site/">Contents</a>'
    next_nb = ' | <a href="#">Next NB Title</a> &gt;'
    nb_nav = '<p style="font-style:italic;font-size:smaller;">{}{}{}</p>'.format(prev_nb, contents, next_nb)
    return nb_nav


def ipynb_to_html(in_nb_dir, out_nb_dir=""):
    """
    Convert list of ipython notebooks to final html files
    with front matter, navigation, body, etc.
    """

    nb_files = glob.glob(in_nb_dir + '*.ipynb')

    if len(nb_files) < 1:
        print("Found no notebooks to convert in {}".format(in_nb_dir))

    for nb_file in nb_files:
        nb_node = nbformat.read(nb_file, as_version=4)

        nb_file_name = nb_file.split("/")[-1]

        front_matter = get_front_matter(nb_node)
        nb_info = get_nb_info(nb_node)
        nb_nav = get_nb_nav()
        body = get_body(nb_node)

        write_path = out_nb_dir + nb_file_name[:-5] + "html"
        print("Writing notebook: {}...".format(write_path))

        with open(write_path, "w") as file:
            file.write(front_matter)
            if nb_info:
                file.write(nb_info)
            if nb_nav:
                file.write(nb_nav)
            file.write(body)

def move_nb_assets(inp_ass_dirs, out_assets_dir):
    """ Move notebook assets to docs/assets folder """
    dest = os.path.join(os.path.dirname(__file__), '..', 'docs/assets/images/')
    print("Preparing to copy asset files to {}...".format(dest.split("/")[-4]))

    for subdir in inp_ass_dirs:
        files = glob.glob(INPUT_NB_DIR + subdir)
        for src in files:
            print("Copying file: {}...".format(src.split("/")[-1]))
            copyfile(src, dest)

if __name__ == '__main__':
    ipynb_to_html(INPUT_NB_DIR, OUTPUT_NB_DIR)
    move_nb_assets(NB_ASSET_DIRS)
    # TODO fix this shit - dont pass in if globally imported
