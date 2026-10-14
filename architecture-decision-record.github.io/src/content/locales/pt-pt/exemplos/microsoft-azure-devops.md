# Microsoft Azure DevOps

Sumário:

* [Resumo](#resumo)
  * [Questão](#questão)
  * [Decisão](#decisão)
  * [Estado](#estado)
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
  * [Resumo de Edward Thomson (gerente de produto do Azure)](#resumo-de-edward-thomson-gerente-de-produto-do-azure)


## Resumo


### Questão

Queremos usar devops para fazer o build, integrar, implantar e hospedar nossos projetos. Estamos considerando o Microsoft Azure DevOps.

  * Queremos que a experiência do desenvolvedor seja rápida e confiável, tanto na configuração do devops, p. ex., configurar, quanto no uso contínuo, p. ex., tempos de build rápidos.
  
  * Queremos considerar o uso do Microsoft Azure como um todo, para hospedar os apps do projeto, bancos de dados etc.


### Decisão

Decidido contra o Microsoft Azure DevOps.


### Estado

Decidido. Abertos a revisitar se/quando chegarem novas informações significativas.


## Detalhes


### Premissas

Todas as premissas usuais de devops, como as do livro Accelerate.

  * Builds rápidos são uma ajuda significativa. Isso acelera os ciclos de feedback.

  * Podemos trocar peças de fornecedores alternativos, ou seja, talvez queiramos trazer nossos próprios servidores de build de maior velocidade, ou usar o sistema de controle de versão de nossa escolha, ou coordenar com um servidor de integração contínua auto-hospedado.
  
  * Usabilidade simplificada é uma ajuda significativa, para a experiência do desenvolvedor e, por sua vez, para áreas sutis como consistência, clareza, segurança e facilidade da curva de aprendizado.

  * Quando algo estiver quebrado ou problemático, queremos uma forma eficaz de relatar o problema. Isso é especialmente importante para quaisquer questões relacionadas à segurança.


### Restrições

Nenhuma conhecida. O Azure tem um compromisso publicado de se dar bem com ferramentas externas.


### Posições

Consideramos usar o Microsoft Azure Devops em vez da AWS, que é a incumbente.

Experimentamos o Azure DevOps, o Azure Pipelines, o Azure Repo e a criação de um novo servidor no Azure via Terraform.

Experimentamos obter suporte de representantes da Microsoft.

Reunimos informações de pares em blogs e no Hacker News.


### Argumento

O Azure DevOps anuncia um excelente conjunto de ofertas, mas elas não se sustentam, não funcionam bem em conjunto e o suporte é ruim.

Nossa experiência de primeira mão:

  * A configuração do Azure é uma bagunça de UIs, algumas das quais se sobrepõem a contas Microsoft, outras não. P. ex., há um login do Azure, um login do Microsoft.com, um login do Live.com etc., e todos estão em jogo simultaneamente.

  * Encontramos um problema de segurança menor durante a configuração e não achamos resolução. Tentamos muitas formas de relatá-lo, a muitos representantes da Microsoft, sem sucesso. Conseguimos relatá-lo à equipe de segurança da Microsoft, que respondeu que não seria corrigido (won't fix).

  * A documentação costuma estar errada ou desatualizada. Pelo menos parte disso se deve ao mecanismo de busca ruim da Microsoft, e parte ao SEO abaixo do padrão.
  
  * A configuração do Terraform é bem documentada e funciona. No entanto, o suporte ao Terraform é fraco em comparação com a AWS, porque a Microsoft está construindo relações comerciais com fornecedores para fazer exemplos de configuração do Terraform em cadeia.

Experiências de nossos pares:

  * Depois de fazermos nossa própria avaliação às cegas, procuramos experiências de pares. O que encontramos confirmou nossas experiências.

  * Os pares relataram problemas adicionais com tempos de build e problemas com servidor de build próprio (bring-your-own). Esses problemas são significativamente mais graves do que problemas de UI, porque fazer builds é o propósito central de um pipeline de build, e esperamos fazer muitos por dia.

  * Encontramos excelente participação de colegas do Azure nas áreas de discussão. Parabéns à Microsoft por isso. Ficamos especialmente impressionados com Edward Thomson, gerente de produto e programador do Azure, por sua participação, franqueza e explicações técnicas.


### Implicações

Escolher o Microsoft Azure DevOps parece provável de ser mais caro (~3x) em tempo e custo do que não escolher o Azure.


## Relacionado


### Decisões relacionadas

Se escolhermos o Azure DevOps, há muitas ofertas relacionadas, incluindo Azure Repo, Azure Pipeline etc. Acreditamos que, se escolhermos o Azure Devops, isso pode facilitar o uso de mais capacidades do Azure, ou pode dificultar o uso de capacidades de outros fornecedores.

Acreditamos que a Microsoft está dando grandes passos na experiência do desenvolvedor, e vemos a Microsoft fazendo grandes aquisições de ferramentas para desenvolvedores (p. ex., GitHub) e dependências (p. ex., Citus).

Se escolhermos o Azure DevOps, talvez queiramos dar ênfase a escolher as ofertas adquiridas pela Microsoft, e também talvez queiramos abordar as ofertas adquiridas com mais cuidado/avaliação por causa de potencial rejeição de tecido, p. ex., risco de rotatividade de pessoal.


### Requisitos relacionados

Queremos tempos de build muito rápidos. Aceitamos pagar um prêmio alto por isso. Isso porque queremos iterar muito rápido.

Queremos confiabilidade muito alta. Aceitamos pagar um prêmio alto por isso. Isso porque estamos testando casos de uso de alto valor, incluindo transações financeiras, transações confidenciais etc.

Nossos 4 principais KPIs de devops incluem o tempo médio de recuperação, o que exige builds rápidos e alta confiabilidade.


### Artefatos relacionados

Queremos que o sistema de build produza artefatos adequados para uso em outros sistemas, como o Artifactory.


### Princípios relacionados

Facilmente reversível. Podemos avaliar o Azure DevOps em paralelo com a AWS incumbente.


## Notas


### Microsoft Devops CI: uma aventura insatisfatória

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

Post de blog.

“Como desenvolvedor de software, sei por experiência própria como é difícil construir produtos de qualidade com rapidez e baixo custo. É uma forma de arte que às vezes acertamos, e outras vezes se degrada em algo parecido com o site do governo de saúde da era Obama. Nosso nível de controle sobre o produto resultante varia, e a culpa pelo fracasso muitas vezes recai sobre as pessoas erradas na hierarquia de tomada de decisão. O Azure DevOps da Microsoft (antes conhecido como Visual Studio Team Services), apesar de intenções claramente boas, é uma tempestade perfeita de más decisões e execução ruim.”


### Destaques da discussão no Hacker News

https://news.ycombinator.com/item?id=18983586

“Usamos o Azure DevOps extensivamente no meu trabalho e, depois de usar GitHub, Gitlab, soluções auto-hospedadas, Jenkins, TeamCity... o Azure DevOps fica em último lugar.”

“A UI é terrivelmente desajeitada em todo lugar. O pior para mim são os pull requests. É incrivelmente difícil trabalhar com pessoas em um pull request. Nem consigo apontar “um” problema específico - para nós está quebrado em todo lugar.”

“O Azure Devops é algo que eu quero amar. A UI não para de mudar, mas não corrige bugs subjacentes que existem há muito tempo.”

“As ferramentas não são bem integradas, a UI é muito lenta, não há visão de painel dos pull requests ativos, builds, releases etc. dos meus repositórios favoritos. Os tempos de build/implantação são absurdamente lentos.”

“Também tentamos usar o Azure Boards (Work Items, Boards, Backlogs etc.). Ai. É uma bagunça completa de UI com ideias desconexas. Em vez de implementar uma coisa bem, eles implementaram duas dúzias de coisas mal.”


### Windows Development MVP

Windows Development MVP aqui. Sinto que devo assumir parte da responsabilidade por não ter sido mais barulhento sobre esses problemas. Mas devo dizer que estou decepcionado ao ouvir que vocês estão “surpresos” com os problemas de UX. Venho dizendo à sua equipe que a UX é terrível (p. ex., desde antes do lançamento) e continuava ouvindo de volta “sabemos, estamos consertando”. Vou começar a formalizar o feedback e encaminhá-lo pelos canais, fiquem atentos. Também sou local (Bellevue), adoraria ir aí e tentar passar nosso app .net/wpf/uwp open source, relativamente simples, por um pipeline. Suspeito que vai abrir os olhos de nós dois.

Alguns exemplos:

* Não dá para montar um pipeline com um repositório git que contenha submódulos

* Achei impossível editar o PATH para algumas ferramentas personalizadas

* A experiência de New Pipeline não faz muito sentido; novos usuários clicando por aí acabarão na documentação errada.


### Resumo de Edward Thomson (gerente de produto do Azure)

Eu escrevi o código que faz o merge dos seus pull requests. Gerente de programas na Microsoft para o Azure DevOps; anteriormente engenheiro de software em ferramentas de controle de versão no GitHub, na Microsoft e na SourceGear.

https://www.edwardthomson.com/

Co-mantenedor do libgit2. https://libgit2.github.io

Coapresentador do All Things Git, o podcast sobre Git. https://www.allthingsgit.com/

Curador do Developer Tools Weekly, uma newsletter sobre ferramentas de desenvolvimento. https://developertoolsweekly.com/
