# Cantinho da Mio

Jogo de exploração e pequenos enigmas em pixel art, com uma cena fixa de **320×240**, personagem com spritesheet PNG, inventário de quatro espaços visíveis e controles adaptados a celular e desktop.

## Assets e execução

- `scripts/generate_assets.py` gera PNGs de arte original, pixel a pixel, usando apenas a biblioteca padrão do Python.
- `assets/room.png`, `assets/mio.png`, `assets/rain.png` e `assets/inventory.png` são gerados no workflow de validação e antes do deploy de GitHub Pages.
- Para testar localmente: `python3 scripts/generate_assets.py` e abra `index.html` por um servidor estático local. O `fetch()` dos poemas pode falhar se abrir como `file://`; use um servidor local.
- GitHub Pages é publicado como site estático, sem build de framework ou dependências npm.

## Controles

- Toque/click num objeto para caminhar até ele; setas/WASD ou D-pad para mover.
- Toque em item do inventário para selecioná-lo e depois toque num objeto para tentar combiná-los.
- **Home** fecha painéis; **Hint** destaca visualmente o próximo objeto; **Sound** liga/desliga a música; **Pause** pausa movimento e música.
- O caderno abre ao interagir com o caderno na escrivaninha. Páginas são desbloqueadas por pequenos enigmas.
- O rádio usa YouTube IFrame Player API, começa após gesto do jogador e tenta avançar no fim/erro. A reprodução real pode depender de disponibilidade regional e das restrições do YouTube.

## Conteúdo e limitações

- Os quatro poemas completos estão separados em `content/poems/poems.json` e o texto é preservado sem reescrita intencional.
- Os três arquivos antigos estão vazios porque o documento mestre só contém marcadores para inserir os originais. O jogo mostra `[texto original a inserir]` sem inventar versos.
- O Arquivo dos Caçadores e o Scrapbook antigos foram removidos do caminho principal para priorizar a mecânica de exploração e enigmas solicitada.
- A arte do quarto, móveis, personagem, chuva e ícones é placeholder original gerado por script; não foi copiado nenhum sprite do Undertale ou de outro jogo. É uma primeira versão funcional de pixel art, não arte final detalhada.
- A validação automatizada verifica sintaxe, dimensões e estrutura dos PNGs. Ela não substitui testes visuais em celular/desktop; a reprodução real de todas as faixas não pode ser garantida sem executar os vídeos em navegador.
- Não há analytics, pontuação, cronômetro, game over nem envio de dados pessoais.
