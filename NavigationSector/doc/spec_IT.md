<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: Settore di navigazione  
========================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/NavigationSector/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Questo modello di dati descrive un settore di navigazione in un porto, compresi i confini geografici e i dettagli operativi**  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o formati/pattern diversi</sub></sup>  
- `address[object]`: L'indirizzo postale  . Modello: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, Spagna  . Modello: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La località in cui si trova l'indirizzo della strada, e che si trova nella regione  . Modello: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Modello: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestito dal governo locale    
	- `postOfficeBoxNumber[string]`: Il numero della casella postale per gli indirizzi della casella postale. Ad esempio, 03578  . Modello: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Modello: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'indirizzo della strada  . Modello: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numero che identifica una proprietà specifica in una strada pubblica    
- `alternateName[string]`: Un nome alternativo per questo elemento  - `areaServed[string]`: L'area geografica in cui un servizio o un elemento offerto è fornito  . Modello: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dei dati dell'entità armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Questo sarà solitamente assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Questo sarà solitamente assegnato dalla piattaforma di archiviazione  - `description[string]`: Una descrizione di questo elemento  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento Geojson all'elemento. Può essere Punto, LineString, Poligono, MultiPunto, MultiLineString o MultiPoligono  - `minProbe[number]`: Profondità minima dell'acqua in metri all'interno del settore  - `minProbeDate[date-time]`: Data in cui è stata registrata l'ultima profondità minima  - `modifiedDate[date-time]`: Data e ora dell'ultima modifica dell'entità del settore di navigazione  - `mrn[string]`: Identificatore codificato MRN. Deve essere relazionato all'entità in un modo noto a diversi organismi il significato e l'iniziatore dell'entità, e tutte le parti successive manterranno il suo valore originale. Questo identificatore deve essere un identificatore univoco dell'entità PortCall assegnato dal sistema che ha creato l'entità per la prima volta. Questo URN deve essere conforme a MRN e IETF, in particolare RFC 2141, RFC 5234 e RFC 8141.   
    Il formato proposto è   
    id::='urn:mrn:eshuv:<ONSS>:portcalls:navigationsector:id:[0-9]+' o    
    dove OID:= Organizzazione UN/LOCODE, OONSS:= Nome dell'organizzazione del servizio, 2099 l'anno in cui è stato avviato il portcall, 9999999 un identificatore univoco crescente che l'emittente dell'entità Bollard identificherà nel proprio sistema (ad esempio un ID di riga SQL),   
    ad esempio urn:mrn:eshuv:portcalls:navigationsector:id:16   
     Vedi [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) per ottenere una risposta su come gestire le unità di misura  
