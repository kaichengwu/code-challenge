

truncate table lu_verb;
truncate table lu_activity_type;
truncate table lu_activity_verb;
truncate table lu_camera_brand;
truncate table lu_camera_model;
truncate table lu_tag_key;

insert into lu_verb(id, verb_name) values(1, 'NEW');
insert into lu_verb(id, verb_name) values(2, 'UPDATE');
insert into lu_verb(id, verb_name) values(3, 'UPLOAD');

insert into lu_activity_type (id, activity_name) value(1, 'CUSTOMER');
insert into lu_activity_type (id, activity_name) value(2, 'IMAGE UPLOAD');
insert into lu_activity_type (id, activity_name) value(3, 'SITE VISIT');
insert into lu_activity_type (id, activity_name) value(4, 'ORDER');

insert into lu_activity_verb(id, activity_id, verb_id) values(1,1,1);
insert into lu_activity_verb(id, activity_id, verb_id) values(2,1,2);
insert into lu_activity_verb(id, activity_id, verb_id) values(3,3,1);
insert into lu_activity_verb(id, activity_id, verb_id) values(4,2,3);
insert into lu_activity_verb(id, activity_id, verb_id) values(5,4,1);
insert into lu_activity_verb(id, activity_id, verb_id) values(6,4,2);

insert into lu_camera_brand(id, camera_brand)values (1, 'Canon');
insert into lu_camera_brand(id, camera_brand)values( -1, 'NOT LISTED');

insert into lu_camera_model(id, camera_brand_id, camera_model) values(1, 1, 'EOS 800');
insert into lu_camera_model(id, camera_brand_id, camera_model) values(-1, -1, 'NOT LISTED');


insert into lu_tag_key  select substr(sha1('key1'),1,12), 'key1';
insert into lu_tag_key  select substr(sha1('key2'),1,12), 'key2';
insert into lu_tag_key  select substr(sha1('key3'),1,12), 'key3';
insert into lu_tag_key  select substr(sha1('key4'),1,12), 'key4';
