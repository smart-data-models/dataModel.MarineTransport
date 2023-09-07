<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: Hafen  
==============<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/Port/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Das Datenmodell dient der Bereitstellung von Informationen über Häfen**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.    
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `contactPoint[object]`: Die Angaben zur Kontaktaufnahme mit dem Artikel  . Model: [https://schema.org/ContactPoint](https://schema.org/ContactPoint)	- `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird. Ersetzt serviceArea    
	- `availabilityRestriction[*]`: Diese Eigenschaft verknüpft eine Kontaktstelle mit Informationen darüber, wann die Kontaktstelle nicht erreichbar ist. Die Details werden über die Klasse "Opening Hours Specification" bereitgestellt  . Model: [http://schema.org/hoursAvailable](http://schema.org/hoursAvailable)  
	- `availableLanguage[*]`: Eine Sprache, die jemand mit oder an dem Gegenstand, der Dienstleistung oder dem Ort verwenden kann. Bitte verwenden Sie einen der Sprachcodes aus dem IETF BCP 47 Standard. Es ist die Option Text implementiert, aber es könnte auch Sprache sein  . Model: [http://schema.org/availableLanguage](http://schema.org/availableLanguage)  
	- `contactOption[*]`: Eine unter dieser Kontaktstelle verfügbare Option (z. B. eine gebührenfreie Nummer oder Unterstützung für hörgeschädigte Anrufer)  . Model: [http://schema.org/contactOption](http://schema.org/contactOption)  
	- `contactType[string]`: Kontaktart dieses Artikels    
	- `email[idn-email]`: E-Mail Adresse des Eigentümers    
	- `faxNumber[string]`: Die Faxnummer  . Model: [http://schema.org/Text](http://schema.org/Text)  
	- `name[string]`: Der Name dieses Artikels    
	- `productSupported[string]`: Das Produkt oder die Dienstleistung, auf die sich diese Support-Kontaktstelle bezieht (z. B. Produktsupport für eine bestimmte Produktlinie). Dies kann ein bestimmtes Produkt oder eine Produktlinie (z. B. "iPhone") oder eine allgemeine Kategorie von Produkten oder Dienstleistungen (z. B. "Smartphones") sein.  . Model: [http://schema.org/Text](http://schema.org/Text)  
	- `telephone[string]`: Telefon dieser Kontaktperson    
- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `gln[number]`: Globale Standortnummer. Siehe [GLN](https://gs1id.org/global-location-number-gln)  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Eindeutiger Bezeichner der Entität  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `portArea[*]`: Geojson-Referenz auf das Element. Es kann Polygon oder MultiPolygon sein  - `portType[string]`: Enum: 'Meer, Inland, Fischerei, Warmwasser, Trocken'. Klassifizierung nach Art des Hafens  . Model: [http://schema.org/Text](http://schema.org/Text)- `refPortAuthority[*]`: Verweis auf die PortAuthority  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `timeZone[string]`: Der angegebene Wert sollte einer der in der IANA-Zeitzonendatenbank aufgeführten Werte sein. Siehe [Zeitzonendatenbank](https://timezonedb.com/time-zones)  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI-Entitätstyp. Es muss Port sein  - `unlocode[string]`: Code der Vereinten Nationen für Handels- und Verkehrsstandorte. Siehe [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `location`  - `type`  - `unlocode`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
## Beispiel-Nutzlasten  
#### Port NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen Port im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird, und liefert die Kontextdaten einer einzelnen Entität.  
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
  "gln":  123456789,  
  "portType": "Sea",  
  "refPortAuthority": "urn:mrn:amura:port-authority:UNLOCODE"  
}  
```  
</details>  
#### Port NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen Port im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
  "portArea":{  
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
      "type": "Reference",  
      "value": "urn:mrn:amura:port-authority:UNLOCODE"  
  }  
}  
```  
</details>  
#### Port NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen Port im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
  "gln":  123456789,  
  "portType": "Sea",  
  "refPortAuthority": "urn:mrn:amura:port-authority:UNLOCODE",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/context.jsonld",  
    "https://gitlab.com/hiades/fiware/smart-data-models/-/raw/main/context.jsonld"  
  ]  
}  
```  
</details>  
#### Port NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen Port im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
