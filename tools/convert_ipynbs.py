import nbformat
import glob
import os
from traitlets.config import Config
from nbconvert import HTMLExporter

INPUT_NB_DIR = os.path.join(os.path.dirname(__file__), '..', 'notebooks')
OUTPUT_NB_DIR = '../docs/_notebooks/'

# Setup html exporter template/configs
html_exporter = HTMLExporter()
html_exporter.template_file = 'basic'

def get_body(nb_node):
    """ Get HTML body from notebook """
    (body, resources) = html_exporter.from_notebook_node(nb_node)
    return body

def get_nb_info(nb_node):
    NB_COMMENT = "<!--NB_INFO-->"
    NB_INFO = NB_COMMENT + """
    <img align="left" style="padding-right:10px;" src="images/python.png">
    <p>This notebook is part of the {{ site.title }}; the content is available <a href="https://github.com/nancynobody">on GitHub</a>.</p>"""
    return NB_INFO


def get_nb_title(nb_node):
    """ Get notebook title give a nb_node (json) """
    for cell in nb_node.cells:
        if cell.source.startswith('#'):
            return cell.source[1:].splitlines()[0].strip()


def get_nb_topics(nb_node):
    """ Get notebook topics give a nb_node (json) """
    # TODO
    return str(["test1", "test2"])


def get_front_matter(nb_node):
    """ Get front matter for Jekyll """
    layout = "notebook"
    title = get_nb_title(nb_node)
    permalink = title.lower()
    topics = str(get_nb_topics(nb_node))
    return "---\nlayout: {}\ntitle: {}\npermalink: \/{}\/\ntopics: {}\n---\n".format(layout, title, permalink, topics)


def ipynb_to_html(in_nb_dir, out_nb_dir=""):
    """
    Convert list of ipython notebooks to final html files
    with front matter, navigation, body, etc.
    """

    nb_files = glob.glob(in_nb_dir + '*.ipynb')

    for nb_file in nb_files:
        nb_node = nbformat.read(nb_file, as_version=4)

        nb_file_name = nb_file.split("/")[-1]

        front_matter = get_front_matter(nb_node)
        nb_info = get_nb_info(nb_node)
        body = get_body(nb_node)

        write_path = out_nb_dir + nb_file_name[:-5] + "html"
        print("Writing notebook: {}...".format(write_path))

        with open(write_path, "w") as file:
            file.write(front_matter)
            file.write(nb_info)
            file.write(body)


if __name__ == '__main__':
    try: 
        ipynb_to_html(INPUT_NB_DIR, OUTPUT_NB_DIR)
    