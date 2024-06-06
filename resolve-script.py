from requests_html import HTMLSession
session = HTMLSession()

r = session.get('https://yeslivetv.com/hls/memfs/27eff6fe-9aa2-4e17-a197-cff54c342a0b.m3u8')

print(r.html.links)