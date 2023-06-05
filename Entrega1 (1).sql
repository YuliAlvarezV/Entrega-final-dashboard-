/* 1)Cantidad de personas que saben leer y escribir en familias con los ingresos más bajos*/
SELECT SUM(total) as num_personas_leen_escriben
FROM Bienes.bienes_dur
WHERE dim = 'Bienes Durables' AND total_low < 5000;
/*2)¿Hay mayor número de mujeres u hombres en zonas de alta pobreza?*/
SELECT sexo, COUNT(*) as num_personas
FROM Bienes.bienes_dur
WHERE estratos = 'Pobreza muy alta'
GROUP BY sexo
ORDER BY num_personas DESC;
/*3)¿En qué alcaldía se tienen familias con pobreza alta y pobreza muy alta?*/
SELECT distinct nomgeo AS Localidad
FROM Bienes.bienes_dur
WHERE estratos LIKE '%Pobreza alta%' OR estratos LIKE '%Pobreza muy alta%'
ORDER BY nomgeo ASC;
/*4)Es mayor el ingreso del hogar si el jefe de hogar es un hombre?*/
SELECT sexo AS Genero_jefe_hogar, AVG(total) AS Ingreso_promedio
FROM Bienes.bienes_dur
GROUP BY Genero_jefe_hogar;
/*5)En lugares con pobreza moderada hay mayor número de familias con ingresos mayores al promedio?*/
SELECT estratos AS Nivel_pobreza,
CASE
WHEN AVG(total) > (SELECT AVG(total) FROM Bienes.bienes_dur) THEN 'Sí'
ELSE 'No'
END AS Ingreso_mayor_promedio,COUNT(*) AS Cantidad_familias
FROM Bienes.bienes_dur
WHERE estratos LIKE '%Pobreza moderada%'
GROUP BY Nivel_pobreza;
/*6)¿Existe mayor índice de necesidades básicas insatisfechas si el tamaño del hogar es mayor a 3 personas?*/
SELECT
CASE
  WHEN tam_hog > 3 THEN 'Mayor a 3 personas'
  ELSE 'Menor o igual a 3 personas'
END AS grupo_personas,
AVG(nbi) AS promedio_nbi
FROM
GNBI.gnbi
GROUP BY
CASE
  WHEN tam_hog > 3 THEN 'Mayor a 3 personas'
  ELSE 'Menor o igual a 3 personas'
END;
/*7)¿Cuál es el porcentaje de personas que saben leer y escribir en la Ciudad de México?*/
SELECT COUNT(*) AS total_personas,
    ROUND((SUM(CASE WHEN alfabet = "1" THEN 1 ELSE 0 END) / COUNT(*)) * 100, 2) AS porcentaje_alfabetismo
FROM GNBI.gnbi;
/*8)¿Cuál es la proporción de personas que tienen acceso a la salud y a la seguridad social en las diferentes alcaldías de la Ciudad de México?*/
SELECT mun AS alcaldia,
  ROUND((SUM(CASE WHEN casi = 1 THEN 1 ELSE 0 END) / COUNT(*)) * 100,2) AS porcentaje_acceso_salud,
ROUND((SUM(CASE WHEN cassi = 1 THEN 1 ELSE 0 END) / COUNT(*)) * 100,2) AS porcentaje_acceso_seg_social
FROM GNBI.gnbi
GROUP BY mun;
/*9)¿Cuál es la distribución de las diferentes categorías de estratos socioeconómicos en la Ciudad de México?*/
SELECT estratos, COUNT(*) as total_personas
FROM Bienes.bienes_dur
AS estrato_table
GROUP BY estratos;
/*10)¿Cuáles son las 5 alcaldías con el mayor porcentaje de hogares con acceso a servicios de seguridad social?*/
SELECT alcaldia, AVG(cassi) AS porcentaje_acceso_seguridad
FROM GNBI.gnbi
GROUP BY alcaldia
ORDER BY porcentaje_acceso_seguridad  DESC
LIMIT 5;
/*11)¿Cantidad de hogares en zonas urbanas y rurales en la Ciudad de México?*/
SELECT ur_rur_2500 AS tipo_localidad,
ROUND((COUNT(*) / (SELECT COUNT(*) FROM `GNBI.gnbi`)) * 100, 2) AS porcentaje_hogares
FROM GNBI.gnbi
GROUP BY ur_rur_2500;


/*12)¿Qué cantidad de hogares con necesidades básicas insatisfechas no tienen acceso a servicios de salud?*/
SELECT COUNT(*) AS hogares_sin_salud_con_nbi
FROM GNBI.gnbi
WHERE casi <0 and nbi > 0;
/*13)¿Cuál es el porcentaje de hogares que tienen acceso a internet en la Ciudad de México?*/
SELECT COUNT(1)  AS Cantidad_hogares_acceso_internet
FROM GNBI.gnbi
WHERE ivj = 1;
/*14)¿Cuántas personas en la categoría  de muy alta y alta pobreza no cuentan con las necesidades básicas dentro de su hogar?*/
SELECT e_nbi, COUNT(*) AS LIFE
FROM `GNBI.gnbi`
WHERE e_nbi = 1 OR e_nbi = 2
GROUP BY e_nbi;
/*15)¿Cuál es la distribución de edades en la población de la Ciudad de México?*/
SELECT CASE 
WHEN edad BETWEEN 0 AND 17 THEN '0-17' 
WHEN edad BETWEEN 18 AND 29 THEN '18-29' 
WHEN edad BETWEEN 30 AND 44 THEN '30-44' 
WHEN edad BETWEEN 45 AND 59 THEN '45-59' 
WHEN edad BETWEEN 60 AND 74 THEN '60-74' 
ELSE '75+' 
END AS rango_edades, COUNT(*) AS total_personas 
FROM GNBI.gnbi 
GROUP BY rango_edades;


/*16)¿Cuál es la proporción de personas mayores de 65 años que viven solas en la Ciudad de México?*/
SELECT COUNT(*) AS total_personas_mayores, 
ROUND((SUM(CASE WHEN edad >= 65 AND tam_hog = 1 THEN 1 ELSE 0 END) / COUNT(*)) * 100, 2) AS porcentaje_personas_mayores_solas 
FROM GNBI.gnbi;


/*17)¿Cuáles son las 5 alcaldías donde más hay hogares conformados por una sola persona?*/
SELECT mun AS alcaldia, COUNT(*) AS cantidad_hogares
FROM GNBI.gnbi
WHERE tam_hog = 1
GROUP BY alcaldia
ORDER BY cantidad_hogares DESC
LIMIT 5;


/*18)¿Cuántas personas en la Ciudad de México cuentan con seguridad social?*/
SELECT COUNT(*) AS total_personas_seguro_medico
FROM GNBI.gnbi
WHERE casi = 1 OR cassi = 1;


/*19)¿En qué alcaldías se encuentran los hogares con los ingresos promedio por edad más altos?*/
SELECT nomgeo AS Alcaldia, AVG(total) AS Ingreso_promedio
FROM Bienes.bienes_dur
GROUP BY Alcaldia
ORDER BY Ingreso_promedio DESC;


/*20)¿En qué alcaldías se encuentra la mayor cantidad de hogares con acceso a internet?*/
SELECT alcaldia, COUNT(*) as total_hogares_acceso_internet
FROM GNBI.gnbi
WHERE ivj = 1
GROUP BY alcaldia
ORDER BY total_hogares_acceso_internet DESC
LIMIT 5;
