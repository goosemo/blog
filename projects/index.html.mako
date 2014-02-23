<% 
    self.page_title="Projects" 
    post.title="Projects" 
%>
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
<%
    github = bf.config.controllers.github
%>
    % for repo in github.full_repo_list:
    <tr>
        <td><a href="${repo.html_url}" title="${repo.name}">
        ${repo.name}</a></td>
        <td>${repo.description}</td>
        
        % if github.link_watchers:
        <td><a href="${repo.html_url}/watchers">${repo.watchers - 1}</a></td>
        % else:
        <td>${repo.watchers - 1}</td>
        % endif
        
        % if github.link_forks:
        <td><a href="${repo.html_url}/network">${repo.forks}</a></td>
        % else:
        <td>${repo.forks}</td>
        % endif
        
        % if github.link_issues:
        <td><a href="${repo.html_url}/issues">${repo.open_issues}</a></td>
        % else:
        <td>${repo.open_issues}</td>
        % endif
    </tr>
    % endfor
    </tbody>
    </table>
  </span>
</div>
