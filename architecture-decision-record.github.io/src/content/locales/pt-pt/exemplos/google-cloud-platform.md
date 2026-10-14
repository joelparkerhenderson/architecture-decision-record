# Registro de decisão de arquitetura para o Google Cloud Platform

## Contexto

O Google Cloud Platform (GCP) é uma plataforma de computação em nuvem de destaque que oferece vários serviços de nuvem, incluindo soluções de computação, armazenamento e rede. Este ADR visa documentar as decisões de arquitetura tomadas para desenvolver e implementar uma infraestrutura baseada em GCP para a nossa organização.

## Decisão

Nossa organização decidiu usar o Google Cloud Platform como infraestrutura de nuvem para a nossa aplicação. As principais considerações para essa decisão são:

   - Custo-benefício

   - Escalabilidade

   - Confiabilidade

   - Flexibilidade

## Seleções

Os seguintes serviços do GCP foram selecionados para atender aos nossos requisitos:

   - Compute Engine para máquinas virtuais e recursos de computação

   - Cloud Storage para armazenamento de objetos e hospedagem de arquivos

   - Cloud SQL para serviço de banco de dados gerenciado

   - Firebase para desenvolvimento e hospedagem de apps

## Justificativa

   - Custo-benefício: o Google Cloud Platform é altamente econômico em comparação com outras plataformas de nuvem, o que o torna uma opção atraente para organizações com restrições orçamentárias.

   - Escalabilidade: a infraestrutura facilmente escalável do GCP permite lidar com qualquer volume de tráfego em tempo real.

   - Confiabilidade: os serviços gerenciados do GCP oferecem alta confiabilidade, com backups automatizados e capacidades de recuperação de desastres que garantem alta disponibilidade de recursos e dados.

   - Flexibilidade: a plataforma fornece diversas ferramentas e serviços em diferentes domínios, como IA, análise de dados e IoT, o que a torna altamente versátil.

## Consequências

Migrar para o Google Cloud Platform exigirá treinar nossas equipes nos serviços do GCP, reprojetar a arquitetura da aplicação para ser compatível com os serviços selecionados e atualizar o código de infraestrutura para dar suporte aos serviços do GCP. No entanto, espera-se que, uma vez concluída a migração, tenhamos uma infraestrutura altamente escalável, confiável e econômica para hospedar nossa aplicação. Além disso, precisaremos gerenciar os custos contínuos de provisionamento de recursos no GCP.

## Conclusão

O Google Cloud Platform é uma excelente escolha para a nossa infraestrutura de nuvem devido ao seu custo-benefício, escalabilidade, confiabilidade e flexibilidade. Ao utilizar os serviços selecionados, podemos fornecer uma infraestrutura altamente disponível e robusta para a nossa aplicação.
