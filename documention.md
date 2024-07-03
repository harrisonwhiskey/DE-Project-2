# USCRN Daily Data Documentation

This documentation provides detailed information about the columns present in the USCRN daily data files. Each column contains specific data related to weather observations and station information. The columns are as follows:

1. **WBANNO**  
   - **Description:** The station WBAN number.

2. **LST_DATE**  
   - **Description:** The Local Standard Time (LST) date of the observation.

3. **CRX_VN**  
   - **Description:** The version number of the station datalogger program in effect at the time of the observation. Note: This field should be treated as text (i.e., string).

4. **LONGITUDE**  
   - **Description:** Station longitude, using WGS-84.

5. **LATITUDE**  
   - **Description:** Station latitude, using WGS-84.

6. **T_DAILY_MAX**  
   - **Description:** Maximum air temperature, in degrees Celsius. See Note F.

7. **T_DAILY_MIN**  
   - **Description:** Minimum air temperature, in degrees Celsius. See Note F.

8. **T_DAILY_MEAN**  
   - **Description:** Mean air temperature, in degrees Celsius, calculated using the typical historical approach: (T_DAILY_MAX + T_DAILY_MIN) / 2. See Note F.

9. **T_DAILY_AVG**  
   - **Description:** Average air temperature, in degrees Celsius. See Note F.

10. **P_DAILY_CALC**  
    - **Description:** Total amount of precipitation, in mm. See Note F.

11. **SOLARAD_DAILY**  
    - **Description:** Total solar energy, in MJ/m², calculated from the hourly average global solar radiation rates and converted to energy by integrating over time.

12. **SUR_TEMP_DAILY_TYPE**  
    - **Description:** Type of infrared surface temperature measurement. 'R' denotes raw measurements, 'C' denotes corrected measurements, and 'U' indicates unknown/missing. See Note G.

13. **SUR_TEMP_DAILY_MAX**  
    - **Description:** Maximum infrared surface temperature, in degrees Celsius.

14. **SUR_TEMP_DAILY_MIN**  
    - **Description:** Minimum infrared surface temperature, in degrees Celsius.

15. **SUR_TEMP_DAILY_AVG**  
    - **Description:** Average infrared surface temperature, in degrees Celsius.

16. **RH_DAILY_MAX**  
    - **Description:** Maximum relative humidity, in %. See Notes H and I.

17. **RH_DAILY_MIN**  
    - **Description:** Minimum relative humidity, in %. See Notes H and I.

18. **RH_DAILY_AVG**  
    - **Description:** Average relative humidity, in %. See Notes H and I.

19. **SOIL_MOISTURE_5_DAILY**  
    - **Description:** Average soil moisture, in fractional volumetric water content (m³/m³), at 5 cm below the surface. See Notes I and J.

20. **SOIL_MOISTURE_10_DAILY**  
    - **Description:** Average soil moisture, in fractional volumetric water content (m³/m³), at 10 cm below the surface. See Notes I and J.

21. **SOIL_MOISTURE_20_DAILY**  
    - **Description:** Average soil moisture, in fractional volumetric water content (m³/m³), at 20 cm below the surface. See Notes I and J.

22. **SOIL_MOISTURE_50_DAILY**  
    - **Description:** Average soil moisture, in fractional volumetric water content (m³/m³), at 50 cm below the surface. See Notes I and J.

23. **SOIL_MOISTURE_100_DAILY**  
    - **Description:** Average soil moisture, in fractional volumetric water content (m³/m³), at 100 cm below the surface. See Notes I and J.

24. **SOIL_TEMP_5_DAILY**  
    - **Description:** Average soil temperature, in degrees Celsius, at 5 cm below the surface. See Notes I and J.

25. **SOIL_TEMP_10_DAILY**  
    - **Description:** Average soil temperature, in degrees Celsius, at 10 cm below the surface. See Notes I and J.

26. **SOIL_TEMP_20_DAILY**  
    - **Description:** Average soil temperature, in degrees Celsius, at 20 cm below the surface. See Notes I and J.

27. **SOIL_TEMP_50_DAILY**  
    - **Description:** Average soil temperature, in degrees Celsius, at 50 cm below the surface. See Notes I and J.

28. **SOIL_TEMP_100_DAILY**  
    - **Description:** Average soil temperature, in degrees Celsius, at 100 cm below the surface. See Notes I and J.

29. **STATE**  
    - **Description:** The state.

30. **LOCATION**  
    - **Description:** The location name.

Notes:
- Note F: Additional information on air temperature measurements.
- Note G: Additional information on infrared surface temperature measurements.
- Notes H and I: Additional information on relative humidity measurements.
- Notes I and J: Additional information on soil moisture and temperature measurements.