# pagination/cursor_handler.py

def paginate(graphql_execute_fn, query, variables, data_path):
    """
    graphql_execute_fn: function(query, variables) -> response dict
    data_path: tuple path to nodes, e.g. ("assets",)
    """
    all_nodes = []
    cursor = None

    while True:
        if cursor:
            variables["after"] = cursor

        resp = graphql_execute_fn(query, variables)

        block = resp
        for key in data_path:
            block = block[key]

        nodes = block["nodes"]
        page_info = block["pageInfo"]

        all_nodes.extend(nodes)

        if not page_info.get("hasNextPage"):
            break

        cursor = page_info.get("endCursor")

    return all_nodes
