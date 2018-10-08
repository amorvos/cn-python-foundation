# coding=utf-8
"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

"""
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

promote_call_number = set()

send_text_num = set()
receive_text_num = set()
send_call_num = set()
receive_call_num = set()

try:
    with open('texts.csv', 'r') as f:
        reader = csv.reader(f)
        texts = list(reader)
        for text in texts:
            send_text_num.add(text[0])
            receive_text_num.add(text[1])
except IOError:
    print("not find the texts.csv, please check the file")

try:
    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)
        for call in calls:
            send_call_num.add(call[0])
            receive_call_num.add(call[1])
except IOError:
    print("not find the texts.csv, please check the file")

for number in send_call_num:
    if send_text_num.__contains__(number):
        continue
    if receive_text_num.__contains__(number):
        continue
    if receive_call_num.__contains__(number):
        continue
    promote_call_number.add(number)

print("These numbers could be telemarketers: ")
for number in sorted(set(promote_call_number)):
    print(number)
