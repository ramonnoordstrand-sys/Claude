import os, urllib.request, urllib.parse
token = '7965094674:AAFlEglGlNrcaq8OXl-mVQpvAB_-3fUe10k'
chat_id = '1409024204'
text = open('briefing.txt').read()
url = 'https://api.telegram.org/bot' + token + '/sendMessage'
chunks = [text[i:i+4000] for i in range(0, len(text), 4000)] or ['']
for chunk in chunks:
    data = urllib.parse.urlencode({'chat_id': chat_id, 'text': chunk}).encode()
    req = urllib.request.Request(url, data=data)
    print(urllib.request.urlopen(req).read().decode())
