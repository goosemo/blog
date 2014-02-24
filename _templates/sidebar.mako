<%
start = bf.config.blog.posts_per_page
end = start + bf.config.blog.latest_post_count
%>
<div class="sidebar_item">
<h3>Latest ${end-start} Posts</h3>
<ul class="sidebar_menu">
% for post in list(bf.config.blog.posts[start:end]):
    <li class="item">
        <a href="${post.path}">${post.title}</a>
    </li>
% endfor
</ul>
<h4 class="align_right">(sans the latest ${start})</h4>
</div>
<br />

<div class="sidebar_item">
<h3>Categories</h3>
<ul>
% for category, num_posts in bf.config.blog.all_categories:
    <li class="item"> 
        <a href="${category.path}">${category}</a> (<a href="${category.path}/feed">rss</a>) (${num_posts})
    </li>
% endfor
</ul>
</div>
<br />

<div class="sidebar_item">
<h3>Links</h3>
<ul>
% for name, desc, url in bf.config.links:
    <li class="item"><a href="${url}" title="${name}">${name}</a> - ${desc}</li>
% endfor 
</ul>
</div>
<br />

% if hasattr(bf.config, "google"):
<%include file="top_posts.mako" />
% endif

<div class="sidebar_item">
<h3>Archives</h3>
<ul>
% for link, name, num_posts in bf.config.blog.archive_links:
    <li class="item"><a href="${bf.util.site_path_helper(bf.config.blog.path,link)}/1"
    title="${name}">${name}</a>&nbsp;(${num_posts})</li>
% endfor
</ul>
</div>
<br />


% if hasattr(bf.config, "github"):
<%include file="github.mako" />
% endif 

% if hasattr(bf.config, "stackoverflow"):
<%include file="stackoverflow.mako" />
% endif 

% if hasattr(bf.config, "tweets"):
<%include file="tweets.mako" />
% endif

% if hasattr(bf.config, "google"):
<%include file="adsense.mako" />
% endif

