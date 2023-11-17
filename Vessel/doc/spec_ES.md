<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: Buque    
==============<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/Vessel/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **El modelo de datos está destinado a proporcionar información sobre los buques. Permite representar las propiedades de cada buque: información estática y dinámica**.    
versión: 0.0.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Lista de propiedades    
<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.    
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección postal, y que está en la región  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, gestiona el gobierno local      
	- `postOfficeBoxNumber[string]`: El número del apartado de correos para las direcciones de apartados postales. Por ejemplo, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: La dirección  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: Número que identifica una propiedad específica en una vía pública      
- `airDraught[number]`: Calado (distancia desde el punto más alto del buque hasta la línea de flotación)  . Model: [http://schema.org/Number](http://schema.org/Number)- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `beam[number]`: Manga del buque  . Model: [https://schema.org/Number](https://schema.org/Number)- `buildingAt[date-time]`: Fecha y hora de construcción del buque representadas por un formato ISO 8601 UTC  . Model: [https://schema.org/Text](https://schema.org/Text)- `callSign[string]`: Los distintivos de llamada marítima son distintivos de llamada asignados como identificadores únicos a los buques  . Model: [https://schema.org/Text](https://schema.org/Text)- `courseOverGround[number]`: Rumbo sobre el terreno (COG)  . Model: [https://schema.org/Number](https://schema.org/Number)- `createdAt[date-time]`: Fecha y hora de creación de la entidad representada por un formato ISO 8601 UTC  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  . Model: [https://schema.org/Text](https://schema.org/Text)- `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `deadweightTonnage[number]`: Tonelaje de peso muerto (TPM)  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: Descripción de este artículo  - `destinationPort[string]`: Puerto de destino (Sistema de codificación geográfica UN/LOCODE (Código de las Naciones Unidas para las Localizaciones Comerciales y de Transporte). https://unece.org/trade/publications/recommendation-ndeg16-united-nations-code-trade-and-transport-locations)  . Model: [https://schema.org/Text](https://schema.org/Text)- `draught[number]`: Calado (distancia vertical entre la línea de flotación y el fondo del casco (quilla))  . Model: [http://schema.org/Number](http://schema.org/Number)- `estimatedTimeOfArrival[date-time]`: Hora estimada de llegada, tal y como estaba prevista inicialmente e introducida por el expedidor, representada por un formato ISO 8601 UTC.  . Model: [https://schema.org/Text](https://schema.org/Text)- `financialOwner[string]`: Propietario financiero  . Model: [https://schema.org/Text](https://schema.org/Text)- `flagCode[string]`: Código internacional de banderas (ISO 3166-1 alfa-2)  . Model: [https://schema.org/Text](https://schema.org/Text)- `grossTonnage[number]`: Tonelaje bruto (GT)  . Model: [https://schema.org/Number](https://schema.org/Number)- `heading[number]`: Rumbo del buque (HDG)  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[string]`: Identificador único de la entidad  - `imo[number]`: Número de la Organización Marítima Internacional (un UID mundial para siempre)  . Model: [https://schema.org/Number](https://schema.org/Number)- `length[number]`: Eslora del buque  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[object]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygoProperty.  	- `coordinates`:       
	- `type`:       
- `manager[string]`: Gestor de buques  . Model: [https://schema.org/Text](https://schema.org/Text)- `maximumDraught[number]`: Calado máximo  . Model: [https://schema.org/Number](https://schema.org/Number)- `mmsi[number]`: Número de Identidad del Servicio Móvil Marítimo (un UID asignado temporalmente, emitido por el Estado de abanderamiento actual de ese objeto).  . Model: [https://schema.org/Number](https://schema.org/Number)- `modifiedAt[date-time]`: Fecha y hora de la última modificación de la entidad representada por un formato ISO 8601 UTC  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: Nombre del buque  . Model: [https://schema.org/Text](https://schema.org/Text)- `navigationStatus[number]`: Enum: 0=En navegación con motor,1=Fondeado,2=Sin mando,3=Maniobrabilidad restringida,4=Restringido por su calado,5=Amarrado,6=En tierra,7=Pescando,8=En navegación,9=Reservado para futura modificación del estado de navegación para HSC,10=Reservado para futura modificación del estado de navegación para WIG,11=Reservado para uso futuro,12=Reservado para uso futuro,13=Reservado para uso futuro,14=AIS-SART activo,15=No definido (por defecto)". Estado de navegación. Formato de datos AIVDM/AIVDO  . Model: [http://schema.org/Number](http://schema.org/Number)- `observedAt[date-time]`: Fecha y hora de esta observación representadas por un formato ISO 8601 UTC  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `ownerVessel[string]`: Propietario Buque  . Model: [https://schema.org/Text](https://schema.org/Text)- `photo[string]`: URL de la foto del buque  . Model: [https://schema.org/Text](https://schema.org/Text)- `positionAccuracy[number]`: receptor del sistema mundial de navegación por satélite (GNSS) o de otro dispositivo electrónico de fijación de la posición; por defecto),1=Alta (< 10 m; modo diferencial de, por ejemplo, un receptor DGNSS)". Código de la precisión del indicador de posición del buque  . Model: [https://schema.org/Number.Enum: 0=Low (> 10 m; autonomous mode of e.g](https://schema.org/Number.Enum: 0=Low (> 10 m; autonomous mode of e.g)- `previousPort[string]`: Puerto anterior (Sistema de codificación geográfica UN/LOCODE (Código de las Naciones Unidas para las Localizaciones Comerciales y de Transporte). https://unece.org/trade/publications/recommendation-ndeg16-united-nations-code-trade-and-transport-locations)  . Model: [https://schema.org/Text](https://schema.org/Text)- `rateOfTurn[number]`: Ratio de giro (ROT)  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `specialManeuverIndicator[number]`: Enum: '0=No disponible (por defecto),1=No involucrado en maniobra especial,2=Involucrado en maniobra especial'. Código de la bandera de maniobra especial  . Model: [https://schema.org/Number](https://schema.org/Number)- `speedOverGround[number]`: Velocidad sobre el suelo (SOG)  . Model: [https://schema.org/Number](https://schema.org/Number)- `technicalManager[string]`: Director técnico  . Model: [https://schema.org/Text](https://schema.org/Text)- `toBow[number]`: Dimensión a proa  . Model: [http://schema.org/Number](http://schema.org/Number)- `toPort[number]`: Dimensión a puerto  . Model: [http://schema.org/Number](http://schema.org/Number)- `toStardboard[number]`: Dimensión a estribor  . Model: [http://schema.org/Number](http://schema.org/Number)- `toStern[number]`: Dimensión a popa  . Model: [http://schema.org/Number](http://schema.org/Number)- `type[string]`: Tipo de entidad NGSI. Tiene que ser Vessel  - `vesselSubType[number]`: Enum: '0=No disponible (por defecto),1-19=Reservado para uso futuro,20=Ala en tierra (WIG), todos los buques de este tipo,21=Ala en tierra (WIG), categoría peligrosa A,22=Ala en tierra (WIG), Categoría peligrosa B,23=Ala en tierra (WIG), Categoría peligrosa C,24=Ala en tierra (WIG), Categoría peligrosa D,25-29=Ala en tierra (WIG), Reservado para uso futuro,30=Pesca,31=Remolque,32=Remolque: eslora superior a 200 m o manga superior a 25 m,33=Operaciones de dragado o submarinas,34=Operaciones de buceo,35=Operaciones militares,36=Vela,37=Naves de recreo,38-39=Reservado,40=Naves de gran velocidad (HSC), todos los buques de este tipo,41=Naves de gran velocidad (HSC), categoría peligrosa A,42=Naves de gran velocidad (HSC), categoría peligrosa B,43=Naves de gran velocidad (HSC), categoría peligrosa C,44=Naves de gran velocidad (HSC), Peligrosas categoría D,45-48=Naves de gran velocidad (HSC), Reservado para uso futuro,49=Naves de gran velocidad (HSC), Sin información adicional,50=Buque piloto,51=Buque de búsqueda y salvamento,52=Remolcador,53=Port Tender,54=Equipo anticontaminación,55=Cumplimiento de la ley,56-57=Buque de repuesto - Local,58=Transporte médico,59=Buque no combatiente según la Resolución RR No. 18,60=Pasajeros, todos los buques de este tipo,61=Pasajeros, categoría peligrosa A,62=Pasajeros, categoría peligrosa B,63=Pasajeros, categoría peligrosa C,64=Pasajeros, categoría peligrosa D,65-68=Pasajeros, Reservado para uso futuro,69=Pasajeros, Sin información adicional,70=Carga, todos los buques de este tipo,71=Carga, categoría peligrosa A,72=Carga, categoría peligrosa B,73=Carga, categoría peligrosa C,74=Carga, categoría peligrosa D,75-78=Carga, Reservado para uso futuro,79=Carga, Sin información adicional,80=Tanker, todos los buques de este tipo,81=Cisterna, categoría peligrosa A,82=Cisterna, categoría peligrosa B,83=Cisterna, categoría peligrosa C,84=Cisterna, categoría peligrosa D,85-88=Cisterna, Reservado para uso futuro,89=Cisterna, Sin información adicional,90=Otro tipo, todos los buques de este tipo,91=Otro tipo, categoría peligrosa A,92=Otro tipo, categoría peligrosa B,93=Otro tipo, categoría peligrosa C,94=Otro tipo, categoría peligrosa D,95-98=Otro tipo, Reservado para uso futuro,99=Otro tipo, sin información adicional". Código del subtipo de buque  . Model: [https://schema.org/Number](https://schema.org/Number)- `vesselType[number]`: Enum: '1=Reservado,2=En tierra,3=Categoría especial,4=Embarcación de gran velocidad,5=Categoría especial,6=Pasajeros,7=Carga,8=Tanque,9=Otro'. Código del tipo de buque  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propiedades requeridas    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Descripción de las propiedades del modelo de datos    
Ordenados alfabéticamente (pulse para más detalles)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
Vessel:      
  description: 'The data model is intended to provide information about vessels. It allows to represent the properties of each vessel: static and dynamic information'      
  properties:      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
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
    airDraught:      
      description: Air Draught (distance from the top of a vessel''s highest point to its waterline)      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
        units: ' meters'      
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
    beam:      
      description: Beam of Vessel      
      maximum: 1000      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: ' meters'      
    buildingAt:      
      description: Date and time of building of the vessel represented by an ISO 8601 UTC format      
      format: date-time      
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
        units: ' degree'      
    createdAt:      
      description: Date and time of creation of the entity represented by an ISO 8601 UTC format      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
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
    deadweightTonnage:      
      description: Deadweight Tonnage (DWT)      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: ' tons'      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    destinationPort:      
      description: 'Destination Port (Geographic coding scheme UN/LOCODE (United Nations Code for Trade and Transport Locations). https://unece.org/trade/publications/recommendation-ndeg16-united-nations-code-trade-and-transport-locations)'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    draught:      
      description: Draught (vertical distance between the waterline and the bottom of the hull (keel))      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
        units: ' meters'      
    estimatedTimeOfArrival:      
      description: 'Estimated time of arrival, as it was originally planned and entered by the shipper, represented by an ISO 8601 UTC format'      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    financialOwner:      
      description: Financial Owner      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    flagCode:      
      description: International Flag Code (ISO 3166-1 alfa-2)      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    grossTonnage:      
      description: Gross Tonnage (GT)      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: ' moorson tons'      
    heading:      
      description: Heading of the Vessel (HDG)      
      maximum: 511      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: ' degree'      
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
        type: Property      
    imo:      
      description: International Maritime Organization Number (a global forever UID)      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    length:      
      description: Length of Vessel      
      maximum: 8000      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: ' meters'      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                type: number      
              minItems: 2      
              type: array      
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
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  type: number      
                minItems: 2      
                type: array      
              minItems: 2      
              type: array      
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
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  items:      
                    type: number      
                  minItems: 2      
                  type: array      
                minItems: 4      
                type: array      
              type: array      
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
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  type: number      
                minItems: 2      
                type: array      
              type: array      
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
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  items:      
                    type: number      
                  minItems: 2      
                  type: array      
                minItems: 2      
                type: array      
              type: array      
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
    manager:      
      description: Manager Vessel      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    maximumDraught:      
      description: Maximum Draught      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: ' meters'      
    mmsi:      
      description: 'Marine Mobile Service Identity Number (a temporarily assigned UID, issued by that object''s current flag state)'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    modifiedAt:      
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
      description: 'Enum: ''0=Under way using engine,1=At anchor,2=Not under command,3=Restricted manoeuverability,4=Constrained by her draught,5=Moored,6=Aground,7=Engaged in Fishing,8=Under way sailing,9=Reserved for future amendment of Navigational Status for HSC,10=Reserved for future amendment of Navigational Status for WIG,11=Reserved for future use,12=Reserved for future use,13=Reserved for future use,14=AIS-SART is active,15=Not defined (default)''. Navigation Status. AIVDM/AIVDO data format'      
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
        model: http://schema.org/Number      
        type: Property      
    observedAt:      
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
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    ownerVessel:      
      description: Owner Vessel      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    photo:      
      description: Vessel Photo URL      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    positionAccuracy:      
      description: 'global navigation satellite system (GNSS) receiver or of other electronic position fixing device; default),1=High (< 10 m; differential mode of e.g. DGNSS receiver)''. Code for the accuracy of the vessel position flag'      
      enum:      
        - 0      
        - 1      
      type: number      
      x-ngsi:      
        model: 'https://schema.org/Number.Enum: 0=Low (> 10 m; autonomous mode of e.g'      
        type: Property      
    previousPort:      
      description: 'Previous Port (Geographic coding scheme UN/LOCODE (United Nations Code for Trade and Transport Locations). https://unece.org/trade/publications/recommendation-ndeg16-united-nations-code-trade-and-transport-locations)'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    rateOfTurn:      
      description: Rate of Turn (ROT)      
      maximum: 708      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: ' degree'      
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    specialManeuverIndicator:      
      description: 'Enum: ''0=Not available (default),1=Not engaged in special maneuver,2=Engaged in special maneuver''. Code for the special maneuver flag'      
      enum:      
        - 0      
        - 1      
        - 2      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    speedOverGround:      
      description: Speed Over Ground (SOG)      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: ' meters per second'      
    technicalManager:      
      description: Technical Manager      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    toBow:      
      description: Dimension to Bow      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
        units: ' meters'      
    toPort:      
      description: Dimension to Port      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
        units: ' meters'      
    toStardboard:      
      description: Dimension to Starboard      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
        units: ' meters'      
    toStern:      
      description: Dimension to Stern      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
        units: ' meters'      
    type:      
      description: NGSI Entity type. It has to be Vessel      
      enum:      
        - Vessel      
      type: string      
      x-ngsi:      
        type: Property      
    vesselSubType:      
      description: 'Enum: ''0=Not available (default),1-19=Reserved for future use,20=Wing in ground (WIG), all ships of this type,21=Wing in ground (WIG), Hazardous category A,22=Wing in ground (WIG), Hazardous category B,23=Wing in ground (WIG), Hazardous category C,24=Wing in ground (WIG), Hazardous category D,25-29=Wing in ground (WIG), Reserved for future use,30=Fishing,31=Towing,32=Towing: length exceeds 200m or breadth exceeds 25m,33=Dredging or underwater ops,34=Diving ops,35=Military ops,36=Sailing,37=Pleasure Craft,38-39=Reserved,40=High speed craft (HSC), all ships of this type,41=High speed craft (HSC), Hazardous category A,42=High speed craft (HSC), Hazardous category B,43=High speed craft (HSC), Hazardous category C,44=High speed craft (HSC), Hazardous category D,45-48=High speed craft (HSC), Reserved for future use,49=High speed craft (HSC), No additional information,50=Pilot Vessel,51=Search and Rescue vessel,52=Tug,53=Port Tender,54=Anti-pollution equipment,55=Law Enforcement,56-57=Spare - Local Vessel,58=Medical Transport,59=Noncombatant ship according to RR Resolution No. 18,60=Passenger, all ships of this type,61=Passenger, Hazardous category A,62=Passenger, Hazardous category B,63=Passenger, Hazardous category C,64=Passenger, Hazardous category D,65-68=Passenger, Reserved for future use,69=Passenger, No additional information,70=Cargo, all ships of this type,71=Cargo, Hazardous category A,72=Cargo, Hazardous category B,73=Cargo, Hazardous category C,74=Cargo, Hazardous category D,75-78=Cargo, Reserved for future use,79=Cargo, No additional information,80=Tanker, all ships of this type,81=Tanker, Hazardous category A,82=Tanker, Hazardous category B,83=Tanker, Hazardous category C,84=Tanker, Hazardous category D,85-88=Tanker, Reserved for future use,89=Tanker, No additional information,90=Other Type, all ships of this type,91=Other Type, Hazardous category A,92=Other Type, Hazardous category B,93=Other Type, Hazardous category C,94=Other Type, Hazardous category D,95-98=Other Type, Reserved for future use,99=Other Type, no additional information''. Code for vessel Sub-Type'      
      enum:      
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
        - 16      
        - 17      
        - 18      
        - 19      
        - 20      
        - 21      
        - 22      
        - 23      
        - 24      
        - 25      
        - 26      
        - 27      
        - 28      
        - 29      
        - 30      
        - 31      
        - 32      
        - 33      
        - 34      
        - 35      
        - 36      
        - 37      
        - 38      
        - 39      
        - 40      
        - 41      
        - 42      
        - 43      
        - 44      
        - 45      
        - 46      
        - 47      
        - 48      
        - 49      
        - 50      
        - 51      
        - 52      
        - 53      
        - 54      
        - 55      
        - 56      
        - 57      
        - 58      
        - 59      
        - 60      
        - 61      
        - 62      
        - 63      
        - 64      
        - 65      
        - 66      
        - 67      
        - 68      
        - 69      
        - 70      
        - 71      
        - 72      
        - 73      
        - 74      
        - 75      
        - 76      
        - 77      
        - 78      
        - 79      
        - 80      
        - 81      
        - 82      
        - 83      
        - 84      
        - 85      
        - 86      
        - 87      
        - 88      
        - 89      
        - 90      
        - 91      
        - 92      
        - 93      
        - 94      
        - 95      
        - 96      
        - 97      
        - 98      
        - 99      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    vesselType:      
      description: 'Enum: ''1=Reserved,2=Wing In Ground,3=Special Category,4=High-Speed Craft,5=Special Category,6=Passenger,7=Cargo,8=Tanker,9=Other''. Code for vessel type'      
      enum:      
        - 1      
        - 2      
        - 3      
        - 4      
        - 5      
        - 6      
        - 7      
        - 8      
        - 9      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/Vessel/LICENSE.md      
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/Vessel/schema.json      
  x-model-tags: I4Trust      
  x-version: 0.1.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Ejemplo de carga útil    
#### Vessel NGSI-v2 key-values Ejemplo    
Aquí hay un ejemplo de un Vessel en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:mrn:amura:vessel:test",  
  "type": "Vessel",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -5.993307,  
      37.362882  
    ]  
  },  
  "imo": 9863637,  
  "mmsi": 210049000,  
  "callSign": "5BPC5",  
  "name": "ELEANOR ROOSEVELT",  
  "speedOverGround": 1,  
  "courseOverGround": 1,  
  "heading": 1,  
  "rateOfTurn": 1,  
  "createdAt": "2022-06-01T07:00:00.00Z",  
  "modifiedAt": "2022-06-01T07:00:00.00Z",  
  "observedAt": "2022-06-01T07:00:00.00Z",  
  "flagCode": "CY",  
  "vesselType": 1,  
  "vesselSubType": 2,  
  "grossTonnage": 12467,  
  "beam": 7,  
  "length": 32,  
  "maximumDraught": 5,  
  "deadweightTonnage": 8,  
  "buildingAt": "2021-01-01T07:00:00.00Z",  
  "toBow": 3,  
  "toStern": 20,  
  "toPort": 17,  
  "toStardboard": 4,  
  "navigationStatus": 4,  
  "airDraught": 4,  
  "draught": 4,  
  "photo": "PHOTO URL",  
  "ownerVessel": "OWNER NAME",  
  "manager": "MANAGER NAME",  
  "financialOwner": "FINANCIAL OWNER NAME",  
  "technicalManager": "TECHNICAL MANAGER NAME",  
  "dataProvider": "AIS",  
  "destinationPort": "ESVLC",  
  "previousPort": "ESPMI",  
  "estimatedTimeOfArrival": "2023-03-01T07:00:00.00Z",  
  "calculatedTimeOfArrival": "2023-03-02T07:00:00.00Z",  
  "positionAccuracy": 0,  
  "specialManeuverIndicator": 1  
}  
```  
</details>    
#### Recipiente NGSI-v2 normalizado Ejemplo    
He aquí un ejemplo de un Vessel en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:mrn:amura:vessel:test",  
  "type": "Vessel",  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -5.993307,  
        37.362882  
      ]  
    }  
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
    "value": "5BPC5"  
  },  
  "name": {  
    "type": "Text",  
    "value": "ELEANOR ROOSEVELT"  
  },  
  "speedOverGround": {  
    "type": "Boolean",  
    "value": true  
  },  
  "courseOverGround": {  
    "type": "Boolean",  
    "value": true  
  },  
  "heading": {  
    "type": "Boolean",  
    "value": true  
  },  
  "rateOfTurn": {  
    "type": "Boolean",  
    "value": true  
  },  
  "createdAt": {  
    "type": "DateTime",  
    "value": "2022-06-01T07:00:00.00Z"  
  },  
  "modifiedAt": {  
    "type": "DateTime",  
    "value": "2022-06-01T07:00:00.00Z"  
  },  
  "observedAt": {  
    "type": "DateTime",  
    "value": "2022-06-01T07:00:00.00Z"  
  },  
  "flagCode": {  
    "type": "Text",  
    "value": "CY"  
  },  
  "vesselType": {  
    "type": "Boolean",  
    "value": true  
  },  
  "vesselSubType": {  
    "type": "Number",  
    "value": 2  
  },  
  "grossTonnage": {  
    "type": "Number",  
    "value": 12467  
  },  
  "beam": {  
    "type": "Number",  
    "value": 7  
  },  
  "length": {  
    "type": "Number",  
    "value": 32  
  },  
  "maximumDraught": {  
    "type": "Number",  
    "value": 5  
  },  
  "deadweightTonnage": {  
    "type": "Number",  
    "value": 8  
  },  
  "buildingAt": {  
    "type": "DateTime",  
    "value": "2021-01-01T07:00:00.00Z1"  
  },  
  "toBow": {  
    "type": "Number",  
    "value": 3  
  },  
  "toStern": {  
    "type": "Number",  
    "value": 20  
  },  
  "toPort": {  
    "type": "Number",  
    "value": 17  
  },  
  "toStardboard": {  
    "type": "Number",  
    "value": 4  
  },  
  "navigationStatus": {  
    "type": "Number",  
    "value": 4  
  },  
  "airDraught": {  
    "type": "Number",  
    "value": 4  
  },  
  "draught": {  
    "type": "Number",  
    "value": 4  
  },  
  "photo": {  
    "type": "Text",  
    "value": "URL PHOTO"  
  },  
  "ownerVessel": {  
    "type": "Text",  
    "value": "OWNER NAME"  
  },  
  "manager": {  
    "type": "Text",  
    "value": "MANAGER NAME"  
  },  
  "financialOwner": {  
    "type": "Text",  
    "value": "FINANCIAL OWNER NAME"  
  },  
  "technicalManager": {  
    "type": "Text",  
    "value": "TECHNICAL MANAGER NAME"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "AIS"  
  },  
  "destinationPort": {  
    "type": "Text",  
    "value": "ESVLC"  
  },  
  "previousPort": {  
    "type": "Text",  
    "value": "ESPMI"  
  },  
  "estimatedTimeOfArrival": {  
    "type": "DateTime",  
    "value": "2023-03-01T07:00:00.00Z"  
  },  
  "positionAccuracy": {  
    "type": "Boolean",  
    "value": false  
  },  
  "specialManeuverIndicator": {  
    "type": "Boolean",  
    "value": true  
  }  
}  
```  
</details>    
#### Vessel NGSI-LD key-values Ejemplo    
Aquí hay un ejemplo de un Vessel en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:mrn:amura:vessel:test",  
  "type": "Vessel",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -5.993307,  
      37.362882  
    ]  
  },  
  "imo": 9863637,  
  "mmsi": 210049000,  
  "callSign": "5BPC5",  
  "name": "ELEANOR ROOSEVELT",  
  "speedOverGround": 1,  
  "courseOverGround": 1,  
  "heading": 1,  
  "rateOfTurn": 1,  
  "createdAt": "2022-06-01T07:00:00.00Z",  
  "modifiedAt": "2022-06-01T07:00:00.00Z",  
  "observedAt": "2022-06-01T07:00:00.00Z",  
  "flagCode": "CY",  
  "vesselType": 1,  
  "vesselSubType": 2,  
  "grossTonnage": 12467,  
  "beam": 7,  
  "length": 32,  
  "maximumDraught": 5,  
  "deadweightTonnage": 8,  
  "buildingAt": "2021-01-01T07:00:00.00Z",  
  "toBow": 3,  
  "toStern": 20,  
  "toPort": 17,  
  "toStardboard": 4,  
  "navigationStatus": 4,  
  "airDraught": 4,  
  "draught": 4,  
  "photo": "PHOTO URL",  
  "ownerVessel": "OWNER NAME",  
  "manager": "MANAGER NAME",  
  "financialOwner": "FINANCIAL OWNER NAME",  
  "technicalManager": "TECHNICAL MANAGER NAME",  
  "dataProvider": "AIS",  
  "destinationPort": "ESVLC",  
  "previousPort": "ESPMI",  
  "estimatedTimeOfArrival": "2023-03-01T07:00:00.00Z",  
  "positionAccuracy": 0,  
  "specialManeuverIndicator": 1,  
  "@context": [  
    "https://gitlab.com/hiades/fiware/smart-data-models/-/raw/main/context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### Recipiente NGSI-LD normalizado Ejemplo    
He aquí un ejemplo de un Vessel en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:mrn:amura:vessel:test",  
    "type": "Vessel",  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -5.993307,  
                37.362882  
            ]  
        }  
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
        "value": "5BPC5"  
    },  
    "name": {  
        "type": "Property",  
        "value": "ELEANOR ROOSEVELT"  
    },  
    "speedOverGround": {  
        "type": "Property",  
        "value": 1  
    },  
    "courseOverGround": {  
        "type": "Property",  
        "value": 1  
    },  
    "heading": {  
        "type": "Property",  
        "value": 1  
    },  
    "rateOfTurn": {  
        "type": "Property",  
        "value": 1  
    },  
    "createdAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2022-06-01T07:00:00.00Z"  
        }  
    },  
    "modifiedAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2022-06-01T07:00:00.00Z"  
        }  
    },  
    "observedAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2022-06-01T07:00:00.00Z"  
        }  
    },  
    "flagCode": {  
        "type": "Property",  
        "value": "CY"  
    },  
    "vesselType": {  
        "type": "Property",  
        "value": 1  
    },  
    "vesselSubType": {  
        "type": "Property",  
        "value": 2  
    },  
    "grossTonnage": {  
        "type": "Property",  
        "value": 12467  
    },  
    "beam": {  
        "type": "Property",  
        "value": 7  
    },  
    "length": {  
        "type": "Property",  
        "value": 32  
    },  
    "maximumDraught": {  
        "type": "Property",  
        "value": 5  
    },  
    "deadweightTonnage": {  
        "type": "Property",  
        "value": 8  
    },  
    "buildingAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-01-01T07:00:00.00Z1"  
        }  
    },  
    "toBow": {  
        "type": "Property",  
        "value": 3  
    },  
    "toStern": {  
        "type": "Property",  
        "value": 20  
    },  
    "toPort": {  
        "type": "Property",  
        "value": 17  
    },  
    "toStardboard": {  
        "type": "Property",  
        "value": 4  
    },  
    "navigationStatus": {  
        "type": "Property",  
        "value": 4  
    },  
    "airDraught": {  
        "type": "Property",  
        "value": 4  
    },  
    "draught": {  
        "type": "Property",  
        "value": 4  
    },  
    "photo": {  
        "type": "Property",  
        "value": "URL PHOTO"  
    },  
    "ownerVessel": {  
        "type": "Property",  
        "value": "OWNER NAME"  
    },  
    "manager": {  
        "type": "Property",  
        "value": "MANAGER NAME"  
    },  
    "financialOwner": {  
        "type": "Property",  
        "value": "FINANCIAL OWNER NAME"  
    },  
    "technicalManager": {  
        "type": "Property",  
        "value": "TECHNICAL MANAGER NAME"  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "AIS"  
    },  
    "destinationPort": {  
        "type": "Property",  
        "value": "ESVLC"  
    },  
    "previousPort": {  
        "type": "Property",  
        "value": "ESPMI"  
    },  
    "estimatedTimeOfArrival": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2023-03-01T07:00:00.00Z"  
        }  
    },  
    "positionAccuracy": {  
        "type": "Property",  
        "value": 0  
    },  
    "specialManeuverIndicator": {  
        "type": "Property",  
        "value": 1  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
