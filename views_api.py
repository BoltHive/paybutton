# views_api.py is for you API endpoints that could be hit by another service

# add your dependencies here

from . import paybutton_ext

# add your endpoints here


@paybutton_ext.get("/api/v1/test/{test_data}")
async def api_paybutton(test_data):
    # Do some python things and return the data
    return test_data
