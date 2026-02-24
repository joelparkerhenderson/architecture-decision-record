# 架構決策記錄：適用於新創產品的全功能、全端網頁應用程式框架

<!--

ChatGPT prompt

Long software architecture decision record
for a web application framework, batteries included, full stack, for a startup product.

Evaluate Python Django, Ruby on Rails, Phoenix Elixir, Rust Loco.

Primary need: web application for paying customers to sign in, upload files, process data, and view reports.

High importance: 1. Agile development because this is for a startup. 2. Full-stack because we do not want to spend extra time on a separate front-end. 3. Works well with AI/ML tools for data analysis, such as Project Jupyter notebooks.

Low importance: 1. Runtime speed. 2. Scalability. 3. Backwards compatibility.

-->

**主要目標：**
構建一個網頁應用程式，讓付費客戶能夠登入、上傳檔案、處理資料和檢視報告，重點在於敏捷開發（Agile Development）、全端功能，以及與 AI/ML 工具（特別是 Project Jupyter notebooks）的良好相容性。

### 背景脈絡與需求：

1. **敏捷開發（高優先）**：作為一家新創公司，我們需要快速迭代和靈活性。敏捷實踐，如快速原型製作、迭代開發和適應變化的能力，是我們開發週期的關鍵。

2. **全端框架（高優先）**：我們的目標是透過選擇一個能夠高效處理後端和前端的框架來最小化開銷，減少對獨立前端框架的需求。

3. **與 AI/ML 工具的相容性（高優先）**：能夠輕鬆與 Jupyter notebooks 和 Python 資料科學生態系統（NumPy、Pandas、TensorFlow 等）等資料分析工具整合至關重要。這將促進高效的資料處理和報告生成。

4. **低重要性標準**：
   - **執行時速度**：雖然效能是相關的，但在起步階段並非最關鍵的因素，因為我們更關注開發速度和功能完整性。
   - **可擴展性**：我們預期會成長，但可擴展性問題可以稍後解決，目前這不是主要需求。
   - **向後相容性**：我們專注於當前的技術，不太擔心與舊系統的向後相容性。

### 評估的框架：

1. **Django (Python)**
2. **Ruby on Rails (Ruby)**
3. **Phoenix (Elixir)**
4. **Loco (Rust)**

---

### 1. **Django (Python)**

**概述**：
Django 是一個高階的 Python 網頁框架，提倡快速開發和乾淨、務實的設計。它以「全功能內建（batteries included）」的哲學聞名，意味著它開箱即用地包含了許多功能，如認證、路由、ORM 和表單處理。

**優勢**：
- **全端**：Django 是一個全面的全端框架，能夠透過整合的功能（如模板引擎、管理介面）處理後端和前端需求。
- **敏捷開發**：Django 明確定義的結構和慣例允許快速開發和適應性，這對新創環境至關重要。該框架擁有優秀的文件和豐富的第三方套件生態系統，加速了開發。
- **AI/ML 整合**：Python 的生態系統在資料科學和機器學習方面無可匹敵。Django 作為基於 Python 的框架，能與 Jupyter notebooks、Pandas、NumPy、TensorFlow 和 scikit-learn 等工具無縫整合。
- **社群和生態系統**：Django 擁有廣泛的社群、完善的文件，以及豐富的外掛和擴充套件，這顯著加速了開發和問題排解。

**劣勢**：
- **執行時速度**：Python 的速度往往比 Rust 或 Elixir 等語言慢。然而，對於效能不是主要考量的此使用案例，這可能不是決定性因素。
- **可擴展性**：雖然 Django 具有高度可擴展性，但在沒有仔細最佳化的情況下，在非常高的規模上可能會面臨挑戰（例如處理大量並發請求）。不過，Django 仍然可以透過負載平衡和快取技術有效地擴展。

**評定**：
Django 在敏捷開發、全端支援和 AI/ML 相容性方面的需求上契合度很高。其 Python 整合提供了對應用程式所需資料科學工具和函式庫的無縫存取。

---

### 2. **Ruby on Rails (Ruby)**

**概述**：
Ruby on Rails (RoR) 是一個成熟的全端網頁應用程式框架，以其慣例優於設定（convention-over-configuration）的方式聞名，促進了快速開發。

**優勢**：
- **全端**：RoR 附帶了用於後端和前端開發的內建工具（如視圖、模板、鷹架），其豐富的 gem 函式庫允許快速實現各種功能。
- **敏捷開發**：Ruby on Rails 以其快速迭代週期特別聞名，這對於希望快速迭代功能的新創公司來說是有利的。RoR 支援測試驅動開發（TDD），並擁有成熟的敏捷工作流程生態系統。
- **社群和生態系統**：RoR 擁有成熟、強大的社群和豐富的 gem，可以加速開發。
- **易用性**：Rails 有非常友善的開發者語法，以快速簡單地處理資料庫遷移、MVC（模型-視圖-控制器）架構和路由而聞名。

