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
        function3
        )
        
    call = dialog.select('[B][COLOR=yellow]Cerebro TV[/COLOR][COLOR=red] Sky Sports News Links[/COLOR][/B]', [
    '[B][COLOR=white]      Sky Sports News Link 1[/COLOR][/B]', 
    '[B][COLOR=white]      Sky Sports News Link 2[/COLOR][/B]', 
    '[B][COLOR=white]      Sky Sports News Link 3[/COLOR][/B]'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-5]

        return func()
    else:
        func = funcs[call]

        return func()
    return 

    
def function1():
    xbmc.executebuiltin('PlayMedia("plugin://program.apollo/?action=apollo&imdb=9999&season=2784&title=2784")')
  
def function2():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.supremacy/?fanart=http%3a%2f%2fstephen-builds.uk%2fart%2f20839702_10207884860798337_363786087_o.jpg&mode=30&name=%5bCOLOR%20aqua%5dSky%20Sport%20NewsHQ%5b%2fCOLOR%5d&url=%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fmamahd.in%2fp%2fmama.php%3fid%3d17809%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fmamahd.in%2fp%2fmama.php%3fid%3d17809%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fcdn2.crichd.info%2fsky-sports-news-live-streaming%23%0d%0a",return)')

def function3():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.weetv/?fanart=http%3a%2f%2fwww.geetee.site%2fwizchannels%2fimages%2fderwentwater.jpg&iconimage=http%3a%2f%2fwww.geetee.site%2fwizchannels%2fimages%2fgb.png&mode=3333&name=SKY%20SPORTS%20NEWS%0d&url=http%3a%2f%2fmidnightiptvstreams.ddns.net%3a5050%2flive%2fjames2%2fjames2%2f57176.ts%0d",return)')
    
menuoptions()