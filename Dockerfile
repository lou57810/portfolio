# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.12
ENV PYTHONBUFFERED 1

# Eviter les fichiers .pyc dans les containers --> ralentissements
ENV PYTHONDONTWRITEBYTECODE 1

# Mounts the application code to the image
RUN mkdir /app
COPY . app
WORKDIR /app

# Allows docker to cache installed dependencies between builds
RUN pip3 install  --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt
RUN python manage.py collectstatic --noinput

# ADD db.sqlite3 /app


EXPOSE 8000

# runs the production server
# ENTRYPOINT ["python", "mysite/manage.py"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "portfolio.wsgi:application"]
