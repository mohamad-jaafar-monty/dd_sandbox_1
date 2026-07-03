"""Intentionally vulnerable code - SAST test fodder for DevDox.

Every finding here is deliberate. This is a sandbox project used to
verify that SonarCloud (MQR taxonomy) reports Security / Reliability /
Maintainability issues and that DevDox renders them. Do not deploy.
"""
import os
import pickle
import sqlite3

import requests

# --- Security: hardcoded credentials (python:S2068) ---
DB_PASSWORD = "SuperSecret_p4ssw0rd!"
API_TOKEN = "ghp_0123456789abcdefghijklmnopqrstuvwxyz"

# --- Security: hardcoded IP address (python:S1313) ---
INTERNAL_HOST = "10.0.14.22"


def get_user(conn: sqlite3.Connection, user_id: str):
    # --- Security: SQL injection (python:S3649) ---
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = '" + user_id + "'")
    return cursor.fetchone()


def call_internal_api(path: str):
    # --- Security: TLS verification disabled (python:S4830) ---
    return requests.get(f"https://{INTERNAL_HOST}/{path}", verify=False, timeout=5)


def load_session(blob: bytes):
    # --- Security: unsafe deserialization (python:S5445 family) ---
    return pickle.loads(blob)


# ---- Below: attack surface NOT present in the original dd_sandbox ----


def run_report(report_name: str):
    # --- Security: OS command injection (python:S4721) ---
    os.system("generate_report " + report_name)


def read_upload(filename: str):
    # --- Security: path traversal (python:S2083) ---
    with open("/var/uploads/" + filename, encoding="utf-8") as handle:
        return handle.read()


def fetch(url: str):
    # --- Security: SSRF - server fetches a caller-controlled URL (python:S5144) ---
    return requests.get(url, timeout=5).text
