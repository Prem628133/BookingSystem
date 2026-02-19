# Docker Commands
up:
	docker compose up

down:
	docker compose down

build:
	docker compose build

rebuild:
	docker compose down -v
	docker compose up --build

logs:
	docker compose logs -f

# Django Commands
migrate:
	docker compose exec web python manage.py migrate

makemigrations:
	docker compose exec web python manage.py makemigrations

createsuperuser:
	docker compose exec web python manage.py createsuperuser

shell:
	docker compose exec web python manage.py shell

# Cleanup
clean:
	docker compose down -v
	docker system prune -f
