import math



PROCESSADORES = {
    "Ryzen 5 5500": {"preco": 650, "socket": "AM4", "ram": "DDR4", "nivel": 1,
                     "jogos": 1, "multitarefa": 1, "watts": 65, "cooler_incluso": True},
    "Ryzen 5 7600": {"preco": 1100, "socket": "AM5", "ram": "DDR5", "nivel": 1, "jogos": 2,
                     "multitarefa": 1, "watts": 65, "cooler_incluso": True},
    "Ryzen 7 7700": {"preco": 1650, "socket": "AM5", "ram": "DDR5", "nivel": 2, "jogos": 3,
                     "multitarefa": 3, "watts": 65, "cooler_incluso": True},
    "Ryzen 7 7800X3D": {"preco": 2300, "socket": "AM5", "ram": "DDR5", "nivel": 3, "jogos": 5,
                       "multitarefa": 3, "watts": 120, "cooler_incluso": False},
    "Ryzen 7 9800X3D": {"preco": 3500, "socket": "AM5", "ram": "DDR5", "nivel": 4,
                       "jogos": 6, "multitarefa": 3, "watts": 120, "cooler_incluso": False},
    "Ryzen 9 9950X3D": {"preco": 6500, "socket": "AM5", "ram": "DDR5", "nivel": 5,
                       "jogos": 5, "multitarefa": 6, "watts": 170, "cooler_incluso": False},
}

PLACAS_MAE = {
    "A520 mATX DDR4": {"preco": 400, "socket": "AM4", "ram": "DDR4", "formato": "mATX"},
    "B650 mATX DDR5": {"preco": 850, "socket": "AM5", "ram": "DDR5", "formato": "mATX"},
    "B650 ATX DDR5": {"preco": 1100, "socket": "AM5", "ram": "DDR5", "formato": "ATX"},
    "X870E ATX DDR5": {"preco": 2500, "socket": "AM5", "ram": "DDR5", "formato": "ATX"},
}

PLACAS_VIDEO = {
    "Radeon RX 6600": {"preco": 1300, "nivel": 1, "watts": 132, "fonte_min": 450,
                       "conectores": 1, "tamanho": 250, "streaming": 1},
    "Radeon RX 7600": {"preco": 1500, "nivel": 1, "watts": 165, "fonte_min": 550,
                       "conectores": 1, "tamanho": 204, "streaming": 1},
    "Radeon RX 7700 XT": {"preco": 2500, "nivel": 2, "watts": 245, "fonte_min": 700,
                          "conectores": 2, "tamanho": 267, "streaming": 1},
    "Radeon RX 7800 XT": {"preco": 3200, "nivel": 3, "watts": 263, "fonte_min": 700,
                          "conectores": 2, "tamanho": 267, "streaming": 1},
    "GeForce RTX 4070 SUPER": {"preco": 3900, "nivel": 3, "watts": 220, "fonte_min": 650,
                               "conectores": 2, "tamanho": 244, "streaming": 3},
    "Radeon RX 7900 XT": {"preco": 5400, "nivel": 4, "watts": 315, "fonte_min": 750,
                          "conectores": 2, "tamanho": 276, "streaming": 1},
    "GeForce RTX 4080 SUPER": {"preco": 7300, "nivel": 5, "watts": 320, "fonte_min": 750,
                               "conectores": 3, "tamanho": 304, "streaming": 3},
    "GeForce RTX 5080": {"preco": 12500, "nivel": 6, "watts": 360, "fonte_min": 850,
                         "conectores": 3, "tamanho": 304, "streaming": 4},
    "GeForce RTX 5090": {"preco": 30000, "nivel": 7, "watts": 575, "fonte_min": 1000,
                         "conectores": 4, "tamanho": 304, "streaming": 5},
}

