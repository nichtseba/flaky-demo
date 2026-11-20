"""Tests für rechner.py, inklusive absichtlich flaky Tests zur Demonstration."""

import random
import time

import pytest

from rechner import addiere, teile


# --- Zuverlässige Tests ---

def test_addiere():
    assert addiere(2, 3) == 5


def test_teile():
    assert teile(10, 2) == 5


def test_teile_durch_null():
    with pytest.raises(ValueError):
        teile(1, 0)


# --- Flaky Tests ---
# Absichtlich instabil, um flaky Verhalten zu demonstrieren. Nicht reparieren.

def test_flaky_zufall():
    # Ohne festen Seed schlägt der Test in ca. 30 % der Läufe fehl.
    assert random.random() > 0.3


def test_flaky_timing():
    # Die Wartezeit überschreitet in ca. 25 % der Läufe das Limit von 0.15 s;
    # auf ausgelasteten Maschinen (z. B. CI) noch häufiger.
    start = time.time()
    time.sleep(random.uniform(0, 0.2))
    dauer = time.time() - start
    assert dauer < 0.15
