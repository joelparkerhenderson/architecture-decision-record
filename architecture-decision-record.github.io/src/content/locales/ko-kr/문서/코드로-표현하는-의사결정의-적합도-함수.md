# 코드로 표현하는 의사결정의 적합도 함수

적합도 함수(fitness function)는 프로그래밍 코드로 작성된 객관적이고 자동화된 검사로, 결정이 유지되고 있는지를 검증합니다.

- 적합도 함수는 결정을 테스트 가능하고 보증 가능하게 만듭니다.

- 결정을 위한 적합도 함수는 품질 보증, 규제 프로세스, 거버넌스 목표에 큰 도움이 될 수 있습니다.

## 적합도 함수와 결정이 연결되는 방식

결정 기록은 결정을 문서화하고, 적합도 함수는 그 결정을 보증합니다.

- 결정 예시: 감사 요구사항을 위해 이벤트 소싱을 사용한다.

- 적합도 함수 예시: 지속적 통합 서버를 사용하여 모든 상태 변경이 이벤트를 생성해야 한다는 것을 테스트한다.

## 적합도 함수가 결정에 도움이 되는 이유

객관적인 측정: 적합도 함수는 통과하거나 실패하므로 작업이 가시적이고 명확합니다.

지속적인 사용: 적합도 함수는 살아 있는 규칙이며 모든 커밋과 빌드에서 실행됩니다.

리팩터링에 대한 자신감: 적합도 함수는 결정 규칙의 오류를 자동으로 잡아냅니다.

확장 가능한 거버넌스: 적합도 함수는 병목을 만들지 않고 표준을 보증합니다.

## 적합도 함수가 AI를 사용할 수 있나요?

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

## 아키텍처 단위 테스트

[ArchUnit](https://www.archunit.org/): 일반적인 Java 단위 테스트 프레임워크를 사용하여 Java 코드의 아키텍처 규칙을 검사합니다.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): Jest, Vitest, Jasmine 등을 사용하여 TypeScript 코드와 JavaScript 코드의 아키텍처 규칙을 검사합니다.
