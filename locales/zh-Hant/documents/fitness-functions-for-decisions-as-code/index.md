# 適應度函數：以程式碼實現決策

適應度函數（Fitness Functions）是客觀的自動化檢查，以程式碼撰寫，用來驗證決策是否被持續遵守。

- 適應度函數使決策具備可測試性與可驗證性。

- 決策的適應度函數能大幅協助品質保證、法規流程與治理目標。

## 適應度函數如何與決策連結

決策記錄（Decision Record）記載決策內容，而適應度函數則確保決策被落實。

- 決策範例：我們使用事件溯源（Event Sourcing）來滿足稽核需求。

- 適應度函數範例：我們使用持續整合伺服器來測試所有狀態變更必須產生事件。

## 為什麼適應度函數有助於決策

客觀衡量：適應度函數只有通過或失敗，因此工作成果清晰可見。

持續運用：適應度函數是你的活規則，在每次提交與建置時執行。

安心重構：適應度函數能自動捕捉違反決策規則的錯誤。

可擴展的治理：適應度函數在不造成瓶頸的情況下確保標準被遵守。

## 適應度函數能否運用 AI？

適應度函數可以利用 AI LLM 來評估決策，針對你的工作提出問題，
例如你的計畫、程式碼、綱要（Schema）、API 等：

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

## 架構單元測試（Architecture Unit Testing）

[ArchUnit](https://www.archunit.org/)：使用任何標準 Java 單元測試框架來檢查 Java 程式碼的架構規則。

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS)：使用 Jest、Vitest、Jasmine 等來檢查 TypeScript 及 JavaScript 程式碼的架構規則。
