import json
def query(client, query: str, op_name: str = None, input: dict = None):
    '''
    Args:
        query (string) - GraphQL query to run
        op_name (string) - If the query is a mutation or named query, you must
                            supply the op_name.  For annon queries ("{ ... }"),
                            should be None (default).
        input (dict) - If provided, the $input variable in GraphQL will be set
                        to this value

    Returns:
        dict, response from graphql endpoint.  The response has the "data" key.
                It will have the "error" key if any error happened.
    '''
    body = {'query': query}
    if op_name:
        body['operation_name'] = op_name
    if input:
        body['variables'] = {'input': input}

    resp = client.post('/graphql', json.dumps(body), content_type='application/json')
    jresp = json.loads(resp.content.decode())
    return jresp