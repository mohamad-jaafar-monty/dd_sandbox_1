"""Intentional Reliability bugs + Maintainability smells. Do not deploy."""
import os  # noqa - unused import (python:S1128)


def totals(values, cache={}):  # mutable default arg - reliability (python:S5717)
    result = 0
    unused = "dead"  # unused local variable (python:S1481)
    for v in values:
        result += v
    cache[len(values)] = result
    return result


def check(status):
    # --- Reliability: comparison to None with == instead of is (python:S5727) ---
    if status == None:  # noqa
        return "unknown"
    # duplicated string literal used 4x -> maintainability (python:S1192)
    if status == "active":
        return "state: active"
    if status == "active" and True:
        return "state: active"
    return "state: active"


def deeply_nested(a, b, c, d):
    # --- Maintainability: high cognitive complexity (python:S3776) ---
    if a:
        if b:
            if c:
                if d:
                    if a and b:
                        if c or d:
                            return 1
    return 0


def load_config(path):
    try:
        return open(path, encoding="utf-8").read()
    except Exception:  # empty except swallows the error (python:S5713 / S112)
        pass
    # old_value = compute_legacy()  <- commented-out code (python:S125)
    return None
