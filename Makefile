unit:
	python -m pytest -v -s test --no-header -vv --cov=src --cov-report=term-missing

mutation:
	echo "Initialising mutation sqlite database"
	cosmic-ray init cosmic_ray_config.toml cosmic_ray.sqlite

	echo "Excluding Operators"
	cr-filter-operators cosmic_ray.sqlite cosmic_ray_config.toml

	echo "Running baseline tests"
	cosmic-ray --verbosity=ERROR baseline cosmic_ray_config.toml

	echo "Running mutation tests"
	cosmic-ray exec cosmic_ray_config.toml cosmic_ray.sqlite

	echo "Mutation tests finished"
	cr-report cosmic_ray.sqlite --show-pending

mutation-multiple-workers:
	echo "Initialising mutation workers container"
	docker-compose -f docker-compose-mutation-workers.yaml up -d

	echo "Initialising mutation sqlite database"
	cosmic-ray init cosmic_ray_config_multiple_workers.toml cosmic_ray_multiple_workers.sqlite

	echo "Excluding Operators"
	cr-filter-operators cosmic_ray_multiple_workers.sqlite cosmic_ray_config_multiple_workers.toml

	echo "Running baseline tests"
	cosmic-ray --verbosity=ERROR baseline cosmic_ray_config_multiple_workers.toml

	echo "Running mutation tests"
	cosmic-ray exec cosmic_ray_config_multiple_workers.toml cosmic_ray_multiple_workers.sqlite

	echo "Mutation tests finished"
	cr-report cosmic_ray_multiple_workers.sqlite --show-pending

	echo "Stopping mutation workers container"
	docker-compose -f docker-compose-mutation-workers.yaml down -v