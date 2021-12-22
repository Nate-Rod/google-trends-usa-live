import re
import pandas as pd
from datetime import datetime, timedelta
from pytrends.request import TrendReq

# get today's trending topics

pytrend = TrendReq(hl='en-US', tz=360, timeout=(10,25), retries=5, backoff_factor=0.2)

def get_todays_top_hits(region="US", cutoff=20):
    return pytrend.today_searches(pn=region).head(cutoff)

def get_live_top_hits():
    return pytrend.trending_searches(pn='united_states')

def get_top_hit_for_state():
    top_hits = map(parse_top_hit, get_todays_top_hits())
    print(get_live_top_hits())

    today_date = datetime.now().date()
    start_date = today_date - timedelta(days=30)

    # Create a string with the start and end dates
    timeframe_interval = "".join([str(start_date), " ", str(today_date)])

    results_by_state_df = pd.DataFrame()

    for hit in top_hits:  # LIST HAS MORE THAN FIVE ELEMENTS, SO WE WILL USE A FOR LOOP
        pytrend.build_payload(kw_list=[hit], cat=0, timeframe=timeframe_interval, geo='US')

        # Interest by region
        data_reg = pytrend.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False)
        results_by_state_df = pd.concat(
            [results_by_state_df, data_reg], join='outer', axis=1
        )
    return results_by_state_df

def parse_top_hit(hit):
    # finding the search term based off of surrounding characters
    query = re.findall("\?q=.+&date=", hit)
    # then stripping those identifying characters away
    query = query[0][3:-6]
    return query.replace("+", " ")
