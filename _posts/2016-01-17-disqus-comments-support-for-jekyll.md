---
layout: post
title:  "Disqus comments support for jekyll"
date:   2016-01-17 18:16:57 -0600
tags:
- disqus
- comments
- jekyll
- github
categories: blog-setup
comments: true
disqus_identifier: 000000000002
---

It is really nice to have some comment support for this blog, so I have googled around and added this Disqus support. Here, I documented the steps.

## Step 0 Register the blog site on Disqus

Disqus is a pretty popular discussion and comment system online. It is pretty simple to set up for jekyll. We will first sign up an account on Disqus, and then register my blog site. The site registration requires a shortname, which does not seem to be connected with the actually site url, but I am not sure. After the registration, Disqus will lead us to a page with Universal Code, that will be used to insert in the "comment" session of our site.

## Step 1 Edit the blog site

We will modify _layouts/post.html to include a "comment" session and create a _includes/disqus.html that holds the actual "comment" session Universal Code.


    _layouts/post.html
    <article>
      ...
      # header
      # content
      <div class="comments">
        { % include disqus.html % } # NOTE, no space between { and %, % and }
      </div>  
    </article>


    _includes/disqus.html
    { % if page.comments % }
    <div class="comments">
      <div id="disqus_thread"></div>
        <script>
        /**
         *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
         *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables
         */
    
        var disqus_config = function () {
            this.page.url = '{ { site.url } }{ { page.url } }';  // Replace PAGE_URL with your page's canonical URL variable
            { % if page.disqus_identifier % }
            this.page.identifier = '{ { page.disqus_identifier } }'; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
            { % endif % }
        };
        (function() {  // DON'T EDIT BELOW THIS LINE
            var d = document, s = d.createElement('script');
        
            s.src = '//SITE_SHORTNAME.disqus.com/embed.js'; // put your site-shortname that is registered on Disqus here
        
            s.setAttribute('data-timestamp', +new Date());
            (d.head || d.body).appendChild(s);
        })();
      </script>
      <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript" rel="nofollow">comments powered by Disqus.</a></noscript>
    </div>
    { % endif % }


The liquid template will read page front matter to parse into variables like page.url, page.layouts, page.comments. A typical way to use the liquid template is like this: { % if page.comments % } { % endif % }. This works like the C macro #ifdef and #endif. To enable such page.comments switch, we will further include the "comments" into the post front matter.


    _posts/2016-01-17-This-is-a-test-post.md
    ---
    layout: post
    title:  "This is a test post"
    date:   2016-01-17 18:16:57 -0600
    categories: default
    comments: true
    disqus_identifier: 000000000001
    ---

    ## Testing


## Optional Disqus Identifier
    
Since a page url can change when we decided to change the title of the post, a Disqus Identifier is better not set to the page url. People suggested different solutions to this situation including generating random numbers to assign to the new post or maintain a counter of the number of the posts. For the former one, as long as there are no random number conflicks, that is, a new generated number does not equal to any previous post, it should be fine. This is an easy soluation but not very reliable. The latter one can avoid possible identifier conflicks but will require the counter to be stored, which will add a little complexity.

---

Thanks to Ankur Gupta's [post](http://www.perfectlyrandom.org/2014/06/29/adding-disqus-to-your-jekyll-powered-github-pages/ "Adding Disqus to your Jekyll") on Perfectly Random. I found it very helpful when I set up the Disqus comments on my blog site.
