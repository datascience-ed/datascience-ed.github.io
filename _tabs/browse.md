---
layout: page
icon: fas fa-align-justify
order: 1
---


<h2 data-toc-skip>Browse the Full Index</h2>

You can Browse the full list of posts below.

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>

{{ post.excerpt }}




