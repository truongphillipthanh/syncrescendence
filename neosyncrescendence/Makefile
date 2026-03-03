.PHONY: inventory check-artifact-law bootstrap-office

inventory:
	python3 operators/validators/artifact_law_inventory.py --format both

check-artifact-law:
	python3 operators/validators/artifact_law_inventory.py --format both --check

bootstrap-office:
	@test -n "$(NAME)" || (echo "usage: make bootstrap-office NAME=office-name" && exit 1)
	python3 operators/bootstrap_office.py "$(NAME)"
