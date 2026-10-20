---
title: "Recorded Lore"
permalink: /projects/recorded-lore/
excerpt: "Recorded Lore의 개발 과정과 세계관 기록을 모아두는 프로젝트입니다."
project: recorded-lore
tools:
  - Godot
  - C#
  - VS Code
  - Git
sidebar:
  nav: [recorded-lore]
---

<nav class="world-archive-nav" aria-label="프로젝트 경로">
  <a href="{{ '/projects/' | relative_url }}">프로젝트</a>
  <span aria-hidden="true">›</span>
  <span aria-current="page">Recorded Lore</span>
</nav>

Godot와 C#으로 개발을 시작한 프로젝트입니다. 개발일지와 세계관 기록을 이곳에서 모아볼 수 있습니다.

## 카테고리

<nav class="world-topics" aria-label="Recorded Lore 하위 카테고리">
  <a href="{{ '/projects/recorded-lore/devlog/' | relative_url }}">개발일지 <span aria-hidden="true">→</span></a>
  <a href="{{ '/projects/recorded-lore/worldbuilding/' | relative_url }}">세계관 <span aria-hidden="true">→</span></a>
</nav>

## 프로젝트 기록

{% assign project_posts = site.posts | where: "project", page.project %}
{% if project_posts.size > 0 %}
<div class="entries-list">
  {% for post in project_posts %}{% include archive-single.html type="list" %}{% endfor %}
</div>
{% else %}
<div class="world-empty"><p>아직 등록된 프로젝트 기록이 없습니다.</p></div>
{% endif %}
