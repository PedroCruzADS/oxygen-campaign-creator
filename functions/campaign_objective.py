
def campaign_objective(form_field: str):
    if form_field == 'CONVERSIONS':
        return '[Conversão]'
    if form_field == 'REACH':
        return '[Alcance]'
    if form_field == 'POST_ENGAGEMENT':
        return '[Engajamento]'
