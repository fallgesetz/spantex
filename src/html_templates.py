"""
HTML templates in heredoc form.
"""
from string import Template

basic = Template("""
<html>
    <head>
        <title>$title</title>
    </head>
    <body>
    $body
    </body>
</html>
""")
