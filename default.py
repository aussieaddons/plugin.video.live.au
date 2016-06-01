import requests
from xbmcswift2 import Plugin

STREAM_MAP = {
    'ALL': [
        {
            'label': 'ABC News 24',
            'icon': 'https://upload.wikimedia.org/wikipedia/en/6/6d/ABC_News_24_logo.png',
            'path': 'http://www.abc.net.au/res/streaming/video/hls/news24.m3u8',
            'is_playable': True
        },
        {
            'label': 'Seven HD',
            'icon': 'https://s.yimg.com/ea/img/-/151001/seven_logo_large_1b0pc8g-1b0pc8k.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224838/MISC2/master_vhigh.m3u8',
            'is_playable': True
        },
        {
            'label': 'Racing.com',
            'icon': 'https://cdn.racing.com/resources/Racing/img/favicon/hub/favicon-200x200.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224825/MISC1/master.m3u8',
            'is_playable': True
        }
    ],
    'NSW': [
        {
            'label': 'Seven Sydney',
            'icon': 'https://s.yimg.com/ea/img/-/151001/seven_logo_large_1b0pc8g-1b0pc8k.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224814/SYD1/master.m3u8',
            'is_playable': True
        },
        {
            'label': '7TWO Sydney',
            'icon': 'https://s.yimg.com/ea/img/-/151001/7two_logo_large_1b0pd8p-1b0pd8v.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224827/SYD2/master.m3u8',
            'is_playable': True
        },
        {
            'label': '7mate Sydney',
            'icon': 'https://s.yimg.com/ea/img/-/150930/7mate_logo_1b0mbg3-1b0mbg8.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224840/SYD3/master.m3u8',
            'is_playable': True
        },
        {
            'label': 'Nine Sydney',
            'icon': 'https://s3-ap-southeast-2.amazonaws.com/mi9-vms-images-prod/2015/11/11/9_Colour_RGB.png',
            'path': 'https://9nowlivehls-i.akamaihd.net/hls/live/226554/ch9sydprd/master.m3u8',
            'is_playable': True
        }
    ],
    'QLD': [
        {
            'label': 'Seven Brisbane',
            'icon': 'https://s.yimg.com/ea/img/-/151001/seven_logo_large_1b0pc8g-1b0pc8k.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224815/BRI1/master.m3u8',
            'is_playable': True
        },
        {
            'label': '7TWO Brisbane',
            'icon': 'https://s.yimg.com/ea/img/-/151001/7two_logo_large_1b0pd8p-1b0pd8v.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224828/BRI2/master.m3u8',
            'is_playable': True
        },
        {
            'label': '7mate Brisbane',
            'icon': 'https://s.yimg.com/ea/img/-/150930/7mate_logo_1b0mbg3-1b0mbg8.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224841/BRI3/master.m3u8',
            'is_playable': True
        },
        {
            'label': 'Seven Cairns',
            'icon': 'https://s.yimg.com/ea/img/-/151001/seven_logo_large_1b0pc8g-1b0pc8k.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224818/CNS1/master.m3u8',
            'is_playable': True
        },
        {
            'label': '7TWO Cairns',
            'icon': 'https://s.yimg.com/ea/img/-/151001/7two_logo_large_1b0pd8p-1b0pd8v.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224831/CNS2/master.m3u8',
            'is_playable': True
        },
        {
            'label': '7mate Cairns',
            'icon': 'https://s.yimg.com/ea/img/-/150930/7mate_logo_1b0mbg3-1b0mbg8.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224844/CNS3/master.m3u8',
            'is_playable': True
        },
        {
            'label': 'Seven Mackay',
            'icon': 'https://s.yimg.com/ea/img/-/151001/seven_logo_large_1b0pc8g-1b0pc8k.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224820/MKY1/master.m3u8',
            'is_playable': True
        },
        {
            'label': '7TWO Mackay',
            'icon': 'https://s.yimg.com/ea/img/-/151001/7two_logo_large_1b0pd8p-1b0pd8v.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224833/MKY2/master.m3u8',
            'is_playable': True
        },
        {
            'label': '7mate Mackay',
            'icon': 'https://s.yimg.com/ea/img/-/150930/7mate_logo_1b0mbg3-1b0mbg8.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224846/MKY3/master.m3u8',
            'is_playable': True
        },
        {
            'label': 'Seven Rockhampton',
            'icon': 'https://s.yimg.com/ea/img/-/151001/seven_logo_large_1b0pc8g-1b0pc8k.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224821/RKY1/master.m3u8',
            'is_playable': True
        },
        {
            'label': '7TWO Rockhampton',
            'icon': 'https://s.yimg.com/ea/img/-/151001/7two_logo_large_1b0pd8p-1b0pd8v.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224834/RKY2/master.m3u8',
            'is_playable': True
        },
        {
            'label': '7mate Rockhampton',
            'icon': 'https://s.yimg.com/ea/img/-/150930/7mate_logo_1b0mbg3-1b0mbg8.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224847/RKY3/master.m3u8',
            'is_playable': True
        },
        {
            'label': 'Seven Sunshine Coast',
            'icon': 'https://s.yimg.com/ea/img/-/151001/seven_logo_large_1b0pc8g-1b0pc8k.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224823/SSC1/master.m3u8',
            'is_playable': True
        },
        {
            'label': '7TWO Sunshine Coast',
            'icon': 'https://s.yimg.com/ea/img/-/151001/7two_logo_large_1b0pd8p-1b0pd8v.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224836/SSC2/master.m3u8',
            'is_playable': True
        },
        {
            'label': '7mate Sunshine Coast',
            'icon': 'https://s.yimg.com/ea/img/-/150930/7mate_logo_1b0mbg3-1b0mbg8.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224849/SSC3/master.m3u8',
            'is_playable': True
        },
        {
            'label': 'Seven Toowoomba',
            'icon': 'https://s.yimg.com/ea/img/-/151001/seven_logo_large_1b0pc8g-1b0pc8k.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224824/TWB1/master.m3u8',
            'is_playable': True
        },
        {
            'label': '7TWO Toowoomba',
            'icon': 'https://s.yimg.com/ea/img/-/151001/7two_logo_large_1b0pd8p-1b0pd8v.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224837/TWB2/master.m3u8',
            'is_playable': True
        },
        {
            'label': '7mate Toowoomba',
            'icon': 'https://s.yimg.com/ea/img/-/150930/7mate_logo_1b0mbg3-1b0mbg8.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224850/TWB3/master.m3u8',
            'is_playable': True
        },
        {
            'label': 'Seven Townsville',
            'icon': 'https://s.yimg.com/ea/img/-/151001/seven_logo_large_1b0pc8g-1b0pc8k.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224819/TSV1/master.m3u8',
            'is_playable': True
        },
        {
            'label': '7TWO Townsville',
            'icon': 'https://s.yimg.com/ea/img/-/151001/7two_logo_large_1b0pd8p-1b0pd8v.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224832/TSV2/master.m3u8',
            'is_playable': True
        },
        {
            'label': '7mate Townsville',
            'icon': 'https://s.yimg.com/ea/img/-/150930/7mate_logo_1b0mbg3-1b0mbg8.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224845/TSV3/master.m3u8',
            'is_playable': True
        },
        {
            'label': 'Seven Wide Bay',
            'icon': 'https://s.yimg.com/ea/img/-/151001/seven_logo_large_1b0pc8g-1b0pc8k.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224822/WBY1/master.m3u8',
            'is_playable': True
        },
        {
            'label': '7TWO Wide Bay',
            'icon': 'https://s.yimg.com/ea/img/-/151001/7two_logo_large_1b0pd8p-1b0pd8v.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224835/WBY2/master.m3u8',
            'is_playable': True
        },
        {
            'label': '7mate Wide Bay',
            'icon': 'https://s.yimg.com/ea/img/-/150930/7mate_logo_1b0mbg3-1b0mbg8.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224848/WBY3/master.m3u8',
            'is_playable': True
        },
        {
            'label': 'Nine Brisbane',
            'icon': 'https://s3-ap-southeast-2.amazonaws.com/mi9-vms-images-prod/2015/11/11/9_Colour_RGB.png',
            'path': 'https://9nowlivehls-i.akamaihd.net/hls/live/226646/ch9bneprd/master.m3u8',
            'is_playable': True
        }
    ],
    'VIC': [
        {
            'label': 'Channel 31 Melbourne',
            'icon': 'http://www.c31.org.au/img/common/logo.png',
            'path': 'http://c31.mediafoundry.com.au/sites/default/files/manifest/manifest_live_27.m3u8',
            'is_playable': True
        },
        {
            'label': 'Seven Melbourne',
            'icon': 'https://s.yimg.com/ea/img/-/151001/seven_logo_large_1b0pc8g-1b0pc8k.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224813/MEL1/master.m3u8',
            'is_playable': True
        },
        {
            'label': '7TWO Melbourne',
            'icon': 'https://s.yimg.com/ea/img/-/151001/7two_logo_large_1b0pd8p-1b0pd8v.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224826/MEL2/master.m3u8',
            'is_playable': True
        },
        {
            'label': '7mate Melbourne',
            'icon': 'https://s.yimg.com/ea/img/-/150930/7mate_logo_1b0mbg3-1b0mbg8.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224839/MEL3/master.m3u8',
            'is_playable': True
        },
        {
            'label': 'Nine Melbourne',
            'icon': 'https://s3-ap-southeast-2.amazonaws.com/mi9-vms-images-prod/2015/11/11/9_Colour_RGB.png',
            'path': 'https://9nowlivehls-i.akamaihd.net/hls/live/226644/ch9melprd/master.m3u8',
            'is_playable': True
        },
        {
            'label': '9Go Melbourne',
            'icon': 'https://s3-ap-southeast-2.amazonaws.com/mi9-vms-images-prod/2015/11/12/9Go_Colour_RGB.png',
            'path': 'https://9nowlivehls-i.akamaihd.net/hls/live/238030/gomelprd/master.m3u8',
            'is_playable': True
        },
        {
            'label': '9Gem Melbourne',
            'icon': 'https://s3-ap-southeast-2.amazonaws.com/mi9-vms-images-prod/2015/11/13/9Gem_Colour_RGB.png',
            'path': 'https://9nowlivehls-i.akamaihd.net/hls/live/238025/gemmelprd/master.m3u8',
            'is_playable': True
        },
        {
            'label': '9Life Melbourne',
            'icon': 'https://s3-ap-southeast-2.amazonaws.com/mi9-vms-images-prod/2015/11/14/9Life_Colour_RGB.png',
            'path': 'https://9nowlivehls-i.akamaihd.net/hls/live/238035/lifemelprd/master.m3u8',
            'is_playable': True
        }
    ],
    'TAS': [
        {
            'label': 'Seven Melbourne',
            'icon': 'https://s.yimg.com/ea/img/-/151001/seven_logo_large_1b0pc8g-1b0pc8k.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224813/MEL1/master.m3u8',
            'is_playable': True
        },
        {
            'label': '7TWO Melbourne',
            'icon': 'https://s.yimg.com/ea/img/-/151001/7two_logo_large_1b0pd8p-1b0pd8v.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224826/MEL2/master.m3u8',
            'is_playable': True
        },
        {
            'label': '7mate Melbourne',
            'icon': 'https://s.yimg.com/ea/img/-/150930/7mate_logo_1b0mbg3-1b0mbg8.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224839/MEL3/master.m3u8',
            'is_playable': True
        },
        {
            'label': 'Nine Melbourne',
            'icon': 'https://s3-ap-southeast-2.amazonaws.com/mi9-vms-images-prod/2015/11/11/9_Colour_RGB.png',
            'path': 'https://9nowlivehls-i.akamaihd.net/hls/live/226644/ch9melprd/master.m3u8',
            'is_playable': True
        }
    ],
    'SA': [
        {
            'label': 'Channel 44 Adelaide',
            'icon': 'http://c44.com.au/wp-content/uploads/newc44logosmlbtweb.png',
            'path': 'http://manifester.mediafoundry.com.au/master/t/c44adelaide_1/manifest.m3u8',
            'is_playable': True
        },
        {
            'label': 'Seven Adelaide',
            'icon': 'https://s.yimg.com/ea/img/-/151001/seven_logo_large_1b0pc8g-1b0pc8k.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224816/ADE1/master.m3u8',
            'is_playable': True
        },
        {
            'label': '7TWO Adelaide',
            'icon': 'https://s.yimg.com/ea/img/-/151001/7two_logo_large_1b0pd8p-1b0pd8v.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224829/ADE2/master.m3u8',
            'is_playable': True
        },
        {
            'label': '7mate Adelaide',
            'icon': 'https://s.yimg.com/ea/img/-/150930/7mate_logo_1b0mbg3-1b0mbg8.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224842/ADE3/master.m3u8',
            'is_playable': True
        },
        {
            'label': 'Nine Adelaide',
            'icon': 'https://s3-ap-southeast-2.amazonaws.com/mi9-vms-images-prod/2015/11/11/9_Colour_RGB.png',
            'path': 'https://9nowlivehls-i.akamaihd.net/hls/live/226647/ch9adlprd/master.m3u8',
            'is_playable': True
        }
    ],
    'NT': [
        {
            'label': 'Seven Adelaide',
            'icon': 'https://s.yimg.com/ea/img/-/151001/seven_logo_large_1b0pc8g-1b0pc8k.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224816/ADE1/master.m3u8',
            'is_playable': True
        },
        {
            'label': '7TWO Adelaide',
            'icon': 'https://s.yimg.com/ea/img/-/151001/7two_logo_large_1b0pd8p-1b0pd8v.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224829/ADE2/master.m3u8',
            'is_playable': True
        },
        {
            'label': '7mate Adelaide',
            'icon': 'https://s.yimg.com/ea/img/-/150930/7mate_logo_1b0mbg3-1b0mbg8.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224842/ADE3/master.m3u8',
            'is_playable': True
        },
        {
            'label': 'Nine Adelaide',
            'icon': 'https://s3-ap-southeast-2.amazonaws.com/mi9-vms-images-prod/2015/11/11/9_Colour_RGB.png',
            'path': 'https://9nowlivehls-i.akamaihd.net/hls/live/226647/ch9adlprd/master.m3u8',
            'is_playable': True
        }
    ],
    'WA': [
        {
            'label': 'Seven Perth',
            'icon': 'https://s.yimg.com/ea/img/-/151001/seven_logo_large_1b0pc8g-1b0pc8k.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224817/PER1/master.m3u8',
            'is_playable': True
        },
        {
            'label': '7TWO Perth',
            'icon': 'https://s.yimg.com/ea/img/-/151001/7two_logo_large_1b0pd8p-1b0pd8v.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224830/PER2/master.m3u8',
            'is_playable': True
        },
        {
            'label': '7mate Melbourne',
            'icon': 'https://s.yimg.com/ea/img/-/150930/7mate_logo_1b0mbg3-1b0mbg8.png',
            'path': 'https://sevenwestmedia01-i.akamaihd.net/hls/live/224843/PER3/master.m3u8',
            'is_playable': True
        },
        {
            'label': 'Nine Perth',
            'icon': 'https://s3-ap-southeast-2.amazonaws.com/mi9-vms-images-prod/2015/11/11/9_Colour_RGB.png',
            'path': 'https://9nowlivehls-i.akamaihd.net/hls/live/226645/ch9perprd/master.m3u8',
            'is_playable': True
        }
    ]
}

plugin = Plugin()

@plugin.route('/')
def index():
    geoip_data = requests.get('https://freegeoip.net/json').json()
    if geoip_data['country_code'] != 'AU':
        return []
    if geoip_data['region_code'] not in STREAM_MAP:
        return STREAM_MAP['ALL']
    else:
        return STREAM_MAP['ALL'] + STREAM_MAP[geoip_data['region_code']]

if __name__ == '__main__':
    plugin.run()
