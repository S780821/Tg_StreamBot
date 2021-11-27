<h2 align="center">Tg Streamer Bot </h2>
<p>
Telegram bot for stream music or video on telegram, 
powered by <a href="https://github.com/pytgcalls/pytgcalls">PyTgCalls</a>
and <a href="https://github.com/pyrogram/pyrogram">Pyrogram</a>
</p>

<div align="center">
    <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a> <br /> 
    <a href="https://deepsource.io/gh/S780821/Tg_StreamBot/?ref=repository-badge"><img src="https://static.deepsource.io/deepsource-badge-light-mini.svg" alt="DeepSource"></a><br> 
    <a href="https://www.codacy.com/gh/S780821/Tg_StreamBot/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=S780821/Tg_StreamBot&amp;utm_campaign=Badge_Grade"><img src="https://app.codacy.com/project/badge/Grade/63ed7098eee74e45956a3c4d0512078b"/></a>
    <a href="https://github.com/S780821/Tg_StreamBot"><img src="https://www.codefactor.io/repository/github/S780821/Tg_StreamBot/badge" alt="CodeFactor" /></a> <br />
    <a href="https://github.com/pyrogram/pyrogram"><img src="https://img.shields.io/badge/Pyrogram-1.2.9-blue?logo=github"></a>
    <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.9.7-blue?logo=python&logoColor=yellow"></a>
    <a href="https://github.com/pytgcalls/pytgcalls"><img src="https://img.shields.io/badge/PyTgCalls-0.8.1-blue?logo=github"></a> <br> <br>
    <a href="https://github.com/S780821/Tg_StreamBot"><img src="https://img.shields.io/github/repo-size/S780821/Tg_StreamBot?logo=github"></a> <br>
    <a href="https://github.com/S780821/Tg_StreamBot"><img src="https://img.shields.io/github/forks/S780821/Tg_StreamBot?logo=github"></a>
    <a href="https://github.com/S780821/Tg_StreamBot"><img src="https://img.shields.io/github/stars/S780821/Tg_StreamBot?logo=github"></a>
</div>


<h3>Features</h3> 
<ul>
    <li>Playlist features</li>
    <li>Multi Language</li>
    <li>Maintained</li>
    <li>Less environment variables</li>
</ul>

<h3>Telegram</h3>
<ul>
    <a href="https://t.me/Xmarty_updates"><img alt="XmartyProject Channel" src="https://img.shields.io/badge/XmartyProject-Channel-blue.svg?logo=telegram"></a> <br/>
    <a href="https://t.me/Xmarty_Support"><img alt="XmartyProject Support" src="https://img.shields.io/badge/XmartyProject-Support-blue.svg?logo=telegram"></a> <br/>
</ul>

<h3>Deploy to Heroku </h3>
<div>
    <a href="https://heroku.com/deploy"><img src="https://www.herokucdn.com/deploy/button.svg"></a>
</div>

### Deploy to VPS
```
$ sudo su
# apt-get update && apt-get upgrade -y
# apt-get install curl
# curl -sL https://deb.nodesource.com/setup_16.x | bash - 
# apt-get install ffmpeg python3-pip python3-virtualenv nodejs -y 
# git clone https://github.com/S780821/Tg_StreamBot && cd Tg_StreamBot 
# virtualenv venv && . venv/bin/activate 
# pip3 install --no-cache-dir -r requirements.txt 
# cp sample.env .env 
# nano .env # fill it with your env 
# python3 main.py
```