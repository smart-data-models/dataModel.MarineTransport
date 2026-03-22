<!-- 10-Header -->  
 
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
 
Entity: NavigationSector  
======================== 
<!-- /10-Header -->  
 
<!-- 15-License -->  
 
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/NavigationSector/LICENSE.md)  
 
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
 
<!-- 20-Description -->  
 
Globalbeschreibung: **Dieses Datenmodell beschreibt einen Navigationssektor in einem Hafen, einschließlich geografischer Grenzen und betrieblicher Details**  
 
Version: 0.0.1  
<!-- /20-Description -->  
 
<!-- 30-PropertiesList -->  
 

## Liste der Eigenschaften  

 
<sup><sub>[*] Wenn in einem Attribut kein Typ angegeben ist, kann es mehrere Typen oder unterschiedliche Formate/Muster haben</sub></sup>  
- `address[object]`: Die Postanschrift. Modell: [https://schema.org/address](https://schema.org/address)  
	- `addressCountry[string]`: Das Land. Zum Beispiel Spanien. Modell: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: Die Ortschaft, in der sich die Straßenadresse befindet und die in der Region liegt. Modell: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: Die Region, in der sich die Ortschaft befindet und die im Land liegt. Modell: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird    
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel 03578. Modell: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel 24004. Modell: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: Die Straßenadresse. Modell: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Eine Nummer, die ein bestimmtes Grundstück auf einer öffentlichen Straße identifiziert    
- `alternateName[string]`: Ein alternativer Name für dieses Element  
- `areaServed[string]`: Der geografische Bereich, in dem ein Dienst oder ein angebotenes Element bereitgestellt wird. Modell: [https://schema.org/Text](https://schema.org/Text)  
- `dataProvider[string]`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Datenentität identifiziert  
- `dateCreated[date-time]`: Zeitstempel der Erstellung der Entität. Dieser wird normalerweise von der Speicherplattform zugewiesen  
- `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird normalerweise von der Speicherplattform zugewiesen  
- `description[string]`: Eine Beschreibung dieses Elements  
- `id[*]`: Eindeutiger Identifikator der Entität  
- `location[*]`: Geojson-Referenz zum Element. Es kann Punkt, Linie, Polygon, MultiPunkt, MultiLinie oder MultiPolygon sein  
- `minProbe[number]`: Mindestwassertiefe in Metern innerhalb des Sektors  
- `minProbeDate[date-time]`: Datum, an dem die Mindestwassertiefe zuletzt aufgezeichnet wurde  
- `modifiedDate[date-time]`: Datum und Uhrzeit der letzten Änderung der Navigationssektor-Entität  
- `mrn[string]`: MRN-kodierter Identifikator. Dieser muss in einer Weise mit der Entität in Verbindung stehen, die für verschiedene Organisationen bekannt ist, und alle nachfolgenden Parteien müssen seinen ursprünglichen Wert beibehalten. Dieser Identifikator muss ein eindeutiger Identifikator der PortCall-Entität sein, der vom System zugewiesen wird, das die Entität zuerst erstellt hat. Diese URN sollte den MRN- und IETF-Standards entsprechen, insbesondere RFC 2141, RFC 5234 und RFC 8141.   
    Das vorgeschlagene Format ist   
    id::='urn:mrn:eshuv:<ONSS>:portcalls:navigationsector:id:[0-9]+' oder    
    wobei OID:= Organisation UN/LOCODE, OONSS:=Organisationsname des Dienstes, 2099 das Jahr, in dem der PortCall initiiert wurde, 9999999 eine zunehmende, eindeutige Identifikator, die der Aussteller der Bollard-Entität in seinem System identifiziert (z. B. eine SQL-Zeile-Id),   
    z. B. urn:mrn:eshuv:portcalls:navigationsector:id:16   
     Siehe [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)In internationalen Standards ist dies auch als [Schiffsbesuch] bekannt  
- `name[string]`: Der Name dieses Elements  
- `navigationArea[string]`: Der breitere Navigationsbereich, in dem sich dieser Sektor befindet  
- `navigationSector[string]`: Identifikator für den Navigationssektor innerhalb des Hafens  
- `owner[array]`: Eine Liste, die eine JSON-kodierte Folge von Zeichen enthält, die auf die eindeutigen Ids der Eigentümer verweisen  
- `portCode[string]`: Code des Hafens, in dem sich dieser Navigationssektor befindet  
- `rank[number]`: Rang oder Prioritätslevel des Navigationssektors  
- `remarks[string]`: Zusätzliche Bemerkungen oder Notizen zum Navigationssektor  
- `sectorType[string]`: Typ des Navigationssektors  
- `seeAlso[*]`: Liste von URIs, die auf zusätzliche Ressourcen zum Element verweisen  
- `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angeben. Es wird empfohlen, den vollständig qualifizierten Domänennamen des Quellproviders oder die URL zum Quellobjekt zu verwenden  
- `type[string]`: NGSI-Entitätstyp. Dieser muss NavigationSector sein  
<!-- /30-PropertiesList -->  
 
<!-- 35-RequiredProperties -->  
 
Erforderliche Eigenschaften  
- `id`  
- `type`  
<!-- /35-RequiredProperties -->  
 
<!-- 40-NotesYaml -->  
 
<!-- /40-NotesYaml -->  
 
<!-- 50-DataModelHeader -->  
 
## Beschreibung des Datenmodells der Eigenschaften  
 
Sortiert alphabetisch (klicken für Details)  
<!-- /50-DataModelHeader -->  
 
<!-- 60-ModelYaml -->  
 
<details><summary><strong>Vollständige YAML-Details</strong></summary>    
 
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
 
## Beispiel-Payloads    
 
#### NavigationSector NGSI-v2 Schlüssel-Wert-Beispiel    
 
Hier ist ein Beispiel für einen NavigationSector im JSON-Format als Schlüssel-Wert. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und die Kontextdaten einer einzelnen Entität zurückgibt.  
<details><summary><strong>Beispiel anzeigen/verstecken</strong></summary>    
 
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
 
#### NavigationSector NGSI-v2 normalisiertes Beispiel    
 
Hier ist ein Beispiel für einen NavigationSector im JSON-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und die Kontextdaten einer einzelnen Entität zurückgibt.  
<details><summary><strong>Beispiel anzeigen/verstecken</strong></summary>    
 
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
 
#### NavigationSector NGSI-LD Schlüssel-Wert-Beispiel    
 
Hier ist ein Beispiel für einen NavigationSector im JSON-LD-Format als Schlüssel-Wert. Dies ist kompatibel mit NGSI-LD, wenn `options=keyValues` verwendet wird und die Kontextdaten einer einzelnen Entität zurückgibt.  
<details><summary><strong>Beispiel anzeigen/verstecken</strong></summary>    
 
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
 
#### NavigationSector NGSI-LD normalisiertes Beispiel    
 
Hier ist ein Beispiel für einen NavigationSector im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und die Kontextdaten einer einzelnen Entität zurückgibt.  
<details><summary><strong>Beispiel anzeigen/verstecken</strong></summary>    
 
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
 
Siehe [FAQ 10](https://smartdatamodels.org/index.php/faqs/), um eine Antwort darauf zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
 
<!-- 97-LastFooter -->  
 
---  
 
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
 

--- ENDE DES DOKUMENTS ---