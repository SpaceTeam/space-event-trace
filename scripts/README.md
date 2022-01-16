# Scripts

Here are some scripts used in development, they are not part of the server per
se.

All sql scripts can be inserted with [`sqlite3`](https://sqlite.org/cli.html).

**TIPP:** When working on the production database, please for the love of
satan **user transactions**!
([Obligatory Tom Scott Video](https://www.youtube.com/watch?v=X6NJkWbM1xk))

Example of how to responsible work in production:

```bash
$ sqlite3 instance/trace.db
sqlite> .changes on
sqlite> BEGIN;
changes:   0   total_changes: 0
sqlite> UPDATE users
   ...> SET vaccinated_till = date(vaccinated_till, '-90 days')
   ...> WHERE vaccinated_till NOT NULL;
changes:  24   total_changes: 24
sqlite> ROLLBACK; --or COMMIT; if you want to keep the changes.
changes:  24   total_changes: 24
sqlite> ^D
$
```

## migrate_db.sql
`space-event-trace` is a weird fork of 
[`space-trace`](https://github.com/SpaceTeam/space-trace).
As such we have the possibility to reuse the db of space-trace so that users 
who uploaded their vaccine certificate there don't have to reupload it here.

However, the db schema is slightly different and this script adapts it from
`space-trace` to `space-event-trace`.

## decrement_dates.sql

This sql statement decrements the expiration dates of all vaccines in case
the government changes those dates.
sudo 

## flask create-db
The create db will create enough seats (as specified in the config).

## reset_visits.sql
Deletes all visits and resets the seats.