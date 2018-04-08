# -*- coding: utf-8 -*-

import requests, xbmcgui, xbmcplugin, xbmc, re, sys, os, xbmcaddon, json, urllib
from threading import Thread
ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.xnxx')# you need to change the folder path here to the name of you plugin folder 
ICON = xbmc.translatePath('special://home/addons/plugin.video.xnxx/icon.png')
fanarts = 'https://i.imgur.com/Qw9DExk.jpg'
USERDATA_PATH = xbmc.translatePath('special://home/userdata/addon_data/')
ADDON_DATA = USERDATA_PATH + '/plugin.video.xnxx/'# you need to change the folder path here to the name of you plugin folder 
favourites = ADDON_DATA + 'favourites'
if os.path.exists(favourites) == True:
    FAV = open(favourites).read()
else:
    FAV = []
next_page_con = 'https://i.imgur.com/s1x9dPi.png'
xnxx_base = 'https://www.xnxx.com'

def Main_Menu():
    Menu('Popular','https://www.xnxx.com/best/',26,ICON,fanarts,'Popular videos from XnXX.','')
    Menu('Hot','https://www.xnxx.com/hot/',22,ICON,fanarts,'Hot videos from XnXX.','')
    Menu('Hits','https://www.xnxx.com/hits/',22,ICON,fanarts,'Hit videos from XnXX.','')
    Menu('Porn Starz','https://www.xnxx.com/pornstars/',23,ICON,fanarts,'Porn Starz from XnXX.','')
    Menu('Search','',2,ICON,fanarts,'Search XnXX.','')
    # Menu('Naughty Favs','',10,ICON,fanarts,'Favorited vids from XnXX.','')
    

# mode 22
def Vid_Page(url):
    html = requests.get(url).content
    block = re.compile('class="mozaique">(.+?)id="footer">',re.DOTALL).findall(html)
    match = re.compile('id="video.+?href="(.+?)">.+?data-src="(.+?)".+?title=".+?">(.+?)</a>.+?duration">(.+?)</span>',re.DOTALL).findall(str(block))
    for pagez,iconz,titlez,time in match:
        page = xnxx_base+pagez
        titlez = titlez.replace('&#039;','\'')
        titlez = titlez.replace('&amp;',' & ')
        title = '[COLOR dodgerblue]%s[/COLOR]%s' % (time,titlez)
        Play(title,page,21,iconz,fanarts,'Best of XnXX','')
    nexzt = re.compile('class="pagination.+?class="active"\s*href=".+?href="(.+?)">.+?</div>.+?id="footer">',re.DOTALL).findall(html)
    for next_Page in nexzt:
        next_Paige = xnxx_base+next_Page
        Menu('NEXT PAGE',next_Paige,22,next_page_con,'','','')

# mode 26
def popular(url):
    html = requests.get(url).content
    block = re.compile('class="mozaique">(.+?)id="footer">',re.DOTALL).findall(html)
    match = re.compile('id="video.+?href="(.+?)">.+?data-src="(.+?)".+?title=".+?">(.+?)</a>.+?duration">(.+?)</span>',re.DOTALL).findall(str(block))
    for pagez,iconz,titlez,time in match:
        page = xnxx_base+pagez
        titlez = titlez.replace('&#039;','\'')
        titlez = titlez.replace('&amp;',' & ')
        title = '[COLOR dodgerblue]%s[/COLOR]%s' % (time,titlez)
        Play(title,page,21,iconz,fanarts,'Best of XnXX','')
    nexzt = re.compile('class="pagination.+?class="act.+?href=.+?href="(.+?)".+?class="no-page".+?id="footer">',re.DOTALL).findall(html)
    for next_Page in nexzt:
        next_Paige = xnxx_base+next_Page
        Menu('NEXT PAGE',next_Paige,26,next_page_con,'','','')
