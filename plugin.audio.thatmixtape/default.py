import re
import requests
import koding
from koding import route
import koding.router as router
import xbmcplugin
import xbmc
import sys

mycon = xbmc.translatePath('special://home/addons/plugin.audio.thatmixtape/icon.png')
link = 'https://thatmixtape.com'
getTracks = ("page")
popular = 'https://thatmixtape.com/mixtapes'
logo = 'https://thatmixtape.com/'
@route("main")
def main():
    koding.Add_Dir(name='Major Mixtapes', mode='major',icon = mycon, folder='true')
    koding.Add_Dir(name='Mixtape Legends', mode='legends',icon = mycon, folder='true')
    koding.Add_Dir(name='Mixtape Charts', mode='top_charts',icon = mycon, folder='true')
    koding.Add_Dir(name='Search', mode='search',icon = mycon, folder='true')
    
    

@route("major")
def major():
    koding.Add_Dir(name='Latest Mixtapes', mode='Popular',icon = mycon,folder='true')
    koding.Add_Dir(name='Various Artist', mode='various_artist', icon= mycon, folder='true')
    koding.Add_Dir(name='Random', mode='hundred_random',icon = mycon,folder='true')
    koding.Add_Dir(name='Popular', mode='top_100',icon = mycon,folder='true')
    

@route("legends")
def legends():
    koding.Add_Dir(name='Lil Wayne',mode='lil_wayne',icon = mycon, folder='true')
    koding.Add_Dir(name='50 Cent',mode='Fifty_Cent',icon = mycon,folder='true')
    koding.Add_Dir(name='Drake',mode='Drake',icon = mycon,folder='true')
    koding.Add_Dir(name='Kendrick Lamar',mode='kendrick_lamar',icon = mycon,folder='true')
    koding.Add_Dir(name='Loyd Banks',mode='Loyd_Banks',icon = mycon,folder='true')
    koding.Add_Dir(name='Young Thug',mode='yung_thug',icon = mycon,folder='true')
    koding.Add_Dir(name='Future',mode='future',icon = mycon,folder='true')
    koding.Add_Dir(name='Curren$Y',mode='currensy',icon = mycon,folder='true')
    koding.Add_Dir(name='2 Chainz',mode='two_chainz',icon = mycon,folder='true')

@route("top_charts")
def top_charts():
    koding.Add_Dir(name='Top Mixtapes This Week',mode='top_this_weak',icon = mycon,folder='true')
    koding.Add_Dir(name='Top Mixtapes This Month',mode='top_this_month',icon = mycon,folder='true')
    koding.Add_Dir(name='Top Mixtapes This Year',mode='top_this_year',icon = mycon,folder='true')
    #koding.Add_Dir(name='Top Mixtapes All Time',mode='all_tyme',icon = mycon,folder='true')

############ SEARCH #######################
@route('search')
def search():
    maine = 'https://thatmixtape.com'
    mytext = koding.Keyboard(heading='Naughty Search',default='')
    cleaned = mytext.replace(' ','+')
    start = 'https://thatmixtape.com/search?searchword='
    url = start+cleaned
    html = requests.get(url).content
    match = re.compile('class="result-title">.+?href="(.+?)">(.+?)</a>',re.DOTALL).findall(html)
    for pagez,title in match:
    	title = title.replace('&lt;span','')
    	title = title.replace('class=&quot;highlight&quot;&gt;','')
    	title = title.replace('highlight&quot;&gt;','')
    	title = title.replace('&lt;/span&gt;',' ')
    	title = title.replace('&amp;amp;','&')
        
        page = maine+pagez
        koding.Add_Dir(

            name= '%s' % (title),
            url=page,
            mode="gettracks",
            folder=True,
            icon=mycon,
            content_type="video")



@route("getlink")
def getlink(url): 
    html = requests.get(url).content
    block = re.compile('class="search-results">(.+?)id="gkFooter">',re.DOTALL).findall(html)
    match = re.compile('class="result-title">.+?href="(.+?)">(.+?)</a>',re.DOTALL).findall(str(block))
    for pagez,title in match:
    	title = title.replace('<span class="highlight">)',' ')
        page = maine+pagez
        koding.Add_Dir(

            name= '%s' % (title),
            url=page,
            mode="gettracks",
            folder=False,
            icon=mycon,
            content_type="video")       







