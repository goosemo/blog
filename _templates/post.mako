<%page args="post"/>
<div class="blog_post">
<% 
    post_anchor = "-".join(post.title.split(" "))

    category_links = []
    for category in post.categories:
        if post.draft:
            #For drafts, we do not write to the category dirs, so just write the categories as text
            category_links.append(category.name)
        else:
           category_links.append("<a href='%s'>%s</a>" % (category.path, category.name))

    if bf.config.blog.disqus.enabled:
        comments_tag = ' | <a href="${post.permalink}#disqus_thread">View Comments</a>'
%>
  <a name="${post_anchor}" />
  <h1 class="blog_post_title"><a href="${post.permapath()}" rel="bookmark" title="Permanent Link to ${post.title}">${post.title}</a></h1>
  <h3>${post.date.strftime("%B %d, %Y at %I:%M %p")} | categories: ${", ".join(category_links)} ${comments_tag}</h3>
  <br />
  <div class="post_prose">
    ${self.post_prose(post)}
  </div>
</div>

<%def name="post_prose(post)">
  ${post.content}
</%def>
<br />

