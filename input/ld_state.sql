

LOAD DATA local INFILE 'state_codes.csv' replace INTO TABLE lu_state
  FIELDS TERMINATED BY ',' ignore 1 lines;
