# Github Pages Template for IPython Notebooks

This repo contains an adaptation of the [minima theme](https://jekyll.github.io/minima/) for IPython notebooks.

**Includes**

* Custom styles (`_sass/custom.css`) for displaying .ipynb's beautifully

* Custom scripts (`tools/convert_ipynbs.py`) for converting your Jupyter Notebooks (ipython specifically) for github pages

## Structure

Github Pages uses [Jekyll](https://jekyllrb.com/) as a static site generator. Checkout the [Github Pages Documentation](https://pages.github.com/) for more info.

*Note: This repo uses `theme: minima` (see `_config.yml`) with certain customizations that override the default theme by being defined explicitly in `_layouts`, `_notebooks`, `_sass`, `assets`, etc. To override any of minima's defaults, just define them explicitly in your sites repo and it will overwrite the default.*

**Repo Structure**

* `notebooks/`: contains contains your ipynb notebooks; here you edit your notebooks just like normal

* `tools/`: contains tools for ipynb conversion; here you will run a python script (`convert_ipynbs.py`) to build your site using the notebooks in your `notebooks/` folder above

* `docs/`: folder that contains all site configs

* `docs/_config.yml`: contains site configurations (eg. theme, site title, etc); update site title, description, etc here

* `docs/_layouts/`: contains the `home.html` and `notebook.html` layout configurations; change layout defaults for home or notebooks here using [Liquid](https://jekyllrb.com/docs/liquid/).

* `docs/_notebooks/`: contains the notebooks that have been converted using the python script (`tools/convert_ipynbs.py`); they contain front matter, site info and notebook content that was compiled using the `convert_ipynbs.py` script in `tools/`

* `docs/_sass/`: contains `custom.scss` style for displaying ipynbs; update the `custom.scss` file to add custom styles

* `docs/assets/`: contains default and custom style imports

* `docs/images/`: contains site images; including images from your notebooks that were placed here by the `convert_ipynbs.py` script

* `docs/pages/`: contains site pages that are not notebooks (eg. about, portfolio, etc); to add/remove pages do it here.

# Usage

The following steps will help you setup your repo so you have a folder structure like this repo with folders: `notebooks/`, `tools/`, and `docs/`

## Step 1: Get the site configs/styles and build tools

* Manually add the `docs/` and `tools/` folders + their contents to the current repo you have your notebooks in; and make sure your notebooks are placed into a notebooks folder.

## Step 2: Enable Github.io Pages on your site

* Enable github pages [as described here](https://guides.github.com/features/pages/)

* In the `Settings` tab of your repo, point the pages source to be the `docs/` folder rather than the master branch.

:exclamation: Don't chose a theme using the Github GUI! The minima theme is already in the `docs/_config.yml` repo already!

## Step 3: Build site, git add, commit, push

Now you can git add, commit, push to keep your notebooks folder up to date just like you normally would. But when you want to rebuild your site (that is, update all current notebooks on the site using your `notebooks` folder) just run the python script in tools, then git add, commit, push.

**Build Site (based on current `notebooks/`)**
```bash
cd tools
python convert_ipynbs.py
```

**Push changes to github + pages**
```bash
git add .
git commit -m "build site after 3 notebook updates"
git push
```

## Site Customizations

TODO: FILL THIS SECTION IN

Explain how to add google analytics and disqus
To customize styles
To customize html...

*Note: The html files use Liquid*

# Future TODOs

* Harden python conversion script

* Fix social icons in footer...apparently they aren't displaying on the site

* Write a gem so you don't have to run the python script

* Make an official theme so you don't have to copy the folders but can just use github pages new `remote_theme` config option in `_config.yml`

* Ugh