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
            "operations": [
                {
                    "collection": "memori_schema_version",
                    "method": "create_index",
                    "args": [[("num", 1)]],
                    "kwargs": {"unique": True},
                },
            ],
        },
        {
            "description": "create collection memori_parent",
            "operations": [
                {
                    "collection": "memori_parent",
                    "method": "create_index",
                    "args": [[("external_id", 1)]],
                    "kwargs": {"unique": True},
                },
                {
                    "collection": "memori_parent",
                    "method": "create_index",
                    "args": [[("uuid", 1)]],
                    "kwargs": {"unique": True},
                },
            ],
        },
        {
            "description": "create collection memori_process",
            "operations": [
                {
                    "collection": "memori_process",
                    "method": "create_index",
                    "args": [[("external_id", 1)]],
                    "kwargs": {"unique": True},
                },
                {
                    "collection": "memori_process",
                    "method": "create_index",
                    "args": [[("uuid", 1)]],
                    "kwargs": {"unique": True},
                },
            ],
        },
        {
            "description": "create collection memori_session",
            "operations": [
                {
                    "collection": "memori_session",
                    "method": "create_index",
                    "args": [[("uuid", 1)]],
                    "kwargs": {"unique": True},
                },
                {
                    "collection": "memori_session",
                    "method": "create_index",
                    "args": [[("parent_id", 1), ("_id", 1)]],
                    "kwargs": {"unique": True, "sparse": True},
                },
                {
                    "collection": "memori_session",
                    "method": "create_index",
                    "args": [[("process_id", 1), ("_id", 1)]],
                    "kwargs": {"unique": True, "sparse": True},
                },
            ],
        },
        {
            "description": "create collection memori_conversation",
            "operations": [
                {
                    "collection": "memori_conversation",
                    "method": "create_index",
                    "args": [[("session_id", 1)]],
                    "kwargs": {"unique": True},
                },
                {
                    "collection": "memori_conversation",
                    "method": "create_index",
                    "args": [[("uuid", 1)]],
                    "kwargs": {"unique": True},
                },
            ],
        },
        {
            "description": "create collection memori_conversation_message",
            "operations": [
                {
                    "collection": "memori_conversation_message",
                    "method": "create_index",
                    "args": [[("uuid", 1)]],
                    "kwargs": {"unique": True},
                },
                {
                    "collection": "memori_conversation_message",
                    "method": "create_index",
                    "args": [[("conversation_id", 1), ("_id", 1)]],
                    "kwargs": {"unique": True},
                },
            ],
        },
    ]
}
