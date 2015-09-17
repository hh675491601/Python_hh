#python操作xml文件问题
#!/usr/<a href="https://www.baidu.com/s?wd=bin&tn=44039180_cpr&fenlei=mv6quAkxTZn0IZRqIHckPjm4nH00T1dBuHuhuyf1mvnsmhwhm1w-0ZwV5Hcvrjm3rH6sPfKWUMw85HfYnjn4nH6sgvPsT6K1TL0qnfK1TL0z5HD0IgF_5y9YIZ0lQzqlpA-bmyt8mh7GuZR8mvqVQL7dugPYpyq8Q1RdnjndPjDvPf" target="_blank" class="baidu-highlight">bin</a>/python
# -*- coding=utf-8 -*-
# author : wklken@yeah.net
# date: 2012-05-25
# version: 0.1
from xml.etree.ElementTree import ElementTree,Element
def read_xml(in_path):
    '''读取并解析<a href="https://www.baidu.com/s?wd=xml%E6%96%87%E4%BB%B6&tn=44039180_cpr&fenlei=mv6quAkxTZn0IZRqIHckPjm4nH00T1dBuHuhuyf1mvnsmhwhm1w-0ZwV5Hcvrjm3rH6sPfKWUMw85HfYnjn4nH6sgvPsT6K1TL0qnfK1TL0z5HD0IgF_5y9YIZ0lQzqlpA-bmyt8mh7GuZR8mvqVQL7dugPYpyq8Q1RdnjndPjDvPf" target="_blank" class="baidu-highlight">xml文件</a>
       in_path: xml路径
       return: ElementTree'''
    tree = ElementTree()
    tree.parse(in_path)
    return tree
def write_xml(tree, out_path):
    '''将<a href="https://www.baidu.com/s?wd=xml%E6%96%87%E4%BB%B6&tn=44039180_cpr&fenlei=mv6quAkxTZn0IZRqIHckPjm4nH00T1dBuHuhuyf1mvnsmhwhm1w-0ZwV5Hcvrjm3rH6sPfKWUMw85HfYnjn4nH6sgvPsT6K1TL0qnfK1TL0z5HD0IgF_5y9YIZ0lQzqlpA-bmyt8mh7GuZR8mvqVQL7dugPYpyq8Q1RdnjndPjDvPf" target="_blank" class="baidu-highlight">xml文件</a>写出
       tree: xml树
       out_path: 写出路径'''
    tree.write(out_path, encoding="utf-8",xml_declaration=True)
def if_match(node, kv_<a href="https://www.baidu.com/s?wd=map&tn=44039180_cpr&fenlei=mv6quAkxTZn0IZRqIHckPjm4nH00T1dBuHuhuyf1mvnsmhwhm1w-0ZwV5Hcvrjm3rH6sPfKWUMw85HfYnjn4nH6sgvPsT6K1TL0qnfK1TL0z5HD0IgF_5y9YIZ0lQzqlpA-bmyt8mh7GuZR8mvqVQL7dugPYpyq8Q1RdnjndPjDvPf" target="_blank" class="baidu-highlight">map</a>):
    '''判断某个节点是否包含所有传入参数属性
       node: 节点
       kv_<a href="https://www.baidu.com/s?wd=map&tn=44039180_cpr&fenlei=mv6quAkxTZn0IZRqIHckPjm4nH00T1dBuHuhuyf1mvnsmhwhm1w-0ZwV5Hcvrjm3rH6sPfKWUMw85HfYnjn4nH6sgvPsT6K1TL0qnfK1TL0z5HD0IgF_5y9YIZ0lQzqlpA-bmyt8mh7GuZR8mvqVQL7dugPYpyq8Q1RdnjndPjDvPf" target="_blank" class="baidu-highlight">map</a>: 属性及属性值组成的<a href="https://www.baidu.com/s?wd=map&tn=44039180_cpr&fenlei=mv6quAkxTZn0IZRqIHckPjm4nH00T1dBuHuhuyf1mvnsmhwhm1w-0ZwV5Hcvrjm3rH6sPfKWUMw85HfYnjn4nH6sgvPsT6K1TL0qnfK1TL0z5HD0IgF_5y9YIZ0lQzqlpA-bmyt8mh7GuZR8mvqVQL7dugPYpyq8Q1RdnjndPjDvPf" target="_blank" class="baidu-highlight">map</a>'''
    for <a href="https://www.baidu.com/s?wd=key&tn=44039180_cpr&fenlei=mv6quAkxTZn0IZRqIHckPjm4nH00T1dBuHuhuyf1mvnsmhwhm1w-0ZwV5Hcvrjm3rH6sPfKWUMw85HfYnjn4nH6sgvPsT6K1TL0qnfK1TL0z5HD0IgF_5y9YIZ0lQzqlpA-bmyt8mh7GuZR8mvqVQL7dugPYpyq8Q1RdnjndPjDvPf" target="_blank" class="baidu-highlight">key</a> in kv_map:
        if node.get(<a href="https://www.baidu.com/s?wd=key&tn=44039180_cpr&fenlei=mv6quAkxTZn0IZRqIHckPjm4nH00T1dBuHuhuyf1mvnsmhwhm1w-0ZwV5Hcvrjm3rH6sPfKWUMw85HfYnjn4nH6sgvPsT6K1TL0qnfK1TL0z5HD0IgF_5y9YIZ0lQzqlpA-bmyt8mh7GuZR8mvqVQL7dugPYpyq8Q1RdnjndPjDvPf" target="_blank" class="baidu-highlight">key</a>) != kv_map.get(<a href="https://www.baidu.com/s?wd=key&tn=44039180_cpr&fenlei=mv6quAkxTZn0IZRqIHckPjm4nH00T1dBuHuhuyf1mvnsmhwhm1w-0ZwV5Hcvrjm3rH6sPfKWUMw85HfYnjn4nH6sgvPsT6K1TL0qnfK1TL0z5HD0IgF_5y9YIZ0lQzqlpA-bmyt8mh7GuZR8mvqVQL7dugPYpyq8Q1RdnjndPjDvPf" target="_blank" class="baidu-highlight">key</a>):
            return False
    return True
