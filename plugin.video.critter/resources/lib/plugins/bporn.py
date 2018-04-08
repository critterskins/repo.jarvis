"""
     
    Copyright (C) 2018

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

########## Examples: ##################

<dir>
  <title>All</title>
  <xvids>category/all</xvids>
</dir>

<dir>
  <title>All</title>
  <xvids>category/lesbian</xvids>
</dir>
################## category tags to use ##############
Amateur
Anal
Asian
BBC
Big Ass
Big Dick
Big Tits
Blonde
Blowjobs
British
Brunette
Cartoon
Casting
Couple
Cream Pie
Cuckold
Cumshots
Czech
Deep Throat
Double Penetration
Ebony
Foot Fetish
Gang Bang
German
Girlfriend
Glamcore
Group Sex
Hairy
Handjobs
Hardcore
HD
Hentai
Interracial
Japanese
Latin
Lesbian
Lingerie
Massage
Masturbation
Milf
Old And Young
Orgasm
Orgy
Parody
POV
Public
Redheads
Russian
Schoolgirl
Spanish Porn
Squirting
Tattoo
Teen
Threesome
Toys
Uniform
Webcams

"""



from __future__ import absolute_import
import requests
import re
import os
import xbmc
import xbmcaddon
import json
from koding import route
from ..plugin import Plugin
from resources.lib.util.context import get_context_items
from resources.lib.util.xml import JenItem, JenList, display_list
from requests.exceptions import HTTPError
import posixpath
import time
from six.moves.urllib.parse import unquote
from six.moves.urllib.parse import quote
from unidecode import unidecode

CACHE_TIME = 3600  # change to wanted cache time in seconds

addon_fanart = xbmcaddon.Addon().getAddonInfo('fanart')
addon_icon = xbmcaddon.Addon().getAddonInfo('icon')
AddonName = xbmc.getInfoLabel('Container.PluginName')
AddonName = xbmcaddon.Addon(AddonName).getAddonInfo('id')


class ADULT(Plugin):
    name = "adult"

    def process_item(self, item_xml):
        if "<xvids>" in item_xml:                                    # xml tag
            item = JenItem(item_xml)
            if "category/" in item.get("xvids", ""):              # info in tag
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "get_cat",                              # name the mode relative to the tag, 
                    'url': item.get("xvids", ""),                # evrything else can stay the same
                    'folder': True,
                    'imdb': "0",
                    'season': "0",
                    'episode': "0",
                    'info': {},
                    'year': "0",
                    'context': get_context_items(item),
                    "summary": item.get("summary", None)
                }
                result_item["properties"] = {
                    'fanart_image': result_item["fanart"]
                }
                result_item['fanart_small'] = result_item["fanart"]
                return result_item                                  

@route(mode='get_cat', args=["url"])
def get_cat(url):
    xml = ""
    if "all" in url:
        html = "http://collectionofbestporn.com/channels/"
        html2 = requests.get(html).content
        match = re.compile('<div class="video-thumb">.+?<img src="(.+?)".+?<a href="(.+?)".+?title="(.+?)"',re.DOTALL).findall(html2)
        for image, link, name in match:
            link = link.split("/")[-1]
            xml += "<dir>"\
                   "<title>%s</title>"\
                   "<thumbnail>%s</thumbnail>"\
                   "<xvids>category/%s</xvids>"\
                   "</dir>" % (name, image, link)
    else:
                   
        url = url.split("/")[-1]
        html = "http://collectionofbestporn.com/category/"+url
        html2 = requests.get(html).content
        match = re.compile('class="video-item .+?<a href="(.+?)".+?<img src="(.+?)".+?title="(.+?)".+?<span class="time">(.+?)</span>',re.DOTALL).findall(html2)
        for page, image, title, length in match:
            html3 = requests.get(page).content
            block = re.compile('<video id="thisPlayer"(.+?)</video>',re.DOTALL).findall(html3)
            match2 = re.compile('<source src="(.+?)"',re.DOTALL).findall(str(block))
            link = match2[-1]
            xml += "<item>"\
                    "<title>%s</title>"\
                    "<time>%s</time>"\
                    "<year></year>"\
                    "<thumbnail>%s</thumbnail>"\
                    "<fanart></fanart>"\
                    "<link>"\
                    "<sublink>%s</sublink>"\
                    "</link>"\
                    "</item>" % (title, length, image, link)

    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())    
