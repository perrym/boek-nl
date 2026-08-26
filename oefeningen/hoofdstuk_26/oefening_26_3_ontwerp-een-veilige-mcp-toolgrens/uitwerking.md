# Uitwerking 26.3 - Ontwerp een veilige MCP-toolgrens

De voorbeeldoplossing in `uitwerking.py` modelleert voor iedere tool een afzonderlijk beleid. De toolnaam, vereiste scope, toegestane parameters en de eis voor menselijke goedkeuring worden buiten het model vastgelegd. Daardoor kan tekst uit een document deze autorisatieregels niet aanpassen.

De drie fictieve tools zijn:

- `document_search`: alleen lezen met scope `documents.read`.
- `ticket_create`: schrijfactie met scope `tickets.write`, approval en een idempotency-key.
- `account_status_update`: gevoelige schrijfactie met scope `accounts.status.write`, approval en een idempotency-key.

`authorize_tool_call()` controleert vervolgens of de tool bestaat, of de gebruiker de juiste scope heeft, of alleen toegestane parameters worden gebruikt en of bij schrijfacties de vereiste approval en idempotency-key aanwezig zijn. Wanneer de aanvraag rechtstreeks voortkomt uit onbetrouwbare documentinhoud, wordt een schrijfactie geweigerd.

Dit sluit aan op de controles uit het boek: rechten worden technisch begrensd, onbetrouwbare content wordt als data behandeld en kan geen autorisatiebeslissing overschrijven, en gevoelige schrijfacties vereisen aanvullende controle.

## Aanvullende controle

Een productie-implementatie moet daarnaast de workflow zelf begrenzen met een maximum aantal stappen en een expliciete stopconditie. Voeg die begrenzing toe aan de orchestrator of agentloop en niet alleen aan de afzonderlijke toolpolicy.

## Zelf verder testen

Verander minimaal één scope, verwijder een idempotency-key en probeer een niet-toegestane parameter. Controleer dat iedere onveilige variant wordt geweigerd.
