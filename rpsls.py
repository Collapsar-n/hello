#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�2020��11��24��
"""
import random
def name_to_number(name):#����Ϸ�����Ӧ����ͬ������
    if name=='ʯͷ':
        name=0
    if name=='ʷ����':
        name=1
    if name=='ֽ':
        name=2
    if name=='����':
        name=3
    if name=='����':
        name=4
    return name

def number_to_name(number):#������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    if number==0:
        number='ʯͷ'
    if number==1:
        number='ʷ����'
    if number==2:
        number='ֽ'
    if number==3:
        number='����'
    if number==4:
        number='����'
    return number

def rpsls(player_choice):#�û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    player_choice=choice_name# ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
    a=random.randrange(0,5) # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
    player_choice_number = name_to_number(player_choice)
    comp_number=number_to_name(a)
    while player_choice_number == name_to_number('ʯͷ'):
        print('����ѡ��Ϊ����ʯͷ' )
        print('�������ѡ��Ϊ��' + number_to_name(a))# ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
        if a==1 or a==2:# ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
            print('�����Ӯ��')
        if a==3 or a==4:
            print('��Ӯ��')
        if a==0:
            print('���ͼ��������һ����')
        break
    while player_choice_number == name_to_number('ʷ����'):
        print('����ѡ��Ϊ����ʷ����' )
        print('�������ѡ��Ϊ��' + number_to_name(a))
        if a==2 or a==3:
            print('�����Ӯ��')
        if a==0 or a==4:
            print('��Ӯ��')
        if a==1:
            print('���ͼ��������һ����')
        break
    while player_choice_number ==name_to_number('ֽ') :
        print('����ѡ��Ϊ��ֽ' )
        print('�������ѡ��Ϊ' + number_to_name(a))
        if a==1 or a==0:
            print('��Ӯ��')
        if a==3 or a==4:
            print('�����Ӯ��')
        if a==2:
            print('���ͼ��������һ����')
        break
    while player_choice_number==name_to_number('����'):
        print('����ѡ��Ϊ����')
        print('�������ѡ��Ϊ' +  number_to_name(a))
        if a==4 or a==0:
            print('�����Ӯ��')
        if a==1 or a==2:
            print('��Ӯ��')
        if a==3:
            print('���ͼ��������һ����')
        break
    while player_choice_number==name_to_number('����'):
        print('����ѡ��Ϊ����')
        print('�������ѡ��Ϊ' +  number_to_name(a))
        if a==0 or a==3:
            print('��Ӯ��')
        if a==1 or a==2:
            print('�����Ӯ��')
        if a==4:
            print('���ͼ��������һ����')
        break
    return player_choice_number

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
if choice_name!='ʯͷ'and choice_name!='����' and choice_name!='ֽ' and choice_name !='����' and choice_name !='ʷ����' :
    print('Error: No Correct Name')#�������뷶Χ�ⱨ��

rpsls(choice_name)








