import json
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, Optional

import yaml
from loguru import logger

# ======================================
# Base Paths
# ======================================
BASE_DIR = Path(__file__).resolve().parent.parent.parent  # repo root
CONFIG_DIR = BASE_DIR / "config"

MODEL_CONFIG_PATH = CONFIG_DIR / "model_config.yaml"
PROMPT_TEMPLATES_PATH = CONFIG_DIR / "prompt_templates.yaml"


# ======================================
# Generic YAML Loader
# ======================================
def load_yaml(path: Path) -> Dict[str, Any]:
    """
    Safely load YAML configuration file.
    """
    if not path.exists():
        logger.error(f"YAML config file not found: {path}")
        raise FileNotFoundError(f"Config file not found: {path}")

    try:
        with path.open("r", encoding="utf-8") as file:
            return yaml.safe_load(file) or {}
    except Exception as exc:
        logger.error(f"Failed to parse YAML [{path}] — {exc}")
        raise


# ======================================
# JSON Loader
# ======================================
def load_json(path: Path) -> Dict[str, Any]:
    """
    Safely load JSON configuration file.
    """
    if not path.exists():
        logger.error(f"JSON config file not found: {path}")
        raise FileNotFoundError(f"Config file not found: {path}")

    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as exc:
        logger.error(f"Failed to parse JSON [{path}] — {exc}")
        raise


# ======================================
# Generic Config Provider Loader (NEW)
# ======================================
def load_config(provider: Optional[str] = None) -> Dict[str, Any]:
    """
    Loads any config inside the ./config folder.

    Example:
        load_config("model_config")       -> config/model_config.yaml
        load_config("prompt_templates")   -> config/prompt_templates.yaml
        load_config("seo_settings")       -> config/seo_settings.json

    If provider=None, returns empty dict.
    """
    if provider is None:
        logger.warning("load_config(provider=None) → returning empty config.")
        return {}

    logger.debug(f"Loading config provider '{provider}'")

    yaml_path = CONFIG_DIR / f"{provider}.yaml"
    yml_path = CONFIG_DIR / f"{provider}.yml"
    json_path = CONFIG_DIR / f"{provider}.json"

    if yaml_path.exists():
        return load_yaml(yaml_path)
    if yml_path.exists():
        return load_yaml(yml_path)
    if json_path.exists():
        return load_json(json_path)

    logger.error(f"No configuration file found for provider '{provider}'")
    raise FileNotFoundError(f"No configuration file found for provider: {provider}")


# ======================================
# Cached Specific Config Getters
# ======================================


@lru_cache(maxsize=1)
def get_model_config() -> Dict[str, Any]:
    """Cached YAML config for all LLM providers."""
    return load_yaml(MODEL_CONFIG_PATH)


@lru_cache(maxsize=1)
def get_prompt_templates() -> Dict[str, Any]:
    """Cached YAML templates."""
    return load_yaml(PROMPT_TEMPLATES_PATH)


# ======================================
# High-Level Helper API Functions
# ======================================


def get_default_provider() -> str:
    """
    Returns the default provider as declared in model_config.yaml.
    """
    config = get_model_config()
    return config.get("default_provider", "openai")


def get_provider_settings(provider: Optional[str] = None) -> Dict[str, Any]:
    """
    Returns configuration block for a specific LLM provider.
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
    Retrieve a specific prompt template from prompt_templates.yaml
    """
    templates = get_prompt_templates()

    if group not in templates:
        raise ValueError(f"Template group '{group}' not found.")

    if template not in templates[group]:
        raise ValueError(f"Template '{template}' not found in group '{group}'.")

    return templates[group][template]
