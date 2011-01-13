% if post and hasattr(post, "title"):
<title>${post.title}</title>
% else:
<title>${bf.config.blog.name}</title>
% endif
<link rel="alternate" type="application/rss+xml" title="RSS 2.0" href="${bf.util.site_path_helper(bf.config.blog.path,'/feed')}" />
<link rel="alternate" type="application/atom+xml" title="Atom 1.0"
href="${bf.util.site_path_helper(bf.config.blog.path,'/feed/atom')}" />
<link rel='stylesheet' href='${bf.config.filters.syntax_highlight.css_dir}/pygments_${bf.config.filters.syntax_highlight.style}.css' type='text/css' />
<link rel="stylesheet" href="/css/global.css" type="text/css" charset="utf-8" />
<link rel="stylesheet" href="/css/table.css" type="text/css" charset="utf-8" />

