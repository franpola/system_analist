---
concepto: Órgano gestor
estado: borrador
revisado: 2026-11-22
rol_facturae: "02"
depende_de: [DIR3, RCF]
relacionado: [oficina-contable, unidad-tramitadora]
fuentes:
  - "Resumen de roles (fuente secundaria): https://taxdown.es/informacion-autonomos/face-facturas"
  - "IGAE, nota informativa sobre identificación de la unidad tramitadora: https://www.igae.pap.hacienda.gob.es/sitios/igae/es-ES/Contabilidad/rcf/Documents/Nota%20informativa%20sobre%20identificación%20de%20la%20unidad%20tramitadora.pdf"
  - "Guía de la Universidad de Jaén (ejemplo): https://www.ujaen.es/servicios/secontab/sites/servicio_secontab/files/uploads/node_seccion_de_micrositio/2022-03/GU%C3%8DA%20BASICA%20PARA%20GENERAR%2C%20FIRMAR%20Y%20PRESENTAR%20UNA%20FACTURA%20ELECTR%C3%93NICA%20EN%20FACE.pdf"
  - "IGAE, propuesta de metadatos Facturae/ENI: https://www.igae.pap.hacienda.gob.es/sitios/igae/es-ES/Contabilidad/rcf/Documents/PropuestaNormalizaciónMetadatosFacturaeENI.pdf"
---

# Órgano gestor

## Qué es
Es la segunda de las tres unidades que debe identificar toda factura a la Administración. Según el resumen consultado (fuente secundaria), es el órgano que acepta o rechaza la factura. Su alcance concreto lo decide cada organismo.

## Cómo se usa
- En el fichero Facturae va en un nodo AdministrativeCentre con RoleTypeCode "02". Es obligatorio.
- Ejemplo de reparto en una universidad (guía de la Universidad de Jaén): el órgano gestor es la propia universidad, la unidad tramitadora es el departamento que hizo el pedido y la oficina contable es el servicio de contabilidad. En ese caso, los códigos del órgano gestor y de la oficina contable son siempre los mismos.

## De qué sistemas depende
- DIR3: su código sale de este directorio.
- RCF: el RCF mantiene un catálogo de órganos gestores, cada uno identificado con su código DIR3.

## Cómo se crea
- El órgano gestor debe estar dado de alta en el catálogo de órganos gestores del RCF.
- Para eso es imprescindible que antes esté dado de alta en DIR3. Si no lo está, se solicita su alta en DIR3.
- PENDIENTE DE VALIDAR: quién gestiona esto en cada organismo y cómo se comunican los datos al proveedor.

## Qué preguntar al usuario (sugerencia, no procede de las fuentes)
- ¿Qué código DIR3 de órgano gestor llevaba la factura?
- ¿Es el que el organismo le indicó para facturar?

## Diagrama
```mermaid
flowchart TD
    A{¿Existe el órgano en DIR3?} -- No --> B[Solicitar alta en DIR3]
    A -- Sí --> C[Alta en el catálogo de órganos gestores del RCF]
    B --> C
    C --> D[El código se usa en las facturas]
```
