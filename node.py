from numbers import Number
import uuid

class Node:
    def __init__(self, feature_idx:int=None, 
                 threshold:Number=None, 
                 left=None, 
                 right=None, 
                 leaf_value:Number=None):
        
        self.feature_idx = feature_idx
        self.threshold = threshold
        self.left = left
        self.right = right
        self.leaf_value = leaf_value
        
        self.node_id = str(uuid.uuid4())
        
    
    def is_leaf_node(self):
        return self.leaf_value is not None
    

    def has_children(self):
        return True if (self.left or self.right) else False
    
    
    def __eq__(self, other):
        if self.is_leaf_node() and other.is_leaf_node():
            return self.node_id == other.node_id
        else:
            return (self.feature_idx == other.feature_idx) and (self.threshold == other.threshold)
        
    
    def __hash__(self):
        if self.is_leaf_node():
            return hash(self.node_id)
        else:
            return hash( (self.feature_idx, self.threshold) )
    
    
    def __str__(self):
        if self.is_leaf_node():
            return f"<leaf_value={self.leaf_value}>"
        else:
            return f"<feature_index={self.feature_idx}, threshold={self.threshold}>"
        
        
    def __repr__(self):
        if self.is_leaf_node():
            return f"<Node leaf_value={self.leaf_value}>"
        else:
            return f"<Node feature_index={self.feature_idx}, threshold={self.threshold}>"