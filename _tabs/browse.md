---
layout: page
icon: fas fa-align-justify
order: 1
---


<h2 data-toc-skip>Browse the Full Index of Posts</h2>

Add some details here.


<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>

{{ post.excerpt }}




