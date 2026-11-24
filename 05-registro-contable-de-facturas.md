---
concepto: Registro contable de facturas (RCF)
estado: borrador
revisado: 2026-11-22
depende_de: [DIR3, FACe]
relacionado: [oficina-contable, organo-gestor, unidad-tramitadora]
fuentes:
  - "Hacienda, FAQ factura electrónica: https://www.hacienda.gob.es/gl-ES/Prensa/Paginas/FAQFacturaelectronica.aspx"
  - "IGAE, puesta en funcionamiento del RCF en SIC'3: https://www.igae.pap.hacienda.gob.es/sitios/igae/es-ES/Contabilidad/rcf/Documents/PuestaenfuncionamientoRCFenSIC3.pdf"
  - "IGAE, propuesta de metadatos Facturae/ENI: https://www.igae.pap.hacienda.gob.es/sitios/igae/es-ES/Contabilidad/rcf/Documents/PropuestaNormalizaciónMetadatosFacturaeENI.pdf"
  - "IGAE, presentación del RCF: https://www.igae.pap.hacienda.gob.es/sitios/igae/es-ES/Contabilidad/rcf/Documents/PresentacionRegistroContableFactura.pdf"
---

# Registro contable de facturas (RCF)

## Qué es
Es el registro donde la oficina contable anota las facturas que recibe. Se creó con la ley de impulso de la factura electrónica y creación del registro contable de facturas en el sector público (Ley 25/2013). Responde a la duda de dónde encaja en el recorrido: es lo que ocurre después de FACe, cuando la factura llega a la oficina contable.

## Cómo se usa
- El RCF descarga de FACe las facturas dirigidas a sus oficinas contables, identificadas por el código DIR3 de cada una.
- Genera un número de registro (número RCF) para cada factura anotada.
- Mantiene tablas que relacionan cada oficina contable, órgano gestor y unidad tramitadora con su código DIR3.
- Según una guía de la IGAE, los sistemas contables comunican a FACe el último estado de la factura.

## De qué sistemas depende
- FACe: de donde descarga las facturas.
- DIR3: para identificar a las unidades.
- Sistema contable del organismo: en el ámbito de la IGAE, el RCF es un módulo de SIC'3. Otros organismos pueden usar un sistema propio.

## Cómo se crea
- Cada organismo tiene su RCF dentro de su sistema contable.
- PENDIENTE DE VALIDAR: cómo se configura en los organismos que no usan SIC'3 y el papel exacto de la AEAD.

## Qué preguntar al usuario (sugerencia, no procede de las fuentes)
- ¿La factura figura como registrada en el RCF? ¿Con qué número?
- ¿Qué estado muestra en FACe?

## Diagrama
```mermaid
flowchart LR
    P[Proveedor] --> F[FACe]
    F --> R[RCF: anotación y número RCF]
    R --> U[Unidad tramitadora]
    U --> O[Órgano gestor]
    R -. estado .-> F
```