############## Mixtape Charts ####################

@route("top_this_weak")
def top_this_weak():
    top_this_week = 'https://thatmixtape.com/top-mixtapes-this-week'
    html = requests.get(top_this_week).content
    match = re.compile(
        'href="(.+?)">.+?data-src="(.+?)"\s*alt="(.+?)".+?class="artist">(.+?)</span>',
        re.DOTALL).findall(html)
    for links, icon, album, artist in match:
        page = link.strip() + links.strip()
        koding.Add_Dir(
            name='[COLORred]%s[/COLOR][CR]Artist: [COLORdodgerblue]%s[/COLOR]' % (album.strip(), artist),
            url=page,
            mode="gettracks",
            folder=True,
            icon=icon,
            content_type="video")

@route("top_this_month")
def top_this_month():
    top_this_munth = 'https://thatmixtape.com/top-100-mixtapes-this-month'
    html = requests.get(top_this_munth).content
    match = re.compile(
        'href="(.+?)">.+?data-src="(.+?)"\s*alt="(.+?)".+?class="artist">(.+?)</span>',
        re.DOTALL).findall(html)
    for links, icon, album, artist in match:
        page = link+ links.strip()
        koding.Add_Dir(
            name='[COLORred]%s[/COLOR][CR]Artist: [COLORdodgerblue]%s[/COLOR]' % (album.strip(), artist),
            url=page,
            mode="gettracks",
            folder=True,
            icon=icon,
            content_type="video")

@route("top_this_year")
def top_this_year():
    top_this_yer = 'https://thatmixtape.com/top-mixtapes-this-year'
    html = requests.get(top_this_yer).content
    match = re.compile(
        'href="(.+?)">.+?data-src="(.+?)"\s*alt="(.+?)".+?class="artist">(.+?)</span>',
        re.DOTALL).findall(html)
    for links, icon, album, artist in match:
        page = link.strip() + links.strip()
        koding.Add_Dir(
            name='[COLORred]%s[/COLOR][CR]Artist: [COLORdodgerblue]%s[/COLOR]' % (album.strip(), artist),
            url=page,
            mode="gettracks",
            folder=True,
            icon=icon,
            content_type="video")

@route("all_tyme")
def all_tyme():
    top_all_time = 'https://thatmixtape.com/top-mixtapes-of-all-time'
    html = requests.get(top_all_time).content
    match = re.compile(
        'href="(.+?)">.+?data-src="(.+?)"\s*alt="(.+?)".+?class="artist">(.+?)</span>',
        re.DOTALL).findall(html)
    for links, icon, album, artist in match:
        page = link.strip() + links.strip()
        koding.Add_Dir(
            name='[COLORred]%s[/COLOR][CR]Artist: [COLORdodgerblue]%s[/COLOR]' % (album.strip(), artist),
            url=page,
            mode="gettracks",
            folder=True,
            icon=icon,
            content_type="video")
    

############## Mixtape Legends ###################
@route("two_chainz")
def two_chainz():
    two_chains = 'https://thatmixtape.com/tm/1/2-Chainz'
    html = requests.get(two_chains).content
    match = re.compile(
        'class="grid_album".+?href="(.+?)".+?data-src="(.+?)"\s*alt="(.+?)".+?</noscript>',
        re.DOTALL).findall(html)
    for links, icon, album in match:
        page = link.strip() + links.strip()
        koding.Add_Dir(
            name='%s' % (album.strip()),
            url=page,
            mode="gettracks",
            folder=True,
            icon=icon,
            content_type="video")

@route("currensy")
def currensy():
    Curreny = 'https://thatmixtape.com/tm/C/Curren-y'
    html = requests.get(Curreny).content
    match = re.compile(
        'class="grid_album".+?href="(.+?)".+?data-src="(.+?)"\s*alt="(.+?)".+?</noscript>',
        re.DOTALL).findall(html)
    for links, icon, album in match:
        page = link.strip() + links.strip()
        koding.Add_Dir(
            name='%s' % (album.strip()),
            url=page,
            mode="gettracks",
            folder=True,
            icon=icon,
            content_type="video")

