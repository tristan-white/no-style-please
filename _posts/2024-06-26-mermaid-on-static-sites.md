---
layout: post
title: Mermaid on Static Sites
---


<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
</script>

<pre class="mermaid">

graph TD
    start["I want to add mermaid<br>to my website"]
    time[How much time am<br>I willing to spend<br>to set it up?]
    easy[Copy/paste a few lines to lines<br>to your post which will import<br>mermaid and create an element<br> to contain your mermaid text.]
    after_medium[Can I just use<br>backticks to create<br>my mermaid graph?]
    style after_medium stroke-dasharray: 5
    medium[Use mermaid.live to create<br>an SVG of your graph,<br>then upload to your post<br>like a normal image.]
    after_easy[But I don't want to<br>have to paste html<br>in my posts.]
    style after_easy stroke-dasharray: 5
    hard[1. Create a github workflow<br>2. Import jekyll-mermaid plugin]
    final[Give this article a fa:fa-hands-clapping <br>]

    start --> time

    time -- 1 min --> easy
    time -- 3 min --> medium
    time -- 15-30 min<br>(skill dependent) --> hard

    easy -- hmm --> after_easy --> time
    easy -- nice! --> final

    medium -- hmm --> after_medium --> time
    medium -- nice! --> final

    hard -- nice! --> finalgraph
</pre>

<!--

[^1]: [GitHub Pages allowed plugins](https://pages.github.com/versions/)


https://github.com/jeffreytse/jekyll-deploy-action

How to use jekyll spaceship with jekyll pages: https://medium.com/@jeffreytse.mail/if-you-dont-mind-to-use-a-plugin-the-below-can-help-you-do-it-easier-in-markdown-95114b27387c
-->