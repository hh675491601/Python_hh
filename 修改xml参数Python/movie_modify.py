#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os
import sys,re
xml_file_test_path = 'movie_xml.xml'
xml_key = 'rank'
xml_modify_value = '9999999'

def modify_xml(xml_path,xml_key,xml_modify_value):
  xml = ET.parse(xml_path)
  # xml = unicode(xml,encoding='gbk').encode('utf-8')
  root = xml.getroot()
  for country in root:
    country.find(xml_key).text = xml_modify_value
    print '%s::%s' % (xml_key,country.find(xml_key).text)
    xml.write('output_xml.xml',encoding = 'utf-8')

modify_xml(xml_file_test_path,xml_key,xml_modify_value)