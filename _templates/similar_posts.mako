
<h3>Similar posts:</h3>
<ul>
% for similar in post.similar_posts:
    <li><a href="${similar.link}>${similar.name}</a></li>
% endfor
</ul>
