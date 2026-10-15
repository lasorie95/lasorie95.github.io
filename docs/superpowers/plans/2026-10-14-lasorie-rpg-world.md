# Lasorie RPG World Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 제공받은 정보로 개발·공부 기록과 Project RPG 포트폴리오를 갖춘 한국어 블로그를 제작하고 GitHub Pages에 게시한다.

**Architecture:** Jekyll과 고정 버전 Minimal Mistakes remote theme로 Markdown을 정적 HTML로 생성한다. 글은 `_posts`, 프로젝트는 `_projects` collection으로 관리하며 홈과 프로젝트 목록에서 같은 카드 구성 요소를 사용한다. 작업 브랜치의 빌드 결과를 검증한 뒤 `main`에 반영하고 기존 GitHub Pages의 브랜치 게시 방식을 사용한다.

**Tech Stack:** GitHub Pages, Jekyll, Minimal Mistakes 4.28.1, Liquid, Sass, Lunr, Python 표준 라이브러리를 사용하는 산출물 확인 도구.

**Spec:** `docs/superpowers/specs/2026-10-14-lasorie-rpg-world-design.md` — 사용자 승인 완료.

## Global Constraints

- 사이트 제목 `Lasorie RPG World`, 작성자 `lasorie95`, 소개 `TA를 지향하는 일반인 입니다.`를 그대로 사용한다.
- 관심 분야는 `게임 개발 일지`, `C#`, `Godot`, `2D dot Graphic`, `공부 회고`이다.
- 테마는 `mmistakes/minimal-mistakes@4.28.1`, skin은 밝은 파란색 계열의 `air`이다.
- `locale: ko-KR`, `timezone: Asia/Seoul`, `url: https://lasorie95.github.io`, `baseurl: ""`, `repository: lasorie95/lasorie95.github.io`로 설정한다.
- 블로그 저장소는 Public이며 기존 저장소와 Git 기록을 보존한다.
- Project RPG는 PC용 2D RPG, 1인 개발, 도구 `Godot`, `VS Code`, `Git`, `Aseprite`까지만 사실로 소개한다. 최종 이름은 미정이다.
- 프로젝트의 개발 상태·진행률·출시일·구현 언어·경력·성과는 추정하지 않는다. `TA`를 임의로 풀어 쓰지 않는다.
- 프로젝트 저장소 링크 후보는 `https://github.com/lasorie95/project_rpg`이며, 익명 방문자도 접근할 수 있음이 확인되기 전에는 링크 대신 `프로젝트 저장소 공개 준비 중`을 표시한다.
- 프로젝트 저장소의 공개 설정이나 비공개 소스는 이 작업의 대상이 아니다. 연락처 미제공 상태를 유지하고 과거 로그인 이메일을 사이트에 넣지 않는다.
- 실제 첫 글과 프로젝트 이미지는 제공되지 않았다. 빈 글 목록과 이미지 없는 프로젝트 카드가 정상 작동해야 한다.
- 검증은 실제 Jekyll 빌드, 생성된 HTML·검색 데이터, 브라우저 탐색과 모바일 화면을 대상으로 한다.

## Review Focus

1. 글이 하나도 없을 때 홈·글 목록·카테고리·태그가 안내 문구와 정상 메뉴를 보여야 한다. Task 1에서 실제 빈 상태를 확인한다.
2. 한국어와 영문이 섞인 프로젝트 내용이 검색되어야 한다. Task 1에서 `Project RPG`, `Godot`, `1인`을 입력한다.
3. 프로젝트 이미지가 없고 저장소가 비공개여도 카드와 상세 설명은 읽을 수 있어야 한다. Task 1에서 이미지 요청과 비공개 GitHub 링크 부재를 확인한다.
4. 긴 사이트 이름과 한국어 메뉴가 좁은 화면에서 겹치지 않아야 한다. Task 1에서 390px 및 1440px 화면을 확인한다.
5. 공개 사이트에 문서·개발 파일·미제공 연락처가 섞이지 않아야 한다. Task 2에서 최종 산출물과 실제 배포를 확인한다.

## Files and Responsibilities

