import sfly_dwh

original_data = [{"type": "CUSTOMER", "verb": "NEW", "key": "96f55c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Smith", "adr_city": "Middletown", "adr_state": "AK"}, {"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e815502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "96f55c7d8f42", "tags": {"some key": "some value"}}, {"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e815502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "96f55c7d8f42", "tags": [{"some key": "some value"}]}, {"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede43b1d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "96f55c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"}, {"type": "ORDER", "verb": "NEW", "key": "68d84e5d1a43", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "96f55c7d8f42", "total_amount": "12.34 USD"}]

#test_data = original_data
test_data = original_data[:]

# print(len(test_data))


## test customer records

sfly_dwh.Ingest({"type": "CUSTOMER", "verb": "NEW", "key": "a6f55c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Batman", "adr_city": "Middletown", "adr_state": "CA"}, test_data)
sfly_dwh.Ingest({"type": "CUSTOMER", "verb": "UPDATE", "key": "a6f55c7d8f42", "event_time": "2017-02-06T12:46:46.384Z", "last_name": "Batman", "adr_city": "Gotham", "adr_state": "NY"}, test_data)
sfly_dwh.Ingest({"type": "CUSTOMER", "verb": "NEW", "key": "b6f55c7d8f42", "event_time": "2017-03-06T12:46:46.384Z", "last_name": "Yoda", "adr_city": "Gotham", "adr_state": "NY"}, test_data)
sfly_dwh.Ingest({"type": "CUSTOMER", "verb": "NEW", "key": "c6f55c7d8f42", "event_time": "2017-04-06T12:46:46.384Z", "last_name": "Skywalker", "adr_city": "Gotham", "adr_state": "NY"}, test_data)


## test image records
sfly_dwh.Ingest({"type": "IMAGE", "verb": "UPLOAD", "key": "18ede43b1d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "a6f55c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"}, test_data)
sfly_dwh.Ingest({"type": "IMAGE", "verb": "NEW", "key": "18ede43b1d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "a6f55c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"}, test_data)


## test order records
#Smith
sfly_dwh.Ingest({"type": "ORDER", "verb": "NEW", "key": "91d84e5d1a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "96f55c7d8f42", "total_amount": "227.34 USD"}, test_data)
sfly_dwh.Ingest({"type": "ORDER", "verb": "NEW", "key": "93d84e5d1a43", "event_time": "2017-11-07T12:55:55.555Z", "customer_id": "96f55c7d8f42", "total_amount": "7.34 USD"}, test_data)
sfly_dwh.Ingest({"type": "ORDER", "verb": "NEW", "key": "94d84e5d1a43", "event_time": "2017-12-26T12:55:55.555Z", "customer_id": "96f55c7d8f42", "total_amount": "12.25 USD"}, test_data)
#Batman
sfly_dwh.Ingest({"type": "ORDER", "verb": "NEW", "key": "28d84e5d1a43", "event_time": "2018-01-06T12:55:55.555Z", "customer_id": "a6f55c7d8f42", "total_amount": "12.34 USD"}, test_data)
sfly_dwh.Ingest({"type": "ORDER", "verb": "UPDATE", "key": "28d84e5d1a43", "event_time": "2018-01-08T12:55:55.555Z", "customer_id": "a6f55c7d8f42", "total_amount": "212.34 USD"}, test_data)
#Yoda
sfly_dwh.Ingest({"type": "ORDER", "verb": "NEW", "key": "b1d84e5d1a43", "event_time": "2018-01-04T12:55:55.555Z", "customer_id": "b6f55c7d8f42", "total_amount": "30.30 USD"}, test_data)
sfly_dwh.Ingest({"type": "ORDER", "verb": "NEW", "key": "b2d84e5d1a43", "event_time": "2018-01-09T12:55:55.555Z", "customer_id": "b6f55c7d8f42", "total_amount": "40.40 USD"}, test_data)
sfly_dwh.Ingest({"type": "ORDER", "verb": "NEW", "key": "b3d84e5d1a43", "event_time": "2018-02-20T12:55:55.555Z", "customer_id": "b6f55c7d8f42", "total_amount": "50.50 USD"}, test_data)
#Skywalker
sfly_dwh.Ingest({"type": "ORDER", "verb": "NEW", "key": "c1d84e5d1a43", "event_time": "2018-05-05T12:55:55.555Z", "customer_id": "c6f55c7d8f42", "total_amount": "10.34 USD"}, test_data)
sfly_dwh.Ingest({"type": "ORDER", "verb": "NEW", "key": "c2d84e5d1a43", "event_time": "2018-06-05T12:55:55.555Z", "customer_id": "c6f55c7d8f42", "total_amount": "21.21 USD"}, test_data)
sfly_dwh.Ingest({"type": "ORDER", "verb": "NEW", "key": "c3d84e5d1a43", "event_time": "2018-07-05T12:55:55.555Z", "customer_id": "c6f55c7d8f42", "total_amount": "31.31 USD"}, test_data)

## test site visit records
#Smith
sfly_dwh.Ingest({"type": "SITE_VISIT", "verb": "NEW", "key": "9105e815502f", "event_time": "2017-11-06T12:45:52.041Z", "customer_id": "a6f55c7d8f42", "tags": {"some key1": "some value1"}}, test_data)
sfly_dwh.Ingest({"type": "SITE_VISIT", "verb": "NEW", "key": "9205e815502f", "event_time": "2017-12-26T12:45:52.041Z", "customer_id": "a6f55c7d8f42", "tags": {"some key1": "some value1"}}, test_data)
#Batman
sfly_dwh.Ingest({"type": "SITE_VISIT", "verb": "NEW", "key": "a105e815502f", "event_time": "2018-01-06T12:45:52.041Z", "customer_id": "a6f55c7d8f42", "tags": {"some key1": "some value1"}}, test_data)
sfly_dwh.Ingest({"type": "SITE_VISIT", "verb": "NEW", "key": "a205e815502f", "event_time": "2018-01-08T12:45:52.041Z", "customer_id": "a6f55c7d8f42", "tags": {"some key2": "some value2"}}, test_data)
sfly_dwh.Ingest({"type": "SITE_VISIT", "verb": "NEW", "key": "a305e815502f", "event_time": "2018-01-06T13:45:52.041Z", "customer_id": "a6f55c7d8f42", "tags": {"some key2": "some value2"}}, test_data)
sfly_dwh.Ingest({"type": "SITE_VISIT", "verb": "NEW", "key": "a405e815502f", "event_time": "2018-01-08T18:45:52.041Z", "customer_id": "a6f55c7d8f42", "tags": {"some key2": "some value2"}}, test_data)
#Yoda
sfly_dwh.Ingest({"type": "SITE_VISIT", "verb": "NEW", "key": "b105e815502f", "event_time": "2018-01-04T12:45:52.041Z", "customer_id": "b6f55c7d8f42", "tags": {"some key1": "some value1"}}, test_data)
sfly_dwh.Ingest({"type": "SITE_VISIT", "verb": "NEW", "key": "b205e815502f", "event_time": "2018-01-09T12:45:52.041Z", "customer_id": "b6f55c7d8f42", "tags": {"some key1": "some value1"}}, test_data)
sfly_dwh.Ingest({"type": "SITE_VISIT", "verb": "NEW", "key": "b305e815502f", "event_time": "2018-02-20T12:45:52.041Z", "customer_id": "b6f55c7d8f42", "tags": {"some key1": "some value1"}}, test_data)
#Skywalker
sfly_dwh.Ingest({"type": "SITE_VISIT", "verb": "NEW", "key": "c105e815502f", "event_time": "2018-05-05T12:45:52.041Z", "customer_id": "c6f55c7d8f42", "tags": {"some key1": "some value1"}}, test_data)
sfly_dwh.Ingest({"type": "SITE_VISIT", "verb": "NEW", "key": "c205e815502f", "event_time": "2018-06-05T12:45:52.041Z", "customer_id": "c6f55c7d8f42", "tags": {"some key1": "some value1"}}, test_data)
sfly_dwh.Ingest({"type": "SITE_VISIT", "verb": "NEW", "key": "c305e815502f", "event_time": "2018-07-05T12:45:52.041Z", "customer_id": "c6f55c7d8f42", "tags": {"some key1": "some value1"}}, test_data)


#print(len(test_data))

###
print('===========')
print('After Ingestion')
print(test_data)

##### Calculation
xrank=2
tmp = sfly_dwh.TopXSimpleLTVCustomers(xrank, test_data)
print('TOP ' + str(xrank) + ' customer LTV are:')
print(tmp)