########### Starz #########################
#mode 23
def xnxx_starz(url):
    html = requests.get(url).content
    match = re.compile('<div id="profile.+?href="(.+?)".+?<img\s*src="(.+?)".+?class="profile-name.+?href=".+?">(.+?)[.,/(].+?</a>',re.DOTALL).findall(html)
    for link,icon,title in match:
        page = xnxx_base+link
        title = title.replace('&#039;','\'')
        title = title.replace('&amp;',' & ')
        Menu(title,page,24,icon,fanarts,'','')
# mode 24
def xnxx_instarz(url):
    html = requests.get(url).content
    match = re.compile('id="video.+?data-src="(.+?)".+?href="(.+?)" title="(.+?)">.+?</a></p><p class="metadata">.+?class="duration">(.+?)</span>',re.DOTALL).findall(html)
    for iconz,pagez,title,time in match:
        page = xnxx_base+pagez
        title = title.replace('&amp;',' & ')
        title = title.replace('&#039;','\'')
        Play(title,page,21,iconz,fanarts,'','')
    #     second_page = re.compile('class="pagination.+?class="active"\s*href=".+?href=.+?href="(.+?)">.+?<div id="footer',re.DOTALL).findall(html)
    # for next_Page in second_page:
    #     next_Paige = url+next_Page.strip().lower()
    #     xbmc.log(next_Paige)
    #     Menu('NEXT PAGE',next_Paige,24,ICON,'','','')

########### Search #########################
# mode 2
def Search():
    Search_url = 'http://collectionofbestporn.com/search/'
    Dialog = xbmcgui.Dialog()
    Search_title = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_name = Search_title.replace(' ','-').lower()
    Search_url = Search_url+Search_name
    url = Search_url
    html = requests.get(url).content
    match = re.compile('<!-- v item -->.+?href="(.+?)".+?src="(.+?)"\s*title="(.+?)".+?class="time">(.+?)</span>.+?</div>.+?<!-- v item end -->',re.DOTALL).findall(html)
    for page,icon,titlez,length in match:
        title = titlez.replace('&amp;',' & ')
        title = title.replace('&#039;','\'')
        title = '[COLOR dodgerblue]%s[/COLOR]%s' % (length,title)
        Play(title,page,25,icon,fanarts,'','')
        nexzt = re.compile('class="pagination.+?class="act.+?href=.+?href="(.+?)".+?class="no-page".+?id="footer">',re.DOTALL).findall(html)
    for next_Page in nexzt:
        next_Paige = xnxx_base+next_Page
        Menu('NEXT PAGE',next_Paige,25,next_page_con,'','','')


# mode 25        
def search_link(page):
    html = requests.get(page).content
    match1 = re.compile('<h1>.+?</h1></div>.+?src=".+?"></script>.+?src=".+?"></script>.+?poster=".+?".+?src="(.+?)".+?</video>.+?class="time">.+?</li>.+?</ul>',re.DOTALL).findall(html)
    for url in match1:
        resolve(name,url)
        

#thanks to apprentice for this dialog qaulity choice   
# mode 21
def xnxx_link(url):
    import xbmc
    HTML = requests.get(url).content
    low = re.compile("html5player.setVideoUrlLow\('(.+?)'\);").findall(HTML)
    for item in low:
        low = item
    medium = re.compile("html5player.setVideoUrlHigh\('(.+?)'\);").findall(HTML)
    for item in medium:
        medium = item
    high = re.compile("html5player.setVideoHLS\('(.+?)'\);").findall(HTML)
    for item in high:
        high = item
    choices = ['Low Quality','Medium Quality','High Quality']
    choice = xbmcgui.Dialog().select('Select Playlink', choices)
    if choice==0:
        play_now(low)
    elif choice==1:
        play_now(medium)
    elif choice==2:
        play_now(high)

#mode 27
def play_now(url): 
    xbmc.Player().play(url, xbmcgui.ListItem(name))
    xbmcplugin.endOfDirectory(int(sys.argv[1]))