@route("future")
def future():
    futur = 'https://thatmixtape.com/tm/F/Future'
    html = requests.get(futur).content
    match = re.compile(
        'class="grid_album".+?href="(.+?)".+?data-src="(.+?)"\s*alt="(.+?)".+?</noscript>',
        re.DOTALL).findall(html)
    for links, icon, album in match:
        page = link.strip() + links.strip()
        koding.Add_Dir(
            name='%s' % (album.strip()),
            url=page,
            mode="gettracks",
            folder=True,
            icon=icon,
            content_type="video")

@route("yung_thug")
def yung_thug():
    yungthug = 'https://thatmixtape.com/tm/Y/Young-Thug'
    html = requests.get(yungthug).content
    match = re.compile(
        'class="grid_album".+?href="(.+?)".+?data-src="(.+?)"\s*alt="(.+?)".+?</noscript>',
        re.DOTALL).findall(html)
    for links, icon, album in match:
        page = link.strip() + links.strip()
        koding.Add_Dir(
            name='%s' % (album.strip()),
            url=page,
            mode="gettracks",
            folder=True,
            icon=icon,
            content_type="video")

@route("Fifty_Cent")
def Fifty_Cent():
    fifty_cent = 'https://thatmixtape.com/tm/1/50-Cent'
    html = requests.get(fifty_cent).content
    match = re.compile(
        'class="grid_album".+?href="(.+?)".+?data-src="(.+?)"\s*alt="(.+?)".+?</noscript>',
        re.DOTALL).findall(html)
    for links, icon, album in match:
        page = link.strip() + links.strip()
        koding.Add_Dir(
            name='%s' % (album.strip()),
            url=page,
            mode="gettracks",
            folder=True,
            icon=icon,
            content_type="video")

@route("Loyd_Banks")
def Loyd_Banks():
    loyd_banks = 'https://thatmixtape.com/tm/L/Lloyd-Banks'
    html = requests.get(loyd_banks).content
    match = re.compile(
        'class="grid_album".+?href="(.+?)".+?data-src="(.+?)"\s*alt="(.+?)".+?</noscript>',
        re.DOTALL).findall(html)
    for links, icon, album in match:
        page = link.strip() + links.strip()
        koding.Add_Dir(
            name='%s' % (album.strip()),
            url=page,
            mode="gettracks",
            folder=True,
            icon=icon,
            content_type="video")

@route("kendrick_lamar")
def kendrick_lamar():
    kendrek_lamar = 'https://thatmixtape.com/tm/K/Kendrick-Lamar'
    html = requests.get(kendrek_lamar).content
    match = re.compile(
        'class="grid_album".+?href="(.+?)".+?data-src="(.+?)"\s*alt="(.+?)".+?</noscript>',
        re.DOTALL).findall(html)
    for links, icon, album in match:
        page = link.strip() + links.strip()
        koding.Add_Dir(
            name='%s' % (album.strip()),
            url=page,
            mode="gettracks",
            folder=True,
            icon=icon,
            content_type="video")

@route("lil_wayne")
def lil_wayne():
    lil_weezy = 'https://thatmixtape.com/tm/L/Lil-Wayne'
    html = requests.get(lil_weezy).content
    match = re.compile(
        'class="grid_album".+?href="(.+?)".+?data-src="(.+?)"\s*alt="(.+?)".+?</noscript>',
        re.DOTALL).findall(html)
    for links, icon, album in match:
        page = link.strip() + links.strip()
        koding.Add_Dir(
            name='%s' % (album.strip()),
            url=page,
            mode="gettracks",
            folder=True,
            icon=icon,
            content_type="video")

