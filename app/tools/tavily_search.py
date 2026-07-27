from tavily import TavilyClient

from app.config.settings import settings

client = TavilyClient(
    api_key=settings.TAVILY_API_KEY
)


def search_web(query: str) -> str:

    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=5,
    )

    results = []

    for item in response["results"]:

        results.append(
            f"""
Title:
{item['title']}

Content:
{item['content']}

URL:
{item['url']}
"""
        )

    return "\n\n".join(results)