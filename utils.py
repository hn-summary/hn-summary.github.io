import pandas as pd
from datetime import date, timedelta

ALL_YEARS = [
    2006,
    2007,
    2008,
    2009,
    2010,
    2011,
    2012,
    2013,
    2014,
    2015,
    2016,
    2017,
    2018,
    2019,
    2020,
    2021,
    2022
]

_all_months = [date(2021, i, 1) for i in range(1, 13)]
ALL_MONTHS = [{
    'numeric': "{:02d}".format(month.month),
    'name': month.strftime('%b')
} for month in _all_months]
del _all_months


def _get_weeks_in_a_year(year):
    return (date(year, 12, 31) - date(year, 1, 1)).days // 7


def get_date_range_for_year(year):
    assert type(year) == int

    start = pd.Timestamp(year, 1, 1)
    end = pd.Timestamp(year + 1, 1, 1)
    return (start, end)


def get_date_range_for_month(year, month):
    assert type(year) == int
    assert type(month) == int

    start = pd.Timestamp(year, month, 1)
    if month == 12:
        end = pd.Timestamp(year + 1, 1, 1)
    else:
        end = pd.Timestamp(year, month + 1, 1)
    return (start, end)


def get_date_range_for_week(year, week):
    assert type(year) == int
    assert type(week) == int
    start = pd.Timestamp(date(year, 1, 1) + timedelta(days=(7 * (week - 1))))
    end = pd.Timestamp(date(year, 1, 1) + timedelta(days=(7 * week)))
    return (start, end)


def generate_top_charts(main_df, domain_groups, start, end):
    df = main_df.query("`Created At` >= @start and `Created At` < @end")

    results = {"groups": {}}
    # Top Stories
    results["top_stories"] = (
        df.query("`Post Type` == 'story'")
        .sort_values(by="Points", ascending=False)
        .head(10)
        .to_dict("records")
    )

    # Top Ask HN
    results["top_ask_hn"] = (
        df.query("`Post Type` == 'ask_hn'")
        .sort_values(by="Points", ascending=False)
        .head(10)
        .to_dict("records")
    )

    # Top Show HN
    results["top_show_hn"] = (
        df.query("`Post Type` == 'show_hn'")
        .sort_values(by="Points", ascending=False)
        .head(10)
        .to_dict("records")
    )

    # Groups
    # TODO: iterate over groups
    stories_df = df.query("`Post Type` == 'story'").dropna(subset=["URL Domain"]).copy()

    for group_title, data in domain_groups.items():
        if "domains" in data:
            sub_df = stories_df.loc[stories_df["URL Domain"].isin(data["domains"])]
        elif "pattern" in data:
            sub_df = stories_df.loc[
                stories_df["URL Domain"].str.contains(data["pattern"])
            ]
        else:
            raise ValueError("Misconfigured group")

        results["groups"][group_title] = {
            "domains": data.get("domains"),
            "pattern": data.get("pattern"),
            "top_posts": sub_df.sort_values(by="Points", ascending=False)
            .head(10)
            .to_dict("records"),
        }

    return results

def get_header_data(year):
    return {
        'ALL_YEARS': ALL_YEARS,
        'ALL_MONTHS': ALL_MONTHS,
        'ALL_WEEKS': list(range(1, _get_weeks_in_a_year(year)+1))
    }

def generate_page_context_year(main_df, domain_groups, year):
    start, end = get_date_range_for_year(year)

    top_charts = generate_top_charts(main_df, domain_groups, start, end)

    context = {
        "start": start,
        "end": end,
        "top_charts": top_charts,
        "selected_year": year,
        **get_header_data(year),
    }
    return context


def generate_page_context_month(main_df, domain_groups, year, month):
    start, end = get_date_range_for_month(year, month)

    top_charts = generate_top_charts(main_df, domain_groups, start, end)

    context = {
        "start": start,
        "end": end,
        "top_charts": top_charts,
        "selected_year": year,
        "selected_month": "{:02d}".format(month),
        **get_header_data(year),
    }
    return context


def generate_page_context_week(main_df, domain_groups, year, week):
    start, end = get_date_range_for_week(year, week)

    top_charts = generate_top_charts(main_df, domain_groups, start, end)

    context = {
        "start": start,
        "end": end,
        "top_charts": top_charts,
        "selected_year": year,
        "selected_week": week,
        **get_header_data(year),
    }
    return context
