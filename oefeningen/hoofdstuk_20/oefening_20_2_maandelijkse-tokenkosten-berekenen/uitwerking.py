def maandkosten(
    verzoeken_per_dag: int,
    input_tokens: int,
    output_tokens: int,
    prijs_input_per_miljoen: float,
    prijs_output_per_miljoen: float,
    dagen: int = 30,
) -> float:
    totaal_input = verzoeken_per_dag * input_tokens * dagen
    totaal_output = verzoeken_per_dag * output_tokens * dagen
    input_kosten = totaal_input / 1_000_000 * prijs_input_per_miljoen
    output_kosten = totaal_output / 1_000_000 * prijs_output_per_miljoen
    return input_kosten + output_kosten

scenario = maandkosten(
    verzoeken_per_dag=2500,
    input_tokens=1800,
    output_tokens=450,
    prijs_input_per_miljoen=2.50,
    prijs_output_per_miljoen=10.00,
)
print(f"Geschatte maandkosten: EUR {scenario:,.2f}")
