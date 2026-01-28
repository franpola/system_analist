# Tipos de Certificados de expediente personal

- Certificado de Trienios y Servicios reconocidos/previos
  
    - Expedido por el Registro Central
    - Expedido por el organismo en el que se prestan los servicios
      
- Certificado de Situacion Administrativa
  
- Certificado de Destino
  
- Certificado de Grado Personal  
  | Código | Documento | Expedido por |
  |-------|------------|--------------|
  | F16R |Resolución de reconocimiento o convalidacion de grado personal| Organismo |
      
- Certificado d Titulaciones y Cursos
- Certificado de Versiones del Puesto
- Certificado de Licencias
- Certificado de Sanciones
- Certificado de modificación de jornada

# Visor de trazas
```
SELECT *
FROM RCPP.MTRESMON
WHERE CDPROCESO='PROCCERTE'
ORDER BY FEPROC DESC;
```
# Gestión de Solicitudes (RPAE)

- Certificados de Expediente personal -> Gestión de Solicitudes
