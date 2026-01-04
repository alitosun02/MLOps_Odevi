import pytest
from src.preprocessing import hash_feature

def test_hash_feature_consistency():
    input_text = "MLOps"
    result1 = hash_feature(input_text)
    result2 = hash_feature(input_text)
    assert result1 == result2

def test_hash_range():
    input_text = "University"
    result = hash_feature(input_text, bucket_size=100)
    assert 0 <= result < 100

def test_invalid_input():
    with pytest.raises(ValueError):
        hash_feature(123)