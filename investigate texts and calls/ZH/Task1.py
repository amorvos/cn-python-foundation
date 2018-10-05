# coding:utf-8
"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."""

total_count_format = "There are {} different telephone numbers in the records."

numbers = set()

try:
    with open('texts.csv', 'r') as f:
        reader = csv.reader(f)
        texts = list(reader)
        for test in texts:
            numbers.add(test[0])
            numbers.add(test[1])
except IOError:
    print("not find the texts.csv, please check the file")

try:
    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)
        for call in calls:
            numbers.add(call[0])
            numbers.add(call[1])
except IOError:
    print("not find the calls.csv, please check the file")

print(total_count_format.format(numbers.__len__()))
