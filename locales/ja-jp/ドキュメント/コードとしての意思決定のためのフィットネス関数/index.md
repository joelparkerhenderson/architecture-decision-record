# コードとしての意思決定のためのフィットネス関数

フィットネス関数とは、プログラミングコードで記述された客観的で自動化されたチェックであり、決定が維持されていることを検証します。

- フィットネス関数は、決定をテスト可能かつ保証可能にします。

- 決定のためのフィットネス関数は、品質保証、規制プロセス、ガバナンスの目標を大いに助けることができます。

## フィットネス関数と決定のつながり

決定記録は決定を文書化し、フィットネス関数はその決定を保証します。

- 決定の例: 監査要件のためにイベントソーシングを使用する。

- フィットネス関数の例: 継続的インテグレーションサーバーを使用して、すべての状態変更がイベントを生成しなければならないことをテストする。

## フィットネス関数が決定に役立つ理由

客観的な測定: フィットネス関数は合格か不合格かのいずれかなので、作業が可視化され明確になります。

継続的な使用: フィットネス関数は生きたルールであり、すべてのコミットとビルドで実行されます。

リファクタリングへの自信: フィットネス関数は決定ルールの誤りを自動的に検出します。

スケーラブルなガバナンス: フィットネス関数は、ボトルネックを作ることなく標準を保証します。

## フィットネス関数は AI を使用できますか?

フィットネス関数は、計画、コード、スキーマ、API などの作業について質問することで、
決定のために AI LLM を活用できます:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

## アーキテクチャの単体テスト

[ArchUnit](https://www.archunit.org/): 通常の Java 単体テストフレームワークを使用して、Java コードのアーキテクチャルールをチェックします。

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): Jest、Vitest、Jasmine などを使用して、TypeScript コードおよび JavaScript コードのアーキテクチャルールをチェックします。
