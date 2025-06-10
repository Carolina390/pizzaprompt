import requests
import json
from types import SimpleNamespace

class DominosAPI():

    def jprint(obj):  
        return json.dumps(obj, sort_keys=True, indent=4)  

    def jgetdata(obj):
        data = json.loads(obj, object_hook=lambda d: SimpleNamespace(**d))
        return data

    def callapi(tmp):
        response = requests.get("https://dominos-production.cdn.content.amplience.net/content/key/slot/uk/products?depth=all")
        return DominosAPI.jgetdata(DominosAPI.jprint(response.json())).linkedContent
        