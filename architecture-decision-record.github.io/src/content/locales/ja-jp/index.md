# アーキテクチャ決定記録(ADR)

アーキテクチャ決定記録(ADR)は、行われた重要なアーキテクチャ上の決定を、そのコンテキストと結果とともに記録した文書です。

> [!IMPORTANT]
> これらのリソースを重要なシステムで使用する前に、ご自身で十分な検討(デューデリジェンス)を行ってください。

目次:

- [アーキテクチャ決定記録とは?](#アーキテクチャ決定記録とは)
- [ADR の使い始め方](#adr-の使い始め方)
- [ツールで ADR を使い始める方法](#ツールで-adr-を使い始める方法)
- [git で ADR を使い始める方法](#git-で-adr-を使い始める方法)
- [ADR 向け Claude Code スキル](#adr-向け-claude-code-スキル)
- [ファイル名規則](#ファイル名規則)
- [良い ADR を書くための提案](#良い-adr-を書くための提案)
- [ADR のテンプレート例](#adr-のテンプレート例)
- [ADR のためのチームワークのアドバイス](#adr-のためのチームワークのアドバイス)
- [ADR のためのチームワークの質問](#adr-のためのチームワークの質問)
- [ADR の次のステップの概念](#adr-の次のステップの概念)
- [アーキテクチャ図、ビュー、ビューポイント](#アーキテクチャ図ビュービューポイント)
- [コードとしての意思決定のためのフィットネス関数](#コードとしての意思決定のためのフィットネス関数)
- [プルリクエストのための決定ガードレール](#プルリクエストのための決定ガードレール)
- [詳細情報](#詳細情報)

テンプレート:

- [ジェフ・タイリーとアート・アッカーマンによる決定記録テンプレート](テンプレート/ジェフ-タイリーとアート-アッカーマンによる決定記録テンプレート/)
- [マイケル・ナイガードによる決定記録テンプレート](テンプレート/マイケル-ナイガードによる決定記録テンプレート/)
- [EdgeX による決定記録テンプレート](テンプレート/edgexによる決定記録テンプレート/)
- [arc42 による決定記録テンプレート](テンプレート/arc42による決定記録テンプレート/)
- [アレクサンドリアン・パターンのための決定記録テンプレート](テンプレート/アレクサンドリアン-パターンのための決定記録テンプレート/)
- [ビジネスケースのための決定記録テンプレート](テンプレート/ビジネスケースのための決定記録テンプレート/)
- [MADR プロジェクトの決定記録テンプレート](テンプレート/madrプロジェクトの決定記録テンプレート/)
- [Planguage を使用した決定記録テンプレート](テンプレート/planguageを使用した決定記録テンプレート/)
- [Paulo Merson による決定記録テンプレート](https://github.com/pmerson/ADR-template)
- [Olaf Zimmermann による決定記録テンプレート](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [ガレス・モーガンによる決定記録テンプレート](テンプレート/ガレス-モーガンによる決定記録テンプレート/)
- [GIG Cymru NHS Wales による決定記録テンプレート](テンプレート/gig-cymru-nhs-walesによる決定記録テンプレート/)
- [Ignacio Larrañaga による重要な技術的決定(ITD)のための決定記録テンプレート](テンプレート/重要な技術的決定のための決定記録テンプレート/)

例:

- [CSS フレームワーク](例/cssフレームワーク/)
- [環境変数の設定](例/環境変数の設定/)
- [メトリクス、モニター、アラート](例/メトリクス-モニター-アラート/)
- [Microsoft Azure DevOps](例/マイクロソフト-アジュール-デブオプス/)
- [モノレポ対マルチレポ](例/モノレポ対マルチレポ/)
- [プログラミング言語](例/プログラミング言語/)
- [シークレットの保管](例/シークレットの保管/)
- [タイムスタンプ形式](例/タイムスタンプ形式/)
- [さらに多数...](例/)

## アーキテクチャ決定記録とは?

**アーキテクチャ決定記録**(ADR)とは、行われた重要なアーキテクチャ上の決定を、そのコンテキストと結果とともに記録した文書です。

**アーキテクチャ決定**(AD)とは、重要な要件に対処するソフトウェア設計上の選択です。

**アーキテクチャ決定ログ**(ADL)とは、特定のプロジェクト(または組織)のために作成され、維持されるすべての ADR の集合です。

**アーキテクチャ上重要な要件**(ASR)とは、ソフトウェアシステムのアーキテクチャに測定可能な影響を与える要件です。

これらはすべて、**アーキテクチャ知識管理**(AKM)というトピックの範囲内にあります。

この文書の目的は、ADR の概要、その作成方法、そしてさらに情報を探す場所を手早く紹介することです。

略語:

  * **AD**: アーキテクチャ決定

  * **ADL**: アーキテクチャ決定ログ

  * **ADR**: アーキテクチャ決定記録

  * **AKM**: アーキテクチャ知識管理

  * **ASR**: アーキテクチャ上重要な要件

## ADR の使い始め方

ADR を使い始めるには、次の領域についてチームメイトと話し合ってください。

決定の特定:

  * AD はどれほど緊急で、どれほど重要ですか?

  * 今すぐ決める必要がありますか、それともより多くのことが分かるまで待てますか?

  * 個人的および集合的な経験、ならびに認知された設計手法やプラクティスは、決定の特定に役立ちます。

  * 理想的には、製品の ToDo リストを補完する決定の ToDo リストを維持します。

意思決定:

  * 一般的なものとソフトウェアアーキテクチャに特化したものの両方で、多くの意思決定手法が存在します。たとえば、ダイアログマッピングがあります。

  * グループ意思決定は活発な研究テーマです。

決定の実施と徹底:

  * AD はソフトウェア設計で使用されるため、システムに資金を提供し、開発し、運用するステークホルダーに伝達され、受け入れられなければなりません。

  * アーキテクチャ上明白なコーディングスタイルと、アーキテクチャ上の懸念と決定に焦点を当てたコードレビューは、関連する 2 つの実践です。

  * AD は、ソフトウェアの進化の中でソフトウェアシステムを近代化する際にも(再)検討されなければなりません。

決定の共有(任意):

  * 多くの AD はプロジェクト間で繰り返されます。

  * したがって、過去の決定に関する良い経験も悪い経験も、明示的な知識管理戦略を採用する際に、価値ある再利用可能な資産になり得ます。

決定の文書化:

  * 決定を記録するための多くのテンプレートとツールが存在します。

  * アジャイルコミュニティを参照してください。たとえば M. Nygard の ADR。

  * 従来のソフトウェアエンジニアリングやアーキテクチャ設計プロセスを参照してください。たとえば、IBM UMF や CapitalOne の Tyree と Akerman が提案するテーブルレイアウト。

詳細:

  * 上記の手順は、Wikipedia の [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision) の項目から採用したものです

## ツールで ADR を使い始める方法

- [MySpec](https://myspec.dev) — プロジェクト憲章、技術アーキテクチャ、ADR を整理された Markdown に構造化し、MCP 経由で提供する、自動化された仕様およびアーキテクチャ決定プラットフォーム。

ツールを使って ADR を使い始めるには、好きな方法で構いません。

例:

  * Google ドライブとオンライン編集が好きなら、Google ドキュメントまたは Google スプレッドシートを作成できます。

  * git などのソースコードバージョン管理が好きなら、各 ADR についてファイルを作成できます。

  * Atlassian Jira などのプロジェクト計画ツールが好きなら、そのツールの計画トラッカーを使用できます。

  * MediaWiki などの wiki が好きなら、ADR の wiki を作成できます。

## git で ADR を使い始める方法

git バージョン管理が好きな方のために、ソースコードを持つ典型的なソフトウェアプロジェクトで git を使って ADR を使い始める私たちの方法を紹介します。

ADR ファイル用のディレクトリを作成します:

```sh
$ mkdir adr
```

各 ADR について、`database.txt` のようなテキストファイルを作成します:

```sh
$ vi database.txt
```

ADR には好きなことを何でも書いてください。アイデアについては、このリポジトリのテンプレートを参照してください。

その ADR を git リポジトリにコミットします。

## ADR 向け Claude Code スキル

このリポジトリは、AI コーディングエージェントが本プロジェクトの推奨どおりに ADR を作成・保守できるよう、[`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/) に 2 つの [Claude Code](https://claude.com/claude-code) スキルを同梱しています。

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — 汎用で、あらゆるプロジェクトで ADR を書く人向けです。決定に ADR が必要かの判断、`adr/` または `decisions/` ディレクトリの用意、ファイル名の付け方、同梱の 11 種類の雛形からのテンプレート選択、そして堅実なコンテキスト/決定/結果の各節の作成を支援します。

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — このリポジトリのメンテナー専用です。リポジトリの構成、README と locales を対応させる規約、新しいテンプレート、例、ツールリンクを追加する正確な手順を文書化しています。

スキルを使うには、そのフォルダを作業中のリポジトリのルートにある `.claude/skills/` に(すべてのプロジェクトで使えるようにするには `~/.claude/skills/` に)コピーし、Claude Code に ADR の作成またはレビューを依頼します。

## ファイル名規則

通常のテキストファイルを使用して ADR を作成する場合は、独自の ADR ファイル名規則を考案するとよいでしょう。

私たちは、特定の形式を持つファイル名規則を使用することを好みます。

例:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

私たちのファイル名規則:

  * 名前には現在形の命令形の動詞句を使用します。これは可読性を高め、私たちのコミットメッセージの形式とも一致します。

  * 名前には小文字とダッシュを使用します(このリポジトリと同じ)。これは可読性とシステムの使いやすさのバランスです。

  * 拡張子は markdown です。これは、簡単な書式設定に役立ちます。

## 良い ADR を書くための提案

良い ADR の特徴:

* 根拠: その特定の AD を行う理由を説明します。これには、コンテキスト(下記参照)、さまざまな選択肢の長所と短所、機能の比較、コスト/便益の議論などが含まれます。

* 具体的: 各 ADR は 1 つの AD について書くべきで、複数の AD を扱うべきではありません。

* タイムスタンプ: ADR 内の各項目がいつ書かれたかを明記します。これは、コスト、スケジュール、スケーリングなど、時間とともに変化する可能性のある側面にとって特に重要です。

* 不変: ADR 内の既存の情報を変更しないでください。代わりに、新しい情報を追加して ADR を修正するか、新しい ADR を作成して ADR を置き換えてください。

ADR の良い「コンテキスト」セクションの特徴:

* 組織の状況とビジネス上の優先事項を説明します。

* チームの社会的構成やスキル構成に基づく根拠と考慮事項を含めます。

* 関連する長所と短所を含め、それらをニーズや目標に沿った言葉で説明します。

ADR の良い「結果」セクションの特徴:

* 決定を行った結果として何が起こるかを説明します。これには、影響、成果、出力、フォローアップなどが含まれます。

* 後続の ADR に関する情報を含めます。ある ADR がさらなる ADR の必要性を引き起こすことは比較的よくあります。たとえば、ある ADR が大きな包括的な選択を行い、それがさらに小さな決定の必要性を生み出す場合などです。

* 事後レビューのプロセスを含めます。チームが各 ADR を 1 か月後にレビューし、ADR の情報を実際に起きたことと比較して、学び成長することは一般的です。

新しい ADR は以前の ADR に取って代わることがあります:

* 以前の ADR に取って代わる、またはそれを無効にする AD が行われた場合は、新しい ADR を作成する必要があります

## ADR のテンプレート例

ネット上で収集した ADR のテンプレート例:

- [Michael Nygard による ADR テンプレート](テンプレート/マイケル-ナイガードによる決定記録テンプレート/) (シンプルで人気)

- [Jeff Tyree と Art Akerman による ADR テンプレート](テンプレート/ジェフ-タイリーとアート-アッカーマンによる決定記録テンプレート/) (より洗練)

- [Alexandrian パターンのための ADR テンプレート](テンプレート/アレクサンドリアン-パターンのための決定記録テンプレート/) (コンテキストの詳細付きのシンプルな形式)

- [ビジネスケースのための ADR テンプレート](テンプレート/ビジネスケースのための決定記録テンプレート/) (より MBA 寄りで、コスト、SWOT、さらに多くの意見を含む)

- [Markdown Any Decision Records(MADR)プロジェクトの ADR テンプレート](テンプレート/madrプロジェクトの決定記録テンプレート/) (簡易版と詳細版があり、後者は選択肢とその長所・短所を重視)

- [Planguage を使った ADR テンプレート](テンプレート/planguageを使用した決定記録テンプレート/) (より品質保証寄り)

- [Ignacio Larrañaga による重要な技術的決定(ITD)のテンプレート](テンプレート/重要な技術的決定のための決定記録テンプレート/) (簡潔で決定ファースト、経営層による迅速なレビューに最適化)

## ADR のためのチームワークのアドバイス

チームで決定記録の使用を検討しているなら、多くのチームと協力する中で私たちが学んだアドバイスを紹介します。

「何を」義務づけるのではなく、「なぜ」を一緒に話し合うことで、チームメイトを導く機会があります。たとえば、決定記録は、チームがより賢く考え、より良く伝え合うための方法です。事後に強制される書類作成の要件にすぎないなら、決定記録に価値はありません。

チームによっては、略語の「ADR」よりも「decisions(決定)」という名前をはるかに好みます。あるチームがディレクトリ名として「decisions」を使うと、電球が点灯したかのように、チームはベンダーの決定、計画の決定、スケジュールの決定など、そのディレクトリにより多くの情報を入れ始めます。これらすべての種類の情報に同じテンプレートを使用できます。私たちは、人々は略語(「ADR」)よりも言葉(「決定」)の方が速く学べること、「記録(record)」という単語を取り除くと作業中の文書を書く動機が高まること、そして一部の開発者や一部のマネージャーは「アーキテクチャ」という言葉を好まないことを仮説として立てています。

理論的には、不変性が理想的です。実際には、私たちのチームでは可変性の方がうまくいっています。既存の ADR に、日付スタンプと、その情報が決定後に届いたという注記を付けて、新しい情報を挿入します。この種のアプローチは、私たち全員が更新できる「生きた文書」につながります。典型的な更新は、新しいチームメイトのおかげで、あるいは新しい提供サービスのおかげで、あるいは私たちの利用の実世界での結果から、あるいはベンダーの機能、料金プラン、ライセンス契約などの事後のサードパーティによる変更の後に、情報を得たときです。

## ADR のためのチームワークの質問

### 誰が ADR を作成できますか?

特定の人、特定の役割、特定のチーム、特定の部門などの領域を検討してください。また、ADR を委託できる人、役割、チーム、部門がいるかどうかも検討してください。つまり、他の誰かが執筆する ADR を依頼できる場合です。 

回答例: アーキテクチャ決定記録の README ページを読んだ組織内の誰もが ADR を提案できます。つまり、その人は ADR の執筆を開始し、チームと共有できます。

### ADR を起こすことを正当化するものは何ですか?

組織のチームの仕事の進め方、ソフトウェアシステムの構造、チーム間の調整、長期的な保守性、外部インターフェース、誰に利益をもたらしたいか、といった領域を検討してください。 

回答例: 私たちは、将来の開発者に自分たちが行っていることの「なぜ」を理解してもらいたいときに、ADR を作成したいと考えます。

### ADR を起こさないことを正当化するものは何ですか?

アーキテクチャに関するものではない決定、リスクが最小限であったり、自己完結していたり、1 人の開発者に限られるなど些細な決定、標準、ポリシー、文書などで既に完全にカバーされている決定、あるいは回避策、概念実証、実験などの一時的な決定といった領域を検討してください。 

回答例: 私たちは、決定が範囲、時間、リスク、コストの面で限定的な場合、または既に他の場所でカバーされている場合は、ADR を省略したいと考えます。

### ADR のライフサイクルとは何ですか?

作成プロセス、調査プロセス、意思決定プロセス、実装プロセス、廃止プロセスといった領域を検討してください。ADR のライフサイクルを時間とともにどのように追跡するか、たとえば ADR をある状態から次の状態へどのように移行させるか、またこれをステークホルダーにどのように伝えるかを検討してください。 

回答例: 私たちは、ADR に 5 つのライフサイクル段階を持たせたいと考えます: 開始(Initiating) → 調査(Researching) → 評価(Evaluating) → 実装(Implementing) → 維持(Maintaining) → 廃止(Sunsetting)。

### ADR のライフサイクルの各ステップの基準は何ですか?

ADR の受け入れ基準といった領域を検討してください。つまり、ある ADR がライフサイクルの次のステップに進むのに十分良いとどうやって判断しますか? 問題は明確に述べられていますか? 代替案は検討されましたか? トレードオフは十分に理解され文書化されていますか?
関連するすべてのコンテキストが揃っていますか? 関連するすべてのステークホルダーが関与していますか? すべてのフィードバックが取り込まれましたか? 

回答例: 私たちは、アクティブなチームが 1) 調査を完了し、2) 評価を完了し、3) コメント依頼と 1 週間の期限を付けて ADR 提案をステークホルダーに公開し、4) すべてのステークホルダーのコメントが取り込まれ対処された時点で、ステークホルダーが ADR について投票することを望みます。

### どのような役割と責任が ADR と関わりますか?

提案者、調査者、評価者、レビュー担当者、承認者、保守担当者などの役割を検討してください。ステークホルダーとのコミュニケーション、期待が満たされていることの確認、ウェブサイトやイントラネットでの共有、作業の定期的な、特に関連する変更が起きたときのレビューなどの責任を検討してください。

回答例: 私たちは、各 ADR に常に、主担当者、副担当者、および責任チームを置きたいと考えます。これらは、コミュニケーション、公開、保守、少なくとも年に一度の定期レビュー、および必要に応じた最終的な廃止に責任を負います。

### ガバナンスは ADR とどのように関わりますか?

組織の仕事の進め方、法務面や人事面などの特別なコンプライアンス上のニーズ、合意対対立対エスカレーションをどのように扱いたいか、といった領域を検討してください。ADR について、承認する、投票する、拒否権を行使するなど、他よりも大きな影響力を持てる領域や人やチームはありますか?

回答例: ADR のガバナンスは次の優先順位です: CEO、CTO、CLO、ADR を実装するチーム、その ADR について最も知識の豊富なチーム内の専門家。ADR に記載されていない限り、他の誰もガバナンスを持ちません。 

### どのような原則が ADR と関わりますか?

素早く動くか、ゆっくり動くか、決定の合意か決定の対立か、リスクの選好か安全の選好か、公開の議論か非公開の議論か、といった組織の仕事の進め方を含む領域を検討してください。

回答例: 私たちは、行動への偏重、反対しつつもコミットする(disagree-and-commit)、容易に元に戻せて容易に切り離せる決定には 70% の見積もりで十分、そして組織の機密保持契約に記載された機密情報を除く公開での仕事の進め方、というリーダーシップ原則を使用します。

## ADR の次のステップの概念

[Arc42](https://arc42.org/) は 2 つの問いに実用的に答え、必要に応じて調整できます。アーキテクチャについて何を文書化/伝達すべきか、どのように文書化/伝達すべきか。Arc42 には、アーキテクチャ決定記録に加え、目標、制約、コンテキスト、品質、リスクなどに関する指針が含まれます。

[C4 モデル](https://c4model.com/) は、ソフトウェアアーキテクチャを図示するための、習得しやすく開発者に優しい手法です。C4 は、コンテキスト、コンテナ、コンポーネント、コードの階層的な図と、システムランドスケープ、動的、デプロイメントを補う図で構成されます。

## アーキテクチャ図、ビュー、ビューポイント

アーキテクチャ図は「アーキテクチャビュー」と呼ばれます。

「アーキテクチャビュー」は「アーキテクチャビューポイント」の実例です。

「アーキテクチャビューポイント」は、特定の関心事を持つ特定の読み手を想定します。

アーキテクチャビューポイント、ビュー、図の例:

- ビジネス能力

- 高レベルのビジネスプロセス

- [バリューストリーム](https://en.wikipedia.org/wiki/Value_stream)

- アプリケーションコンポーネントに対応付けたソフトウェア機能

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) コンテキスト図 (TO-BE / AS-IS)

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) コンテナ図 (TO-BE / AS-IS)

- [エンティティ関連図](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) データエンティティをアプリケーションコンポーネントに対応付けるため

- [シーケンス図](https://en.wikipedia.org/wiki/Sequence_diagram) システム内および統合における機能フローを記述するため

- [ビジネスプロセスモデルと表記法](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) アプリケーションコンポーネント間のデータフローを記述する図

- [ビジネスプロセスモデルと表記法](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) ビジネスプロセス/ユーザーシナリオを記述する図

- [IDおよびアクセス管理](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM) 図

- [ロールベースアクセス制御](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) アプリケーションコンポーネントごとのロールを示す図

- [属性ベースアクセス制御](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) アプリケーションコンポーネントごとの属性を示す図

- プライバシー図

関連する図:

- ユースケース図は、経営陣/顧客にユースケースを示します。これは要件に先立ち、要件はソフトウェアアーキテクチャに先立ちます。

- デプロイメント図は、ソフトウェアコンポーネントが配備される物理的なハードウェア/コンピュータを示します。
- データフロー図は、データがシステム内をどう移動し変換されるかを示します。
- シーケンス図は、HTTP などのプロトコルが時間軸上でどう動作するかを示すために使います。

- アクティビティ図は、NPC の AI のように、ソフトウェアシステムが行う活動のワークフローを描きます。

## コードとしての意思決定のためのフィットネス関数

フィットネス関数とは、プログラミングコードで記述された客観的で自動化されたチェックであり、決定が維持されていることを検証します。

- フィットネス関数は、決定をテスト可能かつ保証可能にします。

- 決定のためのフィットネス関数は、品質保証、規制プロセス、ガバナンスの目標を大いに助けることができます。

### フィットネス関数と決定のつながり

決定記録は決定を文書化し、フィットネス関数はその決定を保証します。

- 決定の例: 監査要件のためにイベントソーシングを使用する。

- フィットネス関数の例: 継続的インテグレーションサーバーを使用して、すべての状態変更がイベントを生成しなければならないことをテストする。

### フィットネス関数が決定に役立つ理由

客観的な測定: フィットネス関数は合格か不合格かのいずれかなので、作業が可視化され明確になります。

継続的な使用: フィットネス関数は生きたルールであり、すべてのコミットとビルドで実行されます。

リファクタリングへの自信: フィットネス関数は決定ルールの誤りを自動的に検出します。

スケーラブルなガバナンス: フィットネス関数は、ボトルネックを作ることなく標準を保証します。

### フィットネス関数は AI を使用できますか?

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

### アーキテクチャの単体テスト

[ArchUnit](https://www.archunit.org/): 通常の Java 単体テストフレームワークを使用して、Java コードのアーキテクチャルールをチェックします。

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): Jest、Vitest、Jasmine などを使用して、TypeScript コードおよび JavaScript コードのアーキテクチャルールをチェックします。

## プルリクエストのための決定ガードレール

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
は、適切なタイミングで、つまり開発者が決定の対象となるコードを実際に変更しているときに、
適切な決定記録を自動的に表示します。マージの前に開発者がドキュメントフォルダを読むことを期待する代わりに、
関連するコンテキストがプルリクエスト上に直接表示されます。

これはあらゆる種類の決定記録で機能します。アーキテクチャ上の決定、データに関する決定、コンプライアンスに関する決定、臨床・医療に関する決定、セキュリティに関する決定などです。

あらゆる CI システム(GitLab、Jenkins、CircleCI)で、またプリコミットフックとして動作します。
オープンソース。MIT ライセンス。

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) は、監視対象のコードパスが、
アーキテクチャ決定記録の追加や更新なしに変更された場合にプルリクエストを失敗させる GitHub
Action です。免除は明示的です。理由付きの `ADR-Exempt:` 行がゲートを通過させ、ジョブの概要に記録されます。テンプレートに依存せず、依存関係もありません。オープンソース。MIT ライセンス。

## 詳細情報

はじめに:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

テンプレート:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

詳細:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - 無料の月次ソフトウェアアーキテクチャ講座

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

ツール:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

企業固有のガイダンス:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

例:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

動画:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

ポッドキャスト:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

書籍:

- [Software Architecture Metrics: Case Studies to Improve the Quality of Your Architecture - by Christian Ciceri, Dave Farley, Neal Ford, Andrew Harmel-Law, Michael Keeling and Carola Lilienthal](https://www.amazon.com/Software-Architecture-Metrics-Christian-Ciceri-ebook/dp/B0B1NZ8Z5V)

- [Software Systems Architecture: Working With Stakeholders Using Viewpoints and Perspectives - by Nick Rozanski and Eoin Woods](https://www.amazon.com/Software-Systems-Architecture-Stakeholders-Perspectives/dp/032171833X)

- [Software Architecture in Practice (SEI Series in Software Engineering)](https://www.amazon.com/Software-Architecture-Practice-SEI-Engineering-ebook/dp/B094CPJ96B)

- [Documenting Software Architectures: Views and Beyond (SEI Series in Software Engineering)](https://www.amazon.com/Documenting-Software-Architectures-Beyond-Engineering-ebook/dp/B0046XS3RO)

- [The Software Architect Elevator: Redefining the Architect's Role in the Digital Enterprise](https://www.amazon.com/Software-Architect-Elevator-Redefining-Architects-ebook/dp/B086WQ9XL1)

- [Fundamentals of Software Architecture: An Engineering Approach - by Mark Richards and Neal Ford](https://www.amazon.com/Fundamentals-Software-Architecture-Engineering-Approach-ebook/dp/B0849MPK73)

- [Building Evolutionary Architectures - by Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage](https://www.amazon.com/Building-Evolutionary-Architectures-Neal-Ford-ebook/dp/B0BN4T1P27?crid=37FA31IFLAS0Z)

- [Foundations of Decision Analysis by Ronald Howard and Ali Abbas](https://www.amazon.com/Foundations-Decision-Analysis-Ronald-Howard-ebook/dp/B00SZECJTI?crid=14BK5SDP76UN6)

- [Head First Software Architecture - by Raju Gandhi, Neal Ford and Mark Richards](https://www.amazon.com/Head-First-Software-Architecture-Architectural-ebook/dp/B0CW1JMNF2)

- [Communication Patterns: A Guide for Developers and Architects - by Jacqui Read](https://www.amazon.com/Communication-Patterns-Guide-Developers-Architects/dp/1098140540)

関連項目:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - 明示的な推論、前提、認知状態、トレードオフとともに決定を表現するための、ベンダー中立で機械可読な YAML/JSON 形式。決定文書に構造化された検証可能な推論を加えることで ADR を補完します。
