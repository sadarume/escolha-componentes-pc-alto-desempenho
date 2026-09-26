# Escolha de componentes para computador de alto desempenho

Sistema especialista didático em Python para recomendar uma configuração de PC de acordo com orçamento, objetivo, resolução, tipo de jogo, RAM e armazenamento.

O programa consulta uma pequena base de conhecimento no próprio código, aplica regras de desempenho e compatibilidade, verifica o orçamento e explica a recomendação. Permite refazer a consulta.

## Executar

Requer Python 3.10 ou mais recente e não usa bibliotecas externas.

```powershell
python "Escolha de componentes para computador de alto desempenho.py"
```

No Windows, também é possível usar `py -3.13` no lugar de `python`.

O arquivo [codigo_python.txt](codigo_python.txt) contém uma cópia do código para leitura em formato TXT. O [LEIA-ME.txt](LEIA-ME.txt) traz instruções resumidas.

## Limites da base

As configurações cadastradas são exemplos e cobrem faixas de preço ilustrativas entre R$ 3.500 e cerca de R$ 44.000. O sistema escolhe a melhor opção **entre as configurações cadastradas**, respeitando resolução, compatibilidade e orçamento. Os preços não são cotações de lojas e devem ser atualizados antes de orientar uma compra.

As categorias e regras de recomendação foram elaboradas para o projeto acadêmico. Algumas especificações de processadores e GPUs foram conferidas nas fichas dos fabricantes, como [AMD Ryzen 5 5500](https://www.amd.com/en/support/downloads/drivers.html/processors/ryzen/ryzen-5000-series/amd-ryzen-5-5500.html), [Radeon RX 6600](https://www.amd.com/en/products/graphics/desktops/radeon/6000-series/amd-radeon-rx-6600.html), [GeForce RTX 5080](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5080/) e [GeForce RTX 5090](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/). Placas-mãe, fontes e gabinetes são classes de referência: confirme o modelo exato e suas medidas e conectores antes de comprar.