- `name[string]`: Il nome di questo elemento  - `navigationArea[string]`: L'area di navigazione più ampia in cui si trova questo settore  - `navigationSector[string]`: Identificatore del settore di navigazione all'interno del porto  - `owner[array]`: Un elenco che contiene una sequenza di caratteri codificati JSON che fa riferimento agli ID univoci dei proprietari  - `portCode[string]`: Codice del porto in cui si trova questo settore di navigazione  - `rank[number]`: Livello di priorità o rango del settore di navigazione  - `remarks[string]`: Osservazioni aggiuntive o note sul settore di navigazione  - `sectorType[string]`: Tipo di settore di navigazione  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che fornisce la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del fornitore di origine o l'URL dell'oggetto di origine  - `type[string]`: Tipo di entità NGSI. Deve essere NavigationSector  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Descrizione del modello di dati delle proprietà  
Ordinato alfabeticamente (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>dettagli yaml completi</strong></summary>    
```yaml  
NavigationSector:    
  description: This data model describes a navigation sector in a port, including geographic boundaries and operational details    
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
    minProbe:    
      description: Minimum depth of water in meters within the sector    
      type: number    
      x-ngsi:    
        type: Property    
    minProbeDate:    
      description: Date when the minimum depth was last recorded    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    modifiedDate:    
      description: Date and time of last modification of the navigation sector entity    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    mrn:    
      description: "MRN coded identifier. It has to be related to the entity in a way that is well-known by different organisms the meaning and the initiator of the entity, and all next parties will maintain on its origianl value. This identifier must be an UNIQUE identifier of the PortCall entity assigned by the system who created on first the entity. This URN should Conforms MRN & IETF specifically RFC 2141, RFC 5234, and RFC 8141. \n    The propossed format is \n    id::='urn:mrn:eshuv:<ONSS>:portcalls:navigationsector:id:[0-9]+' or  \n    where OID:= Organisation UN/LOCODE, OONSS:=Organization Name of Service, 2099 the year on which the portcall was initiated, 9999999 an increasing, unique identifier that the issuer of the Bollard entity will identify on his sistems (i.e. a SQL row-id), \n    i.e. urn:mrn:eshuv:portcalls:navigationsector:id:16 \n     See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)In international standards is also known as [Ship's Visit]"    
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
    navigationArea:    
      description: The broader navigation area where this sector is situated    
      type: string    
      x-ngsi:    
        type: Property    
    navigationSector:    
      description: Identifier for the navigation sector within the port    
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
      description: Code of the port where this navigation sector is located    
      type: string    
      x-ngsi:    
        type: Property    
    rank:    
      description: Rank or priority level of the navigation sector    
      type: number    
      x-ngsi:    
        type: Property    
    remarks:    
      description: Additional remarks or notes about the navigation sector    
      type: string    
      x-ngsi:    
        type: Property    
    sectorType:    
      description: Type of navigation sector    
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
    type:    
      description: NGSI Entity type. It has to be NavigationSector    
      enum:    
        - NavigationSector    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/NavigationSector/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/NavigationSector/schema.json    
  x-model-tags: ESHUV    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload    
#### Esempio di NavigationSector NGSI-v2 chiave-valore    
Ecco un esempio di NavigationSector in formato JSON come chiave-valore. Questo è compatibile con NGSI-v2 quando si utilizza `options=keyValues` e restituisce i dati di contesto di un'entità individuale.  
<details><summary><strong>mostra/nascondi esempio</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:facilities:navigationsector:id:10",  
  "type": "NavigationSector",  
  "portCode": "ESVLC",  
  "navigationSector": "S95",  
  "navigationArea": "AEXT",  
  "rank": 1,  
  "sectorType": "AEXT",  
  "minProbe": 99.0,  
  "minProbeDate": "2022-01-01T00:00:00",  
  "remarks": "Monoboya de crudo",  
  "location": {  
    "type": "Polygon",  
    "coordinates": [  
      [  
        [  
          -3.703790,  
          40.416775  
        ],  
        [  
          -3.703790,  
          40.426775  
        ],  
        [  
          -3.693790,  
          40.426775  
        ],  
        [  
          -3.693790,  
          40.416775  
        ]  
      ]  
    ]  
  }  
}  
```  
</details>  
#### Esempio di NavigationSector NGSI-v2 normalizzato    
Ecco un esempio di NavigationSector in formato JSON come normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di un'entità individuale.  
<details><summary><strong>mostra/nascondi esempio</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:facilities:navigationsector:id:10",  
  "type": "NavigationSector",  
  "portCode": {  
    "type": "Text",  
    "value": "ESVLC"  
  },  
  "navigationSector": {  
    "type": "Text",  
    "value": "S95"  
  },  
  "navigationArea": {  
    "type": "Text",  
    "value": "AEXT"  
  },  
  "rank": {  
    "type": "Number",  
    "value": 1  
  },  
  "sectorType": {  
    "type": "Text",  
    "value": "AEXT"  
  },  
  "minProbe": {  
    "type": "Number",  
    "value": 99.0  
  },  
  "minProbeDate": {  
    "type": "DateTime",  
    "value": "2022-01-01T00:00:00"  
  },  
  "remarks": {  
    "type": "Text",  
    "value": "Monoboya de crudo"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [  
        [  
          [  
            -3.70379,  
            40.416775  
          ],  
          [  
            -3.70379,  
            40.426775  
          ],  
          [  
            -3.69379,  
            40.426775  
          ],  
          [  
            -3.69379,  
            40.416775  
          ]  
        ]  
      ]  
    }  
  }  
}  
```  
</details>  
#### Esempio di NavigationSector NGSI-LD chiave-valore    
Ecco un esempio di NavigationSector in formato JSON-LD come chiave-valore. Questo è compatibile con NGSI-LD quando si utilizza `options=keyValues` e restituisce i dati di contesto di un'entità individuale.  
<details><summary><strong>mostra/nascondi esempio</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:NavigationSector:urn:mrn:eshuv:facilities:navigationsector:id:10",  
  "type": "NavigationSector",  
  "portCode": "ESVLC",  
  "navigationSector": "S95",  
  "navigationArea": "AEXT",  
  "rank": 1,  
  "sectorType": "AEXT",  
  "minProbe": 99.0,  
  "minProbeDate": "2022-01-01T00:00:00",  
  "remarks": "Monoboya de crudo",  
  "location": {  
    "type": "Polygon",  
    "coordinates": [  
      [  
        [  
          -3.703790,  
          40.416775  
        ],  
        [  
          -3.703790,  
          40.426775  
        ],  
        [  
          -3.693790,  
          40.426775  
        ],  
        [  
          -3.693790,  
          40.416775  
        ]  
      ]  
    ]  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Esempio di NavigationSector NGSI-LD normalizzato    
Ecco un esempio di NavigationSector in formato JSON-LD come normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di un'entità individuale.  
<details><summary><strong>mostra/nascondi esempio</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:NavigationSector:urn:mrn:eshuv:facilities:navigationsector:id:10",  
  "type": "NavigationSector",  
  "portCode": {  
    "type": "Property",  
    "value": "ESVLC"  
  },  
  "navigationSector": {  
    "type": "Property",  
    "value": "S95"  
  },  
  "navigationArea": {  
    "type": "Property",  
    "value": "AEXT"  
  },  
  "rank": {  
    "type": "Property",  
    "value": 1  
  },  
  "sectorType": {  
    "type": "Property",  
    "value": "AEXT"  
  },  
  "minProbe": {  
    "type": "Property",  
    "value": 99.0  
  },  
  "minProbeDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-01-01T00:00:00"  
    }  
  },  
  "remarks": {  
    "type": "Property",  
    "value": "Monoboya de crudo"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [  
        [  
          [  
            -3.70379,  
            40.416775  
          ],  
          [  
            -3.70379,  
            40.426775  
          ],  
          [  
            -3.69379,  
            40.426775  
          ],  
          [  
            -3.69379,  
            40.416775  
          ]  
        ]  
      ]  
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
Vedi [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di misura  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
