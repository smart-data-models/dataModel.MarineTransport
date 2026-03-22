<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: Terminal  
================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/Terminal/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Este modelo de datos describe un terminal en un puerto como una unión de instalaciones y terreno, que se puede utilizar para diversas operaciones marítimas.**  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `address[object]`: La dirección de correo  . Modelo: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Modelo: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección de la calle, y que está en la región  . Modelo: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Modelo: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, es gestionado por el gobierno local    
	- `postOfficeBoxNumber[string]`: El número de casilla de correo para direcciones de casilla de correo. Por ejemplo, 03578  . Modelo: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Modelo: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: La dirección de la calle  . Modelo: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Número que identifica una propiedad específica en una calle pública    
- `alternateName[string]`: Un nombre alternativo para este elemento  - `areaServed[string]`: El área geográfica donde se proporciona un servicio o elemento ofrecido  . Modelo: [https://schema.org/Text](https://schema.org/Text)- `code[string]`: Código que identifica el terminal  - `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizados  - `dateCreated[date-time]`: Marca de tiempo de creación de la entidad. Esto generalmente se asignará a la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Esto generalmente se asignará a la plataforma de almacenamiento  - `description[string]`: Una descripción de este elemento  - `id[*]`: Identificador único de la entidad  - `location[*]`: Referencia Geojson al elemento. Puede ser Punto, LineString, Polígono, MultiPunto, MultiLineString o MultiPolígono  - `mrn[string]`: Identificador codificado MRN. Debe estar relacionado con la entidad de una manera que sea bien conocida por diferentes organismos el significado y el iniciador de la entidad, y todas las partes siguientes mantendrán su valor original. Este identificador debe ser un identificador ÚNICO de la entidad PortCall asignado por el sistema que creó la entidad por primera vez. Este URN debe cumplir con MRN e IETF específicamente RFC 2141, RFC 5234 y RFC 8141. El formato propuesto es id::='urn:mrn:eshuv:<ONSS>:portcalls:terminal:code:[A-Z0-9]+' o  . donde OID:= Organización UN/LOCODE, OONSS:=Nombre de la Organización del Servicio, 2099 el año en el que se inició la llamada al puerto, 9999999 un identificador único creciente que el emisor de la entidad Terminal identificará en sus sistemas (por ejemplo, un id de fila SQL), . por ejemplo, urn:mrn:eshuv:portcalls:terminal:id:4 . Consulte [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)En los estándares internacionales también se conoce como [Visita del barco]  - `name[string]`: El nombre de este elemento  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificados en JSON que hacen referencia a los identificadores únicos de los propietarios(s)  - `portCode[string]`: Código del puerto donde se encuentra este terminal  - `remarks[string]`: Comentarios adicionales o notas sobre el terminal  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el elemento  - `source[string]`: Una secuencia de caracteres que da la fuente original de los datos de la entidad como una URL. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto de la fuente  - `tafTsiLocationCode[string]`: Código de ubicación TAF-TSI para la identificación secundaria del terminal  - `terminal[string]`: Nombre del terminal  - `type[string]`: Tipo de entidad NGSI. Debe ser Terminal  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `code`  - `id`  - `portCode`  - `terminal`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Descripción del modelo de datos de las propiedades  
Ordenadas alfabéticamente (haga clic para obtener detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>detalles completos de yaml</strong></summary>    
```yaml  
Terminal:    
  description: This data model describes a terminal in a port as a join of facilities and ground, which can be used for various maritime operations.    
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
    code:    
      description: Code identifying the terminal    
      type: string    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
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
    description:    
      description: A description of this item    
      type: string    
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
    location:    
      description: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              description: BBox of the  Point    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Point    
              items:    
                type: number    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the LineString    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
          properties:    
            bbox:    
              description: BBox coordinates of the Polygon    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Polygon    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MulitPoint    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MultiLineString    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              description: Coordinates of the MultiPolygon    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    mrn:    
      description: MRN coded identifier. It has to be related to the entity in a way that is well-known by different organisms the meaning and the initiator of the entity, and all next parties will maintain on its original value. This identifier must be an UNIQUE identifier of the PortCall entity assigned by the system who created on first the entity. This URN should Conforms MRN & IETF specifically RFC 2141, RFC 5234, and RFC 8141. The proposed format is id::='urn:mrn:eshuv:<ONSS>:portcalls:terminal:code:[A-Z0-9]+' or  . where OID:= Organisation UN/LOCODE, OONSS:=Organization Name of Service, 2099 the year on which the portcall was initiated, 9999999 an increasing, unique identifier that the issuer of the Terminal entity will identify on his systems (i.e. a SQL row-id), . i.e. urn:mrn:eshuv:portcalls:terminal:id:4 . See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)In international standards is also known as [Ship's Visit]    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item    
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
    portCode:    
      description: Code of the port where this terminal is located    
      type: string    
      x-ngsi:    
        type: Property    
    remarks:    
      description: Additional remarks or notes about the terminal    
      type: string    
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
    source:    
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    tafTsiLocationCode:    
      description: TAF-TSI location code for secondary identification of the terminal    
      type: string    
      x-ngsi:    
        type: Property    
    terminal:    
      description: Name of the terminal    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be Terminal    
      enum:    
        - Terminal    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - portCode    
    - terminal    
    - code    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/Terminal/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/Terminal/schema.json    
  x-model-tags: ESHUV    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplos de cargas    
#### Ejemplo de Terminal NGSI-v2 clave-valor    
Aquí hay un ejemplo de un Terminal en formato JSON como clave-valor. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>mostrar/ocultar ejemplo</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:facilities:terminal:id:20",  
  "type": "Terminal",  
  "mrn": "urn:mrn:eshuv:facilities:terminal:id:20",  
  "portCode": "ESVLC",  
  "terminal": "Levante Pesquero",  
  "code": "LEV",  
  "remarks": "Fishing terminal",  
  "tafTsiLocationCode": "XXXxxxx TAF-TSI label localizacion secundaria de la terminal"  
}  
```  
</details>  
#### Ejemplo de Terminal NGSI-v2 normalizado    
Aquí hay un ejemplo de un Terminal en formato JSON como normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>mostrar/ocultar ejemplo</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:facilities:terminal:id:20",  
  "type": "Terminal",  
  "mrn": {  
    "type": "Text",  
    "value": "urn:mrn:eshuv:facilities:terminal:id:20"  
  },  
  "portCode": {  
    "type": "Text",  
    "value": "ESVLC"  
  },  
  "terminal": {  
    "type": "Text",  
    "value": "Levante Pesquero"  
  },  
  "code": {  
    "type": "Text",  
    "value": "LEV"  
  },  
  "remarks": {  
    "type": "Text",  
    "value": "Fishing terminal"  
  },  
  "tafTsiLocationCode": {  
    "type": "Text",  
    "value": "XXXxxxx TAF-TSI label localizacion secundaria de la terminal"  
  }  
}  
```  
</details>  
#### Ejemplo de Terminal NGSI-LD clave-valor    
Aquí hay un ejemplo de un Terminal en formato JSON-LD como clave-valor. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>mostrar/ocultar ejemplo</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Terminal:urn:mrn:eshuv:facilities:terminal:id:20",  
  "type": "Terminal",  
  "mrn": "urn:mrn:eshuv:facilities:terminal:id:20",  
  "portCode": "ESVLC",  
  "terminal": "Levante Pesquero",  
  "code": "LEV",  
  "remarks": "Fishing terminal",  
  "tafTsiLocationCode": "XXXxxxx TAF-TSI label localizacion secundaria de la terminal",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Ejemplo de Terminal NGSI-LD normalizado    
Aquí hay un ejemplo de un Terminal en formato JSON-LD como normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>mostrar/ocultar ejemplo</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Terminal:urn:mrn:eshuv:facilities:terminal:id:20",  
  "type": "Terminal",  
  "mrn": {  
    "type": "Property",  
    "value": "urn:mrn:eshuv:facilities:terminal:id:20"  
  },  
  "portCode": {  
    "type": "Property",  
    "value": "ESVLC"  
  },  
  "terminal": {  
    "type": "Property",  
    "value": "Levante Pesquero"  
  },  
  "code": {  
    "type": "Property",  
    "value": "LEV"  
  },  
  "remarks": {  
    "type": "Property",  
    "value": "Fishing terminal"  
  },  
  "tafTsiLocationCode": {  
    "type": "Property",  
    "value": "XXXxxxx TAF-TSI label localizacion secundaria de la terminal"  
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar con unidades de magnitud  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
