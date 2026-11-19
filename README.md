# Lasorie RPG World

게임 개발·공부 기록과 프로젝트 포트폴리오를 모아두는 블로그입니다.

- [블로그 열기](https://lasorie95.github.io/)
- [개발·공부 기록](https://lasorie95.github.io/posts/)
- [프로젝트](https://lasorie95.github.io/projects/)

## VS Code에서 작성하고 실시간으로 확인하기

이 폴더를 VS Code로 열고 **Ctrl+Shift+B**를 누르면 **블로그 미리보기** 작업이 실행됩니다. 처음 폴더를 열 때 신뢰 여부가 표시되면 본인의 블로그 폴더인지 확인하고 신뢰합니다.

브라우저가 열리면 `http://127.0.0.1:4000`에서 현재 블로그 디자인을 확인할 수 있습니다. VS Code와 브라우저를 나란히 놓고 글을 수정한 다음 **Ctrl+S**로 저장하세요. 빌드가 끝나면 브라우저가 자동으로 갱신됩니다. 서버가 실행된 터미널은 열어 둡니다. 종료하려면 그 터미널에서 **Ctrl+C**를 누르세요.

Windows에서는 [Jekyll Windows 설치 안내](https://jekyllrb.com/docs/installation/windows/)에 따라 Ruby 3.3+Devkit을 설치합니다. 실행 스크립트는 사용자 폴더의 `Ruby33-x64`를 먼저 찾고, 해당 폴더가 없으면 `PATH`에 등록된 Ruby를 사용합니다. 처음 실행할 때는 **터미널 → 작업 실행 → 블로그 의존성 설치**를 실행합니다. 각 작업은 Windows의 프록시 설정을 해당 작업에서만 사용합니다.

### 초안 작성

1. `_drafts` 폴더에 `my-devlog.md`처럼 새 Markdown 파일을 만듭니다. 초안 파일 이름에는 날짜를 붙이지 않아도 됩니다.
2. 새 파일에서 `devlog`를 입력하고 **Ctrl+Space**로 **개발일지 작성 양식**을 선택합니다. **Tab**으로 제목·요약·본문 입력 위치를 이동할 수 있습니다.
3. 글과 이미지를 저장하고 브라우저의 **개발·공부 기록** 목록에서 해당 초안을 엽니다. 미리보기는 `--drafts` 옵션으로 로컬 초안을 함께 표시합니다.
4. 스크린샷은 `assets/images/`에 저장하고 아래의 이미지 문법으로 삽입합니다.

`_drafts/`는 Git에서 제외하므로 현재 PC에만 보관됩니다. PC를 바꾸면 자동으로 따라오지 않습니다. 아직 공개하지 않을 이미지는 글을 게시할 때 함께 추가하거나, Git 변경 목록에서 올릴 파일을 직접 선택하세요.

### 완성한 글 게시·수정

공개할 준비가 된 초안은 `_posts/2026-10-16-crafting-devlog.md`처럼 **게시일-영문제목.md** 이름으로 옮깁니다. 파일 안에 `date:`가 있다면 게시일과 맞춥니다. 제목·카테고리·태그·이미지 경로를 확인한 뒤, VS Code의 **소스 제어**에서 해당 글과 필요한 이미지만 선택해 커밋하고 Push합니다. 이후 GitHub Pages가 자동으로 게시합니다. **Ctrl+S로 저장만 하면 공개 사이트에 올라가지는 않습니다.**

이미 게시한 글은 `_posts/`의 해당 파일을 열어 수정합니다. 기존 파일 이름을 유지하면 현재 글 주소도 유지됩니다. 수정 후 다시 커밋하고 Push하면 반영됩니다.

VS Code 기본 Markdown 미리보기와 실제 블로그는 모양이 다를 수 있으므로 최종 화면은 Jekyll 미리보기 브라우저에서 확인합니다. `_config.yml`을 변경했을 때는 미리보기를 종료하고 다시 실행해야 합니다. 로컬에서 확인한 초안은 온라인에 게시되지 않으며, 실시간 갱신에는 파일 저장과 재빌드 시간이 필요합니다.

## 첫 글 작성하기

GitHub에서 이 저장소를 열고 **Add file → Create new file**을 선택합니다. 파일 이름을 `_posts/2026-10-15-godot-notes.md`처럼 입력합니다. 날짜 뒤의 영문 부분은 글 주소에 사용됩니다.

아래는 형식 예시입니다. 이 README의 예시는 블로그 글로 게시되지 않습니다. 제목·날짜·내용을 자신의 기록으로 바꿔 사용하세요.

````markdown
---
title: "Godot 공부 기록"
date: 2026-10-15
categories:
  - Godot
tags:
  - Godot
  - 공부
excerpt: "이번 기록의 내용을 한두 문장으로 적습니다."
---

## 오늘 배운 내용

배운 내용을 정리합니다.

## 코드 메모

```csharp
// 정리할 코드를 여기에 적습니다.
```

## 돌아보기

어려웠던 점과 다음에 확인할 내용을 적습니다.
````

**Commit changes**로 `main`에 저장하면 GitHub Pages가 자동으로 게시합니다. 처음 반영되기까지 몇 분 걸릴 수 있습니다. 작성한 글은 최신 글·카테고리·태그·검색에 반영됩니다. 예시의 글 주소는 `/posts/godot-notes/`입니다.

`date`를 미래 날짜로 지정하면 그 날짜 전에는 글이 표시되지 않을 수 있습니다. 임시 글은 파일 앞부분에 `published: false`를 추가하면 블로그에서 숨길 수 있습니다. Public 저장소의 파일 원본은 GitHub에서 볼 수 있으므로, 개인 메모는 별도로 보관하세요.

## 이미지 넣기

이미지를 저장소의 `assets/images/` 폴더에 올린 뒤 글이나 프로젝트 본문에서 사용합니다. 예를 들어 `assets/images/game-screen.png`를 올렸다면 다음처럼 적습니다.

```markdown
![게임 화면](/assets/images/game-screen.png)
```

이미지는 실제 본인이 공개할 화면을 사용하고, 설명은 이미지 내용을 알 수 있게 적습니다. 현재 블로그에는 게임 화면이나 프로필 사진을 임의로 넣지 않았습니다.

## 프로젝트 소개 수정하기

Recorded Lore는 **프로젝트 → Recorded Lore**에서 **개발일지**와 **세계관**으로 나누어 탐색합니다.

- 프로젝트 소개와 기록 목록: `_projects/recorded-lore.md`
- 개발일지 카테고리: `_pages/recorded-lore-devlog.html`
- 세계관 카테고리: `_pages/recorded-lore-worldbuilding.html`
- 프로젝트 내부 메뉴: `_data/navigation.yml`의 `recorded-lore`

Recorded Lore 글에는 앞부분에 `project: recorded-lore`를 넣으면 프로젝트 기록 목록에 자동으로 표시됩니다. 세계관 글은 다음 형식으로 작성하면 세계관 카테고리에도 표시됩니다. 아직 세계관 글이 없어도 카테고리 페이지와 메뉴는 열립니다.

개발일지는 같은 형식에서 `categories`를 `개발일지`로 지정하면 개발일지 카테고리에 표시됩니다. 기존 개발일지 #01도 이 분류를 사용합니다.

```yaml
---
title: "세계관 글 제목"
date: 2026-10-21
project: recorded-lore
categories:
  - 세계관
tags:
  - Recorded Lore
sidebar:
  nav: [recorded-lore]
---
```

새 프로젝트를 소개하려면 `_projects/` 안에 별도의 Markdown 파일을 추가합니다. 프로젝트 이름·소개·도구·역할과 본문을 작성하면 프로젝트 목록과 상세 페이지에 반영됩니다.

## 블로그 설정

| 바꿀 내용 | 파일 |
| --- | --- |
| 블로그 이름, 소개, 작성자, GitHub 링크 | `_config.yml` |
| 주요 메뉴 | `_data/navigation.yml` |
| 소개 페이지 | `_pages/about.md` |
| 홈의 소개 영역과 관심 분야 | `index.html` |
| 프로젝트 정보 | `_projects/` 안의 Markdown 파일 |
| 색상과 간격 등 추가 스타일 | `_sass/lasorie-pixel.scss` |

공개 연락처는 아직 설정하지 않았습니다. Minimal Mistakes 4.28.1을 기반으로 픽셀 모험 일지 디자인을 적용했으며, 글과 프로젝트는 Markdown으로 관리합니다.

제목에는 갈무리11, 본문에는 Pretendard를 사용합니다. 폰트 파일은 `assets/fonts/`에서 직접 제공하며, 코드 블록은 고정폭 글꼴을 유지합니다. 폰트별 저작권과 SIL Open Font License는 같은 폴더의 라이선스 파일에 보관합니다. 출처: [갈무리](https://github.com/quiple/galmuri), [Pretendard](https://github.com/orioncactus/pretendard). 홈의 픽셀 산은 배경 장식이며 실제 게임 화면이 아닙니다.

## 게시 확인과 문제 해결

저장소의 **Actions**에서 빌드 결과를 볼 수 있습니다. 작업 브랜치의 **Build blog preview**는 검토용 HTML을 만들며 실제 사이트를 배포하지 않습니다. 실제 게시 원본은 **Settings → Pages → main / (root)**입니다.

산출물 검증은 다음 명령으로 실행합니다.

```text
python scripts/check_site.py --site-dir _site
```

이 검증은 필수 페이지와 내부 링크, 프로필 정보, 개발 파일 제외 여부를 확인합니다. 블로그 이름이나 프로필을 변경했다면 `scripts/check_site.py`의 해당 콘텐츠 확인 항목도 새 내용에 맞춰 조정하세요.

빌드가 실패하면 Actions의 실패한 단계에서 오류 내용을 확인합니다. 글 위쪽의 `---` 구분, YAML 들여쓰기, 파일 날짜, 이미지 경로를 먼저 확인하세요. 기존 게시물이 남아 있다면 Pages 배포 결과와 브라우저 새로고침도 확인합니다.
