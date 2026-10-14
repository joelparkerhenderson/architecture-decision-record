# [000] タイトル
*参照とカタログ化を容易にするため、各 ADR に番号を割り当ててください* \
*注: イタリック体のテキストはすべてヒントであり、本番用には削除してください*

## 状態 - DRAFT / ACTIVE /  DEPRECATED by [000] / SUPERSEDES [000]

## コンテキスト
*この ADR が対処しようとしている問題と、その問題が存在する理由を簡潔に説明してください。*

## 決定したアプローチ
*行われた/行われる予定のアーキテクチャ上重要な決定を詳述し、それがコンテキストセクションで概説した問題にどのように対処するかを説明してください。*

## 結果
*この決定は、システムのアーキテクチャ特性と機能要件にどのような影響を与えますか?*

## ガバナンス
*この決定の成果はどのように監視されますか?* \
*この決定への準拠はどのように確保されますか?*

## 選択肢の分析
*該当する場合は、この文書の決定に至るために実施されたトレードオフ分析を含めるか、それにリンクしてください。*

### 凡例
*任意: ステークホルダーが肯定的および否定的なトレードオフを素早く見つけるのに役立つ視覚的補助を提供します。たとえば、肯定的または否定的な接頭辞を付けた単純な信号機のハイライトなどです。*

<span style="background-color:#4bce97; color:black;">緑</span>の背景は適合度が高いことを示し、<span style="background-color:#f1c232; color:black;">黄</span>を経て悪化し、<span style="background-color:#e06666; color:black;">赤</span>が最も適合度が低いことを示します。 \
\+ は肯定的な影響のあるコメントを示します \
\- は否定的な影響のあるコメントを示します

### 概要
*各選択肢は、問題のコンテキストにどの程度適合していますか? 一目で分かるようにしてください。*

<table>
  <thead>
    <tr>
      <th>概要</th>
      <th>選択肢 1</th>
      <th>選択肢 2</th>
      <th>選択肢 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>実装の容易さ</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
          + 非常に簡単
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - 厄介
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - 専門知識を必要とする大規模な実装
        </span>
      </td>
    </tr>
    <tr>
      <td><i>スケジュール</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + 非常に迅速
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - かなり遅い
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - 非常に遅い
        </span>
      </td>
    </tr>
    <tr>
      <td><i>戦略的価値</i></td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - 戦略的価値なし、純粋に戦術的
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            + 顧客のオンボーディング体験をわずかに改善する
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + 今後の合併に最適
        </span>
      </td>
    </tr>
  </tbody>
</table>

### 機能要件
*各選択肢は、望ましい機能要件にどの程度適合していますか?*

<table>
  <thead>
    <tr>
      <th>シナリオ</th>
      <th><i>選択肢 1</i></th>
      <th><i>選択肢 2</i></th>
      <th><i>選択肢 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>シナリオ 1</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>シナリオ 2</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>シナリオ 3</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*任意: 既知の将来のシナリオを網羅するために、行を追加するか、別の表を追加してください。*

### 非機能要件
*各選択肢は、望ましいアーキテクチャ特性にどの程度適合していますか?
注: 「アーキテクチャ特性」の方がより適切なタイトルですが、ビジネスドメインに馴染みのある言葉に合わせて調整してください。*

<table>
  <thead>
    <tr>
      <th>アーキテクチャ </br> 特性</th>
      <th><i>選択肢 1</i></th>
      <th><i>選択肢 2</i></th>
      <th><i>選択肢 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>スケーラビリティ</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>パフォーマンス</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>可用性</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*任意: ビジネス/製品に関連するアーキテクチャ特性の定義を追加するか、リンクしてください。*
