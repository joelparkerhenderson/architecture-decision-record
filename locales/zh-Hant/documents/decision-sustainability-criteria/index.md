# 決策永續性準則

<https://www.infoq.com/articles/sustainable-architectural-design-decisions/>

為了詳細定義決策永續性（Decision Sustainability），我們推導出五項關鍵準則。

## 策略性（Strategic）

在決策制定過程中，考量策略性後果的人應思考諸如決策的長期影響——例如未來的營運與維護成本。

## 可衡量且可管理（Measurable and Manageable）

你可以根據客觀準則（理想情況下為數值準則，例如品質屬性情境與工作坊所倡導的方式）來衡量和評估決策的成果。擷取所有細粒度的決策是不可能的，因此架構師必須將決策的粒度限制在特定的詳細程度（例如建立設計類別）。這將產生一組更具永續性的決策，以及更少的可追溯性連結。此外，限制決策之間的依賴數量可減少變更的漣漪效應（Ripple Effect）。

## 可達成且務實（Achievable and Realistic）

將解決方案與問題適配的理由應以務實的方式選擇，並明確說明。例如，架構師可以表明他們已注意避免過度工程或工程不足（即應採用「足夠好」的方法）。

## 植根於需求（Rooted in Requirements）

決策制定應立基於領域專屬的架構經驗與脈絡。它應考量公司環境以及專案需求與限制，包括開發團隊目前的技能、培訓預算與流程。

## 超越時間（Timeless）

決策應基於不太可能很快過時的經驗與知識。例如，架構師可以選擇平台中立的架構模式（Architectural Patterns）或策略（Tactics）。
