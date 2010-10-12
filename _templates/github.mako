% if bf.config.github.enabled:
<div class="sidebar_item">
<h3>Github Projects</h3>
<ul>
% for project in bf.config.controllers.github.repo_list:
    <li><a href="${project.url}" title="${project.name}">
    ${project.name}</a>&nbsp;${project.description}</li>
% endfor
</ul>
</div>
<br />
% endif
