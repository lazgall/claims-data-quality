from claims_quality import check_missing_claim_ids, find_duplicate_claim_ids
from claims_quality import get_api_key

def test_check_missing_claim_ids():
    claim_ids = [101, None, 103, None]

    result = check_missing_claim_ids(claim_ids)

    assert result == [None, None]


def test_find_duplicate_claim_ids():
    claim_ids = [101, 102, 101, 103, 102]

    result = find_duplicate_claim_ids(claim_ids)

    assert set(result) == {101, 102}

def test_api_key_is_available():
    assert get_api_key() is not None
