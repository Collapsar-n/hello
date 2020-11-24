#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：聂媛媛
日期：2020年11月24日
"""
import random
def name_to_number(name):#将游戏对象对应到不同的整数
    if name=='石头':
        name=0
    if name=='史波克':
        name=1
    if name=='纸':
        name=2
    if name=='蜥蜴':
        name=3
    if name=='剪刀':
        name=4
    return name

def number_to_name(number):#将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    if number==0:
        number='石头'
    if number==1:
        number='史波克'
    if number==2:
        number='纸'
    if number==3:
        number='蜥蜴'
    if number==4:
        number='剪刀'
    return number

def rpsls(player_choice):#用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    player_choice=choice_name# 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice
    a=random.randrange(0,5) # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number
    player_choice_number = name_to_number(player_choice)
    comp_number=number_to_name(a)
    while player_choice_number == name_to_number('石头'):
        print('您的选择为·：石头' )
        print('计算机的选择为：' + number_to_name(a))# 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象
        if a==1 or a==2:# 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果
            print('计算机赢了')
        if a==3 or a==4:
            print('您赢了')
        if a==0:
            print('您和计算机出的一样呢')
        break
    while player_choice_number == name_to_number('史波克'):
        print('您的选择为·：史波克' )
        print('计算机的选择为：' + number_to_name(a))
        if a==2 or a==3:
            print('计算机赢了')
        if a==0 or a==4:
            print('您赢了')
        if a==1:
            print('您和计算机出的一样呢')
        break
    while player_choice_number ==name_to_number('纸') :
        print('您的选择为：纸' )
        print('计算机的选择为' + number_to_name(a))
        if a==1 or a==0:
            print('您赢了')
        if a==3 or a==4:
            print('计算机赢了')
        if a==2:
            print('您和计算机出的一样呢')
        break
    while player_choice_number==name_to_number('蜥蜴'):
        print('您的选择为蜥蜴')
        print('计算机的选择为' +  number_to_name(a))
        if a==4 or a==0:
            print('计算机赢了')
        if a==1 or a==2:
            print('您赢了')
        if a==3:
            print('您和计算机出的一样呢')
        break
    while player_choice_number==name_to_number('剪刀'):
        print('您的选择为剪刀')
        print('计算机的选择为' +  number_to_name(a))
        if a==0 or a==3:
            print('您赢了')
        if a==1 or a==2:
            print('计算机赢了')
        if a==4:
            print('您和计算机出的一样呢')
        break
    return player_choice_number

print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
if choice_name!='石头'and choice_name!='剪刀' and choice_name!='纸' and choice_name !='蜥蜴' and choice_name !='史波克' :
    print('Error: No Correct Name')#设置输入范围外报错

rpsls(choice_name)








