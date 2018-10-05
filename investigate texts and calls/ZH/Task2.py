# coding=utf-8
"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

"""
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""

call_statistics = {}

statistics_result_format = "{} spent the longest time, {} seconds, on the phone during September 2016."

try:
    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)
        for call in calls:
            if call_statistics.has_key(call[0]):
                call_statistics[call[0]] += int(call[3])
            else:
                call_statistics[call[0]] = int(call[3])
            if call_statistics.has_key(call[1]):
                call_statistics[call[1]] += int(call[3])
            else:
                call_statistics[call[1]] = int(call[3])
except IOError:
    print("not find the calls.csv, please check the file")

use_time = sorted(call_statistics.values())[call_statistics.__len__() - 1]
phone = list(call_statistics.keys())[list(call_statistics.values()).index(use_time)]
print(statistics_result_format.format(phone, use_time))
