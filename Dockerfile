FROM python:3.9 AS base

FROM base AS python-base

# Install pipenv and compilation dependencies
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Install python dependencies in /.venv
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy


FROM base as runtime

# Copy virtual env from python-base stage
COPY --from=python-base /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

# Create and switch to a new user
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

# Install application into container
COPY . .

# Run the application

EXPOSE 8000

ENTRYPOINT ["python", "manage.py", "runserver","0.0.0.0:8000","--noreload"]