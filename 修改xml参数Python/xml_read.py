#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 传入 路径 + key 返回一个对应的key值
import xml.etree.ElementTree as ET
import urllib2
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

xml_test_key = 'CHGameKey'
xml_file_test_path = 'channel_xml.xml'
xml_output_path = 'output_channel_xml.xml'
xml_key = 'CHAppID'
xml_modify_value = 'jdsfssjklajslkaj接口接口来即可了解 ajdlkajdlkjaslkdjalsk'
server_url = "http://www.517huwai.com/Mobile/travels?count=10&page="

def get_value(xml_key,xml_path):
	xml = ET.parse(xml_path)
	root = xml.getroot()
	for channel in root:
		# print channel.find(xml_key).text
	  return 	channel.find(xml_key).text	

def modify_xml(xml_path,xml_key,xml_modify_value):
  xml = ET.parse(xml_path)
  root = xml.getroot()
  for channel in root:
    channel.find(xml_key).text = xml_modify_value
    print '%s::%s' % (xml_key,channel.find(xml_key).text)
    xml.write(xml_output_path,encoding = 'utf-8',xml_declaration=True)

#向服务器请求数据 返回key对应的value
def get_json_data(server_url):
    print 'requesting...'
	# url = 'http://movie.douban.com'
    json_http = urllib2.urlopen(server_url)
    data = json_http.read()
    json_data = json.loads(data)
    # print json_data
    r = json_data['travels']
    # print r
    #测试数据
    r_data = r[2]
    print r_data
    return r[2]

def get_some_value(json_list,jsondic_key):
    return json_list[jsondic_key]

# json_list = get_json_data(server_url)
# print get_some_value(json_list,'userId')
  	
# print get_value(xml_test_key,file_test_xml_path)
modify_xml(xml_file_test_path,xml_key,xml_modify_value)