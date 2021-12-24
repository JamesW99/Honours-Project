import time

import requests
from lxml import etree
import wget
from connect_db import *
import re

# 所有品牌的链接
def all():
    '''
    所有品牌的链接
    :return:
    '''
    html_code = etree.parse('download/all.html', etree.HTMLParser())

    count = 0

    for i in range(1149):
        result = html_code.xpath('//tbody/tr[' + str(i+1) + ']/td[1]/a')
        numbers = html_code.xpath(f'//tbody/tr[' + str(i+1) + ']/td[2]')

        print(result[0].attrib['href'])
        # print(numbers[0].text)
        count += int(numbers[0].text)

    print('estimate there have', count, ' bikes')

# 该品牌所有车
def spe():
    '''
    输入一个品牌列表，输出该列表所有车
    :param link:
    :param size:
    :return:
    '''
    counter = 0
    for i in range(1149):
        html_code = etree.parse('brand/b'+str(i+1)+'.html', etree.HTMLParser())
        index = 1
        while True:
            try:
                bike_link = html_code.xpath('//tbody/tr[' + str(index) + ']/td[2]/a')
                # print process and url
                # print(counter)
                print(bike_link[0].attrib['href'])

                counter+=1
                index+=1

            except:
                # print('end')
                break

            # time.sleep(0.01)
        # print('this brand total: ' + str(index-1))
    print('total bikes: ' + str(counter))


def countSize(html):
    '''
    Calculate how many sizes this bike comes in
    :param html: Parsed html source code
    :return: Size list ['48 cm', '52 cm', '56 cm', '60 cm']
    '''
    size_counter = 0
    size_list = []
    while True:
        try:
            size = html.xpath('//table/thead/tr/th[' + str(size_counter + 2) + ']/strong')[0].text.strip()
            # print(size)
            size_list.append(size)
            size_counter += 1
        except:
            break
    return size_list


def backAethos():
    '''
    每个车的细节
    :return:
    '''
    dict1 = {}
    dict2 = {}
    dict3 = {}
    dict4 = {}
    dict5 = {}
    dict6 = {}
    dict7 = {}
    dict8 = {}
    dict9 = {}
    dict10 = {}
    dict11 = {}
    dict12 = {}
    dict13 = {}
    dict14 = {}
    dict15 = {}
    dict16 = {}

    def dict(index, row, num):
        if index == 1:
            dict1[row] = num
        if index == 2:
            dict2[row] = num
        if index == 3:
            dict3[row] = num
        if index == 4:
            dict4[row] = num
        if index == 5:
            dict5[row] = num
        if index == 6:
            dict6[row] = num
        if index == 7:
            dict7[row] = num
        if index == 8:
            dict8[row] = num
        if index == 9:
            dict9[row] = num
        if index == 10:
            dict10[row] = num
        if index == 11:
            dict11[row] = num
        if index == 12:
            dict12[row] = num
        if index == 13:
            dict13[row] = num
        if index == 14:
            dict14[row] = num
        if index == 15:
            dict15[row] = num
        if index == 16:
            dict16[row] = num


    # 自行车编号
    index = 0

    while index<3000:
        html_code = etree.parse('bikes/' + str(index+1) + '.html', etree.HTMLParser())
        size_list = countSize(html_code)

        if len(size_list) == 0:
            index += 1
            continue
        print(size_list)




        # get bike name
        title = html_code.xpath('/html/body/div[2]/header/div[3]/h1')[0].text
        print(title)
        # name_list.append(title)

        # get bike photo if exist
        try:
            image = html_code.xpath('/html/body/div[2]/section[1]/div[1]/a/img')[0].attrib['data-src']
            print(image)
        except:
            pass

        # get bike geometry detail
        try:
            parameter = html_code.xpath('//table/tbody/tr[2]/td[1]')[0].text
            print(parameter)
            # first_argument = float(html_code.xpath('//table/tbody/tr[2]/td[2]')[0].text)
            # print(first_argument)
        except:
            print("We don't currently have any geometry data for this bike.")

        index+=1
            # print(index)
            # time.sleep(0.01)


    print('Done, total have ', index, 'bikes.')


