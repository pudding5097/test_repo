#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 22:47:46 2019

@author: sinnoha
"""


"""
Exercise 1
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券）
使用 Python 如何生成 200 个激活码（或者优惠券）？

**********************
UUID: 
通用唯一标识符 ( Universally Unique Identifier )
对于所有的UUID它可以保证在空间和时间上的唯一性.
它是通过MAC地址, 时间戳, 命名空间, 随机数, 伪随机数来保证生成ID的唯一性, 有着固定的大小( 128 bit ).
它的唯一性和一致性特点使得可以无需注册过程就能够产生一个新的UUID.
UUID可以被用作多种用途, 既可以用来短时间内标记一个对象, 也可以可靠的辨别网络中的持久性对象.

为什么要使用UUID?
很多应用场景需要一个id, 
但是又不要求这个id 有具体的意义, 仅仅用来标识一个对象.
常见的例子有数据库表的id 字段.
另一个例子是前端的各种UI库, 
因为它们通常需要动态创建各种UI元素, 这些元素需要唯一的id , 这时候就需要使用UUID了. 
**********************
"""



#%%

"""
方法一：在字典里随机选4个字符，选四组
"""

import random

char_dict = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

parts = []
for i in range(4):
    gen_parts = random.sample(char_dict, 4)
    parts.append(''.join(gen_parts))
keys = '-'.join(parts)
print('Here is the Keys: {:s}'.format(keys))
print('Enjoy it!')

#%%

"""
方法二：通过UUID模块中的 uuid.uuid4() 函数随机生成标识符，取中间16位
"""

import uuid

gen_keys = str(uuid.uuid4())
source_code = gen_keys.replace('-', '')

parts = []
for i in range(4):
    gen_parts = source_code[i * 4 + 8: i * 4 + 12]
    parts.append(''.join(gen_parts))
keys = '-'.join(parts)
print('Here is the Keys: {:s}'.format(keys.upper()))
print('Enjoy it!')