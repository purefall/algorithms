def solve(tree):
    def visit(node,lo,hi):
        if node is None: return True
        value,left,right=node
        if lo is not None and value<=lo: return False
        if hi is not None and value>=hi: return False
        return visit(left,lo,value) and visit(right,value,hi)
    return visit(tree,None,None)
