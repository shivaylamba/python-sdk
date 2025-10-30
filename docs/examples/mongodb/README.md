# Memori MongoDB Example

Example showing how to use Memori with MongoDB for flexible, document-based conversation persistence.

## What This Demonstrates

- Memori integration with MongoDB (NoSQL document database)
- MongoDB Atlas cloud connection
- Document-based message storage
- Schema-less persistence for flexible data models
- PyMongo driver usage

## Quick Start

1. **Install dependencies**:
   ```bash
   uv sync
   ```

2. **Set environment variables**:
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   export MONGODB_CONNECTION_STRING=mongodb+srv://user:password@cluster.mongodb.net/dbname
   ```

3. **Run the example**:
   ```bash
   uv run python main.py
   ```

## Environment Variables

- `OPENAI_API_KEY` (required) - Your OpenAI API key
- `MONGODB_CONNECTION_STRING` (required) - MongoDB connection string
  - Format: `mongodb+srv://user:password@cluster.mongodb.net/database`
  - Can also use local: `mongodb://localhost:27017/database`
- `MONGODB_DATABASE` (optional) - Database name if not specified in URL (defaults to `memori`)

## Database Setup

### MongoDB Atlas (Cloud)

1. Create a free cluster at [mongodb.com/cloud/atlas](https://www.mongodb.com/cloud/atlas)
2. Create a database user with read/write permissions
3. Whitelist your IP address (or use 0.0.0.0/0 for development)
4. Get the connection string from the Atlas dashboard

### Local MongoDB

```bash
# Install MongoDB
brew install mongodb-community  # macOS
# or download from mongodb.com

# Start MongoDB
brew services start mongodb-community

# Connection string
export MONGODB_CONNECTION_STRING=mongodb://localhost:27017/memori
```

## How It Works

1. Connects to MongoDB cluster using PyMongo
2. Verifies connection with a ping command
3. Registers OpenAI client with Memori
4. Configures attribution with `parent_id` (user) and `process_id` (bot/session)
5. Builds Memori collections automatically
6. Runs interactive chat loop where all messages are persisted as documents
7. No explicit commits needed - MongoDB writes are immediate

## Why MongoDB?

- **Flexible schema**: Store arbitrary JSON structures
- **Document model**: Natural fit for conversation data
- **Scalable**: Easy horizontal scaling with sharding
- **Rich queries**: Powerful aggregation and query capabilities
- **Cloud-native**: Fully managed with MongoDB Atlas

## What Gets Persisted

Memori automatically stores:
- User messages (as JSON documents)
- Assistant responses
- Conversation context
- Attribution metadata (parent_id, process_id)
- Timestamps and other metadata

All data is stored in flexible JSON document format.

## Document Structure

Each message is stored as a document with fields like:
```json
{
  "_id": "...",
  "role": "user",
  "content": "Hello!",
  "parent_id": "12345",
  "process_id": "my-ai-bot",
  "timestamp": "2024-01-01T00:00:00Z",
  ...
}
```

## Production Considerations

- Use connection string with authentication in production
- Enable SSL/TLS for secure connections
- Configure appropriate read/write concerns
- Set up indexes for common query patterns
- Monitor database performance with Atlas monitoring
- Set up automated backups (included in Atlas)

## Next Steps

- Check MongoDB Atlas (or Compass) to see stored documents
- Modify `parent_id` and `process_id` to track different users/sessions
- Query conversations using MongoDB's rich query language
- Explore other database examples (SQLite, PostgreSQL, CockroachDB)
