def chunk_woorden(tekst: str, grootte: int, overlap: int) -> list[str]:
    if overlap >= grootte:
        raise ValueError("Overlap moet kleiner zijn dan chunkgrootte")
    woorden = tekst.split()
    stap = grootte - overlap
    return [" ".join(woorden[i:i + grootte]) for i in range(0, len(woorden), stap)]

# Simuleer een beleidsdocument met herkenbare secties.
secties = [
    "Doel en reikwijdte van het informatiebeveiligingsbeleid.",
    "Identiteitsbeheer vereist MFA en periodieke toegangsreviews.",
    "Incidenten moeten binnen vastgestelde termijnen worden gemeld.",
    "Leveranciers worden beoordeeld op beveiliging en continuïteit.",
]
tekst = " ".join(secties * 400)

for grootte, overlap in [(200, 40), (1200, 120)]:
    chunks = chunk_woorden(tekst, grootte, overlap)
    gemiddelde = sum(len(c.split()) for c in chunks) / len(chunks)
    print(f"grootte={grootte}, overlap={overlap}, aantal={len(chunks)}, gemiddeld={gemiddelde:.1f}")
