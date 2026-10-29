# Cantinho da Mio

Experiência point-and-click em um quarto ilustrado em 2D. O cenário é uma ilustração SVG original do projeto; os objetos são acessados diretamente por áreas interativas, sem personagem, joystick ou movimentação.

## Recursos

- Quarto ilustrado responsivo, com pontos de interação para janela, cama, cômoda, estante, mesa, caderno e rádio.
- Inventário com seleção e uso de itens em objetos.
- **Arquivo dos Caçadores:** investigação de pistas e escolha de hipótese, sem cronômetro ou penalidades.
- **Scrapbook da Kássia:** composição de uma página com recortes que podem ser adicionados e removidos.
- Caderno com os quatro poemas completos presentes no arquivo de conteúdo.
- Rádio com as seis faixas solicitadas. Cada faixa abre uma busca correspondente no YouTube; a reprodução não é automática e depende da plataforma externa.
- Interface adaptada a telas pequenas, foco de teclado visível e respeito à preferência por movimento reduzido.

## Conteúdo

Os poemas são carregados de `content/poems/poems.json` e mantidos sem reescrita. O projeto não cria textos para poemas cujos originais não estão disponíveis.

A lista musical está documentada em [MUSICAS.md](MUSICAS.md).

## Execução

Projeto estático, sem etapa de build. Abra `index.html` por um servidor HTTP local ou publique a raiz do repositório no GitHub Pages para que o JSON de poemas seja carregado corretamente.
