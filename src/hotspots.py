"""Intentional Security Hotspots - SAST test fodder. Do not deploy."""
import hashlib
import random
import subprocess

from flask import Flask

app = Flask(__name__)


def fingerprint(data: str) -> str:
    # --- Hotspot: weak hash for security context (python:S4790) ---
    return hashlib.md5(data.encode()).hexdigest()


def evaluate(expr: str):
    # --- Hotspot: dynamic code execution (python:S1523) ---
    return eval(expr)  # noqa


def ping(host: str):
    # --- Hotspot: subprocess with shell=True (python:S4721) ---
    return subprocess.call("ping -c1 " + host, shell=True)


def make_reset_token() -> str:
    # --- Hotspot: non-cryptographic RNG for a secret (python:S2245) ---
    return "".join(str(random.randint(0, 9)) for _ in range(6))


if __name__ == "__main__":
    # --- Hotspot: Flask debug mode (python:S4507) ---
    app.run(debug=True)
