# [000] 제목
*쉬운 참조와 분류를 위해 각 ADR에 번호를 부여하십시오* \
*참고: 기울임꼴 텍스트는 모두 힌트이므로 실제 사용 시 제거해야 합니다*

## 상태 - DRAFT / ACTIVE /  DEPRECATED by [000] / SUPERSEDES [000]

## 맥락
*이 ADR이 다루려는 문제와 그 문제가 존재하는 이유를 간략히 설명하십시오.*

## 결정된 접근 방식
*내려졌거나 내려질 아키텍처상 중요한 결정을 상세히 기술하고, 그것이 맥락 섹션에 개략된 문제를 어떻게 해결하는지 설명하십시오.*

## 결과
*이 결정이 시스템의 아키텍처 특성과 기능 요구사항에 어떤 영향을 미칩니까?*

## 거버넌스
*이 결정의 결과는 어떻게 모니터링됩니까?* \
*이 결정에 대한 준수는 어떻게 보장됩니까?*

## 선택지 분석
*해당되는 경우, 이 문서의 결정에 도달하기 위해 수행된 트레이드오프 분석을 포함하거나 링크하십시오.*

### 범례
*선택 사항: 이해관계자가 긍정적 및 부정적 트레이드오프를 빠르게 파악하는 데 도움이 되는 시각적 보조 수단을 제공하십시오. 예를 들어 긍정 또는 부정 접두사가 붙은 간단한 신호등 강조 표시.*

<span style="background-color:#4bce97; color:black;">녹색</span> 배경은 적합도가 좋음을 나타내며, <span style="background-color:#f1c232; color:black;">황색</span>을 거치며 나빠지고, <span style="background-color:#e06666; color:black;">적색</span>이 가장 나쁜 적합도입니다. \
\+ 는 긍정적인 영향을 주는 의견을 나타냅니다 \
\- 는 부정적인 영향을 주는 의견을 나타냅니다

### 상위 수준 개요
*각 선택지가 문제 맥락에 얼마나 잘 맞는지 한눈에 보여 주십시오.*

<table>
  <thead>
    <tr>
      <th>요약</th>
      <th>선택지 1</th>
      <th>선택지 2</th>
      <th>선택지 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>구현 용이성</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
          + 매우 쉬움
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - 까다로움
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - 전문 지식이 필요한 대규모 구현
        </span>
      </td>
    </tr>
    <tr>
      <td><i>일정</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + 매우 빠름
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - 꽤 느림
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - 매우 느림
        </span>
      </td>
    </tr>
    <tr>
      <td><i>전략적 가치</i></td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - 전략적 가치 없음, 순수하게 전술적
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            + 고객 온보딩 경험을 약간 개선
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + 다가오는 합병에 이상적
        </span>
      </td>
    </tr>
  </tbody>
</table>

### 기능 요구사항
*각 가능한 선택지가 원하는 기능 요구사항에 얼마나 잘 맞습니까?*

<table>
  <thead>
    <tr>
      <th>시나리오</th>
      <th><i>선택지 1</i></th>
      <th><i>선택지 2</i></th>
      <th><i>선택지 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>시나리오 1</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>시나리오 2</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>시나리오 3</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*선택 사항: 알려진 향후 시나리오를 다루기 위해 행을 추가하거나 다른 표를 추가하십시오.*

### 비기능 요구사항
*각 가능한 선택지가 원하는 아키텍처 특성에 얼마나 잘 맞습니까?
참고: ‘아키텍처 특성’이 더 적절한 제목이지만, 비즈니스 도메인에 익숙한 용어로 조정하십시오.*

<table>
  <thead>
    <tr>
      <th>아키텍처 </br> 특성</th>
      <th><i>선택지 1</i></th>
      <th><i>선택지 2</i></th>
      <th><i>선택지 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>확장성</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>성능</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>가용성</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*선택 사항: 비즈니스/제품과 관련된 아키텍처 특성의 정의를 추가하거나 링크하십시오.*
