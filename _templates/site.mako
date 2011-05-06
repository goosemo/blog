<%inherit file="base.mako" />
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" 
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
        ${self.head()}
    </head>

    <body>
    <div class="content_centered">
        ${self.header()}
        <div id="main_content">
            <div id="prose_block">
                ${next.body()}
            </div><!-- End Prose Block -->
        </div><!-- End Main Block -->
        <div id="column_right">
            ${self.sidebar()}
        </div>
        <div id="footer">
            ${self.footer()}
        </div> <!-- End Footer -->
    </div> <!-- End Content -->
    </body>
</html>

<%def name="head()">
    <%include file="head.mako" />
</%def>

<%def name="header()">
    <%include file="header.mako" />
</%def>

<%def name="sidebar()">
    <%include file="sidebar.mako" />
</%def>

<%def name="footer()">
    <hr/>
    <%include file="footer.mako" />
</%def>
