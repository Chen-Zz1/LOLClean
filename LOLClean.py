#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
import os
import re
import shutil

rootlist = ['Game', 'LeagueClient', 'Riot Client', 'TCLS', 'WeGameLauncher', 'LOLClean.py']
LeagueClientDelDirList = ['FeedBack', 'NetworkAssist', 'TQM']
date_match = r'\d{4}-\d{2}-\d{2}'
TCLSDelDirList = 'TP'

def delf(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
        print ('正在删除:' + path)
    else:
        os.remove(path)
        print('正在删除：' + path)

def delfuc():
    currentPath = os.getcwd().replace('\\','/')
    if currentPath[-4:] != '英雄联盟':
        print('请将脚本移动到英雄联盟安装文件夹运行（目录名为：“英雄联盟”）')
        return
    print('将会保留根目录以下文件夹，其余无用文件将会被删除，是否继续？')
    for file in rootlist:
        print (file)
    flag = input('输入y并使用回车以继续，其他操作终止删除。\n> ')
    if flag != 'y' and flag != 'Y':
        print('任务终止！')
        return
    CurrentFile = os.listdir('.')
    for file in CurrentFile:
        if file in rootlist:
            continue
        else:
            delf(file)
    print('删除成功！')
    print('即将删除LeagueClient目录下无用文件，以下文件夹以及日志文件将被清除：')
    CurrentFile = os.listdir('./LeagueClient/')
    for file in CurrentFile:
        if file in LeagueClientDelDirList:
            print(file)
    flag = input('输入y并使用回车以继续，其他操作终止删除。\n> ')
    if flag != 'y' and flag != 'Y':
        print ('任务终止!')
        return
    for file in CurrentFile:
        if file in LeagueClientDelDirList:
            filepath = './LeagueClient/' + file
            delf(filepath)
        elif re.match(date_match, file):
            filepath = './LeagueClient/' + file
            delf(filepath)
    print('删除完毕！')

if __name__ == '__main__':
    delfuc()
    os.system('pause')
