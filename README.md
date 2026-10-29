# Cantinho do meu amor

Quarto interativo em pixel art, pensado primeiro para celular, com atmosfera noturna azulada, janela alternável entre chuva e céu estrelado, rádio manual, caderno de poemas, estante com bilhetes e dois minijogos.

## Como abrir

- Abra `index.html` em um navegador moderno.
- Para publicar como site estático, habilite GitHub Pages nas configurações do repositório e selecione a branch `main` e a pasta raiz.
- Não há etapa de build nem dependências de pacote.

## O que está implementado

- Cena principal com layout responsivo e preferência por movimento reduzido.
- Janela com alternância entre chuva e céu estrelado.
- Rádio com seis faixas, seleção e botões anterior/próxima; nunca inicia áudio automaticamente. Os IDs de vídeo são candidatos e ainda precisam ser verificados manualmente; o player pode ser bloqueado pelo YouTube, e há link alternativo para abrir a faixa.
- Caderno com os quatro poemas completos disponíveis no documento de referência, sem acrescentar os três poemas antigos cujo conteúdo integral não estava disponível.
- Estante com mensagens opcionais.
- Arquivo dos Caçadores, com pistas interativas e conclusão narrativa sem cronômetro.
- Scrapbook com adesivos que podem ser arrastados e removidos.
- Segredo opcional, painéis fecháveis, foco visível e textos em português.

## Limitações conhecidas

- Os três poemas antigos reservados no documento de referência precisam ser fornecidos pelo autor antes de serem incluídos; o conteúdo não foi inventado.
- O funcionamento e a disponibilidade dos vídeos incorporados não foram verificados automaticamente.
- O scrapbook existe apenas durante a sessão do navegador: não envia dados nem persiste conteúdo.
- A arte do quarto é construída com CSS e formas originais, não é uma ilustração pixel art detalhada desenhada à mão.

## Privacidade e acessibilidade

Não há analytics nem coleta de dados pessoais. O áudio não toca automaticamente. A interface inclui foco de teclado visível, rótulos acessíveis, áreas de toque e respeito a `prefers-reduced-motion`.
