# 아키텍처 의사결정 기록(ADR)

아키텍처 의사결정 기록(ADR)은 내려진 중요한 아키텍처 결정을 그 맥락과 결과와 함께 기록하는 문서입니다.

> [!IMPORTANT]
> 이 자료를 중요한 시스템에서 사용하기 전에 직접 충분히 검토(실사)하세요.

목차:

- [아키텍처 의사결정 기록이란 무엇인가?](#아키텍처-의사결정-기록이란-무엇인가)
- [ADR 시작하는 방법](#adr-시작하는-방법)
- [도구로 ADR 시작하는 방법](#도구로-adr-시작하는-방법)
- [git으로 ADR 시작하는 방법](#git으로-adr-시작하는-방법)
- [ADR을 위한 Claude Code 스킬](#adr을-위한-claude-code-스킬)
- [파일 이름 규칙](#파일-이름-규칙)
- [좋은 ADR 작성을 위한 제안](#좋은-adr-작성을-위한-제안)
- [ADR 예제 템플릿](#adr-예제-템플릿)
- [ADR을 위한 팀워크 조언](#adr을-위한-팀워크-조언)
- [ADR을 위한 팀워크 질문](#adr을-위한-팀워크-질문)
- [ADR의 다음 단계 개념](#adr의-다음-단계-개념)
- [아키텍처 다이어그램, 뷰, 뷰포인트](#아키텍처-다이어그램-뷰-뷰포인트)
- [코드로 표현하는 의사결정의 적합도 함수](#코드로-표현하는-의사결정의-적합도-함수)
- [풀 리퀘스트를 위한 결정 가드레일](#풀-리퀘스트를-위한-결정-가드레일)
- [더 많은 정보](#더-많은-정보)

템플릿:

- [Jeff Tyree와 Art Akerman의 의사결정 기록 템플릿](템플릿/제프-타이리와-아트-아커먼의-의사결정-기록-템플릿/)
- [Michael Nygard의 의사결정 기록 템플릿](템플릿/마이클-나이가드의-의사결정-기록-템플릿/)
- [EdgeX의 의사결정 기록 템플릿](템플릿/edgex의-의사결정-기록-템플릿/)
- [arc42의 의사결정 기록 템플릿](템플릿/arc42의-의사결정-기록-템플릿/)
- [알렉산드리아 패턴을 위한 의사결정 기록 템플릿](템플릿/알렉산드리아-패턴을-위한-의사결정-기록-템플릿/)
- [비즈니스 케이스를 위한 의사결정 기록 템플릿](템플릿/비즈니스-케이스를-위한-의사결정-기록-템플릿/)
- [MADR 프로젝트의 의사결정 기록 템플릿](템플릿/madr-프로젝트의-의사결정-기록-템플릿/)
- [Planguage를 사용한 의사결정 기록 템플릿](템플릿/planguage를-사용한-의사결정-기록-템플릿/)
- [Paulo Merson의 결정 기록 템플릿](https://github.com/pmerson/ADR-template)
- [Olaf Zimmermann의 결정 기록 템플릿](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Gareth Morgan의 의사결정 기록 템플릿](템플릿/개러스-모건의-의사결정-기록-템플릿/)
- [GIG Cymru NHS Wales의 의사결정 기록 템플릿](템플릿/gig-cymru-nhs-wales의-의사결정-기록-템플릿/)
- [Ignacio Larrañaga의 중요한 기술 의사결정을 위한 의사결정 기록 템플릿](템플릿/중요한-기술-의사결정을-위한-의사결정-기록-템플릿/)

예제:

- [CSS 프레임워크](예시/css-프레임워크/)
- [환경 변수 설정](예시/환경-변수-설정/)
- [메트릭, 모니터, 알림](예시/메트릭-모니터-알림/)
- [Microsoft Azure DevOps](예시/마이크로소프트-애저-데브옵스/)
- [모노레포 대 멀티레포](예시/모노레포-대-멀티레포/)
- [프로그래밍 언어](예시/프로그래밍-언어/)
- [비밀 정보 저장](예시/비밀-정보-저장/)
- [타임스탬프 형식](예시/타임스탬프-형식/)
- [훨씬 더 많은 예제...](예시/)

## 아키텍처 의사결정 기록이란 무엇인가?

**아키텍처 의사결정 기록**(ADR)은 내려진 중요한 아키텍처 결정을 그 맥락 및 결과와 함께 담은 문서입니다.

**아키텍처 결정**(AD)은 중요한 요구사항을 다루는 소프트웨어 설계상의 선택입니다.

**아키텍처 결정 로그**(ADL)는 특정 프로젝트(또는 조직)를 위해 작성되고 유지되는 모든 ADR의 모음입니다.

**아키텍처상 중요한 요구사항**(ASR)은 소프트웨어 시스템의 아키텍처에 측정 가능한 영향을 미치는 요구사항입니다.

이 모든 것은 **아키텍처 지식 관리**(AKM)라는 주제에 속합니다.

이 문서의 목표는 ADR이 무엇인지, 어떻게 작성하는지, 더 많은 정보를 어디에서 찾을 수 있는지에 대한 빠른 개요를 제공하는 것입니다.

약어:

  * **AD**: 아키텍처 결정

  * **ADL**: 아키텍처 결정 로그

  * **ADR**: 아키텍처 의사결정 기록

  * **AKM**: 아키텍처 지식 관리

  * **ASR**: 아키텍처상 중요한 요구사항

## ADR 시작하는 방법

ADR을 시작하려면 다음 영역에 대해 팀원들과 이야기해 보십시오.

결정 식별:

  * AD는 얼마나 시급하고 얼마나 중요한가?

  * 지금 내려야 하는가, 아니면 더 많은 것이 알려질 때까지 기다릴 수 있는가?

  * 개인적 경험과 집단적 경험은 물론 인정받는 설계 방법과 관행도 결정 식별에 도움이 될 수 있습니다.

  * 이상적으로는 제품 할 일 목록을 보완하는 결정 할 일 목록을 유지하십시오.

의사결정:

  * 일반적인 기법과 소프트웨어 아키텍처에 특화된 기법을 포함하여 여러 의사결정 기법이 존재합니다. 예를 들어 다이얼로그 매핑이 있습니다.

  * 그룹 의사결정은 활발한 연구 주제입니다.

결정의 시행과 집행:

  * AD는 소프트웨어 설계에 사용되므로 시스템에 자금을 대고, 개발하고, 운영하는 이해관계자에게 전달되고 그들에게 수용되어야 합니다.

  * 아키텍처가 드러나는 코딩 스타일과 아키텍처 관련 사안 및 결정에 초점을 맞춘 코드 검토는 관련된 두 가지 관행입니다.

  * AD는 소프트웨어 진화 과정에서 소프트웨어 시스템을 현대화할 때에도 (재)고려되어야 합니다.

결정 공유(선택 사항):

  * 많은 AD가 프로젝트 간에 반복됩니다.

  * 따라서 과거 결정에 대한 경험은 좋은 것이든 나쁜 것이든 명시적인 지식 관리 전략을 사용할 때 가치 있는 재사용 가능한 자산이 될 수 있습니다.

결정 문서화:

  * 결정을 기록하기 위한 많은 템플릿과 도구가 있습니다.

  * 애자일 커뮤니티를 참조하십시오. 예: M. Nygard의 ADR.

  * 전통적인 소프트웨어 공학 및 아키텍처 설계 프로세스를 참조하십시오. 예: IBM UMF와 CapitalOne의 Tyree 및 Akerman이 제안한 표 레이아웃.

더 알아보기:

  * 위 단계는 Wikipedia의 [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision) 항목에서 가져온 것입니다

## 도구로 ADR 시작하는 방법

- [MySpec](https://myspec.dev) — 프로젝트 헌장, 기술 아키텍처, ADR을 깔끔한 Markdown으로 구조화하고 MCP로 제공하는 자동화된 명세 및 아키텍처 의사결정 플랫폼.

도구를 사용해 ADR을 시작하는 방법은 원하는 대로 선택할 수 있습니다.

예를 들어:

  * Google 드라이브와 온라인 편집을 좋아한다면 Google 문서나 Google 스프레드시트를 만들 수 있습니다.

  * git 같은 소스 코드 버전 관리를 좋아한다면 ADR마다 파일을 하나씩 만들 수 있습니다.

  * Atlassian Jira 같은 프로젝트 계획 도구를 좋아한다면 그 도구의 계획 트래커를 사용할 수 있습니다.

  * MediaWiki 같은 위키를 좋아한다면 ADR 위키를 만들 수 있습니다.

## git으로 ADR 시작하는 방법

git 버전 관리를 좋아한다면, 소스 코드가 있는 일반적인 소프트웨어 프로젝트에서 우리가 git으로 ADR을 시작하는 방법은 다음과 같습니다.

ADR 파일을 위한 디렉터리를 만듭니다:

```sh
$ mkdir adr
```

각 ADR마다 `database.txt` 같은 텍스트 파일을 만듭니다:

```sh
$ vi database.txt
```

ADR에는 원하는 내용을 무엇이든 작성하십시오. 아이디어는 이 저장소의 템플릿을 참조하십시오.

ADR을 git 저장소에 커밋합니다.

## ADR을 위한 Claude Code 스킬

이 저장소는 AI 코딩 에이전트가 이 프로젝트가 권장하는 방식으로 ADR을 작성하고 유지할 수 있도록 [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/) 아래에 두 개의 [Claude Code](https://claude.com/claude-code) 스킬을 제공합니다.

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — 어떤 프로젝트에서든 ADR을 쓰는 모든 사람을 위한 범용 스킬입니다. 결정에 ADR이 필요한지 판단하고, `adr/` 또는 `decisions/` 디렉터리를 만들고, 파일 이름을 정하고, 포함된 11개의 뼈대 중 템플릿을 고르고, 탄탄한 맥락/결정/결과 섹션을 쓰도록 돕습니다.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — 이 저장소의 관리자를 위한 스킬입니다. 저장소의 구조, README와 locales를 맞추는 관례, 새 템플릿·예제·도구 링크를 추가하는 정확한 단계를 문서화합니다.

스킬을 사용하려면 그 폴더를 작업 중인 저장소 루트의 `.claude/skills/`에(모든 프로젝트에서 쓰려면 `~/.claude/skills/`에) 복사한 다음, Claude Code에 ADR 작성이나 검토를 요청하세요.

## 파일 이름 규칙

일반 텍스트 파일로 ADR을 작성하기로 했다면 ADR 파일 이름 규칙을 직접 정해 두는 것이 좋습니다.

우리는 특정 형식을 가진 파일 이름 규칙을 사용하는 것을 선호합니다.

예시:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

우리의 파일 이름 규칙:

  * 이름은 현재 시제 명령형 동사구로 짓습니다. 이는 가독성을 높이고 우리의 커밋 메시지 형식과 맞습니다.

  * 이름은 소문자와 대시를 사용합니다(이 저장소와 동일). 이는 가독성과 시스템 사용성 사이의 균형입니다.

  * 확장자는 markdown입니다. 서식을 쉽게 적용하는 데 유용할 수 있습니다.

## 좋은 ADR 작성을 위한 제안

좋은 ADR의 특징:

* 근거: 해당 AD를 수행하는 이유를 설명합니다. 여기에는 맥락(아래 참조), 다양한 잠재적 선택지의 장단점, 기능 비교, 비용/편익 논의 등이 포함될 수 있습니다.

* 구체성: 각 ADR은 여러 AD가 아니라 하나의 AD에 관한 것이어야 합니다.

* 타임스탬프: ADR의 각 항목이 언제 작성되었는지 표시합니다. 이는 비용, 일정, 확장 등 시간이 지나면서 바뀔 수 있는 측면에서 특히 중요합니다.

* 불변성: ADR의 기존 정보를 변경하지 마십시오. 대신 새 정보를 추가하여 ADR을 수정하거나, 새 ADR을 만들어 ADR을 대체하십시오.

ADR의 좋은 “맥락” 섹션의 특징:

* 조직의 상황과 비즈니스 우선순위를 설명합니다.

* 팀의 사회적 구성과 기술 구성에 기반한 근거와 고려 사항을 포함합니다.

* 관련 있는 장단점을 포함하고, 필요와 목표에 부합하는 용어로 설명합니다.

ADR의 좋은 “결과” 섹션의 특징:

* 결정을 내린 결과로 무엇이 뒤따르는지 설명합니다. 여기에는 영향, 성과, 산출물, 후속 조치 등이 포함될 수 있습니다.

* 후속 ADR에 대한 정보를 포함합니다. 하나의 ADR이 더 많은 ADR의 필요성을 촉발하는 경우는 비교적 흔합니다. 예를 들어 한 ADR이 큰 포괄적 선택을 하면, 그것이 다시 더 작은 결정들의 필요를 낳는 경우입니다.

* 사후 검토 프로세스를 포함합니다. 팀이 각 ADR을 한 달 뒤에 검토하여 ADR 정보를 실제로 일어난 일과 비교하고, 이를 통해 배우고 성장하는 것이 일반적입니다.

새 ADR이 이전 ADR을 대체할 수 있습니다:

* 이전 ADR을 대체하거나 무효화하는 AD가 내려지면 새 ADR을 작성해야 합니다

## ADR 예제 템플릿

인터넷에서 수집한 ADR 예제 템플릿:

- [Michael Nygard의 ADR 템플릿](템플릿/마이클-나이가드의-의사결정-기록-템플릿/) (간단하고 인기 있음)

- [Jeff Tyree와 Art Akerman의 ADR 템플릿](템플릿/제프-타이리와-아트-아커먼의-의사결정-기록-템플릿/) (더 정교함)

- [Alexandrian 패턴을 위한 ADR 템플릿](템플릿/알렉산드리아-패턴을-위한-의사결정-기록-템플릿/) (맥락 세부 정보가 있는 간단한 형식)

- [비즈니스 케이스를 위한 ADR 템플릿](템플릿/비즈니스-케이스를-위한-의사결정-기록-템플릿/) (비용, SWOT, 더 많은 의견을 포함한 MBA 지향)

- [Markdown Any Decision Records(MADR) 프로젝트의 ADR 템플릿](템플릿/madr-프로젝트의-의사결정-기록-템플릿/) (간단한 버전과 정교한 버전이 있으며, 후자는 선택지와 그 장단점을 강조)

- [Planguage를 사용하는 ADR 템플릿](템플릿/planguage를-사용한-의사결정-기록-템플릿/) (품질 보증 지향)

- [Ignacio Larrañaga의 중요 기술 결정(ITD) 템플릿](템플릿/중요한-기술-의사결정을-위한-의사결정-기록-템플릿/) (간결하고 결정 우선이며 신속한 경영진 검토에 최적화)

## ADR을 위한 팀워크 조언

팀에서 결정 기록을 사용하는 것을 고려하고 있다면, 여러 팀과 함께 일하며 배운 조언을 소개합니다.

“무엇을” 강제하기보다 “왜”에 대해 함께 이야기함으로써 팀원들을 이끌 기회가 있습니다. 예를 들어 결정 기록은 팀이 더 똑똑하게 생각하고 더 잘 소통하는 방법입니다. 결정 기록이 사후에 강제되는 서류 작업 요건에 불과하다면 가치가 없습니다.

일부 팀은 약어인 “ADR”보다 “결정(decisions)”이라는 이름을 훨씬 선호합니다. 일부 팀이 디렉터리 이름으로 “decisions”를 사용하면 전구가 켜지는 듯한 일이 일어나고, 팀은 공급업체 결정, 계획 결정, 일정 결정 등 더 많은 정보를 그 디렉터리에 넣기 시작합니다. 이 모든 종류의 정보에 같은 템플릿을 쓸 수 있습니다. 우리는 사람들이 약어(“ADR”)보다 단어(“결정”)로 더 빨리 배우고, “기록(record)”이라는 단어를 빼면 진행 중인 작업 문서를 쓰려는 동기가 더 커지며, 또한 일부 개발자와 일부 관리자는 “아키텍처”라는 단어를 싫어한다고 가정합니다.

이론적으로는 불변성이 이상적입니다. 실제로는 우리 팀에서는 가변성이 더 잘 맞았습니다. 우리는 기존 ADR에 날짜 스탬프와 그 정보가 결정 이후에 들어왔다는 메모와 함께 새 정보를 삽입합니다. 이런 접근 방식은 우리 모두가 갱신할 수 있는 “살아 있는 문서”로 이어집니다. 전형적인 갱신은 새로운 팀원 덕분에, 새로운 제공 서비스 덕분에, 우리 사용의 실제 결과 덕분에, 또는 공급업체의 기능, 요금제, 라이선스 계약 같은 사후 제3자 변경 이후에 정보를 얻을 때 이루어집니다.

## ADR을 위한 팀워크 질문

### 누가 ADR을 작성할 수 있습니까?

특정 사람, 특정 역할, 특정 팀, 특정 부서 같은 영역을 고려하십시오. 또한 ADR을 의뢰할 수 있는 사람, 역할, 팀, 부서가 있는지도 고려하십시오. 즉 다른 사람이 작성할 ADR을 요청할 수 있는 경우입니다. 

답변 예시: 아키텍처 의사결정 기록 README 페이지를 읽은 우리 조직의 누구나 ADR을 제안할 수 있습니다. 즉 그 사람이 작성을 시작하고 팀과 공유할 수 있습니다.

### 무엇이 ADR을 제기하는 것을 정당화합니까?

조직 팀의 업무 방식, 소프트웨어 시스템 구조, 팀 간 조율, 장기 유지보수성, 외부 인터페이스, 누구에게 이익을 주고 싶은지 같은 영역을 고려하십시오. 

답변 예시: 우리는 미래의 개발자가 우리가 하는 일의 “이유”를 이해하기를 바랄 때 ADR을 작성하고자 합니다.

### 무엇이 ADR을 제기하지 않는 것을 정당화합니까?

아키텍처에 관한 것이 아닌 결정, 위험이 최소이거나 독립적이거나 개발자 한 명에 한정되는 등 사소한 결정, 표준, 정책, 문서 등으로 이미 다른 곳에서 완전히 다뤄지는 결정, 또는 임시방편, 개념 증명, 실험처럼 일시적인 결정 같은 영역을 고려하십시오. 

답변 예시: 결정이 범위, 시간, 위험, 비용 면에서 제한적이거나 이미 다른 곳에서 다뤄지는 경우 ADR을 생략하고자 합니다.

### ADR의 수명 주기는 무엇입니까?

작성 프로세스, 조사 프로세스, 의사결정 프로세스, 구현 프로세스, 폐기 프로세스 같은 영역을 고려하십시오. ADR 수명 주기를 시간에 따라 어떻게 추적할지, 예를 들어 ADR을 한 상태에서 다음 상태로 어떻게 옮길지, 그리고 이를 이해관계자에게 어떻게 알릴지를 고려하십시오. 

답변 예시: 우리는 ADR이 다섯 가지 수명 주기 단계를 갖기를 바랍니다: 시작(Initiating) → 조사(Researching) → 평가(Evaluating) → 구현(Implementing) → 유지(Maintaining) → 폐기(Sunsetting).

### ADR의 수명 주기 단계에 대한 기준은 무엇입니까?

ADR의 수락 기준 같은 영역을 고려하십시오. 즉 한 수명 주기 단계에서 다음 단계로 넘어갈 만큼 충분히 좋다는 것을 어떻게 알 수 있습니까? 문제가 명확하게 서술되어 있습니까? 대안이 검토되었습니까? 트레이드오프가 충분히 이해되고 문서화되었습니까?
모든 관련 맥락이 갖춰져 있습니까? 모든 관련 이해관계자가 참여했습니까? 모든 피드백이 반영되었습니까? 

답변 예시: 우리는 활동 팀이 1) 조사를 완료하고, 2) 평가를 완료하고, 3) 의견 요청과 일주일의 시간 제한을 두고 ADR 제안을 이해관계자에게 게시하고, 4) 모든 이해관계자 의견이 반영되고 처리되었을 때 이해관계자가 ADR에 대해 투표하기를 바랍니다.

### 어떤 역할과 책임이 ADR과 상호작용합니까?

제안자, 조사자, 평가자, 검토자, 승인자, 유지 관리자 같은 역할을 고려하십시오. 이해관계자와의 소통, 기대 충족 보장, 웹사이트나 인트라넷에서의 공유, 그리고 특히 관련 변경이 있을 때 작업을 주기적으로 검토하는 것 같은 책임을 고려하십시오.

답변 예시: 우리는 각 ADR에 항상 주 담당자, 부 담당자, 책임 팀이 있기를 바랍니다. 이들은 소통, 게시, 유지 관리, 최소 연 1회 주기적 검토, 필요에 따른 최종 폐기를 책임집니다.

### 거버넌스는 ADR과 어떻게 상호작용합니까?

조직의 업무 방식, 법률 측면이나 인사 측면 같은 특별한 규정 준수 요구, 합의 대 갈등 대 에스컬레이션을 어떻게 다루고 싶은지 같은 영역을 고려하십시오. ADR과 관련하여 승인하거나, 투표하거나, 거부권을 행사할 수 있는 것처럼 다른 사람보다 더 큰 영향력을 가질 수 있는 영역, 사람, 팀이 있습니까?

답변 예시: ADR의 거버넌스는 다음 우선순위 순서입니다: CEO, CTO, CLO, ADR을 구현하는 팀, ADD에 대해 가장 지식이 풍부한 팀 내 전문가. ADR에 기술되지 않는 한 그 누구도 거버넌스를 갖지 않습니다. 

### 어떤 원칙이 ADR과 상호작용합니까?

빠르게 움직일지 느리게 움직일지, 결정 합의 대 결정 갈등, 위험 선호 대 안전 선호, 공개 논의 대 비공개 논의 같은 조직의 업무 방식을 포함하는 영역을 고려하십시오.

답변 예시: 우리는 행동 편향(bias for action), 반대하되 헌신하기(disagree-and-commit), 쉽게 되돌릴 수 있고 쉽게 격리할 수 있는 결정에는 70% 추정이면 충분하다는 원칙, 그리고 우리 조직의 기밀 유지 계약에 기술된 기밀 정보를 제외한 공개적인 업무 방식이라는 리더십 원칙을 사용합니다.

## ADR의 다음 단계 개념

[Arc42](https://arc42.org/)는 두 가지 질문에 실용적으로 답하며 필요에 맞게 조정할 수 있습니다. 아키텍처에 대해 무엇을 문서화/전달해야 할까요? 어떻게 문서화/전달해야 할까요? Arc42에는 아키텍처 결정 기록과 함께 목표, 제약, 맥락, 품질, 위험 등에 대한 안내가 포함됩니다.

[C4 모델](https://c4model.com/)은 소프트웨어 아키텍처를 다이어그램으로 그리는, 배우기 쉽고 개발자 친화적인 접근법입니다. C4는 맥락, 컨테이너, 컴포넌트, 코드를 위한 계층적 다이어그램과 시스템 환경, 동적 동작, 배포를 위한 보조 다이어그램으로 구성됩니다.

## 아키텍처 다이어그램, 뷰, 뷰포인트

아키텍처 다이어그램을 "아키텍처 뷰"라고 합니다.

"아키텍처 뷰"는 "아키텍처 뷰포인트"의 한 사례입니다.

"아키텍처 뷰포인트"는 특정한 관심사를 가진 특정 독자를 염두에 둡니다.

아키텍처 뷰포인트, 뷰, 다이어그램의 예:

- 비즈니스 역량

- 상위 수준 비즈니스 프로세스

- [가치 흐름](https://en.wikipedia.org/wiki/Value_stream)

- 애플리케이션 컴포넌트에 매핑된 소프트웨어 기능

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) 컨텍스트 다이어그램 (TO-BE / AS-IS)

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) 컨테이너 다이어그램 (TO-BE / AS-IS)

- [개체-관계 다이어그램](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) 데이터 개체를 애플리케이션 컴포넌트에 매핑하기 위해

- [시퀀스 다이어그램](https://en.wikipedia.org/wiki/Sequence_diagram) 시스템 내부와 통합에서의 기능 흐름을 설명하기 위해

- [비즈니스 프로세스 모델 및 표기법](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) 애플리케이션 컴포넌트 간 데이터 흐름을 설명하는 다이어그램

- [비즈니스 프로세스 모델 및 표기법](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) 비즈니스 프로세스/사용자 시나리오를 설명하는 다이어그램

- [ID 및 액세스 관리](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM) 다이어그램

- [역할 기반 액세스 제어](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) 애플리케이션 컴포넌트별 역할을 보여 주는 다이어그램

- [속성 기반 액세스 제어](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) 애플리케이션 컴포넌트별 속성을 보여 주는 다이어그램

- 프라이버시 다이어그램

관련 다이어그램:

- 유스 케이스 다이어그램은 경영진/고객에게 유스 케이스를 보여 줍니다. 이는 요구사항보다 먼저 오며, 요구사항은 소프트웨어 아키텍처보다 먼저 옵니다.

- 배포 다이어그램은 소프트웨어 컴포넌트가 배포되는 물리적 하드웨어/컴퓨터를 보여 줍니다.
- 데이터 흐름 다이어그램은 데이터가 시스템을 통해 어떻게 이동하고 변환되는지 보여 줍니다.
- 시퀀스 다이어그램은 HTTP 같은 프로토콜이 시간 축에서 어떻게 동작하는지 보여 주는 데 사용합니다.

- 액티비티 다이어그램은 NPC AI처럼 소프트웨어 시스템이 수행하는 활동의 워크플로를 나타냅니다.

## 코드로 표현하는 의사결정의 적합도 함수

적합도 함수(fitness function)는 프로그래밍 코드로 작성된 객관적이고 자동화된 검사로, 결정이 유지되고 있는지를 검증합니다.

- 적합도 함수는 결정을 테스트 가능하고 보증 가능하게 만듭니다.

- 결정을 위한 적합도 함수는 품질 보증, 규제 프로세스, 거버넌스 목표에 큰 도움이 될 수 있습니다.

### 적합도 함수와 결정이 연결되는 방식

결정 기록은 결정을 문서화하고, 적합도 함수는 그 결정을 보증합니다.

- 결정 예시: 감사 요구사항을 위해 이벤트 소싱을 사용한다.

- 적합도 함수 예시: 지속적 통합 서버를 사용하여 모든 상태 변경이 이벤트를 생성해야 한다는 것을 테스트한다.

### 적합도 함수가 결정에 도움이 되는 이유

객관적인 측정: 적합도 함수는 통과하거나 실패하므로 작업이 가시적이고 명확합니다.

지속적인 사용: 적합도 함수는 살아 있는 규칙이며 모든 커밋과 빌드에서 실행됩니다.

리팩터링에 대한 자신감: 적합도 함수는 결정 규칙의 오류를 자동으로 잡아냅니다.

확장 가능한 거버넌스: 적합도 함수는 병목을 만들지 않고 표준을 보증합니다.

### 적합도 함수가 AI를 사용할 수 있나요?

적합도 함수는 계획, 코드, 스키마, API 등 작업에 대한 질문을 함으로써
결정을 위해 AI LLM을 활용할 수 있습니다:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### 아키텍처 단위 테스트

[ArchUnit](https://www.archunit.org/): 일반적인 Java 단위 테스트 프레임워크를 사용하여 Java 코드의 아키텍처 규칙을 검사합니다.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): Jest, Vitest, Jasmine 등을 사용하여 TypeScript 코드와 JavaScript 코드의 아키텍처 규칙을 검사합니다.

## 풀 리퀘스트를 위한 결정 가드레일

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)은
적절한 순간, 즉 개발자가 그 결정이 다루는 코드를 실제로 수정하는 때에
적절한 결정 기록을 자동으로 보여 줍니다. 병합 전에 개발자가 문서 폴더를 읽기를 바라는 대신,
관련 맥락이 풀 리퀘스트에 곧바로 나타납니다.

이는 모든 종류의 결정 기록에서 작동합니다. 아키텍처 결정, 데이터 결정, 규정 준수 결정, 임상 및 의료 결정, 보안 결정 등입니다.

모든 CI 시스템(GitLab, Jenkins, CircleCI)과 프리커밋 훅으로 작동합니다.
오픈 소스. MIT 라이선스.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates)는 감시 대상 코드 경로가
아키텍처 결정 기록의 추가나 갱신 없이 변경되면 풀 리퀘스트를 실패시키는 GitHub
Action입니다. 면제는 명시적입니다. 이유가 적힌 `ADR-Exempt:` 줄은 게이트를 통과시키고 작업 요약에 기록됩니다. 템플릿에 구애받지 않으며 의존성이 없습니다. 오픈 소스. MIT 라이선스.

## 더 많은 정보

소개:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

템플릿:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

심층 자료:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - 무료 월간 소프트웨어 아키텍처 강의

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

도구:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

기업별 안내:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

예제:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

동영상:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

팟캐스트:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

도서:

- [Software Architecture Metrics: Case Studies to Improve the Quality of Your Architecture - by Christian Ciceri, Dave Farley, Neal Ford, Andrew Harmel-Law, Michael Keeling and Carola Lilienthal](https://www.amazon.com/Software-Architecture-Metrics-Christian-Ciceri-ebook/dp/B0B1NZ8Z5V)

- [Software Systems Architecture: Working With Stakeholders Using Viewpoints and Perspectives - by Nick Rozanski and Eoin Woods](https://www.amazon.com/Software-Systems-Architecture-Stakeholders-Perspectives/dp/032171833X)

- [Software Architecture in Practice (SEI Series in Software Engineering)](https://www.amazon.com/Software-Architecture-Practice-SEI-Engineering-ebook/dp/B094CPJ96B)

- [Documenting Software Architectures: Views and Beyond (SEI Series in Software Engineering)](https://www.amazon.com/Documenting-Software-Architectures-Beyond-Engineering-ebook/dp/B0046XS3RO)

- [The Software Architect Elevator: Redefining the Architect's Role in the Digital Enterprise](https://www.amazon.com/Software-Architect-Elevator-Redefining-Architects-ebook/dp/B086WQ9XL1)

- [Fundamentals of Software Architecture: An Engineering Approach - by Mark Richards and Neal Ford](https://www.amazon.com/Fundamentals-Software-Architecture-Engineering-Approach-ebook/dp/B0849MPK73)

- [Building Evolutionary Architectures - by Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage](https://www.amazon.com/Building-Evolutionary-Architectures-Neal-Ford-ebook/dp/B0BN4T1P27?crid=37FA31IFLAS0Z)

- [Foundations of Decision Analysis by Ronald Howard and Ali Abbas](https://www.amazon.com/Foundations-Decision-Analysis-Ronald-Howard-ebook/dp/B00SZECJTI?crid=14BK5SDP76UN6)

- [Head First Software Architecture - by Raju Gandhi, Neal Ford and Mark Richards](https://www.amazon.com/Head-First-Software-Architecture-Architectural-ebook/dp/B0CW1JMNF2)

- [Communication Patterns: A Guide for Developers and Architects - by Jacqui Read](https://www.amazon.com/Communication-Patterns-Guide-Developers-Architects/dp/1098140540)

함께 보기:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - 명시적인 추론, 가정, 인지 상태, 상충 관계와 함께 결정을 표현하기 위한 벤더 중립적이고 기계가 읽을 수 있는 YAML/JSON 형식. 결정 문서에 구조화되고 검증 가능한 추론을 더해 ADR을 보완합니다.
