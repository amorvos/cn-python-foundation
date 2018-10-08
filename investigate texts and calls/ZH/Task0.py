# coding:utf-8
"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

text_print_format = "First record of texts, {} texts {} at time {}"
call_print_format = "Last record of calls, {} calls {} at time {}, lasting {} seconds"

text_first = []
call_last = []

"""
任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

try:
    with open('texts.csv', 'r') as f:
        reader = csv.reader(f)
        texts = list(reader)
        if len(texts) > 0:
            text_first = texts[0]
except IOError:
    print("not find the texts.csv, please check the file")

try:
    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)
        if len(calls) > 0:
            call_last = calls[-1]
except IOError:
    print("not find the texts.csv, please check the file")

if text_first != "":
    print(text_print_format.format(text_first[0], text_first[1], text_first[2]))
else:
    print("text file format error, the error data is " + str(text_first))

if call_last != "":
    print(call_print_format.format(call_last[0], call_last[1], call_last[2], call_last[3]))
else:
    print("call file format error, the error data is " + str(call_last))
