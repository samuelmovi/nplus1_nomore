echo '[#] Starting Postgres database container: nplus1-pg...'
docker run --rm --name nplus1-pg -e POSTGRES_USER=nplus1-pg -e POSTGRES_PASSWORD=nplus1-pg -v $PWD/pg/:/var/lib/postgresql/data -d postgres:12-alpine
