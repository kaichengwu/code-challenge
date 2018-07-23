
create database shutterfly;


use shutterfly;



drop table  lu_state;
create table lu_state
(
   id int not null,
   state_code varchar(10) not null,
   state_name varchar(30) not null
);


drop table  lu_camera_brand;
create table lu_camera_brand
(
   id int not null,
   camera_brand varchar(100) not null
);

drop table  lu_camera_model;
create table lu_camera_model
(
   id int not null,
   camera_brand_id int not null,
   camera_model varchar(100) not null
);

drop table lu_activity_type;
create table lu_activity_type
(
   id int not null,
   activity_name varchar(20) not null
); 

drop table lu_verb;
create table lu_verb
(
   id int not null,
   verb_name varchar(20) not null
);

drop table lu_activity_verb;
create table lu_activity_verb
(
   id int not null,
   activity_id int not null,
   verb_id int not null
);

drop table sfly_customer_dtl;
create table sfly_customer_dtl
(
   customer_hash_key varchar(20) not null,
   verb_id int not null,
   event_time timestamp not null,
   last_name varchar(100),
   adr_city  varchar(100),
   adr_state_code varchar(10)
);

drop table sfly_image_hist;
create table sfly_image_hist
(
   image_hash_key  varchar(20) not null,
   verb_id int not null,
   event_time  timestamp not null,
   customer_hash_key varchar(20) not null,
   camera_brand_id int,
   camera_model_id int
);

drop table sfly_order_hist;
create table sfly_order_hist
(
   order_hash_key varchar(20) not null,
   verb_id int not null,
   customer_hash_key varchar(20) not null,
   event_time timestamp not null,
   total_amt float not null
);

drop table sfly_site_visit;
create table sfly_site_visit
(
   page_hash_key varchar(20) not null,
   customer_hash_key varchar(20) not null,
   verb_id int not null,
   event_time timestamp not null
);


drop table lu_tag_key;
create table lu_tag_key
(
   tag_hash_key varchar(20) not null,
   key_name     varchar(100) not null
);

drop table sfly_site_visit_tag;
create table sfly_site_visit_tag
(
   tag_page_hash_key varchar(20) not null,
   tag_hash_key varchar(20) not null,
   key_val      varchar(100) not null
);



exit; 
