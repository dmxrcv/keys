import re
import json
import requests

def get_keys():
    r = requests.get('https://github.com/dmxrcv/keys/blob/main/keys.json')
    keys = re.findall(r'"rawLines":\[\"(.*?)\"\],"stylingDirectives', r.text).pop().replace('\\', '')
    return json.loads(keys)

if __name__ == '__main__':
  keys = get_keys()
  print('Keys:', json.dumps(keys))
