# Memori SQLite Example

A minimal example showing how to use Memori with SQLite for local conversation persistence.

## What This Demonstrates

- Basic Memori integration with a local SQLite database
- Automatic schema creation and management
- Conversation persistence with attribution tracking
- SQLAlchemy ORM session management

## Quick Start

1. **Install dependencies**:
   ```bash
   uv sync
   ```

2. **Set environment variables**:
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

3. **Run the example**:
   ```bash
   uv run python main.py
   ```

## Environment Variables

- `OPENAI_API_KEY` (required) - Your OpenAI API key
- `SQLITE_DB_PATH` (optional) - Path to SQLite database file (defaults to `./memori.sqlite`)

## How It Works

1. Connects to a local SQLite database (creates if doesn't exist)
2. Registers OpenAI client with Memori
3. Configures attribution with `parent_id` (user) and `process_id` (bot/session)
4. Builds Memori schema automatically
5. Runs interactive chat loop where all messages are persisted
6. Commits after each interaction to save conversation history

## What Gets Persisted

Memori automatically stores:
- User messages
- Assistant responses
- Conversation context
- Attribution metadata (parent_id, process_id)
- Timestamps and other metadata

## Next Steps

- Check out the generated `memori.sqlite` database to see stored conversations
- Modify `parent_id` and `process_id` to track different users/sessions
- Explore other database examples (PostgreSQL, MongoDB, CockroachDB)
