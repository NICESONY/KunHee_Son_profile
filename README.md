# KunHee Son 개인 홈페이지

## 바로 보기

`html_source_file/index.html`을 브라우저에서 열면 된다. 실행 환경 설치는 필요 없다. 글꼴은 Google Fonts를 사용하며, 인터넷 연결이 없으면 기본 serif 글꼴로 표시된다. 사진, 스타일, 메뉴 스크립트와 본문은 로컬 파일이다.

HTTP로 확인하려면 이 폴더에서 실행한다.

```powershell
python -m http.server 8765 --bind 127.0.0.1 --directory html_source_file
```

브라우저 주소: `http://127.0.0.1:8765/`

## 내용 수정

`_data/profile.json`이 프로필과 모든 기록의 원본이다. 파일을 수정한 뒤 아래 명령을 실행한다.

```powershell
python -m pip install -r requirements.txt
python scripts/build_site.py
```

이 명령은 Jekyll용 `index.md`, `_config.yml`의 기본 프로필 값, 정적 HTML 버전인 `html_source_file/`을 갱신한다. `index.md`와 `html_source_file/index.html`은 생성 파일이므로 직접 편집하면 다음 빌드에서 덮어써진다.

- 화면 구조: `_layouts/homepage.html`
- 추가 스타일: `assets/css/profile.css`
- 프로필 사진: `assets/img/profile.jpg`
- CV: `assets/files/CV_KunHeeSon_AILAB.pdf`. 사용자가 지정한 GIST 이규빈 교수님 연구실 컨택용 원본을 복사했고, 프로필의 CV 버튼으로 새 탭에서 열린다.
- Google Scholar: `_data/profile.json`의 `google_scholar`. 사용자가 제공한 `L9IDiMgAAAAJ` 프로필을 Scholar 버튼에 연결했다.
- LinkedIn: `_data/profile.json`의 `linkedin`. 사용자의 CV PDF에 포함된 `https://www.linkedin.com/in/kunhee-son-9922932a1/` 주소를 연결했다.
- 원문에는 있지만 공개 접근이 되지 않는 주소: `_data/profile.json`의 `unavailable_links`. 이 목록의 주소는 원문 데이터에 보존되며 페이지에 링크로 출력되지 않는다.

`scripts/import_google_sites.py`는 작업공간의 `source_material/` 스냅샷에서 최초 데이터를 가져오는 도구다. 사용자가 내용을 수정한 뒤 다시 실행하면 원문 스냅샷 내용으로 돌아가므로, 평소에는 `build_site.py`만 사용한다. 이 최초 이관 도구에는 별도로 `beautifulsoup4`가 필요하다.

## 구성

| 항목 | 이관 내용 |
| --- | --- |
| 프로필 | 사진, 이름, 소속, 이메일, GitHub, 자기소개 |
| 연구 | 관심 분야, 최근·이전 연구 분야, 원문의 KIICE 표기 |
| 학력 | 2건 |
| 논문 | 3건 |
| 프로젝트 | ROS 2건, Web 5건 |
| 수상 | 10건 |
| 대외활동 | 8건 |
| 역량 | 프로그래밍 3건, 영어 시험 2건 |

Google Sites의 CV, Hugging Face, Scholar, LinkedIn 및 일부 `link` 글자에는 URL이 없었다. CV는 후속 요청에 따라 로컬에서 찾은 PDF로, Scholar는 사용자가 제공한 주소로, LinkedIn은 CV에 담긴 주소로 연결했다. 나머지 주소는 추측하지 않았다. 잘못된 날짜와 원문 링크에 관한 확인 사항은 작업공간의 `MIGRATION.md`에 기록했다.

## 게시용 파일

`html_source_file/` 전체가 정적 게시용 폴더다. `index.html`, `assets/`, `.nojekyll`, `LICENSE`를 함께 사용한다. 상위의 질문 기록이나 수집 자료는 게시용 폴더에 포함되지 않는다.

공개 저장소는 [NICESONY/KunHee_Son_profile](https://github.com/NICESONY/KunHee_Son_profile)이며, 공식 테마를 fork해 사용한다. 공개 주소는 [https://nicesony.github.io/KunHee_Son_profile/](https://nicesony.github.io/KunHee_Son_profile/)다. `.github/workflows/pages.yml`은 `main`에 push할 때 데이터를 빌드하고 `html_source_file/`만 GitHub Pages에 배포한다.

GitHub Pages 프로젝트 주소의 마지막 경로는 저장소 이름을 따른다. 사용자의 요청에 따라 저장소 이름을 `minimal-light`, `profile`을 거쳐 `KunHee_Son_profile`로 변경했다. 주소 경로에 밑줄(`_`)을 사용할 수 있다. 테마 이름과 로컬 작업 폴더 이름은 주소를 결정하지 않는다.

프로필의 CV·Email·GitHub·Scholar·LinkedIn과 본문의 외부 링크는 아이콘으로 표시한다. 툴팁과 접근성 이름으로 링크의 용도를 알 수 있다. 연구 키워드는 사용자의 수정 요청을 반영한 `Robotic Manipulation`, `Data Collection Systems`, `Sim-to-Real`이다.

루트에는 Jekyll 소스도 유지했다. Ruby/Bundler가 없는 현재 환경에서는 Jekyll 빌드를 실행하지 않았으며, 브라우저 검증은 생성된 정적 HTML을 기준으로 수행했다.

## 출처와 라이선스

- 내용: [Kun-Hee Son Google Sites](https://sites.google.com/view/khson-profile-record), 2026-09-19 수집.
- 테마: [yaoyao-liu/minimal-light](https://github.com/yaoyao-liu/minimal-light), 기준 commit `1ea07f39518ac44644406380c83da6f89037c4fc`.
- 원본 테마의 CC0 라이선스는 `LICENSE`에 보존했다. 개인 사진과 프로필 내용의 권리는 해당 권리자에게 있다.
