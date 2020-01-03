---
layout: notebook
title: Bla
permalink: \bla\
topics: ['test1', 'test2']
---
<!--NB_INFO-->
    <img align="left" style="padding-right:10px;" src="images/python.png">
    <p>This notebook contains an excerpt from the [Python Data Science Handbook](http://shop.oreilly.com/product/0636920034919.do) by Jake VanderPlas; the content is available [on GitHub](https://github.com/jakevdp/PythonDataScienceHandbook).</p>
    <p>The text is released under the [CC-BY-NC-ND license](https://creativecommons.org/licenses/by-nc-nd/3.0/us/legalcode), and code is released under the [MIT license](https://opensource.org/licenses/MIT). If you find this content useful, please consider supporting the work by [buying the book](http://shop.oreilly.com/product/0636920034919.do)!</p><div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Bla">Bla<a class="anchor-link" href="#Bla">&#182;</a></h1><p><strong>Purpose:</strong> The purpose of this workbook is to help you get comfortable with functions in Python3.</p>
<p><strong>Recomended Usage</strong></p>
<ul>
<li>Run each of the cells (Shift+Enter) and edit them as necessary to solidify your understanding</li>
<li>Do any of the exercises that are relevant to helping you understand the material</li>
</ul>
<p><strong>Topics Covered</strong></p>
<ul>
<li>Basic Functions</li>
<li>Generators</li>
<li>Lambda Expressions</li>
<li>Partial Functions</li>
<li>Nested Functions</li>
<li>Positional and Keyword Arguments (args and kwargs)</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Workbook-Setup">Workbook Setup<a class="anchor-link" href="#Workbook-Setup">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Troubleshooting-Tips">Troubleshooting Tips<a class="anchor-link" href="#Troubleshooting-Tips">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>If you run into issues running any of the code in this notebook, check your version of Jupyter, extensions, etc.</p>
<div class="highlight"><pre><span></span>!jupyter --version

jupyter core     : <span class="m">4</span>.6.1
jupyter-notebook : <span class="m">6</span>.0.2
qtconsole        : not installed
ipython          : <span class="m">7</span>.9.0
ipykernel        : <span class="m">5</span>.1.3
jupyter client   : <span class="m">5</span>.3.4
jupyter lab      : <span class="m">1</span>.2.3
nbconvert        : <span class="m">5</span>.6.1
ipywidgets       : not installed
nbformat         : <span class="m">4</span>.4.0
traitlets        : <span class="m">4</span>.3.3
</pre></div>
<div class="highlight"><pre><span></span>!jupyter-labextension list

JupyterLab v1.2.3
Known labextensions:
   app dir: /usr/local/share/jupyter/lab
        @aquirdturtle/collapsible_headings v0.5.0  enabled  OK
        @jupyter-widgets/jupyterlab-manager v1.1.0  enabled  OK
        @jupyterlab/git v0.8.2  enabled  OK
        @jupyterlab/github v1.0.1  enabled  OK
        jupyterlab-flake8 v0.4.0  enabled  OK

Uninstalled core extensions:
    @jupyterlab/github
    jupyterlab-flake8
</pre></div>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="ch">#!jupyter --version</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="ch">#!jupyter-labextension list</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Notebook-Configs">Notebook Configs<a class="anchor-link" href="#Notebook-Configs">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># AUTO GENERATED CELL FOR NOTEBOOK SETUP</span>

<span class="c1"># NOTEBOOK WIDE MAGICS</span>

<span class="c1"># Reload all modules before executing a new line</span>
<span class="o">%</span><span class="k">load_ext</span> autoreload
<span class="o">%</span><span class="k">autoreload</span> 2

<span class="c1"># Abide by PEP8 code style</span>
<span class="o">%</span><span class="k">load_ext</span> pycodestyle_magic
<span class="o">%</span><span class="k">pycodestyle_on</span>

<span class="c1"># LIBRARY SPECIFIC MAGICS - UNCOMMENT AS NEEDED</span>

<span class="c1"># Plot all matplotlib plots in output cell and save on close</span>
<span class="c1"># %matplotlib inline</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">functools</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Basic-Functions">Basic Functions<a class="anchor-link" href="#Basic-Functions">&#182;</a></h1><blockquote><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">function_name</span><span class="p">(</span><span class="n">arg_1</span><span class="p">,</span> <span class="n">arg_2</span><span class="p">):</span>
    <span class="k">pass</span>
</pre></div>
</blockquote>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">my_function</span><span class="p">(</span><span class="n">arg_1</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;arg_1 is: </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">arg_1</span><span class="p">))</span>


