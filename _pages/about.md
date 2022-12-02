---
title: "About"
layout: gridlay
sitemap: false
permalink: /about/
---

## About 


{% for member in site.data.pi %}

<div class="row">
  <img src="{{ site.url }}{{ site.baseurl }}/images/team/{{ member.photo-large }}" class="img-responsive avatar-about" />
  <h3>{{ member.name }}</h3>
  <i style="font-size:20px">{{ member.info }}</i><br>

  {% if member.website %}<a href="{{ member.website }}" target="_blank"><i class="fa fa-home fa-3x"></i></a> {% endif %}
  {% if member.email %}<a href="mailto:{{ member.email }}" target="_blank"><i class="fa fa-envelope-square fa-3x"></i></a> {% endif %}
  {% if member.cv %} <a href="{{ member.cv }}" target="_blank"><i class="ai ai-cv-square ai-3x"></i></a> {% endif %}
  {% if member.orcid %} <a href="{{ member.orcid }}" target="_blank"><i class="ai ai-orcid-square ai-3x"></i></a> {% endif %}
  {% if member.linkedin %} <a href="{{ member.linkedin }}" target="_blank"><i class="fa fa-linkedin-square fa-3x"></i></a> {% endif %}
  {% if member.scholar %} <a href="{{ member.scholar }}" target="_blank"><i class="ai ai-google-scholar-square ai-3x"></i></a> {% endif %}
  {% if member.researchgate %} <a href="{{ member.researchgate }}" target="_blank"><i class="ai ai-researchgate-square ai-3x"></i></a> {% endif %}
  {% if member.github %} <a href="{{ member.github }}" target="_blank"><i class="fa fa-github-square fa-3x"></i></a> {% endif %}
  <ul style="overflow: hidden">

  {% if member.number_educ == 1 %}
  <li> {{ member.education1 }} </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  {% endif %}

  {% if member.number_educ == 3 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  {% endif %}

  {% if member.number_educ == 4 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  {% endif %}

  {% if member.number_educ == 5 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  <li> {{ member.education5 }} </li>
  {% endif %}

  {% if member.number_educ == 6 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  <li> {{ member.education5 }} </li>
  <li> {{ member.education6 }} </li>
  {% endif %}

  </ul>
</div>

{% endfor %}

## Short biography

<div class="short-bio">
  Roben Castagna Lunardi is an Associate Professor at the Federal Institute of Education, Science and Technology of Rio Grande do Sul (IFRS) - Campus Restinga. He obtained his BSc in Computer Science from the Federal University of Santa Maria (UFSM). During his BSc, he performed an internship and participated in scientific projects at the Southern Regional Center for Space Research (CRSPE) of the National Institute for Space Research (INPE). He obtained an MSc in Computing from the Federal University of Rio Grande do Sul (UFRGS), where he participated in a research project focused on Change Management in IT Infrastructure funded by Hewlett-Packard (HP) R & D Brazil. He obtained a PhD in Computer Science from the Pontifical Catholic University of Rio Grande do Sul (PUCRS). During his PhD, he participated in the research internship program promoted by the Australian Academy of Science (Australia-Americas PhD Research Internship Program) at the University of New South Wales (UNSW), Sydney/Australia in 2018, with the supervision of Professor Salil Kanhere. He also participated a doctoral internship (Sandwich Doctorate) at Newcastle University (Newcastle Upon Tyne / United Kingdom), from October 2019 to March 2020, under the supervision of Professor Aad van Moorsel. He has experience in Computer Science, with an emphasis on Systems Security, Computer Networks and Automation, acting on the following subjects: Blockchains, Information Security, Computer Network Management, Software Defined Networks, Infrastructure Change Management IT, IoT and Educational Robotics. Member of the Brazilian Computer Society (SBC) and member of the IEEE.
</div>

{% if site.data.awards %}
## Awards
<div class="rowl1" style="padding-top: 10px;">

{% for award in site.data.awards %}
{{ forloop.index }}. {% if award.name_url %}<a href="{{ award.name_url }}" target="_blank">{% endif %}<strong>{{ award.name }}</strong>{% if award.name_url %}</a>{% endif %} {% if award.organisation %} from {% if award.organisation_url %}<a href="{{ award.organisation_url }}" target="_blank">{% endif %} {{ award.organisation }}{% if award.organisation_url %}</a>{% endif %}{% endif %}{% if award.subtitle %}: {{ award.subtitle }}{% endif %} ({{ award.year }}).
{% endfor %}
</div>
{% endif %}

{% if site.data.grants %}
## Grants
<div class="rowl1" style="padding-top: 10px;">

{% for grant in site.data.grants %}
{{ forloop.index }}. {% if grant.name_url %}<a href="{{ grant.name_url }}" target="_blank">{% endif %}<strong>{{ grant.name }}</strong>{% if grant.name_url %}</a>{% endif %} {% if grant.organisation %} from {% if grant.organisation_url %}<a href="{{ grant.organisation_url }}" target="_blank">{% endif %} {{ grant.organisation }}{% if grant.organisation_url %}</a>{% endif %}{% endif %}{% if grant.subtitle %}: {{ grant.subtitle }}{% endif %} ({{ grant.year }}).
{% endfor %}
</div>
{% endif %}

{% if site.data.collaborators %}
## Collaborations
<div class="rowl1" style="padding-top: 10px;">

{% for collaborator in site.data.collaborators %}
{{ forloop.index }}. {% if collaborator.name_url %}<a href="{{ collaborator.name_url }}" target="_blank">{% endif %}<strong>{{ collaborator.name }}</strong>{% if collaborator.name_url %}</a>{% endif %} ({{ collaborator.field }}, {% if collaborator.institution_url %}<a href="{{ collaborator.institution_url }}" target="_blank">{% endif %}{{ collaborator.institution }}{% if collaborator.institution_url %}</a>{% endif %}).
{% endfor %}
</div>
{% endif %}


