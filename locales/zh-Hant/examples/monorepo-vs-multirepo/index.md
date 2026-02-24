# 單一儲存庫（Monorepo）vs 多儲存庫（Multirepo）

目錄：

* [摘要](#摘要)
  * [議題](#議題)
  * [決策](#決策)
  * [狀態](#狀態)
* [細節](#細節)
  * [假設](#假設)
  * [限制條件](#限制條件)
  * [立場](#立場)
  * [論點](#論點)
  * [影響](#影響)
* [相關內容](#相關內容)
  * [相關決策](#相關決策)
  * [相關需求](#相關需求)
  * [相關產出物](#相關產出物)
  * [相關原則](#相關原則)
* [備註](#備註)


## 摘要


### 議題

我們的專案涉及開發三大類軟體：

  * 前端 GUI
  * 中介軟體服務（Middleware Services）
  * 後端伺服器

在開發過程中，我們的原始碼管理（SCM）版本控制系統（VCS）使用 git。

我們需要決定如何使用 git 來組織我們的程式碼。

最上層的選擇是採用「單一儲存庫（monorepo）」、「多儲存庫（polyrepo）」或「混合式（hybrid）」：

  * Monorepo 意味著我們將所有部分放入一個大型儲存庫
  * Polyrepo 意味著我們將每個部分放在各自的儲存庫
  * Hybrid 意味著混合使用 monorepo 和 polyrepo

更多資訊請參閱 https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### 決策

當組織/團隊/專案規模相對較小，且快速迭代的優先順序高於維持穩定性時，採用 Monorepo。

當組織/團隊/專案規模相對較大，且維持穩定性的優先順序高於快速迭代時，採用 Polyrepo。


### 狀態

已決定。若有新的工具可用於管理 monorepo 和/或 polyrepo，我們願意重新評估。


## 細節


### 假設

我們正在開發的所有程式碼都是為了一個組織的產品，而非面向一般大眾。也就是說，該券商（Broker-Dealer）並不打算讓一般大眾的志願開發者參與。


### 限制條件

限制條件在 https://github.com/joelparkerhenderson/monorepo-vs-polyrepo 中有詳細記錄。


### 立場

我們考慮了 Google、Facebook 等公司風格的 monorepo。我們認為任何 monorepo 的擴展性問題都還很遙遠，到那時我們將能夠借鏡 Google 和 Facebook 的做法。

我們考慮了典型 Git 開源專案風格的 polyrepo，例如 Google Android、Facebook React 等。我們認為這些是一般大眾參與（例如世界上任何人都可以貢獻程式碼）和獨立可用性（例如該專案可以獨立使用，不需要其他元件）的最佳選擇。


### 論點

當組織/團隊/專案規模相對較小時，我們選擇 monorepo，因為快速迭代的優先順序顯著高於維持穩定性。

當組織/團隊/專案規模相對較大時，我們選擇 polyrepo，因為維持穩定性的優先順序顯著高於快速迭代。


### 影響

如果已有 CI+CD 管線，我們可能需要調整它以支援在一個儲存庫中測試多個專案。

Monorepo 的 CI+CD 完整建置可能需要更多時間，因為 CI+CD 可能會建置 monorepo 中的所有專案。

如果組織/團隊/專案成長，monorepo 將面臨擴展性問題。

Monorepo 的擴展性問題可能使轉移到 polyrepo 變得越來越有價值。

從 monorepo 轉移到 polyrepo 是一項重大的 DevOps 任務，需要進行規劃、管理和程式開發。


## 相關內容


### 相關決策

我們將針對管理 monorepo（例如 Google Bazel）和 polyrepo（例如 Lyft Refactorator）的相關工具做出決策。


### 相關需求

我們需要開發能與 git 良好配合的 CI+CD 管線。


### 相關產出物

我們預期儲存庫的組織結構會有與佈建（provisioning）、組態管理（configuration management）、測試及類似 DevOps 領域相關的產出物。


### 相關原則

易於逆轉。如果 monorepo 在實務上行不通，或不被管理層接受，轉換為 polyrepo 是簡單的。

客戶至上（Customer Obsession）。我們重視讓專案盡快交到客戶手中，我們相信 monorepo 能比 polyrepo 更快地達到這個目標，並幫助我們更快速地迭代。

格局要大（Think Big）。Google 和 Facebook 都是 monorepo 相較於 polyrepo 的強力支持者，因為所有核心產品可以一起開發/測試/部署。


## 備註

在此加入任何備註。