def aethos():
    '''
    每个车的细节
    :return:
    '''

    dict0 = {}
    dict1 = {}
    dict2 = {}
    dict3 = {}
    dict4 = {}
    dict5 = {}
    dict6 = {}
    dict7 = {}
    dict8 = {}
    dict9 = {}
    dict10 = {}
    dict11 = {}
    dict12 = {}
    dict13 = {}
    dict14 = {}
    dict15 = {}
    dict16 = {}

    # 第几个size就插入第几个字典
    def dict(index, row, num):
        if index == 0:
            dict0[row] = num
        if index == 1:
            dict1[row] = num
        if index == 2:
            dict2[row] = num
        if index == 3:
            dict3[row] = num
        if index == 4:
            dict4[row] = num
        if index == 5:
            dict5[row] = num
        if index == 6:
            dict6[row] = num
        if index == 7:
            dict7[row] = num
        if index == 8:
            dict8[row] = num
        if index == 9:
            dict9[row] = num
        if index == 10:
            dict10[row] = num
        if index == 11:
            dict11[row] = num
        if index == 12:
            dict12[row] = num
        if index == 13:
            dict13[row] = num
        if index == 14:
            dict14[row] = num
        if index == 15:
            dict15[row] = num
        if index == 16:
            dict16[row] = num


    # 自行车编号(第几个自行车)
    index = 0
    # index = 261
    # while index<1476:
    while index<13146:
        def saveClear():
            if len(size_list) == 1:
                insert(get_database(), "new_geo", [dict0])
            if len(size_list) == 2:
                insert(get_database(), "new_geo", [dict0, dict1])
            if len(size_list) == 3:
                insert(get_database(), "new_geo", [dict0, dict1, dict2])
            if len(size_list) == 4:
                insert(get_database(), "new_geo", [dict0, dict1, dict2, dict3])
            if len(size_list) == 5:
                insert(get_database(), "new_geo", [dict0, dict1, dict2, dict3, dict4])
            if len(size_list) == 6:
                insert(get_database(), "new_geo", [dict0, dict1, dict2, dict3, dict4, dict5])
            if len(size_list) == 7:
                insert(get_database(), "new_geo", [dict0, dict1, dict2, dict3, dict4, dict5, dict6])
            if len(size_list) == 8:
                insert(get_database(), "new_geo", [dict0, dict1, dict2, dict3, dict4, dict5, dict6, dict7])
            if len(size_list) == 9:
                insert(get_database(), "new_geo", [dict0, dict1, dict2, dict3, dict4, dict5, dict6, dict7, dict8])
            if len(size_list) == 10:
                insert(get_database(), "new_geo", [dict0, dict1, dict2, dict3, dict4, dict5, dict6, dict7, dict8, dict9])
            if len(size_list) == 11:
                insert(get_database(), "new_geo", [dict0, dict1, dict2, dict3, dict4, dict5, dict6, dict7, dict8, dict9, dict10])
            if len(size_list) == 12:
                insert(get_database(), "new_geo", [dict0, dict1, dict2, dict3, dict4, dict5, dict6, dict7, dict8, dict9, dict10, dict11])
            if len(size_list) == 13:
                insert(get_database(), "new_geo", [dict0, dict1, dict2, dict3, dict4, dict5, dict6, dict7, dict8, dict9, dict10, dict11, dict12])
            if len(size_list) == 14:
                insert(get_database(), "new_geo", [dict0, dict1, dict2, dict3, dict4, dict5, dict6, dict7, dict8, dict9, dict10, dict11, dict12, dict13])
            if len(size_list) == 15:
                insert(get_database(), "new_geo", [dict0, dict1, dict2, dict3, dict4, dict5, dict6, dict7, dict8, dict9, dict10, dict11, dict12, dict13, dict14])
            if len(size_list) == 16:
                insert(get_database(), "new_geo", [dict0, dict1, dict2, dict3, dict4, dict5, dict6, dict7, dict8, dict9, dict10, dict11, dict12, dict13, dict14, dict15])
            if len(size_list) == 17:
                insert(get_database(), "new_geo", [dict0, dict1, dict2, dict3, dict4, dict5, dict6, dict7, dict8, dict9, dict10, dict11, dict12, dict13, dict14, dict15, dict16])

            # 清空字典-该自行车循环结束
            dict0.clear()
            dict1.clear()
            dict2.clear()
            dict3.clear()
            dict4.clear()
            dict5.clear()
            dict6.clear()
            dict7.clear()
            dict8.clear()
            dict9.clear()
            dict10.clear()
            dict11.clear()
            dict12.clear()
            dict13.clear()
            dict14.clear()
            dict15.clear()
            dict16.clear()

        html_code = etree.parse('bikes/' + str(index+1) + '.html', etree.HTMLParser())
        size_list = countSize(html_code)

        # 排除空网页
        if len(size_list) == 0:
            index += 1
            continue
        # print(size_list)

        # 展示进度
        print(index+1)

        # 把本型号所有信息加入字典
        for i in range(len(size_list)): # 循环所有尺码

            # add bike name into dict
            title = html_code.xpath('/html/body/div[2]/header/div[3]/h1')[0].text
            # print(title)
            dict(i, 'Name', title)

            # use regex find year data in title
            try:
                year = int(re.search(r"(19|20)\d{2}$", title).group(0))
                # print(year)
                dict(i, 'Year', year)
            except: pass

            # add bike photo url to dict
            try:
                image = html_code.xpath('/html/body/div[2]/section[1]/div[1]/a/img')[0].attrib['data-src']
                dict(i, 'Image', image)
            except: pass

            # add bike size to dict
            dict(i, 'Size', size_list[i].strip())

            # 本地html文件的序号
            dict(i, 'Index', index+1)

            # geometrygeeks.bike的链接
            url = html_code.xpath('/html/head/link[22]')[0].attrib['href']
            dict(i, 'URL', url)


            row_index = 2
            while True: # 循环此尺码所有信息
                try:
                    # key 为数据名称
                    key = html_code.xpath('//table/tbody/tr['+ str(row_index) +']/td[1]')[0].text

                    try:
                        # 尝试使用float保存值
                        value = float(html_code.xpath('//table/tbody/tr['+ str(row_index) +']/td['+ str(i+2) +']')[0].text)
                    except ValueError:
                        # float不可用则保存为string
                        value = html_code.xpath('//table/tbody/tr['+ str(row_index) +']/td['+ str(i+2) +']')[0].text.strip()

                        # 如果是Head Angle or Seat Angle 则进一步处理
                        if key == "Head Angle" or key == "Seat Angle":
                            # 去掉'°'和'˚'
                            value = value.strip('°')
                            value = value.strip('˚')
                            value = value.strip('°')
                            value = value.strip('˚')
                            # ','替换为 '.'
                            value = value.replace(',', '.')
                            # 验证是否为纯数字
                            try:
                                value = float(value)
                            except:
                                # 非纯数字则保存为string
                                if len(value):
                                    print(index+1,' Head or Seat Angle is String:', value)
                                # 否则为空
                                else:
                                    print(index + 1, ' Head or Seat Angle is empty:', value)
                                    value = None

                    # 将获得的数据和名称保存到字典中
                    dict(i, key, value)
                    row_index +=1

                # 结束该尺码的循环时获取数据源信息
                except:
                    try:
                        # 尝试获取数据源url
                        value = html_code.xpath('//table/tbody/tr[' + str(row_index - 1) + ']/td[' + str(i + 2) + ']/a')[0].attrib['href']
                    except IndexError:
                        # 获取不到则改为获取数据源种类
                        try:
                            value = html_code.xpath('//table/tbody/tr[' + str(row_index - 1) + ']/td[' + str(i + 2) + ']/small')[0].text.strip()
                        except AttributeError:
                            value = None
                            # 否则报错
                            # print('bike', index+1, 'cant get data source')

                    dict(i, key, value)

                    # print(i+1, 'size done')

                    # 结束该尺码循环
                    break

        saveClear()


        index+=1
        # print(index)
        # time.sleep(0.01)


    print('Done, total have', index, 'bikes.')


