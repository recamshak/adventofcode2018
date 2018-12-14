import sys

def parse_tree(input):
    n_children = next(input)
    n_metadata = next(input)
    return (
        [parse_tree(input) for _ in range(n_children)],
        [next(input) for _ in range(n_metadata)]
    )

def sum_meta_data(tree):
    children, metadata = tree
    return sum(metadata) + sum(sum_meta_data(child) for child in children)

def node_value(tree):
    children, metadata = tree
    if len(children) == 0:
        return sum(metadata)
    else:
        children_idx = (idx - 1 for idx in metadata if 1 <= idx <= len(children))
        return sum(node_value(children[child_idx]) for child_idx in children_idx)

input = map(int, sys.stdin.read().split())
tree = parse_tree(input)
print(sum_meta_data(tree))
print(node_value(tree))
