# Cantinho da Mio

Jogo de exploração em pixel art, mobile-first, num quarto noturno. A cena é um canvas de baixa resolução (320×180) escalado com pixelização; o jogador pode andar com setas/WASD ou D-pad e interagir com janela, estante, rádio, caderno, mesa e segredos.

## Abrir e publicar

Abra `index.html` num navegador moderno. GitHub Pages publica o projeto como site estático, sem etapa de build ou dependências de pacote.

## Recursos

- Exploração do quarto em canvas, movimento em quatro direções e colisão com paredes/móveis.
- Janela com chuva/estrelas e luz pulsante; animação reduzida quando `prefers-reduced-motion` está ativo.
- Diálogo de RPG com efeito de escrita, botão para revelar o texto completo e escolhas simples.
- Controles por teclado e D-pad de toque, interação por proximidade, painel que fecha com Esc/B/X e retorno à posição anterior.
- Rádio usando a YouTube IFrame Player API: começa após o primeiro gesto do jogador, avança ao terminar, tenta pular erros, oferece play/pause e links de pesquisa no YouTube.
- Caderno com os quatro poemas completos do documento mestre. Os três antigos permanecem reservados.
- Estante, Arquivo dos Caçadores e scrapbook com adesivos móveis.
- Sem analytics, sem coleta de dados, sem pontuação ou game over.

## Limitações honestas

- A personagem usa um spritesheet original de 3 colunas × 4 direções em `assets/mio-sprites.svg`. O cenário e o tilemap são desenhados por código; nenhum pacote externo de tileset licenciado foi incorporado nesta revisão.
- Os IDs do YouTube não foram verificados individualmente em reprodução real. A API lida com eventos de erro quando são reportados, mas algumas restrições de vídeo podem variar por região/conta.
- Não foi possível testar o jogo num celular físico nesta sessão. A validação automática confere estrutura, IDs, integração declarada e sintaxe JS, não substitui teste visual/manual.
- Os três poemas antigos precisam dos textos originais antes de serem adicionados.
- O scrapbook não salva conteúdo depois que a página é fechada.

## Privacidade e acessibilidade

Não há analytics nem armazenamento remoto. A interface inclui foco visível, rótulos, controles de toque e teclado, áreas de toque grandes e suporte a movimento reduzido.
