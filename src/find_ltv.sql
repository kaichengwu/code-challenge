use shutterfly

/*
Create a reporting weekly tally table.

Aggregate by Week, and customer
*/

drop table sfly_ltv_tally;

create table sfly_ltv_tally
       (week_period       varchar(20),
        customer_hash_key varchar(20),
        num_visit         int,
        exp_amt           float)
 select wk week_period,
        customer_hash_key,
        sum(visit_cnt) num_visit,
        sum(exp_amt) exp_amt 
   from ( select customer_hash_key, 
                yearweek(event_time) wk,
                0 visit_cnt,
                sum(total_amt) exp_amt
           from sfly_order_hist
          group by customer_hash_key, 
                   yearweek(event_time) 
          union all
          select customer_hash_key, 
                 yearweek(event_time) wk,
                 count(page_hash_key) visit_cnt,
                 0 exp_amt
            from sfly_site_visit 
           group by customer_hash_key, 
                    yearweek(event_time)
          ) tally
   group by week_period, customer_hash_key;


/*

Find the total amount paid during the last 52 weeks starting from the latest recorded transaction period (week).

Multiply by 10 (Average customer lifespan.
Aggregate by customer for the top customer LTV.
*/

select a.customer_hash_key,
       b.last_name,
       sum(num_visit) total_num_visit,
       sum(exp_amt) * 10 total_LTV
  from sfly_ltv_tally a,
       sfly_customer_dtl b
 where a.week_period <= (select max(week_period) from sfly_ltv_tally)
   and a.week_period >= 
       (select yearweek(date_add(str_to_date(
               concat(convert(maxwk, char), ' Monday'), '%X%V %W'),
                       interval -365 DAY)) 
          from (select max(week_period) maxwk from sfly_ltv_tally) t
       )
    and a.customer_hash_key = b.customer_hash_key
  group by a.customer_hash_key,
           b.last_name
  order by total_LTV desc;

