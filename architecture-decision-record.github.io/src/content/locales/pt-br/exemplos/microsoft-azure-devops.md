# Microsoft Azure DevOps

Conteúdo:

* [Resumo](#resumo)
  * [Questão](#questão)
  * [Decisão](#decisão)
  * [Status](#status)
* [Detalhes](#detalhes)
  * [Premissas](#premissas)
  * [Restrições](#restrições)
  * [Posições](#posições)
  * [Argumento](#argumento)
  * [Implicações](#implicações)
* [Relacionado](#relacionado)
  * [Decisões relacionadas](#decisões-relacionadas)
  * [Requisitos relacionados](#requisitos-relacionados)
  * [Artefatos relacionados](#artefatos-relacionados)
  * [Princípios relacionados](#princípios-relacionados)
* [Notas](#notas)
  * [Microsoft Devops CI: uma aventura insatisfatória](#microsoft-devops-ci-uma-aventura-insatisfatória)
  * [Destaques da discussão no Hacker News](#destaques-da-discussão-no-hacker-news)
  * [Windows Development MVP](#windows-development-mvp)
  * [Resumo de Edward Thomson (Azure PM)](#resumo-de-edward-thomson-azure-pm)


## Resumo


### Questão

Queremos usar devops para fazer build, integrar, implantar e hospedar nossos projetos. Estamos considerando Microsoft Azure DevOps.

  * Queremos que a experiência do desenvolvedor seja rápida e confiável, para a configuração do devops, por exemplo configurar, bem como para o uso contínuo, por exemplo tempos de build rápidos.

  * Queremos considerar usar Microsoft Azure como um todo, para hospedar os apps, bancos de dados etc. do projeto.


### Decisão

Decidido contra Microsoft Azure DevOps.


### Status

Decidido. Aberto a revisitar se/quando novas informações significativas chegarem.


## Detalhes


### Premissas

Todas as premissas usuais de devops, como no livro Accelerate.

  * Builds rápidos são uma ajuda significativa. Isso acelera os loops de feedback.

  * Podemos trocar peças de/para fornecedores alternativos, isto é, podemos querer trazer nossos servidores de build de maior velocidade, ou usar nossa própria escolha de sistema de controle de versão, ou coordenar com um servidor de integração contínua auto-hospedado.

  * Usabilidade simplificada é uma ajuda significativa para a experiência do desenvolvedor e, por sua vez, para áreas sutis como consistência, clareza, segurança e facilidade da curva de aprendizado.

  * Quando algo está quebrado ou problemático, queremos uma forma efetiva de relatar o problema. Isso é especialmente importante para quaisquer problemas relacionados a segurança.


### Restrições

Nenhuma conhecida. Azure tem um compromisso publicado de funcionar bem com ferramentas externas.


### Posições

Consideramos usar Microsoft Azure Devops vs. AWS, que é o incumbente.

Experimentamos Azure DevOps, Azure Pipelines, Azure Repo e o spin up de novo servidor Azure via Terraform.

Experimentamos obter suporte de representantes da Microsoft.

Coletamos informações de pares em blogs e no Hacker News.


### Argumento

Azure DevOps anuncia um excelente conjunto de ofertas, mas elas não se sustentam, não funcionam bem juntas e o suporte é ruim.

Nossa experiência em primeira mão:

  * A configuração do Azure é uma bagunça de UIs, algumas das quais se sobrepõem a contas Microsoft, algumas não. Por exemplo, há um login Azure, um login Microsoft.com, um login Live.com etc., e todos estão simultaneamente em jogo.

  * Encontramos um problema menor de segurança durante a configuração e não encontramos resolução. Tentamos muitas formas de relatá-lo, a muitos representantes da Microsoft, sem sucesso. Conseguimos relatá-lo à segurança da Microsoft, que respondeu com não vai corrigir.

  * A documentação frequentemente está errada ou desatualizada. Pelo menos parte disso se deve ao mecanismo de busca ruim da Microsoft, e parte disso se deve a SEO abaixo do ideal.

  * A configuração do Terraform é bem documentada e funciona. No entanto, o suporte a Terraform é fraco em comparação com AWS porque a Microsoft está construindo relacionamentos de negócio com fornecedores para fazer exemplos encadeados de configuração com Terraform.

Nossas experiências de pares:

  * Depois que fizemos nossa própria avaliação às cegas, procuramos experiências de pares. O que encontramos confirmou nossas experiências.

  * Pares relataram problemas adicionais com tempos de build e problemas com trazer seu próprio servidor de build. Esses problemas são significativamente mais graves do que problemas de UI, porque fazer builds é o propósito central de um pipeline de build, e esperamos fazer muitos por dia.

  * Encontramos excelente participação de colegas da Azure nas áreas de discussão. Parabéns à Microsoft por isso. Estamos especialmente impressionados com Edward Thomson, Azure PM e coder, por causa de sua participação, franqueza e explicações técnicas.


### Implicações

Escolher Microsoft Azure DevOps parece provavelmente ser mais caro (~3x) em tempo e custo do que não escolher Azure.


## Relacionado


### Decisões relacionadas

Se escolhermos Azure DevOps, há muitas ofertas relacionadas, incluindo Azure Repo, Azure Pipeline etc. Acreditamos que, se escolhermos Azure Devops, isso pode tornar mais fácil usar mais capacidades Azure, ou pode tornar mais difícil usar capacidades de outros fornecedores.

Acreditamos que a Microsoft está dando grandes passos em experiência do desenvolvedor, e vemos a Microsoft fazendo grandes aquisições de ferramentas de desenvolvedor (por exemplo, GitHub) e dependências (por exemplo, Citus).

Se escolhermos Azure DevOps, então talvez queiramos enfatizar a escolha das ofertas de aquisição da Microsoft, e talvez também queiramos abordar as ofertas de aquisição com mais cuidado/avaliação por causa de potencial rejeição de tecido, por exemplo risco de rotatividade de equipe.


### Requisitos relacionados

Queremos que os tempos de build sejam muito rápidos. Aceitamos pagar um prêmio alto por isso. Isso porque queremos iterar muito rápido.

Queremos que a confiabilidade seja muito alta. Aceitamos pagar um prêmio alto por isso. Isso porque estamos testando casos de uso de alto valor, incluindo transações financeiras, transações confidenciais etc.

Nossos 4 principais KPIs de devops incluem tempo médio de recuperação, o que necessita de builds rápidos e alta confiabilidade.


### Artefatos relacionados

Queremos que o sistema de build gere artefatos adequados para uso em outros sistemas, como Artifactory.


### Princípios relacionados

Facilmente reversível. Podemos avaliar Azure DevOps em paralelo com o incumbente AWS.


## Notas


### Microsoft Devops CI: uma aventura insatisfatória

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

Post de blog.

"Como desenvolvedor de software, sei em primeira mão o quanto é difícil construir produtos de qualidade de forma rápida e barata. É uma forma de arte que às vezes acertamos, e em outras vezes degrada para algo parecido com o site governamental de saúde da era Obama. Nosso nível de controle sobre o produto resultante varia, e a culpa pelo fracasso muitas vezes recai sobre as pessoas erradas na hierarquia de tomada de decisão. O Azure DevOps da Microsoft (anteriormente conhecido como Visual Studio Team Services), apesar de intenções claramente boas, é uma tempestade perfeita de decisões ruins e execução pobre."


### Destaques da discussão no Hacker News

https://news.ycombinator.com/item?id=18983586

"Usamos Azure DevOps extensivamente no meu trabalho e, depois de ter usado GitHub, Gitlab, soluções auto-hospedadas, Jenkins, TeamCity... Azure DevOps fica em último lugar."

"A UI é terrivelmente desajeitada em todos os lugares. O pior para mim são pull requests. Incrivelmente difícil trabalhar com pessoas em um pull request. Eu nem consigo apontar para "um" problema em particular - para nós está quebrado em todos os lugares."

"Azure Devops é algo que eu quero amar. A UI continua mudando, mas não corrige bugs subjacentes que existem há anos."

"As ferramentas não são bem integradas, a UI é realmente lenta, não há visualização de dashboard de pull requests, builds, releases etc. ativos para meus repos favoritos. Tempos de build/deploy são insanamente lentos."

"Tentamos também usar Azure Boards (Work Items, Boards, Backlogs etc.). Ai. É uma bagunça completa de UI de ideias desconexas. Em vez de implementar uma coisa bem, eles implementaram duas dúzias de coisas terrivelmente."


### Windows Development MVP

Windows Development MVP aqui. Sinto que devo assumir parte da responsabilidade aqui por não ter sido mais vocal sobre esses problemas. Mas preciso dizer, estou decepcionado ao ouvir que vocês estão "surpresos" com os problemas de UX. Venho dizendo ao seu pessoal que a UX é horrível (por exemplo, desde antes do lançamento) e continuei ouvindo de volta "sabemos, estamos corrigindo". Vou começar a formalizar o feedback e empurrá-lo pelos canais, aguardem. Também sou local (Bellevue), adoraria ir aí e tentar fazer pipeline do nosso app oss .net/wpf/uwp relativamente simples. Suspeito que será uma revelação para nós dois.

Alguns exemplos:

* Você não consegue construir um pipeline com um repo git que contém submódulos

* Achei impossível editar o PATH para algum ferramental customizado

* A experiência New Pipeline simplesmente não faz muito sentido; novos usuários clicando por aí acabarão eventualmente nos Docs errados.


### Resumo de Edward Thomson (Azure PM)

Escrevi o código que faz merge dos seus pull requests. Program Manager na Microsoft para Azure DevOps; anteriormente engenheiro de software em ferramentas de controle de versão no GitHub, Microsoft, SourceGear.

https://www.edwardthomson.com/

Co-mantenedor da libgit2. https://libgit2.github.io

Co-host de All Things Git, o Podcast sobre Git. https://www.allthingsgit.com/

Curador de Developer Tools Weekly, uma newsletter sobre ferramentas de desenvolvimento. https://developertoolsweekly.com/
