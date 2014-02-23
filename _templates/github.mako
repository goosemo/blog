% if bf.config.github.enabled:
<div class="sidebar_item">
<h3>Github Projects</h3>
<ul>
% for repo in bf.config.controllers.github.repo_list:
    <li><a href="${repo.html_url}" title="${repo.name}">
    ${repo.name}</a>&nbsp;${repo.description}</li>
% endfor
</ul>
</div>
<br />
% endif
