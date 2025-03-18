
class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        props_as_html = ""
        prop_keys = self.props.keys()
        
        for key in prop_keys:
            props_as_html += f" {key}=\"{self.props[key]}\"" 
        
        print(f"TEST: {props_as_html}")
        return props_as_html
    
