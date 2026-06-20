-- Average Temperature

SELECT
AVG(temperature) AS avg_temperature
FROM sensor_data;

--------------------------------------------------

-- Maximum Vibration

SELECT
MAX(vibration) AS max_vibration
FROM sensor_data;

--------------------------------------------------

-- Equipment-wise Average Power Consumption

SELECT
equipment_name,
ROUND(AVG(power_consumption),2) AS avg_power
FROM sensor_data
GROUP BY equipment_name;

--------------------------------------------------

-- Equipment-wise Total Production

SELECT
equipment_name,
ROUND(SUM(production_rate),2) AS total_production
FROM sensor_data
GROUP BY equipment_name;

--------------------------------------------------

-- Running Equipment Records

SELECT *
FROM sensor_data
WHERE status='Running';

--------------------------------------------------

-- Top 10 Highest Temperature Readings

SELECT *
FROM sensor_data
ORDER BY temperature DESC
LIMIT 10;

--------------------------------------------------

-- Average Temperature by Equipment

SELECT
equipment_name,
ROUND(AVG(temperature),2) AS avg_temp
FROM sensor_data
GROUP BY equipment_name;

--------------------------------------------------

-- Equipment Count by Status

SELECT
status,
COUNT(*) AS total_records
FROM sensor_data
GROUP BY status;