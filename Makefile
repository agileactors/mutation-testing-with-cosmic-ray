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
