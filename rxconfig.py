"""Reflex configuration file."""

import reflex as rx
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

config = rx.Config(
    app_name="reflex_gpt",
    # Database configuration
    db_url=os.getenv(
        "DATABASE_URL",
        "sqlite:///reflex.db"
    ),
    # App settings
    frontend_packages=[
        "@radix-ui/themes@^2.0.0",
    ],
    # Optimization
    compile_mode="prod",
    # Tailwind CSS configuration
    tailwind_config={
        "theme": {
            "extend": {
                "colors": {
                    "primary": "#3b82f6",
                    "secondary": "#1e293b",
                }
            }
        }
    },
    # Environment settings
    env=rx.Env.DEV,
)

# Production settings
if os.getenv("ENVIRONMENT") == "production":
    config.env = rx.Env.PROD
    config.compile_mode = "prod"
