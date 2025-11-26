#!/bin/bash

# Create directories
mkdir -p starter/.github/workflows
mkdir -p starter/config
mkdir -p starter/src/llm
mkdir -p starter/src/content/services
mkdir -p starter/src/content/prompt_engineering
mkdir -p starter/src/content/processors
mkdir -p starter/src/calibration/services
mkdir -p starter/src/images/services
mkdir -p starter/src/images/providers
mkdir -p starter/src/seo/services
mkdir -p starter/src/utils
mkdir -p starter/src/handlers
mkdir -p starter/data/cache
mkdir -p starter/data/prompts/v1
mkdir -p starter/data/prompts/v2
mkdir -p starter/data/outputs
mkdir -p starter/data/embeddings
mkdir -p starter/examples
mkdir -p starter/notebooks
mkdir -p starter/tests/content
mkdir -p starter/tests/images
mkdir -p starter/tests/seo
mkdir -p starter/tests/integration
mkdir -p starter/scripts
mkdir -p starter/docker
mkdir -p starter/ansible/inventory
mkdir -p starter/ansible/playbooks

# Create placeholder files
touch starter/.github/workflows/build.yml
touch starter/.github/workflows/test.yml
touch starter/.github/workflows/deploy.yml

touch starter/config/__init__.py
touch starter/config/settings.py
touch starter/config/model_config.yaml
touch starter/config/prompt_templates.yaml
touch starter/config/logging_config.yaml

touch starter/src/__init__.py
touch starter/src/main.py
touch starter/src/celery_app.py
touch starter/src/database.py
touch starter/src/dependencies.py

touch starter/src/llm/__init__.py
touch starter/src/llm/base.py
touch starter/src/llm/factory.py
touch starter/src/llm/openai_client.py
touch starter/src/llm/anthropic_client.py
touch starter/src/llm/ollama_client.py

touch starter/src/content/__init__.py
touch starter/src/content/router.py
touch starter/src/content/schemas.py
touch starter/src/content/services/__init__.py
touch starter/src/content/services/generator.py
touch starter/src/content/services/article_generator.py
touch starter/src/content/services/blog_generator.py
touch starter/src/content/services/news_generator.py
touch starter/src/content/services/marketing_generator.py
touch starter/src/content/prompt_engineering/__init__.py
touch starter/src/content/prompt_engineering/base.py
touch starter/src/content/prompt_engineering/templates.py
touch starter/src/content/prompt_engineering/few_shot.py
touch starter/src/content/prompt_engineering/chainer.py
touch starter/src/content/processors/__init__.py
touch starter/src/content/processors/text_processor.py
touch starter/src/content/processors/html_formatter.py
touch starter/src/content/processors/markdown_converter.py
touch starter/src/content/tasks.py

touch starter/src/calibration/__init__.py
touch starter/src/calibration/router.py
touch starter/src/calibration/schemas.py
touch starter/src/calibration/services/__init__.py
touch starter/src/calibration/services/calibration_service.py
touch starter/src/calibration/services/tone_analyzer.py
touch starter/src/calibration/services/style_matcher.py
touch starter/src/calibration/tasks.py

touch starter/src/images/__init__.py
touch starter/src/images/router.py
touch starter/src/images/schemas.py
touch starter/src/images/services/__init__.py
touch starter/src/images/services/suggestion_service.py
touch starter/src/images/services/keyword_extractor.py
touch starter/src/images/services/relevance_scorer.py
touch starter/src/images/providers/__init__.py
touch starter/src/images/providers/base.py
touch starter/src/images/providers/unsplash.py
touch starter/src/images/providers/pexels.py
touch starter/src/images/providers/pixabay.py
touch starter/src/images/tasks.py

touch starter/src/seo/__init__.py
touch starter/src/seo/router.py
touch starter/src/seo/schemas.py
touch starter/src/seo/services/__init__.py
touch starter/src/seo/services/seo_analyzer.py
touch starter/src/seo/services/keyword_optimizer.py
touch starter/src/seo/services/meta_generator.py
touch starter/src/seo/services/readability_scorer.py
touch starter/src/seo/tasks.py

touch starter/src/utils/__init__.py
touch starter/src/utils/rate_limiter.py
touch starter/src/utils/token_counter.py
touch starter/src/utils/cache.py
touch starter/src/utils/logger.py
touch starter/src/utils/error_handler.py

touch starter/src/handlers/__init__.py
touch starter/src/handlers/error_handler.py

touch starter/examples/__init__.py
touch starter/examples/basic_generation.py
touch starter/examples/batch_generation.py
touch starter/examples/custom_calibration.py
touch starter/examples/image_suggestion.py

touch starter/tests/__init__.py
touch starter/tests/conftest.py
touch starter/tests/test_api.py
touch starter/tests/content/__init__.py
touch starter/tests/content/test_generator.py
touch starter/tests/content/test_prompts.py
touch starter/tests/content/test_processors.py
touch starter/tests/images/__init__.py
touch starter/tests/images/test_suggestion.py
touch starter/tests/seo/__init__.py
touch starter/tests/seo/test_analyzer.py
touch starter/tests/integration/__init__.py
touch starter/tests/integration/test_full_workflow.py

touch starter/scripts/start_api.sh
touch starter/scripts/start_worker.sh
touch starter/scripts/run_tests.sh
touch starter/scripts/seed_prompts.py

touch starter/docker/Dockerfile.api
touch starter/docker/Dockerfile.worker
touch starter/docker/docker-compose.yml

touch starter/ansible/inventory/production
touch starter/ansible/inventory/staging
touch starter/ansible/playbooks/deploy.yml
touch starter/ansible/playbooks/rollback.yml

touch starter/.env.example
touch starter/.dockerignore
touch starter/.gitignore
touch starter/requirements.txt
touch starter/requirements-dev.txt
touch starter/pyproject.toml
touch starter/setup.py
touch starter/pytest.ini
touch starter/README.md
touch starter/CHANGELOG.md

echo "Template generated successfully!"
