from duckduckgo_search import DDGS

with DDGS() as ddgs:
    results = [r for r in ddgs.text("Current weather in Colombo", max_results=3)]
    print("seach resalt:")
    for result in results:
        print(f"\nTitle: {result['title']}")
        print(f"Link: {result['href']}")