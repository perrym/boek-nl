from dataclasses import dataclass
from enum import Enum


class Verdict(str, Enum):
    SUPPORTED = "SUPPORTED"
    UNCERTAIN = "UNCERTAIN"
    INSUFFICIENT_EVIDENCE = "INSUFFICIENT_EVIDENCE"


@dataclass(frozen=True)
class Case:
    case_id: str
    claim: str
    evidence: list[str]
    evidence_supports_claim: bool
    retrieval_relevant: bool


CASES = [
    Case("C1", "Logging is actief.", ["Configuratie: logging=true"], True, True),
    Case("C2", "MFA is verplicht.", ["Policy: MFA required"], True, True),
    Case("C3", "De server staat in Amsterdam.", ["Geen locatie vermeld"], False, True),
    Case("C4", "Alle accounts zijn veilig.", ["MFA is actief voor beheerders"], False, True),
    Case("C5", "Retentie is 90 dagen.", ["Document over wachtwoordbeleid"], False, False),
    Case("C6", "De dataset is volledig.", [], False, True),
]


def baseline_classify(case: Case) -> tuple[Verdict, str]:
    if not case.evidence:
        return Verdict.INSUFFICIENT_EVIDENCE, "Geen bewijs beschikbaar"

    if not case.retrieval_relevant:
        return Verdict.INSUFFICIENT_EVIDENCE, "Opgehaalde bron is niet relevant"

    if case.evidence_supports_claim:
        return Verdict.SUPPORTED, f"Ondersteund door: {case.evidence[0]}"

    return Verdict.UNCERTAIN, f"Bewijs ondersteunt de claim niet: {case.evidence[0]}"


if __name__ == "__main__":
    for case in CASES:
        verdict, reason = baseline_classify(case)
        print(case.case_id, verdict.value, "-", reason)
