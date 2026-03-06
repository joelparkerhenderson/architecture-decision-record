# Microsoft Azure DevOps

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
* [相關資訊](#相關資訊)
  * [相關決策](#相關決策)
  * [相關需求](#相關需求)
  * [相關產出物](#相關產出物)
  * [相關原則](#相關原則)
* [備註](#備註)
  * [Microsoft DevOps CI：一次不滿意的歷程](#microsoft-devops-ci一次不滿意的歷程)
  * [Hacker News 討論重點](#hacker-news-討論重點)
  * [Windows Development MVP](#windows-development-mvp)
  * [Edward Thomson（Azure PM）摘要](#edward-thomsonazure-pm摘要)


## 摘要


### 議題

我們希望使用 DevOps 來建置、整合、部署和託管我們的專案。我們正在考慮 Microsoft Azure DevOps。

  * 我們希望開發者體驗快速且可靠，包括 DevOps 的設置（例如配置）以及持續使用（例如快速的建置時間）。

  * 我們希望考慮整體採用 Microsoft Azure 來託管專案的應用程式、資料庫等。


### 決策

決定不採用 Microsoft Azure DevOps。


### 狀態

已決定。若有重要的新資訊出現，願意重新評估。


## 細節


### 假設

所有常見的 DevOps 假設，例如《Accelerate》一書中提到的。

  * 快速建置是重要的助力。這能加速回饋循環。

  * 我們可以從替代供應商替換組件，例如我們可能想要自帶更高速的建置伺服器，或使用我們自己選擇的版本控制系統，或與自行託管的持續整合伺服器協作。

  * 流暢的可用性是重要的助力，有利於開發者體驗，進而影響一致性、清晰度、安全性和學習曲線等細微方面。

  * 當任何東西出問題或有問題時，我們希望有有效的方式來回報問題。這對於任何與安全相關的問題尤為重要。


### 限制條件

無已知限制。Azure 已發布承諾與外部工具良好配合。


### 立場

我們考慮使用 Microsoft Azure DevOps 與現有的 AWS 進行比較。

我們實驗了 Azure DevOps、Azure Pipelines、Azure Repo，以及透過 Terraform 啟動 Azure 新伺服器。

我們實驗了向 Microsoft 代表尋求支援。

我們從部落格和 Hacker News 上的同行那裡蒐集資訊。


### 論點

Azure DevOps 宣傳了一套出色的產品，但它們名不符實，而且它們之間的協作不佳，支援也很差。

我們的第一手經驗：

  * Azure 的設置是各種 UI 的混亂組合，有些與 Microsoft 帳號重疊，有些則不會。例如，有 Azure 登入、Microsoft.com 登入、Live.com 登入等，所有這些同時在運作。

  * 我們在設置過程中遇到了一個小安全問題，但找不到解決方案。我們嘗試了多種方式向多位 Microsoft 代表回報，但沒有成功。我們成功地向 Microsoft 安全團隊報告了此問題，對方回覆不予修復。

  * 文件經常不是錯誤就是過時。至少部分原因是 Microsoft 的搜尋引擎不佳，部分原因是 SEO 不足。

  * Terraform 設置有良好的文件記錄，且能正常運作。然而，與 AWS 相比，Terraform 支援較弱，因為 Microsoft 正在與供應商建立商業關係，以進行鏈式透傳（Chain-Through）的 Terraform 設置範例。

我們的同行經驗：

  * 在我們自己的獨立評估之後，我們尋找了同行經驗。我們發現的結果證實了我們的經歷。

  * 同行回報了建置時間方面的額外問題，以及自帶建置伺服器（Bring-Your-Own-Build Server）的問題。這些問題比 UI 問題嚴重得多，因為執行建置是建置管線（Build Pipeline）的核心目的，而我們預計每天要執行多次。

  * 我們發現 Azure 團隊成員在討論區的參與度很高。對此向 Microsoft 致敬。我們對 Edward Thomson（Azure PM 和程式設計師）特別印象深刻，因為他的參與度、直接和技術解釋。


### 影響

選擇 Microsoft Azure DevOps 在時間和成本上可能比不選 Azure 貴約 3 倍。


## 相關資訊


### 相關決策

如果我們選擇 Azure DevOps，有許多相關的產品，包括 Azure Repo、Azure Pipeline 等。我們認為，如果選擇 Azure DevOps，這可能會使我們更容易使用更多 Azure 功能，或者可能使我們更難使用其他供應商的功能。

我們相信 Microsoft 在開發者體驗方面取得了巨大進步，我們看到 Microsoft 大量收購開發者工具（例如 GitHub）和依賴項（例如 Citus）。

如果我們選擇 Azure DevOps，那麼我們可能想要優先選擇 Microsoft 收購的產品，同時我們也可能需要更加謹慎地評估這些收購產品，因為可能存在排斥反應（Tissue-Rejection），例如員工流失風險。


### 相關需求

我們希望建置時間非常快。我們願意為此支付高額溢價。這是因為我們希望快速迭代。

我們希望可靠性非常高。我們願意為此支付高額溢價。這是因為我們正在測試高價值的使用案例，包括金融交易、機密交易等。

我們的前 4 名 DevOps KPI 包括平均恢復時間（Mean Time to Recovery），這需要快速建置和高可靠性。


### 相關產出物

我們希望建置系統能輸出適合在其他系統中使用的產出物（Artifact），例如 Artifactory。


### 相關原則

容易復原（Easily Reversible）。我們可以將 Azure DevOps 的評估與現有的 AWS 並行進行。


## 備註


### Microsoft DevOps CI：一次不滿意的歷程

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

部落格文章。

「身為軟體開發者，我深知快速且便宜地建構高品質產品有多困難。這是一門藝術，有時我們做對了，有時則退化成類似 Obama 時代醫療保健政府網站的東西。我們對最終產品的控制程度各不相同，失敗的責任經常落在決策層級中錯誤的人身上。Microsoft 的 Azure DevOps（前身為 Visual Studio Team Services），儘管明顯出於好意，卻是錯誤決策和拙劣執行的完美風暴。」


### Hacker News 討論重點

https://news.ycombinator.com/item?id=18983586

「我們在工作中大量使用 Azure DevOps，在使用過 GitHub、GitLab、自行託管解決方案、Jenkins、TeamCity 之後... Azure DevOps 排名墊底。」

「UI 到處都笨重得可怕。對我來說最糟糕的是 Pull Request。與人在 Pull Request 上協作非常困難。我甚至無法指出『某個』特定問題——對我們來說它到處都是壞的。」

「Azure DevOps 是我想要喜歡的東西。UI 不斷變化，但不修復那些存在已久的底層 Bug。」

「工具之間整合不佳，UI 非常慢，沒有為我常用的儲存庫提供活躍的 Pull Request、建置、發布等的儀表板檢視。建置/部署時間慢得離譜。」

「我們也嘗試使用 Azure Boards（工作項目、看板、待辦清單等）。哎。它是一堆脫節想法的 UI 大雜燴。他們沒有把一件事做好，而是把幾十件事都做得很糟。」


### Windows Development MVP

Windows Development MVP 在此。我覺得我必須為沒有更大聲地提出這些問題承擔一些責任。但必須說，聽到你們對 UX 問題感到「驚訝」我很失望。我一直在告訴你們的人 UX 很糟糕（例如早在正式發布之前）並且不斷聽到回覆說「我們知道，我們在修」。我會開始正式化回饋並推送到管道中，敬請期待。我也在本地（Bellevue），很樂意過來嘗試為我們相對簡單的開源 .NET/WPF/UWP 應用程式設置管線。我猜這對我們雙方都會是一次大開眼界的經歷。

一些例子：

* 你無法用包含子模組（Submodule）的 Git 儲存庫建構管線

* 發現無法編輯某些自訂工具的 PATH

* 新管線體驗不太合理，新使用者到處點擊最終會到達錯誤的文件


### Edward Thomson（Azure PM）摘要

我寫了合併你的 Pull Request 的程式碼。Microsoft 的 Azure DevOps 專案經理（Program Manager）；之前在 GitHub、Microsoft、SourceGear 擔任版本控制工具的軟體工程師。

https://www.edwardthomson.com/

libgit2 共同維護者。https://libgit2.github.io

All Things Git 播客共同主持人，一個關於 Git 的 Podcast。https://www.allthingsgit.com/

Developer Tools Weekly 策展人，一份關於開發工具的電子報。https://developertoolsweekly.com/
