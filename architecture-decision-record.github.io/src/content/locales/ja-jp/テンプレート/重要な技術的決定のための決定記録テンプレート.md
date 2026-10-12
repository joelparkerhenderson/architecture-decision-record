# 重要な技術的決定(ITD)のための決定記録テンプレート

これは、
[ITDs: a lean ADR for executive technical decision-making at scale - Ignacio Larrañaga](https://ignaciolarranaga.medium.com/itds-a-lean-adr-for-executive-technical-decision-making-at-scale-e18bb3f6a563)
で説明されている重要な技術的決定(Important Technical Decisions、ITD)テンプレートです。

ITD は ADR を焦点を絞って進化させたもので、スピード、明確さ、経営層による
検証に最適化されています。ADR が何が決定されたかを文書化するのに対し、ITD は
決定そのものをレビュー可能にする、決定を最優先とするリーンな成果物であり、
ステークホルダーは素早く目を通し、容易に異議を唱えることができます。ITD は、
モデル、ライブラリ、CI/CD 戦略の選択など、厳密にはアーキテクチャに関するもので
はない技術的決定に適しています。

各 ITD ファイルに、次のセクションを書きます:

# タイトル

トピックの説明ではなく、決定そのものを述べます。
たとえば、「オンデバイス翻訳に Qwen2.5 1.5B Instruct を使用する」。

## 問題

私たちが解決しようとしていることを述べる 1 文。

## 検討した選択肢

検討の対象となった代替案。選択された選択肢は**太字**で示します。

## 根拠

選択につながった決定的な要因のみ。すべての長所と短所を網羅的に
列挙するものではありません。

## 注記

任意。制約、前提、リンクなど、記録する価値のある追加のコンテキスト。
