<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: AisVessel  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/AisVessel/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Esquema NGSI-LD para la entidad AisVessel, que representa la información AIS de los buques desde diferentes fuentes de datos AIS**  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o formatos/patrones diferentes</sub></sup>  
- `aisTypeSummary[string]`: Resumen del tipo de buque AIS  - `alternateName[string]`: Un nombre alternativo para este elemento  - `averageSpeed[number]`: Velocidad media en el último viaje  - `beam[number]`: Manga o ancho  - `callSign[string]`: Señal de llamada del buque  - `courseOverGround[number]`: Curso sobre el terreno (grados)  - `createdAt[date-time]`: Hora de creación del registro (ISO 8601)  - `currentPortCountry[string]`: País del puerto actual  - `currentPortId[number]`: ID del puerto actual  - `currentPortName[string]`: Nombre del puerto actual  - `currentPortUnlocode[string]`: UN/LOCODE del puerto actual  - `dataProvider[string]`: Proveedor de datos AIS  - `dateCreated[date-time]`: Marca de tiempo de creación de la entidad. Esto suele ser asignado por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Esto suele ser asignado por la plataforma de almacenamiento  - `deletedAt[date-time]`: Hora de eliminación lógica (ISO 8601)  - `description[string]`: Una descripción de este elemento  - `destination[string]`: Destino del buque  - `distanceToGo[number]`: Distancia restante al destino  - `distanceToPort[number]`: Distancia al puerto  - `distanceTravelled[number]`: Distancia recorrida desde el último puerto  - `draught[number]`: Calado del buque  - `dsrc[string]`: Fuente AIS (TER, SAT, ROAM)  - `dwt[number]`: Arqueo bruto  - `eta[date-time]`: Hora estimada de llegada (ISO 8601)  - `etaCalculated[date-time]`: ETA calculada (ISO 8601)  - `etaUpdatedAt[date-time]`: Hora de la última actualización de la ETA (ISO 8601)  - `expectedArrival[boolean]`: ¿Se espera que el buque llegue  - `flagCode[string]`: Código de la bandera del país  - `gt[number]`: Arqueo bruto  - `heading[number]`: Rumbo en grados  - `id[*]`: Identificador único de la entidad  - `imo[number]`: Número IMO del buque  - `lastPortCode[string]`: Código del puerto anterior  - `lastPortCountry[string]`: País del último puerto  - `lastPortId[number]`: ID del último puerto  - `lastPortName[string]`: Nombre del último puerto  - `lastPortTime[date-time]`: Hora de salida del último puerto (ISO 8601)  - `lastPortUnlocode[string]`: UN/LOCODE del último puerto  - `latitude[number]`: Latitud en grados decimales  - `lfore[number]`: Distancia desde la estación AIS hasta la proa  - `loa[number]`: Longitud total  - `longitude[number]`: Longitud en grados decimales  - `market[string]`: Mercado comercial del buque  - `maxSpeed[number]`: Velocidad máxima registrada  - `mmsi[number]`: Número MMSI del buque  - `modifiedAt[date-time]`: Hora de la última modificación (ISO 8601)  - `name[string]`: El nombre de este elemento  - `navigationStatus[number]`: ID del estado de navegación  - `nextPortCode[string]`: Código del próximo puerto  - `nextPortCountry[string]`: País del próximo puerto  - `nextPortId[number]`: ID del próximo puerto  - `nextPortName[string]`: Nombre del próximo puerto  - `nextPortUnlocode[string]`: UN/LOCODE del próximo puerto  - `observedAt[date-time]`: Marca de tiempo de la última observación (ISO 8601)  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificados en JSON que hacen referencia a los ID únicos de los propietarios  - `portCallNumber[string]`: Número de la llamada al puerto  - `portCode[string]`: Código del puerto actual  - `publishedAt[date-time]`: Hora en que se publicó el registro (ISO 8601)  - `rot[number]`: Tasa de giro  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el elemento  - `shipClass[string]`: Clase del buque  - `shipCountry[string]`: País del buque  - `shipType[string]`: Tipo de buque desde AIS  - `source[string]`: Una secuencia de caracteres que da la fuente original de los datos de la entidad como una URL. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente o la URL del objeto de la fuente  - `speedOverGround[number]`: Velocidad sobre el terreno (nudos)  - `type[string]`: Tipo de entidad NGSI. Debe ser 'AisVessel'  - `typeName[string]`: Nombre del tipo de buque de MarineTraffic  - `utcSeconds[number]`: Segundos UTC de la ranura de tiempo AIS  - `vesselInPort[boolean]`: ¿El buque está actualmente en el puerto  - `vesselName[string]`: Nombre del buque  - `vesselRef[string]`: Referencia maestra única del buque  - `wleft[number]`: Distancia desde la estación AIS hasta el costado del puerto  - `yearBuilt[number]`: Año en que se construyó el buque  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades obligatorias  
- `id`  - `latitude`  - `longitude`  - `mmsi`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Descripción del modelo de datos de las propiedades  
Ordenadas alfabéticamente (haga clic para obtener detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>detalles de yaml completos</strong></summary>    
```yaml  
AisVessel:    
  description: NGSI-LD schema for AisVessel entity, representing vessel AIS information from different AIS data-sources    
  properties:    
    aisTypeSummary:    
      description: AIS ship type summary    
      type: string    
      x-ngsi:    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    averageSpeed:    
      description: Average speed on last voyage    
      type: number    
      x-ngsi:    
        type: Property    
    beam:    
      description: Beam or width    
      type: number    
      x-ngsi:    
        type: Property    
        units: meters    
    callSign:    
      description: Call sign of the vessel    
      type: string    
      x-ngsi:    
        type: Property    
    courseOverGround:    
      description: Course over ground (degrees)    
      type: number    
      x-ngsi:    
        type: Property    
    createdAt:    
      description: Record creation time (ISO 8601)    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    currentPortCountry:    
      description: Country of current port    
      type: string    
      x-ngsi:    
        type: Property    
    currentPortId:    
      description: Current port ID    
      type: number    
      x-ngsi:    
        type: Property    
    currentPortName:    
      description: Current port name    
      type: string    
      x-ngsi:    
        type: Property    
    currentPortUnlocode:    
      description: UN/LOCODE of current port    
      type: string    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: AIS data provider    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    deletedAt:    
      description: Logical deletion time (ISO 8601)    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    destination:    
      description: Destination of the vessel    
      type: string    
      x-ngsi:    
        type: Property    
    distanceToGo:    
      description: Remaining distance to destination    
      type: number    
      x-ngsi:    
        type: Property    
    distanceToPort:    
      description: Distance to the port    
      type: number    
      x-ngsi:    
        type: Property    
    distanceTravelled:    
      description: Distance travelled since last port    
      type: number    
      x-ngsi:    
        type: Property    
    draught:    
      description: Draught of the vessel    
      type: number    
      x-ngsi:    
        type: Property    
        units: meters    
    dsrc:    
      description: AIS source (TER, SAT, ROAM)    
      type: string    
      x-ngsi:    
        type: Property    
    dwt:    
      description: Deadweight tonnage    
      type: number    
      x-ngsi:    
        type: Property    
    eta:    
      description: Estimated Time of Arrival (ISO 8601)    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    etaCalculated:    
      description: Calculated ETA (ISO 8601)    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    etaUpdatedAt:    
      description: ETA last updated (ISO 8601)    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    expectedArrival:    
      description: Is the vessel expected to arrive    
      type: boolean    
      x-ngsi:    
        type: Property    
    flagCode:    
      description: Country flag code    
      type: string    
      x-ngsi:    
        type: Property    
    gt:    
      description: Gross Tonnage    
      type: number    
      x-ngsi:    
        type: Property    
    heading:    
      description: Heading in degrees    
      type: number    
      x-ngsi:    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Relationship    
    imo:    
      description: IMO number of the vessel    
      type: number    
      x-ngsi:    
        type: Property    
    lastPortCode:    
      description: Previous port code    
      type: string    
      x-ngsi:    
        type: Property    
    lastPortCountry:    
      description: Country of last port    
      type: string    
      x-ngsi:    
        type: Property    
    lastPortId:    
      description: ID of the last port    
      type: number    
      x-ngsi:    
        type: Property    
    lastPortName:    
      description: Name of last port    
      type: string    
      x-ngsi:    
        type: Property    
    lastPortTime:    
      description: Departure time from last port (ISO 8601)    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    lastPortUnlocode:    
      description: UN/LOCODE of last port    
      type: string    
      x-ngsi:    
        type: Property    
    latitude:    
      description: Latitude in decimal degrees    
      type: number    
      x-ngsi:    
        type: Property    
    lfore:    
      description: Distance from AIS station to bow    
      type: number    
      x-ngsi:    
        type: Property    
    loa:    
      description: Length Overall    
      type: number    
      x-ngsi:    
        type: Property    
        units: meters    
    longitude:    
      description: Longitude in decimal degrees    
      type: number    
      x-ngsi:    
        type: Property    
    market:    
      description: Vessel's commercial market    
      type: string    
      x-ngsi:    
        type: Property    
    maxSpeed:    
      description: Maximum speed recorded    
      type: number    
      x-ngsi:    
        type: Property    
    mmsi:    
      description: MMSI number of the vessel    
      type: number    
      x-ngsi:    
        type: Property    
    modifiedAt:    
      description: Last modification time (ISO 8601)    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    navigationStatus:    
      description: Navigation status ID    
      type: number    
      x-ngsi:    
        type: Property    
    nextPortCode:    
      description: Next port code    
      type: string    
      x-ngsi:    
        type: Property    
    nextPortCountry:    
      description: Next port country    
      type: string    
      x-ngsi:    
        type: Property    
    nextPortId:    
      description: Next port ID    
      type: number    
      x-ngsi:    
        type: Property    
    nextPortName:    
      description: Next port name    
      type: string    
      x-ngsi:    
        type: Property    
    nextPortUnlocode:    
      description: UN/LOCODE of next port    
      type: string    
      x-ngsi:    
        type: Property    
    observedAt:    
      description: Timestamp of the last observation (ISO 8601)    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Relationship    
      type: array    
      x-ngsi:    
        type: Property    
    portCallNumber:    
      description: Number of the port call    
      type: string    
      x-ngsi:    
        type: Property    
    portCode:    
      description: Current port code    
      type: string    
      x-ngsi:    
        type: Property    
    publishedAt:    
      description: Time when record was published (ISO 8601)    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    rot:    
      description: Rate of Turn    
      type: number    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    shipClass:    
      description: Class of the vessel    
      type: string    
      x-ngsi:    
        type: Property    
    shipCountry:    
      description: Country of the ship    
      type: string    
      x-ngsi:    
        type: Property    
    shipType:    
      description: Ship type from AIS    
      type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    speedOverGround:    
      description: Speed over ground (knots)    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. Must be 'AisVessel'    
      enum:    
        - AisVessel    
      type: string    
      x-ngsi:    
        type: Property    
    typeName:    
      description: MarineTraffic ship type name    
      type: string    
      x-ngsi:    
        type: Property    
    utcSeconds:    
      description: UTC seconds of AIS timeslot    
      type: number    
      x-ngsi:    
        type: Property    
    vesselInPort:    
      description: Is the vessel currently in port    
      type: boolean    
      x-ngsi:    
        type: Property    
    vesselName:    
      description: Name of the vessel    
      type: string    
      x-ngsi:    
        type: Property    
    vesselRef:    
      description: Unique Master Vessel Reference    
      type: string    
      x-ngsi:    
        type: Property    
    wleft:    
      description: Distance from AIS station to port side    
      type: number    
      x-ngsi:    
        type: Property    
    yearBuilt:    
      description: Year the vessel was built    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - mmsi    
    - latitude    
    - longitude    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/AisVessel/LICENSE.md    
  x-model-schema: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/AisVessel/schema.json    
  x-model-tags: ''    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplos de cargas útiles    
#### Ejemplo de AisVessel NGSI-v2 clave-valor    
Aquí hay un ejemplo de un AisVessel en formato JSON como clave-valor. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>mostrar/ocultar ejemplo</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:aisvessel:mtid:11221",  
  "type": "AisVessel",  
  "distanceTravelled": 200,  
  "beam": 17.2,  
  "callSign": "PDSW",  
  "courseOverGround": 48,  
  "destination": "MA MOH > ESHUV",  
  "draught": 47,  
  "dwt": 4995,  
  "eta": "2025-11-08T20:00:00Z",  
  "flagCode": "NL",  
  "gt": 4703,  
  "heading": 322,  
  "imo": 9753832,  
  "latitude": 37.104038,  
  "loa": 108,  
  "longitude": -6.859847,  
  "maxSpeed": 12.3,  
  "mmsi": 244994000,  
  "navigationStatus": 1,  
  "portCallNumber": "ESHUV202501140",  
  "speedOverGround": 0.1,  
  "vesselName": "BITUMA",  
  "vesselRef": "urn:mrn:eshuv:portcalls:mastervessel:id:8028",  
  "dataProvider": "MarineTraffic",  
  "aisTypeSummary": "Tanker",  
  "averageSpeed": 11.2,  
  "currentPortCountry": "ES",  
  "currentPortId": 20645,  
  "currentPortName": "HUELVA ANCH",  
  "currentPortUnlocode": "ESHUV",  
  "distanceToGo": 0,  
  "distanceToPort": 7.86,  
  "dsrc": "TERR",  
  "etaCalculated": "2025-11-08T19:54:00Z",  
  "etaUpdatedAt": "2025-11-08T19:35:00Z",  
  "lastPortCountry": "MA",  
  "lastPortId": 811,  
  "lastPortName": "MOHAMMEDIA",  
  "lastPortTime": "2025-11-08T01:41:00Z",  
  "lastPortUnlocode": "MAMOH",  
  "lfore": 86,  
  "nextPortCountry": "ES",  
  "nextPortId": 1669,  
  "nextPortName": "HUELVA",  
  "nextPortUnlocode": "ESHUV",  
  "rot": 0,  
  "shipClass": "HANDYSIZE",  
  "shipCountry": "Netherlands",  
  "shipType": "80",  
  "utcSeconds": 21,  
  "vesselInPort": true,  
  "wleft": 2,  
  "yearBuilt": 2016,  
  "typeName": "Oil/Chemical Tanker",  
  "market": "WET BULK"  
}  
```  
</details>  
#### Ejemplo de AisVessel NGSI-v2 normalizado    
Aquí hay un ejemplo de un AisVessel en formato JSON como normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>mostrar/ocultar ejemplo</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:aisvessel:mtid:11221",  
  "type": "AisVessel",  
  "distanceTravelled": {  
    "type": "Number",  
    "value": 200  
  },  
  "beam": {  
    "type": "Number",  
    "value": 17.2  
  },  
  "callSign": {  
    "type": "Text",  
    "value": "PDSW"  
  },  
  "courseOverGround": {  
    "type": "Number",  
    "value": 48  
  },  
  "destination": {  
    "type": "Text",  
    "value": "MA MOH > ESHUV"  
  },  
  "draught": {  
    "type": "Number",  
    "value": 47  
  },  
  "dwt": {  
    "type": "Number",  
    "value": 4995  
  },  
  "eta": {  
    "type": "DateTime",  
    "value": "2025-11-08T20:00:00Z"  
  },  
  "flagCode": {  
    "type": "Text",  
    "value": "NL"  
  },  
  "gt": {  
    "type": "Number",  
    "value": 4703  
  },  
  "heading": {  
    "type": "Number",  
    "value": 322  
  },  
  "imo": {  
    "type": "Number",  
    "value": 9753832  
  },  
  "latitude": {  
    "type": "Number",  
    "value": 37.104038  
  },  
  "loa": {  
    "type": "Number",  
    "value": 108  
  },  
  "longitude": {  
    "type": "Number",  
    "value": -6.859847  
  },  
  "maxSpeed": {  
    "type": "Number",  
    "value": 12.3  
  },  
  "mmsi": {  
    "type": "Number",  
    "value": 244994000  
  },  
  "navigationStatus": {  
    "type": "Number",  
    "value": 1  
  },  
  "portCallNumber": {  
    "type": "Text",  
    "value": "ESHUV202501140"  
  },  
  "speedOverGround": {  
    "type": "Number",  
    "value": 0.1  
  },  
  "vesselName": {  
    "type": "Text",  
    "value": "BITUMA"  
  },  
  "vesselRef": {  
    "type": "Text",  
    "value": "urn:mrn:eshuv:portcalls:mastervessel:id:8028"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "MarineTraffic"  
  },  
  "aisTypeSummary": {  
    "type": "Text",  
    "value": "Tanker"  
  },  
  "averageSpeed": {  
    "type": "Number",  
    "value": 11.2  
  },  
  "currentPortCountry": {  
    "type": "Text",  
    "value": "ES"  
  },  
  "currentPortId": {  
    "type": "Number",  
    "value": 20645  
  },  
  "currentPortName": {  
    "type": "Text",  
    "value": "HUELVA ANCH"  
  },  
  "currentPortUnlocode": {  
    "type": "Text",  
    "value": "ESHUV"  
  },  
  "distanceToGo": {  
    "type": "Number",  
    "value": 0  
  },  
  "distanceToPort": {  
    "type": "Number",  
    "value": 7.86  
  },  
  "dsrc": {  
    "type": "Text",  
    "value": "TERR"  
  },  
  "etaCalculated": {  
    "type": "DateTime",  
    "value": "2025-11-08T19:54:00Z"  
  },  
  "etaUpdatedAt": {  
    "type": "DateTime",  
    "value": "2025-11-08T19:35:00Z"  
  },  
  "lastPortCountry": {  
    "type": "Text",  
    "value": "MA"  
  },  
  "lastPortId": {  
    "type": "Number",  
    "value": 811  
  },  
  "lastPortName": {  
    "type": "Text",  
    "value": "MOHAMMEDIA"  
  },  
  "lastPortTime": {  
    "type": "DateTime",  
    "value": "2025-11-08T01:41:00Z"  
  },  
  "lastPortUnlocode": {  
    "type": "Text",  
    "value": "MAMOH"  
  },  
  "lfore": {  
    "type": "Number",  
    "value": 86  
  },  
  "nextPortCountry": {  
    "type": "Text",  
    "value": "ES"  
  },  
  "nextPortId": {  
    "type": "Number",  
    "value": 1669  
  },  
  "nextPortName": {  
    "type": "Text",  
    "value": "HUELVA"  
  },  
  "nextPortUnlocode": {  
    "type": "Text",  
    "value": "ESHUV"  
  },  
  "rot": {  
    "type": "Number",  
    "value": 0  
  },  
  "shipClass": {  
    "type": "Text",  
    "value": "HANDYSIZE"  
  },  
  "shipCountry": {  
    "type": "Text",  
    "value": "Netherlands"  
  },  
  "shipType": {  
    "type": "Text",  
    "value": "80"  
  },  
  "utcSeconds": {  
    "type": "Number",  
    "value": 21  
  },  
  "vesselInPort": {  
    "type": "Boolean",  
    "value": true  
  },  
  "wleft": {  
    "type": "Number",  
    "value": 2  
  },  
  "yearBuilt": {  
    "type": "Number",  
    "value": 2016  
  },  
  "typeName": {  
    "type": "Text",  
    "value": "Oil/Chemical Tanker"  
  },  
  "market": {  
    "type": "Text",  
    "value": "WET BULK"  
  }  
}  
```  
</details>  
#### Ejemplo de AisVessel NGSI-LD clave-valor    
Aquí hay un ejemplo de un AisVessel en formato JSON-LD como clave-valor. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>mostrar/ocultar ejemplo</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AisVessel:urn:mrn:eshuv:portcalls:aisvessel:mtid:11221",  
  "type": "AisVessel",  
  "distanceTravelled": 200,  
  "beam": 17.2,  
  "callSign": "PDSW",  
  "courseOverGround": 48,  
  "destination": "MA MOH > ESHUV",  
  "draught": 47,  
  "dwt": 4995,  
  "eta": "2025-11-08T20:00:00Z",  
  "flagCode": "NL",  
  "gt": 4703,  
  "heading": 322,  
  "imo": 9753832,  
  "latitude": 37.104038,  
  "loa": 108,  
  "longitude": -6.859847,  
  "maxSpeed": 12.3,  
  "mmsi": 244994000,  
  "navigationStatus": 1,  
  "portCallNumber": "ESHUV202501140",  
  "speedOverGround": 0.1,  
  "vesselName": "BITUMA",  
  "vesselRef": "urn:mrn:eshuv:portcalls:mastervessel:id:8028",  
  "dataProvider": "MarineTraffic",  
  "aisTypeSummary": "Tanker",  
  "averageSpeed": 11.2,  
  "currentPortCountry": "ES",  
  "currentPortId": 20645,  
  "currentPortName": "HUELVA ANCH",  
  "currentPortUnlocode": "ESHUV",  
  "distanceToGo": 0,  
  "distanceToPort": 7.86,  
  "dsrc": "TERR",  
  "etaCalculated": "2025-11-08T19:54:00Z",  
  "etaUpdatedAt": "2025-11-08T19:35:00Z",  
  "lastPortCountry": "MA",  
  "lastPortId": 811,  
  "lastPortName": "MOHAMMEDIA",  
  "lastPortTime": "2025-11-08T01:41:00Z",  
  "lastPortUnlocode": "MAMOH",  
  "lfore": 86,  
  "nextPortCountry": "ES",  
  "nextPortId": 1669,  
  "nextPortName": "HUELVA",  
  "nextPortUnlocode": "ESHUV",  
  "rot": 0,  
  "shipClass": "HANDYSIZE",  
  "shipCountry": "Netherlands",  
  "shipType": "80",  
  "utcSeconds": 21,  
  "vesselInPort": true,  
  "wleft": 2,  
  "yearBuilt": 2016,  
  "typeName": "Oil/Chemical Tanker",  
  "market": "WET BULK",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Ejemplo de AisVessel NGSI-LD normalizado    
Aquí hay un ejemplo de un AisVessel en formato JSON-LD como normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>mostrar/ocultar ejemplo</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AisVessel:urn:mrn:eshuv:portcalls:aisvessel:mtid:11221",  
  "type": "AisVessel",  
  "distanceTravelled": {  
    "type": "Property",  
    "value": 200  
  },  
  "beam": {  
    "type": "Property",  
    "value": 17.2  
  },  
  "callSign": {  
    "type": "Property",  
    "value": "PDSW"  
  },  
  "courseOverGround": {  
    "type": "Property",  
    "value": 48  
  },  
  "destination": {  
    "type": "Property",  
    "value": "MA MOH > ESHUV"  
  },  
  "draught": {  
    "type": "Property",  
    "value": 47  
  },  
  "dwt": {  
    "type": "Property",  
    "value": 4995  
  },  
  "eta": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2025-11-08T20:00:00Z"  
    }  
  },  
  "flagCode": {  
    "type": "Property",  
    "value": "NL"  
  },  
  "gt": {  
    "type": "Property",  
    "value": 4703  
  },  
  "heading": {  
    "type": "Property",  
    "value": 322  
  },  
  "imo": {  
    "type": "Property",  
    "value": 9753832  
  },  
  "latitude": {  
    "type": "Property",  
    "value": 37.104038  
  },  
  "loa": {  
    "type": "Property",  
    "value": 108  
  },  
  "longitude": {  
    "type": "Property",  
    "value": -6.859847  
  },  
  "maxSpeed": {  
    "type": "Property",  
    "value": 12.3  
  },  
  "mmsi": {  
    "type": "Property",  
    "value": 244994000  
  },  
  "navigationStatus": {  
    "type": "Property",  
    "value": 1  
  },  
  "portCallNumber": {  
    "type": "Property",  
    "value": "ESHUV202501140"  
  },  
  "speedOverGround": {  
    "type": "Property",  
    "value": 0.1  
  },  
  "vesselName": {  
    "type": "Property",  
    "value": "BITUMA"  
  },  
  "vesselRef": {  
    "type": "Property",  
    "value": "urn:mrn:eshuv:portcalls:mastervessel:id:8028"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "MarineTraffic"  
  },  
  "aisTypeSummary": {  
    "type": "Property",  
    "value": "Tanker"  
  },  
  "averageSpeed": {  
    "type": "Property",  
    "value": 11.2  
  },  
  "currentPortCountry": {  
    "type": "Property",  
    "value": "ES"  
  },  
  "currentPortId": {  
    "type": "Property",  
    "value": 20645  
  },  
  "currentPortName": {  
    "type": "Property",  
    "value": "HUELVA ANCH"  
  },  
  "currentPortUnlocode": {  
    "type": "Property",  
    "value": "ESHUV"  
  },  
  "distanceToGo": {  
    "type": "Property",  
    "value": 0  
  },  
  "distanceToPort": {  
    "type": "Property",  
    "value": 7.86  
  },  
  "dsrc": {  
    "type": "Property",  
    "value": "TERR"  
  },  
  "etaCalculated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2025-11-08T19:54:00Z"  
    }  
  },  
  "etaUpdatedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2025-11-08T19:35:00Z"  
    }  
  },  
  "lastPortCountry": {  
    "type": "Property",  
    "value": "MA"  
  },  
  "lastPortId": {  
    "type": "Property",  
    "value": 811  
  },  
  "lastPortName": {  
    "type": "Property",  
    "value": "MOHAMMEDIA"  
  },  
  "lastPortTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2025-11-08T01:41:00Z"  
    }  
  },  
  "lastPortUnlocode": {  
    "type": "Property",  
    "value": "MAMOH"  
  },  
  "lfore": {  
    "type": "Property",  
    "value": 86  
  },  
  "nextPortCountry": {  
    "type": "Property",  
    "value": "ES"  
  },  
  "nextPortId": {  
    "type": "Property",  
    "value": 1669  
  },  
  "nextPortName": {  
    "type": "Property",  
    "value": "HUELVA"  
  },  
  "nextPortUnlocode": {  
    "type": "Property",  
    "value": "ESHUV"  
  },  
  "rot": {  
    "type": "Property",  
    "value": 0  
  },  
  "shipClass": {  
    "type": "Property",  
    "value": "HANDYSIZE"  
  },  
  "shipCountry": {  
    "type": "Property",  
    "value": "Netherlands"  
  },  
  "shipType": {  
    "type": "Property",  
    "value": "80"  
  },  
  "utcSeconds": {  
    "type": "Property",  
    "value": 21  
  },  
  "vesselInPort": {  
    "type": "Property",  
    "value": true  
  },  
  "wleft": {  
    "type": "Property",  
    "value": 2  
  },  
  "yearBuilt": {  
    "type": "Property",  
    "value": 2016  
  },  
  "typeName": {  
    "type": "Property",  
    "value": "Oil/Chemical Tanker"  
  },  
  "market": {  
    "type": "Property",  
    "value": "WET BULK"  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar con las unidades de magnitud  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->