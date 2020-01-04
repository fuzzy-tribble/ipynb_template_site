# Github.io Pages Template for IPython Notebooks

A template for pushing ipython notebooks to github pages site.

*Adapted from ...*

# How to use

## Step 1: Get the site configs/styles and build tools

add the following line to your `_config.yml` file

`remote-theme: nancynobody/ipynb_template_site`






* Clone this repo and add your notebooks to the "notebooks" folder

OR

* Add the `docs/` and `tools/` folder to the current repo you have your notebooks in

## Step 2: Enable Github.io Pages on your site

* Enable github pages [as described here](https://guides.github.com/features/pages/)

*Note: Don't chose a theme...all styles are in the `docs` repo already*

**TODO: Update tools so they don't have to run the convert script manually**

## Step 3: Git add, commit, push
*  When you push to the notebooks folder, you should see the changes on your site

# Structure

* `docs/`: contains all of the website stylistic features

* `notebooks/`: contains all of the notebooks you want to include in the site

* `tools/`: tools for converting the python notebooks to html for the site