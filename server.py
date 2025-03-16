import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("SEK Exchange Rate")


@mcp.tool()
async def fetch_fx(currency: str) -> str:
    """Fetch current exchange rate for some currency to SEK using the API from Riksbanken

    Args:
        currency: 3-letter ISO 4217 currency code (e.g. USD, EUR)
    """
    if len(currency) != 3 or not currency.isalpha():
        raise ValueError("Currency must be a 3-letter code (e.g. USD, EUR)")

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://api.riksbank.se/swea/v1/Observations/Latest/sek{currency}pmi"
            )
            if response.status_code != 200:
                raise RuntimeError(
                    f"Failed to fetch FX rate from API: Received status code {response.status_code}"
                )
            return response.text
    except httpx.RequestError as e:
        raise RuntimeError(f"Failed to connect to FX rate API: {str(e)}")


@mcp.prompt()
def get_exchange_rate_prompt(currency: str) -> str:
    """Generate a properly formatted exchange rate request

    Args:
        currency: 3-letter currency code (e.g. USD, EUR)
    """
    return f"""Please provide the current {currency} to SEK exchange rate.
Include the following details:
- Currency: {currency}
"""
