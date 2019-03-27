-- 按比例排名

SELECT
	city_manager_code,
	city_manager_name,
	sum( CASE WHEN apply_times IS NULL THEN 0 ELSE 1 END ) applied,
	sum( CASE WHEN apply_times IS NULL THEN 1 ELSE 0 END ) unapplied ,
	sum( CASE WHEN apply_times IS NULL THEN 0 ELSE 1 END )/(sum( CASE WHEN apply_times IS NULL THEN 0 ELSE 1 END )+ sum( CASE WHEN apply_times IS NULL THEN 1 ELSE 0 END )) rate
FROM
	display_apply_view 
GROUP BY
	city_manager_code,
	city_manager_name
ORDER BY rate
limit 20
OFFSET 0

	
	
-- 按报备排名

SELECT
	city_manager_code,
	city_manager_name,
	sum( CASE WHEN apply_times IS NULL THEN 0 ELSE 1 END ) applied,
	sum( CASE WHEN apply_times IS NULL THEN 1 ELSE 0 END ) unapplied ,
	(sum( CASE WHEN apply_times IS NULL THEN 0 ELSE 1 END )+ sum( CASE WHEN apply_times IS NULL THEN 1 ELSE 0 END )) total
FROM
	display_apply_view v
WHERE v.sales_man_code in ()
GROUP BY
	city_manager_code,
	city_manager_name
ORDER BY applied
limit 20
OFFSET 0
