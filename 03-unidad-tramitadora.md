---
concepto: Unidad tramitadora
estado: borrador
revisado: 2026-11-22
rol_facturae: "03"
depende_de: [DIR3, RCF, organo-gestor]
relacionado: [oficina-contable, organo-gestor]
fuentes:
  - "Resumen de roles (fuente secundaria): https://taxdown.es/informacion-autonomos/face-facturas"
  - "IGAE, nota informativa sobre identificación de la unidad tramitadora: https://www.igae.pap.hacienda.gob.es/sitios/igae/es-ES/Contabilidad/rcf/Documents/Nota%20informativa%20sobre%20identificación%20de%20la%20unidad%20tramitadora.pdf"
  - "IGAE, puesta en funcionamiento del RCF en SIC'3 (nota de 2013): https://www.igae.pap.hacienda.gob.es/sitios/igae/es-ES/Contabilidad/rcf/Documents/PuestaenfuncionamientoRCFenSIC3.pdf"
  - "IGAE, actuaciones previas RCF: https://www.igae.pap.hacienda.gob.es/sitios/igae/es-ES/Contabilidad/rcf/Documents/ActuacionespreviasRCF.pdf"
---

# Unidad tramitadora

## Qué es
Es una unidad administrativa del organismo destinatario de la factura. Recibe la factura de la oficina contable y anota en el registro contable de facturas (RCF) si se acepta o se rechaza. No es la empresa que emite la factura ni un simple código: el código DIR3 es lo que la identifica.

## Cómo se usa
- En el fichero Facturae va en un nodo AdministrativeCentre con RoleTypeCode "03". Es obligatoria.
- La unidad tramitadora es quien debe facilitar al proveedor su denominación y su código DIR3 para que figuren en la factura.
- Dentro de un mismo organismo suele variar de una factura a otra, porque depende de quién hizo el pedido, mientras que el órgano gestor y la oficina contable suelen ser fijos.

## De qué sistemas depende
- DIR3: de donde sale su código.
- RCF: mantiene un catálogo de unidades tramitadoras y, para cada una, a qué órganos gestores da servicio (con fecha de alta, de baja y un indicador de si está activa).
- Órgano gestor: cada unidad tramitadora está asociada a uno o varios.

## Cómo se crea
- Debe estar dada de alta en el catálogo de unidades tramitadoras del RCF.
- Para eso es imprescindible que antes esté dada de alta en DIR3; si no lo está, hay que solicitar su alta en ese directorio.
- En el ámbito de SIC'3 (IGAE), según una nota de 2013, el alta se hace desde Gestión de Unidades Tramitadoras > Alta Unidad Tramitadora Factura.
- La misma nota recomienda que las oficinas desglosen su estructura en DIR3: si no se dan de alta las unidades que necesitan, todas las facturas llegan a una sola de las áreas.
- PENDIENTE DE VALIDAR: el procedimiento vigente, porque la nota es de 2013, y cómo se hace en la AEAD.

## Qué preguntar al usuario (sugerencia, no procede de las fuentes)
- ¿Qué código DIR3 de unidad tramitadora llevaba la factura?
- ¿Se lo facilitó el propio organismo? ¿Está dado de alta y activo en DIR3 y en el RCF?

## Diagrama
```mermaid
flowchart TD
    A{¿Existe la unidad en DIR3?} -- No --> B[Solicitar alta en DIR3]
    A -- Sí --> C[Alta en el catálogo de unidades tramitadoras del RCF]
    B --> C
    C --> D[La unidad comunica su código al proveedor]
    D --> E[El proveedor lo incluye en la factura]
```
