<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: Operación  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/Operation/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Este modelo de datos está destinado a proporcionar información sobre las operaciones comerciales realizadas en una parada de un buque durante una Escala (entidad Atraque). Una Operación se define como las actividades relacionadas con las operaciones comerciales que tienen lugar durante el atraque. Cada Operación tiene una entidad y algunas operaciones pueden realizarse en el mismo atraque (atracado o fondeado), y se distinguen por su número de secuencia en el tiempo (operationRank)**.  
versión: 0.0.1  
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
- `alternateName[string]`: Un nombre alternativo para este artículo  - `amount[number]`: Número de unidades de carga/descarga  . Model: [https://schema.org/Number](https://schema.org/Number)- `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `berthRef[uri]`: Referencia a la entidad matriz MarineTransport:Berth  - `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `etc[date-time]`: Representado por un formato ISO 8601 UTC, Fecha y hora de la Hora Estimada de Llegada al Atraque prevista por la Autoridad Portuaria (formato ISO 8601 UTC). Si se trata del primer atraque, la ETA-berth debe ser la misma que la ETA-PBP.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `ets[date-time]`:   . Model: [https://schema.org/DateTime.Represented by an ISO 8601 UTC format, Date and time of Estimated Time of starting the operation.](https://schema.org/DateTime.Represented by an ISO 8601 UTC format, Date and time of Estimated Time of starting the operation.)- `id[*]`: Identificador único de la entidad  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `manipulationMeansCode[string]`: Código que identifica los medios de manipulación. Enum: 1=Medios propios del buque, 2=Rampa de rodadura, 3=Grúas de muelle, 4=Grúas automotrices, 5=Tubos, 6=Cintas transportadoras, 7=Instalaciones de bombeo neumático, 8=Instalaciones especiales, 9=Otros medios".  . Model: [https://schema.org/Text](https://schema.org/Text)- `manipulationMeansNumber[number]`: Número de medios de manipulación  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxWeightPerUnit[number]`: Peso máximo por unidad de carga/descarga  . Model: [https://schema.org/Number](https://schema.org/Number)- `measureUnit[string]`: Tipo de unidad de carga/descarga  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: El nombre de este artículo  - `operationRank[number]`: Rango o Número de esta Operación en todas las operaciones comerciales realizadas en atraque en la secuencia de operaciones (descarga, carga, ...)  . Model: [https://schema.org/Number](https://schema.org/Number)- `operationTypeCode[string]`: Código que identifica el tipo de operación comercial. Enum: 'ZD=Desembarque; ZE=Embarque; ZT=Transbordo; ZR=Residuos; AV=Victuaje; DT=Desembarque en tránsito; RE=Restow'.  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `portCallNumber[string]`: Identificador PortCall en formato urn. MarineTransport:PortCall:portCallNumber  . Model: [https://schema.org/Text](https://schema.org/Text)- `portCallRef[uri]`: Referencia a la entidad matriz MarineTransport:PortCall  - `portCode[string]`: Código del puerto de escala  . Model: [https://schema.org/Text](https://schema.org/Text)- `position[string]`: Texto que especifica la posición en el puerto donde se ha producido la operación  . Model: [https://schema.org/Text](https://schema.org/Text)- `productCode[string]`: Código que identifica el tipo de producto de esta operación. Enum: Z01=Petróleo crudo; Z02=Fuelóleo; Z03=Gasóleo; Z04=Gasolina; Z05=Asfalto; Z06=Otros productos petrolíferos; Z07=Gases energéticos del petróleo; Z08=Mineral de hierro; Z09=Piritas; Z10=Otros minerales; Z11=Chatarra de hierro; Z12=Carbones y coque de petróleo; Z13=Productos siderúrgicos; Z14=Fosfatos; Z15=Potasses; Z16=Abonizantes naturales y artificiales; Z17=Productos químicos; Z18=Cemento y clinker; Z19=Madera y corcho; Z20=Materiales de construcción; Z21=Cereales y sus harinas; Z22=Frijoles y harina de soja; Z23=Frutas, hortalizas y legumbres; Z24=Vinos, bebidas alcohólicas y derivados; Z25=Sal común; Z26=Papel y pasta de papel; Z27=Conservas; Z28=Tabaco, cacao, café y especias; Z29=Aceites y grasas; Z30=Otros productos alimenticios; Z31=Maquinaria, aparatos, herramientas y piezas de recambio; Z32=Automóviles y piezas de recambio; Z33=Pescado congelado; Z34= Resto de mercancías; Z35=Gas natural; Z36=Otros productos metalúrgicos; Z37=Piensos y forrajes; Z38=Tara de camión plataforma de carga; Z39=Tara de contenedor; Z40=Mercancías en contenedores en tránsito; Z41=Contenedores llenos; Z42=Contenedores vacíos; Z43=Vehículos; Z44=Partes de vehículos; Z91=Pasajeros; Z92=Pasajeros de cruceros; 1=Pescado fresco; Z51=Biocombustibles; Z52=Otros minerales no metálicos; ZR1= Lastre sucio; ZR2=Lodos y tanques de decantación; ZR3=Tanques de aguas oleosas sucias; ZR4=Aguas sucias; ZR5=Basura;  . Model: [https://schema.org/Text](https://schema.org/Text)- `remarks[string]`: Observaciones sobre la operación  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `stevedoreRef[string]`: Id del estibador. Formato urn:mrn:<oid>:portcalls:operation:stevedore:9999  . Model: [https://schema.org/Text](https://schema.org/Text)- `stopRank[number]`: Rango o Número de esta parada en la parada (atracadero o zona de fondeo) ordenada por secuencia temporal  . Model: [https://schema.org/Number](https://schema.org/Number)- `terminal[string]`: Terminal donde tiene lugar la operación  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Tipo de entidad NGSI. Tiene que ser Operación. En algunas normas internacionales también se conoce como [Parada del buque].  - `year[number]`: Año de init del atraque  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Descripción de las propiedades del modelo de datos  
Ordenados alfabéticamente (pulse para más detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Operation:    
  description: 'This data model is intended to provide information about commercial operations made in a stop of a ship during a PortCall (Berth entity). An Operation is defined as the activities related to commercial operations that take in place during the berth. Each Operation has an entity and some operations can be made in the same berth (docked or anchorage), and are distinguished by its sequence number on time (operationRank)'    
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
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    amount:    
      description: Number of units loading/discharge    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    berthRef:    
      description: 'Reference to parent MarineTransport:Berth entity'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
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
    etc:    
      description: 'Represented by an ISO 8601 UTC format, Date and time of Estimated Time of Arrival to Berth expected by Port Authority  (ISO 8601 UTC format). If this is the first berthing, the ETA-berth should be the same than ETA-PBP'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    ets:    
      description: ""    
      format: date-time    
      type: string    
      x-ngsi:    
        model: 'https://schema.org/DateTime.Represented by an ISO 8601 UTC format, Date and time of Estimated Time of starting the operation.'    
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
    manipulationMeansCode:    
      description: 'Code identifying the manipulation means. Enum: 1=Vessel''s own resources, 2=Roll-on-roll-off ramp, 3=Dock cranes, 4=Automotive cranes, 5=Pipes, 6=Conveyor belts, 7=Pneumatic pumping installations, 8=Special installations, 9=Other means'''    
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
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    manipulationMeansNumber:    
      description: Number of manipulation means    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maxWeightPerUnit:    
      description: Maximum Weight per unit loading/discharge    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Tm    
    measureUnit:    
      description: Unit type of load loading/discharge    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    operationRank:    
      description: 'Rank or Number of this Operation in all the commercial operations made in berth in the sequence of operations (discharge, charge, ...)'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    operationTypeCode:    
      description: 'Code identifying the type of commercial operation. Enum: ''ZD=Disembarkation; ZE=Embarkation; ZT=Transshipment; ZR=Waste; AV=Victualling; DT=Disembarkation in transit; RE=Restow'''    
      enum:    
        - AV    
        - DT    
        - RE    
        - ZD    
        - ZE    
        - ZR    
        - ZT    
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
      description: 'PortCall identifier in urn format. MarineTransport:PortCall:portCallNumber'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    portCallRef:    
      description: 'Reference to parent MarineTransport:PortCall entity'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    portCode:    
      description: Code of the port of the call    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    position:    
      description: Text specifying the position in the port where the operations has place    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    productCode:    
      description: 'Code identifying the type of product of this operation. Enum: Z01=Crude oil; Z02=Fuel oil; Z03=Gas-oil; Z04=Gasoline; Z05=Asphalt; Z06=Other petroleum products; Z07=Petroleum energy gases; Z08=Iron ore; Z09=Pyrites; Z10=Other minerals; Z11=Iron scrap; Z12=Coals and petroleum coke; Z13=Steel products; Z14=Phosphates; Z15=Potasses; Z16=Natural and artificial fertilizers; Z17=Chemical products; Z18=Cement and clinker; Z19=Wood and cork; Z20=Construction materials; Z21=Cereals and their flour; Z22=Beans and soy flour; Z23=Fruits, vegetables and legumes; Z24=Wines, alcoholic beverages and derivatives; Z25=Common salt; Z26=Paper and pulp; Z27=Canned; Z28=Tobacco, cocoa, coffee and spices; Z29=Oils and fats; Z30=Other food products; Z31=Machinery, appliances, tools and spare parts; Z32=Automobiles and parts; Z33=Frozen fish; Z34=Rest of merchandise; Z35=Natural gas; Z36=Other metallurgical products; Z37=Feed and forage; Z38=Tare truck cargo platform; Z39=Container tare; Z40=Merchandise in transit containers; Z41=Containers full; Z42=Empty containers; Z43=Vehicles; Z44=Vehicle parts; Z91=Passengers; Z92=Cruise passengers; 1=Fresh fish; Z51=Biofuels; Z52=Other non-metallic minerals; ZR1=Dirty ballast; ZR2=Sludge and settling tanks; ZR3=Bilge oily water tanks; ZR4=Dirty waters; ZR5=Garbage;'    
      enum:    
        - Z01    
        - Z02    
        - Z03    
        - Z04    
        - Z05    
        - Z06    
        - Z07    
        - Z08    
        - Z09    
        - Z10    
        - Z11    
        - Z12    
        - Z13    
        - Z14    
        - Z15    
        - Z16    
        - Z17    
        - Z18    
        - Z19    
        - Z20    
        - Z21    
        - Z22    
        - Z23    
        - Z24    
        - Z25    
        - Z26    
        - Z27    
        - Z28    
        - Z29    
        - Z30    
        - Z31    
        - Z32    
        - Z33    
        - Z34    
        - Z35    
        - Z36    
        - Z37    
        - Z38    
        - Z39    
        - Z40    
        - Z41    
        - Z42    
        - Z43    
        - Z44    
        - Z91    
        - Z92    
        - Z51    
        - Z52    
        - ZR1    
        - ZR2    
        - ZR3    
        - ZR4    
        - ZR5    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    remarks:    
      description: Remarks of the operation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    stevedoreRef:    
      description: 'Id of the stevedore. Format urn:mrn:<oid>:portcalls:operation:stevedore:9999'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    stopRank:    
      description: Rank or Number of this stop in the stop (berth or anchor area) ordered by time sequence    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    terminal:    
      description: Terminal where the operation takes place    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be Operation. In some international standards is also known as [Ship''s Stop]'    
      enum:    
        - Operation    
      type: string    
      x-ngsi:    
        type: Property    
    year:    
      description: Year of the init of the berthing    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2024 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/Operation/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/Berth/schema.json    
  x-model-tags: ESHUV    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### Funcionamiento NGSI-v2 key-values Ejemplo  
He aquí un ejemplo de una Operación en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:activity:id:40923",  
  "type": "Operation",  
  "portCode": "ESHUV",  
  "year": 2023,  
  "portCallNumber": "ESHUV202300123",  
  "portCallRef": "urn:mrn:eshuv:portcalls:activity:id:941",  
  "berthRef": "urn:mrn:eshuv:portcalls:berth:id:1234",  
  "stopRank": 2,  
  "operationRank": 1,  
  "ets": "2023-01-01T07:30:00",  
  "etc": "2023-01-01T07:30:00",  
  "operationTypeCode": "ZE",  
  "productCode": "Z41",  
  "amount": 120,  
  "measureUnit": "TEU",  
  "maxWeightPerUnit": 23.3,  
  "terminal": "Muelle Sur",  
  "position": "Segunda linea granel",  
  "remarks": "Delayed 1h",  
  "manipulationMeansCode": "3",  
  "manipulationMeansNumber": 2,  
  "stevedoreRef": "1234"  
}  
```  
</details>  
#### Funcionamiento NGSI-v2 normalizado Ejemplo  
He aquí un ejemplo de una Operación en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:activity:id:40923",  
  "type": "Operation",  
  "portCode": {  
    "type": "Text",  
    "value": "ESHUV"  
  },  
  "year": {  
    "type": "Number",  
    "value": 2023  
  },  
  "portCallNumber": {  
    "type": "Text",  
    "value": "ESHUV202300123"  
  },  
  "portCallRef": {  
    "type": "Text",  
    "value": "urn:mrn:eshuv:portcalls:activity:id:941"  
  },  
  "berthRef": {  
    "type": "Text",  
    "value": "urn:mrn:eshuv:portcalls:berth:id:1234"  
  },  
  "stopRank": {  
    "type": "Number",  
    "value": 2  
  },  
  "operationRank": {  
    "type": "Number",  
    "value": 1  
  },  
  "ets": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:30:00"  
  },  
  "etc": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:30:00"  
  },  
  "operationTypeCode": {  
    "type": "Text",  
    "value": "ZE"  
  },  
  "productCode": {  
    "type": "Text",  
    "value": "Z41"  
  },  
  "amount": {  
    "type": "Number",  
    "value": 120  
  },  
  "measureUnit": {  
    "type": "Text",  
    "value": "TEU"  
  },  
  "maxWeightPerUnit": {  
    "type": "Number",  
    "value": 23.3  
  },  
  "terminal": {  
    "type": "Text",  
    "value": "Muelle Sur"  
  },  
  "position": {  
    "type": "Text",  
    "value": "Segunda linea granel"  
  },  
  "remarks": {  
    "type": "Text",  
    "value": "Delayed 1h"  
  },  
  "manipulationMeansCode": {  
    "type": "Text",  
    "value": "3"  
  },  
  "manipulationMeansNumber": {  
    "type": "Number",  
    "value": 2  
  },  
  "stevedoreRef": {  
    "type": "Text",  
    "value": "1234"  
  }  
}  
```  
</details>  
#### Operación NGSI-LD key-values Ejemplo  
He aquí un ejemplo de una Operación en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:activity:id:40923",  
  "type": "Operation",  
  "portCode": "ESHUV",  
  "year": 2023,  
  "portCallNumber": "ESHUV202300123",  
  "portCallRef": "urn:mrn:eshuv:portcalls:activity:id:941",  
  "berthRef": "urn:mrn:eshuv:portcalls:berth:id:1234",  
  "stopRank": 2,  
  "operationRank": 1,  
  "ets": "2023-01-01T07:30:00",  
  "etc": "2023-01-01T07:30:00",  
  "operationTypeCode": "ZE",  
  "productCode": "Z41",  
  "amount": 120,  
  "measureUnit": "TEU",  
  "maxWeightPerUnit": 23.3,  
  "terminal": "Muelle Sur",  
  "position": "Segunda linea granel",  
  "remarks": "Delayed 1h",  
  "manipulationMeansCode": "3",  
  "manipulationMeansNumber": 2,  
  "stevedoreRef": "1234",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Funcionamiento NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de Operación en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:activity:id:40923",  
  "type": "Operation",  
  "portCode": {  
    "type": "Property",  
    "value": "ESHUV"  
  },  
  "year": {  
    "type": "Property",  
    "value": 2023  
  },  
  "portCallNumber": {  
    "type": "Property",  
    "value": "ESHUV202300123"  
  },  
  "portCallRef": {  
    "type": "Relationship",  
    "object": "urn:mrn:eshuv:portcalls:activity:id:941"  
  },  
  "berthRef": {  
    "type": "Relationship",  
    "object": "urn:mrn:eshuv:portcalls:berth:id:1234"  
  },  
  "stopRank": {  
    "type": "Property",  
    "value": 2  
  },  
  "operationRank": {  
    "type": "Property",  
    "value": 1  
  },  
  "ets": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:30:00"  
    }  
  },  
  "etc": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:30:00"  
    }  
  },  
  "operationTypeCode": {  
    "type": "Property",  
    "value": "ZE"  
  },  
  "productCode": {  
    "type": "Property",  
    "value": "Z41"  
  },  
  "amount": {  
    "type": "Property",  
    "value": 120  
  },  
  "measureUnit": {  
    "type": "Property",  
    "value": "TEU"  
  },  
  "maxWeightPerUnit": {  
    "type": "Property",  
    "value": 23.3  
  },  
  "terminal": {  
    "type": "Property",  
    "value": "Muelle Sur"  
  },  
  "position": {  
    "type": "Property",  
    "value": "Segunda linea granel"  
  },  
  "remarks": {  
    "type": "Property",  
    "value": "Delayed 1h"  
  },  
  "manipulationMeansCode": {  
    "type": "Property",  
    "value": "3"  
  },  
  "manipulationMeansNumber": {  
    "type": "Property",  
    "value": 2  
  },  
  "stevedoreRef": {  
    "type": "Property",  
    "value": "1234"  
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
