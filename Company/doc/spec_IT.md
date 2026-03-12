<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: Azienda  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/Company/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Questo modello di dati descrive un'azienda in un porto**  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o formati/modello diversi</sub></sup>  
- `active[boolean]`: Stato di attivazione dell'azienda o entità con attività o responsabilità nel porto  - `address[object]`: L'indirizzo postale  . Modello: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, Spagna  . Modello: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La località in cui si trova l'indirizzo stradale, e che si trova nella regione  . Modello: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Modello: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestito dal governo locale    
	- `postOfficeBoxNumber[string]`: Il numero della casella postale per gli indirizzi di posta  . Ad esempio, 03578  . Modello: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Modello: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'indirizzo stradale  . Modello: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numero che identifica una proprietà specifica in una strada pubblica    
- `admissionDate[date-string]`: Data in cui l'azienda è stata registrata nel modello  - `alias[string]`: Nome non ufficiale (soprannome) dell'azienda o entità con attività o responsabilità nel porto  - `alternateName[string]`: Un nome alternativo per questo elemento  - `areaServed[string]`: L'area geografica in cui un servizio o un elemento offerto è fornito  . Modello: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzati  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Questo sarà solitamente assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Questo sarà solitamente assegnato dalla piattaforma di archiviazione  - `description[string]`: Una descrizione di questo elemento  - `email[idn-email]`: Indirizzo email del proprietario  - `entityType[string]`: Tipo di azienda o entità con attività o responsabilità nel porto  - `id[*]`: Identificatore univoco dell'entità  - `legalCode[string]`: Codice dell'azienda o entità con attività o responsabilità nel porto  - `licenses[array]`: Licenze di operazione dell'azienda. Di solito in coppia, codice e descrizione  - `location[*]`: Riferimento Geojson all'elemento. Può essere Punto, LineString, Poligono, MultiPunto, MultiLineString o MultiPoligono  - `mrn[string]`: Identificatore codificato MRN. Questo URN dovrebbe essere conforme a MRN e IETF in particolare RFC 2141, RFC 5234 e RFC 8141. Il formato proposto è  id::='urn:mrn:<PORT>:<ONSS>:community:company:id:[0-9]+' o dove PORT := UN/LOCODE del porto, OID:= Organizzazione UN/LOCODE, OONSS:=Organizzazione Nome del Servizio, 9999999 un identificatore univoco che il creatore dell'entità del registro dell'azienda identificherà nei propri sistemi (ad esempio un ID di riga SQL), ad esempio urn:mrn:eshuv:community:company:id:1296  - `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco che contiene una sequenza di caratteri JSON che fa riferimento agli ID univoci dei proprietari  - `registeredName[string]`: Nome ufficiale dell'azienda o entità con attività o responsabilità nel porto  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che fornisce la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del fornitore di origine o l'URL dell'oggetto di origine  - `telephone[string]`: Telefono di questo contatto  - `type[*]`: Tipo di entità NGSI. Deve essere Azienda  <!-- /30-PropertiesList -->  
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
Company:    
  description: This data model describes a company in a port    
  properties:    
    active:    
      description: Status of activation of the company or entity with activities or responsibility in the port    
      type: boolean    
      x-ngsi:    
        type: Property    
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
    admissionDate:    
      description: Date in which the company was registered in the model    
      format: date-string    
      type: string    
      x-ngsi:    
        type: Property    
    alias:    
      description: Non official Name (nickname) of the company or entity with activities or responsibility in the port    
      type: string    
      x-ngsi:    
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
    email:    
      description: Email address of owner    
      format: idn-email    
      type: string    
      x-ngsi:    
        type: Property    
    entityType:    
      description: Type of the company or entity with activities or responsibility in the port    
      enum:    
        - Agent    
        - Carrier    
        - Consignee    
        - LogisticsOperator    
        - PortAuthority    
        - PortReceptionFacilityOperator    
        - PublicBody    
        - ServiceProvider    
        - Steevedore    
        - TerminalOperator    
        - TransportCompany    
        - WasteManagementCompany    
        - Other    
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
    legalCode:    
      description: Code of the company or entity with activities or responsibility in the port    
      type: string    
      x-ngsi:    
        type: Property    
    licenses:    
      description: Licenses of operation of the Company. Usually in pairs, code and description    
      items:    
        description: Description of an item of the licenses. Usually a pair code and description    
        items:    
          description: Every item in the usual pairs. Can be either the code or the description    
          type: string    
          x-ngsi:    
            type: Property    
        type: array    
        x-ngsi:    
          type: Property    
      type: array    
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
    mrn:    
      description: MRN coded identifier. This URN should Conforms MRN & IETF specifically RFC 2141, RFC 5234, and RFC 8141. The proposed format is  id::='urn:mrn:<PORT>:<ONSS>:community:company:id:[0-9]+' or where PORT := UN/LOCODE of port, OID:= Organisation UN/LOCODE, OONSS:=Organization Name of Service, 9999999 an unique identifier that the creator of the company registry entity will identify on his systems (i.e. a SQL row-id), i.e. urn:mrn:eshuv:community:company:id:1296    
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
    registeredName:    
      description: official Name of the company or entity with activities or responsibility in the port    
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
    telephone:    
      description: Telephone of this contact    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be Company    
      enum:    
        - Company    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/Company/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/company/schema.json    
  x-model-tags: ESHUV    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload    
