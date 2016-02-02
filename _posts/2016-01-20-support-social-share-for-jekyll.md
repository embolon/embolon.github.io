---
layout: post
title:  "Support Social Share for Jekyll"
date:   2016-01-20 21:33:10 -0600
categories: blog-setup
tags: 
- jekyll
- github
- share
comments: true
disqus_identifier: 000000000102
language: english
---

One of the most important method to get a post more attention is to share it to the social media. Such a feature is must for my blog site too. Today I will briefly introduce how to add this feature to the jekyll supported github page.

## Step 0 Should I use a shortUrl?

It is very common to use shortUrl in Twitter posts due to its previous 140 character limiations, but the fact is, most of these limitations already become history thanks to technology improvements. For example, Twitter and Weibo both now internally support their own shortUrl features, so a third part shortUrl service is no longer a necessity. So I decided to just use the origin post url for share purposes.

## Step 1 Create a share.html template

Thanks to Wenli Zhang's [post](http://zhangwenli.com/blog/2014/08/03/make-your-own-social-sharing-bar-with-jekyll/ "Make Your Own Social Sharing Bar with Jekyll"), it is a very good guidence to setup the sharing feature. I have comment out everything related to the shortUrl. To add a new share site, check out the code below.


     <a class="social-share-element" id="social-weibo" href="http://v.t.sina.com.cn/share/share.php?title=来看看+%40[YOUR_WEIBO_USERNAME]+的博文吧：{{ page.title }}&url={{ site.url }}{{ page.url }}" target="_blank" title="Share this post on Sina Weibo">Weibo</a>


Different SNS sites have very similar sharing templates. For more information, please check my site's [source code](http://github.com/embolon/embolon.github.io) (/_includes/share.html). At last, don't forget to include share.html into _layouts/post.html.

## Step 2 Make social share buttons using good looking icons

TBD. Will update soon.


* Find good looking icons.
* Learn to modify css styles.

## Step 3 Alternative Services

I have later found that services such as [AddThis](http://www.addthis.com) and [JiaThis](http://www.jiathis.com) can provide a much easier solution to social network sharings. I used AddThis for my English posts and JiaThis for my Chinese posts. It is very straightforward to implement these two. Go to their websites. Use their GUI tool to design your share buttons. Then copy and paste the generated code to _layouts/post.html as suggested.