def test():
    # '//table/tbody/tr[17]/td[2]/small' 5933
    # html_code = etree.parse('../index.html.5970', etree.HTMLParser())

    # html_code = etree.parse('bikes/712.html', etree.HTMLParser())
    # # key = html_code.xpath('//table/tbody/tr[14]/td[2]/a/small')[0].text
    # # key = html_code.xpath('//table/tbody/tr[15]/td[2]/a/small')
    # # key = html_code.xpath('//table/tbody/tr[17]/td[2]/a')[0].attrib['href']
    # key = html_code.xpath('//table/tbody/tr[6]/td[1]')[0].text
    # if key == "Head Angle" or key == "Seat Angle":
    #     value = html_code.xpath('//table/tbody/tr[5]/td[2]')[0].text.strip()
    #     value = value.strip('°')
    #     value = value.strip('˚')
    #     value = value.replace(',','.')
    #     try:
    #         value = float(value)
    #     except:
    #         pass
    #         value = None
    # print(key)
    # print(type(value))

    for i in range(10000):
        html_code = etree.parse('bikes/'+str(i+1)+'.html', etree.HTMLParser())
        url = html_code.xpath('/html/head/link[22]')[0].attrib['href']
        print(url)





if __name__ == '__main__':
    # all()
    # spe()
    # random()
    aethos()
    # test()