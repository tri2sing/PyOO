'''
Created on Nov 19, 2015

@author: Sameer Adhikari

'''

from patterns.state.node import Node

# All the states are defined is one file due to the circular dependency between router and each state.
# Putting each state in a separate model meant that the circular dependency caused import errors.

class StartState(object):
    '''
    The starting state of the parser, when no
    processing of the input string has taken place.
    '''

    def process(self, remaining_string, parser):
        i_start_tag = remaining_string.find('<')
        i_end_tag = remaining_string.find('>')
        tag_name = remaining_string[i_start_tag + 1 : i_end_tag]
        root = Node(tag_name)
        parser.root = root
        parser.current_node = root
        parser.state = RouterState()
        return remaining_string[i_end_tag + 1:]
    
    
class TagOpenState(object):
    '''
    '''
    def process(self, remaining_string, parser):
        i_start_tag = remaining_string.find('<')
        i_end_tag = remaining_string.find('>')
        tag_name = remaining_string[i_start_tag + 1 : i_end_tag]
        node = Node(tag_name, parser.current_node)
        parser.current_node.children.append(node)
        parser.current_node = node 
        parser.state = RouterState()
        return remaining_string[i_end_tag + 1:].strip()


class TagCloseState(object):
    '''
    '''
    def process(self, remaining_string, parser):
        i_start_tag = remaining_string.find('<')
        i_end_tag = remaining_string.find('>')
        assert remaining_string[i_start_tag + 1] == '/'
        tag_name = remaining_string[i_start_tag + 2 : i_end_tag]
        assert tag_name == parser.current_node.tag_name
        parser.current_node = parser.current_node.parent #closing a tag so switch back to parent
        parser.state = RouterState()
        return remaining_string[i_end_tag + 1:].strip()


class TagTextState(object):
    '''
    '''
    def process(self, remaining_string, parser):
        i_start_tag = remaining_string.find('<')
        text = remaining_string[:i_start_tag]
        parser.current_node.text = text
        parser.state = RouterState()
        return remaining_string[i_start_tag:]


class RouterState(object):
    '''
    State that determines which state to switch to next.
    All states switch to this state once they finish their tasks.
    Then this states decides which one of those to move to next.
    This state does not actually extract parts of the string.
    '''
    def process(self, remaining_string, parser):
        stripped = remaining_string.strip()
        if stripped.startswith('</'):
            parser.state = TagCloseState()
        elif stripped.startswith('<'):
            parser.state = TagOpenState()
        else:
            parser.state = TagTextState()  
            
        return stripped

