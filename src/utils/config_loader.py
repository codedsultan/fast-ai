import yaml
from pathlib import Path
from functools import lru_cache
from typing import Any, Dict


# =========
# File paths
# =========
BASE_DIR = Path(__file__).resolve().parent.parent.parent  # repo root

MODEL_CONFIG_PATH = BASE_DIR / "config" / "model_config.yaml"
PROMPT_TEMPLATES_PATH = BASE_DIR / "config" / "prompt_templates.yaml"


# =========
# YAML Loader
# =========
def load_yaml(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    with open(path, "r") as file:
        return yaml.safe_load(file)


# ==============================
# Cached config getters (fast)
# ==============================

@lru_cache(maxsize=1)
def get_model_config() -> Dict[str, Any]:
    """
    Returns model_config.yaml as a dict.
    Cached to avoid repeated disk reads.
    """
    return load_yaml(MODEL_CONFIG_PATH)


@lru_cache(maxsize=1)
def get_prompt_templates() -> Dict[str, Any]:
    """
    Returns prompt_templates.yaml as a dict.
    Cached for performance.
    """
    return load_yaml(PROMPT_TEMPLATES_PATH)


# ==============================
# Helper API Functions
# ==============================

def get_default_provider() -> str:
    """
    Returns default LLM provider (openai, anthropic, ollama).
    """
    config = get_model_config()
    return config.get("default_provider", "openai")


def get_provider_settings(provider: str = None) -> Dict[str, Any]:
    """
    Returns settings for a given provider.
    If no provider is given, returns default provider settings.
    """
    config = get_model_config()

    if provider is None:
        provider = config.get("default_provider", "openai")

    providers = config.get("providers", {})

    if provider not in providers:
        raise ValueError(f"Unknown LLM provider: {provider}")

    return providers[provider]


def get_prompt_template(group: str, template: str) -> str:
    """
    Retrieve a specific template from prompt_templates.yaml.

    Example:
        get_prompt_template("content_generation", "base_template")
    """
    templates = get_prompt_templates()

    if group not in templates:
        raise ValueError(f"Template group '{group}' not found.")

    if template not in templates[group]:
        raise ValueError(f"Template '{template}' not found in group '{group}'.")

    return templates[group][template]
