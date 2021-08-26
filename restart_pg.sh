echo "[#] Remove migrations folders"
rm -r nplus1_nomore/*/migrations

echo "[#] Remove cache folders"
rm -r nplus1_nomore/*/__pycache__

echo "[#] Delete db folders"
sudo rm -r pg/

echo "[#] Recreate db folders"
mkdir pg

echo '[#] Starting Postgres database container: nplus1-pg...'
docker run --rm --name nplus1-pg -e POSTGRES_USER=nplus1-pg -e POSTGRES_PASSWORD=nplus1-pg -v $PWD/pg/:/var/lib/postgresql/data -d postgres:12-alpine
