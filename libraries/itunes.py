import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

itunes_url = "https://itunes.apple.com"

# response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=1&term=${sys.argv[1]}")
response = requests.get(f"{itunes_url}/search?entity=song&limit=5&term=${sys.argv[1]}")
song = response.json()
# song = json.dumps(response.json(), indent=2)

# print(song)
# print(song["results"][0]["trackName"])

for result in song["results"]:
    print(result["trackName"])
