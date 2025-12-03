# Contributing to Reflex-GPT

Thank you for your interest in contributing to Reflex-GPT! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Use clear and concise communication
- Report issues responsibly
- Follow best practices and project guidelines

## How to Contribute

### 1. Fork and Clone

```bash
git clone https://github.com/YOUR_USERNAME/reflex-gpt.git
cd reflex-gpt
```

### 2. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 3. Development Setup

```bash
python3.11 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
reflex run
```

## Coding Standards

### Python Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use type hints for all functions
- Write docstrings for all modules, classes, and functions
- Maximum line length: 99 characters

### Example Code

```python
from typing import Optional

def process_message(content: str, max_length: int = 1000) -> Optional[str]:
    """Process a message with length validation.
    
    Args:
        content: The message content to process
        max_length: Maximum allowed message length
        
    Returns:
        Processed message or None if validation fails
    """
    if not content or len(content) > max_length:
        return None
    return content.strip()
```

## Commit Messages

Use conventional commits format:

```
<type>: <subject>

<body>

<footer>
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`, `ci`, `devops`

Examples:
- `feat: Add user authentication module`
- `fix: Resolve OpenAI API timeout issue`
- `docs: Update installation instructions`
- `test: Add unit tests for utils module`

## Pull Request Process

1. **Update README.md** if needed with new features
2. **Add/Update Tests** for your changes
3. **Run Tests** locally to ensure they pass
4. **Update CHANGELOG** if applicable
5. **Submit PR** with clear description

## Testing

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_models.py

# With coverage
pytest --cov=reflex_gpt
```

## Code Review

- Respond to review comments promptly
- Be open to suggestions
- Ask for clarification if needed
- Update code based on feedback

## Documentation

- Update docstrings for modified functions
- Add comments for complex logic
- Keep README.md current
- Document new features

## Reporting Issues

When reporting bugs, include:

- Python version and OS
- Detailed steps to reproduce
- Expected vs actual behavior
- Error messages and stack traces
- Your environment setup

## Feature Requests

- Clearly describe the feature
- Explain the use case
- Provide examples if possible
- Discuss implementation approach

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

Feel free to:
- Open an issue for discussions
- Email the maintainers
- Check existing documentation

## Thank You!

Your contributions make Reflex-GPT better for everyone!
