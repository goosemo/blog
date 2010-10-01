<div class="sidebar_item">
<h3>Top Posts</h3>
<ul>
% for link, name, num_hits in bf.config.google_analytics.top_posts:
    <li><a href="${link}"
    title="${name}">${name}</a>&nbsp;(${num_hits})</li>
    <br/>
% endfor
</ul>
</div>
<br />

