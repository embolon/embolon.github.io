---
layout: post
title:  "Support favicon and footer modification"
date:   2016-04-08 04:18:27 
categories: blog-setup
tags: 
- jekyll
- github
- favicon
- license
- social-icon
comments: true
identifier: 000000000111
language: english
---

After a few days of posting random stuff, I decided to add some new features to the Blog: favicon and a better looking footer.

## Favicon

This little thing lives in your browser tag and favorite folders. It usually is a 16x16 size png or ico image. After googling around, I found a pretty good [website](http://www.realfavicongenerator.net "Real Favicon Generator.net"), which has detailed instructions and codes to show you how to add the favicon to your site. One thing to keep in mind is that there is a debate on whether you should put favicon.ico (together with some other files)in the site root directory. It has benefits and drawbacks.

To keep things short. Prepare an image with good quality to serve as your original icon. Feed it to a favicon gen website and get a set of icons. Upload this set of icons to blog site and modify the html head accordingly.

## Footer modification

I think the three column footer is really not necessary for my blog. So I modified it to look like this [Blog](http://themicronaut.github.io/). To add the license information is pretty straight forward, just check the [Creative Commons License](http://creativecommons.org/licenses/by-nc-sa/4.0) for detailed instructions. The difficult part is to add social icons. In order to do so, we will have to touch CSS which is a whole new experience for me. 

### Step 0

Find and download a set of the favorate icon images. You can choose the icon color to match your footer font color. Note: do not forget to credit the icon authors.

### Step 1

We will have to add a new social-icon class to the css file (_sass/_layout.scss) as below.

{% highlight scss %}    
.social-icons {
    margin: 1em;
    a {
      text-decoration: none; /* remove underline in social icons */
      padding: 4px 4px;
      &:hover {
        color: &grey-color;
      }
    }
}
{% endhighlight %}

I have added the text-decoration: none; to get ride of the annoying underline on the icons, but there might be a better way to do so. 

### Step 2

To add a icon, we can it like below (_includes/footer.html):

{% highlight html %}
<div class="social-icons">
{ % if site.owner.github % }<a href="https://github.com/{ { site.owner.github } }" title="{ { site.owner.name } } on Github" target="_black"><span class="icon32 icon--github">{ % include icon-github.svg % }</span></a>{ % endif % }
</div>
{% endhighlight %}

Now you can add as many social icons as you like!
