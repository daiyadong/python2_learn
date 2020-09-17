#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print "dict['Name']: ", dict['Name']
print "dict['Age']: ", dict['Age']

print("---修改、添天dict---")
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8 # 更新
dict['School'] = "RUNOOB" # 添加


print "dict['Age']: ", dict['Age']
print "dict['School']: ", dict['School']

print("---删除---")
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del dict['Name']  # 删除键是'Name'的条目
dict.clear()      # 清空字典所有条目
del dict          # 删除字典

#print "dict['Age']: ", dict['Age'] #会出错
#print "dict['School']: ", dict['School']

print("---同一键被赋值两次---")
dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print "dict['Name']: ", dict['Name']
