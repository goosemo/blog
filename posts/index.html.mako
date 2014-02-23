<% 
    self.page_title="Posts" 
%>
<%inherit file="_templates/site.mako" />

<div class="blog_post">
  <span class="post_prose">
    <h1>Posts I've written</h1>
    <br/> 
    <table border="0" cellspacing="0" cellpadding="0">
    <thead>
    <tr>
       <th class="span-8">Title</th>
       <th class="span-2">Date</th>
       <th class="span-6">Categories</th>
       <th class="span-1">Hits</th>
    </tr>
    </thead>
    <tbody>
    % for post in bf.config.blog.posts:
    <tr>
        <td><a href="${post.path}" title="${post.title}">${post.title}</a></td>
        <td>${post.date.strftime("%m/%d/%Y")}</td>
        <td>${post.categories}</td>
        % if False:
        <td>${post.hit_count}</td>
        % else:
        <td></td>
        % endif
    </tr>
    % endfor
    </tbody>
    </table>
  </span>
</div>