| 파일 | 책임 |
| --- | --- |
| `_config.yml`, `Gemfile`, `.gitignore` | 테마·플러그인·언어·URL·collection·빌드 제외 설정 |
| `_data/navigation.yml`, `_data/ui-text.yml` | 주요 메뉴와 테마의 한국어 UI 문구 |
| `index.html` | 소개, 최신 글, 대표 프로젝트를 가진 홈 |
| `_pages/posts.html`, `_pages/categories.html`, `_pages/tags.html` | 글 목록과 분류별 탐색, 빈 상태 |
| `_pages/about.md` | 소개 문구, 관심 분야, 공개 GitHub 프로필 |
| `_pages/projects.html`, `_projects/project-rpg.md` | 프로젝트 목록과 제공받은 프로젝트 정보 |
| `_includes/project-card.html` | 홈·프로젝트 목록에서 공유하는 카드 |
| `_includes/project-repository-link.html` | 공개 상태에 따른 저장소 링크 또는 안내 |
| `assets/css/main.scss`, `_sass/lasorie.scss` | 테마 import와 블로그에 필요한 작은 스타일 조정 |
| `_posts/.gitkeep` | 첫 글을 넣을 디렉터리 보존 |
| `scripts/check_site.py` | 생성된 사이트의 경로·정보·내부 링크 확인 |
| `.github/workflows/build.yml` | 작업 브랜치와 PR의 Jekyll 빌드 및 검토용 산출물 업로드 |
| `README.md` | 글·이미지·프로젝트 수정과 게시 방법을 설명하는 한국어 운영 안내 |

## Execution Environment

- 로컬 체크아웃은 `C:/Users/USER/Documents/ChatGPT/test/lasorie95.github.io`, 작업 브랜치는 `codex/lasorie-rpg-blog`이다. GitHub 연동 계정은 `lasorie95`이고 저장소 admin/push 권한이 확인됐다.
- 이 Windows 세션에는 사용 가능한 Ruby/bundle과 WSL Linux 환경이 확인되지 않았고, 로컬 `gh`는 인증되지 않았다. 기본 검증 경로는 GitHub Actions의 Linux 빌드 산출물이다.
- 실행을 시작할 때 `superpowers:using-git-worktrees`에 따라 블로그 저장소를 대상으로 격리한다. 앱의 현재 작업 폴더는 별도의 Git 저장소이므로 그 저장소에 블로그 브랜치를 만들지 않는다. 기존 로컬 블로그 체크아웃을 쓰거나, 블로그 저장소에서 파생한 worktree를 사용한다.
- 작업 브랜치의 원격 변경에는 기존 GitHub 연동을 사용한다. 워크플로 파일 쓰기 권한이 부족하면 사용자 권한을 임의로 바꾸지 않고 공식 RubyInstaller 기반의 로컬 빌드 대안을 확인한다. 두 검증 경로 모두 사용할 수 없으면 검토 가능한 소스를 보존하고 정확히 필요한 접근만 요청한다.
- 빌드 결과를 로컬에 내려받아 Python 정적 서버와 지원되는 브라우저 도구로 화면을 점검한다. 예시 서버 명령은 `python -m http.server 8765 --directory _site`이다.
- 로컬의 `python` 명령에는 번들 실행 파일 `C:/Users/USER/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`를 사용한다. JS 문법 확인에는 같은 번들의 `dependencies/node/bin/node.exe`를 사용한다. Actions의 Linux runner에서는 `python3`를 사용한다.

---

### Task 1: 블로그와 프로젝트 페이지 제작 및 빌드 검증

**Files:** 위 표에서 README를 제외한 모든 제작·검증 파일을 생성하거나 수정한다. 기존 `index.html`을 블로그 홈으로 교체한다.

**Interfaces:**
- Consumes: 승인된 spec의 문구와 경로, 현재 저장소의 `main` 및 작업 브랜치.
- Produces: 완성된 Jekyll source와 `_site` 산출물. 글 상세 경로는 `/posts/:title/`, 프로젝트 상세는 `/projects/:path/`이다.
- 프로젝트 front matter는 `title: Project RPG`, `permalink: /projects/project-rpg/`, `role: 1인 개발`, `tools: [Godot, VS Code, Git, Aseprite]`, `repository_url: https://github.com/lasorie95/project_rpg`, `repository_public: false`를 사용한다. 방문자 공개 접근이 별도로 확인된 경우에만 마지막 값을 true로 바꾼다.
- `project-card.html`과 `project-repository-link.html`은 `include.project`로 Jekyll document를 받는다. 카드 제목은 문서의 `url`로 연결한다. 저장소 helper는 `repository_public`과 URL이 모두 유효할 때만 외부 링크를 만든다.
- 검증 도구의 인터페이스는 `read_page(site_dir: Path, route: str) -> str`, `check_site(site_dir: Path) -> list[str]`, CLI `python scripts/check_site.py --site-dir <directory>`이다. 오류가 없으면 `PASS`와 종료 코드 0, 오류가 있으면 경로별 오류와 종료 코드 1을 반환한다.