#### Esempio di azienda NGSI-v2 chiave-valore    
Ecco un esempio di un'azienda in formato JSON come chiave-valore. Questo è compatibile con NGSI-v2 quando si utilizza `options=keyValues` e restituisce i dati di contesto di un'entità individuale.  
<details><summary><strong>mostra/nascondi esempio</strong></summary>    
```json  
{  
  "type": "Company",  
  "dataProvider": "PCS/other",  
  "id": "urn:mrn:eshuv:pcs:company:cif:B90244585",  
  "legalCode": "B90244585",  
  "registeredName": "BERGE Maritima SL",  
  "alias": "BERGE",  
  "entityType": "Consignee",  
  "address": {  
    "streetAddress": "Avda Sociedad colombina Onubense",  
    "addressLocality": "Huelva",  
    "addressRegion": "Andalucía",  
    "addressCountry": "ES",  
    "postalCode": "21300",  
    "streetNr": "S/N"  
  },  
  "email": "berge@puertohuelva.es",  
  "telephone": "900252526",  
  "active": true,  
  "admissionDate": "2024-12-01T00:00:00",  
  "licenses": [  
    [  
      "Suministro de combustible a buques mediante camión",  
      "SC-013"  
    ],  
    [  
      "SCM-003",  
      "Suministro de combustible a maquinaria mediante camión"  
    ],  
    [  
      "MAR-23",  
      "MarpolAnnex1"  
    ]  
  ]  
}  
```  
</details>  
#### Esempio di azienda NGSI-v2 normalizzato    
Ecco un esempio di un'azienda in formato JSON come normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di un'entità individuale.  
<details><summary><strong>mostra/nascondi esempio</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:pcs:company:cif:B90244585",  
  "type": "Company",  
  "dataProvider": {  
    "type": "Text",  
    "value": "PCS/other"  
  },  
  "legalCode": {  
    "type": "Text",  
    "value": "B90244585"  
  },  
  "registeredName": {  
    "type": "Text",  
    "value": "BERGE Maritima SL"  
  },  
  "alias": {  
    "type": "Text",  
    "value": "BERGE"  
  },  
  "entityType": {  
    "type": "Text",  
    "value": "Consignee"  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "streetAddress": "Avda Sociedad colombina Onubense",  
      "addressLocality": "Huelva",  
      "addressRegion": "Andalucía",  
      "addressCountry": "ES",  
      "postalCode": "21300",  
      "streetNr": "S/N"  
    }  
  },  
  "email": {  
    "type": "Text",  
    "value": "berge@puertohuelva.es"  
  },  
  "telephone": {  
    "type": "Text",  
    "value": "900252526"  
  },  
  "active": {  
    "type": "Boolean",  
    "value": true  
  },  
  "admissionDate": {  
    "type": "DateTime",  
    "value": "2024-12-01T00:00:00"  
  },  
  "licenses": {  
    "type": "Array",  
    "value": [  
      [  
        "Suministro de combustible a buques mediante camión",  
        "SC-013"  
      ],  
      [  
        "SCM-003",  
        "Suministro de combustible a maquinaria mediante camión"  
      ],  
      [  
        "MAR-23",  
        "MarpolAnnex1"  
      ]  
    ]  
  }  
}  
```  
</details>  
#### Esempio di azienda NGSI-LD chiave-valore    
Ecco un esempio di un'azienda in formato JSON-LD come chiave-valore. Questo è compatibile con NGSI-LD quando si utilizza `options=keyValues` e restituisce i dati di contesto di un'entità individuale.  
<details><summary><strong>mostra/nascondi esempio</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Company:urn:mrn:eshuv:pcs:company:cif:B90244585",  
  "type": "Company",  
  "dataProvider": "PCS/other",  
  "legalCode": "B90244585",  
  "registeredName": "BERGE Maritima SL",  
  "alias": "BERGE",  
  "entityType": "Consignee",  
  "address": {  
    "streetAddress": "Avda Sociedad colombina Onubense",  
    "addressLocality": "Huelva",  
    "addressRegion": "Andalucía",  
    "addressCountry": "ES",  
    "postalCode": "21300",  
    "streetNr": "S/N"  
  },  
  "email": "berge@puertohuelva.es",  
  "telephone": "900252526",  
  "active": true,  
  "admissionDate": "2024-12-01T00:00:00",  
  "licenses": [  
    [  
      "Suministro de combustible a buques mediante camión",  
      "SC-013"  
    ],  
    [  
      "SCM-003",  
      "Suministro de combustible a maquinaria mediante camión"  
    ],  
    [  
      "MAR-23",  
      "MarpolAnnex1"  
    ]  
  ],  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Esempio di azienda NGSI-LD normalizzato    
Ecco un esempio di un'azienda in formato JSON-LD come normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di un'entità individuale.  
<details><summary><strong>mostra/nascondi esempio</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Company:urn:mrn:eshuv:pcs:company:cif:B90244585",  
  "type": "Company",  
  "dataProvider": {  
    "type": "Property",  
    "value": "PCS/other"  
  },  
  "legalCode": {  
    "type": "Property",  
    "value": "B90244585"  
  },  
  "registeredName": {  
    "type": "Property",  
    "value": "BERGE Maritima SL"  
  },  
  "alias": {  
    "type": "Property",  
    "value": "BERGE"  
  },  
  "entityType": {  
    "type": "Property",  
    "value": "Consignee"  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Avda Sociedad colombina Onubense",  
      "addressLocality": "Huelva",  
      "addressRegion": "Andalucía",  
      "addressCountry": "ES",  
      "postalCode": "21300",  
      "streetNr": "S/N"  
    }  
  },  
  "email": {  
    "type": "Property",  
    "value": "berge@puertohuelva.es"  
  },  
  "telephone": {  
    "type": "Property",  
    "value": "900252526"  
  },  
  "active": {  
    "type": "Property",  
    "value": true  
  },  
  "admissionDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-12-01T00:00:00"  
    }  
  },  
  "licenses": {  
    "type": "Property",  
    "value": [  
      [  
        "Suministro de combustible a buques mediante camión",  
        "SC-013"  
      ],  
      [  
        "SCM-003",  
        "Suministro de combustible a maquinaria mediante camión"  
      ],  
      [  
        "MAR-23",  
        "MarpolAnnex1"  
      ]  
    ]  
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