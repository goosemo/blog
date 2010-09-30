<%inherit file="site.mako" />
% for post in posts:
  <%include file="post.mako" args="post=post" />
% if bf.config.blog.disqus.enabled:
    <div class="after_post">
        <div id="comments" class="float_left">
            <a href="${post.permalink}#disqus_thread">Read and Post Comments</a>
        </div>
        <div id="buttons" class="float_right">
            <a href="http://reddit.com/submit" onclick="window.location =
            'http://reddit.com/submit?url=' + encodeURIComponent(window.location);
            return false"> <img src="http://reddit.com/static/spreddit7.gif" 
            alt="submit to reddit" border="0" /> </a>
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
