import re
import os
# 全局替换str
# 

print(os.getcwd())
print(os.path.exists('中国裁判文书网2.js'))

def sub_substr(matched):
    # matched = .sunstr(\d+,\d+)//.substr(\d+)
    # 将substr方法替换为python的切片
    a = matched.group(1)
    b = matched.group(2)
    if b:
        return '['+a+': '+b+']'
    else:
        return '['+a+':]'

def sub_length(matched):
    # matched = \w+\.length
    return '< len('+matched.group(1)+')'

def main():
    f = open('中国裁判文书网2.js', 'r', encoding='utf-8')
    data = f.read()
    f.close()
    # 替换所有的function为 def
    text1 = data.replace('function', 'def')
    # 去掉所有的}
    text2 = text1.replace('}', '')
    # 按行分隔
    text3_list = text2.split('\n')
    text4_list = []
    # 遍历检查每一行
    for each_line in text3_list:
        # 删除末尾的;
        each_line = each_line.strip(';')
        # 去掉var
        each_line = re.sub('var ?', '', each_line)
        # 去掉new
        each_line = re.sub('new', '', each_line)
        # ++换成 +=1
        each_line = each_line.replace('++', '+=1')
        # 如果这行有def,{换成
        if 'def' in each_line:
            each_line = each_line.replace('{', ':')
        # # 如果有substr替换
        # if 'substr' in each_line:
        #     each_line = re.sub('\.substr\((\d+),? ?(\d+)?\)', sub_substr, each_line)
        # # 如果有length参数替换成len()
        # if '.length' in each_line:
        #     each_line = re.sub('< ?(.+)\.length', sub_length, each_line)
        # 如果有for 大改动
        if 'for' in each_line:
            # 去掉for 和()
            print(each_line)
            each_line = each_line.replace('for ', '').strip('{').replace('(', '', 1).rstrip().strip(')')
            # 按;分隔
            # [    i=0,i<len(a), i++]
            lines = each_line.split(';')
            indent = ''
            for i in lines[0]:
                if i == ' ':
                    indent = indent + i
                else:
                    break
            try:
                text4_list.append(lines[0])
                text4_list.append(indent+'while '+lines[1]+':')
                text4_list.append(indent*2+lines[2].strip())
            except:
                pass
        else:
            text4_list.append(each_line)
    # 保存数据
    with open('china.py', 'w', encoding='utf-8') as f:
        for each_line in text4_list:
            print(each_line)
            f.write(each_line+'\n')

try:
    main()
except Exception as exc:
    raise exc