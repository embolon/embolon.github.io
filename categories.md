---
layout: page
title: Categories
permalink: /categories/
---

Click on a category to see relevent posts.

<ul class="categories">
{% for category in site.categories %}
  {% assign c = category | first %}
  {% assign posts = category | last %}
  <li><a href="/categories/#{{c | downcase | replace:" ","-" }}">{{ c | downcase }}</a> has {{ posts | size }} posts</li>
{% endfor %}
</ul>

---

{% for category in site.categories %}
  {% assign c = category | first %}
  {% assign posts = category | last %}

<h4><a name="{{c | downcase | replace:" ","-" }}"></a><a class="internal" href="/categories/#{{c | downcase | replace:" ","-" }}">{{ c | downcase }}</a></h4>
<ul>
{% for post in posts %}
  {% if post.categories contains c %}
  <li>
    <a href="{{ post.url }}">{{ post.title }}</a>
    <span class="date">{{ post.date | date: "%B %-d, %Y"  }}</span>
  </li>
  {% endif %}
{% endfor %}
</ul>

---

{% endfor %}
