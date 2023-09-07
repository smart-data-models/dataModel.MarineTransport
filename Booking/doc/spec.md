<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: Booking  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/Booking/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **Provide the bookings electronic messaging description**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `actualWindowFrom[number]`: Time window actually used, if arrival was 15’ earlier  - `actualWindowTo[number]`: Time window actually used  - `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: The country. For example, Spain  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: The locality in which the street address is, and which is in the region  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: The region in which the locality is, and which is in the country  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: A district is a type of administrative division that, in some countries, is managed by the local government    
	- `postOfficeBoxNumber[string]`: The post office box number for PO box addresses. For example, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: The postal code. For example, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: The street address  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `bookingDate[number]`: Booking date  - `bookingNumber[number]`: Unique ID of the booking  - `bookingStatus[string]`: Booking status  - `company[string]`: Company making the booking  - `containersExport[number]`: Number of containers to pick-up from the CT yard  - `containersImport[number]`: Number of containers to drop-off to the CT yard  - `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `enterDate[number]`: Actual time of entering  - `exportContainer1[string]`: Unique container ID for 1st container to be picked-up  - `exportContainer2[string]`: Unique container ID for 2nd container to be picked-up  - `id[*]`: Unique identifier of the entity  - `importContainer1[string]`: Unique container ID for 1st container to be dropped-off  - `importContainer2[string]`: Unique container ID for 2nd container to be dropped-off  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name[string]`: The name of this item  - `originalWindowFrom[number]`: Originally booked time window to enter  - `originalWindowTo[number]`: Originally estimated time window to leave  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `windowDate[number]`: Date of the time window  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Limitation of the size of trucks to two containers justify having properties ended 1 and 2.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Booking:    
  description: Provide the bookings electronic messaging description    
  properties:    
    actualWindowFrom:    
      description: 'Time window actually used, if arrival was 15’ earlier'    
      type: number    
      x-ngsi:    
        type: Property    
    actualWindowTo:    
      description: Time window actually used    
      type: number    
      x-ngsi:    
        type: Property    
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
    bookingDate:    
      description: Booking date    
      type: number    
      x-ngsi:    
        type: Property    
    bookingNumber:    
      description: Unique ID of the booking    
      type: number    
      x-ngsi:    
        type: Property    
    bookingStatus:    
      description: Booking status    
      enum:    
        - Pending    
        - No show    
        - Visited    
        - Cancelled by user (on time)    
        - No-slot booking    
      type: string    
      x-ngsi:    
        type: Property    
    company:    
      description: Company making the booking    
      type: string    
      x-ngsi:    
        type: Property    
    containersExport:    
      description: Number of containers to pick-up from the CT yard    
      maximum: 2    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    containersImport:    
      description: Number of containers to drop-off to the CT yard    
      maximum: 2    
      minimum: 0    
      type: number    
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
    enterDate:    
      description: Actual time of entering    
      type: number    
      x-ngsi:    
        type: Property    
    exportContainer1:    
      description: Unique container ID for 1st container to be picked-up    
      type: string    
      x-ngsi:    
        type: Property    
    exportContainer2:    
      description: Unique container ID for 2nd container to be picked-up    
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
        type: Property    
    importContainer1:    
      description: Unique container ID for 1st container to be dropped-off    
      type: string    
      x-ngsi:    
        type: Property    
    importContainer2:    
      description: Unique container ID for 2nd container to be dropped-off    
      type: string    
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
    originalWindowFrom:    
      description: Originally booked time window to enter    
      type: number    
      x-ngsi:    
        type: Property    
    originalWindowTo:    
      description: Originally estimated time window to leave    
      type: number    
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
    windowDate:    
      description: Date of the time window    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/Booking/LICENSE.md    
  x-model-schema: https://github.com/smart-data-models/dataModel.MarineTransport/master/Booking/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
#### Booking NGSI-v2 key-values Example    
Here is an example of a Booking in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ThPA:Booking:463589473290389",  
  "type": "Booking",  
  "bookingNumber": 463589473290389,  
  "bookingDate": 20220621,  
  "company": "Pantelis Bouratsis",  
  "enterDate": 2021,  
  "originalWindowFrom": 660,  
  "actualWindowFrom": 645,  
  "originalWindowTo": 720,  
  "actualWindowTo": 960,  
  "windowDate": 20220621,  
  "bookingStatus": "Pending",  
  "containersImport": 1,  
  "containersExport": 2,  
  "exportContainer1": "",  
  "exportContainer2": "",  
  "importContainer1": "ZCSU7627029",  
  "importContainer2": ""  
}  
```  
</details>  
#### Booking NGSI-v2 normalized Example    
Here is an example of a Booking in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ThPA:Booking:463589473290389",  
  "type": "Booking",  
  "actualWindowFrom": {  
    "type": "Number",  
    "value": 645,  
    "metadata": {}  
  },  
  "actualWindowTo": {  
    "type": "Number",  
    "value": 960,  
    "metadata": {}  
  },  
  "bookingDate": {  
    "type": "Text",  
    "value": "20220621",  
    "metadata": {}  
  },  
  "bookingNumber": {  
    "type": "Text",  
    "value": "463589473290389",  
    "metadata": {}  
  },  
  "bookingStatus": {  
    "type": "Text",  
    "value": "Pending",  
    "metadata": {}  
  },  
  "company": {  
    "type": "Text",  
    "value": "Pantelis Bouratsis",  
    "metadata": {}  
  },  
  "containersExport": {  
    "type": "Number",  
    "value": 0,  
    "metadata": {}  
  },  
  "containersImport": {  
    "type": "Number",  
    "value": 1,  
    "metadata": {}  
  },  
  "exportContainer1": {  
    "type": "Text",  
    "value": "",  
    "metadata": {}  
  },  
  "exportContainer2": {  
    "type": "Text",  
    "value": "",  
    "metadata": {}  
  },  
  "importContainer1": {  
    "type": "Text",  
    "value": "ZCSU7627029",  
    "metadata": {}  
  },  
  "importContainer2": {  
    "type": "Text",  
    "value": "",  
    "metadata": {}  
  },  
  "originalWindowFrom": {  
    "type": "Number",  
    "value": 660,  
    "metadata": {}  
  },  
  "originalWindowTo": {  
    "type": "Number",  
    "value": 720,  
    "metadata": {}  
  },  
  "windowDate": {  
    "type": "Text",  
    "value": "20220621",  
    "metadata": {}  
  }  
}  
```  
</details>  
#### Booking NGSI-LD key-values Example    
Here is an example of a Booking in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ThPA:Booking:463589473290389",  
  "type": "Booking",  
  "bookingNumber": 463589473290389,  
  "bookingDate": 20220621,  
  "company": "Pantelis Bouratsis",  
  "enterDate": 2021,  
  "originalWindowFrom": 660,  
  "actualWindowFrom": 645,  
  "originalWindowTo": 720,  
  "actualWindowTo": 960,  
  "windowDate": 20220621,  
  "bookingStatus": "Pending",  
  "containersImport": 1,  
  "containersExport": 2,  
  "exportContainer1": "",  
  "exportContainer2": "",  
  "importContainer1": "ZCSU7627029",  
  "importContainer2": "",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Booking NGSI-LD normalized Example    
Here is an example of a Booking in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ThPA:Booking:463589473290389",  
  "type": "Booking",  
  "actualWindowFrom": {  
    "type": "Property",  
    "value": 645  
  },  
  "actualWindowTo": {  
    "type": "Property",  
    "value": 960  
  },  
  "bookingDate": {  
    "type": "Property",  
    "value": "20220621"  
  },  
  "bookingProperty": {  
    "type": "Property",  
    "value": "463589473290389"  
  },  
  "bookingStatus": {  
    "type": "Property",  
    "value": "Pending"  
  },  
  "company": {  
    "type": "Property",  
    "value": "Pantelis Bouratsis"  
  },  
  "containersExport": {  
    "type": "Property",  
    "value": 0  
  },  
  "containersImport": {  
    "type": "Property",  
    "value": 1  
  },  
  "exportContainer1": {  
    "type": "Property",  
    "value": ""  
  },  
  "exportContainer2": {  
    "type": "Property",  
    "value": ""  
  },  
  "importContainer1": {  
    "type": "Property",  
    "value": "ZCSU7627029"  
  },  
  "importContainer2": {  
    "type": "Property",  
    "value": ""  
  },  
  "originalWindowFrom": {  
    "type": "Property",  
    "value": 660  
  },  
  "originalWindowTo": {  
    "type": "Property",  
    "value": 720  
  },  
  "windowDate": {  
    "type": "Property",  
    "value": "20220621"  
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
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
