r"""
 __  __                           _
|  \/  | ___ _ __ ___   ___  _ __(_)
| |\/| |/ _ \ '_ ` _ \ / _ \| '__| |
| |  | |  __/ | | | | | (_) | |  | |
|_|  |_|\___|_| |_| |_|\___|_|  |_|
                  perfectam memoriam
                         by GibsonAI
                       memorilabs.ai
"""

migrations = {
    1: [
        {
            "description": "create collection memori_schema_version",
            "operation": """
db['memori_schema_version'].create_index([('num', 1)], unique=True)
            """,
        },
        {
            "description": "create collection memori_parent",
            "operation": """
db['memori_parent'].create_index([('external_id', 1)], unique=True)
db['memori_parent'].create_index([('uuid', 1)], unique=True)
            """,
        },
        {
            "description": "create collection memori_process",
            "operation": """
db['memori_process'].create_index([('external_id', 1)], unique=True)
db['memori_process'].create_index([('uuid', 1)], unique=True)
            """,
        },
        {
            "description": "create collection memori_session",
            "operation": """
db['memori_session'].create_index([('uuid', 1)], unique=True)
db['memori_session'].create_index([('parent_id', 1), ('_id', 1)], unique=True, sparse=True)
db['memori_session'].create_index([('process_id', 1), ('_id', 1)], unique=True, sparse=True)
            """,
        },
        {
            "description": "create collection memori_conversation",
            "operation": """
db['memori_conversation'].create_index([('session_id', 1)], unique=True)
db['memori_conversation'].create_index([('uuid', 1)], unique=True)
            """,
        },
        {
            "description": "create collection memori_conversation_message",
            "operation": """
db['memori_conversation_message'].create_index([('uuid', 1)], unique=True)
db['memori_conversation_message'].create_index([('conversation_id', 1), ('_id', 1)], unique=True)
            """,
        },
    ]
}
