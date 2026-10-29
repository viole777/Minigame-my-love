# Cantinho da Mio

Jogo de puzzle point-and-click em um quarto ilustrado. Não há personagem para movimentar: toque diretamente nos objetos, investigue, encontre itens e combine-os com outros objetos para desbloquear páginas do caderno.

## Jogabilidade

- Toque em um objeto do cenário para abrir sua inspeção.
- Use **Investigar** para procurar itens ou descobrir pistas.
- Toque em um item do inventário para selecioná-lo; depois investigue outro objeto para tentar usá-lo.
- **Dica** mostra uma pista do próximo enigma.
- **Caderno** reúne os poemas encontrados.
- **Rádio** abre a seleção musical.
- **Reiniciar** limpa o progresso da sessão.

A interface se adapta a celular e desktop. O cenário usa ilustração vetorial feita em CSS, sem pixel art, joystick ou movimentação de personagem.

## Música

A lista oficial contém somente as seis faixas solicitadas em [MUSICAS.md](MUSICAS.md). A reprodução usa a YouTube IFrame Player API; disponibilidade e reprodução em segundo plano dependem do YouTube e do navegador. Se uma faixa não tocar incorporada, o link abre a faixa no YouTube.

## Poemas

Os quatro poemas completos permanecem em `content/poems/poems.json`. Os três primeiros dependem dos textos originais, que não estão presentes nos arquivos atuais; o jogo não inventa nem substitui esses poemas.

## Execução

O projeto é estático e pode ser publicado no GitHub Pages. Para testar localmente, sirva a pasta por um servidor HTTP para que o navegador consiga carregar os arquivos JSON e TXT.
