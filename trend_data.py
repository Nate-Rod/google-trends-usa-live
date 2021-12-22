import re
import pandas as pd
from pytrends.request import TrendReq
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor

# get today's trending topics
pytrend = TrendReq(hl='en-US', tz=360, timeout=(10,25), retries=5, backoff_factor=0.2)

def get_todays_top_hits(region="US", cutoff=20):
    return pytrend.today_searches(pn=region).head(cutoff)

def get_top_hits_df_for_state():
    top_hits = map(parse_top_hit, get_todays_top_hits())
    #th_l = list(top_hits)

    today_date = datetime.now().date()
    start_date = today_date - timedelta(days=30)

    # Create a string with the start and end dates
    timeframe_interval = "".join([str(start_date), " ", str(today_date)])
    results_by_state_df = pd.DataFrame()

    # with ThreadPoolExecutor(max_workers=len(th_l)) as executor:
    #     executor.map(append_interest_to_df, th_l)

    for hit in top_hits:
        pytrend.build_payload(kw_list=[hit], cat=0, timeframe=timeframe_interval, geo='US')

        # Interest by region
        data_reg = pytrend.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False)

        results_by_state_df = pd.concat(
            [results_by_state_df, data_reg], join='outer', axis=1
        )
        #print(results_by_state_df)

    for state in results_by_state_df.index:
        get_top_hit_of_state(state, results_by_state_df)

    return results_by_state_df

# def append_interest_to_df(hit):
#     print(f"Running with {hit}")
#     pytrend.build_payload(kw_list=[hit], cat=0, timeframe=timeframe_interval, geo='US')
#
#     # Interest by region
#     data_reg = pytrend.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False)
#     return data_reg

def get_top_hit_of_state(state, df):
    from us_state_abbrev import us_state_to_abbrev
    state_interest = df.loc[state]
    print(f"{us_state_to_abbrev.get(state)} - {state} - {state_interest.idxmax()} - {state_interest.max()}")


def parse_top_hit(hit):
    # finding the search term based off of surrounding characters
    query = re.findall("\?q=.+&date=", hit)
    # then stripping those identifying characters away
    query = query[0][3:-6]
    return query.replace("+", " ")
