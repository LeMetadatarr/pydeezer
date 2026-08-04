"""Row-schema equivalence tests for the Deezer scraper.

Relocated verbatim (assertions untouched) from metadatarr's
test_scrapers_batch4.py, keeping only the tests for the scraper that
lives in this package, re-pointed at pydeezer.harvest.*. These lock the
exact flat-row shape the scraper emits (the contract the LeData datasets
depend on) against a realistic upstream sample, so a future engine change
can't silently alter the output schema.
"""
from __future__ import annotations

from harvestkit.engine import all_sources

from pydeezer.harvest.deezer_artists import DeezerArtistsSource


def test_deezer_artists_map_row_schema():
    src = DeezerArtistsSource()
    row = src.map_row(27, {
        "name": "Daft Punk", "picture_big": "http://big.jpg", "picture": "http://small.jpg",
        "nb_album": 10, "nb_fan": 5_000_000, "link": "http://deezer.com/artist/27",
    })
    assert row == {
        "deezer_id": 27,
        "name": "Daft Punk",
        "picture_url": "http://big.jpg",
        "nb_album": 10,
        "nb_fan": 5_000_000,
        "url": "http://deezer.com/artist/27",
    }
    assert set(row) == {"deezer_id", "name", "picture_url", "nb_album", "nb_fan", "url"}


def test_deezer_artists_fetch_walks_id_chunk_and_stops_at_end():
    src = DeezerArtistsSource()
    src.end = 5
    src.throttle.wait = lambda: None
    src._fetch_artist = lambda i: ({"deezer_id": i, "name": f"a{i}"} if i in (1, 3) else None)
    rows, cursor = src.fetch(1)
    assert [r["deezer_id"] for r in rows] == [1, 3]
    assert cursor is None


def test_deezer_artists_fetch_stops_when_start_beyond_end():
    src = DeezerArtistsSource()
    src.end = 5
    rows, cursor = src.fetch(6)
    assert rows == []
    assert cursor is None


def test_deezer_artists_registered():
    assert all_sources().get("deezer_artists") is DeezerArtistsSource
