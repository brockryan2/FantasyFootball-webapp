
sources{('football', 'NFL'): 'db connection',
        ('football', 'NCAA'): 'db connection',
        ('baseball', 'MLB'): 'db connection',
        ('baseball', 'NCAA'): 'db connection',
        ('basketball', 'NBA'): 'db connection',
        ('basketball', 'NCAAM'): 'db connection',
        ('basketball', 'NCAAW'): 'db connection',
        ('usa_soccer', 'MLS'): 'db connection',
        ('golf', 'PGA'): 'db connection',
        ('tennis', 'Mens'): 'db connection',
        ('tennis', 'Womens'): 'db connection'}


def set_data_source(sport=None, subtype=None):
    try:
        return sources[(sport, subtype)]

    except KeyError as ke:
        logging.log_error(ke)
        raise KeyError("Incorrect sport type or sport subtype given. Try again.")