<span class="n">my_function</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>arg_1 is: test
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">my_function</span><span class="p">(</span><span class="n">arg_1</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">arg_1</span> <span class="o">+</span> <span class="mi">1</span>


<span class="n">result</span> <span class="o">=</span> <span class="n">my_function</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>4
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Generators">Generators<a class="anchor-link" href="#Generators">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Generators produce values one-at-a-time as opposed to functions which give them all at once. Its particularly useful when dealing with big data because we just access values one at a time.</p>
<div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">my_generator</span><span class="p">():</span>
    <span class="k">yield</span> <span class="s2">&quot;a&quot;</span>
</pre></div>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Generator-functions">Generator functions<a class="anchor-link" href="#Generator-functions">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[27]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Regular function</span>
<span class="k">def</span> <span class="nf">function_a</span><span class="p">():</span>
    <span class="k">return</span> <span class="s2">&quot;a&quot;</span>

<span class="c1"># Generator function</span>
<span class="k">def</span> <span class="nf">generator_a</span><span class="p">():</span>
    <span class="k">yield</span> <span class="s2">&quot;a&quot;</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[28]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">function_a</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[28]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&#39;a&#39;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[29]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">generator_a</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[29]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;generator object generator_a at 0x11410df50&gt;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[32]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">next</span><span class="p">(</span><span class="n">generator_a</span><span class="p">())</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[32]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&#39;a&#39;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><em>Note: You can only use a generator ONCE (once you get to the end, you're done).</em></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Generator-Expressions">Generator Expressions<a class="anchor-link" href="#Generator-Expressions">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[43]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Traditional list comprehension (uses brackets)</span>
