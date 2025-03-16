# sek-fx-mcp

Detta är en Python-implementering av Model Context Protocol (MCP), som är ett verktyg för att hantera kommunikation mellan applikationer och stora språkmodeller (LLM).

Den kontaktar Riksbankens API och frågar efter växlingskursen för en viss valuta till svenska kronor. Den accepterar ISO 4217 koden för valutor dvs NOK (norska kronor), EUR (Euro), GBP (brittiska pund) etc.

Testad i Claude Desktop i MacOS. Kräver Python och uv.

Installation:
```bash
uv run mcp install server.py
```

## Vidare läsning:
https://en.wikipedia.org/wiki/ISO_4217

https://github.com/modelcontextprotocol/python-sdk

https://www.riksbank.se/sv/statistik/rantor-och-valutakurser/hamta-rantor-och-valutakurser-via-api/

https://modelcontextprotocol.io/introduction
