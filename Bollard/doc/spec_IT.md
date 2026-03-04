<!-- 10-Header -->  
 
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
 
Entità: Bollardo  
=============== 
<!-- /10-Header -->  
 
<!-- 15-License -->  
 
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/Bollard/LICENSE.md)  
 
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
 
<!-- 20-Description -->  
 
Descrizione globale: **Questo modello di dati descrive un bollardo in una struttura portuale, utilizzato per l'ormeggio delle navi.**  
 
versione: 0.0.1  
<!-- /20-Description -->  
 
<!-- 30-PropertiesList -->  
 

 
## Elenco delle proprietà  

 
<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o formati/modello diversi</sub></sup>  
- `address[object]`: L'indirizzo di posta  . Modello: [https://schema.org/address](https://schema.org/address)  
	- `addressCountry[string]`: Il paese. Ad esempio, Spagna  . Modello: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La località in cui si trova l'indirizzo di strada, e che si trova nella regione  . Modello: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Modello: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestito dal governo locale    
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di posta  . Ad esempio, 03578  . Modello: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Modello: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'indirizzo di strada  . Modello: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numero che identifica una proprietà specifica in una strada pubblica    
- `alternateName[string]`: Un nome alternativo per questo elemento   
- `areaServed[string]`: L'area geografica in cui un servizio o un elemento offerto è fornito  . Modello: [https://schema.org/Text](https://schema.org/Text)  
- `bollardIndex[number]`: Numero di indice del bollardo all'interno della struttura.   
- `code[string]`: Codice che identifica il bollardo.   
- `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzati   
- `dateCreated[date-time]`: Timestamp di creazione dell'entità. Questo sarà solitamente assegnato dalla piattaforma di archiviazione   
- `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Questo sarà solitamente assegnato dalla piattaforma di archiviazione   
- `description[string]`: Una descrizione di questo elemento   
- `distanceFromPrevious[number]`: Distanza in metri dal bollardo precedente.   
- `distanceFromStart[number]`: Distanza in metri dall'inizio della struttura.   
- `facilityRef[string]`: Riferimento all'entità della struttura a cui appartiene questo bollardo.   
- `id[*]`: Identificatore univoco dell'entità   
- `latitude[number]`: Coordinate di latitudine della posizione del bollardo.   
- `location[*]`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon   
- `longitude[number]`: Coordinate di longitudine della posizione del bollardo.   
- `modifiedDate[date-time]`: Data e ora dell'ultima modifica dell'entità del bollardo.   
- `mrn[string]`: Identificatore codificato MRN. Deve essere relazionato all'entità in un modo che sia ben noto a diverse organizzazioni il significato e l'iniziatore dell'entità, e tutte le parti successive manterranno il suo valore originale. Questo identificatore deve essere un identificatore univoco dell'entità PortCall assegnato dal sistema che ha creato per la prima volta l'entità. Questo URN dovrebbe conformarsi a MRN e IETF in particolare RFC 2141, RFC 5234 e RFC 8141. Il formato proposto è     id::='urn:mrn:eshuv:<ONSS>:portcalls:bollard:code:[0-9]+' o dove OID:= Organizzazione UN/LOCODE, OONSS:=Nome dell'organizzazione del servizio, 2099 l'anno in cui la chiamata del porto è stata avviata, 9999999 un identificatore univoco crescente che l'emittente dell'entità del bollardo identificherà nel suo sistema (ad esempio un ID di riga SQL), ad esempio urn:mrn:eshuv:portcalls:bollard:id:296 Vedi [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)Nello standard internazionale è noto anche come [Visita della nave]   
- `name[string]`: Il nome di questo elemento   
- `outOfOrder[boolean]`: Indica se il bollardo è attualmente fuori servizio.   
- `owner[array]`: Un elenco che contiene una sequenza di caratteri in formato JSON che fa riferimento agli ID univoci dei proprietari   
- `portCode[string]`: Codice del porto in cui si trova questo bollardo.   
- `probe[number]`: Profondità dell'acqua nella posizione del bollardo in metri.   
- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento   
- `source[string]`: Una sequenza di caratteri che fornisce la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del fornitore di origine o l'URL dell'oggetto di origine   
- `type[string]`: Tipo di entità NGSI. Deve essere Bollardo   
<!-- /30-PropertiesList -->  
 
