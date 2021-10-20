## Search 기능 설정

> - Jekyll 블로그는 정적 사이트다 보니 검색 기능이 따로 없다.
> - ` Google Custom Search` 기능을 쓸 수 있지만 `광고`가 뜨고, `스타일` 조절이 어렵다.
> - 대안으로 `lurn.js` 이용 가능 `lurn.js`는 `client side full-text search engine` 이다.
> - Jasper2가 가지고 있는 `subscribe` 기능을 `search` 기능으로 바꿔서 사용할 예정



#### 1. `_includes/site-nav.html` 파일 수정

> - 여기서 `Subscribe`를 `Search`로 변경

`C:\blogmaker\_includes\site-nav.html`

```html
<nav class="site-nav">
    <div class="site-nav-left">
        {% if page.current != 'home' %}
            {% if site.logo %}
                <a class="site-nav-logo" href="{{ site.url }}{{ site.baseurl }}"><img src="{{ site.baseurl}}{{ site.logo }}" alt="{{ site.title }}" /></a>
            {% else %}
                <a class="site-nav-logo" href="{{ site.url }}{{ site.baseurl }}">{{ site.title }}</a>
            {% endif %}
        {% endif %}
        {% if page.navigation %}
            {% include navigation.html %}
        {% endif %}
    </div>
    <div class="site-nav-right">
        <div class="social-links">
            {% if site.facebook %}
                <a class="social-link social-link-fb" href="https://facebook.com/{{ site.facebook }}" target="_blank" rel="noopener">{% include facebook.html %}</a>
            {% endif %}
            {% if site.twitter %}
                <a class="social-link social-link-tw" href="https://twitter.com/{{ site.twitter }}" target="_blank" rel="noopener">{% include twitter.html %}</a>
            {% endif %}
        </div>
        {% if site.subscribers %}
            <a class="subscribe-button" href="#subscribe">Search</a>
        {% endif %}
    </div>
</nav>

```



#### 2. `_layouts/default.html` 파일 수정

> - 다음과 같이 `h1` 태그와  `p` 태그의 내용을 수정한다. & 맨 마지막쯤 `placeholder="keyword"`로 수정

`C:\blogmaker\_layouts\default.html`

```html
{% if site.subscribers %}
        <div id="subscribe" class="subscribe-overlay">
            <a class="subscribe-overlay-close" href="#"></a>
            <div class="subscribe-overlay-content">
                {% if site.logo %}
                    <img class="subscribe-overlay-logo" src="{{ site.baseurl }}{{ site.logo }}" alt="{{ site.title }}" />
                {% endif %}
                <h1 class="subscribe-overlay-title">Search {{ site.title }}</h1>
                <p class="subscribe-overlay-description">lunr.js를 이용한 post 검색</p>
                {% include subscribe-form.html placeholder="keyword" %}
            </div>
        </div>
    {% endif %}
```



#### 3. `_includes/subscribe-form.html` 파일 수정

> - 아래 내용을 복붙

`C:\blogmaker\_includes\subscribe-form.html`

```html
<span id="searchform" method="post" action="/subscribe/" class="">
    <input class="confirm" type="hidden" name="confirm"  />
    <input class="location" type="hidden" name="location"  />
    <input class="referrer" type="hidden" name="referrer"  />

    <div class="form-group">
        <input class="subscribe-email" onkeyup="myFunc()"
               id="searchtext" type="text" name="searchtext"
               placeholder="Search..." />
    </div>
    <script type="text/javascript">
        function myFunc() {
            if(event.keyCode == 13) {
                var url = encodeURIComponent($("#searchtext").val());
                location.href = "/search.html?query=" + url;
            }
        }
    </script>
</span>
```



#### 4. search.html 파일 생성

> - 결론적으로 검색 창에서 키워드 검색하고 엔터치면
> - `C:\blogmaker\search.html` 페이지로 이동하면서 검색 결과가 출력되게끔 한다.
> - 그러기 위해 `blogmaker` 하단에 `search.html` 파일 생성한다
> - 그리고, 아래 코드를 입력한다.

