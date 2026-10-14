# Registro de Decisão de Arquitetura para Google Cloud Platform

## Contexto

Google Cloud Platform (GCP) é uma plataforma proeminente de cloud computing que oferece vários serviços de cloud, incluindo soluções de computação, armazenamento e rede. Esta ADR visa documentar as decisões de arquitetura tomadas para desenvolver e implementar uma infraestrutura baseada em GCP para nossa organização.

## Decisão

Nossa organização decidiu usar Google Cloud Platform como a infraestrutura de cloud para nossa aplicação. As principais considerações para esta decisão são:

   - Custo-benefício

   - Escalabilidade

   - Confiabilidade

   - Flexibilidade

## Seleções

Os seguintes serviços da GCP foram selecionados para atender aos nossos requisitos:

   - Compute Engine para máquinas virtuais e recursos de computação

   - Cloud Storage para armazenamento de objetos e hospedagem de arquivos

   - Cloud SQL para serviço gerenciado de banco de dados

   - Firebase para desenvolvimento e hospedagem de apps

## Justificativa

   - Custo-benefício: Google Cloud Platform é altamente custo-efetiva em comparação com outras plataformas de cloud, tornando-se uma opção atraente para organizações com restrições de orçamento.

   - Escalabilidade: A infraestrutura fácil de escalar da GCP permite lidar com qualquer quantidade de tráfego em tempo real.

   - Confiabilidade: Os serviços gerenciados da GCP oferecem alta confiabilidade, com backups automatizados e capacidades de recuperação de desastres que garantem alta disponibilidade de recursos e dados.

   - Flexibilidade: A plataforma fornece várias ferramentas e serviços em diferentes domínios, como IA, análise de dados e IoT, tornando-a altamente versátil.

## Consequências

Migrar para Google Cloud Platform exigirá treinar nossas equipes nos serviços da GCP, rearquitetar a aplicação para ser compatível com os serviços selecionados e atualizar o código de infraestrutura para suportar serviços GCP. No entanto, espera-se que, quando a migração for concluída, tenhamos uma infraestrutura altamente escalável, confiável e custo-efetiva para hospedar nossa aplicação. Além disso, precisaremos gerenciar os custos contínuos de provisionamento de recursos na GCP.

## Conclusão

Google Cloud Platform é uma excelente escolha para nossa infraestrutura de cloud devido ao seu custo-benefício, escalabilidade, confiabilidade e flexibilidade. Ao utilizar os serviços selecionados, podemos fornecer uma infraestrutura altamente disponível e robusta para nossa aplicação.
