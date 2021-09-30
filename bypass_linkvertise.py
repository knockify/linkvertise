import requests

def bypasslink(x):
  if requests.get("https://bypass.bot.nu/bypass2?url=" + x).status_code != 200:
      return 0
  else:
    z = requests.get("https://bypass.bot.nu/bypass2?url=" + x).text
    y = json.loads(z)
    return y['destination']