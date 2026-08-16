# DRIQON Backend - Current Structure

## Purpose

This is an early smart-device backend. Its intended job is to manage users and
devices in PostgreSQL, and to validate Firebase ID tokens for client requests.

## Request and data flow

```text
Client
  |
  v
FastAPI application (main.py)
  |-- User CRUD routes ----> auth.py ----> PostgreSQL `users` table
  |-- Device CRUD routes --> devices.py -> PostgreSQL `devices` table
  `-- Token route ---------> firebase_config.py -> Firebase Admin SDK
```

## Files and responsibilities

| File | Current responsibility |
| --- | --- |
| `main.py` | FastAPI entry point and HTTP routes. It initializes SQL and Firebase when imported. |
| `auth.py` | Creates, looks up, lists, and deletes users. Database operations target the `users` table. |
| `devices.py` | Creates, looks up, updates, and deletes devices. Database operations target the `devices` table. |
| `sql_connection.py` | Opens a PostgreSQL connection using values in `config.py`. |
| `config.py` | Holds PostgreSQL, MQTT, and Firebase configuration values. MQTT is configured but not used. |
| `firebase_config.py` | Initializes Firebase Admin and verifies Firebase ID tokens. |
| `database.py` | Defines an empty in-memory `user` dictionary; it is imported but not functionally used. |
| `menu.py` | Older interactive command-line menu for user/device actions; it is not started by `main.py`. |
| `users.json` / `devices.json` | Sample or legacy JSON data. Only `users.json` is read by `show_all_users()`; CRUD uses PostgreSQL. |
| `Dockerfile` | Container recipe intended to expose the API on port 8000. |
| `utils.py` | Empty placeholder. |

## HTTP API currently defined

All input values are FastAPI query parameters because no request-body models are
defined yet.

| Method | Route | Behavior |
| --- | --- | --- |
| GET | `/` | Returns a greeting. |
| GET | `/HEALTH` | Returns a basic health message; it does not check SQL or Firebase connectivity. |
| POST | `/REGISTER user` | Inserts `user_id`, `user_name`, and `user_password` into `users`. |
| POST | `/FIND user` | Fetches a user by `user_id`. |
| POST | `/ DELETE User` | Deletes a user by `user_id`. |
| POST | `/REGISTER device` | Inserts a device into `devices`. |
| POST | `/device detail` | Fetches a device by `device_id`. |
| POST | `/UPDATE device` | Updates a device's type and status. |
| POST | `/DELETE device` | Deletes a device by `device_id`. |
| POST | `/verify-token` | Verifies a Firebase ID token and returns its UID and email when valid. |

## What is working by design

- SQL statements use parameter binding, avoiding direct SQL-string injection.
- The device layer supports full CRUD operations.
- The user layer supports create, find, and delete operations.
- Firebase token verification is implemented as a standalone endpoint.

## Important current gaps and blockers

1. **Application startup is currently inconsistent.** `firebase_config.py` refers
   to a credential filename that is not present in this project, while `config.py`
   refers to a different filename. Firebase initialization therefore fails unless
   the expected credential file is supplied or the code is corrected.
2. **The Docker startup command does not match this flat project layout.** It
   starts `app.main:app`, but there is no `app/` package; the application object
   is in `main.py`.
3. **`requirements.txt` is absent**, although the Dockerfile requires it to build.
4. **The database is opened three times during API import**: once by `auth.py`,
   once by `devices.py`, and once by `main.py`. Connections are global and are
   not closed or managed per request.
5. **User passwords are stored directly and returned by `SELECT *`.** There is
   no password hashing or real password verification. The token endpoint is not
   applied as protection to user or device routes.
6. **There is no schema/migration definition** for the required `users` and
   `devices` PostgreSQL tables.
7. **MQTT settings exist but no MQTT client, topic, or device-control logic uses
   them yet.**
8. **Route names contain spaces and inconsistent casing**, which makes the API
   harder for clients to use and maintain.

## Current maturity

The project is a CRUD prototype: the core SQL operations are present, but it
needs startup/configuration cleanup, dependency and schema definitions, and an
authentication/security pass before it is ready for deployment.