def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )
        
        
def Menu(name,url,mode,iconimage,fanart,description,extra,showcontext=False,allinfo={}):
        fav_mode = mode
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)+"&extra="+urllib.quote_plus(extra)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if showcontext:
            contextMenu = []
            if showcontext == 'fav':
                contextMenu.append(('Remove from test Favorites','XBMC.RunPlugin(%s?mode=12&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
            if not name in FAV:
                contextMenu.append(('Add to Addon Favourites','XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s&fanart=%s&description=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), fav_mode, urllib.quote_plus(fanart), urllib.quote_plus(description))))
            liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
        

        
def Play(name,url,mode,iconimage,fanart,description,extra,showcontext=False,allinfo={}):
        fav_mode = mode
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)+"&extra="+urllib.quote_plus(extra)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if showcontext:
            contextMenu = []
            if showcontext == 'fav':
                contextMenu.append(('Remove from test Favorites','XBMC.RunPlugin(%s?mode=12&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
            if not name in FAV:
                contextMenu.append(('Add to test Favourites','XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s&fanart=%s&description=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), fav_mode, urllib.quote_plus(fanart), urllib.quote_plus(description))))
            liz.addContextMenuItems(contextMenu)
            contextMenu.append(('Queue Item', 'RunPlugin(%s?mode=14)' % sys.argv[0]))
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
        
# ===============================Favourites-----------Not sure whos code this is but credit due to them-------------------------------

def addFavorite(name, url, mode, iconimage, fanart, description, extra):
    favList = []
    # xbmc.log(extra)
    try:
        name = name.encode('utf-8', 'ignore')
    except:
        pass
    if os.path.exists(favourites) == False:
        favList.append((name, url, mode, iconimage, fanart, description, extra))
        a = open(favourites, "w")
        a.write(json.dumps(favList))
        a.close()
    else:
        a = open(favourites).read()
        data = json.loads(a)
        data.append((name, url, mode, iconimage, fanart, description, extra))
        b = open(favourites, "w")
        b.write(json.dumps(data))
        b.close()


def getFavourites():
    if not os.path.exists(favourites):
        favList = []
        favList.append(('test Favourites Section', '', '', '', '', '', ''))
        a = open(favourites, "w")
        a.write(json.dumps(favList))
        a.close()
    else:
        items = json.loads(open(favourites).read())
        for i in items:
            name = i[0]
            url = i[1]
            try:
                iconimage = i[3]
            except:
                iconimage = ''
            try:
                fanart = i[4]
            except:
                fanart = ''
            try:
                description = i[5]
            except:
                description = ''
            try:
                extra = i[6]
            except:
                extra = ''

            if i[2] == 20:
                Play(name, url, i[2], iconimage, fanart, description, extra, 'fav')
            else:
                Menu(name, url, i[2], iconimage, fanart, description, extra, 'fav')


def rmFavorite(name):
    data = json.loads(open(favourites).read())
    for index in range(len(data)):
        if data[index][0] == name:
            del data[index]
            b = open(favourites, "w")
            b.write(json.dumps(data))
            b.close()
            break
    xbmc.executebuiltin("XBMC.Container.Refresh")       

def resolve(name,url): 
    xbmc.Player().play(url, xbmcgui.ListItem(name))
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2: 
                params=sys.argv[2] 
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}    
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param
        
params=get_params()
url=None
name=None
iconimage=None
mode=None
fanart=None
description=None
trailer=None
fav_mode=None
extra=None

try:
    extra=urllib.unquote_plus(params["extra"])
except:
    pass

try:
    fav_mode=int(params["fav_mode"])
except:
    pass

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass

#####################################################END PROCESSES##############################################################        
        
if mode == None: Main_Menu()
elif mode == 2 : Search()

elif mode == 10: getFavourites()
elif mode==11:
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    addFavorite(name, url, fav_mode, iconimage, fanart, description, extra)
elif mode==12:
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    rmFavorite(name)
elif mode == 14 : queueItem()   
elif mode == 20: resolve(name,url)
elif mode == 21: xnxx_link(url)
elif mode == 22: Vid_Page(url)
elif mode == 23: xnxx_starz(url)
elif mode == 24: xnxx_instarz(url)
elif mode == 25: search_link(url)
elif mode == 26: popular(url)
elif mode == 27: play_now(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))