**劣勢**：
- **效能**：Ruby 的執行時效能往往比 Python 或 Elixir 慢。雖然 RoR 可以透過適當的基礎設施進行擴展，但 Ruby 的效能可能會成為需要大量即時處理或高並發流量的應用程式的瓶頸。
- **AI/ML 整合**：雖然 Ruby 有一些機器學習函式庫，但在 AI/ML 社群中的採用率不如 Python 廣泛。與 Jupyter notebooks 等工具的整合不如 Python 順暢，使得 Python 對於資料密集型應用程式來說是更強的選擇。

**評定**：
雖然 Ruby on Rails 在敏捷開發和快速原型製作方面表現出色，但在 AI/ML 相容性方面與 Python (Django) 相比有所不足。對於優先考慮快速迭代而非深度資料分析整合的新創公司來說，它是一個可行的選擇。

---

### 3. **Phoenix (Elixir)**

**概述**：
Phoenix 是一個用 Elixir 構建的網頁框架，Elixir 是一種專為可擴展性和並發性設計的函數式程式語言。Phoenix 利用 Erlang VM，以處理大規模並發和容錯系統而聞名。

**優勢**：
- **可擴展性和效能**：Phoenix 在可擴展性和處理高並發方面表現出色。它建立在 Erlang VM 之上，能夠支援數千（甚至數百萬）個並發連線，使其成為需要即時資料處理或高流量的應用程式的強大候選者。
- **全端**：Phoenix 包含構建應用程式後端和前端所需的一切。它支援即時視圖（Live Views）以進行互動式 UI 更新，並包含模板引擎。
- **敏捷開發**：Phoenix 高度模組化，允許對功能進行快速迭代。它非常適合需要快速行動的新創公司。
- **AI/ML 相容性**：雖然 Elixir 有新興的機器學習函式庫，但在 AI/ML 任務方面的支援不如 Python 廣泛。與 Jupyter notebooks 等工具的整合需要變通方案，因為 Elixir 的資料科學生態系統不如 Python 成熟。

**劣勢**：
- **AI/ML 生態系統**：Elixir 不是資料科學或機器學習中使用的主要語言，其生態系統不如 Python 成熟。因此，與 Jupyter notebooks 或流行的 AI 函式庫（TensorFlow、PyTorch）的整合會比較麻煩。
- **學習曲線**：如果團隊不熟悉函數式程式設計和 Elixir，可能會有更陡峭的學習曲線。

**評定**：
如果可擴展性和並發性是主要考量，Phoenix 是一個絕佳的選擇。然而，鑑於 AI/ML 相容性的優先地位，由於 Elixir 在此領域的生態系統有限，Phoenix 可能不是最佳選擇。

---

### 4. **Loco (Rust)**

**概述**：
Loco 是一個用 Rust 構建的網頁框架，Rust 是一種以效能、記憶體安全和並發性聞名的系統程式語言。Rust 在構建高效能應用程式方面越來越受歡迎。

**優勢**：
- **效能**：Rust 的主要優勢在於其高效能和記憶體安全，使其成為需要底層控制或極高效能的應用程式的絕佳選擇。
- **並發性**：Rust 的所有權系統在允許安全的並發程式設計的同時確保記憶體安全，使其非常適合需要高效擴展和處理平行運算的系統。

**劣勢**：
- **全端開發**：Loco 雖然前景看好，但在提供完整的全端解決方案方面不如其他框架成熟。它更適合後端開發，圍繞 Rust 的前端生態系統仍在發展中。
- **敏捷開發**：由於 Rust 的底層特性和更陡峭的學習曲線，使用 Rust 開發可能比 Python 或 Ruby 等高階語言更慢。
- **AI/ML 生態系統**：Rust 不具備與 Python 相同的廣泛 AI/ML 生態系統。雖然 Rust 中有越來越多的數值計算函式庫，但它們遠不如 Python 的產品成熟，如 Jupyter notebooks 或機器學習框架。

**評定**：
雖然 Rust 及其框架 Loco 提供了卓越的效能，但缺乏全端支援、敏捷開發優勢和 AI/ML 生態系統，使其對此特定使用案例不太理想。它更適合效能關鍵型應用程式，而非整合資料科學工具的快速網頁開發。

---

### 結論

在根據專案需求評估各選項後，**Django (Python)** 是最合適的選擇。它提供以下優勢：

- **全端能力**：Django 是一個整合後端和前端開發的全端框架。
- **敏捷開發**：該框架非常適合快速原型製作和迭代，這對新創環境至關重要。
- **AI/ML 相容性**：Python 是 AI/ML 領域的領先語言，Django 與 Jupyter notebooks 等函式庫的相容性確保了資料分析和處理的順暢整合。
- **社群和生態系統**：Django 強大的社群支援和廣泛的函式庫生態系統提供了大量工具來加速開發。

雖然 **Ruby on Rails** 在敏捷開發方面也是一個強有力的競爭者，但其有限的 AI/ML 支援使其對此特定使用案例不太理想。**Phoenix (Elixir)** 和 **Loco (Rust)** 雖然在可擴展性和效能方面表現出色，但在 AI/ML 整合和全端開發方面有所不足。因此，Django 是此專案的推薦框架。
