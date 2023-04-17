import numpy as np
from node import Node
import graphviz as gpz
# from subprocess import check_call

class DecisionTreeVisualizer:
    def __init__(self, node:Node, columns_names:np.ndarray=None):
        self.node = node
        self.columns_names = columns_names
        self.nodes_dict = {}
        
        self.graph:gpz.graphs.Digraph = None
        
    
    def visualize_tree(self):
        if not self.nodes_dict:
            self._build_dict(self.node)
        
        dt_graph = gpz.Digraph(name="Decision Tree", 
                               node_attr={'shape': 'box'},
                               format='png')
        
        for node, children in self.nodes_dict.items():
            node_name = None
            
            if self.columns_names is not None:
                node_name = f'feature="{self.columns_names[node.feature_idx]}", threshold={node.threshold}'
            else:
                node_name = str(node)
                
            dt_graph.node(node.node_id, label=node_name)
                
            for child in children:
                child_name = None
                
                if (self.columns_names is not None) and (not child.is_leaf_node()):
                    child_name = f'feature="{self.columns_names[child.feature_idx]}", threshold={child.threshold}'
                    dt_graph.node(child.node_id, label=child_name)
                    dt_graph.edge(node.node_id, child.node_id)
                else:
                    child_name = str(child)
                    dt_graph.node(child.node_id, label=child_name)
                    dt_graph.edge(node.node_id, child.node_id)
                    
        self.graph = dt_graph
                    
        return self.graph
    
    
    def save(self, file_name:str=None, directory:str=None, format='png', view=False):
        if self.graph is None:
            raise Exception("The Tree hasn't been visualized. Run the method visualize_tree() first.")
        elif filename is None:
            raise Exception("The filename should be provided.")
        else:
            directory = '' if directory is None else directory
            
            self.graph.render(filename=file_name, 
                              directory=directory, 
                              format=format, 
                              view=view).replace('\\', '/')
            
            # source = f"{file_name}.dot"
            # self.graph.save(filename=f'{source}', directory=f'{directory}')
            # if directory:
            #     check_call(['dot','-Tpng',f'{directory}/{source}','-o', f'{directory}/{file_name}.png'])
            # else:
            #     check_call(['dot','-Tpng',f'{source}','-o', f'{file_name}.png'])
            
    
    def _build_dict(self, node:Node):
        children = [node.left, node.right]
        children = [child for child in children if child]
        # children = [child for child in children if (child.has_children() or child.is_leaf_node())]
        
        if children:
            self.nodes_dict[node] = children
        
        for child in children:
            if (not child.is_leaf_node()) and child.has_children():
                self._build_dict(child)
            