@route("Drake")
def Drake():
    drake = 'https://thatmixtape.com/tm/D/Drake'
    html = requests.get(drake).content
    match = re.compile(
        'class="grid_album".+?href="(.+?)".+?data-src="(.+?)"\s*alt="(.+?)".+?</noscript>',
        re.DOTALL).findall(html)
    for links, icon, album in match:
        page = link.strip() + links.strip()
        koding.Add_Dir(
            name='%s' % (album.strip()),
            url=page,
            mode="gettracks",
            folder=True,
            icon=icon,
            content_type="video")       

############### Major Mixtapes ###############
@route("hundred_random")
def hundred_random():
    random_hundred = 'https://thatmixtape.com/mixtape-wall'
    html = requests.get(random_hundred).content
    match = re.compile(
        'class="random_album">.+?data-src="(.+?)".+?class="artist">(.+?)</span>.+?class="name_search">(.+?)</span>.+?class="playme" \s*href="(.+?)">Play.+?</div>',
        re.DOTALL).findall(html)
    for icon, artist, album, links in match:
        page = link.strip() + links.strip()
        koding.Add_Dir(
            name='[COLORred]%s[/COLOR][CR]Artist: [COLORdodgerblue]%s[/COLOR]' % (album.strip(), artist),
            url=page,
            mode="gettracks",
            folder=True,
            icon=icon,
            content_type="video")

@route("various_artist")
def various_artist():
    artist_various = 'https://thatmixtape.com/mixtape-series'
    html = requests.get(artist_various).content
    match = re.compile(
        'class="random_album">.+?data-src="(.+?)".+?class="artist">(.+?)</span>.+?class="name_search">(.+?)</span>.+?class="playme" \s*href="(.+?)">Play.+?</div>',
        re.DOTALL).findall(html)
    for icon, artist, album, links in match:
        page = link.strip() + links.strip()
        koding.Add_Dir(
            name='[COLORred]%s[/COLOR][CR]Artist: [COLORdodgerblue]%s[/COLOR]' % (album.strip(), artist),
            url=page,
            mode="gettracks",
            folder=True,
            icon=icon,
            content_type="video")

@route("top_100")
def top_100():
    latest_official = 'https://thatmixtape.com/latest-official-tapes'
    html = requests.get(latest_official).content
    match = re.compile(
        'class="random_album">.+?data-src="(.+?)".+?class="artist">(.+?)</span>.+?class="name_search">(.+?)</span>.+?class="playme" \s*href="(.+?)">Play.+?</div>',
        re.DOTALL).findall(html)
    for icon, artist, album, links in match:
        page = link.strip() + links.strip()
        koding.Add_Dir(
            name='[COLORred]%s[/COLOR][CR]Artist: [COLORdodgerblue]%s[/COLOR]' % (album.strip(), artist),
            url=page,
            mode="gettracks",
            folder=True,
            icon=icon,
            content_type="video")

@route("Popular")
def Popular():
    html = requests.get(popular).content
    match = re.compile(
        'class="random_album">.+?data-src="(.+?)".+?class="artist">(.+?)</span>.+?class="name_search">(.+?)</span>.+?class="playme" \s*href="(.+?)">Play.+?</div>',
        re.DOTALL).findall(html)

    for icon, artist, album, links in match:
        page = link.strip() + links.strip()
        koding.Add_Dir(
            name='[COLORred]%s[/COLOR][CR]Artist: [COLORdodgerblue]%s[/COLOR]' % (album.strip(), artist),
            url=page,
            mode="gettracks",
            folder=True,
            icon=icon,
            content_type="video")

########   Grab songs from selected pages #####################
@route("gettracks", ["url"])
def gettracks(page):
    html = requests.get(page).content
    match1 = re.compile('{file.+?"(.+?)".+?title:"(.+?)".+?description:"(.+?)".+?image.+?"(.+?)"};',re.DOTALL).findall(html)

    for mp3, titles, artist, icon in match1:
        koding.Add_Dir(
            name='[COLORred]%s[/COLOR][CR]Artist: [COLORdodgerblue]%s[/COLOR]' % (titles, artist),
            url=mp3.replace(" ", "%20"),
            description='artist',
            mode="play",
            folder=False,
            icon=icon,
            content_type="video")


@route("play", ["url"])
def play(url):
    xbmc.Player().play(url)


router.Run()
xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=False)
