from django.db import connections


def query_to_dicts(query_string, params=None, using=None):
    """Run a simple query and produce a generator    
    that returns the results as a bunch of dictionaries    
    with keys for the column values selected.    
    """
    params = params or ()
    using = using or "default"
    cursor = connections[using].cursor()
    cursor.execute(query_string, params)
    col_names = [desc[0] for desc in cursor.description]
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        row_dict = dict(zip(col_names, row))
        yield row_dict
