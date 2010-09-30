<%
start = bf.config.blog.posts_per_page
end = start + bf.config.blog.latest_post_count
%>
<div class="sidebar_item">
<h3>Latest ${end-start} Posts</h3>
<ul class="sidebar_menu">
% for post in bf.config.blog.posts[start:end]:
    <li>
        <div class="item">
            <a href="${post.path}">${post.title}</a>
        </div>
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
<div class="item">
    <li> 
        <a href="${category.path}">${category}</a> (<a href="${category.path}/feed">rss</a>) (${num_posts})
    </li>
    <br/>
</div>
% endfor
</ul>
</div>
<br />

% if bf.config.tweets.enabled:
<div class="sidebar_item">
    <h3>Twitter&nbsp;
    <a href="http://www.twitter.com/${bf.config.tweets.username}">
    <img src="http://twitter-badges.s3.amazonaws.com/t_mini-b.png" alt="Follow
    ${bf.config.tweets.username} on Twitter"/></a>
    </h3>
    <script src="http://twitterjs.googlecode.com/svn/trunk/src/twitter.min.js" type="text/javascript">
    </script>
    <script type="text/javascript" charset="utf-8">
    getTwitters('tweet', { 
        id: '${bf.config.tweets.username}', 
        count: ${bf.config.tweets.count}, 
        enableLinks: ${bf.config.tweets.enable_links}, 
        ignoreReplies: ${bf.config.tweets.ignore_replies}, 
        clearContents: true,
        template: '${bf.config.tweets.template}',
    });
    </script>
    <div id="tweet">
    </div>
</div>
<br />
% endif

<div class="sidebar_item">
<h3>Links</h3>
<ul>
% for name, desc, url in bf.config.links:
    <li><a href="${url}" title="${name}">${name}</a> - ${desc}</li>
    <br/>
% endfor 
</ul>
</div>
<br />

<div class="sidebar_item">
<h3>Archives</h3>
<ul>
% for link, name, num_posts in bf.config.blog.archive_links:                
    <li><a href="${bf.util.site_path_helper(bf.config.blog.path,link)}/1"
    title="${name}">${name}</a>&nbsp;(${num_posts})</li>
    <br/>
% endfor
</ul>
</div>
<br />

% if bf.config.github.enabled:
<%include file="github.mako" />
% endif
