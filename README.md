# Reflex-GPT

> A full-stack ChatGPT-like application built with Python, Reflex, Neon Postgres, and Docker

## Overview

Reflex-GPT is a modern, responsive web application that demonstrates how to build production-ready AI applications using Python and the Reflex framework. This project integrates OpenAI's GPT API, PostgreSQL database with Neon, and Docker containerization for seamless deployment.

## Features

- **Frontend & Backend in Python**: Entire application written in Python using Reflex framework
- **Real-time Chat Interface**: Responsive UI with real-time message streaming
- **Database Integration**: PostgreSQL integration using Neon for scalable storage
- **AI-Powered Responses**: OpenAI API integration for intelligent responses
- **Docker Ready**: Complete Docker setup for easy deployment
- **Responsive Design**: Mobile-friendly interface with adaptive layouts
- **Session Management**: Track conversation history and manage multiple sessions

## Tech Stack

- **Frontend Framework**: [Reflex](https://reflex.dev/) - The Python Web Framework
- **Backend**: Python with Reflex Server
- **Database**: PostgreSQL via [Neon](https://neon.tech/)
- **ORM**: SQLModel for database operations
- **AI API**: OpenAI GPT Models
- **Containerization**: Docker & Docker Compose
- **Deployment**: GitHub Actions with Ansible

## Project Structure

```
reflex-gpt/
├── reflex_gpt/
│   ├── __init__.py
│   ├── reflex_gpt.py          # Main application file
│   ├── pages/                 # Page components
│   │   ├── __init__.py
│   │   ├── home.py            # Home page
│   │   └── about.py           # About page
│   ├── ui/                    # Reusable UI components
│   │   ├── __init__.py
│   │   ├── base.py            # Base layout component
│   │   ├── navbar.py          # Navigation bar
│   │   └── footer.py          # Footer component
│   └── navigation/            # Navigation configuration
│       ├── __init__.py
│       └── routes.py          # Route definitions
├── rxconfig.py                # Reflex configuration
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker configuration
├── docker-compose.yml         # Docker Compose setup
└── README.md                  # This file
```

## Getting Started

### Prerequisites

- Python 3.11+
- Virtual Environment (venv, poetry, or similar)
- Docker (optional, for containerized deployment)
- OpenAI API Key
- Neon PostgreSQL credentials

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sourabh-Narvariya/reflex-gpt.git
   cd reflex-gpt
   ```

2. **Create virtual environment**
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```
   Update `.env` with your credentials:
   ```
   OPENAI_API_KEY=your_openai_key
   DATABASE_URL=postgresql://user:password@host/dbname
   ```

5. **Run the application**
   ```bash
   reflex run
   ```
   Visit `http://localhost:3000`

### Docker Deployment

1. **Build Docker image**
   ```bash
   docker build -t reflex-gpt:latest .
   ```

2. **Run with Docker Compose**
   ```bash
   docker-compose up
   ```

## Usage

### Starting a Chat

1. Navigate to the home page
2. Type your message in the chat input
3. Submit to receive AI-powered responses
4. Responses are saved to your chat history
5. Create new chat sessions as needed

### Navigation

- **Home**: Main chat interface
- **About**: Project information and developer details
- **Chat Sessions**: View and manage conversation history

## Key Components

### UI Components
- **Base Layout**: Reusable container with navbar and footer
- **Navigation Bar**: Responsive menu with routing
- **Chat Interface**: Real-time message display and input
- **Session Manager**: Handle multiple conversations

### Backend Features
- **State Management**: Reflex state for reactive updates
- **Database Models**: SQLModel schemas for users and messages
- **API Integration**: OpenAI API wrapper
- **Route Handling**: URL-based page routing

## Configuration

### Reflex Configuration (`rxconfig.py`)
Configure app name, database connection, API endpoints:
```python
config = rx.Config(
    app_name="reflex_gpt",
    db_url="sqlite:///reflex.db",  # or PostgreSQL URL
)
```

### Environment Setup
Create `.env` file with required variables:
- `OPENAI_API_KEY`
- `DATABASE_URL`
- `APP_SECRET_KEY`

## Development

### Running in Development Mode
```bash
reflex run --loglevel debug
```

### Hot Reload
Reflex automatically reloads when you modify files.

### Database Migrations
```bash
reflex db migrate
```

## Deployment

### Deploy to VM with Docker
1. Push to GitHub
2. GitHub Actions builds and pushes to registry
3. Ansible deploys to VM
4. Application runs in Docker container

### Deploy to Cloud (Vercel, Render, Railway)
Reflex provides built-in deployment options. See [Reflex Deployment Docs](https://reflex.dev/docs/deployment/)

## Performance Optimization

- **Lazy Loading**: Load pages on-demand
- **Database Indexing**: Optimize queries for chat history
- **Caching**: Cache frequently accessed data
- **Connection Pooling**: Manage database connections efficiently

## Security Considerations

- Store API keys in environment variables
- Use HTTPS for all connections
- Validate user inputs
- Implement rate limiting for API calls
- Regular security updates for dependencies

## Troubleshooting

### Common Issues

**Issue**: Database connection failed
- Check `DATABASE_URL` in environment
- Verify Neon credentials
- Ensure PostgreSQL server is running

**Issue**: OpenAI API errors
- Verify API key is valid
- Check rate limits
- Monitor API usage

**Issue**: Reflex not starting
- Clear cache: `rm -rf .web`
- Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`
- Check Python version (3.11+)

## Learning Resources

- [Reflex Documentation](https://reflex.dev/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Neon PostgreSQL Documentation](https://neon.tech/docs)
- [Docker Documentation](https://docs.docker.com/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## License

This project is open source and available under the MIT License.

## Author

**Sourabh Narvariya**
- GitHub: [@Sourabh-Narvariya](https://github.com/Sourabh-Narvariya)
- Email: sourabhnarvariya55@gmail.com
- Location: India
- Education: B.Tech in Computer Science and Engineering (AI Collaboration with IBM)

## Acknowledgments

- Reflex framework for providing an excellent Python web framework
- OpenAI for powerful GPT API
- Neon for serverless PostgreSQL
- Docker for containerization capabilities
- The Python and open-source communities

## Support

If you have any questions or need help:
1. Check the [troubleshooting](#troubleshooting) section
2. Review the [Reflex docs](https://reflex.dev/)
3. Open an issue on GitHub
4. Contact the author

---

**Last Updated**: December 2025
**Version**: 1.0.0
**Status**: Active Development