<span class="n">lc_example</span> <span class="o">=</span> <span class="p">[</span><span class="n">n</span><span class="o">**</span><span class="mi">2</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">]]</span>
<span class="n">lc_example</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[43]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>[1, 4, 9, 16, 25]</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[48]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Generator expression (uses parentheses)</span>
<span class="n">gen_exp1</span> <span class="o">=</span> <span class="p">(</span><span class="n">n</span><span class="o">**</span><span class="mi">2</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">])</span>
<span class="n">gen_exp1</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[48]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;generator object &lt;genexpr&gt; at 0x113367350&gt;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>There are two ways to get the next item from a generator; next() and a for loop</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[49]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="nb">next</span><span class="p">(</span><span class="n">gen_exp1</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">next</span><span class="p">(</span><span class="n">gen_exp1</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">next</span><span class="p">(</span><span class="n">gen_exp1</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>1
4
9
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[52]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">gen_exp1</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">item</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>16
25
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[51]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">gen_exp2</span> <span class="o">=</span> <span class="p">(</span><span class="n">n</span><span class="o">**</span><span class="mi">2</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">]</span> <span class="k">if</span> <span class="n">n</span> <span class="o">&gt;=</span> <span class="mi">3</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">next</span><span class="p">(</span><span class="n">gen_exp2</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">next</span><span class="p">(</span><span class="n">gen_exp2</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>9
16
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>One practical example could be to read in a very large file row by row.</p>
<div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">rowByRowGenerator</span><span class="p">():</span>
    <span class="nb">file</span> <span class="o">=</span> <span class="s2">&quot;veryBIGFile.csv&quot;</span>
    <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="nb">open</span><span class="p">(</span><span class="nb">file</span><span class="p">):</span>
        <span class="k">yield</span> <span class="n">row</span>
</pre></div>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Lambda-Expressions">Lambda Expressions<a class="anchor-link" href="#Lambda-Expressions">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Lambda expressions (sometimes called lambda functions) are small (single expression) anonymous functions created using the lambda keyword. They are especially useful in situations when you don't want/need to use a whole function definition but rather just have a small expression.</p>
<blockquote><p><code>lambda arguments: expression</code></p>
</blockquote>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>For example, the following are functionally equivalent:</p>
<div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">f</span><span class="p">(</span><span class="n">x</span><span class="p">):</span> <span class="k">return</span> <span class="mi">2</span><span class="o">*</span><span class="n">x</span> 
<span class="c1"># ACTS THE SAME AS</span>
<span class="n">f</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="mi">2</span><span class="o">*</span><span class="n">x</span>
</pre></div>
<p><span style="color:red;"><b>Best Practice Note:</b> Though the def and lambda expression above are equivalent, you generally want to assign a lambda expression to a name. It defeats the purpose of it, see best use cases below.</span></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Lambda-expressions-as-function-arguments">Lambda expressions as function arguments<a class="anchor-link" href="#Lambda-expressions-as-function-arguments">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Lambda expressions are really useful when a function takes another function as a parameter like in the <code>map()</code> function</p>
<blockquote><p><code>map(func, *iterables) --&gt; map object</code></p>
</blockquote>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">original_list</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">doubled_list</span> <span class="o">=</span> <span class="nb">map</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="o">*</span><span class="mi">2</span><span class="p">,</span> <span class="n">original_list</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s1">&#39;Original List: </span><span class="si">{}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">original_list</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;Doubled List: </span><span class="si">{}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">doubled_list</span><span class="p">)))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Original List: [1, 2, 3, 4]
Doubled List: [2, 4, 6, 8]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>You can also use it in the case of in the <code>sort()</code> function.</p>
<blockquote><p><code>sort(*, key=None, reverse=False)</code></p>
</blockquote>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">pairs</span> <span class="o">=</span> <span class="p">[(</span><span class="mi">4</span><span class="p">,</span> <span class="s1">&#39;c&#39;</span><span class="p">),</span> <span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="s1">&#39;b&#39;</span><span class="p">),</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="s1">&#39;a&#39;</span><span class="p">),</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="s1">&#39;d&#39;</span><span class="p">)]</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Sort the pairs by the 0th element in each pair</span>
<span class="n">pairs</span><span class="o">.</span><span class="n">sort</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">pair</span><span class="p">:</span> <span class="n">pair</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
<span class="nb">print</span><span class="p">(</span><span class="n">pairs</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[(1, &#39;d&#39;), (2, &#39;b&#39;), (3, &#39;a&#39;), (4, &#39;c&#39;)]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Sort the pairs by the 1th element in each pair</span>
<span class="n">pairs</span><span class="o">.</span><span class="n">sort</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">pair</span><span class="p">:</span> <span class="n">pair</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
<span class="nb">print</span><span class="p">(</span><span class="n">pairs</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[(3, &#39;a&#39;), (2, &#39;b&#39;), (4, &#39;c&#39;), (1, &#39;d&#39;)]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Partial-Functions">Partial Functions<a class="anchor-link" href="#Partial-Functions">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>After importing partial from functools you can use partial functions.</p>
<p>A partial function is really useful for being able to add some default arguments to a function so you don't need to repeat all the arguments all of the time.</p>
<p>The general syntax for a partial function is this:</p>
<blockquote><p><code>variable = partial(function_name, function_params)</code></p>
</blockquote>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">functools</span> <span class="k">import</span> <span class="n">partial</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Say we have a regular function def that multiplies two numbers</span>
<span class="k">def</span> <span class="nf">multiply</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">x</span> <span class="o">*</span> <span class="n">y</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># We can create a new function that multiplies by 2</span>
<span class="n">dbl</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">multiply</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Then dbl(4) is called with the 2 already there</span>
<span class="nb">print</span><span class="p">(</span><span class="n">dbl</span><span class="p">(</span><span class="mi">4</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>2 4
8
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>In this case we start with a normal function definition called <code>multiply()</code> that multiplies to inputs. We can then create a partial function definition that uses a spin off of that function called <code>dble</code> by always setting one param as 2.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Nested-Functions">Nested Functions<a class="anchor-link" href="#Nested-Functions">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>In Python, you can define nested or inner functions like in the examples below. They are most widely used in the case of decorators (see the "Decorators Workbook" for more).</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">parent</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;parent() funct&quot;</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">first_child</span><span class="p">():</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;first_child() funct&quot;</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">second_child</span><span class="p">():</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;second_child() funct&quot;</span><span class="p">)</span>

    <span class="n">first_child</span><span class="p">()</span>
    <span class="n">second_child</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">parent</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>parent() funct
first_child() funct
second_child() funct
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>We can call <code>parent()</code> and return the functions that handle each case</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">parent</span><span class="p">(</span><span class="n">num</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">first_child</span><span class="p">():</span>
        <span class="k">return</span> <span class="s2">&quot;Hi, I am the 1st child&quot;</span>

    <span class="k">def</span> <span class="nf">second_child</span><span class="p">():</span>
        <span class="k">return</span> <span class="s2">&quot;Hi, I am the 2nd child&quot;</span>

    <span class="k">if</span> <span class="n">num</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">first_child</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">second_child</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">first</span> <span class="o">=</span> <span class="n">parent</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="n">first</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[10]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;function __main__.parent.&lt;locals&gt;.first_child()&gt;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">first</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[11]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&#39;Hi, I am the 1st child&#39;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[12]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">second</span> <span class="o">=</span> <span class="n">parent</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
<span class="n">second</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[12]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;function __main__.parent.&lt;locals&gt;.second_child()&gt;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[13]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">second</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[13]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&#39;Hi, I am the 2nd child&#39;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Positional-and-Keyword-Arguments">Positional and Keyword Arguments<a class="anchor-link" href="#Positional-and-Keyword-Arguments">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Functions in Python can have positional and/or keyword arguments. They can be a fixed number of arguments or variable.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>In Python3.8 there is a new function parameter syntax <code>/</code> to indicate that some function parameters must be specified positionally and cannot be used as keyword arguments. Check out the <a href="https://docs.python.org/3.8/whatsnew/3.8.html#summary-release-highlights">examples from the docs below</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Make sure you are using Python3 or you may get an error</span>
<span class="kn">import</span> <span class="nn">sys</span>
<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">version</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>3.7.5 (default, Nov  1 2019, 13:00:01) 
[Clang 11.0.0 (clang-1100.0.33.8)]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">f</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">,</span> <span class="o">/</span><span class="p">,</span> <span class="n">c</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">e</span><span class="p">,</span> <span class="n">f</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">,</span> <span class="n">c</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="n">e</span><span class="p">,</span> <span class="n">f</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_text output_error">
<pre>
<span class="ansi-cyan-fg">  File </span><span class="ansi-green-fg">&#34;&lt;ipython-input-4-bd67c2300f8f&gt;&#34;</span><span class="ansi-cyan-fg">, line </span><span class="ansi-green-fg">1</span>
<span class="ansi-red-fg">    def f(a, b, /, c, d, *, e, f):</span>
                ^
<span class="ansi-red-fg">SyntaxError</span><span class="ansi-red-fg">:</span> invalid syntax
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">f</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="mi">30</span><span class="p">,</span> <span class="n">d</span><span class="o">=</span><span class="mi">40</span><span class="p">,</span> <span class="n">e</span><span class="o">=</span><span class="mi">50</span><span class="p">,</span> <span class="n">f</span><span class="o">=</span><span class="mi">60</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">f</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="n">b</span><span class="o">=</span><span class="mi">20</span><span class="p">,</span> <span class="n">c</span><span class="o">=</span><span class="mi">30</span><span class="p">,</span> <span class="n">d</span><span class="o">=</span><span class="mi">40</span><span class="p">,</span> <span class="n">e</span><span class="o">=</span><span class="mi">50</span><span class="p">,</span> <span class="n">f</span><span class="o">=</span><span class="mi">60</span><span class="p">)</span>   <span class="c1"># b cannot be a keyword argument</span>
<span class="n">f</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="mi">30</span><span class="p">,</span> <span class="mi">40</span><span class="p">,</span> <span class="mi">50</span><span class="p">,</span> <span class="n">f</span><span class="o">=</span><span class="mi">60</span><span class="p">)</span>           <span class="c1"># e must be a keyword argument</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Since the parameters to the left of / are not exposed as possible keywords, the parameters names remain available for use in **kwargs:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">f</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">,</span> <span class="o">/</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span>

<span class="n">f</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="n">a</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">b</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span> <span class="n">c</span><span class="o">=</span><span class="mi">3</span><span class="p">)</span>         <span class="c1"># a and b are used in two ways</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Packing-and-unpacking-using-*">Packing and unpacking using <code>*</code><a class="anchor-link" href="#Packing-and-unpacking-using-*">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>When you see <code>*</code> or <code>**</code> in front of a variable in Python they are used to unpack iterables and dictionaries respectively.</p>
<p>They are frequently used to unpack a variable number of function arguments using <code>*args</code> (arguments) and <code>**kwargs</code> (keyword arguments) in function definitions.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[37]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># *args is used to pass in a variable number of arguments</span>
<span class="k">def</span> <span class="nf">sayThis1</span><span class="p">(</span><span class="o">*</span><span class="n">argv</span><span class="p">):</span>
    <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">argv</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">arg</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>2:1: E302 expected 2 blank lines, found 0
2:1: E302 expected 2 blank lines, found 0
2:1: E302 expected 2 blank lines, found 0
2:1: E302 expected 2 blank lines, found 0
2:1: E302 expected 2 blank lines, found 0
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[15]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sayThis1</span><span class="p">(</span><span class="s1">&#39;Hi&#39;</span><span class="p">,</span> <span class="s1">&#39;whats&#39;</span><span class="p">,</span> <span class="s1">&#39;going&#39;</span><span class="p">,</span> <span class="s1">&#39;on&#39;</span><span class="p">)</span> <span class="c1"># Pass in any number of args</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_text output_error">
<pre>
<span class="ansi-red-fg">---------------------------------------------------------------------------</span>
<span class="ansi-red-fg">NameError</span>                                 Traceback (most recent call last)
<span class="ansi-green-fg">&lt;ipython-input-15-52fbf7181596&gt;</span> in <span class="ansi-cyan-fg">&lt;module&gt;</span>
<span class="ansi-green-fg">----&gt; 1</span><span class="ansi-red-fg"> </span>sayThis1<span class="ansi-blue-fg">(</span><span class="ansi-blue-fg">&#39;Hi&#39;</span><span class="ansi-blue-fg">,</span> <span class="ansi-blue-fg">&#39;whats&#39;</span><span class="ansi-blue-fg">,</span> <span class="ansi-blue-fg">&#39;going&#39;</span><span class="ansi-blue-fg">,</span> <span class="ansi-blue-fg">&#39;on&#39;</span><span class="ansi-blue-fg">)</span> <span class="ansi-red-fg"># Pass in any number of args</span>

<span class="ansi-red-fg">NameError</span>: name &#39;sayThis1&#39; is not defined</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>1:39: E261 at least two spaces before inline comment
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># **kwargs is used to pass a variable number of keyword arguments   </span>
<span class="k">def</span> <span class="nf">sayThis2</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
    <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">items</span><span class="p">():</span> 
        <span class="nb">print</span> <span class="p">(</span><span class="s2">&quot;</span><span class="si">%s</span><span class="s2"> == </span><span class="si">%s</span><span class="s2">&quot;</span> <span class="o">%</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[31]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sayThis2</span><span class="p">(</span><span class="n">first</span> <span class="o">=</span><span class="s1">&#39;Love&#39;</span><span class="p">,</span> <span class="n">mid</span> <span class="o">=</span><span class="s1">&#39;is&#39;</span><span class="p">,</span> <span class="n">last</span><span class="o">=</span><span class="s1">&#39;good&#39;</span><span class="p">)</span> 
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>first == Love
mid == is
last == good
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[25]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">my_list</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">my_list</span><span class="p">)</span>  <span class="c1"># Packed</span>
<span class="nb">print</span><span class="p">(</span><span class="o">*</span><span class="n">my_list</span><span class="p">)</span>  <span class="c1"># Unpacked</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[1, 2, 3]
1 2 3
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Extract/unpack-the-body-of-a-list">Extract/unpack the body of a list<a class="anchor-link" href="#Extract/unpack-the-body-of-a-list">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The asterisk can also be used to unpack the body of something.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">my_list</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">]</span>
<span class="n">my_list</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[6]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>[1, 2, 3, 4, 5, 6]</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[29]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">a</span><span class="p">,</span> <span class="o">*</span><span class="n">b</span><span class="p">,</span> <span class="n">c</span> <span class="o">=</span> <span class="n">my_list</span>
<span class="nb">print</span><span class="p">(</span><span class="n">a</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">b</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">c</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>1
[2, 3, 4, 5]
6
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Merging-lists-and-dicts-by-unpacking">Merging lists and dicts by unpacking<a class="anchor-link" href="#Merging-lists-and-dicts-by-unpacking">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[32]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">list1</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span>
<span class="n">list2</span> <span class="o">=</span> <span class="p">[</span><span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">]</span>
<span class="n">merged_list</span> <span class="o">=</span> <span class="p">[</span><span class="o">*</span><span class="n">list1</span><span class="p">,</span> <span class="o">*</span><span class="n">list2</span><span class="p">]</span>  <span class="c1"># Unpack each list into a new list</span>

<span class="nb">print</span><span class="p">(</span><span class="n">merged_list</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[1, 2, 3, 4, 5, 6]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[33]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dict1</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;A&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span> <span class="s2">&quot;B&quot;</span><span class="p">:</span> <span class="mi">2</span><span class="p">}</span>
<span class="n">dict2</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;C&quot;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span> <span class="s2">&quot;D&quot;</span><span class="p">:</span> <span class="mi">4</span><span class="p">}</span>
<span class="n">merged_dict</span> <span class="o">=</span> <span class="p">{</span><span class="o">**</span><span class="n">dict1</span><span class="p">,</span> <span class="o">**</span><span class="n">dict2</span><span class="p">}</span>

<span class="nb">print</span><span class="p">(</span><span class="n">merged_dict</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>{&#39;A&#39;: 1, &#39;B&#39;: 2, &#39;C&#39;: 3, &#39;D&#39;: 4}
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Unpack-a-string-into-chars">Unpack a string into chars<a class="anchor-link" href="#Unpack-a-string-into-chars">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[35]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">a</span> <span class="o">=</span> <span class="p">[</span><span class="o">*</span><span class="s2">&quot;SomeStringOfChars&quot;</span><span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">a</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[&#39;S&#39;, &#39;o&#39;, &#39;m&#39;, &#39;e&#39;, &#39;S&#39;, &#39;t&#39;, &#39;r&#39;, &#39;i&#39;, &#39;n&#39;, &#39;g&#39;, &#39;O&#39;, &#39;f&#39;, &#39;C&#39;, &#39;h&#39;, &#39;a&#39;, &#39;r&#39;, &#39;s&#39;]
</pre>
</div>
</div>

</div>
</div>

</div>
 

