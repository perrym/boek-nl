from dataclasses import dataclass

@dataclass
class EmailConcept:
    ontvanger: str
    onderwerp: str
    tekst: str
    bevat_gevoelige_data: bool
    goedgekeurd: bool = False


def verzend(email: EmailConcept) -> None:
    if email.bevat_gevoelige_data and not email.goedgekeurd:
        raise PermissionError("Menselijke goedkeuring is vereist")
    print(f"SIMULATIE: e-mail verzonden naar {email.ontvanger}")

concept = EmailConcept(
    ontvanger="leverancier@example.com",
    onderwerp="Technisch resultaat",
    tekst="Bijgevoegd staat de conceptanalyse.",
    bevat_gevoelige_data=True,
)

try:
    verzend(concept)
except PermissionError as fout:
    print("Geblokkeerd:", fout)

concept.goedgekeurd = True
verzend(concept)
