# 架构决策记录 (ADR)

架构决策记录（ADR）是一份记录重要架构决策及其背景和后果的文件。

内容：

- [什么是架构决策记录 ADR](#什么是架构决策记录？)
- [如何开始使用 ADR](#how-to-start-using-adrs)
- [如果开始使用工具进行 ADR](#how-to-start-using-adrs-with-tools)
- [如何开始使用 Git 进行 ADR](#how-to-start-using-adrs-with-git)
- [ADR 文件名约定](#file-name-conventions-for-adrs)
- [编写良好 ADR 的建议](#suggestions-for-writing-good-adrs)
- [ADR 示例模板](#adr-example-templates)
* [ADR 的团队协作建议](#teamwork-advice-for-adrs)
* [ADR 的团队协作问题](#teamwork-questions-for-adrs)
* [ADR 的下一步概念](#next-step-concepts-for-adrs)
* [了解更多信息](#for-more-information)

模板：

* [Decision record template by Jeff Tyree and Art Akerman](locales/zh/templates/decision-record-template-by-jeff-tyree-and-art-akerman/)
* [Decision record template by Michael Nygard](locales/zh/templates/decision-record-template-by-michael-nygard/)
* [Decision record template by EdgeX](locales/zh/templates/decision-record-template-by-edgex/)
* [Decision record template by arc42](locales/zh/templates/decision-record-template-by-arc42/)
* [Decision record template for Alexandrian pattern](locales/zh/templates/decision-record-template-for-alexandrian-pattern/)
* [Decision record template for business case](locales/zh/templates/decision-record-template-for-business-case/)
* [Decision record template of the MADR project](locales/zh/templates/decision-record-template-of-the-madr-project/)
* [Decision record template using Planguage](locales/zh/templates/decision-record-template-using-planguage/)
* [Decision record template by Paulo Merson](https://github.com/pmerson/ADR-template)
* [Decision record template by Olaf Zimmermann](https://medium.com/olzzio/y-statements-10eb07b5a177)
* [Decision record template by Gareth Morgan](locales/zh/templates/decision-record-template-by-gareth-morgan/)
* [Decision record template by GIG Cymru NHS Wales](locales/zh/templates/decision-record-template-by-gig-cymru-nhs-wales/)
* [Translations into more languages](locales/)

案例：

* [CSS 框架](locales/zh/examples/css-framework/)
* [环境变量配置](locales/zh/examples/environment-variable-configuration/)
* [指标、监控与告警](locales/zh/examples/metrics-monitors-alerts/)
* [Microsoft Azure DevOps](locales/zh/examples/microsoft-azure-devops/)
* [单仓库 vs 多仓库](locales/zh/examples/monorepo-vs-multirepo/)
* [编程语言](locales/zh/examples/programming-languages/)
* [密钥存储](locales/zh/examples/secrets-storage/)
* [时间戳格式](locales/zh/examples/timestamp-format/)
* [更多示例...](locales/zh/examples/)

[更多语言](locales/)


<div class="include" data-path="locales/zh/what-is-an-architecture-decision-record">

## 什么是架构决策记录？

**架构决策记录**（ADR）是一份记录重要架构决策及其背景和后果的文件。

**架构决策** (AD) 是满足重要需求的软件设计选择。

**架构决策日志** (ADL) 是为某个项目（或组织）创建和维护的所有 ADR 的集合。

**具体架构意义的重大需求**（ASR）是指对软件系统架构有可衡量的影响的需求。

所有这些都属于**架构知识管理**（AKM）的范畴。

本文件旨在快速介绍 ADR、如何创建 ADR 以及从何处获取更多信息。

缩略语：

  * **AD**: 架构决策

  * **ADL**: 架构决策日志

  * **ADR**: 架构决策记录

  * **AKM**: 架构知识管理

  * **ASR**: 具有架构意义的重大需求

</div>