<!-- 35-RequiredProperties -->  
 
Proprietà richieste  
- `bollardIndex`   
- `id`   
- `type`   
<!-- /35-RequiredProperties -->  
 
<!-- 40-NotesYaml -->  
 
<!-- /40-NotesYaml -->  
 
<!-- 50-DataModelHeader -->  
 
## Descrizione del modello di dati delle proprietà  
 
Ordinato alfabeticamente (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
 
<!-- 60-ModelYaml -->  
 
<details><summary><strong>dettagli yaml completi</strong></summary>    
 
```yaml  
Bollard:    
  description: This data model describes a bollard in a port facility, used for mooring vessels.    
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
    bollardIndex:    
      description: Index number of the bollard within the facility.    
      type: number    
      x-ngsi:    
        type: Property    
    code:    
      description: Code identifying the bollard.    
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
    distanceFromPrevious:    
      description: Distance in meters from the previous bollard.    
      type: number    
      x-ngsi:    
        type: Property    
    distanceFromStart:    
      description: Distance in meters from the start of the facility.    
      type: number    
      x-ngsi:    
        type: Property    
    facilityRef:    
      description: Reference to the facility entity this bollard belongs to.    
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
    latitude:    
      description: Latitude coordinate of the bollard location.    
      type: number    
      x-ngsi:    
        type: Property    
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
    longitude:    
      description: Longitude coordinate of the bollard location.    
      type: number    
      x-ngsi:    
        type: Property    
    modifiedDate:    
      description: Date and time of last modification of the bollard entity.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    mrn:    
      description: MRN coded identifier. It has to be related to the entity in a way that is well-known by different organisms the meaning and the initiator of the entity, and all next parties will maintain on its original value. This identifier must be an UNIQUE identifier of the PortCall entity assigned by the system who created on first the entity. This URN should Conforms MRN & IETF specifically RFC 2141, RFC 5234, and RFC 8141. The propossed format is     id::='urn:mrn:eshuv:<ONSS>:portcalls:bollard:code:[0-9]+' or where OID:= Organisation UN/LOCODE, OONSS:=Organization Name of Service, 2099 the year on which the portcall was initiated, 9999999 an increasing, unique identifier that the issuer of the Bollard entity will identify on his sistems (i.e. a SQL row-id), i.e. urn:mrn:eshuv:portcalls:bollard:id:296 See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)In international standards is also known as [Ship's Visit]    
      enum:    
        - PortCall    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    outOfOrder:    
      description: Indicates if the bollard is currently out of order.    
      type: boolean    
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
      description: Code of the port where this bollard is located.    
      type: string    
      x-ngsi:    
        type: Property    
    probe:    
      description: Water depth at the bollard location in meters.    
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
    source:    
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be Bollard    
      enum:    
        - Bollard    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - bollardIndex    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/Bollard/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/Bollard/schema.json    
  x-model-tags: ESHUV    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
 
<!-- 70-MiddleNotes -->  
 
<!-- /70-MiddleNotes -->  
 
<!-- 80-Examples -->  
 
## Esempi di payload    
 
#### Esempio di Bollardo NGSI-v2 chiave-valore    
 
Ecco un esempio di un Bollardo in formato JSON come chiave-valore. Questo è compatibile con NGSI-v2 quando si utilizza `options=keyValues` e restituisce i dati di contesto di un'entità individuale.  
<details><summary><strong>mostra/nascondi esempio</strong></summary>    
 
```json  
{  
  "id": "urn:mrn:eshuv:facilities:bollard:id:20",  
  "type": "Bollard",  
  "portCode": "ESVLC",  
  "facilityRef": "urn:mrn:eshuv:facilities:facility:code:20",  
  "code": "1",  
  "bollardIndex": 4,  
  "probe": 12.5,  
  "distanceFromPrevious": 15.0,  
  "distanceFromStart": 132.2,  
  "latitude": 37.2614,  
  "longitude":  -6.9447,  
  "outOfOrder": false  
}  
```  
</details>  
 
#### Esempio di Bollardo NGSI-v2 normalizzato    
 
Ecco un esempio di un Bollardo in formato JSON come normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di un'entità individuale.  
<details><summary><strong>mostra/nascondi esempio</strong></summary>    
 
```json  
{  
  "id": "urn:mrn:eshuv:facilities:bollard:id:20",  
  "type": "Bollard",  
  "portCode": {  
    "type": "Text",  
    "value": "ESVLC"  
  },  
  "facilityRef": {  
    "type": "Text",  
    "value": "urn:mrn:eshuv:facilities:facility:code:20"  
  },  
  "code": {  
    "type": "Text",  
    "value": "1"  
  },  
  "bollardIndex": {  
    "type": "Number",  
    "value": 4  
  },  
  "probe": {  
    "type": "Number",  
    "value": 12.5  
  },  
  "distanceFromPrevious": {  
    "type": "Number",  
    "value": 15.0  
  },  
  "distanceFromStart": {  
    "type": "Number",  
    "value": 132.2  
  },  
  "latitude": {  
    "type": "Number",  
    "value": 37.2614  
  },  
  "longitude": {  
    "type": "Number",  
    "value": -6.9447  
  },  
  "outOfOrder": {  
    "type": "Boolean",  
    "value": false  
  }  
}  
```  
</details>  
 
#### Esempio di Bollardo NGSI-LD chiave-valore    
 
Ecco un esempio di un Bollardo in formato JSON-LD come chiave-valore. Questo è compatibile con NGSI-LD quando si utilizza `options=keyValues` e restituisce i dati di contesto di un'entità individuale.  
<details><summary><strong>mostra/nascondi esempio</strong></summary>    
 
```json  
{  
  "id": "urn:ngsi-ld:Bollard:urn:mrn:eshuv:facilities:bollard:id:20",  
  "type": "Bollard",  
  "portCode": "ESVLC",  
  "facilityRef": "urn:mrn:eshuv:facilities:facility:code:20",  
  "code": "1",  
  "bollardIndex": 4,  
  "probe": 12.5,  
  "distanceFromPrevious": 15.0,  
  "distanceFromStart": 132.2,  
  "latitude": 37.2614,  
  "longitude": -6.9447,  
  "outOfOrder": false,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```  
</details>  
 
#### Esempio di Bollardo NGSI-LD normalizzato    
 
Ecco un esempio di un Bollardo in formato JSON-LD come normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di un'entità individuale.  
<details><summary><strong>mostra/nascondi esempio</strong></summary>    
 
```json  
{  
  "id": "urn:ngsi-ld:Bollard:urn:mrn:eshuv:facilities:bollard:id:20",  
  "type": "Bollard",  
  "portCode": {  
    "type": "Property",  
    "value": "ESVLC"  
  },  
  "facilityRef": {  
    "type": "Property",  
    "value": "urn:mrn:eshuv:facilities:facility:code:20"  
  },  
  "code": {  
    "type": "Property",  
    "value": "1"  
  },  
  "bollardIndex": {  
    "type": "Property",  
    "value": 4  
  },  
  "probe": {  
    "type": "Property",  
    "value": 12.5  
  },  
  "distanceFromPrevious": {  
    "type": "Property",  
    "value": 15.0  
  },  
  "distanceFromStart": {  
    "type": "Property",  
    "value": 132.2  
  },  
  "latitude": {  
    "type": "Property",  
    "value": 37.2614  
  },  
  "longitude": {  
    "type": "Property",  
    "value": -6.9447  
  },  
  "outOfOrder": {  
    "type": "Property",  
    "value": false  
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
 
Vedi [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di misura  
<!-- /95-Units -->  
 
<!-- 97-LastFooter -->  
 
---  
 
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->