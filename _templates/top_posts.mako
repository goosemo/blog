% if bf.config.google.analytics.top_posts_enabled:
<div class="sidebar_item">
<h3>Top Posts</h3>
<ul>
% for link, name, num_hits in bf.config.google.analytics.top_posts:
    <li><a href="${link}"
    title="${name}">${name}</a>&nbsp;
    % if bf.config.google.analytics.show_count:
    (${num_hits})
    % endif
    </li>
    <br/>
% endfor
</ul>
</div>
<br />
% endif
