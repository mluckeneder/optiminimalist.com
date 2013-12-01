---
tags:
tldr: Virtualenv and Virtualenvwrapper provide a simple way to manage multiple Python versions
---
# Managing multiple Python version in OS X

When I worked with Ruby, there were two good solutions to manage multiple versions of Ruby - [RVM](https://rvm.io/) and [rbenv](http://rbenv.org/). Both allow you to install a new Ruby version with a single command and then simply switch between them.

Recently, I've started working with [Python](http://www.python.org) and tried to find a similar solution to manage multiple versions which is a necessity considering that there are two major, incompatible versions - 2.x and 3.x.

Many blog posts and tutorials I found, suggested using the popular [virtualenv](http://www.virtualenv.org/en/latest/) tool to make a new isolated environment for each Python version. Unfortunately, I didn't find an explicit mention of the 'best' or easiest way to do this.

This blog post summarizes my current setup which has worked well for me in the past.

## Preliminary

The tutorial assumes that you have enough knowledge of OS X to compile Python on your machine. I personally use [Homebrew](http://brew.sh) to install dependencies.

## Setting up the Pythons

All Python versions will be installed in _/opt/pythons_. Let's initialize the directory with:<div class="codehilite"><pre><div class="nn">~% sudo mkdir -p /opt/pythons</div></pre></div>


<div class="codehilite"><pre><div class="nn">~% curl http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tgz | tar xvzf -<br/>~% cd Python-2.7.5<br/>~% ./configure --prefix=/opt/pythons/2.7.5<br/>~% make<br/>~% sudo mkdir -p /opt/pythons<br/>~% sudo make install</div></pre></div>


## Installing Virtualenv and Virtualenvwrapper

## Setting up the Virtualenvs
