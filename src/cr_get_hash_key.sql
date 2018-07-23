create function get_hash_key(p_str varchar(100))
     returns varchar(20) deterministic
     return substr(sha1(p_str), 1, 12);

