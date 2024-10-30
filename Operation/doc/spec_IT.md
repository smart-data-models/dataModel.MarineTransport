<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: Operazione  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/Operation/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Questo modello di dati è destinato a fornire informazioni sulle operazioni commerciali effettuate in una sosta di una nave durante un PortCall (entità Berth). Un'operazione è definita come le attività relative alle operazioni commerciali che si svolgono durante l'ormeggio. Ogni operazione ha un'entità e alcune operazioni possono essere effettuate nello stesso ormeggio (ormeggio o ancoraggio) e si distinguono per il numero di sequenza nel tempo (operationRank)**.  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale.    
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numero che identifica una proprietà specifica su una strada pubblica    
- `alternateName[string]`: Un nome alternativo per questa voce  - `amount[number]`: Numero di unità di carico/scarico  . Model: [https://schema.org/Number](https://schema.org/Number)- `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `berthRef[uri]`: Riferimento all'entità parentale MarineTransport:Berth  - `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `etc[date-time]`: Rappresentato da un formato ISO 8601 UTC, data e ora dell'orario stimato di arrivo all'ormeggio previsto dall'Autorità portuale (formato ISO 8601 UTC). Se si tratta del primo attracco, l'ETA-berth deve essere uguale all'ETA-PBP.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `ets[date-time]`:   . Model: [https://schema.org/DateTime.Represented by an ISO 8601 UTC format, Date and time of Estimated Time of starting the operation.](https://schema.org/DateTime.Represented by an ISO 8601 UTC format, Date and time of Estimated Time of starting the operation.)- `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `manipulationMeansCode[string]`: Codice che identifica il mezzo di manipolazione. Enum: 1=Risorse proprie della nave, 2=Rimorchio su rampa, 3=Gru da banchina, 4=Gru automobilistiche, 5=Tubi, 6=Nastri trasportatori, 7=Impianti di pompaggio pneumatico, 8=Impianti speciali, 9=Altri mezzi".  . Model: [https://schema.org/Text](https://schema.org/Text)- `manipulationMeansNumber[number]`: Numero di mezzi di manipolazione  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxWeightPerUnit[number]`: Peso massimo per unità di carico/scarico  . Model: [https://schema.org/Number](https://schema.org/Number)- `measureUnit[string]`: Tipo di unità di carico/scarico  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: Il nome di questo elemento  - `operationRank[number]`: Classifica o numero di questa operazione in tutte le operazioni commerciali effettuate all'ormeggio nella sequenza di operazioni (scarico, carica, ...)  . Model: [https://schema.org/Number](https://schema.org/Number)- `operationTypeCode[string]`: Codice che identifica il tipo di operazione commerciale. Enum: "ZD=Sbarco; ZE=Imbarco; ZT=Trasbordo; ZR=Rifiuti; AV=Vicinanza; DT=Sbarco in transito; RE=Rimessa a dimora".  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `portCallNumber[string]`: Identificatore PortCall in formato urn. MarineTransport:PortCall:portCallNumber  . Model: [https://schema.org/Text](https://schema.org/Text)- `portCallRef[uri]`: Riferimento all'entità padre MarineTransport:PortCall  - `portCode[string]`: Codice del porto di scalo  . Model: [https://schema.org/Text](https://schema.org/Text)- `position[string]`: Testo che specifica la posizione nel porto in cui è avvenuta l'operazione  . Model: [https://schema.org/Text](https://schema.org/Text)- `productCode[string]`: Codice che identifica il tipo di prodotto di questa operazione. Enum: Z01=Petrolio grezzo; Z02=Olio combustibile; Z03=Gasolio; Z04=Benzina; Z05=Asfalto; Z06=Altri prodotti petroliferi; Z07=Gas energetici da petrolio; Z08=Minerale di ferro; Z09=Pirite; Z10=Altri minerali; Z11=Rottami di ferro; Z12=Carbone e coke di petrolio; Z13=Prodotti dell'acciaio; Z14=Fosfati; Z15=Potassa; Z16=Fertilizzanti naturali e artificiali; Z17=Prodotti chimici; Z18=Cemento e clinker; Z19=Legno e sughero; Z20=Materiali da costruzione; Z21=Cereali e loro farine; Z22=Fagioli e farine di soia; Z23=Frutta, ortaggi e legumi; Z24=Vini, bevande alcoliche e derivati; Z25=Sale comune; Z26=Carta e pasta di legno; Z27=Conserve; Z28=Tabacco, cacao, caffè e spezie; Z29=Oli e grassi; Z30=Altri prodotti alimentari; Z31=Macchinari, apparecchi, utensili e parti di ricambio; Z32=Automobili e parti; Z33=Pesce congelato; Z34=Resto della merce; Z35=Gas naturale; Z36=Altri prodotti metallurgici; Z37=Mangimi e foraggi; Z38=Tara per autocarri; Z39=Tara per container; Z40=Merce in contenitori in transito; Z41=Contenitori pieni; Z42=Contenitori vuoti; Z43=Veicoli; Z44=Parti di veicoli; Z91=Passeggeri; Z92=Passeggeri in crociera; 1=Pesce fresco; Z51=Biocarburanti; Z52=Altri minerali non metallici; ZR1=Zavorra sporca; ZR2=Cisterne per fanghi e decantazione; ZR3=Cisterne per acque oleose; ZR4=Acque sporche; ZR5=Rifiuti;  . Model: [https://schema.org/Text](https://schema.org/Text)- `remarks[string]`: Osservazioni sull'operazione  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `stevedoreRef[string]`: Id dello stivatore. Formato urn:mrn:<oid>:portcalls:operation:stevedore:9999  . Model: [https://schema.org/Text](https://schema.org/Text)- `stopRank[number]`: Grado o numero di questa fermata nella sosta (ormeggio o area di ancoraggio) ordinata per sequenza temporale  . Model: [https://schema.org/Number](https://schema.org/Number)- `terminal[string]`: Terminale in cui avviene l'operazione  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Tipo di entità NGSI. Deve essere Operazione. In alcuni standard internazionali è noto anche come [Ship's Stop].  - `year[number]`: Anno di inizio dell'ormeggio  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
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
## Esempi di payload  
#### Funzionamento Valori chiave NGSI-v2 Esempio  
Ecco un esempio di operazione in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### Funzionamento NGSI-v2 normalizzato Esempio  
Ecco un esempio di operazione in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
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
#### Funzionamento Valori chiave NGSI-LD Esempio  
Ecco un esempio di operazione in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### Funzionamento NGSI-LD normalizzato Esempio  
Ecco un esempio di operazione in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
