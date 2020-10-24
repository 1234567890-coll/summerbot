import discord
from discord import activity
from discord.embeds import Embed
from discord.ext import commands
import asyncio
import re
import datetime
from parser import *
import random
import time
import os
import urllib.request
import json
import bs4
import urllib.request
import sys
import youtube_dl
from urllib.request import urlopen, Request 
import urllib
from selenium import webdriver
import openpyxl
from discord import Member
import requests, re
from bs4 import BeautifulSoup
from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen
from urllib.request import Request, urlopen
import warnings
import unicodedata
from urllib.parse import quote
import time

client = discord.Client()
calcResult = 0




token = "NzYwNTE1NzU1MDYxMjgwNzg5.X3NLfQ.Y-9EBx3GAkhxYO-Gx04p2YbpExY"
client = commands.Bot(command_prefix='/')
mod = 0
msg = ''



@client.event
async def on_ready():

    print("=========================")
    print("다음으로 로그인 합니다 : ")
    print(client.user.name)
    print("connection was successful")
    game = discord.Game("봇이 활동 중에 표시 될 이름")
    print("=========================")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "안녕":
        await message.channel.send
        ("ㅎㅇ!")
    if message.content == "ㅋㅋㄹㅃㅃ":
        await message.channel.send
        ("크크루삥뽕")
    if message.content == "재익 컴퍼니":
        await message.channel.send
        ("재익 컴퍼니는 약탈 서버로 기획중 추후에 서버 개발 예정이다")
    if message.content == "레식":
        await message.channel.send
        ("감자도리 서버에 FPS게임")
    if message.content == "토피아":
        await message.channel.send
        ("http:www.topia.co.krgateindex.asp")
    if message.content == "배그":
        await message.channel.send
        ("FPS시장의 한획을 그은겜!") 
    if message.content == "사랑해":
        await message.channel.send
        ("(?)")
    if message.content == "영어 중간고사":
        await message.channel.send
        ("https:bit.ly36iJxRr")
    if message.content == "짜증나":
        await message.channel.send
        ("미안해요...")
    if message.content == "너 떄문에 아니야":
        await message.channel.send
        ("**네!**")    
    if message.content == "고양이":
        await message.channel.send
        ("https:bit.ly31fe2EC")
    if message.content == "ㅋ":
        await message.channel.send
        ("ㅋㅋㅋㅋㅋㅋㅋ")
    if message.content == "ㅋㅋ":
        await message.channel.send
        ("ㅋㅋㅋㅋㅋ")
    if message.content == "ㅋㅋㅋ":
        await message.channel.send
        ("ㅋㅋㅋㅋㅋㅋ")
    if message.content.startswith('/너 인성문제 있어?'):
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="아닙니다!", color=discord.Color.blue()))
        else:
            await message.channel.send(message.channel, embed=discord.Embed(title="악!", colour=discord.Color.blue()))

    if message.content == "/핑":
        la = client.latency
        await message.channel.send(embed=discord.Embed(title=(f'{str(round(la * 1000))}ms'), colour=discord.Color.blue()))





    if message.content == "도움말":
        embed = discord.Embed(colour=0x5100FF, timestamp=message.created_at)
        embed.add_field(name="시간", value="현재 시간을 알려드립니다", inline=False)
        embed.add_field(name="핑", value="현재 봇의 핑을 알려드립니다", inline=False)
        embed.add_field(name="정보", value="자신의 정보를 볼수있습니다", inline=False)
        embed.add_field(name="가위바위보", value="가위바위보 규칙을 알려드립니다", inline=False)
        embed.add_field(name="테스트", value="봇이 잘작동되는지 알려드립니다", inline=False)
        embed.add_field(name="채팅청소", value="채팅을 청소 해줍니다 (**제한 없음**)", inline=False)
        embed.add_field(name="킥 @맨션", value="유저를 킥합니다", inline=False)
        embed.add_field(name="밴 @맨션", value="유저를 밴합니다", inline=False)
        embed.add_field(name="초대링크", value="초대링크 사용법을 알려드립니다", inline=False)
        embed.add_field(name="디엠", value="전체공지를 DM으로 합니다", inline=False)
        embed.add_field(name="이미지(검색)", value="원하는 이미지가 검색됩니다", inline=False)
        embed.add_field(name="고양이", value="랜덤으로 고양이 사진이 나옵니다", inline=False)
        embed.add_field(name="강아지", value="랜덤으로 강아지 사진이 나옵니다", inline=False)
        embed.add_field(name="랜덤 사진", value="랜덤으로 사진이 올라옵니다", inline=False)
        embed.add_field(name="복권", value="가상 복권을 랜덤으로 줍니다", inline=False)
        embed.add_field(name="주사위", value="랜덤으로 1~6까지의 숫자가 나옵니다", inline=False)
        embed.add_field(name="랜덤 이모티콘", value="랜덤으로 이모티콘을 줍니다", inline=False)
        embed.add_field(name="타이머", value="타이머를 설정합니다", inline=False)
        embed.add_field(name="익스마을 예산", value="지금 익스마을의 예산을 알려줍니다", inline=False)
        embed.add_field(name="익스마을 도움말", value="익스마을의 도움말을 알려드립니다", inline=False)
        embed.add_field(name="익스마을 혜택", value="익스마을의 혜택을 알려드립니다", inline=False)
        embed.add_field(name="익스마을 이벤트", value="익스마을의 이벤트를 알려드립니다", inline=False)
        embed.add_field(name="익스마을 인원", value="익스마을의 인원을 알려드립니다", inline=False)
        embed.add_field(name="익스마을 정보", value="익스마을의 정보를 알려드립니다", inline=False)
        embed.add_field(name="익스마을 역할", value="익스마을의 역할을 알려드립니다", inline=False)
        embed.add_field(name="익스마을 규칙", value="익스마을의 하지말아야할 규칙을 알려드립니다", inline=False)
        embed.set_footer(text=f"{message.author}, 작성자", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == "익스마을 도움말":
        embed = discord.Embed(colour=0x5100FF, timestamp=message.created_at)
        embed.add_field(name="익스마을 예산", value="지금 익스마을의 예산을 알려줍니다", inline=False)
        embed.add_field(name="익스마을 혜택", value="익스마을의 혜택을 알려드립니다", inline=False)
        embed.add_field(name="익스마을 이벤트", value="익스마을의 이벤트를 알려드립니다", inline=False)
        embed.add_field(name="익스마을 인원", value="익스마을의 인원을 알려드립니다", inline=False)
        embed.add_field(name="익스마을 정보", value="익스마을의 정보를 알려드립니다", inline=False)
        embed.add_field(name="익스마을 역할", value="익스마을의 역할을 알려드립니다", inline=False)
        embed.add_field(name="익스마을 규칙", value="익스마을의 하지말아야할 규칙을 알려드립니다", inline=False)
        embed.set_footer(text=f"{message.author}, 작성자", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == "익스마을 예산":
        embed = discord.Embed(colour=0x5100FF, timestamp=message.created_at)
        embed.add_field(name="익스마을 총 예산 가치액", value="현재 예산:0원 입니다", inline=False)

    if message.content == "익스마을 혜택":
        embed = discord.Embed(colour=0x5100FF, timestamp=message.created_at)
        embed.add_field(name="익스마을 혜택 1번쨰", value="만약 여러분이 돈이 필요하다 계급에 따라서 한도가 있습니다! 그걸로 필요할떄 말해주세요", inline=False)
        embed.add_field(name="익스마을 혜택 2번쨰", value="마을에서 계약이 끝나면 사회에 잘나가라고 아이템과 소량의 돈을 드립니다", inline=False)
        embed.add_field(name="익스마을 혜택 3번쨰", value="마을의 공용 기부함이 있습니다 거기서 저희가 탬을 기부할거기 떄문에 보시는것도 좋으실거 같습니다 소량의 돈도 있을수 있습니다", inline=False)
        embed.add_field(name="익스마을 혜택 4번쨰", value="저희는 우수원을 뽑아서 소량의 돈을 드릴것입니다", inline=False)
        embed.add_field(name="익스마을 혜택 5번쨰", value="마을에서 이벤트도 할것입니다 이벤트의 난이도에따라 받는 돈이 다 같지 않습니다 (**어쩔때는 소,중 말고 대량의 돈을 드립니다!**)", inline=False)
        embed.add_field(name="익스마을 혜택 6번쨰", value="만약 익스마을 건축가 기술자가 되고싶다면 지원금을 드립니다!", inline=False)
        embed.add_field(name="익스마을 혜택 7번쨰", value="저희는 전쟁에 이기면 항복금을 지급합니다 (**항복금에 30%는 세금으로 걷어 갈겄이고 70%를 공동배분 할것입니다 부마을장 마을장은 돈을 안받습니다**", inline=False)
        embed.add_field(name="익스마을 혜택 8번쨰", value="만약 게임에서 1분이 당첨되면 그분에게 최신형 익스마을에 있는집,대량의돈,중량의 돈 + MVP++++, 한도 추가가 있습니다(**4가지 중에서 골라야 합니다**)", inline=False)
        embed.add_field(name="익스마을 혜택 9번쨰", value="만약 마을이 10위건 안에 들면 다량의 돈을 나눠드릴것이고 1단계 씩 오를떄마다 이벤트와 소량의 돈을 지급할것입니다", inline=False)
        embed.add_field(name="익스마을 혜택 10번쨰", value="배고프면 무료 급식 배급소에 오십시요 직원들이 줄것입니다", inline=False)
        embed.add_field(name="익스마을 혜택 11번쨰", value="대출을 받을수있습니다 실제로 무이자 14일 까지 가능합니다 그다음부터는 이자 지급해야합니다", inline=False)
        embed.set_footer(text=f"{message.author}, 작성자", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == "초대링크":
        embed = discord.Embed(colour=0x5100FF, timestamp=message.created_at)
        embed.add_field(name="초대링크 30", value="30분짜리 초대링크 입니다", inline=False)
        embed.add_field(name="초대링크 60", value="60분 즉 1시간 짜리 초대링크 입니다", inline=False)
        embed.add_field(name="초대링크 6시간", value="6시간 짜리 초대링크 입니다", inline=False)
        embed.add_field(name="초대링크 12시간", value="12시간짜리 초대링크 입니다", inline=False)
        embed.add_field(name="초대링크 1일", value="1일짜리 초대링크 입니다", inline=False)
        embed.add_field(name="초대링크 영구", value="영구 초대링크 입니다", inline=False)
        embed.set_footer(text=f"{message.author}, 작성자", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    
 
    if message.content.startswith("/채팅청소"):
        if message.author.guild_permissions.manage_messages:
            try:
                amount = message.content[6:]
                await message.channel.purge(limit=int(amount))
                await message.channel.send(embed=discord.Embed(title=(f"**{amount}**개의 메시지를 지웠습니다."), colour=discord.Color.blue()))
            except ValueError:
                await message.channel.send
                ("청소하실 메시지의 **수**를 입력해 주세요.")
        else:
            await message.channel.send
            ("권한이 없습니다.")
 
    if message.content.startswith("정보"):
       date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
       embed = discord.Embed(colour=0x5100FF, timestamp=message.created_at)
       embed.add_field(name="이름", value=message.author.name, inline=False)
       embed.add_field(name="서버닉네임", value=message.author.display_name, inline=False)
       embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=False)
       embed.add_field(name="아이디", value=message.author.id, inline=False)
       embed.set_thumbnail(url=message.author.avatar_url)
       await message.channel.send(message.channel, embed=embed)













    if message.content.startswith('/DM'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.id == 700967119696822273:
                        embed = discord.Embed(colour=0x5100FF, timestamp=message.created_at, title="__**공지**__")
                        embed.add_field(name="**여름샵 공지 입니다**", value=msg, inline=True)
                        embed.set_footer(text=f"{message.author}, 작성자", icon_url=message.author.avatar_url)
                        await i.send(embed=embed)
                except:
                    pass
                     

    
    if(message.content == "시간"):
        await message.channel.send
        await message.channel.send(embed=discord.Embed(title="Time", timestamp=datetime.datetime.utcnow()))

    if message.content.startswith("킥"):
        if message.author.guild_permissions.Adminstartor:
            userid = message.content[3:]
            user_id = re.findall("\d+", userid)
            userkick = message.guild.get_member(int(user_id[0]))
            await message.guild.kick(userkick)
            await message.channel.send
            (str(userkick) + "님을 추방했습니다")



    if message.content.startswith("밴"):
        if message.author.guild_permissions.administrator:
            userid = message.content[3:]
            user_id = re.findall("\d+", userid)
            userban = message.guild.get_member(int(user_id[0]))
            await message.guild.ban(userban)
            await message.channel.send
            (str(userban) + "님을 차단했습니다") 


    if message.content == "초대링크 30":
        embed = discord.Embed(colour=0x5100FF, timestamp=message.created_at)
        embed.add_field(name="✔밑에 초대링크가 있습니다!✔", value="https:discord.ggMk8wkr", inline=False)
        embed.set_footer(text=f"{message.author}, 작성자", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == "초대링크 60":
        embed = discord.Embed(colour=0x5100FF, timestamp=message.created_at)
        embed.add_field(name="✔밑에 초대링크가 있습니다!✔", value="https:discord.ggnQZ5uH", inline=False)
        embed.set_footer(text=f"{message.author}, 작성자", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == "초대링크 6시간":
        embed = discord.Embed(colour=0x5100FF, timestamp=message.created_at)
        embed.add_field(name="✔밑에 초대링크가 있습니다!✔", value="https:discord.ggqVFHWA", inline=False)
        embed.set_footer(text=f"{message.author}, 작성자", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == "초대링크 12시간":
        embed = discord.Embed(colour=0x5100FF, timestamp=message.created_at)
        embed.add_field(name="✔밑에 초대링크가 있습니다!✔", value="https:discord.ggBrkG9e", inline=False)
        embed.set_footer(text=f"{message.author}, 작성자", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == "초대링크 1일":
        embed = discord.Embed(colour=0x5100FF, timestamp=message.created_at)
        embed.add_field(name="✔밑에 초대링크가 있습니다!✔", value="https:discord.ggUQ6PKR", inline=False)
        embed.set_footer(text=f"{message.author}, 작성자", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == "초대링크 영구":
        embed = discord.Embed(colour=0x5100FF, timestamp=message.created_at)
        embed.add_field(name="✔밑에 초대링크가 있습니다!✔", value="https:discord.ggcEppGRP", inline=False)
        embed.set_footer(text=f"{message.author}, 작성자", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)


    

    if message.content == "테스트":
        embed = discord.Embed(colour=0x5100FF, timestamp=message.created_at)
        embed.add_field(name="봇 작동 테스트", value="임베드가 잘작동하네요! 봇을 사용해도 괜찮을거 같습니다!", inline=False)
        embed.set_footer(text=f"{message.author}, 작성자", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == "관리자 도움말":
        if message.author.guild_permissions.administrator:
         embed = discord.Embed(colour=0x5100FF, timestamp=message.created_at)
         embed.add_field(name="킥", value="사람을 킥합니다", inline=False)
         embed.add_field(name="밴", value="사람을 밴합니다", inline=False)
         embed.add_field(name="디엠", value="전체 DM을 할수있습니다", inline=False)
         embed.add_field(name="채팅청소", value="메세지를 지울수있습니다 (*재한 없음*)", inline=False)
         embed.set_footer(text=f"{message.author}, 작성자", icon_url=message.author.avatar_url)(embed=embed)     

    if message.content == "가위바위보":
        embed = discord.Embed(colour=0x5100FF, timestamp=message.created_at)
        embed.add_field(name="가위바위보 규칙!", value="가위바위보 (바위,가위,보)중에서 고르세요!", inline=False)
        embed.add_field(name="게임에 너무 집착해주지 마세요!", value="**게임은 게임일 뿐 입니다**", inline=False)
        embed.add_field(name="가위바위보 재밌게 즐겨주세요!", value="이상 제작자 였습니다", inline=False)                 
        embed.set_footer(text=f"{message.author}, 작성자", icon_url=message.author.avatar_url)
        await message.channel.send
        await message.channel.send(embed=embed)
                          
    elif message.content.startswith('도배모드 키기'):
        time.sleep(1)
        await message.channel.send('3초후 도배모드 작동')
        time.sleep(1)
        await message.channel.send('2초후 도배모드 작동')
        time.sleep(1)
        await message.channel.send('1초후 도배모드 작동')
        time.sleep(1)
        mod = 0
        while mod < 1000:
            embed = discord.Embed(colour=0x5100FF, timestamp=message.created_at)
            embed = discord.Embed(title='도배모드 실행중', description='도배모드 작동중', color=0x5100FF)
            embed.set_footer(text='끄고 싶으면 도배모드 끄기 를 해주세요')
            await message.channel.send(embed=embed)
            mod = mod + 1

    elif message.content.startswith('도배모드 끄기'):
        mod = 1000
        await message.channel.send('도배모드 꺼짐')

    if message.content.startswith('고양이'):
        embed = discord.Embed(colour=0x5100FF, timestamp=message.created_at)
        embed.add_field(
            title='고양이는',
            description='냐옹',
            colour=0x5100FF()
        )

        urlBase = 'https:loremflickr.com320240?lock='
        randomNum = random.randrange(1, 30977)
        urlF = urlBase+str(randomNum)
        embed.set_image(url = urlF)
        await message.channel.send(message.channel, embed=embed)

    if message.content.startswith('강아지'):
        embed = discord.Embed(colour=0x5100FF, timestamp=message.created_at)
        embed.add_field(title='강아지는',description='멍멍')

        urlBase = 'https:loremflickr.com320240dog?lock='
        randomNum = random.randrange(1, 30977)
        urlF = urlBase+str(randomNum)
        embed.set_image(url = urlF)
        await message.channel.send
        await message.channel.send(message.channel, embed=embed)

    if message.content.startswith('랜덤 사진'):
        embed = discord.Embed(colour=0x5100FF, timestamp=message.created_at)
        embed.add_field
        embed2 = discord.Embed
        embed3 = discord.Embed
        randomnumber = random.randrange(100, 407)
        randomgiho = random.randrange(1,3)
        print('?번째사진 : '+str(randomnumber))
        print('기호 : '+str(randomgiho))
        strandomnumber = str(randomnumber)
        file1 = '.png'
        file2 = '.jpg'
        file3 = '.jpeg'
        giho = '_'
        if randomgiho==1:
            urlbase1 = "https:cdn.nekos.lifenekoneko" + strandomnumber + file1
            urlbase2 = "https:cdn.nekos.lifenekoneko" + strandomnumber + file2
            urlbase3 = "https:cdn.nekos.lifenekoneko" + strandomnumber + file3
            embed.set_image(url=urlbase1)
            embed2.set_image(url=urlbase2)
            embed3.set_image(url=urlbase3)
            await message.channel.send(message.channel, embed=embed)
            await message.channel.send(message.channel, embed=embed2)
            await message.channel.send(message.channel, embed=embed3)
        else:
            urlbase_1 = "https:cdn.nekos.lifenekoneko" + giho + strandomnumber + file1
            urlbase_2 = "https:cdn.nekos.lifenekoneko" + giho + strandomnumber + file2
            urlbase_3 = "https:cdn.nekos.lifenekoneko" + giho + strandomnumber + file3
            embed.set_image(url=urlbase_1)
            embed2.set_image(url=urlbase_2)
            embed3.set_image(url=urlbase_3)
            await message.channel.send(message.channel, embed=embed)
            await message.channel.send(message.channel, embed=embed2)
            await message.channel.send(message.channel, embed=embed3)

    if message.content.startswith("!복권"):
        Text = ""
        number = [1, 2, 3, 4, 5, 6, 7]
        count = 0
        for i in range(0, 7):
            num = random.randrange(1, 46)
            number[i] = num
            if count >= 1:
                for i2 in range(0, i):
                    if number[i] == number[i2]:  # 만약 현재랜덤값이 이전숫자들과 값이 같다면
                        numberText = number[i]
                        print("작동 이전값 : " + str(numberText))
                        number[i] = random.randrange(1, 46)
                        numberText = number[i]
                        print("작동 현재값 : " + str(numberText))
                        if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
                            numberText = number[i]
                            print("작동 이전값 : " + str(numberText))
                            number[i] = random.randrange(1, 46)
                            numberText = number[i]
                            print("작동 현재값 : " + str(numberText))
                            if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
                                numberText = number[i]
                                print("작동 이전값 : " + str(numberText))
                                number[i] = random.randrange(1, 46)
                                numberText = number[i]
                                print("작동 현재값 : " + str(numberText))

            count = count + 1
            Text = Text + "  " + str(number[i])

        print(Text.strip())
        embed = discord.Embed(
            title="복권 숫자!",
            description=Text.strip(),
            colour=discord.Color.red()
        )
        await message.channel.send(message.channel, embed=embed)

    if message.content.startswith('!이모티콘'):

        emoji = [" ꒰⑅ᵕ༚ᵕ꒱ ", " ꒰◍ˊ◡ˋ꒱ ", " ⁽⁽◝꒰ ˙ ꒳ ˙ ꒱◜⁾⁾ ", " ༼ つ ◕_◕ ༽つ ", " ⋌༼ •̀ ⌂ •́ ༽⋋ ",
                 " ( ･ิᴥ･ิ) ", " •ө• ", " ค^•ﻌ•^ค ", " つ╹㉦╹)つ ", " ◕ܫ◕ ", " ᶘ ͡°ᴥ͡°ᶅ ", " ( ؕؔʘ̥̥̥̥ ه ؔؕʘ̥̥̥̥ ) ",
                 " ( •́ ̯•̀ ) ",
                 " •̀.̫•́✧ ", " '͡•_'͡• ", " (΄◞ิ౪◟ิ‵) ", " ˵¯͒ བ¯͒˵ ", " ͡° ͜ʖ ͡° ", " ͡~ ͜ʖ ͡° ", " (づ｡◕‿‿◕｡)づ ",
                 " ´_ゝ` ", " ٩(͡◕_͡◕ ", " ⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄ ", " ٩(͡ï_͡ï☂ ", " ௐ ", " (´･ʖ̫･`) ", " ε⌯(ง ˙ω˙)ว ",
                 " (っ˘ڡ˘ς) ", "●▅▇█▇▆▅▄▇", "╋╋◀", "︻╦̵̵̿╤──", "ー═┻┳︻▄", "︻╦̵̵͇̿̿̿̿══╤─",
                 " ጿ ኈ ቼ ዽ ጿ ኈ ቼ ዽ ጿ ", "∑◙█▇▆▅▄▃▂", " ♋♉♋ ", " (๑╹ω╹๑) ", " (╯°□°）╯︵ ┻━┻ ",
                 " (▽) ", " σ(oдolll) ", " 【o´ﾟ□ﾟ`o】 ", " ＼(^o^)／ ", " (◕‿‿◕｡) ", " ･ᴥ･ ", " ꈍ﹃ꈍ "
                                                                                                 " ˃̣̣̣̣̣̣︿˂̣̣̣̣̣̣ ",
                 " ( ◍•㉦•◍ ) ", " (｡ì_í｡) ", " (╭•̀ﮧ •́╮) ", " ଘ(੭*ˊᵕˋ)੭ ", " ´_ゝ` ", " (~˘▾˘)~ "] # 이모티콘 배열입니다.

        randomNum = random.randrange(0, len(emoji)) # 0 ~ 이모티콘 배열 크기 중 랜덤숫자를 지정합니다.
        print("랜덤수 값 :" + str(randomNum))
        print(emoji[randomNum])
        await message.channel.send(message.channel, embed=discord.Embed(description=emoji[randomNum])) # 랜덤 이모티콘을 메시지로 출력합니다.






    if message.content.startswith('/주사위'):

        randomNum = random.randrange(1, 7) # 1~6까지 랜덤수
        print(randomNum)
        if randomNum == 1:
            await message.channel.send(message.channel, embed=discord.Embed(description=':game_die: '+ ':one:'))
        if randomNum == 2:
            await message.channel.send(message.channel, embed=discord.Embed(description=':game_die: ' + ':two:'))
        if randomNum ==3:
            await message.channel.send(message.channel, embed=discord.Embed(description=':game_die: ' + ':three:'))
        if randomNum ==4:
            await message.channel.send(message.channel, embed=discord.Embed(description=':game_die: ' + ':four:'))
        if randomNum ==5:
            await message.channel.send(message.channel, embed=discord.Embed(description=':game_die: ' + ':five:'))
        if randomNum ==6:
            await message.channel.send(message.channel, embed=discord.Embed(description=':game_die: ' + ':six: '))

    if message.content.startswith('/타이머'):

        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        for i in range(1, vrsize):  # 띄어쓰기 한 텍스트들 인식함
            Text = Text + " " + learn[i]

        secint = int(Text)
        sec = secint

        for i in range(sec, 0, -1):
            print(i)
            await message.channel.send(message.channel, embed=discord.Embed(description='타이머 작동중 : '+str(i)+'초'))
            time.sleep(1)

        else:
            print("땡")
            await message.channel.send(message.channel, embed=discord.Embed(description='타이머 종료'))
            

    if message.content.startswith('/이미지'):




        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        for i in range(1, vrsize):  # 띄어쓰기 한 텍스트들 인식함
            Text = Text + " " + learn[i]
        print(Text.strip())  # 입력한 명령어

        randomNum = random.randrange(0, 40) # 랜덤 이미지 숫자

        location = Text
        enc_location = urllib.parse.quote(location) # 한글을 url에 사용하게끔 형식을 바꿔줍니다. 그냥 한글로 쓰면 실행이 안됩니다.
        hdr = {'User-Agent': 'Mozilla5.0'}
        # 크롤링 하는데 있어서 가끔씩 안되는 사이트가 있습니다.
        # 그 이유는 사이트가 접속하는 상대를 봇으로 인식하였기 때문인데
        # 이 코드는 자신이 봇이 아닌것을 증명하여 사이트에 접속이 가능해집니다!
        url = 'https:search.naver.comsearch.naver?where=image&sm=tab_jum&query=' + enc_location # 이미지 검색링크+검색할 키워드
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser") # 전체 html 코드를 가져옵니다.
        # print(bsObj)
        imgfind1 = bsObj.find('div', {'class': 'photo_grid _box'}) # bsjObj에서 div class : photo_grid_box 의 코드를 가져옵니다.
        # print(imgfind1)
        imgfind2 = imgfind1.findAll('a', {'class': 'thumb _thumb'}) # imgfind1 에서 모든 a태그 코드를 가져옵니다.
        imgfind3 = imgfind2[randomNum]  # 0이면 1번째사진 1이면 2번째사진 형식으로 하나의 사진 코드만 가져옵니다.
        imgfind4 = imgfind3.find('img') # imgfind3 에서 img코드만 가져옵니다.
        imgsrc = imgfind4.get('data-source') # imgfind4 에서 data-source(사진링크) 의 값만 가져옵니다.
        print(imgsrc)
        embed = discord.Embed(colour=0x5100FF, timestamp=message.created_at)
        embed.add_field(name='검색 : '+Text, value='링크 : '+imgsrc, inline=False)
        embed.set_image(url=imgsrc) # 이미지의 링크를 지정해 이미지를 설정합니다.
        await message.channel.send(message.channel, embed=embed) # 메시지를 보냅니다.

    if message.content.startswith("/계산"):
            global calcResult
            param = message.content.split()
            try:
                if param[1].startswith("더하기"):
                    calcResult = int(param[2])+int(param[3])
                    await message.channel.send("답 : "+str(calcResult))
                if param[1].startswith("빼기"):
                    calcResult = int(param[2])-int(param[3])
                    await message.channel.send("답 : "+str(calcResult))
                if param[1].startswith("곱하기"):
                    calcResult = int(param[2])*int(param[3])
                    await message.channel.send("답 : "+str(calcResult))
                if param[1].startswith("나누기"):
                    calcResult = int(param[2])/int(param[3])
                    await message.channel.send("답 : "+str(calcResult))
            except IndexError:
                await message.channel.send(message.channel, embed=discord.Embed(title="무슨 숫자를 계산할지 알려주세요.", color=discord.Color.blue()))
            except ValueError:
                await message.channel.send(message.channel, embed=discord.Embed(title="숫자로 넣어주세요.", color=discord.Color.blue()))
            except ZeroDivisionError:
                await message.channel.send("You can't divide with 0.")

    if message.content.startswith("!경쟁전1"):#TabErrorTPP 
        baseURL = "https://dak.gg/profile/"
        playerNickname = ''.join((message.content).split(' ')[1:])
        URL = baseURL + quote(playerNickname)
        
        try:
            html = urlopen(URL)
            bs = BeautifulSoup(html, 'html.parser')
            if len(message.content.split(" ")) == 1:
                embed = discord.Embed(title="닉네임이 입력되지 않았습니다", description="", color=0x5CD1E5)
                embed.add_field(name="Player nickname not entered",
                                value="To use command !경쟁전(1 : TPP or 2 : FPP) : !경쟁전 (Nickname)", inline=False)
                embed.set_footer(text='Service provided by Hoplin.',
                                 icon_url='https://avatars2.githubusercontent.com/u/45956041?s=460&u=1caf3b112111cbd9849a2b95a88c3a8f3a15ecfa&v=4')
                await message.channel.send("Error : Incorrect command usage ", embed=embed)
            else:
                accessors = bs.findAll('a', {'href': re.compile('\/statistics\/[A-Za-z]')})

                # Season Information : ['PUBG',(season info),(Server),'overview']
                seasonInfo = []
                for si in bs.findAll('li', {'class': "active"}):
                    seasonInfo.append(si.text.strip())
                serverAccessorAndStatus = []
                # To prevent : Parsing Server Status, Make a result like Server:\nOnline. So I need to delete '\n'to get good result
                for a in accessors:
                    serverAccessorAndStatus.append(re.sub(pattern='[\n]', repl="", string=a.text.strip()))

                # Varaible serverAccessorAndStatus : [(accessors),(ServerStatus),(Don't needed value)]
                
                # Varaibel rankElements : index 0: fpp 1 : tpp
                
                rankElements = bs.findAll('div',{'class' : re.compile('squad ranked [A-Za-z0-9]')})
                
                '''
                -> 클래스 값을 가져와서 판별하는 것도 있지만 이 방법을 사용해 본다.
                -> 만약 기록이 존재 하지 않는 경우 class 가 no_record라는 값을 가진 <div>가 생성된다. 이 태그로 데이터 유무 판별하면된다.
                print(rankElements[1].find('div',{'class' : 'no_record'}))
                '''
                
                if rankElements[0].find('div',{'class' : 'no_record'}) != None: # 인덱스 0 : 경쟁전 fpp -> 정보가 있는지 없는지 유무를 판별한다.
                    embed = discord.Embed(title="기록을 찾을수 없습니다 죄송합니다.", description="Rank TPP 기록을 찾을수 없습니다 죄송합니다..",color=0x5CD1E5)
                    embed.add_field(name="배그 전적 검색 사이트(**출저**)", value=URL, inline=False)
                    embed.set_footer(text='Service provided by Hoplin.',
                                     icon_url='https://avatars2.githubusercontent.com/u/45956041?s=460&u=1caf3b112111cbd9849a2b95a88c3a8f3a15ecfa&v=4')
                    await message.channel.send("PUBG player " + playerNickname + "'s TPP Ranking information",embed=embed) 
                else:
                    #Short of fpp Rank
                    fR = rankElements[0]
                    # Tier Information
    
                    # Get tier medal image
                    tierMedalImage = fR.find('div',{'class' : 'grade-info'}).img['src']
                    # Get tier Information
                    tierInfo = fR.find('div',{'class' : 'grade-info'}).img['alt']
    
                    # Rating Inforamtion
                    # RP Score
                    RPScore = fR.find('div',{'class' : 'rating'}).find('span',{'class' : 'caption'}).text
    
                    #Get top rate statistics
                    
                    #등수
                    topRatioRank  = topRatio = fR.find('p',{'class' : 'desc'}).find('span',{'class' : 'rank'}).text     
                     #상위 %                          
                    topRatio = fR.find('p',{'class' : 'desc'}).find('span',{'class' : 'top'}).text
    
                    # Main : Stats all in here.
    
                    mainStatsLayout = fR.find('div',{'class' : 'stats'})
    
                    #Stats Data Saved As List
    
                    statsList = mainStatsLayout.findAll('p',{'class' : 'value'})# [KDA,승률,Top10,평균딜량, 게임수, 평균등수]
                    statsRatingList = mainStatsLayout.findAll('span',{'class' : 'top'})#[KDA, 승률,Top10 평균딜량, 게임수]
            
                    for r in range(0,len(statsList)):
                    # \n으로 큰 여백이 있어 split 처리
                        statsList[r] = statsList[r].text.strip().split('\n')[0]
                        statsRatingList[r] = statsRatingList[r].text
                    # 평균등수는 stats Rating을 표시하지 않는다.
                    statsRatingList = statsRatingList[0:5]
                                               
                    
                    embed = discord.Embed(title="Player Unkonw Battle Ground 배그 전적 검색 사이트(**출저**)", description="",color=0x5CD1E5)
                    embed.add_field(name="배그 전적 검색 사이트(**출저**)", value=URL, inline=False)
                    embed.add_field(name="Real Time Accessors and Server Status",
                                    value="Accessors : " + serverAccessorAndStatus[0] + " | " "Server Status : " +
                                          serverAccessorAndStatus[1].split(':')[-1], inline=False)  
                    embed.add_field(name="Player located server", value=seasonInfo[2] + " Server", inline=False)
                    embed.add_field(name = "Tier / Top Rate / Average Rank",
                                   value = tierInfo + " (" + RPScore + ") / "+topRatio + " / " + topRatioRank,inline=False)
                    embed.add_field(name="K/D", value=statsList[0] + "/" + statsRatingList[0], inline=True)
                    embed.add_field(name="승률", value=statsList[1] + "/" + statsRatingList[1], inline=True)
                    embed.add_field(name="Top 10 비율", value=statsList[2] + "/" + statsRatingList[2], inline=True)
                    embed.add_field(name="평균딜량", value=statsList[3] + "/" + statsRatingList[3], inline=True)
                    embed.add_field(name="게임수", value=statsList[4] + "판/" + statsRatingList[4], inline=True)
                    embed.add_field(name="평균등수", value=statsList[5],inline=True)
                    embed.set_thumbnail(url=f'https:{tierMedalImage}')
                    embed.set_footer(text='Service provided by Hoplin.',
                                     icon_url='https://avatars2.githubusercontent.com/u/45956041?s=460&u=1caf3b112111cbd9849a2b95a88c3a8f3a15ecfa&v=4')
                    await message.channel.send("PUBG player " + playerNickname + "'s TPP Ranking information", embed=embed)
                    
            
        except HTTPError as e:
            embed = discord.Embed(title="Not existing plyer", description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)
            print(e)
        except AttributeError as e:
            embed = discord.Embed(title="Not existing plyer",
                                  description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",
                                  color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)
            print(e)
    
    if message.content.startswith("!경쟁전2"):#FPP 
        baseURL = "https://dak.gg/profile/"
        playerNickname = ''.join((message.content).split(' ')[1:])
        URL = baseURL + quote(playerNickname)
        
        try:
            html = urlopen(URL)
            bs = BeautifulSoup(html, 'html.parser')
            if len(message.content.split(" ")) == 1:
                embed = discord.Embed(title="닉네임이 입력되지 않았습니다", description="", color=0x5CD1E5)
                embed.add_field(name="Player nickname not entered",
                                value="To use command !경쟁전(1 : TPP or 2 : FPP) : !경쟁전 (Nickname)", inline=False)
                embed.set_footer(text='Service provided by Hoplin.',
                                 icon_url='https://avatars2.githubusercontent.com/u/45956041?s=460&u=1caf3b112111cbd9849a2b95a88c3a8f3a15ecfa&v=4')
                await message.channel.send("Error : Incorrect command usage ", embed=embed)
            else:
                accessors = bs.findAll('a', {'href': re.compile('\/statistics\/[A-Za-z]')})

                # Season Information : ['PUBG',(season info),(Server),'overview']
                seasonInfo = []
                for si in bs.findAll('li', {'class': "active"}):
                    seasonInfo.append(si.text.strip())
                serverAccessorAndStatus = []
                # To prevent : Parsing Server Status, Make a result like Server:\nOnline. So I need to delete '\n'to get good result
                for a in accessors:
                    serverAccessorAndStatus.append(re.sub(pattern='[\n]', repl="", string=a.text.strip()))

                # Varaible serverAccessorAndStatus : [(accessors),(ServerStatus),(Don't needed value)]
                
                # index 0: fpp 1 : tpp
                
                rankElements = bs.findAll('div',{'class' : re.compile('squad ranked [A-Za-z0-9]')})
                
                '''
                -> 클래스 값을 가져와서 판별하는 것도 있지만 이 방법을 사용해 본다.
                -> 만약 기록이 존재 하지 않는 경우 class 가 no_record라는 값을 가진 <div>가 생성된다. 이 태그로 데이터 유무 판별하면된다.
                print(rankElements[1].find('div',{'class' : 'no_record'}))
                '''
                
                if rankElements[1].find('div',{'class' : 'no_record'}) != None: # 인덱스 0 : 경쟁전 fpp -> 정보가 있는지 없는지 유무를 판별한다a.
                    embed = discord.Embed(title="기록을 찾을수 없습니다 죄송합니다.", description="솔로 기록을 찾을수 없습니다 죄송합니다..",
                                          color=0x5CD1E5)
                    embed.add_field(name="배그 전적 검색 사이트(**출저**)", value=URL, inline=False)
                    embed.set_footer(text='Service provided by Hoplin.',
                                     icon_url='https://avatars2.githubusercontent.com/u/45956041?s=460&u=1caf3b112111cbd9849a2b95a88c3a8f3a15ecfa&v=4')
                    await message.channel.send("PUBG player " + playerNickname + "'s FPP Ranking information",embed=embed) 
                else:
                    #Short of fpp Rank
                    fR = rankElements[1]
                    # Tier Information
    
                    # Get tier medal image
                    tierMedalImage = fR.find('div',{'class' : 'grade-info'}).img['src']
                    # Get tier Information
                    tierInfo = fR.find('div',{'class' : 'grade-info'}).img['alt']
    
                    # Rating Inforamtion
                    # RP Score
                    RPScore = fR.find('div',{'class' : 'rating'}).find('span',{'class' : 'caption'}).text
    
                    #Get top rate statistics
                    
                    #등수
                    topRatioRank  = topRatio = fR.find('p',{'class' : 'desc'}).find('span',{'class' : 'rank'}).text     
                     #상위 %                          
                    topRatio = fR.find('p',{'class' : 'desc'}).find('span',{'class' : 'top'}).text
    
                    # Main : Stats all in here.
    
                    mainStatsLayout = fR.find('div',{'class' : 'stats'})
    
                    #Stats Data Saved As List
    
                    statsList = mainStatsLayout.findAll('p',{'class' : 'value'})# [KDA,승률,Top10,평균딜량, 게임수, 평균등수]
                    statsRatingList = mainStatsLayout.findAll('span',{'class' : 'top'})#[KDA, 승률,Top10 평균딜량, 게임수]
            
                    for r in range(0,len(statsList)):
                    # \n으로 큰 여백이 있어 split 처리
                        statsList[r] = statsList[r].text.strip().split('\n')[0]
                        statsRatingList[r] = statsRatingList[r].text
                    # 평균등수는 stats Rating을 표시하지 않는다.
                    statsRatingList = statsRatingList[0:5]
                                               
                    
                    embed = discord.Embed(title="Player Unkonw Battle Ground 배그 전적 검색 사이트(**출저**)", description="",color=0x5CD1E5)
                    embed.add_field(name="배그 전적 검색 사이트(**출저**)", value=URL, inline=False)
                    embed.add_field(name="Real Time Accessors and Server Status",
                                    value="Accessors : " + serverAccessorAndStatus[0] + " | " "Server Status : " +
                                          serverAccessorAndStatus[1].split(':')[-1], inline=False)  
                    embed.add_field(name="Player located server", value=seasonInfo[2] + " Server", inline=False)
                    embed.add_field(name = "Tier / Top Rate / Average Rank",
                                   value = tierInfo + " (" + RPScore + ") / "+topRatio + " / " + topRatioRank,inline=False)
                    embed.add_field(name="K/D", value=statsList[0] + "/" + statsRatingList[0], inline=True)
                    embed.add_field(name="승률", value=statsList[1] + "/" + statsRatingList[1], inline=True)
                    embed.add_field(name="Top 10 비율", value=statsList[2] + "/" + statsRatingList[2], inline=True)
                    embed.add_field(name="평균딜량", value=statsList[3] + "/" + statsRatingList[3], inline=True)
                    embed.add_field(name="게임수", value=statsList[4] + "판/" + statsRatingList[4], inline=True)
                    embed.add_field(name="평균등수", value=statsList[5],inline=True)
                    embed.set_thumbnail(url=f'https:{tierMedalImage}')
                    embed.set_footer(text='Service provided by Hoplin.',
                                     icon_url='https://avatars2.githubusercontent.com/u/45956041?s=460&u=1caf3b112111cbd9849a2b95a88c3a8f3a15ecfa&v=4')
                    await message.channel.send("PUBG player " + playerNickname + "'s FPP Ranking information", embed=embed)
                    
            
        except HTTPError as e:
            embed = discord.Embed(title="Not existing plyer", description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)
        except AttributeError as e:
            embed = discord.Embed(title="Not existing plyer",
                                  description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",
                                  color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)

    if message.content.startswith("!배그솔로1"):
        baseURL = "https://dak.gg/profile/"
        playerNickname = ''.join((message.content).split(' ')[1:])
        URL = baseURL + quote(playerNickname)
        try:
            html = urlopen(URL)
            bs = BeautifulSoup(html, 'html.parser')
            if len(message.content.split(" ")) == 1:
                embed = discord.Embed(title="닉네임이 입력되지 않았습니다", description="", color=0x5CD1E5)
                embed.add_field(name="Player nickname not entered",
                                value="To use command !배그솔로 : !배그솔로 (Nickname)", inline=False)
                embed.set_footer(text='Service provided by Hoplin.',
                                 icon_url='https://avatars2.githubusercontent.com/u/45956041?s=460&u=1caf3b112111cbd9849a2b95a88c3a8f3a15ecfa&v=4')
                await message.channel.send("Error : Incorrect command usage ", embed=embed)

            else:
                accessors = bs.findAll('a', {'href': re.compile('\/statistics\/[A-Za-z]')})

                # Season Information : ['PUBG',(season info),(Server),'overview']
                seasonInfo = []
                for si in bs.findAll('li', {'class': "active"}):
                    seasonInfo.append(si.text.strip())
                serverAccessorAndStatus = []
                # To prevent : Parsing Server Status, Make a result like Server:\nOnline. So I need to delete '\n'to get good result
                for a in accessors:
                    serverAccessorAndStatus.append(re.sub(pattern='[\n]', repl="", string=a.text.strip()))

                # Varaible serverAccessorAndStatus : [(accessors),(ServerStatus),(Don't needed value)]

                soloQueInfo = bs.find('section', {'class': "solo modeItem"}).find('div', {'class': "mode-section tpp"})
                if soloQueInfo == None:
                    embed = discord.Embed(title="기록을 찾을수 없습니다 죄송합니다.", description="솔로 기록을 찾을수 없습니다 죄송합니다..",
                                          color=0x5CD1E5)
                    embed.add_field(name="배그 전적 검색 사이트(**출저**)", value=URL, inline=False)
                    await message.channel.send("PUBG player " + playerNickname + "'s TPP solo que information", embed=embed)
                else:
                    # print(soloQueInfo)
                    # Get total playtime
                    soloQueTotalPlayTime = soloQueInfo.find('span', {'class': "time_played"}).text.strip()
                    # Get Win/Top10/Lose : [win,top10,lose]
                    soloQueGameWL = soloQueInfo.find('em').text.strip().split(' ')
                    # RankPoint
                    rankPoint = soloQueInfo.find('span', {'class': 'value'}).text
                    # Tier image url, tier
                    tierInfos = soloQueInfo.find('img', {
                        'src': re.compile('\/\/static\.dak\.gg\/images\/icons\/tier\/[A-Za-z0-9_.]')})
                    tierImage = "https:" + tierInfos['src']
                    print(tierImage)
                    tier = tierInfos['alt']

                    # Comprehensive info
                    comInfo = []
                    # [K/D,승률,Top10,평균딜량,게임수, 최다킬수,헤드샷,저격거리,생존,평균순위]
                    for ci in soloQueInfo.findAll('p', {'class': 'value'}):
                        comInfo.append(''.join(ci.text.split()))

                    embed = discord.Embed(title="Player Unkonw Battle Ground 배그 전적 검색 사이트(**출저**)", description="",
                                          color=0x5CD1E5)
                    embed.add_field(name="배그 전적 검색 사이트(**출저**)", value=URL, inline=False)
                    embed.add_field(name="Real Time Accessors and Server Status",
                                    value="Accessors : " + serverAccessorAndStatus[0] + " | " "Server Status : " +
                                          serverAccessorAndStatus[1].split(':')[-1], inline=False)
                    embed.add_field(name="Player located server", value=seasonInfo[2] + " Server / Total playtime : " +soloQueTotalPlayTime, inline=False)
                    embed.add_field(name="Tier",
                                    value=tier + " ("+rankPoint+"p)" , inline=False)
                    embed.add_field(name="K/D", value=comInfo[0], inline=True)
                    embed.add_field(name="승률", value=comInfo[1], inline=True)
                    embed.add_field(name="Top 10 비율", value=comInfo[2], inline=True)
                    embed.add_field(name="평균딜량", value=comInfo[3], inline=True)
                    embed.add_field(name="게임수", value=comInfo[4] + "판", inline=True)
                    embed.add_field(name="최다킬수", value=comInfo[5] + "킬", inline=True)
                    embed.add_field(name="헤드샷 비율", value=comInfo[6], inline=True)
                    embed.add_field(name="저격거리", value=comInfo[7], inline=True)
                    embed.add_field(name="평균생존시간", value=comInfo[8], inline=True)
                    embed.set_footer(text='Service provided by Hoplin.',
                                     icon_url='https://avatars2.githubusercontent.com/u/45956041?s=460&u=1caf3b112111cbd9849a2b95a88c3a8f3a15ecfa&v=4')
                    await message.channel.send("PUBG player " + playerNickname + "'s TPP solo que information", embed=embed)
        except HTTPError as e:
            embed = discord.Embed(title="Not existing plyer", description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)
        except AttributeError as e:
            embed = discord.Embed(title="Not existing plyer",
                                  description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",
                                  color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)

    if message.content.startswith("!배그듀오1"):
        baseURL = "https://dak.gg/profile/"
        playerNickname = ''.join((message.content).split(' ')[1:])
        URL = baseURL + quote(playerNickname)
        try:
            html = urlopen(URL)
            bs = BeautifulSoup(html, 'html.parser')
            if len(message.content.split(" ")) == 1:
                embed = discord.Embed(title="닉네임이 입력되지 않았습니다", description="", color=0x5CD1E5)
                embed.add_field(name="Player nickname not entered",
                                value="To use command !배그스쿼드 : !배그스쿼드 (Nickname)", inline=False)
                embed.set_footer(text='Service provided by Hoplin.',
                                 icon_url='https://avatars2.githubusercontent.com/u/45956041?s=460&u=1caf3b112111cbd9849a2b95a88c3a8f3a15ecfa&v=4')
                await message.channel.send("Error : Incorrect command usage ", embed=embed)

            else:
                accessors = bs.findAll('a', {'href': re.compile('\/statistics\/[A-Za-z]')})

                # Season Information : ['PUBG',(season info),(Server),'overview']
                seasonInfo = []
                for si in bs.findAll('li', {'class': "active"}):
                    seasonInfo.append(si.text.strip())
                serverAccessorAndStatus = []
                # To prevent : Parsing Server Status, Make a result like Server:\nOnline. So I need to delete '\n'to get good result
                for a in accessors:
                    serverAccessorAndStatus.append(re.sub(pattern='[\n]', repl="", string=a.text.strip()))

                # Varaible serverAccessorAndStatus : [(accessors),(ServerStatus),(Don't needed value)]

                duoQueInfo = bs.find('section',{'class' : "duo modeItem"}).find('div',{'class' : "mode-section tpp"})
                if duoQueInfo == None:
                    embed = discord.Embed(title="기록을 찾을수 없습니다 죄송합니다.", description="듀오 기록을 찾을수 없습니다 죄송합니다..",
                                          color=0x5CD1E5)
                    embed.add_field(name="배그 전적 검색 사이트(**출저**)", value=URL, inline=False)
                    await message.channel.send("PUBG player " + playerNickname + "'s TPP duo que information", embed=embed)
                else:
                    # print(duoQueInfo)
                    # Get total playtime
                    duoQueTotalPlayTime = duoQueInfo.find('span', {'class': "time_played"}).text.strip()
                    # Get Win/Top10/Lose : [win,top10,lose]
                    duoQueGameWL = duoQueInfo.find('em').text.strip().split(' ')
                    # RankPoint
                    rankPoint = duoQueInfo.find('span', {'class': 'value'}).text
                    # Tier image url, tier
                    tierInfos = duoQueInfo.find('img', {
                        'src': re.compile('\/\/static\.dak\.gg\/images\/icons\/tier\/[A-Za-z0-9_.]')})
                    tierImage = "https:" + tierInfos['src']
                    tier = tierInfos['alt']

                    # Comprehensive info
                    comInfo = []
                    # [K/D,승률,Top10,평균딜량,게임수, 최다킬수,헤드샷,저격거리,생존,평균순위]
                    for ci in duoQueInfo.findAll('p', {'class': 'value'}):
                        comInfo.append(''.join(ci.text.split()))

                    embed = discord.Embed(title="Player Unkonw Battle Ground 배그 전적 검색 사이트(**출저**)", description="",
                                          color=0x5CD1E5)
                    embed.add_field(name="배그 전적 검색 사이트(**출저**)", value=URL, inline=False)
                    embed.add_field(name="Real Time Accessors and Server Status",
                                    value="Accessors : " + serverAccessorAndStatus[0] + " | " "Server Status : " +
                                          serverAccessorAndStatus[1].split(':')[-1], inline=False)
                    embed.add_field(name="Player located server and total playtime", value=seasonInfo[2] + " Server / Total playtime : " +duoQueTotalPlayTime, inline=False)
                    embed.add_field(name="Tier(Rank Point)",
                                    value=tier + " ("+rankPoint+"p)", inline=False)
                    embed.add_field(name="K/D", value=comInfo[0], inline=True)
                    embed.add_field(name="승률", value=comInfo[1], inline=True)
                    embed.add_field(name="Top 10 비율", value=comInfo[2], inline=True)
                    embed.add_field(name="평균딜량", value=comInfo[3], inline=True)
                    embed.add_field(name="게임수", value=comInfo[4] + "판", inline=True)
                    embed.add_field(name="최다킬수", value=comInfo[5] + "킬", inline=True)
                    embed.add_field(name="헤드샷 비율", value=comInfo[6], inline=True)
                    embed.add_field(name="저격거리", value=comInfo[7], inline=True)
                    embed.add_field(name="평균생존시간", value=comInfo[8], inline=True)
                    embed.set_footer(text='Service provided by Hoplin.',
                                     icon_url='https://avatars2.githubusercontent.com/u/45956041?s=460&u=1caf3b112111cbd9849a2b95a88c3a8f3a15ecfa&v=4')
                    await message.channel.send("PUBG player " + playerNickname + "'s TPP duo que information", embed=embed)
        except HTTPError as e:
            embed = discord.Embed(title="Not existing plyer",
                                  description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",
                                  color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)
        except AttributeError as e:
            embed = discord.Embed(title="Not existing plyer",
                                  description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",
                                  color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)

    if message.content.startswith("!배그스쿼드1"):
        baseURL = "https://dak.gg/profile/"
        playerNickname = ''.join((message.content).split(' ')[1:])
        URL = baseURL + quote(playerNickname)
        try:
            html = urlopen(URL)
            bs = BeautifulSoup(html, 'html.parser')
            if len(message.content.split(" ")) == 1:
                embed = discord.Embed(title="닉네임이 입력되지 않았습니다", description="", color=0x5CD1E5)
                embed.add_field(name="Player nickname not entered",
                                value="To use command !배그솔로 : !배그솔로 (Nickname)", inline=False)
                embed.set_footer(text='Service provided by Hoplin.',
                                 icon_url='https://avatars2.githubusercontent.com/u/45956041?s=460&u=1caf3b112111cbd9849a2b95a88c3a8f3a15ecfa&v=4')
                await message.channel.send("Error : Incorrect command usage ", embed=embed)

            else:
                accessors = bs.findAll('a', {'href': re.compile('\/statistics\/[A-Za-z]')})

                # Season Information : ['PUBG',(season info),(Server),'overview']
                seasonInfo = []
                for si in bs.findAll('li', {'class': "active"}):
                    seasonInfo.append(si.text.strip())
                serverAccessorAndStatus = []
                # To prevent : Parsing Server Status, Make a result like Server:\nOnline. So I need to delete '\n'to get good result
                for a in accessors:
                    serverAccessorAndStatus.append(re.sub(pattern='[\n]', repl="", string=a.text.strip()))

                # Varaible serverAccessorAndStatus : [(accessors),(ServerStatus),(Don't needed value)]

                squadQueInfo = bs.find('section',{'class' : "squad modeItem"}).find('div',{'class' : "mode-section tpp"})
                if squadQueInfo == None:
                    embed = discord.Embed(title="기록을 찾을수 없습니다 죄송합니다.", description="스쿼드 기록을 찾을수 없습니다 죄송합니다..",
                                          color=0x5CD1E5)
                    embed.add_field(name="배그 전적 검색 사이트(**출저**)", value=URL, inline=False)
                    await message.channel.send("PUBG player " + playerNickname + "'s TPP squad que information", embed=embed)
                else:
                    # print(duoQueInfo)
                    # Get total playtime
                    squadQueTotalPlayTime = squadQueInfo.find('span', {'class': "time_played"}).text.strip()
                    # Get Win/Top10/Lose : [win,top10,lose]
                    squadQueGameWL = squadQueInfo.find('em').text.strip().split(' ')
                    # RankPoint
                    rankPoint = squadQueInfo.find('span', {'class': 'value'}).text
                    # Tier image url, tier
                    tierInfos = squadQueInfo.find('img', {
                        'src': re.compile('\/\/static\.dak\.gg\/images\/icons\/tier\/[A-Za-z0-9_.]')})
                    tierImage = "https:" + tierInfos['src']
                    tier = tierInfos['alt']

                    # Comprehensive info
                    comInfo = []
                    # [K/D,승률,Top10,평균딜량,게임수, 최다킬수,헤드샷,저격거리,생존,평균순위]
                    for ci in squadQueInfo.findAll('p', {'class': 'value'}):
                        comInfo.append(''.join(ci.text.split()))
                    embed = discord.Embed(title="Player Unkonw Battle Ground 배그 전적 검색 사이트(**출저**)", description="",
                                          color=0x5CD1E5)
                    embed.add_field(name="배그 전적 검색 사이트(**출저**)", value=URL, inline=False)
                    embed.add_field(name="Real Time Accessors and Server Status",
                                    value="Accessors : " + serverAccessorAndStatus[0] + " | " "Server Status : " +
                                          serverAccessorAndStatus[1].split(':')[-1], inline=False)
                    embed.add_field(name="Player located server", value=seasonInfo[2] + " Server / Total playtime : " +squadQueTotalPlayTime, inline=False)
                    embed.add_field(name="Tier(Rank Point)",
                                    value=tier + " (" + rankPoint + "p)", inline=False)
                    embed.add_field(name="K/D", value=comInfo[0] , inline=True)
                    embed.add_field(name="승률", value=comInfo[1] , inline=True)
                    embed.add_field(name="Top 10 비율", value=comInfo[2] , inline=True)
                    embed.add_field(name="평균딜량", value=comInfo[3] , inline=True)
                    embed.add_field(name="게임수", value=comInfo[4] + "판", inline=True)
                    embed.add_field(name="최다킬수", value=comInfo[5] + "킬", inline=True)
                    embed.add_field(name="헤드샷 비율", value=comInfo[6], inline=True)
                    embed.add_field(name="저격거리", value=comInfo[7], inline=True)
                    embed.add_field(name="평균생존시간", value=comInfo[8], inline=True)
                    embed.set_footer(text='Service provided by Hoplin.',
                                     icon_url='https://avatars2.githubusercontent.com/u/45956041?s=460&u=1caf3b112111cbd9849a2b95a88c3a8f3a15ecfa&v=4')
                    await message.channel.send("PUBG player " + playerNickname + "'s TPP squad que information", embed=embed)
        except HTTPError as e:
            embed = discord.Embed(title="Not existing plyer",
                                  description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",
                                  color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)
        except AttributeError as e:
            embed = discord.Embed(title="Not existing plyer",
                                  description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",
                                  color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)

    if message.content.startswith("!배그솔로2"):
        baseURL = "https://dak.gg/profile/"
        playerNickname = ''.join((message.content).split(' ')[1:])
        URL = baseURL + quote(playerNickname)
        try:
            html = urlopen(URL)
            bs = BeautifulSoup(html, 'html.parser')
            if len(message.content.split(" ")) == 1:
                embed = discord.Embed(title="닉네임이 입력되지 않았습니다", description="", color=0x5CD1E5)
                embed.add_field(name="Player nickname not entered",
                                value="To use command !배그솔로 : !배그솔로 (Nickname)", inline=False)
                embed.set_footer(text='Service provided by Hoplin.',
                                 icon_url='https://avatars2.githubusercontent.com/u/45956041?s=460&u=1caf3b112111cbd9849a2b95a88c3a8f3a15ecfa&v=4')
                await message.channel.send("Error : Incorrect command usage ", embed=embed)

            else:
                accessors = bs.findAll('a', {'href': re.compile('\/statistics\/[A-Za-z]')})

                # Season Information : ['PUBG',(season info),(Server),'overview']
                seasonInfo = []
                for si in bs.findAll('li', {'class': "active"}):
                    seasonInfo.append(si.text.strip())
                serverAccessorAndStatus = []
                # To prevent : Parsing Server Status, Make a result like Server:\nOnline. So I need to delete '\n'to get good result
                for a in accessors:
                    serverAccessorAndStatus.append(re.sub(pattern='[\n]', repl="", string=a.text.strip()))

                # Varaible serverAccessorAndStatus : [(accessors),(ServerStatus),(Don't needed value)]

                soloQueInfo = bs.find('section', {'class': "solo modeItem"}).find('div', {'class': "mode-section fpp"})
                if soloQueInfo == None:
                    embed = discord.Embed(title="기록을 찾을수 없습니다 죄송합니다.", description="솔로 기록을 찾을수 없습니다 죄송합니다..",
                                          color=0x5CD1E5)
                    embed.add_field(name="배그 전적 검색 사이트(**출저**)", value=URL, inline=False)
                    await message.channel.send("PUBG player " + playerNickname + "'s FPP solo que information",
                                               embed=embed)
                else:
                    # print(soloQueInfo)
                    # Get total playtime
                    soloQueTotalPlayTime = soloQueInfo.find('span', {'class': "time_played"}).text.strip()
                    # Get Win/Top10/Lose : [win,top10,lose]
                    soloQueGameWL = soloQueInfo.find('em').text.strip().split(' ')
                    # RankPoint
                    rankPoint = soloQueInfo.find('span', {'class': 'value'}).text
                    # Tier image url, tier
                    tierInfos = soloQueInfo.find('img', {
                        'src': re.compile('\/\/static\.dak\.gg\/images\/icons\/tier\/[A-Za-z0-9_.]')})
                    tierImage = "https:" + tierInfos['src']
                    print(tierImage)
                    tier = tierInfos['alt']

                    # Comprehensive info
                    comInfo = []
                    # [K/D,승률,Top10,평균딜량,게임수, 최다킬수,헤드샷,저격거리,생존,평균순위]
                    for ci in soloQueInfo.findAll('p', {'class': 'value'}):
                        comInfo.append(''.join(ci.text.split()))
                    embed = discord.Embed(title="Player Unkonw Battle Ground 배그 전적 검색 사이트(**출저**)", description="",
                                          color=0x5CD1E5)
                    embed.add_field(name="배그 전적 검색 사이트(**출저**)", value=URL, inline=False)
                    embed.add_field(name="Real Time Accessors and Server Status",
                                    value="Accessors : " + serverAccessorAndStatus[0] + " | " "Server Status : " +
                                          serverAccessorAndStatus[1].split(':')[-1], inline=False)
                    embed.add_field(name="Player located server",
                                    value=seasonInfo[2] + " Server / Total playtime : " + soloQueTotalPlayTime,
                                    inline=False)
                    embed.add_field(name="Tier(Rank Point)",
                                    value=tier + " (" + rankPoint + "p)", inline=False)
                    embed.add_field(name="K/D", value=comInfo[0], inline=True)
                    embed.add_field(name="승률", value=comInfo[1], inline=True)
                    embed.add_field(name="Top 10 비율", value=comInfo[2], inline=True)
                    embed.add_field(name="평균딜량", value=comInfo[3], inline=True)
                    embed.add_field(name="게임수", value=comInfo[4] + "판" , inline=True)
                    embed.add_field(name="최다킬수", value=comInfo[5] + "킬" , inline=True)
                    embed.add_field(name="헤드샷 비율", value=comInfo[6] , inline=True)
                    embed.add_field(name="저격거리", value=comInfo[7], inline=True)
                    embed.add_field(name="평균생존시간", value=comInfo[8] , inline=True)
                    embed.set_footer(text='Service provided by Hoplin.',
                                     icon_url='https://avatars2.githubusercontent.com/u/45956041?s=460&u=1caf3b112111cbd9849a2b95a88c3a8f3a15ecfa&v=4')
                    await message.channel.send("PUBG player " + playerNickname + "'s FPP solo que information",
                                               embed=embed)
        except HTTPError as e:
            embed = discord.Embed(title="Not existing plyer",
                                  description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",
                                  color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)
        except AttributeError as e:
            embed = discord.Embed(title="Not existing plyer",
                                  description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",
                                  color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)

    if message.content.startswith("!배그듀오2"):
        baseURL = "https://dak.gg/profile/"
        playerNickname = ''.join((message.content).split(' ')[1:])
        URL = baseURL + quote(playerNickname)
        try:
            html = urlopen(URL)
            bs = BeautifulSoup(html, 'html.parser')
            if len(message.content.split(" ")) == 1:
                embed = discord.Embed(title="닉네임이 입력되지 않았습니다", description="", color=0x5CD1E5)
                embed.add_field(name="Player nickname not entered",
                                value="To use command !배그스쿼드 : !배그스쿼드 (Nickname)", inline=False)
                embed.set_footer(text='Service provided by Hoplin.',
                                 icon_url='https://avatars2.githubusercontent.com/u/45956041?s=460&u=1caf3b112111cbd9849a2b95a88c3a8f3a15ecfa&v=4')
                await message.channel.send("Error : Incorrect command usage ", embed=embed)

            else:
                accessors = bs.findAll('a', {'href': re.compile('\/statistics\/[A-Za-z]')})

                # Season Information : ['PUBG',(season info),(Server),'overview']
                seasonInfo = []
                for si in bs.findAll('li', {'class': "active"}):
                    seasonInfo.append(si.text.strip())
                serverAccessorAndStatus = []
                # To prevent : Parsing Server Status, Make a result like Server:\nOnline. So I need to delete '\n'to get good result
                for a in accessors:
                    serverAccessorAndStatus.append(re.sub(pattern='[\n]', repl="", string=a.text.strip()))

                # Varaible serverAccessorAndStatus : [(accessors),(ServerStatus),(Don't needed value)]

                duoQueInfo = bs.find('section', {'class': "duo modeItem"}).find('div', {'class': "mode-section fpp"})
                if duoQueInfo == None:
                    embed = discord.Embed(title="기록을 찾을수 없습니다 죄송합니다.", description="듀오 기록을 찾을수 없습니다 죄송합니다..",
                                          color=0x5CD1E5)
                    embed.add_field(name="배그 전적 검색 사이트(**출저**)", value=URL, inline=False)
                    await message.channel.send("PUBG player " + playerNickname + "'s FPP duo que information",
                                               embed=embed)
                else:
                    # print(duoQueInfo)
                    # Get total playtime
                    duoQueTotalPlayTime = duoQueInfo.find('span', {'class': "time_played"}).text.strip()
                    # Get Win/Top10/Lose : [win,top10,lose]
                    duoQueGameWL = duoQueInfo.find('em').text.strip().split(' ')
                    # RankPoint
                    rankPoint = duoQueInfo.find('span', {'class': 'value'}).text
                    # Tier image url, tier
                    tierInfos = duoQueInfo.find('img', {
                        'src': re.compile('\/\/static\.dak\.gg\/images\/icons\/tier\/[A-Za-z0-9_.]')})
                    tierImage = "https:" + tierInfos['src']
                    tier = tierInfos['alt']

                    # Comprehensive info
                    comInfo = []
                    # [K/D,승률,Top10,평균딜량,게임수, 최다킬수,헤드샷,저격거리,생존,평균순위]
                    for ci in duoQueInfo.findAll('p', {'class': 'value'}):
                        comInfo.append(''.join(ci.text.split()))
                    embed = discord.Embed(title="Player Unkonw Battle Ground 배그 전적 검색 사이트(**출저**)", description="",
                                          color=0x5CD1E5)
                    embed.add_field(name="배그 전적 검색 사이트(**출저**)", value=URL, inline=False)
                    embed.add_field(name="Real Time Accessors and Server Status",
                                    value="Accessors : " + serverAccessorAndStatus[0] + " | " "Server Status : " +
                                          serverAccessorAndStatus[1].split(':')[-1], inline=False)
                    embed.add_field(name="Player located server and total playtime",
                                    value=seasonInfo[2] + " Server / Total playtime : " + duoQueTotalPlayTime,
                                    inline=False)
                    embed.add_field(name="Tier(Rank Point)",
                                    value=tier + " (" + rankPoint + "p)", inline=False)
                    embed.add_field(name="K/D", value=comInfo[0] , inline=True)
                    embed.add_field(name="승률", value=comInfo[1], inline=True)
                    embed.add_field(name="Top 10 비율", value=comInfo[2], inline=True)
                    embed.add_field(name="평균딜량", value=comInfo[3], inline=True)
                    embed.add_field(name="게임수", value=comInfo[4] + "판", inline=True)
                    embed.add_field(name="최다킬수", value=comInfo[5] + "킬", inline=True)
                    embed.add_field(name="헤드샷 비율", value=comInfo[6] , inline=True)
                    embed.add_field(name="저격거리", value=comInfo[7] , inline=True)
                    embed.add_field(name="평균생존시간", value=comInfo[8] , inline=True)
                    embed.set_footer(text='Service provided by Hoplin.',
                                     icon_url='https://avatars2.githubusercontent.com/u/45956041?s=460&u=1caf3b112111cbd9849a2b95a88c3a8f3a15ecfa&v=4')
                    await message.channel.send("PUBG player " + playerNickname + "'s FPP duo que information",
                                               embed=embed)
        except HTTPError as e:
            embed = discord.Embed(title="Not existing plyer",
                                  description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",
                                  color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)
        except AttributeError as e:
            embed = discord.Embed(title="Not existing plyer",
                                  description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",
                                  color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)

    if message.content.startswith("!배그스쿼드2"):
        baseURL = "https://dak.gg/profile/"
        playerNickname = ''.join((message.content).split(' ')[1:])
        URL = baseURL + quote(playerNickname)
        try:
            html = urlopen(URL)
            bs = BeautifulSoup(html, 'html.parser')
            if len(message.content.split(" ")) == 1:
                embed = discord.Embed(title="닉네임이 입력되지 않았습니다", description="", color=0x5CD1E5)
                embed.add_field(name="Player nickname not entered",
                                value="To use command !배그솔로 : !배그솔로 (Nickname)", inline=False)
                embed.set_footer(text='Service provided by Hoplin.',
                                 icon_url='https://avatars2.githubusercontent.com/u/45956041?s=460&u=1caf3b112111cbd9849a2b95a88c3a8f3a15ecfa&v=4')
                await message.channel.send("Error : Incorrect command usage ", embed=embed)

            else:
                accessors = bs.findAll('a', {'href': re.compile('\/statistics\/[A-Za-z]')})

                # Season Information : ['PUBG',(season info),(Server),'overview']
                seasonInfo = []
                for si in bs.findAll('li', {'class': "active"}):
                    seasonInfo.append(si.text.strip())
                serverAccessorAndStatus = []
                # To prevent : Parsing Server Status, Make a result like Server:\nOnline. So I need to delete '\n'to get good result
                for a in accessors:
                    serverAccessorAndStatus.append(re.sub(pattern='[\n]', repl="", string=a.text.strip()))

                # Varaible serverAccessorAndStatus : [(accessors),(ServerStatus),(Don't needed value)]

                squadQueInfo = bs.find('section', {'class': "squad modeItem"}).find('div',
                                                                                    {'class': "mode-section fpp"})
                if squadQueInfo == None:
                    embed = discord.Embed(title="기록을 찾을수 없습니다 죄송합니다.", description="스쿼드 기록을 찾을수 없습니다 죄송합니다..",
                                          color=0x5CD1E5)
                    embed.add_field(name="배그 전적 검색 사이트(**출저**)", value=URL, inline=False)
                    await message.channel.send("PUBG player " + playerNickname + "'s FPP squad que information",
                                               embed=embed)
                else:
                    # print(duoQueInfo)
                    # Get total playtime
                    squadQueTotalPlayTime = squadQueInfo.find('span', {'class': "time_played"}).text.strip()
                    # Get Win/Top10/Lose : [win,top10,lose]
                    squadQueGameWL = squadQueInfo.find('em').text.strip().split(' ')
                    # RankPoint
                    rankPoint = squadQueInfo.find('span', {'class': 'value'}).text
                    # Tier image url, tier
                    tierInfos = squadQueInfo.find('img', {
                        'src': re.compile('\/\/static\.dak\.gg\/images\/icons\/tier\/[A-Za-z0-9_.]')})
                    tierImage = "https:" + tierInfos['src']
                    tier = tierInfos['alt']

                    # Comprehensive info
                    comInfo = []
                    # [K/D,승률,Top10,평균딜량,게임수, 최다킬수,헤드샷,저격거리,생존,평균순위]
                    for ci in squadQueInfo.findAll('p', {'class': 'value'}):
                        comInfo.append(''.join(ci.text.split()))
                    embed = discord.Embed(title="Player Unkonw Battle Ground 배그 전적 검색 사이트(**출저**)", description="",
                                          color=0x5CD1E5)
                    embed.add_field(name="배그 전적 검색 사이트(**출저**)", value=URL, inline=False)
                    embed.add_field(name="Real Time Accessors and Server Status",
                                    value="Accessors : " + serverAccessorAndStatus[0] + " | " "Server Status : " +
                                          serverAccessorAndStatus[1].split(':')[-1], inline=False)
                    embed.add_field(name="Player located server",
                                    value=seasonInfo[2] + " Server / Total playtime : " + squadQueTotalPlayTime,
                                    inline=False)
                    embed.add_field(name="Tier(Rank Point)",
                                    value=tier + " (" + rankPoint + "p)", inline=False)
                    embed.add_field(name="K/D", value=comInfo[0], inline=True)
                    embed.add_field(name="승률", value=comInfo[1], inline=True)
                    embed.add_field(name="Top 10 비율", value=comInfo[2], inline=True)
                    embed.add_field(name="평균딜량", value=comInfo[3], inline=True)
                    embed.add_field(name="게임수", value=comInfo[4] + "판", inline=True)
                    embed.add_field(name="최다킬수", value=comInfo[5] + "킬", inline=True)
                    embed.add_field(name="헤드샷 비율", value=comInfo[6] , inline=True)
                    embed.add_field(name="저격거리", value=comInfo[7], inline=True)
                    embed.add_field(name="평균생존시간", value=comInfo[8], inline=True)
                    embed.set_footer(text='Service provided by Hoplin.',
                                     icon_url='https://avatars2.githubusercontent.com/u/45956041?s=460&u=1caf3b112111cbd9849a2b95a88c3a8f3a15ecfa&v=4')
                    await message.channel.send("PUBG player " + playerNickname + "'s FPP squad que information",
                                               embed=embed)
        except HTTPError as e:
            embed = discord.Embed(title="Not existing plyer",
                                  description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",
                                  color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)
        except AttributeError as e:
            embed = discord.Embed(title="Not existing plyer",
                                  description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",
                                  color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)
















        


client.run(token)