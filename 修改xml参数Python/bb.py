#!/usr/bin/python
#-*-coding:utf-8-*-


from xml.etree import ElementTree
from xml.etree.ElementTree import Element

'''
class MyTreeBuilder(ElementTree.TreeBuilder):
   def comment(self, data):
       self.start(ElementTree.Comment, {})
       self.data(data)
       self.end(ElementTree.Comment)
with open('/Users/cg/Desktop/channel.xml', 'r') as f:
   xml = ElementTree.parse(
       f, parser=ElementTree.XMLParser(target=MyTreeBuilder()))
ElementTree.dump(xml)
'''


class CommentedTreeBuilder ( ElementTree.XMLTreeBuilder ):
    def __init__ ( self, html = 0, target = None ):
        ElementTree.XMLTreeBuilder.__init__( self, html, target )
        self._parser.CommentHandler = self.handle_comment
    
    def handle_comment ( self, data ):
        self._target.start( ElementTree.Comment, {} )
        self._target.data( data )
        self._target.end( ElementTree.Comment )


with open( '/Users/cg/Desktop/channel.xml', 'r' ) as f:
    xml = ElementTree.parse(f,parser =CommentedTreeBuilder())
root = xml.getroot()
e_movie = Element('movie')  
root.append(e_movie)
ElementTree.ElementTree(root).write('/Users/cg/Desktop/channel.xml', 'UTF-8')