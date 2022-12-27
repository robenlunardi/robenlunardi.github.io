---
title: "Talks"
layout: gridlay
sitemap: false
permalink: /talks/
---

# Talks

{% if site.data.conference_talks %}
## Conference presentations
<div class="rowl1" style="padding-top: 10px;">

{% for talk in site.data.conference_talks %}
{{ forloop.index }}. <strong>{{ talk.title }}</strong> <br/> <i>{{ talk.authors }}</i>, {{ talk.conf }} ({{ talk.year }}).
{% endfor %}
</div>
{% endif %}

{% if site.data.invited_talks %}
## Talks and webinars
<div class="rowl1" style="padding-top: 10px;">

{% for talk in site.data.invited_talks %}
{{ forloop.index }}. {% if talk.link %}<a href="{{ talk.link }}" target="_blank">{% endif %}<strong>{{ talk.title }}</strong>{% if talk.link %}</a>{% endif %} ({{ talk.year }}){% if talk.subtitle %}<br>{{ talk.subtitle }}{% endif %}.
{% endfor %}
</div>
{% endif %}

{% if site.data.chairing %}
## Chairing sessions
<div class="rowl1" style="padding-top: 10px;">

{% for session in site.data.chairing %}
{{ forloop.index }}. {% if session.link %}<a href="{{ session.link }}" target="_blank">{% endif %}<strong>{{ session.title }}</strong>{% if session.link %}</a>{% endif %} ({{ session.year }}){% if session.subtitle %} {{ session.subtitle }}{% endif %}<br/>{{ session.conf }}.
{% endfor %}
</div>
{% endif %}
