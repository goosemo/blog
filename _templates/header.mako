<div id="content_centered">
    <div id="header">
        <h1><a href="${bf.util.site_path_helper()}">${bf.config.blog.name}</a></h1>
        <h2>${bf.config.blog.description}</h2>
        <ul id="header_menu">
        % for menu_item, menu_url in bf.config.menu.items():
            <li><a href="${menu_url}">${menu_item}</a></li>
        % endfor
        </ul>
    </div>
    <hr/>
