<%inherit file="_templates/site.mako" />
<div class="blog_post">
  <span class="post_prose">
    
    <h1>A simple list of everything I have going on at gihub</h1>
    
    <table border="0" cellspacing="0" cellpadding="0">
    <thead>
    <tr>
       <th class="span-6">Project</th>
       <th class="span-8">Description</th>
       <th class="span-10">Watchers</th>
       <th class="span-12">Forks</th>
       <th class="span-14">Issues</th>
    </tr>
    </thead>
    <tbody>

    % for project in bf.config.controllers.github.full_repo_list:
    <tr>
        <td><a href="${project.url}" title="${project.name}">
        ${project.name}</a></td>
        <td>${project.description}</td>
        <td>${project.watchers}</td>
        <td>${project.forks}</td>
        <td>${project.open_issues}</td>
    </tr>
    % endfor
    </tbody>
    </table>
  </span>
</div>
