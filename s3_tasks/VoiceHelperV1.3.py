# 语音助手
# 2018-05-31
# coding:utf-8

import urllib.request
import urllib
import json
import base64
import os
import wave
import pyaudio
import pygame as pg
import time


class BaiduRest:
    def __init__(self, cu_id, api_key, api_secert):
        # token认证的url
        self.token_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s"
        # 语音合成的resturl
        self.getvoice_url = "http://tsn.baidu.com/text2audio?tex=%s&lan=zh&cuid=%s&ctp=1&tok=%s"
        # 语音识别的resturl
        self.upvoice_url = 'http://vop.baidu.com/server_api'

        self.cu_id = cu_id

        self.getToken(api_key, api_secert)
        return

    def getToken(self, api_key, api_secert):
        # 1.获取token
        token_url = self.token_url % (api_key, api_secert)

        r_str = urllib.request.urlopen(token_url).read()
        token_data = json.loads(r_str)
        self.token_str = token_data['access_token']
        pass

    def getVoice(self, text, filename):
        # 2. 向Rest接口提交数据
        get_url = self.getvoice_url % (urllib.parse.quote(text), self.cu_id, self.token_str)

        voice_data = urllib.request.urlopen(get_url).read()
        # 3.处理返回数据
        voice_fp = open(filename, 'wb+')
        voice_fp.write(voice_data)
        voice_fp.close()
        pass

    def getText(self, filename):
        # 2. 向Rest接口提交数据
        data = {}
        # 语音的一些参数
        data['format'] = 'wav'
        data['rate'] = 16000
        data['channel'] = 1
        data['cuid'] = self.cu_id
        data['token'] = self.token_str
        wav_fp = open(filename, 'rb')
        voice_data = wav_fp.read()
        data['len'] = len(voice_data)
        data['speech'] = base64.b64encode(voice_data).decode('utf-8')
        post_data = json.dumps(data)
        r_data = urllib.request.urlopen(self.upvoice_url, data=bytes(post_data, encoding="utf-8")).read()
        # 3.处理返回数据
        return json.loads(r_data)['result']


class RecoderAndPlay():

    def recoder(self, seconds, filename):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000
        RECORD_SECONDS = seconds
        WAVE_OUTPUT_FILENAME = filename
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("小豆豆：好的，让我想想你说的什么~")
        stream.stop_stream()
        stream.close()
        p.terminate()
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    def play_music(self, music_file):
        '''
        stream music with mixer.music module in blocking manner
        this will stream the sound from disk while playing
        '''
        freq = 16000  # audio CD quality

        bitsize = -16  # unsigned 16 bit
        # channels = 1  # 1 is mono, 2 is stereo
        channels = 2  # 1 is mono, 2 is stereo

        buffer = 2048  # number of samples (experiment to get right sound)
        pg.mixer.init(freq, bitsize, channels, buffer)
        # optional volume 0 to 1.0
        pg.mixer.music.set_volume(0.8)
        try:
            clock = pg.time.Clock()
            try:
                pg.mixer.music.load(music_file)
                # print("Music file {} loaded!".format(music_file))
            except Exception as e:
                # print("File {} not found! {}".format(music_file, pg.get_error()))
                return
            pg.mixer.music.play()
            # check if playback has finished
            while pg.mixer.music.get_busy():
                clock.tick(30)
        except KeyboardInterrupt:
            # if user hits Ctrl/C then exit
            pg.mixer.music.fadeout(1000)
            pg.mixer.music.stop()
            raise SystemExit


def judge(str):
    # 传入字符串，逻辑判断模块，有待扩展
    if str.strip() == '':
        ret_text = "我没有听到声音,请再说一遍"
    elif "小姐姐" in str:
        ret_text = "叫我干嘛？"
    else:
        ret_text = "我没有听懂，请再说一遍"
    print("小豆豆：",ret_text)
    return ret_text


if __name__ == "__main__":
    # 我的api_key,供大家测试用，在实际工程中请换成自己申请的应用的key和secert
    api_key = "HqyYoGUsoMUaW1D6csev3jKG"
    api_secert = "92lZKBLmMaswDN8ZDObqwVuI5pelPQZz"
    # 初始化
    bdr = BaiduRest('1131248689625', api_key, api_secert)
    rnp = RecoderAndPlay()
    # 播放打招呼语音
    print("小豆豆：你好啊~，我是你的语音助手小豆豆，请调教我吧~~")
    rnp.play_music("hello.mp3")
    time.sleep(1)
    try:
        # 播放语音提示录入
        sec=5
        print("小豆豆：开始对话吧，你有%d秒时间和我交谈" % sec)
        rnp.play_music("dialog.mp3")
        # 录音，存入input文件
        rnp.recoder(sec, "input.wav")
        # 播放语音提示处理
        rnp.play_music("think.mp3")
        # 发往百度，进行语音识别
        rec_text = bdr.getText("input.wav")
        rec_text = rec_text[0]
        print("小豆豆：你说的是不是，", rec_text)
        # 逻辑判断
        ret_text = judge(rec_text)
        # 语音合成
        bdr.getVoice(str(ret_text), "output.mp3")
        # 语音播放
        rnp.play_music("output.mp3")
        # #移除缓存文件
        os.remove("./input.wav")
        # os.remove("./output.mp3")
        # os.remove("./output.wav")
    except Exception as e:
        print("错误：", e)