FONTES = {
    "500 W Bronze": {"preco": 300, "watts": 500, "conectores": 1},
    "550 W Bronze": {"preco": 400, "watts": 550, "conectores": 1},
    "650 W Bronze": {"preco": 500, "watts": 650, "conectores": 2},
    "750 W Gold": {"preco": 700, "watts": 750, "conectores": 3},
    "1000 W Gold": {"preco": 1200, "watts": 1000, "conectores": 4},
    "1200 W Gold": {"preco": 1800, "watts": 1200, "conectores": 4},
}

GABINETES = {
    "mATX entrada": {"preco": 250, "formatos": ["mATX"],
                    "gpu_max": 300, "radiador_240": False, "radiador_360": False},
    "mATX ventilado": {"preco": 350, "formatos": ["mATX"],
                       "gpu_max": 300, "radiador_240": False, "radiador_360": False},
    "ATX ventilado": {"preco": 550, "formatos": ["mATX", "ATX"],
                      "gpu_max": 350, "radiador_240": True, "radiador_360": False},
    "ATX grande": {"preco": 1200, "formatos": ["mATX", "ATX"],
                   "gpu_max": 400, "radiador_240": True, "radiador_360": True},
}

PRECO_RAM = {"DDR4": {16: 300, 32: 550, 64: 1100},
             "DDR5": {16: 450, 32: 750, 64: 1450}}  # Kits de 2 módulos.
PRECO_SSD = {500: 300, 1000: 450, 2000: 800}  # SSDs NVMe M.2.
PRECO_COOLER = {"240 mm": 450, "360 mm": 800}  # Para CPU sem cooler incluso.


OPCOES = [
    {"nome": "entrada", "resolucoes": ["1080p"],
     "cpu": "Ryzen 5 5500", "placa": "A520 mATX DDR4",
     "gpu": "Radeon RX 6600", "fonte": "500 W Bronze", "gabinete": "mATX entrada"},
    {"nome": "básico", "resolucoes": ["1080p"],
     "cpu": "Ryzen 5 7600", "placa": "B650 mATX DDR5",
     "gpu": "Radeon RX 7600", "fonte": "550 W Bronze", "gabinete": "mATX ventilado"},
    {"nome": "equilibrado", "resolucoes": ["1080p", "1440p"],
     "cpu": "Ryzen 7 7700", "placa": "B650 mATX DDR5",
     "gpu": "Radeon RX 7700 XT", "fonte": "750 W Gold", "gabinete": "mATX ventilado"},
    {"nome": "foco em gráficos", "resolucoes": ["1440p"],
     "cpu": "Ryzen 7 7700", "placa": "B650 mATX DDR5",
     "gpu": "Radeon RX 7800 XT", "fonte": "750 W Gold", "gabinete": "mATX ventilado"},
    {"nome": "foco em streaming", "resolucoes": ["1440p"],
     "cpu": "Ryzen 7 7700", "placa": "B650 mATX DDR5",
     "gpu": "GeForce RTX 4070 SUPER", "fonte": "650 W Bronze", "gabinete": "mATX ventilado"},
    {"nome": "alto desempenho", "resolucoes": ["1440p"],
     "cpu": "Ryzen 7 9800X3D", "placa": "B650 ATX DDR5",
     "gpu": "Radeon RX 7900 XT", "fonte": "750 W Gold", "gabinete": "ATX ventilado"},
    {"nome": "foco em gráficos", "resolucoes": ["4K"],
     "cpu": "Ryzen 7 7800X3D", "placa": "B650 ATX DDR5",
     "gpu": "Radeon RX 7900 XT", "fonte": "750 W Gold", "gabinete": "ATX ventilado"},
    {"nome": "foco em streaming", "resolucoes": ["4K"],
     "cpu": "Ryzen 7 7800X3D", "placa": "B650 ATX DDR5",
     "gpu": "GeForce RTX 4080 SUPER", "fonte": "750 W Gold", "gabinete": "ATX ventilado"},
    {"nome": "alto desempenho", "resolucoes": ["4K"],
     "cpu": "Ryzen 7 9800X3D", "placa": "B650 ATX DDR5",
     "gpu": "GeForce RTX 5080", "fonte": "1000 W Gold", "gabinete": "ATX ventilado"},
    {"nome": "jogos e trabalho avançado", "resolucoes": ["4K"], "cooler": "360 mm",
     "cpu": "Ryzen 9 9950X3D", "placa": "X870E ATX DDR5",
     "gpu": "GeForce RTX 5080", "fonte": "1000 W Gold", "gabinete": "ATX grande"},
    {"nome": "premium", "resolucoes": ["4K"], "cooler": "360 mm",
     "cpu": "Ryzen 9 9950X3D", "placa": "X870E ATX DDR5",
     "gpu": "GeForce RTX 5090", "fonte": "1200 W Gold", "gabinete": "ATX grande"},
]


