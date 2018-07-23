
truncate table sfly_customer_dtl;
truncate table sfly_image_hist   ;   
truncate table sfly_order_hist    ;  
truncate table sfly_site_visit     ; 
truncate table sfly_site_visit_tag;

insert into sfly_customer_dtl values('96f55c7d8f42', 1, '2017-01-06T12:45:52.041', 'Smith', 'Middletown', 'AK');
insert into sfly_customer_dtl values( get_hash_key('Skywalker'), 1, '2017-01-06T12:45:52.041', 'Skywalker', 'town1', 'CA');
insert into sfly_customer_dtl values( get_hash_key('Solo'), 1, '2017-01-06T12:45:52.041', 'Skywalker', 'town2', 'NY');
insert into sfly_customer_dtl values( get_hash_key('Organa'), 1, '2017-01-06T12:45:52.041', 'Organa', 'town3', 'FL');
insert into sfly_customer_dtl values( get_hash_key('Yoda'), 1, '2017-01-06T12:45:52.041', 'Yoda', 'town5', 'WY');


insert into sfly_image_hist values('d8ede43b1d9f',3,'2017-01-06T12:47:12.344', '96f55c7d8f42', 1, 1);
insert into sfly_image_hist values(get_hash_key('img1'),3,'2017-01-06T12:47:12.344', get_hash_key('Solo'), 1, 1);
insert into sfly_image_hist values(get_hash_key('img2'),3,'2017-01-06T12:47:12.344', get_hash_key('Yoda'), 1, 1);
insert into sfly_image_hist values(get_hash_key('img3'),3,'2017-01-06T12:47:12.344', get_hash_key('Skywalker'), 1, 1);
insert into sfly_image_hist values(get_hash_key('img4'),3,'2017-01-06T12:47:12.344', get_hash_key('Organa'), 1, 1);

insert into sfly_order_hist values('68d84e5d1a43', 1, '96f55c7d8f42', '2017-01-06T12:55:55.555', 12.34);
insert into sfly_order_hist values(get_hash_key('order1'), 1, get_hash_key('Solo'), '2017-01-06T12:55:55.555', 22.34);
insert into sfly_order_hist values(get_hash_key('order2'), 1, get_hash_key('Yoda'), '2017-01-06T12:55:55.555', 32.34);
insert into sfly_order_hist values(get_hash_key('order3'), 1, get_hash_key('Organa'), '2017-01-06T12:55:55.555', 42.34);
insert into sfly_order_hist values(get_hash_key('order4'), 1, get_hash_key('Skywalker'), '2017-01-06T12:55:55.555', 52.34);
insert into sfly_order_hist values(get_hash_key('order2'), 2, get_hash_key('Yoda'), '2017-01-06T12:55:55.555', 32.34);
insert into sfly_order_hist values(get_hash_key('order3'), 2, get_hash_key('Organa'), '2017-01-06T12:55:55.555', 42.34);
insert into sfly_order_hist values(get_hash_key('order4'), 2, get_hash_key('Skywalker'), '2017-01-06T12:55:55.555', 52.34);

insert into sfly_site_visit values( 'ac05e815502f', '96f55c7d8f42', 1, '2017-01-06T12:45:52.041');
insert into sfly_site_visit values( 'ac05e815502f', '96f55c7d8f42', 1, '2017-01-06T12:45:52.041');
insert into sfly_site_visit values( get_hash_key('url1'), get_hash_key('Solo'), 1, '2017-01-06T12:45:52.041');
insert into sfly_site_visit values( get_hash_key('url1'), get_hash_key('Skywalker'), 1, '2017-01-06T12:45:52.041');
insert into sfly_site_visit values( get_hash_key('url2'), get_hash_key('Yoda'), 1, '2017-01-06T12:45:52.041');
insert into sfly_site_visit values( get_hash_key('url3'), get_hash_key('Organa'), 1, '2017-01-06T12:45:52.041');

insert into sfly_site_visit_tag values( get_hash_key(concat(get_hash_key('url1'), get_hash_key('Solo'), get_hash_key('2017-01-06T12:45:52.041'))), get_hash_key('key1'), 'val30');
insert into sfly_site_visit_tag values( get_hash_key(concat(get_hash_key('url2'), get_hash_key('Yoda'), get_hash_key('2017-01-06T12:45:52.041'))), get_hash_key('key2'), 'val90');
insert into sfly_site_visit_tag values( get_hash_key(concat('ac05e815502f', '96f55c7d8f42', get_hash_key('2017-01-06T12:45:52.041'))), get_hash_key('key3'), 'val120');
insert into sfly_site_visit_tag values( get_hash_key(concat('ac05e815502f', '96f55c7d8f42', get_hash_key('2017-01-06T12:45:52.041'))), get_hash_key('key4'), 'val110');

/*  === adding more order records === */
insert into sfly_order_hist select order_hash_key, verb_id, customer_hash_key, DATE_ADD(event_time, INTERVAL 3 DAY), total_amt + 20.1 from sfly_order_hist;
insert into sfly_order_hist select order_hash_key, verb_id, customer_hash_key, DATE_ADD(event_time, INTERVAL 5 DAY), total_amt + 10.3 from sfly_order_hist;

insert into sfly_order_hist select order_hash_key, verb_id, customer_hash_key, DATE_ADD(event_time, INTERVAL -100 DAY), total_amt + 10.3 from sfly_order_hist;
insert into sfly_order_hist select order_hash_key, verb_id, customer_hash_key, DATE_ADD(event_time, INTERVAL -500 DAY), total_amt + 10.3 from sfly_order_hist;

/* === adding more data to site_visit ****/
insert into sfly_site_visit select page_hash_key, customer_hash_key, verb_id, DATE_ADD(event_time, INTERVAL 3 DAY) from sfly_site_visit;
insert into sfly_site_visit select page_hash_key, customer_hash_key, verb_id, DATE_ADD(event_time, INTERVAL 8 DAY) from sfly_site_visit;

insert into sfly_site_visit select page_hash_key, customer_hash_key, verb_id, DATE_ADD(event_time, INTERVAL -100 DAY) from sfly_site_visit;
insert into sfly_site_visit select page_hash_key, customer_hash_key, verb_id, DATE_ADD(event_time, INTERVAL -500 DAY) from sfly_site_visit;
