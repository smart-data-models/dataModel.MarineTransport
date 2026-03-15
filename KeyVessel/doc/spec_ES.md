<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: KeyVessel  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/KeyVessel/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **El modelo de datos tiene como objetivo proporcionar información sobre los buques clave en los que una comunidad portuaria debe centrar su trabajo en los próximos días. Permite representar las propiedades de cada buque: información estática y dinámica**  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque podría tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `address[object]`: La dirección de correo  . Modelo: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Modelo: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección de la calle, y que se encuentra en la región  . Modelo: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que se encuentra en el país  . Modelo: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, es gestionado por el gobierno local    
	- `postOfficeBoxNumber[string]`: El número de casilla de correos para direcciones de casilla de correos. Por ejemplo, 03578  . Modelo: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Modelo: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: La dirección de la calle  . Modelo: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Número que identifica una propiedad específica en una calle pública    
- `alternateName[string]`: Un nombre alternativo para este elemento  - `areaServed[string]`: El área geográfica donde se ofrece un servicio o elemento  . Modelo: [https://schema.org/Text](https://schema.org/Text)- `callSign[string]`: Las señales de llamada marítimas son señales de llamada asignadas como identificadores únicos a los buques  . Modelo: [https://schema.org/Text](https://schema.org/Text)- `courseOverGround[number]`: Curso sobre el terreno (COG)  . Modelo: [https://schema.org/Number](https://schema.org/Number)- `createdDate[date-time]`: Fecha y hora de creación de la entidad representada por un formato UTC ISO 8601  . Modelo: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizados  . Modelo: [https://schema.org/Text](https://schema.org/Text)- `dateCreated[date-time]`: Marca de tiempo de creación de la entidad. Esto suele ser asignado por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Esto suele ser asignado por la plataforma de almacenamiento  - `deletedDate[date-time]`: Fecha y hora de eliminación de la entidad representada por un formato UTC ISO 8601  . Modelo: [https://schema.org/Text](https://schema.org/Text)- `description[string]`: Una descripción de este elemento  - `etaAis[date-time]`: Hora estimada de llegada, como se informa por el sistema AIS, representada por un formato UTC ISO 8601  . Modelo: [https://schema.org/Text](https://schema.org/Text)- `etaAlgorithm[date-time]`: Hora estimada de llegada, calculada por un algoritmo basado en las posiciones del buque, representada por un formato UTC ISO 8601  . Modelo: [https://schema.org/Text](https://schema.org/Text)- `flagCode[string]`: Las señales de llamada marítimas son señales de llamada asignadas como identificadores únicos a los buques  . Modelo: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: Identificador único de la entidad  - `imo[number]`: Número de la Organización Marítima Internacional (un UID global para siempre)  . Modelo: [https://schema.org/Number](https://schema.org/Number)- `lastPortCode[string]`: Último puerto de escala, codificado. El código que representa el puerto inmediatamente anterior al puerto de llegada, si está disponible. [EMSWe: DE-005-05] [EDIFACT:LOC-3227-92] [IMO:IMO0076]   . Modelo: [https://schema.org/Text](https://schema.org/Text)- `latitude[number]`: Coordenada de latitud del buque  - `location[*]`: Referencia Geojson a la posición del buque. Debe ser un Punto donde el buque se encontraba en la fecha observada    
	- `longitude[number]`: Coordenada de longitud del buque  - `mmsi[number]`: Número de identidad del servicio móvil marítimo (un UID temporalmente asignado, emitido por el estado de la bandera actual del objeto)  . Modelo: [https://schema.org/Number](https://schema.org/Number)- `modifiedDate[date-time]`: Fecha y hora de la última modificación de la entidad representada por un formato UTC ISO 8601  . Modelo: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: El nombre de este elemento  - `navigationStatus[number]`: Enum:'0=En marcha utilizando motor, 1=Anclado, 2=No bajo control, 3=Maniobrabilidad restringida, 4=Limitado por su calado, 5=Atraque, 6=Varado, 7=Engañado en la pesca, 8=En marcha a vela, 9=Reservado para futuras enmiendas del estado de navegación para HSC, 10=Reservado para futuras enmiendas del estado de navegación para WIG, 11=Reservado para uso futuro, 12=Reservado para uso futuro, 13=Reservado para uso futuro, 14=AIS-SART está activo, 15=No definido (predeterminado)'. Estado de navegación. Formato de datos AIVDM/AIVDO'  . Modelo: [https://schema.org/Number](https://schema.org/Number)- `nextPortCode[string]`: Próximo puerto de escala, codificado. El código que representa el puerto inmediatamente anterior al puerto de llegada, si está disponible. Relacionado con IALA_S211: nestPortCallCod / IMO. [EMSWe: DE-005-07] [EDIFACT:LOC-3227-61] [IMO:IMO0120]  . Modelo: [https://schema.org/Text](https://schema.org/Text)- `observedDate[date-time]`: Fecha y hora de esta observación representada por un formato UTC ISO 8601  . Modelo: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificados en JSON que hacen referencia a los identificadores únicos de los propietarios(s)  - `portCallNumber[string]`: Identificador de llamada al puerto en formato MRN. El primer elemento de la NSS debe ser el código UN/LOCODE de 5 caracteres del puerto, seguido del año y terminando con un número secuencial en este puerto [LLLLLYYYY99999] donde LLLLL es el UN/LOCODE del puerto visitado, YYYY es el año y 99999 es un número secuencial único asignado por la autoridad portuaria única en cada año (por ejemplo, ESHUV202310323). Se puede utilizar una abreviatura para UN/LOCODE (por ejemplo, H202310323). El número de llamada al puerto se asigna durante los pasos iniciales de la visita, pero puede ser nulo al principio. En los estándares internacionales también se conoce como [ID de llamada al puerto], [ID de visita] o [Llamada al puerto codificada]. Ver [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) [EMSWe: DG-004/DG-004-01] [EDIFACT:BGM-1004] [IALA_S211:portCallId] [IMO:IMO108+IMO0153]  . Modelo: [https://schema.org/Text](https://schema.org/Text)- `portCallRef[uri]`: Referencia a la entidad PortCall principal. [NGSI-MarineTransport.PortCall.id]  - `portCode[string]`: Código de la Organización de las Naciones Unidas para el Comercio y el Transporte. Ver [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) [EMSWe: DE-004-04] [EDIFACT:LOC-3227-153] [IALA_S211:portCode] [IMO:IMO0108]   . Modelo: [https://schema.org/Text](https://schema.org/Text)- `positionAccuracy[number]`: Enum:'0=Bajo (> 10 m; modo autónomo de, por ejemplo, receptor de sistema de navegación global por satélite (GNSS) o de otro dispositivo de fijación de posición electrónica; predeterminado), 1=Alto (< 10 m; modo diferencial de, por ejemplo, receptor DGNSS)'. Código para la precisión de la bandera de posición del buque  . Modelo: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el elemento  - `source[string]`: Una secuencia de caracteres que da la fuente original de los datos de la entidad como una URL. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto de la fuente  - `speedOverGround[number]`: Velocidad sobre el terreno (SOG)  . Modelo: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Tipo de entidad NGSI. Debe ser KeyVessel  - `vesselAtPort[boolean]`: El buque se encuentra dentro de los límites del puerto, incluyendo la espera fuera, en la entrada del puerto, esperando instrucciones, etc  . Modelo: [https://schema.org/Boolean](https://schema.org/Boolean)- `vesselName[string]`: Nombre del buque  . Modelo: [https://schema.org/Text](https://schema.org/Text)- `vesselRef[uri]`: Referencia a la entidad MasterVessel principal. [NGSI-MarineTransport.MasterVessel.id]- urn:mrn:<oid>:portcalls:mastervessel:id:9999  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades obligatorias  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Descripción del modelo de datos de las propiedades  
Ordenadas alfabéticamente (haga clic para obtener detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>detalles de yaml completos</strong></summary>    
```yaml  
KeyVessel:    
  description: 'The data model is intended to provide information about key vessels that a port community must focus his work on next days. It allows to represent the properties of each vessel: static and dynamic information'    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: The country. For example, Spain    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: The locality in which the street address is, and which is in the region    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: The region in which the locality is, and which is in the country    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: A district is a type of administrative division that, in some countries, is managed by the local government    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: The post office box number for PO box addresses. For example, 03578    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: The postal code. For example, 24004    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    callSign:    
      description: Maritime call signs are call signs assigned as unique identifiers to vessels    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    courseOverGround:    
      description: Course Over Ground (COG)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: degree    
    createdDate:    
      description: Date and time of creation of the entity represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      enum:    
        - AIS    
        - AISHUB    
        - ALGORITHM    
        - IA    
        - MARINETRAFFIC    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    deletedDate:    
      description: Date and time of deletion of the entity represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    etaAis:    
      description: Estimated time of arrival, as it is reported by AIS system, represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    etaAlgorithm:    
      description: Estimated time of arrival, computed by an algorithm based on vessel's positions, represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    flagCode:    
      description: Maritime call signs are call signs assigned as unique identifiers to vessels    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
      description: International Maritime Organization Number (a global forever UID)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    lastPortCode:    
      description: 'Last port of call, coded.The code representing the port immediately previous to the port of arrival, if available. [EMSWe: DE-005-05] [EDIFACT:LOC-3227-92] [IMO:IMO0076] '    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    latitude:    
      description: Latitude coordinate of the vessel    
      type: number    
      x-ngsi:    
        type: Property    
    location:    
      '@id': http://uri.etsi.org/ngsi-ld/location    
      '@type': https://uri.etsi.org/ngsi-ld/GeoProperty    
      description: Geojson reference to the vessel position. It must be a Point where the vessel was placed at observedDate date    
      x-ngsi:    
        type: GeoProperty    
    longitude:    
      description: Longitude coordinate of the vessel    
      type: number    
      x-ngsi:    
        type: Property    
    mmsi:    
      description: Marine Mobile Service Identity Number (a temporarily assigned UID, issued by that object's current flag state)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    modifiedDate:    
      description: Date and time of last modification of the entity represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    navigationStatus:    
      description: Enum:'0=Under way using engine, 1=At anchor, 2=Not under command, 3=Restricted manoeuverability,4=Constrained by her draught, 5=Moored, 6=Aground, 7=Engaged in Fishing, 8=Under way sailing, 9=Reserved for future amendment of Navigational state for HSC, 10=Reserved for future amendment of Navigational Status for WIG, 11=Reserved for future use, 12=Reserved for future use,13=Reserved for future use, 14=AIS-SART is active, 15=Not defined (default)'. Navigation Status. AIVDM/AIVDO data format'    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
        - 6    
        - 7    
        - 8    
        - 9    
        - 10    
        - 11    
        - 12    
        - 13    
        - 14    
        - 15    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    nextPortCode:    
      description: 'Next port of call, coded.The code representing the port immediately previous to the port of arrival, if available.. Related to IALA_S211:nestPortCallCod / IMO. [EMSWe: DE-005-07] [EDIFACT:LOC-3227-61] [IMO:IMO0120]'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    observedDate:    
      description: Date and time of this observation represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
      description: 'Port call identifier in MRN format. First element of the NSS should be the 5 character UN/Locode of the port, later the YEAR and finishing with a sequential number in this port [LLLLLYYYY99999] where LLLLL is the UN/LOCODE of the visited port, YYYY is the year, and 99999 is a unique sequential number assigned by port authority unique on each year (i.e. ESHUV202310323). An abbreviation can be used for UN/LOCODE (i.e. H202310323). The portCallNumber is assigned during the initial steps of the visit, but could be null at the beginning. In international standards is also known as [Port Call ID], [Visit ID] or [Port Call Coded]. See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) [EMSWe: DG-004/DG-004-01] [EDIFACT:BGM-1004] [IALA_S211:portCallId] [IMO:IMO108+IMO0153]'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    portCallRef:    
      description: Reference to parent PortCall entity. [NGSI-MarineTransport.PortCall.id]    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    portCode:    
      description: 'United Nations Code for Trade and Transport Locations. See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) [EMSWe: DE-004-04] [EDIFACT:LOC-3227-153] [IALA_S211:portCode] [IMO:IMO0108] '    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    positionAccuracy:    
      description: Enum:'0=Low (> 10 m; autonomous mode of e.g.global navigation satellite system (GNSS) receiver or of other electronic position fixing device; default), 1=High (< 10 m; differential mode of e.g.DGNSS receiver)'. Code for the accuracy of the vessel position flag    
      enum:    
        - 0    
        - 1    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    source:    
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    speedOverGround:    
      description: Speed Over Ground (SOG)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meters per second    
    type:    
      description: NGSI Entity type. It has to be KeyVessel    
      enum:    
        - KeyVessel    
      type: string    
      x-ngsi:    
        type: Property    
    vesselAtPort:    
      description: The vessel is in port limits, including waiting outside, at the harbor entrance, awaiting instructions, etc    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    vesselName:    
      description: Vessel Name    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vesselRef:    
      description: Reference to parent MasterVessel entity. [NGSI-MarineTransport.MasterVessel.id]- urn:mrn:<oid>:portcalls:mastervessel:id:9999    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/KeyVessel/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/VesselAtPort/schema.json    
  x-model-tags: I4Trust    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplos de cargas    
#### Ejemplo de KeyVessel NGSI-v2 clave-valor    
Aquí hay un ejemplo de un KeyVessel en formato JSON como clave-valor. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>mostrar/ocultar ejemplo</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:portcallvessel:id:1234",  
  "type": "KeyVessel",  
  "vesselRef": "urn:mrn:eshuv:portcalls:mastervessel:imo:9863637",  
  "imo": 9863637,  
  "mmsi": 210049000,  
  "callSign": "5BPC3",  
  "flagCode": "ES",  
  "vesselName": "ELEANOR R.",  
  "portCode":   "ESHUV",  
  "lastPortCode": "ESPMI",  
  "nextPortCode": "ESVLC",  
  "portCallNumber": "ESHUV202401233",  
  "portCallRef": "urn:mrn:eshuv:portcalls:portcall:code:1233",  
  "dataProvider": "AIS",  
  "latitude": 37.2614,  
  "longitude":  -6.9447,  
  "speedOverGround": 11.3,  
  "courseOverGround": 122,  
  "navigationStatus": 4,  
  "observedDate": "2024-07-01T03:11:32Z",  
  "modifiedDate": "2024-07-01T03:07:12Z",  
  "createdDate": "2023-06-03T07:00:00Z",  
  "deletedDate": "2024-07-01T03:07:12Z"  
}  
```  
</details>  
#### Ejemplo de KeyVessel NGSI-v2 normalizado    
Aquí hay un ejemplo de un KeyVessel en formato JSON como normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>mostrar/ocultar ejemplo</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:portcallvessel:id:1234",  
  "type": "KeyVessel",  
  "vesselRef": {  
    "type": "Text",  
    "value": "urn:mrn:eshuv:portcalls:mastervessel:imo:9863637"  
  },  
  "imo": {  
    "type": "Number",  
    "value": 9863637  
  },  
  "mmsi": {  
    "type": "Number",  
    "value": 210049000  
  },  
  "callSign": {  
    "type": "Text",  
    "value": "5BPC3"  
  },  
  "flagCode": {  
    "type": "Text",  
    "value": "ES"  
  },  
  "vesselName": {  
    "type": "Text",  
    "value": "ELEANOR R."  
  },  
  "portCode": {  
    "type": "Text",  
    "value": "ESHUV"  
  },  
  "lastPortCode": {  
    "type": "Text",  
    "value": "ESPMI"  
  },  
  "nextPortCode": {  
    "type": "Text",  
    "value": "ESVLC"  
  },  
  "portCallNumber": {  
    "type": "Text",  
    "value": "ESHUV202401233"  
  },  
  "portCallRef": {  
    "type": "Text",  
    "value": "urn:mrn:eshuv:portcalls:portcall:code:1233"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "AIS"  
  },  
  "latitude": {  
    "type": "Number",  
    "value": 37.2614  
  },  
  "longitude": {  
    "type": "Number",  
    "value": -6.9447  
  },  
  "speedOverGround": {  
    "type": "Number",  
    "value": 11.3  
  },  
  "courseOverGround": {  
    "type": "Number",  
    "value": 122  
  },  
  "navigationStatus": {  
    "type": "Number",  
    "value": 4  
  },  
  "observedDate": {  
    "type": "DateTime",  
    "value": "2024-07-01T03:11:32Z"  
  },  
  "modifiedDate": {  
    "type": "DateTime",  
    "value": "2024-07-01T03:07:12Z"  
  },  
  "createdDate": {  
    "type": "DateTime",  
    "value": "2023-06-03T07:00:00Z"  
  },  
  "deletedDate": {  
    "type": "DateTime",  
    "value": "2024-07-01T03:07:12Z"  
  }  
}  
```  
</details>  
#### Ejemplo de KeyVessel NGSI-LD clave-valor    
Aquí hay un ejemplo de un KeyVessel en formato JSON-LD como clave-valor. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>mostrar/ocultar ejemplo</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:KeyVessel:urn:mrn:eshuv:portcalls:portcallvessel:id:1234",  
  "type": "KeyVessel",  
  "vesselRef": "urn:mrn:eshuv:portcalls:mastervessel:imo:9863637",  
  "imo": 9863637,  
  "mmsi": 210049000,  
  "callSign": "5BPC3",  
  "flagCode": "ES",  
  "vesselName": "ELEANOR R.",  
  "portCode": "ESHUV",  
  "lastPortCode": "ESPMI",  
  "nextPortCode": "ESVLC",  
  "portCallNumber": "ESHUV202401233",  
  "portCallRef": "urn:mrn:eshuv:portcalls:portcall:code:1233",  
  "dataProvider": "AIS",  
  "latitude": 37.2614,  
  "longitude": -6.9447,  
  "speedOverGround": 11.3,  
  "courseOverGround": 122,  
  "navigationStatus": 4,  
  "observedDate": "2024-07-01T03:11:32Z",  
  "modifiedDate": "2024-07-01T03:07:12Z",  
  "createdDate": "2023-06-03T07:00:00Z",  
  "deletedDate": "2024-07-01T03:07:12Z",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Ejemplo de KeyVessel NGSI-LD normalizado    
Aquí hay un ejemplo de un KeyVessel en formato JSON-LD como normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>mostrar/ocultar ejemplo</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:KeyVessel:urn:mrn:eshuv:portcalls:portcallvessel:id:1234",  
  "type": "KeyVessel",  
  "vesselRef": {  
    "type": "Property",  
    "value": "urn:mrn:eshuv:portcalls:mastervessel:imo:9863637"  
  },  
  "imo": {  
    "type": "Property",  
    "value": 9863637  
  },  
  "mmsi": {  
    "type": "Property",  
    "value": 210049000  
  },  
  "callSign": {  
    "type": "Property",  
    "value": "5BPC3"  
  },  
  "flagCode": {  
    "type": "Property",  
    "value": "ES"  
  },  
  "vesselName": {  
    "type": "Property",  
    "value": "ELEANOR R."  
  },  
  "portCode": {  
    "type": "Property",  
    "value": "ESHUV"  
  },  
  "lastPortCode": {  
    "type": "Property",  
    "value": "ESPMI"  
  },  
  "nextPortCode": {  
    "type": "Property",  
    "value": "ESVLC"  
  },  
  "portCallNumber": {  
    "type": "Property",  
    "value": "ESHUV202401233"  
  },  
  "portCallRef": {  
    "type": "Property",  
    "value": "urn:mrn:eshuv:portcalls:portcall:code:1233"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "AIS"  
  },  
  "latitude": {  
    "type": "Property",  
    "value": 37.2614  
  },  
  "longitude": {  
    "type": "Property",  
    "value": -6.9447  
  },  
  "speedOverGround": {  
    "type": "Property",  
    "value": 11.3  
  },  
  "courseOverGround": {  
    "type": "Property",  
    "value": 122  
  },  
  "navigationStatus": {  
    "type": "Property",  
    "value": 4  
  },  
  "observedDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-07-01T03:11:32Z"  
    }  
  },  
  "modifiedDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-07-01T03:07:12Z"  
    }  
  },  
  "createdDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2023-06-03T07:00:00Z"  
    }  
  },  
  "deletedDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-07-01T03:07:12Z"  
    }  
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
Ver [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar con unidades de magnitud  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