`C:\blogmaker\search.html`

```html
---
layout: page
current: search
title: Search Result
navigation: true
logo:
class: page-template
subclass: 'post page'
---

<form action="/search" method="get" hidden="hidden">
    <label for="search-box"></label>
    <input type="text" id="search-box" name="query">
</form>

<ul class="mylist" id="search-results"></ul>

<script>
    window.store = {
    {% for post in site.posts %}
    "{{ post.url | slugify }}": {
        "title": "{{ post.title | xml_escape }}",
            "author": "{{ post.author | xml_escape }}",
            "category": "{{ post.category | xml_escape }}",
            "content": {{ post.content | strip_html | strip_newlines | jsonify }},
        "url": "{{ post.url | xml_escape }}"
    }
    {% unless forloop.last %},{% endunless %}
    {% endfor %}
    };
</script>
<script src="assets/js/lunr.js"></script>
<script src="assets/js/search.js"></script>
```



#### 5. `lunr.js` 생성

> - [얼큰우동TV 블로그](https://moon9342.github.io/jekyll-search) 에서 제공해주는 `lunr.js` [링크](https://moon9342.github.io/assets/downloads/lunr.js)(minified js 파일)를 통해 파일 생성한 후 내용 복붙
> - `lurn.js` 파일은 `C:/blogmaker/assets/js` 하단에 생성

`C:/blogmaker/assets/js/lurn.js`

```javascript
/**
 * lunr - http://lunrjs.com - A bit like Solr, but much smaller and not as bright - 0.7.2
 * Copyright (C) 2016 Oliver Nightingale
 * @license MIT
 */
!function(){var t=function(e){var n=new t.Index;return  ...
```





#### 6. `search.js` 파일 생성

> - 위 `lunr.js`와 똑같은 경로에 생성 해서 아래 내용 복붙

`C:/blogmaker/assets/js/search.js`

```javascript
(function() {
    function displaySearchResults(results, store) {
        var searchResults = document.getElementById('search-results');

        if (results.length) { // Are there any results?
            var appendString = '';

            for (var i = 0; i < results.length; i++) {  // Iterate over the results
                var item = store[results[i].ref];
                appendString += '<li><a href="' + item.url + '"><h6>' + item.title + '</h6></a>';
                appendString += '<p>' + item.content.substring(0, 150) + '...</p></li>';
            }

            searchResults.innerHTML = appendString;
        } else {
            searchResults.innerHTML = '<li>검색 결과가 없습니다.</li>';
        }
    }

    function getQueryVariable(variable) {
        var query = window.location.search.substring(1);
        var vars = query.split('&');

        for (var i = 0; i < vars.length; i++) {
            var pair = vars[i].split('=');

            if (pair[0] === variable) {
                return decodeURIComponent(pair[1].replace(/\+/g, '%20'));
            }
        }
    }

    function trimmerEnKo(token) {
        return token
            .replace(/^[^\w가-힣]+/, '')
            .replace(/[^\w가-힣]+$/, '');
    };

    var searchTerm = getQueryVariable('query');

    if (searchTerm) {
        document.getElementById('search-box').setAttribute("value", searchTerm);

        // Initalize lunr with the fields it will be searching on. I've given title
        // a boost of 10 to indicate matches on this field are more important.
        var idx = lunr(function () {
            this.pipeline.reset();
            this.pipeline.add(
                trimmerEnKo,
                lunr.stopWordFilter,
                lunr.stemmer
            );
            this.field('id');
            this.field('title', { boost: 10 });
            this.field('author');
            this.field('category');
            this.field('content');
        });

        for (var key in window.store) { // Add the data to lunr
            idx.add({
                'id': key,
                'title': window.store[key].title,
                'author': window.store[key].author,
                'category': window.store[key].category,
                'content': window.store[key].content
            });

            var results = idx.search(searchTerm); // Get lunr to perform a search
            displaySearchResults(results, window.store); // We'll write this in the next section
        }
    }
})();
```

