## 블로그 디자인 변경

> - `_layouts\post.html` 파일 ==> 블로그 포스팅 올라갈 때 디자인 전체 담당하는 파일
> - 포스팅한 게시물을 열었을 때, 맨 위에 배경 이미지가 처음부터 보이는 것을 바꾸는 방법

```html
<!-- page.cover 주석 처리 == 게시물 안에서 배경화면 없애기
        {% if page.cover %}
        <figure class="post-full-image" style="background-image: url({{ site.baseurl }}{{ page.cover }})">
        </figure>
        {% endif %}
        -->
```



> - 구독 칸 없애기
> - 똑같이 `_layouts\post.html` 파일에서 수정

```html
<!-- Email subscribe form at the bottom of the page 
            {% if site.subscribers %}
                <section class="subscribe-form">
                    <h3 class="subscribe-form-title">Subscribe to {{ site.title }}</h3>
                    <p>Get the latest posts delivered right to your inbox</p>
                    {% include subscribe-form.html placeholder="youremail@example.com" %}
                </section>
            {% endif %}
            -->
```





## Archive 설정

> - `C:\blogmaker`폴더에 `archive.md` 와 `author_archive.md` 파일 생성
> - archive 파일을 통해 포스팅한 시간 순서대로 보여줄 때 사용한다.



- `C:\blogmaker\archive.md`

```md
---
layout: page
current: archive
title: All Posts
navigation: true
logo: 
class: page-template
subclass: 'post page'
---

<div class="well article">
{%for post in site.posts %}
    {% unless post.next %}
        <h2>{{ post.date | date: '%Y' }}</h2>
        <ul>
    {% else %}
        {% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
        {% capture nyear %}{{ post.next.date | date: '%Y' }}{% endcapture %}
        {% if year != nyear %}
            </ul>
            <h3>{{ post.date | date: '%Y' }}</h3>
            <ul>
        {% endif %}
    {% endunless %}
    <li><span class="post-date">
        {% assign date_format = site.date_format.archive %}
        {{ post.date | date: '%Y-%m-%d' }} </span><a href=".{{ post.url }}" target="_blank">{{ post.title }}</a></li>
{% endfor %}
</ul>
</div>
```

![image-20211009234253804](md-images/image-20211009234253804.png)



- `C:\blogmaker\author_archive.md`

```md
---
layout: page
current: archive
title: All Tags
navigation: true
logo:
class: page-template
subclass: 'post page'
---

<div id="post-index" class="well article">
{% capture site_tags %}{% for tag in site.tags %}{{ tag | first }}{% unless forloop.last %},{% endunless %}{% endfor %}{% endcapture %}
{% assign tags_list = site_tags | split:',' | sort %}

<ul class="entry-meta inline-list">
  {% for item in (0..site.tags.size) %}{% unless forloop.last %}
    {% capture this_word %}{{ tags_list[item] | strip_newlines }}{% endcapture %}
  	<li><a href="#{{ this_word }}" class="tag"><span class="term alltags">{{ this_word }}</span> <span class="count alltags">{{ site.tags[this_word].size }}</span></a></li>
  {% endunless %}{% endfor %}
</ul>

{% for item in (0..site.tags.size) %}{% unless forloop.last %}
{% capture this_word %}{{ tags_list[item] | strip_newlines }}{% endcapture %}
<article>
<h2 id="{{ this_word }}" class="tag-heading">{{ this_word | upcase }}</h2>
<ul>
{% for post in site.tags[this_word] %}{% if post.title != null %}
<!-- <li class="entry-title"><a href="{{ site.url }}{{ post.url }}" target="_blank" title="{{ post.title }}">{{ post.title }}</a></li> -->
<li class="entry-title"><a href="{{ post.url }}" target="_blank" title="{{ post.title }}">{{ post.title }}</a></li>
{% endif %}{% endfor %}
</ul>
</article><!-- /.hentry -->
{% endunless %}{% endfor %}
</div>
```

![image-20211009234309835](md-images/image-20211009234309835.png)