#---------------search -----
def find_nodes(tree, path):
    '''查找某个路径匹配的所有节点
       tree: xml树
       path: 节点路径'''
    return tree.findall(path)
def get_node_by_keyvalue(nodelist, kv_map):
    '''根据属性及属性值定位符合的节点，返回节点
       nodelist: 节点列表
       kv_map: 匹配属性及属性值map'''
    result_nodes = []
    for node in nodelist:
        if if_match(node, kv_map):
            result_nodes.append(node)
    return result_nodes
#---------------change -----
def change_node_properties(nodelist, kv_map, is_delete=False):
    '''修改/增加 /删除 节点的属性及属性值
       nodelist: 节点列表
       kv_map:属性及属性值map'''
    for node in nodelist:
        for key in kv_map:
            if is_delete:
                if key in node.attrib:
                    del node.attrib[key]
            else:
                node.set(key, kv_map.get(key))
                
def change_node_text(nodelist, text, is_add=False, is_delete=False):
    '''改变/增加/删除一个节点的文本
       nodelist:节点列表
       text : 更新后的文本'''
    for node in nodelist:
        if is_add:
            node.text += text
        elif is_delete:
            node.text = ""
        else:
            node.text = text
                
def create_node(tag, property_map, content):
    '''新造一个节点
       tag:节点标签
       property_map:属性及属性值map
       content: 节点闭合标签里的文本内容
       return 新节点'''
    element = Element(tag, property_map)
    element.text = content
    return element
            
def add_child_node(nodelist, element):
    '''给一个节点添加子节点
       nodelist: 节点列表
       element: 子节点'''
    for node in nodelist:
        node.append(element)
            
def del_node_by_tagkeyvalue(nodelist, tag, kv_map):
    '''同过属性及属性值定位一个节点，并删除之
       nodelist: 父节点列表
       tag:子节点标签
       kv_map: 属性及属性值列表'''
    for parent_node in nodelist:
        children = parent_node.getchildren()
        for child in children:
            if child.tag == tag and if_match(child, kv_map):
                parent_node.remove(child)
                            
if __name__ == "__main__":
        
    #1. 读取<a href="https://www.baidu.com/s?wd=xml%E6%96%87%E4%BB%B6&tn=44039180_cpr&fenlei=mv6quAkxTZn0IZRqIHckPjm4nH00T1dBuHuhuyf1mvnsmhwhm1w-0ZwV5Hcvrjm3rH6sPfKWUMw85HfYnjn4nH6sgvPsT6K1TL0qnfK1TL0z5HD0IgF_5y9YIZ0lQzqlpA-bmyt8mh7GuZR8mvqVQL7dugPYpyq8Q1RdnjndPjDvPf" target="_blank" class="baidu-highlight">xml文件</a>
    tree = read_xml("./test.xml")
        
    #2. 属性修改
      #A. 找到父节点
    nodes = find_nodes(tree, "processers/processer")
      #B. 通过属性准确定位子节点
    result_nodes = get_node_by_keyvalue(nodes, {"name":"BProcesser"})
      #C. 修改节点属性
    change_node_properties(result_nodes, {"age": "1"})
      #D. 删除节点属性
    change_node_properties(result_nodes, {"value":""}, True)
        
    #3. 节点修改
      #A.<a href="https://www.baidu.com/s?wd=%E6%96%B0%E5%BB%BA&tn=44039180_cpr&fenlei=mv6quAkxTZn0IZRqIHckPjm4nH00T1dBuHuhuyf1mvnsmhwhm1w-0ZwV5Hcvrjm3rH6sPfKWUMw85HfYnjn4nH6sgvPsT6K1TL0qnfK1TL0z5HD0IgF_5y9YIZ0lQzqlpA-bmyt8mh7GuZR8mvqVQL7dugPYpyq8Q1RdnjndPjDvPf" target="_blank" class="baidu-highlight">新建</a>节点
    a = create_node("person", {"age":"15","money":"200000"}, "this is the firest content")
      #B.插入到父节点之下
    add_child_node(result_nodes, a)
        
    #4. 删除节点
       #定位父节点
    del_parent_nodes = find_nodes(tree, "processers/services/service")
       #准确定位子节点并删除之
    target_del_node = del_node_by_tagkeyvalue(del_parent_nodes, "chain", {"sequency" : "chain1"})
        
    #5. 修改节点文本
       #定位节点
    text_nodes = get_node_by_keyvalue(find_nodes(tree, "processers/services/service/chain"), {"sequency":"chain3"})
    change_node_text(text_nodes, "new text")
        
    #6. 输出到结果文件
    write_xml(tree, "./out.xml")