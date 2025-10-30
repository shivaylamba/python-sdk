# Memori PostgreSQL Example

Production-ready example showing how to use Memori with PostgreSQL for conversation persistence.

## What This Demonstrates

- Memori integration with PostgreSQL
- SQLAlchemy ORM with connection pooling
- Production database patterns (SSL, connection management)
- Conversation persistence with attribution tracking

## Quick Start

1. **Install dependencies**:
   ```bash
   uv sync
   ```

2. **Set environment variables**:
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   export DATABASE_CONNECTION_STRING=postgresql+psycopg://user:password@localhost:5432/dbname
   ```

3. **Run the example**:
   ```bash
   uv run python main.py
   ```

## Environment Variables

- `OPENAI_API_KEY` (required) - Your OpenAI API key
- `DATABASE_CONNECTION_STRING` (required) - PostgreSQL connection string
  - Format: `postgresql+psycopg://user:password@host:port/database`
  - For SSL: Add `?sslmode=require` to the end

## Database Setup

Make sure you have a PostgreSQL database ready:

```bash
# Local PostgreSQL
createdb memori_test

# Or use a managed service (Heroku, Supabase, AWS RDS, etc.)
```

## How It Works

1. Connects to PostgreSQL with connection pooling enabled
2. Registers OpenAI client with Memori
3. Configures attribution with `parent_id` (user) and `process_id` (bot/session)
4. Builds Memori schema automatically
5. Runs interactive chat loop where all messages are persisted
6. Commits after each interaction to save conversation history

## Connection Pooling

This example uses SQLAlchemy's connection pooling with:
- `pool_pre_ping=True` - Validates connections before use
- Automatic connection recycling
- Proper session management with try/finally

## What Gets Persisted

Memori automatically stores:
- User messages
- Assistant responses
- Conversation context
- Attribution metadata (parent_id, process_id)
- Timestamps and other metadata

## Production Considerations

- Use SSL connections for production (`?sslmode=require`)
- Set appropriate connection pool sizes
- Configure database timeouts
- Use environment-specific credentials
- Monitor database connections

## Next Steps

- Query the database to see stored conversations
- Modify `parent_id` and `process_id` to track different users/sessions
- Explore other database examples (SQLite, MongoDB, CockroachDB)
