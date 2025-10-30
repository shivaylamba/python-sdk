# Memori CockroachDB Example

Example showing how to use Memori with CockroachDB for distributed, resilient conversation persistence.

## What This Demonstrates

- Memori integration with CockroachDB (distributed SQL)
- Raw psycopg2 driver usage (no ORM)
- SSL-enabled production connections
- Message persistence across distributed database nodes
- Automatic replication and consistency

## Quick Start

1. **Install dependencies**:
   ```bash
   uv sync
   ```

2. **Set environment variables**:
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   export COCKROACH_CONNECTION_STRING=postgresql://user:password@host:26257/defaultdb?sslmode=require
   ```

3. **Run the example**:
   ```bash
   uv run python main.py
   ```

## Environment Variables

- `OPENAI_API_KEY` (required) - Your OpenAI API key
- `COCKROACH_CONNECTION_STRING` (required) - CockroachDB connection string
  - Format: `postgresql://user:password@host:26257/database?sslmode=require`
  - Note: CockroachDB uses PostgreSQL wire protocol

## Database Setup

### CockroachDB Cloud

1. Create a free cluster at [cockroachlabs.cloud](https://cockroachlabs.cloud)
2. Download the CA certificate if required
3. Get the connection string from the cloud console

### Local CockroachDB

```bash
# Start a local single-node cluster
cockroach start-single-node --insecure --listen-addr=localhost:26257

# Create a database
cockroach sql --insecure -e "CREATE DATABASE memori_test"
```

## How It Works

1. Connects to CockroachDB cluster using psycopg2
2. Verifies connection with a test query (`SELECT now()`)
3. Registers OpenAI client with Memori
4. Configures attribution with `parent_id` (user) and `process_id` (bot/session)
5. Builds Memori schema (automatically distributed across nodes)
6. Runs interactive chat loop where all messages are persisted
7. Commits after each interaction (distributed transaction)

## Why CockroachDB?

- **Distributed**: Data automatically replicated across nodes
- **Resilient**: Survives node failures without data loss
- **PostgreSQL compatible**: Uses familiar psycopg2 driver
- **Horizontally scalable**: Add nodes as your app grows
- **ACID transactions**: Strong consistency guarantees

## What Gets Persisted

Memori automatically stores:
- User messages
- Assistant responses
- Conversation context
- Attribution metadata (parent_id, process_id)
- Timestamps and other metadata

All data is automatically replicated across your CockroachDB cluster.

## Production Considerations

- Always use SSL in production (`?sslmode=require`)
- Configure appropriate replication factors
- Monitor cluster health and performance
- Use connection pooling for high-traffic applications
- Set up backups (automatic in CockroachDB Cloud)

## Next Steps

- Check CockroachDB console to see stored conversations
- Modify `parent_id` and `process_id` to track different users/sessions
- Scale your cluster by adding more nodes
- Explore other database examples (SQLite, PostgreSQL, MongoDB)
