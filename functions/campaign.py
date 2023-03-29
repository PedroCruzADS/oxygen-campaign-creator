from functions.campaign_objective import campaign_objective


def create_campaign_model(name: str, objective: str, status: str, daily_budget: str):

    return {
        'name':  campaign_objective(objective) + ' ' + name,
        'objective': objective,
        'status': status,
        'daily_budget': int(daily_budget) * 100,
        'buying_type': 'AUCTION',
        'bid_strategy': 'LOWEST_COST_WITHOUT_CAP',
        'special_ad_categories': []}
