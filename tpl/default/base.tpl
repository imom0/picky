<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html lang="en">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    {% block head %}
<!--    <link rel="stylesheet" href="style.css" /> -->
    <title>{% block title %}{% endblock %} - iMom0.'s Public Secret.</title>
    {% endblock %}
</head>
<body>
    <div id="content">{% block content %}{% endblock %}</div>
    <div id="footer">
        {% block footer %}
        &copy; Copyright 2008 by <a href="http://imimom0.appspot.com/">iMom0.</a>.
        {% endblock %}
    </div>
</body>
