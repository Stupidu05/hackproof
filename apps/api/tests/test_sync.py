from datetime import UTC, datetime

import pytest

from hackproof.indexer.sync import ensure_within_retention

OLDEST = datetime(2026, 10, 27, 9, 0, tzinfo=UTC)


def test_a_window_older_than_the_rpc_history_stops_the_sync():
    with pytest.raises(RuntimeError, match="can no longer be synced"):
        ensure_within_retention(datetime(2026, 10, 25, 9, 0, tzinfo=UTC), OLDEST)


def test_a_window_inside_the_rpc_history_goes_ahead():
    ensure_within_retention(datetime(2026, 10, 28, 9, 0, tzinfo=UTC), OLDEST)
