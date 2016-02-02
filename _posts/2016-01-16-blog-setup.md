---
layout: post
title:  "Blog Setup"
date:   2016-01-16 11:04:38 -0600
tags: 
- jekyll
- github
categories: blog-setup
comments: false
disqus_identifier: 000000000001
language: english
---

### Step 0 Have a Github account

If you write programs, chances are, you already have an account. But no worries if you do not, it is super easy to setup a github account and you will find it very useful in the future. 

---

### Step 1 Create a Github Page repository

Assume you already know how to create a new repository on Github. The name of a Github Blog repository is usually like USERNAME.github.io, where USERNAME is user customizable. We can add a index.html into the repository for testing. Note that a blog page should use the normal master branch, but a project page should use a special gh-pages branch instead.

    git clone https://github.com/USERNAME/USERNAME.github.io
    cd USERNAME.github.io
    echo "Hello World!" > index.html
    git add index.html
    git commit -a -m "Initial commit"
    git push -u origin master

Once the repository is created, we can visit http://USERNAME.github.io to check out the new blog site. If you see a "Hello World" appear on the left cornor of the blog site, you are done!

---

### Step 2 Setup jekyll

This step will enable us to use jekyll to locally run and test our blog before uploading. I would recommend using either a Ubuntu or Mac machine rather than Windows, since I run into various issues trying to get jekyll work on my cygwin terminal. Here, I used a Ubuntu 12.04 as an example.

#### Installing jekyll

Since the ubuntu default ruby and jekyll packages are out-dated, I used the rvm -- Ruby Version Manager to install ruby. And using rvm can avoid issues such as requiring root privilege when installing gem tools.

    # install RVM
    gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
    curl -L get.rvm.io | bash -s stable --auto

    # install ruby
    source ~/.rvm/scripts/rvm  # this will enable rvm and its enviroment settings
    rvm install ruby-VERSION   # we can choose VERSION, if left none then will install the default version

    # install jekyll
    gem install jekyll

My current versions:

    ruby -v
    ruby 2.2.1p85
    jekyll -v
    jekyll 3.0.1

Now we have successfully installed jekyll!

---

### Step 3 Edit your blog site locally

Now that we have blog repository set up and jekyll installed, we can start to edit our blog site locally. Assuming our local repo at USERNAME.github.io, we can add the jekyll base theme to it. 

    cd USERNAME.github.io
    git rm index.html  # remove the previous index.html page
    jekyll new .       # initiate jekyll theme
    jekyll serve       # start jekyll serve

Now we can visit localhost:4000 to check our local blog site. It should be the standard jekyll theme. We can edit _config.yml to change the blog title, email, twitter and github account information, etc. There are a lot of things we can change to make our blog better. Just google around to find new jekyll themes and follow their instructions.

Once we have picked the ideal jekyll theme, it is time to bring the blog site online. One of the good thing I like Github page is that we can upload our blog site by simply pushing local repo to the remote.

    git add ALL_FILES
    git commit -a -m "SOME COMMENT"
    git push -u origin master

It's Alive!

---

### Step 4 Start posting 

Now we are good to post!
