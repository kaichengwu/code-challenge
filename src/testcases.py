import sfly_dwh

original_data = [{"type": "CUSTOMER", "verb": "NEW", "key": "96f55c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Smith", "adr_city": "Middletown", "adr_state": "AK"}, {"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e815502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "96f55c7d8f42", "tags": {"some key": "some value"}}, {"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e815502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "96f55c7d8f42", "tags": [{"some key": "some value"}]}, {"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede43b1d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "96f55c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"}, {"type": "ORDER", "verb": "NEW", "key": "68d84e5d1a43", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "96f55c7d8f42", "total_amount": "12.34 USD"}]

#test_data = original_data
test_data = original_data[:]
print(len(test_data))


## test customer records

sfly_dwh.Ingest({"type": "CUSTOMER", "verb": "NEW", "key": "a6f55c7d8f42", "event_time": "2018-01-06T12:46:46.384Z", "last_name": "Batman", "adr_city": "Middletown", "adr_state": "CA"}, test_data)
sfly_dwh.Ingest({"type": "CUSTOMER", "verb": "UPDATE", "key": "a6f55c7d8f42", "event_time": "2018-01-06T12:46:46.384Z", "last_name": "Batman", "adr_city": "Gotham", "adr_state": "NY"}, test_data)


## test image records
sfly_dwh.Ingest({"type": "IMAGE", "verb": "UPLOAD", "key": "18ede43b1d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "a6f55c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"}, test_data)
sfly_dwh.Ingest({"type": "IMAGE", "verb": "NEW", "key": "18ede43b1d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "a6f55c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"}, test_data)


## test order records
sfly_dwh.Ingest({"type": "ORDER", "verb": "NEW", "key": "28d84e5d1a43", "event_time": "2018-01-06T12:55:55.555Z", "customer_id": "a6f55c7d8f42", "total_amount": "12.34 USD"}, test_data)
sfly_dwh.Ingest({"type": "ORDER", "verb": "UPDATE", "key": "28d84e5d1a43", "event_time": "2018-01-06T12:55:55.555Z", "customer_id": "a6f55c7d8f42", "total_amount": "212.34 USD"}, test_data)

## test site visit records
sfly_dwh.Ingest({"type": "SITE_VISIT", "verb": "NEW", "key": "3c05e815502f", "event_time": "2018-01-06T12:45:52.041Z", "customer_id": "a6f55c7d8f42", "tags": {"some key1": "some value1"}}, test_data)
sfly_dwh.Ingest({"type": "SITE_VISIT", "verb": "OLD", "key": "3c05e815502f", "event_time": "2018-01-06T12:45:52.041Z", "customer_id": "a6f55c7d8f42", "tags": {"some key2": "some value2"}}, test_data)


print("After Ingestion")
print((test_data))
print("Top 1 Customer LTV")
tmp = sfly_dwh.TopXSimpleLTVCustomers(1, test_data)
print(tmp)
