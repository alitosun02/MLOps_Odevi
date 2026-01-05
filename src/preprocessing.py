
def hash_feature(input_string, bucket_size=100):
    if not isinstance(input_string, str):
        raise ValueError("Girdi bir string olmalı")

    hashed_value = hash(input_string) 
    return hashed_value

if __name__ == "__main__":
    print(f"Test sonucu: {hash_feature('Istanbul')}")