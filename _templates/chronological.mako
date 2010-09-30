<%inherit file="site.mako" />
% for post in posts:
  <%include file="post.mako" args="post=post" />
% if bf.config.blog.disqus.enabled:
    <div class="after_post">
       <div id="buttons" class="float_right">
            <script type="text/javascript">
                reddit_url = "${post.permalink}";
                reddit_title = "${post.title}";
                reddit_newwindow = "1";
                reddit_styled = "off";
            </script>
            <script type="text/javascript" 
            src="http://reddit.com/static/button/button1.js">
            </script>
        </div>
        <div id="comments" class="float_left">
            <a href="${post.permalink}#disqus_thread">Read and Post Comments</a>
        </div>
     </div>
    <br/>
    <br/>
% endif
  <hr class="interblog" />
  <br/>
  <br/>
% endfor
% if prev_link:
 <a href="${prev_link}">« Previous Page</a>
% endif
% if prev_link and next_link:
  --  
% endif
% if next_link:
 <a href="${next_link}">Next Page »</a>
% endif
