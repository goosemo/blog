<div class="float_left">
<p>
    <a href="http://validator.w3.org/check?uri=referer"><img
    src="http://www.w3.org/Icons/valid-xhtml10"
    alt="Valid XHTML 1.0 Strict" height="31" width="88" /></a>
</p>
</div>

<div class="float_right">
<p id="credits">
Powered by <a href="http://www.blogofile.com">Blogofile</a>.<br />
<br />

% if bf.config.feedburner.enabled:
RSS feeds for <a href="${bf.config.feedburner.url}">Entries</a>
% else:
RSS feeds for <a href="${bf.util.site_path_helper(bf.config.blog.path,'feed')}">Entries</a>
% endif

% if bf.config.blog.disqus.enabled:
 and <a href="http://${bf.config.blog.disqus.name}.disqus.com/latest.rss">Comments</a>.
% endif
<br />
</p>
% if bf.config.blog.disqus.enabled:
<script type="text/javascript">
//<![CDATA[
(function() {
		var links = document.getElementsByTagName('a');
		var query = '?';
		for(var i = 0; i < links.length; i++) {
			if(links[i].href.indexOf('#disqus_thread') >= 0) {
				query += 'url' + i + '=' + encodeURIComponent(links[i].href) + '&';
			}
		}
		document.write('<script charset="utf-8" type="text/javascript" src="http://disqus.com/forums/${bf.config.blog.disqus.name}/get_num_replies.js' + query + '"></' + 'script>');
	})();
//]]>
</script>
% endif

% if bf.config.google.analytics.enabled:
    <%include file="google_analytics.mako"/>
% endif
</div>
</div>
