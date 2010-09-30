<%inherit file="_templates/site.mako" />
<div class="blog_post">
  <span class="post_prose">
    
    <h1>Simple list of everything I have going on at gihub</h1>
    <br/> 
    <table border="0" cellspacing="0" cellpadding="0">
    <thead>
    <tr>
       <th class="span-5">Project</th>
       <th class="span-8">Description</th>
       <th class="span-1">Watchers</th>
       <th class="span-1">Forks</th>
       <th class="span-1">Issues</th>
    </tr>
    </thead>
    <tbody>

    % for project in bf.config.controllers.github.full_repo_list:
    <tr>
        <td><a href="${project.url}" title="${project.name}">
        ${project.name}</a></td>
        <td>${project.description}</td>
        <td>${project.watchers - 1}</td> 
        <td>${project.forks}</td>
        <td>${project.open_issues}</td>
    </tr>
    % endfor
    </tbody>
    </table>
  </span>
</div>
