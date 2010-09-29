<div class="sidebar_item">
<h3>Latest Posts</h3>
<ul class="sidebar_menu">
% for post in bf.config.blog.posts[:bf.config.blog.latest_post_count]:
    <li>
        <div class="item">
            <a href="${post.path}">${post.title}</a>
        </div>
    </li>
% endfor
</ul>
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
</div>
% endfor
</ul>
</div>
<br />

<div class="sidebar_item">
    <h3>Twitter</h3>
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

<div class="sidebar_item">
<h3>Links</h3>
</div>
<br />
