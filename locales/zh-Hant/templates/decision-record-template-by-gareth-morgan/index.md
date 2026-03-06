# [000] 標題
*為每個 ADR 分配一個編號以便於引用和歸檔* \
*注意：所有斜體文字提供提示，在正式版本中應移除*

## 狀態 - 草稿（DRAFT）/ 生效中（ACTIVE）/ 已被 [000] 棄用（DEPRECATED）/ 取代 [000]（SUPERSEDES）

## 背景脈絡
*簡要描述此 ADR 打算處理的問題，以及問題存在的原因。*

## 決定的方案
*詳述已做出/將做出的具架構重要性的決策，並描述它如何處理「背景脈絡」章節中所列的問題。*

## 結果
*此決策對系統的架構特性和功能需求有什麼影響？*

## 治理
*此決策的成果將如何被監控？* \
*如何確保對此決策的遵循？*

## 選項分析
*如適用，包含或連結為達成本文件中的決策所進行的取捨分析。*

### 圖例
*選擇性：提供視覺輔助給利害關係人，以幫助快速辨識正面和負面的取捨——例如簡單的紅綠燈標示搭配正面或負面前綴。*

<span style="background-color:#4bce97; color:black;">綠色</span>背景表示良好匹配，逐漸遞減為<span style="background-color:#f1c232; color:black;">黃色</span>，<span style="background-color:#e06666; color:black;">紅色</span>為最差匹配。 \
\+ 表示正面影響的評語 \
\- 表示負面影響的評語

### 高層級概覽
*每個選項一眼看去與問題脈絡的匹配程度如何？*

<table>
  <thead>
    <tr>
      <th>摘要</th>
      <th>選項 1</th>
      <th>選項 2</th>
      <th>選項 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>實作難易度</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
          + 非常容易
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - 有些棘手
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - 大規模實作，需要專家知識
        </span>
      </td>
    </tr>
    <tr>
      <td><i>時程</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + 非常快
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - 相當慢
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - 非常慢
        </span>
      </td>
    </tr>
    <tr>
      <td><i>策略價值</i></td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - 無策略價值，純為戰術性
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            + 略微改善客戶入職體驗
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + 非常適合即將到來的合併
        </span>
      </td>
    </tr>
  </tbody>
</table>

### 功能需求
*每個潛在選項與所需功能需求的匹配程度如何？*

<table>
  <thead>
    <tr>
      <th>情境</th>
      <th><i>選項 1</i></th>
      <th><i>選項 2</i></th>
      <th><i>選項 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>情境 1</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>情境 2</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>情境 3</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*選擇性：新增列 / 另一個表格以涵蓋已知的未來情境。*

### 非功能需求
*每個潛在選項與所需架構特性的匹配程度如何？
注意：「架構特性（Architecture Characteristics）」是更適當的標題，但請依你的業務領域中熟悉的語言進行調整。*

<table>
  <thead>
    <tr>
      <th>架構 </br> 特性</th>
      <th><i>選項 1</i></th>
      <th><i>選項 2</i></th>
      <th><i>選項 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>可擴展性（Scalability）</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>效能（Performance）</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>可用性（Availability）</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*選擇性：新增或連結架構特性在你的業務/產品中的定義。*
