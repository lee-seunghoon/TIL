## Menu bar 생성

> - `_includes\navigation.html` 파일에서 수정



```html
<ul class="nav" role="menu">
    <li class="nav-home" role="menuitem"><a href="{{site.baseurl}}">Home</a></li>

    <!-- about 폴더가 따로 있다. 그 안에 index.md 파일을 수정 -->
    <li class="nav-about" role="menuitem"><a href="{{site.baseurl}}about/">About</a></li>

    <!-- href에 우리가 tags.yml 파일에서 설정한 tag명을 넣어준다. -->
    <li class="nav-Python" role="menuitem"><a href="{{site.baseurl}}tag/Python/">Python</a></li>
    <li class="nav-AI" role="menuitem"><a href="{{site.baseurl}}tag/AI/">AI_ML/DL</a></li>

    <!-- 모든 포스트를 전체 보여주는 -->
    <li class="nav-archive" role="'menuitem">
        <a href="/archive.html">All Posts</a>
    </li>

    <!-- Tag별로 포스트를 모아주는 -->
    <li class="nav-archive" role="menuitem">
        <a href="author_archive.html">Tag별 Posts</a>
    </li>
</ul>

```



## Post 생성

> - 글을 포스팅하기 위해서 `_posts`  폴더에 있는 파일을 잘 관리할 필요 있음
> - 기존 있는 것은 모두 지우고, tag에 맞게 폴더를 생성한 후
> - `yyyy-mm-dd-title.md` 형식으로 파일을 만들어야 함



- `_posts\python\2021-10-09-python_basic.md`

```tex
---
layout: post
current: post
cover: assets/built/images/python.jpg
navigation: True
title: Python 정리 Test
date: 2021-10-09 13:19:00 +0900		==> 오늘 날짜로 올려줄 때는 +0900 추가 필요
tags: [Python]						==> Tag 명을 잘 세팅할 필요 있음
class: post-template
subclass: 'post tag-python'
author: sherlocky					==> 나의 author 명과 동일하게
---

# 파이썬 시작

안녕하세요.
파이썬 관련 내용 업로드합니다.

```