def perguntar(titulo, alternativas):
    print("\n" + titulo)
    for numero, item in enumerate(alternativas, 1):
        print(f"{numero}. {item}")
    while True:
        resposta = input("Escolha: ").strip()
        if resposta.isdigit() and 1 <= int(resposta) <= len(alternativas):
            return alternativas[int(resposta) - 1]
        print("Escolha um número válido.")


def reais(valor):
    return "R$ " + f"{valor:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")


def coletar_dados():
    while True:
        try:
            texto = input("Orçamento máximo em R$ (ex.: 8500): ").replace(",", ".")
            orcamento = float(texto)
            if math.isfinite(orcamento) and orcamento > 0:
                break
        except ValueError:
            pass
        print("Informe um orçamento maior que zero.")
    return {
        "orcamento": orcamento,
        "objetivo": perguntar("Objetivo", ["jogos", "jogos e streaming", "jogos e trabalho"]),
        "resolucao": perguntar("Resolução", ["1080p", "1440p", "4K"]),
        "jogos": perguntar("Tipo de jogo", ["competitivos", "AAA", "ambos"]),
        "ram": perguntar("RAM desejada", [16, 32, 64]),
        "ssd": perguntar("SSD desejado (GB)", [500, 1000, 2000]),
    }


def atende_requisitos(opcao, dados):
    """RN05-07, RI01-03: requisitos de desempenho do perfil."""
    if dados["resolucao"] not in opcao["resolucoes"]:
        return False
    cpu = PROCESSADORES[opcao["cpu"]]
    gpu = PLACAS_VIDEO[opcao["gpu"]]
    minimo_gpu = {"1080p": 1, "1440p": 2, "4K": 4}[dados["resolucao"]]
    maximo_gpu = {"1080p": 3, "1440p": 4, "4K": 7}[dados["resolucao"]]
    if dados["jogos"] in ("AAA", "ambos") and dados["resolucao"] == "1080p":
        minimo_gpu = 2
    if dados["resolucao"] == "1080p" and dados["orcamento"] <= 7000:
        maximo_gpu = 2  # RI01: em 1080p econômico, evitar GPU excessiva.
    if not minimo_gpu <= gpu["nivel"] <= maximo_gpu:
        return False
    if dados["objetivo"] == "jogos e streaming" and cpu["nivel"] < 2:
        return False
    return True


def compativel(opcao):
    """RN02-04, RN09 e RI04-06: rejeita peças incompatíveis."""
    cpu = PROCESSADORES[opcao["cpu"]]
    placa = PLACAS_MAE[opcao["placa"]]
    gpu = PLACAS_VIDEO[opcao["gpu"]]
    fonte = FONTES[opcao["fonte"]]
    gabinete = GABINETES[opcao["gabinete"]]
    consumo = cpu["watts"] + gpu["watts"] + 80  # Demais peças: 80 W estimados.
    return (
        cpu["socket"] == placa["socket"] and cpu["ram"] == placa["ram"]
        and placa["formato"] in gabinete["formatos"]
        and gpu["tamanho"] <= gabinete["gpu_max"]
        and fonte["watts"] >= max(gpu["fonte_min"], consumo * 1.3)
        and fonte["conectores"] >= gpu["conectores"]
        and (cpu["cooler_incluso"] or gabinete["radiador_360" if opcao.get("cooler") == "360 mm" else "radiador_240"])
    )


