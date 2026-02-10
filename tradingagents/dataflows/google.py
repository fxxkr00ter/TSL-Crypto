from typing import Annotated
from datetime import datetime
from dateutil.relativedelta import relativedelta
from .googlenews_utils import getNewsData


def get_google_news(
    query: Annotated[str, "Query to search with"],
    curr_date: Annotated[str, "Curr date in yyyy-mm-dd format"],
    look_back_days: Annotated[int, "how many days to look back"],
) -> str:
    query = query.replace(" ", "+")

    start_date = datetime.strptime(curr_date, "%Y-%m-%d")
    before = start_date - relativedelta(days=look_back_days)
    before = before.strftime("%Y-%m-%d")

    news_results = getNewsData(query, before, curr_date)

    news_str = ""

    for news in news_results:
        news_str += (
            f"### {news['title']} (source: {news['source']}) \n\n{news['snippet']}\n\n"
        )

    if len(news_results) == 0:
        return ""

    return f"## {query} Google News, from {before} to {curr_date}:\n\n{news_str}"


def get_google_news_range(
    query: Annotated[str, "Query to search with"],
    start_date: Annotated[str, "Start date in yyyy-mm-dd format"],
    end_date: Annotated[str, "End date in yyyy-mm-dd format"],
) -> str:
    start_dt = datetime.strptime(start_date, "%Y-%m-%d")
    end_dt = datetime.strptime(end_date, "%Y-%m-%d")
    look_back_days = max((end_dt - start_dt).days, 1)
    return get_google_news(query, end_date, look_back_days)


def get_global_news_google(
    curr_date: Annotated[str, "Curr date in yyyy-mm-dd format"],
    look_back_days: Annotated[int, "how many days to look back"] = 7,
    limit: Annotated[int, "how many results to include"] = 5,
) -> str:
    query = "crypto market macro"
    news = get_google_news(query, curr_date, look_back_days)
    if not news:
        return ""
    if limit <= 0:
        return news
    # Soft-limit by truncating the number of items in the rendered text
    split_items = news.split("### ")
    header = split_items[0]
    items = split_items[1:limit + 1]
    return header + "### " + "### ".join(items) if items else news