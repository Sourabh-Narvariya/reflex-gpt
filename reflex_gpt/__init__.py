"""Reflex-GPT package."""

__version__ = "1.0.0"
__author__ = "Sourabh Narvariya"
__email__ = "sourabhnarvariya55@gmail.com"
__description__ = "Full-stack ChatGPT-like application built with Reflex, Neon Postgres, and Docker"

from .reflex_gpt import State, index, app

__all__ = ["State", "index", "app"]
