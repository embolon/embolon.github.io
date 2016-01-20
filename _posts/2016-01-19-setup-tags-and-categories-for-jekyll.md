---
layout: post
title:  "Setup tags and categories for Jekyll"
date:   2016-01-19 21:46:50 -0600
categories: blog-setup
tags: 
- jekyll
- github
- tags
- categories
comments: true
disqus_identifier: 000000000101
---

Previously we setup the Disqus comment feature to the blog site, this time I am going to add tags and categories pages. Although there is no limitation on how many categories a post can have, I would consider category as a directory that a post belongs to only one category. As for tags, it is perfectly OK for one post to have multiple tags.

## Step 1 Add tags in a post
Adding tags in a new post is easy. Just includes the tags in the front matter like this.


    ---
    ...
    tags:
    - jekyll
    - github
    - tags
    - categories
    ...
    ---
 

Since space might bring issues in the future, if one the tag contains space, it is better to switch space into dash. For example, a tag "github page" should be "github-page".

---

## Step 2 Show the tags and categories on a post

It would be really nice to show categories and tags parallel to time right under the title of the post. So after trying a bit, I came up with this code to insert after the "time" and "author" session in the header part. This code can show both categories and tags like this: "Jan 19, 2016 \| blog-setup \| github jekyll tags categories", where the category and tags can be clicked to go to their links.

    
    { % if page.categories % } | <a href='/categories/#{ {page.categories} }'>{ {page.categories} }</a> { % endif % }{ % if page.tags % } | { % for tag in page.tags % } <a href='/tags/#{ {tag} }'>{ {tag} }</a> { % endfor % } { % endif % }


Now, the tags and categories will show up on a new post. But we still need a tags and a categories page to show all the posts like a catalog.

## Step 3 Create tags and categories pages

Lazy me, here I just copied other people's tags.md to my own repo and it worked. And I copied this tags.md to categories.md and changed all "tags" into "categories" to make categories work. Most importantly, Github Page does not support many plugins, so we can only provide this tags and categories page in a static way. If a solution propose using some customized tag plugin, changes are, it might not work on Github Page. Secondly, since previously in the post.html we set the tags and categories link to be '/tags/#{ {tag}}' and '/categories/#{ {categories}}', we must add "permalink: /tags/" or "permalink: /categories/" to the tags.md and categories.md to make the two pages like a directory.

For detailed codes, you can check Joe Kampschmidt's [post](http://www.jokecamp.com/blog/listing-jekyll-posts-by-tag/ How to list your jekyll posts by tags). It is very helpful when I setup the tags and categories for my blog site.
