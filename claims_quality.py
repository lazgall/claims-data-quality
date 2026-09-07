def check_claims():
    print("Claims data quality check running")

def check_missing_claim_ids(claim_ids):
    return [claim_id for claim_id in claim_ids if claim_id is None]

def find_duplicate_claim_ids(claim_ids):
    duplicates = {
        claim_id
        for claim_id in claim_ids
        if claim_ids.count(claim_id) > 1
    }

    #return list(duplicates)
    return []

if __name__ == "__main__":
    check_claims()