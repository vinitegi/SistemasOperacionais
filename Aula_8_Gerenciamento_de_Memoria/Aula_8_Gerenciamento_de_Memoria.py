def fifo(paginas, quantidade_frames):
    memoria = []
    faltas = 0
    hits = 0

    print("\n===== FIFO =====")

    for pagina in paginas:

        if pagina in memoria:
            hits += 1
            resultado = "HIT"

        else:
            faltas += 1
            resultado = "PAGE FAULT"

            if len(memoria) >= quantidade_frames:
                memoria.pop(0)

            memoria.append(pagina)

        print(f"Página {pagina:<2} -> {str(memoria):<15} {resultado}")

    total = faltas + hits
    taxa_fault = (faltas / total) * 100
    taxa_hit = (hits / total) * 100

    print("\nResultado FIFO")
    print("Page Faults:", faltas)
    print("Hits:", hits)
    print(f"Taxa de Faults: {taxa_fault:.2f}%")
    print(f"Taxa de Hits: {taxa_hit:.2f}%")

    return faltas, hits


def lru(paginas, quantidade_frames):
    memoria = []
    faltas = 0
    hits = 0

    print("\n===== LRU =====")

    for pagina in paginas:

        if pagina in memoria:
            hits += 1
            resultado = "HIT"

            memoria.remove(pagina)
            memoria.append(pagina)

        else:
            faltas += 1
            resultado = "PAGE FAULT"

            if len(memoria) >= quantidade_frames:
                memoria.pop(0)

            memoria.append(pagina)

        print(f"Página {pagina:<2} -> {str(memoria):<15} {resultado}")

    total = faltas + hits
    taxa_fault = (faltas / total) * 100
    taxa_hit = (hits / total) * 100

    print("\nResultado LRU")
    print("Page Faults:", faltas)
    print("Hits:", hits)
    print(f"Taxa de Faults: {taxa_fault:.2f}%")
    print(f"Taxa de Hits: {taxa_hit:.2f}%")

    return faltas, hits


entrada = input("Digite as páginas separadas por espaço: ")
paginas = [int(valor) for valor in entrada.split()]

quantidade_frames = int(input("Digite a quantidade de frames: "))

print("\nSequência:", paginas)
print("Frames:", quantidade_frames)

faltas_fifo, hits_fifo = fifo(paginas, quantidade_frames)
faltas_lru, hits_lru = lru(paginas, quantidade_frames)

print("\n===== COMPARAÇÃO FINAL =====")

if faltas_fifo < faltas_lru:
    print("FIFO teve menos Page Faults.")
elif faltas_lru < faltas_fifo:
    print("LRU teve menos Page Faults.")
else:
    print("FIFO e LRU tiveram a mesma quantidade de Page Faults.")

print(f"\nFIFO -> Faults: {faltas_fifo} | Hits: {hits_fifo}")
print(f"LRU  -> Faults: {faltas_lru} | Hits: {hits_lru}")