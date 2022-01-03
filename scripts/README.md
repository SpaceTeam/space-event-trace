# Scripts

Here are some scripts used in development, they are not part of the server per
se.

## migrate_db.sql
`space-event-trace` is a weird fork of 
[`space-trace`](https://github.com/SpaceTeam/space-trace).
As such we have the possibility to reuse the db of space-trace so that users 
who uploaded their vaccine certificate there don't have to reupload it here.

However, the db schema is slightly different and this script addapts it from
`space-trace` to `space-event-trace`.

## decrement_dates.sql

This sql statement decrements the expiration dates of all vaccines in case
the goverment changes those dates.