def custo(opcao, dados):
    cpu = PROCESSADORES[opcao["cpu"]]
    ram = dados["ram"]
    ssd = dados["ssd"]
    total = (cpu["preco"] + PLACAS_MAE[opcao["placa"]]["preco"]
             + PLACAS_VIDEO[opcao["gpu"]]["preco"] + FONTES[opcao["fonte"]]["preco"]
             + GABINETES[opcao["gabinete"]]["preco"]
             + PRECO_RAM[PLACAS_MAE[opcao["placa"]]["ram"]][ram] + PRECO_SSD[ssd])
    if not cpu["cooler_incluso"]:
        total += PRECO_COOLER[opcao.get("cooler", "240 mm")]
    return total, ram, ssd


def recomendar(dados):
    """Aplica regras à base; busca alternativa quando o orçamento falha."""
    melhor = None
    menor_custo = None
    for opcao in OPCOES:
        if not atende_requisitos(opcao, dados) or not compativel(opcao):
            continue
        total, ram, ssd = custo(opcao, dados)
        menor_custo = total if menor_custo is None else min(menor_custo, total)
        if total > dados["orcamento"]:  # RN01, RN08, RI07: procurar outra.
            continue
        cpu, gpu = PROCESSADORES[opcao["cpu"]], PLACAS_VIDEO[opcao["gpu"]]
        peso_cpu, peso_gpu = {"competitivos": (35, 20), "AAA": (15, 45),
                              "ambos": (25, 35)}[dados["jogos"]]
        nota = cpu["jogos"] * peso_cpu + gpu["nivel"] * peso_gpu
        if dados["objetivo"] == "jogos e streaming":
            nota += cpu["multitarefa"] * 15 + gpu["streaming"] * 10
        if dados["objetivo"] == "jogos e trabalho":
            nota += cpu["multitarefa"] * 20
        if melhor is None or (nota, -total) > (melhor[0], -melhor[2]):
            melhor = (nota, opcao, total, ram, ssd)
    return melhor, menor_custo


def mostrar_resultado(dados, resultado):
    melhor, menor_custo = resultado
    if melhor is None:
        print("\nNenhuma configuração compatível cabe no orçamento.")
        print("Orçamento informado:", reais(dados["orcamento"]))
        if menor_custo is not None:
            print("Menor custo que atende aos requisitos:", reais(menor_custo))
        return
    _, opcao, total, ram, ssd = melhor
    print("\n=== RECOMENDAÇÃO ===")
    print(f"Configuração: {dados['resolucao']} - {opcao['nome']}")
    for campo, rotulo in [("cpu", "Processador"), ("placa", "Placa-mãe"),
                          ("gpu", "Placa de vídeo"), ("fonte", "Fonte"),
                          ("gabinete", "Gabinete")]:
        print(f"{rotulo}: {opcao[campo]}")
    print(f"RAM: {ram} GB {PLACAS_MAE[opcao['placa']]['ram']} (2 módulos); SSD NVMe: {ssd} GB")
    print("Cooler:", "incluso com a CPU" if PROCESSADORES[opcao["cpu"]]["cooler_incluso"]
          else f"water cooler {opcao.get('cooler', '240 mm')} AM5")
    print(f"Custo estimado: {reais(total)}; saldo: {reais(dados['orcamento'] - total)}")
    print("Compatibilidade aprovada: socket, RAM, fonte, gabinete e cooler.")
    print(f"Justificativa: GPU de nível {PLACAS_VIDEO[opcao['gpu']]['nivel']} para {dados['resolucao']};"
          f" perfil de jogos {dados['jogos']} e objetivo {dados['objetivo']}.")
    print("Preços ilustrativos: atualize a base antes de comprar.")


def main():
    print("=== SISTEMA ESPECIALISTA PARA PC DE JOGOS ===")
    while True:  # RF12: permite refazer a consulta.
        dados = coletar_dados()
        mostrar_resultado(dados, recomendar(dados))
        if input("\nRefazer consulta? (s/n): ").strip().lower() not in ("s", "sim"):
            break


if __name__ == "__main__":
    main()
