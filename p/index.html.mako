<%inherit file="_templates/site.mako" />
<%
import simplejson
import urllib

url = "http://morgangoose.com/p/presentations.json"
presentations = simplejson.load(urllib.urlopen(url))

%>
<div class="blog_post">
  <span class="post_prose">
    
    <h1>Presentations I've made and given</h1>
    <br/> 
    <table border="0" cellspacing="0" cellpadding="0">
    <thead>
    <tr>
       <th class="span-5">Presentation</th>
       <th class="span-8">Description</th>
       <th class="span-1"></th>
       <th class="span-1"></th>
       <th class="span-1"></th>
    </tr>
    </thead>
    <tbody>

    % for name, description in presentations.items():
    <tr>
        <td><a href="/p/${name}" title="${name}">${name}</a></td>
        <td>${description}</td>
        <td><a class="pdf" href="/p/${name}/${name}.pdf"> </a></td> 
        <td><a class="source" href="/p/${name}/${name}.rst"> </a></td> 
        <td><a class="package" href="/p/${name}.tgz"> </a></td> 
    </tr>
    % endfor
    </tbody>
    </table>
  </span>
</div>
