## Font 설정

> - 가독성을 위해 폰트 설정
> - 로컬 폰트가 아니라 `웹 폰트` 즉, 웹 상에서 제공해주는 폰트를 사용해서 언제 어디서든 사용할 수 있도록 세팅
> - 구글 웹 폰트 서치하면 된다.

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/earlyaccess/nanumgothic.css">
```

> - 위 코드를 `C:\blogmaker\_layouts\default.html` 에 추가해준다.

`C:\blogmaker\_layouts\default.html`

```html
<!DOCTYPE html>
<html>
<head>

    <!-- Document Settings -->
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />

    <!-- Base Meta -->
    {% include dynamic_title.html %}
    <title>{% if title %}{{ title }}{% elsif page.title %}{{ page.title }}{% else %}{{ site.title }}{% endif %}</title>
    <meta name="HandheldFriendly" content="True" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!-- Styles'n'Scripts -->
    <link rel="stylesheet" type="text/css" href="{{ site.baseurl }}assets/built/screen.css" />
    <link rel="stylesheet" type="text/css" href="{{ site.baseurl }}assets/built/screen.edited.css" />
    <link rel="stylesheet" type="text/css" href="{{ site.baseurl }}assets/built/syntax.css" />

    <!-- custom.css 추가 -->
    <link rel="stylesheet" type="text/css" href="{{ site.baseurl }}assets/built/custom.css" />

    <!--  Web font 추가  -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/earlyaccess/nanumgothic.css">
```



> - 이 다음 설정으로 css 파일을 수정해서 특정 class에 대한 font-family에 나눔고딕 폰트 추가하기
> - Jasper2 theme에서 올리는 대부분의 포스트는 `.post-full-content` css class의 영향을 받는다.
> - 다른 theme를 사용한다면 그 theme가 어떤 css class에 영향 받는지 확인해야한다.
> - `assets\css\screen.css` 파일에서 `.post-full-content` 찾아서 다름과 같이 수정한다.

```css
.post-full-content {
    position: relative;
    margin: 0 auto;
    padding: 70px 100px 0;
    min-height: 230px;
    font-family: Georgia, 'Nanum Gothic', serif;
    font-size: 2.2rem;
    line-height: 1.6em;
    background: #fff;
}
```

> - 영문폰트는 `Georgia`로 사용하고 그 다음 영어 외 한글을 쓴다면 `Nanum Gothic` 폰트로 사용
> - css 변경 됐으니 `gulp`를 이용해서 `minified` 하기 위해서 터미널 창에서  `gulp css` 입력한다.

```Terminal
gulp css
```

> - 그 후 `bundle exec jekyll serve` 실행해서 확인하면 바뀐 것을 확인할 수 있다.



## Font Awesome 사용 설정

> - 아이콘`(icon)`을 폰트처럼 사용하게 해주는 기능
> - CDN 방식으로 적용

```html
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
```

> - 위 `Font Awesome CDN` 코드를 `default.css` 파일에 붙여넣기 (아래 보이는 순서로 붙여 놓는다.)
> - 현재는 `custom.css` 파일 안에 Font Awesome 사용할 수 있도록 세팅이 다 돼 있다. (만약 처음부터 한다면 이 부분도 세팅해야 한다는 의미)

`C:\blogmaker\_layouts\default.html`

```html
<!-- custom.css 추가 -->
    <link rel="stylesheet" type="text/css" href="{{ site.baseurl }}assets/built/custom.css" />

    <!--  Font Awesome CDN  -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">

    <!--  Web font 추가  -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/earlyaccess/nanumgothic.css">
```



`C:\blogmaker\assets\css\custom.css`

```css
/* 링크뒤쪽에 FontAwesome표현을 위한 custom CSS */
.post-full-content a[target="_blank"]::after {
    content: '\f08e';
    display: inline-block;
    margin: 0 2px 0 4px;
    line-height: 1;
    font-family: "FontAwesome";
    font-size: 2rem;
    font-weight: normal;
    font-style: normal;
}
```