- [x] **Step 1: 실제 출력에 대한 확인 도구를 먼저 작성한다.** 필수 경로 `/`, `/posts/`, `/categories/`, `/tags/`, `/projects/`, `/projects/project-rpg/`, `/about/`와 로컬 내부 링크의 파일 존재 여부를 확인한다. 생성된 HTML에 사이트 제목·소개·Project RPG·역할·도구가 표시되고, 비공개 저장소 링크와 mailto 링크는 없음을 확인한다.
- [x] **Step 2: 초기 저장소에서 확인이 실패하는지 확인한다.** `python scripts/check_site.py --site-dir .`를 실행한다. 현재 Hello World 화면과 없는 페이지 때문에 종료 코드 1이어야 한다.
- [x] **Step 3: Jekyll 설정을 작성한다.** Gemfile에 공식 remote-theme 방식의 `github-pages`와 `jekyll-include-cache`를 넣고, config plugins에 `jekyll-remote-theme`, `jekyll-include-cache`, `jekyll-feed`, `jekyll-sitemap`을 설정한다. `_pages`를 include하고 `projects` collection의 `output: true`와 permalink를 설정한다. docs·scripts·README·Gemfile·빌드 캐시를 HTML 산출물에서 제외한다.
- [x] **Step 4: 한국어 UI와 읽기 화면을 작성한다.** 테마 버전의 한국어 UI 문구를 사용하고 사용자 제공 메뉴명을 적용한다. 홈은 소개·최신 글·대표 프로젝트 영역, 글 목록은 최신순, 분류 페이지는 테마의 Liquid category/tag archive를 사용한다. 등록된 글이 없을 때 각 화면에 한국어 안내를 표시한다. 소개는 정확한 소개 문구와 관심 분야를 사용한다.
- [x] **Step 5: 포트폴리오와 공유 helper를 작성한다.** 제공한 설명·도구·역할을 `_projects/project-rpg.md`에 넣고 메뉴 및 홈에서 프로젝트 상세로 연결한다. 실제 이미지 없이 텍스트 카드로 렌더링하며, 저장소 링크 대신 공개 준비 안내를 표시한다.
- [x] **Step 6: 검색과 스타일을 적용한다.** config는 `search: true`, `search_provider: lunr`, `lunr.search_within_pages: true`로 설정한다. air skin을 import한 뒤 사이트 영역에 한정한 모바일 여백·카드 간격·제목 줄바꿈 스타일을 적용한다. 테마의 검색·코드 강조·RSS·사이트맵을 사용한다.
- [x] **Step 7: 게시 없는 빌드 workflow를 작성한다.** push(작업 브랜치 포함)와 pull_request 이벤트에서 `permissions: contents: read`로 `actions/checkout@v6`, `actions/jekyll-build-pages@v1`(`source: ./`, `destination: ./_site`), 산출물 확인 도구, `actions/upload-pages-artifact@v4`를 실행한다. deploy 단계와 Pages 설정 변경은 넣지 않는다. Actions에서는 `python3 scripts/check_site.py --site-dir _site`를 실행한다.
- [x] **Step 8: 제작 소스를 기록하고 작업 브랜치만 올린다.** `git diff --check`와 변경 파일을 확인한 후 제작·검증 파일을 commit한다. 원격 현재 commit을 다시 확인해 동시 변경을 보존하고 검토용 PR을 만든다. PR을 만들면 앱에 연결한다. PR-triggered workflow의 성공과 해당 commit SHA에 대한 산출물을 확인한다. 쓰기 권한 제한이 있으면 위 환경 대안으로 실제 Jekyll 빌드를 실행한다.
- [x] **Step 9: 검토용 산출물을 확인한다.** 다운로드한 archive는 별도의 검토 디렉터리에 풀고 `python scripts/check_site.py --site-dir <output>`를 실행한다. `sitemap.xml`, `feed.xml`, 테마 CSS·JS가 존재하며 unresolved Liquid가 없는지 확인한다. `node --check <output>/assets/js/lunr/lunr-store.js`의 종료 코드 0으로 검색 데이터 JS 문법도 확인한다.
- [x] **Step 10: 브라우저로 확인한다.** 1440px/390px에서 홈·프로젝트 상세·메뉴를 보고 링크를 따라 이동한다. 검색에 `Project RPG`, `Godot`, `1인`을 입력해 실제 결과와 이동을 확인한다. 빈 글·카테고리·태그 화면, 이미지 없는 카드, 공개 준비 안내도 확인한다. 발견한 오류만 수정한 뒤 영향받은 확인을 다시 수행한다.
- [x] **Step 11: 확인된 상태를 기록한다.** 화면 검증에서 수정한 파일이 있으면 `git diff --check` 후 commit하고 영향받은 빌드·화면을 다시 확인한다. Task 2가 사용할 정확한 원격 commit과 빌드 결과를 기록한다.

