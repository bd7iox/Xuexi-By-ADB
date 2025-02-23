#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   easyadb.py
@Time    :   2020/03/30
@Version :   1.0.0
@Author  :   Triston Chow
@Contact :   triston2021@outlook.com
@License :   (C)Copyright 2020-2021, Triston Chow
@Desc    :   封装常用ADB指令，简化调用操作
'''


import os
import subprocess


class EasyADB:
    def __init__(self, device_tag=''):
        if device_tag == '':
            self.adb = 'adb'
        else:
            if device_tag.isdecimal():
                self.adb = f'adb -t {device_tag}'
            else:
                self.adb = f'adb -s {device_tag}'
        
        self.KEY = {
            'power':26, 'menu':82, 'home':3, 'back':4,
            'volume_up':24, 'volume_down':25, 'volume_mute':164,
            'screen_on':224, 'screen_off':223,
            'ACTION_DOWN': 0,
            'ACTION_MULTIPLE': 2,
            'ACTION_UP': 1,
            'FLAG_CANCELED': 32,
            'FLAG_CANCELED_LONG_PRESS': 256,
            'FLAG_EDITOR_ACTION': 16,
            'FLAG_FALLBACK': 1024,
            'FLAG_FROM_SYSTEM': 8,
            'FLAG_KEEP_TOUCH_MODE': 4,
            'FLAG_LONG_PRESS': 128,
            'FLAG_SOFT_KEYBOARD': 2,
            'FLAG_TRACKING': 512,
            'FLAG_VIRTUAL_HARD_KEY': 64,
            'FLAG_WOKE_HERE': 1,
            'KEYCODE_0': 7,
            'KEYCODE_1': 8,
            'KEYCODE_11': 227,
            'KEYCODE_12': 228,
            'KEYCODE_2': 9,
            'KEYCODE_3': 10,
            'KEYCODE_3D_MODE': 206,
            'KEYCODE_4': 11,
            'KEYCODE_5': 12,
            'KEYCODE_6': 13,
            'KEYCODE_7': 14,
            'KEYCODE_8': 15,
            'KEYCODE_9': 16,
            'KEYCODE_A': 29,
            'KEYCODE_ALL_APPS': 284,
            'KEYCODE_ALT_LEFT': 57,
            'KEYCODE_ALT_RIGHT': 58,
            'KEYCODE_APOSTROPHE': 75,
            'KEYCODE_APP_SWITCH': 187,
            'KEYCODE_ASSIST': 219,
            'KEYCODE_AT': 77,
            'KEYCODE_AVR_INPUT': 182,
            'KEYCODE_AVR_POWER': 181,
            'KEYCODE_B': 30,
            'KEYCODE_BACK': 4,
            'KEYCODE_BACKSLASH': 73,
            'KEYCODE_BOOKMARK': 174,
            'KEYCODE_BREAK': 121,
            'KEYCODE_BRIGHTNESS_DOWN': 220,
            'KEYCODE_BRIGHTNESS_UP': 221,
            'KEYCODE_BUTTON_1': 188,
            'KEYCODE_BUTTON_10': 197,
            'KEYCODE_BUTTON_11': 198,
            'KEYCODE_BUTTON_12': 199,
            'KEYCODE_BUTTON_13': 200,
            'KEYCODE_BUTTON_14': 201,
            'KEYCODE_BUTTON_15': 202,
            'KEYCODE_BUTTON_16': 203,
            'KEYCODE_BUTTON_2': 189,
            'KEYCODE_BUTTON_3': 190,
            'KEYCODE_BUTTON_4': 191,
            'KEYCODE_BUTTON_5': 192,
            'KEYCODE_BUTTON_6': 193,
            'KEYCODE_BUTTON_7': 194,
            'KEYCODE_BUTTON_8': 195,
            'KEYCODE_BUTTON_9': 196,
            'KEYCODE_BUTTON_A': 96,
            'KEYCODE_BUTTON_B': 97,
            'KEYCODE_BUTTON_C': 98,
            'KEYCODE_BUTTON_L1': 102,
            'KEYCODE_BUTTON_L2': 104,
            'KEYCODE_BUTTON_MODE': 110,
            'KEYCODE_BUTTON_R1': 103,
            'KEYCODE_BUTTON_R2': 105,
            'KEYCODE_BUTTON_SELECT': 109,
            'KEYCODE_BUTTON_START': 108,
            'KEYCODE_BUTTON_THUMBL': 106,
            'KEYCODE_BUTTON_THUMBR': 107,
            'KEYCODE_BUTTON_X': 99,
            'KEYCODE_BUTTON_Y': 100,
            'KEYCODE_BUTTON_Z': 101,
            'KEYCODE_C': 31,
            'KEYCODE_CALCULATOR': 210,
            'KEYCODE_CALENDAR': 208,
            'KEYCODE_CALL': 5,
            'KEYCODE_CAMERA': 27,
            'KEYCODE_CAPS_LOCK': 115,
            'KEYCODE_CAPTIONS': 175,
            'KEYCODE_CHANNEL_DOWN': 167,
            'KEYCODE_CHANNEL_UP': 166,
            'KEYCODE_CLEAR': 28,
            'KEYCODE_COMMA': 55,
            'KEYCODE_CONTACTS': 207,
            'KEYCODE_COPY': 278,
            'KEYCODE_CTRL_LEFT': 113,
            'KEYCODE_CTRL_RIGHT': 114,
            'KEYCODE_CUT': 277,
            'KEYCODE_D': 32,
            'KEYCODE_DEL': 67,
            'KEYCODE_DEMO_APP_1': 301,
            'KEYCODE_DEMO_APP_2': 302,
            'KEYCODE_DEMO_APP_3': 303,
            'KEYCODE_DEMO_APP_4': 304,
            'KEYCODE_DPAD_CENTER': 23,
            'KEYCODE_DPAD_DOWN': 20,
            'KEYCODE_DPAD_DOWN_LEFT': 269,
            'KEYCODE_DPAD_DOWN_RIGHT': 271,
            'KEYCODE_DPAD_LEFT': 21,
            'KEYCODE_DPAD_RIGHT': 22,
            'KEYCODE_DPAD_UP': 19,
            'KEYCODE_DPAD_UP_LEFT': 268,
            'KEYCODE_DPAD_UP_RIGHT': 270,
            'KEYCODE_DVR': 173,
            'KEYCODE_E': 33,
            'KEYCODE_EISU': 212,
            'KEYCODE_ENDCALL': 6,
            'KEYCODE_ENTER': 66,
            'KEYCODE_ENVELOPE': 65,
            'KEYCODE_EQUALS': 70,
            'KEYCODE_ESCAPE': 111,
            'KEYCODE_EXPLORER': 64,
            'KEYCODE_F': 34,
            'KEYCODE_F1': 131,
            'KEYCODE_F10': 140,
            'KEYCODE_F11': 141,
            'KEYCODE_F12': 142,
            'KEYCODE_F2': 132,
            'KEYCODE_F3': 133,
            'KEYCODE_F4': 134,
            'KEYCODE_F5': 135,
            'KEYCODE_F6': 136,
            'KEYCODE_F7': 137,
            'KEYCODE_F8': 138,
            'KEYCODE_F9': 139,
            'KEYCODE_FEATURED_APP_1': 297,
            'KEYCODE_FEATURED_APP_2': 298,
            'KEYCODE_FEATURED_APP_3': 299,
            'KEYCODE_FEATURED_APP_4': 300,
            'KEYCODE_FOCUS': 80,
            'KEYCODE_FORWARD': 125,
            'KEYCODE_FORWARD_DEL': 112,
            'KEYCODE_FUNCTION': 119,
            'KEYCODE_G': 35,
            'KEYCODE_GRAVE': 68,
            'KEYCODE_GUIDE': 172,
            'KEYCODE_H': 36,
            'KEYCODE_HEADSETHOOK': 79,
            'KEYCODE_HELP': 259,
            'KEYCODE_HENKAN': 214,
            'KEYCODE_HOME': 3,
            'KEYCODE_I': 37,
            'KEYCODE_INFO': 165,
            'KEYCODE_INSERT': 124,
            'KEYCODE_J': 38,
            'KEYCODE_K': 39,
            'KEYCODE_KANA': 218,
            'KEYCODE_KATAKANA_HIRAGANA': 215,
            'KEYCODE_L': 40,
            'KEYCODE_LANGUAGE_SWITCH': 204,
            'KEYCODE_LAST_CHANNEL': 229,
            'KEYCODE_LEFT_BRACKET': 71,
            'KEYCODE_M': 41,
            'KEYCODE_MANNER_MODE': 205,
            'KEYCODE_MEDIA_AUDIO_TRACK': 222,
            'KEYCODE_MEDIA_CLOSE': 128,
            'KEYCODE_MEDIA_EJECT': 129,
            'KEYCODE_MEDIA_FAST_FORWARD': 90,
            'KEYCODE_MEDIA_NEXT': 87,
            'KEYCODE_MEDIA_PAUSE': 127,
            'KEYCODE_MEDIA_PLAY': 126,
            'KEYCODE_MEDIA_PLAY_PAUSE': 85,
            'KEYCODE_MEDIA_PREVIOUS': 88,
            'KEYCODE_MEDIA_RECORD': 130,
            'KEYCODE_MEDIA_REWIND': 89,
            'KEYCODE_MEDIA_SKIP_BACKWARD': 273,
            'KEYCODE_MEDIA_SKIP_FORWARD': 272,
            'KEYCODE_MEDIA_STEP_BACKWARD': 275,
            'KEYCODE_MEDIA_STEP_FORWARD': 274,
            'KEYCODE_MEDIA_STOP': 86,
            'KEYCODE_MEDIA_TOP_MENU': 226,
            'KEYCODE_MENU': 82,
            'KEYCODE_META_LEFT': 117,
            'KEYCODE_META_RIGHT': 118,
            'KEYCODE_MINUS': 69,
            'KEYCODE_MOVE_END': 123,
            'KEYCODE_MOVE_HOME': 122,
            'KEYCODE_MUHENKAN': 213,
            'KEYCODE_MUSIC': 209,
            'KEYCODE_MUTE': 91,
            'KEYCODE_N': 42,
            'KEYCODE_NAVIGATE_IN': 262,
            'KEYCODE_NAVIGATE_NEXT': 261,
            'KEYCODE_NAVIGATE_OUT': 263,
            'KEYCODE_NAVIGATE_PREVIOUS': 260,
            'KEYCODE_NOTIFICATION': 83,
            'KEYCODE_NUM': 78,
            'KEYCODE_NUMPAD_0': 144,
            'KEYCODE_NUMPAD_1': 145,
            'KEYCODE_NUMPAD_2': 146,
            'KEYCODE_NUMPAD_3': 147,
            'KEYCODE_NUMPAD_4': 148,
            'KEYCODE_NUMPAD_5': 149,
            'KEYCODE_NUMPAD_6': 150,
            'KEYCODE_NUMPAD_7': 151,
            'KEYCODE_NUMPAD_8': 152,
            'KEYCODE_NUMPAD_9': 153,
            'KEYCODE_NUMPAD_ADD': 157,
            'KEYCODE_NUMPAD_COMMA': 159,
            'KEYCODE_NUMPAD_DIVIDE': 154,
            'KEYCODE_NUMPAD_DOT': 158,
            'KEYCODE_NUMPAD_ENTER': 160,
            'KEYCODE_NUMPAD_EQUALS': 161,
            'KEYCODE_NUMPAD_LEFT_PAREN': 162,
            'KEYCODE_NUMPAD_MULTIPLY': 155,
            'KEYCODE_NUMPAD_RIGHT_PAREN': 163,
            'KEYCODE_NUMPAD_SUBTRACT': 156,
            'KEYCODE_NUM_LOCK': 143,
            'KEYCODE_O': 43,
            'KEYCODE_P': 44,
            'KEYCODE_PAGE_DOWN': 93,
            'KEYCODE_PAGE_UP': 92,
            'KEYCODE_PAIRING': 225,
            'KEYCODE_PASTE': 279,
            'KEYCODE_PERIOD': 56,
            'KEYCODE_PICTSYMBOLS': 94,
            'KEYCODE_PLUS': 81,
            'KEYCODE_POUND': 18,
            'KEYCODE_POWER': 26,
            'KEYCODE_PROFILE_SWITCH': 288,
            'KEYCODE_PROG_BLUE': 186,
            'KEYCODE_PROG_GREEN': 184,
            'KEYCODE_PROG_RED': 183,
            'KEYCODE_PROG_YELLOW': 185,
            'KEYCODE_Q': 45,
            'KEYCODE_R': 46,
            'KEYCODE_REFRESH': 285,
            'KEYCODE_RIGHT_BRACKET': 72,
            'KEYCODE_RO': 217,
            'KEYCODE_S': 47,
            'KEYCODE_SCROLL_LOCK': 116,
            'KEYCODE_SEARCH': 84,
            'KEYCODE_SEMICOLON': 74,
            'KEYCODE_SETTINGS': 176,
            'KEYCODE_SHIFT_LEFT': 59,
            'KEYCODE_SHIFT_RIGHT': 60,
            'KEYCODE_SLASH': 76,
            'KEYCODE_SLEEP': 223,
            'KEYCODE_SOFT_LEFT': 1,
            'KEYCODE_SOFT_RIGHT': 2,
            'KEYCODE_SOFT_SLEEP': 276,
            'KEYCODE_SPACE': 62,
            'KEYCODE_STAR': 17,
            'KEYCODE_STB_INPUT': 180,
            'KEYCODE_STB_POWER': 179,
            'KEYCODE_STEM_1': 265,
            'KEYCODE_STEM_2': 266,
            'KEYCODE_STEM_3': 267,
            'KEYCODE_STEM_PRIMARY': 264,
            'KEYCODE_SWITCH_CHARSET': 95,
            'KEYCODE_SYM': 63,
            'KEYCODE_SYSRQ': 120,
            'KEYCODE_SYSTEM_NAVIGATION_DOWN': 281,
            'KEYCODE_SYSTEM_NAVIGATION_LEFT': 282,
            'KEYCODE_SYSTEM_NAVIGATION_RIGHT': 283,
            'KEYCODE_SYSTEM_NAVIGATION_UP': 280,
            'KEYCODE_T': 48,
            'KEYCODE_TAB': 61,
            'KEYCODE_THUMBS_DOWN': 287,
            'KEYCODE_THUMBS_UP': 286,
            'KEYCODE_TV': 170,
            'KEYCODE_TV_ANTENNA_CABLE': 242,
            'KEYCODE_TV_AUDIO_DESCRIPTION': 252,
            'KEYCODE_TV_AUDIO_DESCRIPTION_MIX_DOWN': 254,
            'KEYCODE_TV_AUDIO_DESCRIPTION_MIX_UP': 253,
            'KEYCODE_TV_CONTENTS_MENU': 256,
            'KEYCODE_TV_DATA_SERVICE': 230,
            'KEYCODE_TV_INPUT': 178,
            'KEYCODE_TV_INPUT_COMPONENT_1': 249,
            'KEYCODE_TV_INPUT_COMPONENT_2': 250,
            'KEYCODE_TV_INPUT_COMPOSITE_1': 247,
            'KEYCODE_TV_INPUT_COMPOSITE_2': 248,
            'KEYCODE_TV_INPUT_HDMI_1': 243,
            'KEYCODE_TV_INPUT_HDMI_2': 244,
            'KEYCODE_TV_INPUT_HDMI_3': 245,
            'KEYCODE_TV_INPUT_HDMI_4': 246,
            'KEYCODE_TV_INPUT_VGA_1': 251,
            'KEYCODE_TV_MEDIA_CONTEXT_MENU': 257,
            'KEYCODE_TV_NETWORK': 241,
            'KEYCODE_TV_NUMBER_ENTRY': 234,
            'KEYCODE_TV_POWER': 177,
            'KEYCODE_TV_RADIO_SERVICE': 232,
            'KEYCODE_TV_SATELLITE': 237,
            'KEYCODE_TV_SATELLITE_BS': 238,
            'KEYCODE_TV_SATELLITE_CS': 239,
            'KEYCODE_TV_SATELLITE_SERVICE': 240,
            'KEYCODE_TV_TELETEXT': 233,
            'KEYCODE_TV_TERRESTRIAL_ANALOG': 235,
            'KEYCODE_TV_TERRESTRIAL_DIGITAL': 236,
            'KEYCODE_TV_TIMER_PROGRAMMING': 258,
            'KEYCODE_TV_ZOOM_MODE': 255,
            'KEYCODE_U': 49,
            'KEYCODE_UNKNOWN': 0,
            'KEYCODE_V': 50,
            'KEYCODE_VIDEO_APP_1': 289,
            'KEYCODE_VIDEO_APP_2': 290,
            'KEYCODE_VIDEO_APP_3': 291,
            'KEYCODE_VIDEO_APP_4': 292,
            'KEYCODE_VIDEO_APP_5': 293,
            'KEYCODE_VIDEO_APP_6': 294,
            'KEYCODE_VIDEO_APP_7': 295,
            'KEYCODE_VIDEO_APP_8': 296,
            'KEYCODE_VOICE_ASSIST': 231,
            'KEYCODE_VOLUME_DOWN': 25,
            'KEYCODE_VOLUME_MUTE': 164,
            'KEYCODE_VOLUME_UP': 24,
            'KEYCODE_W': 51,
            'KEYCODE_WAKEUP': 224,
            'KEYCODE_WINDOW': 171,
            'KEYCODE_X': 52,
            'KEYCODE_Y': 53,
            'KEYCODE_YEN': 216,
            'KEYCODE_Z': 54,
            'KEYCODE_ZENKAKU_HANKAKU': 211,
            'KEYCODE_ZOOM_IN': 168,
            'KEYCODE_ZOOM_OUT': 169,
            'MAX_KEYCODE': 84,
            'META_ALT_LEFT_ON': 16,
            'META_ALT_MASK': 50,
            'META_ALT_ON': 2,
            'META_ALT_RIGHT_ON': 32,
            'META_CAPS_LOCK_ON': 1048576,
            'META_CTRL_LEFT_ON': 8192,
            'META_CTRL_MASK': 28672,
            'META_CTRL_ON': 4096,
            'META_CTRL_RIGHT_ON': 16384,
            'META_FUNCTION_ON': 8,
            'META_META_LEFT_ON': 131072,
            'META_META_MASK': 458752,
            'META_META_ON': 65536,
            'META_META_RIGHT_ON': 262144,
            'META_NUM_LOCK_ON': 2097152,
            'META_SCROLL_LOCK_ON': 4194304,
            'META_SHIFT_LEFT_ON': 64,
            'META_SHIFT_MASK': 193,
            'META_SHIFT_ON': 1,
            'META_SHIFT_RIGHT_ON': 128,
            'META_SYM_ON': 4
        }
        
        self.APP = {
            '抖音':'com.ss.android.ugc.aweme/.splash.SplashActivity',
            '抖音极速版':'com.ss.android.ugc.aweme.lite/com.ss.android.ugc.aweme.main.MainActivity',
            '快手极速版':'com.kuaishou.nebula/com.yxcorp.gifshow.HomeActivity',
            '学习强国':'cn.xuexi.android/com.alibaba.android.rimet.biz.SplashActivity'
        }
        
        self.cwd = os.path.abspath(os.path.dirname(__file__)).replace('\\', '/')
        
        os.system(f'{self.adb} start-server')
    
    
    def showDeviceInfo(self):
        os.system(f'{self.adb} devices -l')
    
    
    def showActivity(self):
        os.system(f'{self.adb} shell dumpsys activity activities | findstr mResumedActivity')
    
    
    def startAPP(self, appname:str) -> bool:
        # 此处使用subprocess.Popen是为了捕获错误信息
        with subprocess.Popen(
            f'{self.adb} shell am start -n {self.APP[appname]}',
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            ) as p:
            result = p.stdout.read()
            error = p.stderr.read()
        
        if error == b'':
            print(str(result, encoding='utf-8'))
            return True
        else:
            print(str(error, encoding='utf-8'))
            return False
    
    
    def touchScreen(self, x, y):
        os.system(f'{self.adb} shell input tap {x} {y}')
    
    
    def swipeScreen(self, start_x, start_y, end_x, end_y, duration = ''):
        os.system(f'{self.adb} shell input swipe {start_x} {start_y} {end_x} {end_y} {duration}')
    
    
    def pressKeyCode(self, keycode):
        os.system(f'{self.adb} shell input keyevent {keycode}')
    
    
    def longPressKeyCode(self, keycode):
        os.system(f'{self.adb} shell input keyevent --longpress {keycode}')
    
    
    def pressKey(self, keyname):
        os.system(f'{self.adb} shell input keyevent {self.KEY[keyname]}')
    
    
    def uiDump(self, device_path=''):
        # 此处使用subprocess.Popen是为了避免控制台打印错误信息
        with subprocess.Popen(
            f'{self.adb} shell uiautomator dump --compressed {device_path}',
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL
            ) as p:
            result = p.stdout.read()
        result = str(result, encoding='utf-8')
        
        if 'dumped to:' in result:
            return result.split()[-1]
    
    
    def pullFile(self, device_path, local_path=''):
        with subprocess.Popen(
            f'{self.adb} pull {device_path} {local_path}',
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL
            ) as p:
            result = p.stdout.read()
        result = str(result, encoding='utf-8')
        
        if 'pulled' in result:
            if local_path == '':
                local_path = f'{self.cwd}/{os.path.split(device_path)[-1]}'
            return local_path
