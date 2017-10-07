import time
import xbmc
import os
import xbmcgui
import urllib2

def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2,
        function3,
        function4
        )
        
    call = dialog.select('[B][COLOR=yellow]Cerebro TV[/COLOR][COLOR=red] Sky Sports Premier League Links[/COLOR][/B]', [
    '[B][COLOR=white]      Sky Sports Premier League Link 1[/COLOR][/B]', 
    '[B][COLOR=white]      Sky Sports Premier League Link 2[/COLOR][/B]',
    '[B][COLOR=white]      Sky Sports Premier League Link 3[/COLOR][/B]',
    '[B][COLOR=white]      Sky Sports Premier League Link 4[/COLOR][/B]'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-4]
        return func()
    else:
        func = funcs[call]
        return func()
    return 

    
def function1():
    xbmc.executebuiltin('PlayMedia("plugin://program.apollo/?action=apollo&imdb=9999&season=1133&title=1133")')
  
def function2():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.supremacy/?fanart=http%3a%2f%2fstephen-builds.uk%2fart%2f20839702_10207884860798337_363786087_o.jpg&mode=30&name=%5bCOLOR%20aqua%5dSky%20Sport%20premier%20league%5b%2fCOLOR%5d&url=%0d%0asublink%3aplugin%3a%2f%2fplugin.video.f4mTester%2f%3furl%3dhttp%3a%2f%2fmagportal.ddns.net%3a25461%2flive%2fultra123%2fultra123%2f272.ts%26streamtype%3dTSDOWNLOADER%26name%3dFHD%20SUPREMACY-ADD-ON%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.f4mTester%2f%3furl%3dhttp%3a%2f%2fmagportal.ddns.net%3a25461%2flive%2fultra123%2fultra123%2f271.ts%26streamtype%3dTSDOWNLOADER%26name%3dHD%20SUPREMACY-ADD-ON%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.f4mTester%2f%3furl%3dhttp%3a%2f%2fmagportal.ddns.net%3a25461%2flive%2fultra123%2fultra123%2f270.ts%26streamtype%3dTSDOWNLOADER%26name%3dSD%20SUPREMACY-ADD-ON%23%0d%0a",return)')

def function3():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.supremacy/?fanart=http%3a%2f%2fstephen-builds.uk%2fart%2f20839702_10207884860798337_363786087_o.jpg&mode=30&name=%5bCOLOR%20aqua%5dSky%20Sport%20premier%20league%5b%2fCOLOR%5d&url=%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fwww.jokerstream.com%2fp%2fsky-sports-5-hd.html%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fmamahd.in%2fp%2fmama.php%3fid%3d17805%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fcricfree.sc%2fsky-sports-premier-league-live-streaming%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fwww.jokerstream.com%2fp%2fsky-sports-5-hd.html%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fcricfree.sc%2fsky-sports-premier-league-live-streaming%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fnowwatchtvlive.cc%2fsky-sports-premier-league-channel-live-stream-online-hdtv%2f%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fcricfree.sc%2fiframe%2fhdlive%2fsky5.php%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fsstream.net%2fsky5.html%23%0d%0a",return)')

def function4():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.OTV_MEDIA/?function=play__liveonlinetv24&sCat=6&sFav=play__liveonlinetv24&sId=liveonlinetv247&sMovieTitle=Sky%20Sports%20Premier%20League&site=liveonlinetv247&siteUrl=http%3a%2f%2fwww.liveonlinetv247.info%2fwatch.php%3ftitle%3dSky%20Sports%20Premier%20League%26channel%3dskysportspremierleague&title=Sky%20Sports%20Premier%20League")')
     
menuoptions()