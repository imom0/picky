{% extends "base.tpl" %}
{% block title %}Index{% endblock %}
{% block head %}
    {{ super() }}
    <style type="text/css">
        .important { color: #336699; }
    </style>
{% endblock %}
{% block content %}
    <h1>Index</h1>
    <p class="important">{{values.test}}
      Welcome on my awesome homepage.
    </p>
{% endblock %}
