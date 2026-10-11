# 중요한 기술 의사결정(ITD)을 위한 의사결정 기록 템플릿

이것은
[ITDs: a lean ADR for executive technical decision-making at scale - Ignacio Larrañaga](https://ignaciolarranaga.medium.com/itds-a-lean-adr-for-executive-technical-decision-making-at-scale-e18bb3f6a563)
에서 설명하는 중요한 기술 의사결정(Important Technical Decisions, ITD) 템플릿입니다.

ITD는 속도, 명확성, 경영진 검증에 최적화된 ADR의 집중된 진화형입니다. ADR이
무엇이 결정되었는지를 문서화한다면, ITD는 결정 자체를 검토 가능하게 만드는 린하고
결정 우선적인 산출물이어서 이해관계자가 빠르게 훑어보고 쉽게 이의를 제기할 수
있습니다. ITD는 모델, 라이브러리, CI/CD 전략을 선택하는 것처럼 엄밀히 아키텍처에
관한 것이 아닌 기술적 결정에 적합합니다.

각 ITD 파일에 다음 섹션을 작성하십시오:

# 제목

주제에 대한 설명이 아니라 결정 자체를 서술하십시오.
예를 들어 “온디바이스 번역에 Qwen2.5 1.5B Instruct를 사용한다”.

## 문제

우리가 해결하려는 것을 서술하는 한 문장.

## 고려한 선택지

검토 대상이었던 대안들이며, 선택된 선택지는 **굵게** 표시합니다.

## 근거

선택으로 이어진 결정적인 요인만 적고, 모든 장단점을 망라한 목록은
쓰지 않습니다.

## 비고

선택 사항. 제약, 가정, 링크처럼 기록할 가치가 있는 추가 맥락.
