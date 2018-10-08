# coding=utf-8
"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
import re

"""
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，[每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""

fixed_line_telephone = r'^\(0\d+\)\d+'
mobile_telephone = r'^[7-9]\d+ \d+'
area_code = r"^\(0\d+\)"
bangalore_area_code = "(080)"

bangalore_call_number = []


def is_from_bangalore(from_number, call_number):
    """
    :param from_number: 打电话的号码
    :param call_number:  接电话的号码
    """
    if str(from_number).startswith(bangalore_area_code):
        bangalore_call_number.append(call_number)


try:
    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)
        for call in calls:
            is_from_bangalore(call[0], call[1])
except IOError:
    print("not find the texts.csv, please check the file")

analyze_call_number = []
for target_number in bangalore_call_number:
    if re.match(r'%s' % fixed_line_telephone, target_number):
        analyze_call_number.append(str(re.findall(area_code, target_number)[0])[1:-1])
    if re.match(r'%s' % mobile_telephone, target_number):
        analyze_call_number.append(str(str(target_number).split(" ")[0])[0:4])

print("The numbers called by people in Bangalore have codes:")
for number in sorted(set(analyze_call_number)):
    print(number)

target_number_bangalore = list(filter(lambda number: number.startswith(bangalore_area_code), bangalore_call_number))
print("{}% percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
    target_number_bangalore.__len__() * 100 / bangalore_call_number.__len__()))