### Task 2: 운영 안내, 최종 검토, 실제 게시

**Files:** `README.md`를 수정한다. 필요할 때만 Task 1 파일의 검증에서 발견된 오류를 수정한다.

**Interfaces:**
- Consumes: Task 1의 source commit, 성공한 build 결과, 사이트 경로와 프로젝트 front matter.
- Produces: 한국어 작성 안내, 검증된 `main` source, 실제 `https://lasorie95.github.io/`의 게시 결과.

- [ ] **Step 1: README를 작성한다.** 새 글 파일명 `YYYY-MM-DD-title.md`, front matter의 `title`·`date`·`categories`·`tags`, 코드 블록과 `/assets/images/` 경로를 설명한다. 실제 활동처럼 게시되지 않는 글 예시를 README 안에만 둔다. 프로젝트 도구·역할 수정과 공개 확인 후 `repository_public` 변경 방법도 설명한다.
- [ ] **Step 2: 최종 소스를 검증한다.** `git diff --check`와 실제 Jekyll build를 수행한다. 산출물 확인 도구가 PASS이고 docs·scripts·README·Gemfile이 게시 산출물에 없는지 확인한다. 이메일이나 연락처가 새로 들어가지 않았음을 확인한다. 문서-only 변경에 별도 unit test는 추가하지 않는다.
- [ ] **Step 3: 최종 변경을 독립적으로 검토한다.** 검토자는 승인된 spec와 이 계획을 함께 읽고 제공한 사실·기능 범위·모바일·검색·링크와 빌드 증거를 확인한다. 지적이 있으면 근거를 확인하고 해당 부분을 수정·재검증한다.
- [ ] **Step 4: 검증된 변경을 게시한다.** 사용자가 요청한 블로그 제작·게시 범위 안에서 검증한 PR/commit을 `main`에 반영한다. 기존 Pages source를 확인하고 필요하면 `main` 루트의 브랜치 Jekyll 게시로 설정한다. 프로젝트 저장소와 접근 정책은 변경하지 않는다.
- [ ] **Step 5: 실제 게시 결과를 확인한다.** 최신 source commit에 대한 게시 성공을 확인하고 공개 URL과 주요 경로의 정상 응답, 새 사이트 제목, Project RPG 소개, 검색·CSS·메뉴를 확인한다. 실패하면 빌드·게시 오류를 수정하고 최신 commit의 성공을 다시 확인한다.
- [ ] **Step 6: 사용자가 쓸 결과를 전달한다.** 공개 블로그 링크와 README의 글 작성 안내를 제공한다. 첫 글·게임 화면을 나중에 추가할 위치와 프로젝트 링크 공개 준비 상태만 간단히 설명한다.

## Execution Recommendation

**직접 구현(Native)을 추천한다.** 두 작업이 같은 Jekyll 설정·문구·레이아웃을 공유하므로 이 세션에서 연속 구현하고 마지막에 독립 검토를 받는 방식이 간단하다. 단계별 구현·검토(Subagent-driven)는 각 작업에 별도 구현자와 검토자를 사용해 검토를 더 자주 수행하는 대안이다.

사용자가 이 계획을 검토하고 실행 방식을 선택하기 전에는 제품 코드, 의존성 설치, 원격 파일 변경을 시작하지 않는다.

## References

- [Minimal Mistakes 설정](https://mmistakes.github.io/minimal-mistakes/docs/configuration/)
- [Minimal Mistakes 레이아웃](https://mmistakes.github.io/minimal-mistakes/docs/layouts/)
- [GitHub 공식 Jekyll 빌드 workflow](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
