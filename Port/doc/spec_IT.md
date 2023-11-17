<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entità: Porto    
=============<!-- /10-Header -->    
<!-- 15-License -->    
[Licenza aperta](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/Port/LICENSE.md)    
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descrizione globale: **Il modello di dati è destinato a fornire informazioni sulle porte**    
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
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `contactPoint[object]`: I dati da contattare con l'articolo  . Model: [https://schema.org/ContactPoint](https://schema.org/ContactPoint)	- `areaServed[string]`: L'area geografica in cui viene fornito un servizio o un articolo offerto. Sostituisce ServiceArea      
	- `availabilityRestriction[*]`: Questa proprietà collega un punto di contatto a informazioni su quando il punto di contatto non è disponibile. I dettagli sono forniti utilizzando la classe Specifica degli orari di apertura  . Model: [http://schema.org/hoursAvailable](http://schema.org/hoursAvailable)    
	- `availableLanguage[*]`: Una lingua che qualcuno può usare con o per l'oggetto, il servizio o il luogo. Utilizzare uno dei codici lingua dello standard BCP 47 dell'IETF. È stata implementata l'opzione Testo, ma potrebbe essere anche Lingua.  . Model: [http://schema.org/availableLanguage](http://schema.org/availableLanguage)    
	- `contactOption[*]`: Un'opzione disponibile su questo punto di contatto (ad esempio un numero verde o un supporto per chi chiama con problemi di udito)  . Model: [http://schema.org/contactOption](http://schema.org/contactOption)    
	- `contactType[string]`: Tipo di contatto di questo articolo      
	- `email[idn-email]`: Indirizzo e-mail del proprietario      
	- `faxNumber[string]`: Il numero di fax  . Model: [http://schema.org/Text](http://schema.org/Text)    
	- `name[string]`: Il nome di questo elemento      
	- `productSupported[string]`: Il prodotto o il servizio a cui si riferisce il punto di contatto dell'assistenza (ad esempio, l'assistenza per una particolare linea di prodotti). Può trattarsi di un prodotto o di una linea di prodotti specifici (ad esempio, "iPhone") o di una categoria generale di prodotti o servizi (ad esempio, "smartphone").  . Model: [http://schema.org/Text](http://schema.org/Text)    
	- `telephone[string]`: Telefono di questo contatto      
- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `gln[number]`: Numero di posizione globale. Vedere [GLN](https://gs1id.org/global-location-number-gln)  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `portArea[*]`: Riferimento geojson all'elemento. Può essere poligono o multipoligono.  - `portType[string]`: Enum: "Mare, Entroterra, Pesca, Acque calde, Secche". Classificazione per tipo di porto  . Model: [http://schema.org/Text](http://schema.org/Text)- `refPortAuthority[*]`: Riferimento alla PortAuthority  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `timeZone[string]`: Il valore fornito deve essere tra quelli elencati nel database dei fusi orari IANA. Vedere [Database dei fusi orari](https://timezonedb.com/time-zones).  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Tipo di entità NGSI. Deve essere Porta  - `unlocode[string]`: Codice delle Nazioni Unite per le località di commercio e trasporto. Vedere [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Proprietà richieste    
- `id`  - `location`  - `type`  - `unlocode`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modello di dati descrizione delle proprietà    
Ordinati in ordine alfabetico (clicca per i dettagli)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
Port:      
  description: The data model is intended to provide information about ports      
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
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    contactPoint:      
      description: The details to contact with the item      
      properties:      
        areaServed:      
          description: The geographic area where a service or offered item is provided. Supersedes serviceArea      
          type: string      
          x-ngsi:      
            type: Property      
        availabilityRestriction:      
          anyOf:      
            - description: Array of identifiers format of any NGSI entity      
              items:      
                maxLength: 256      
                minLength: 1      
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
                type: string      
              type: array      
              x-ngsi:      
                type: Property      
            - description: Array of identifiers format of any NGSI entity      
              items:      
                format: uri      
                type: string      
              type: array      
              x-ngsi:      
                type: Property      
          description: This property links a contact point to information about when the contact point is not available. The details are provided using the Opening Hours Specification class      
          x-ngsi:      
            model: http://schema.org/hoursAvailable      
            type: Relationship      
        availableLanguage:      
          anyOf:      
            - anyOf:      
                - type: string      
                - items:      
                    type: string      
                  type: array      
          description: 'A language someone may use with or at the item, service or place. Please use one of the language codes from the IETF BCP 47 standard. It is implemented the Text option but it could be also Language'      
          x-ngsi:      
            model: http://schema.org/availableLanguage      
            type: Property      
        contactOption:      
          anyOf:      
            - type: string      
            - items:      
                type: string      
              type: array      
          description: An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers)      
          x-ngsi:      
            model: http://schema.org/contactOption      
            type: Property      
        contactType:      
          description: Contact type of this item      
          type: string      
          x-ngsi:      
            type: Property      
        email:      
          description: Email address of owner      
          format: idn-email      
          type: string      
          x-ngsi:      
            type: Property      
        faxNumber:      
          description: The fax number      
          type: string      
          x-ngsi:      
            model: http://schema.org/Text      
            type: Property      
        name:      
          description: The name of this item      
          type: string      
          x-ngsi:      
            type: Property      
        productSupported:      
          description: The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. 'iPhone') or a general category of products or services (e.g. 'smartphones')      
          type: string      
          x-ngsi:      
            model: http://schema.org/Text      
            type: Property      
        telephone:      
          description: Telephone of this contact      
          type: string      
          x-ngsi:      
            type: Property      
        url:      
          description: URL which provides a description or further information about this item      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/ContactPoint      
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
    gln:      
      description: 'Global Location Number. See [GLN](https://gs1id.org/global-location-number-gln)'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
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
        type: Property      
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
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    portArea:      
      description: Geojson reference to the item. It can be Polygon or MultiPolygon      
      oneOf:      
        - $id: https://geojson.org/schema/Polygon.json      
          $schema: "http://json-schema.org/draft-07/schema#"      
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
        - $id: https://geojson.org/schema/MultiPolygon.json      
          $schema: "http://json-schema.org/draft-07/schema#"      
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
    portType:      
      description: 'Enum: ''Sea, Inland, Fishing, WarmWater, Dry''. Classification by type of port'      
      enum:      
        - Dry      
        - Fishing      
        - Inland      
        - Sea      
        - WarmWater      
      type: string      
      x-ngsi:      
        model: http://schema.org/Text      
        type: Property      
    refPortAuthority:      
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
      description: Reference to the PortAuthority      
      x-ngsi:      
        model: https://schema.org/URL      
        type: Relationship      
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
    timeZone:      
      description: 'The value provided should be among those listed in the IANA Time Zone Database. See [Time Zone Database](https://timezonedb.com/time-zones)'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    type:      
      description: NGSI Entity type. It has to be Port      
      enum:      
        - Port      
      type: string      
      x-ngsi:      
        type: Property      
    unlocode:      
      description: 'United Nations Code for Trade and Transport Locations. See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
  required:      
    - id      
    - type      
    - location      
    - unlocode      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/Port/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Ports/Port/schema.json      
  x-model-tags: ""      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Esempi di payload    
#### Porta NGSI-v2 valori-chiave Esempio    
Ecco un esempio di porta in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:mrn:amura:port:UNLOCODE",  
  "type": "Port",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -0.3048254137983776,  
      39.431348987126704  
    ]  
  },  
  "name": "Port name",  
  "unlocode": "Unlocode",  
  "description": "Port description",  
  "address": {  
    "streetAddress": "Avda. Example",  
    "addressCountry": "ES",  
    "addressLocality": "Locality",  
    "postalCode": "1234"  
  },  
  "contactPoint": {  
    "telephone": "+34 12 34 56 78",  
    "email": "example@port.com",  
    "availableLanguage": [  
      "en-EN",  
      "es-ES"  
    ],  
    "faxNumber": "12 345 67 89",  
    "name": "Portname",  
    "url": "https://URL"  
  },  
  "portArea": {  
    "type": "MultiPolygon",  
    "coordinates": [  
      [  
        [  
          [  
            -0.33295074395914526,  
            39.4631637203228  
          ],  
          [  
            -0.33295074395914526,  
            39.42053808578652  
          ],  
          [  
            -0.2829300303054083,  
            39.42053808578652  
          ],  
          [  
            -0.2829300303054083,  
            39.4631637203228  
          ],  
          [  
            -0.33295074395914526,  
            39.4631637203228  
          ]  
        ]  
      ]  
    ]  
  },  
  "timeZone": "Europe/London",  
  "gln": 123456789,  
  "portType": "Sea",  
  "refPortAuthority": "urn:mrn:amura:port-authority:UNLOCODE"  
}  
```  
</details>    
#### Porta NGSI-v2 normalizzata Esempio    
Ecco un esempio di Porta in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si usano le opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:mrn:amura:port:UNLOCODE",  
  "type": "Port",  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -0.3048254137983776,  
        39.431348987126704  
      ]  
    }  
  },  
  "name": {  
    "type": "Text",  
    "value": "Port name"  
  },  
  "unlocode": {  
    "type": "Text",  
    "value": "Unlocode"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Port description"  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Avda. Example",  
      "addressCountry": "ES",  
      "addressLocality": "Locality",  
      "postalCode": "1234"  
    }  
  },  
  "contactPoint": {  
    "type": "StructuredValue",  
    "value": {  
      "telephone": "+34 12 34 56 78",  
      "email": "example@port.com",  
      "availableLanguage": [  
        "en-EN",  
        "es-ES"  
      ],  
      "faxNumber": "12 345 67 89",  
      "name": "Portname",  
      "url": "https://URL"  
    }  
  },  
  "portArea": {  
    "type": "geo:json",  
    "value": {  
      "type": "MultiPolygon",  
      "coordinates": [  
        [  
          [  
            [  
              -0.33295074395914526,  
              39.4631637203228  
            ],  
            [  
              -0.33295074395914526,  
              39.42053808578652  
            ],  
            [  
              -0.2829300303054083,  
              39.42053808578652  
            ],  
            [  
              -0.2829300303054083,  
              39.4631637203228  
            ],  
            [  
              -0.33295074395914526,  
              39.4631637203228  
            ]  
          ]  
        ]  
      ]  
    }  
  },  
  "timeZone": {  
    "type": "Text",  
    "value": "Europe/London"  
  },  
  "gln": {  
    "type": "Number",  
    "value": 123456789  
  },  
  "portType": {  
    "type": "Text",  
    "value": "Sea"  
  },  
  "refPortAuthority": {  
    "type": "Text",  
    "value": "urn:mrn:amura:port-authority:UNLOCODE"  
  }  
}  
```  
</details>    
#### Valori chiave NGSI-LD della porta Esempio    
Ecco un esempio di porta in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:mrn:amura:port:UNLOCODE",  
  "type": "Port",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -0.3048254137983776,  
      39.431348987126704  
    ]  
  },  
  "name": "Port name",  
  "unlocode": "Unlocode",  
  "description": "Port description",  
  "address": {  
    "streetAddress": "Avda. Example",  
    "addressCountry": "ES",  
    "addressLocality": "Locality",  
    "postalCode": "1234"  
  },  
  "contactPoint": {  
    "telephone": "+34 12 34 56 78",  
    "email": "example@port.com",  
    "availableLanguage": [  
      "en-EN",  
      "es-ES"  
    ],  
    "faxNumber": "12 345 67 89",  
    "name": "Portname",  
    "url": "https://URL"  
  },  
  "portArea": {  
    "type": "MultiPolygon",  
    "coordinates": [  
      [  
        [  
          [  
            -0.33295074395914526,  
            39.4631637203228  
          ],  
          [  
            -0.33295074395914526,  
            39.42053808578652  
          ],  
          [  
            -0.2829300303054083,  
            39.42053808578652  
          ],  
          [  
            -0.2829300303054083,  
            39.4631637203228  
          ],  
          [  
            -0.33295074395914526,  
            39.4631637203228  
          ]  
        ]  
      ]  
    ]  
  },  
  "timeZone": "Europe/London",  
  "gln": 123456789,  
  "portType": "Sea",  
  "refPortAuthority": "urn:mrn:amura:port-authority:UNLOCODE",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/context.jsonld",  
    "https://gitlab.com/hiades/fiware/smart-data-models/-/raw/main/context.jsonld"  
  ]  
}  
```  
</details>    
#### Porta NGSI-LD normalizzata Esempio    
Ecco un esempio di porta in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:mrn:amura:port:UNLOCODE",  
  "type": "Port",  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
          -0.3048254137983776,  
          39.431348987126704  
      ]  
    }  
  },  
  "name": {  
      "type": "Property",  
      "value": "Port name"  
  },  
  "unlocode": {  
    "type": "Property",  
    "value": "Unlocode"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Port description"  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Avda. Example",  
      "addressCountry": "ES",  
      "addressLocality": "Locality",  
      "postalCode": "1234"  
    }  
  },  
  "contactPoint": {  
    "type": "Property",  
    "value": {  
      "telephone": "+34 12 34 56 78",  
      "email": "example@port.com",  
      "availableLanguage": [  
        "en-EN",  
        "es-ES"  
      ],  
      "faxProperty": "12 345 67 89",  
      "name": "Portname",  
      "url": "https://URL"  
    }  
  },  
  "portArea":{  
    "type": "GeoProperty",  
    "value": {  
      "type": "MultiPolygon",  
      "coordinates": [  
        [  
          [  
            [  
              -0.33295074395914526,  
              39.4631637203228  
            ],  
            [  
              -0.33295074395914526,  
              39.42053808578652  
            ],  
            [  
              -0.2829300303054083,  
              39.42053808578652  
            ],  
            [  
              -0.2829300303054083,  
              39.4631637203228  
            ],  
            [  
              -0.33295074395914526,  
              39.4631637203228  
            ]  
          ]  
        ]  
      ]  
    }  
  },  
  "timeZone": {  
    "type": "Property",  
    "value": "Europe/London"  
  },  
  "gln": {  
    "type": "Property",  
    "value": 123456789  
  },  
  "portType": {  
    "type": "Property",  
    "value": "Sea"  
  },  
  "refPortAuthority": {  
      "type": "Relationship",  
      "value": "urn:mrn:amura:port-authority:UNLOCODE"  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/context.jsonld",  
    "https://gitlab.com/hiades/fiware/smart-data-models/-/raw/main/context.jsonld"  
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
