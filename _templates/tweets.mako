% if bf.config.tweets.enabled:
<div class="sidebar_item">
    <h3>Twitter&nbsp;
    <a href="http://www.twitter.com/${bf.config.tweets.username}">
        <img src="http://twitter-badges.s3.amazonaws.com/t_mini-b.png" alt="Follow
        ${bf.config.tweets.username} on Twitter"/>
    </a>
    </h3>
    <script type="text/javascript" charset="utf-8">
    <!--
    getTwitters('tweet', { 
        id: '${bf.config.tweets.username}', 
        count: ${bf.config.tweets.count}, 
        enableLinks: ${bf.config.tweets.enable_links}, 
        ignoreReplies: ${bf.config.tweets.ignore_replies}, 
        clearContents: true,
        template: '${bf.config.tweets.template}',
    });
    -->
    </script>

    <div id="tweet">
    </div>
</div>
<br />
% endif

