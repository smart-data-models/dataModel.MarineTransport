<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: Unternehmen  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/Company/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Dieses Datenmodell beschreibt ein Unternehmen in einem Hafen**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn in einem Attribut kein Typ angegeben ist, kann dies daran liegen, dass es mehrere Typen oder unterschiedliche Formate/Muster haben kann</sub></sup>  
- `active[boolean]`: Status der Aktivierung des Unternehmens oder der Entität mit Aktivitäten oder Verantwortung im Hafen  - `address[object]`: Die Postanschrift  . Modell: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel Spanien  . Modell: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: Die Ortschaft, in der sich die Straßenadresse befindet und die in der Region liegt  . Modell: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: Die Region, in der sich die Ortschaft befindet und die im Land liegt  . Modell: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird    
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Modell: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Modell: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: Die Straßenadresse  . Modell: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Nummer, die ein bestimmtes Grundstück auf einer öffentlichen Straße identifiziert    
- `admissionDate[date-string]`: Datum, an dem das Unternehmen im Modell registriert wurde  - `alias[string]`: Inoffizieller Name (Spitzname) des Unternehmens oder der Entität mit Aktivitäten oder Verantwortung im Hafen  - `alternateName[string]`: Ein alternativer Name für diesen Eintrag  - `areaServed[string]`: Das geografische Gebiet, in dem ein Dienst oder ein angebotenes Element bereitgestellt wird  . Modell: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Datenentität identifiziert  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `description[string]`: Eine Beschreibung dieses Elements  - `email[idn-email]`: E-Mail-Adresse des Eigentümers  - `entityType[string]`: Typ des Unternehmens oder der Entität mit Aktivitäten oder Verantwortung im Hafen  - `id[*]`: Eindeutige Identifikationsnummer der Entität  - `legalCode[string]`: Code des Unternehmens oder der Entität mit Aktivitäten oder Verantwortung im Hafen  - `licenses[array]`: Betriebslizenzen des Unternehmens. Normalerweise in Paaren, Code und Beschreibung  - `location[*]`: Geojson-Referenz zum Element. Es kann sich um einen Punkt, eine Linie, ein Polygon, einen Multi-Punkt, eine Multi-Linie oder ein Multi-Polygon handeln  - `mrn[string]`: MRN-kodierter Identifikator. Diese URN sollte MRN- und IETF-Konformität erfüllen, insbesondere RFC 2141, RFC 5234 und RFC 8141. Das vorgeschlagene Format ist  id::='urn:mrn:<PORT>:<ONSS>:community:company:id:[0-9]+' oder wobei PORT := UN/LOCODE des Hafens, OID:= Organisation UN/LOCODE, OONSS:=Organisationsname des Dienstes, 9999999 eine eindeutige Identifikationsnummer, die der Ersteller der Unternehmensregistrierungsentität in seinem System identifiziert (z. B. eine SQL-Zeile-Id), z. B. urn:mrn:eshuv:community:company:id:1296  - `name[string]`: Der Name dieses Elements  - `owner[array]`: Eine Liste, die eine JSON-kodierte Folge von Zeichen enthält, die auf die eindeutigen IDs der Eigentümer verweisen  - `registeredName[string]`: Offizieller Name des Unternehmens oder der Entität mit Aktivitäten oder Verantwortung im Hafen  - `seeAlso[*]`: Liste von URIs, die auf zusätzliche Ressourcen zu diesem Element verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angeben. Es wird empfohlen, den vollständig qualifizierten Domänennamen des Quellproviders oder die URL des Quellobjekts zu verwenden  - `telephone[string]`: Telefonnummer dieses Kontakts  - `type[*]`: NGSI-Entitätstyp. Es muss Unternehmen sein  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Beschreibung des Datenmodells der Eigenschaften  
Sortiert alphabetisch (klicken für Details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>Vollständige YAML-Details</strong></summary>    
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
## Beispiele für Nutzlasten    
#### Unternehmen NGSI-v2 Schlüssel-Wert-Beispiel    
Hier ist ein Beispiel für ein Unternehmen im JSON-Format als Schlüssel-Wert. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und die Kontextdaten einer einzelnen Entität zurückgibt.  
<details><summary><strong>Beispiel anzeigen/verstecken</strong></summary>    
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
#### Unternehmen NGSI-v2 normalisiertes Beispiel    
Hier ist ein Beispiel für ein Unternehmen im JSON-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und die Kontextdaten einer einzelnen Entität zurückgibt.  
<details><summary><strong>Beispiel anzeigen/verstecken</strong></summary>    
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
#### Unternehmen NGSI-LD Schlüssel-Wert-Beispiel    
Hier ist ein Beispiel für ein Unternehmen im JSON-LD-Format als Schlüssel-Wert. Dies ist kompatibel mit NGSI-LD, wenn `options=keyValues` verwendet wird und die Kontextdaten einer einzelnen Entität zurückgibt.  
<details><summary><strong>Beispiel anzeigen/verstecken</strong></summary>    
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
#### Unternehmen NGSI-LD normalisiertes Beispiel    
Hier ist ein Beispiel für ein Unternehmen im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und die Kontextdaten einer einzelnen Entität zurückgibt.  
<details><summary><strong>Beispiel anzeigen/verstecken</strong></summary>    
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
Siehe [FAQ 10](https://smartdatamodels.org/index.php/faqs/), um eine Antwort darauf zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->