<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: KeyVessel  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/KeyVessel/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **The data model is intended to provide information about key vessels that a port community must focus his work on next days. It allows to represent the properties of each vessel: static and dynamic information**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: The country. For example, Spain  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: The locality in which the street address is, and which is in the region  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: The region in which the locality is, and which is in the country  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: A district is a type of administrative division that, in some countries, is managed by the local government    
	- `postOfficeBoxNumber[string]`: The post office box number for PO box addresses. For example, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: The postal code. For example, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: The street address  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Number identifying a specific property on a public street    
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `callSign[string]`: Maritime call signs are call signs assigned as unique identifiers to vessels  . Model: [https://schema.org/Text](https://schema.org/Text)- `courseOverGround[number]`: Course Over Ground (COG)  . Model: [https://schema.org/Number](https://schema.org/Number)- `createdDate[date-time]`: Date and time of creation of the entity represented by an ISO 8601 UTC format  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  . Model: [https://schema.org/Text](https://schema.org/Text)- `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `deletedDate[date-time]`: Date and time of deletion of the entity represented by an ISO 8601 UTC format  . Model: [https://schema.org/Text](https://schema.org/Text)- `description[string]`: A description of this item  - `etaAis[date-time]`: Estimated time of arrival, as it is reported by AIS system, represented by an ISO 8601 UTC format  . Model: [https://schema.org/Text](https://schema.org/Text)- `etaAlgorithm[date-time]`: Estimated time of arrival, computed by an algorithm based on vessel's positions, represented by an ISO 8601 UTC format  . Model: [https://schema.org/Text](https://schema.org/Text)- `flagCode[string]`: Maritime call signs are call signs assigned as unique identifiers to vessels  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: Unique identifier of the entity  - `imo[number]`: International Maritime Organization Number (a global forever UID)  . Model: [https://schema.org/Number](https://schema.org/Number)- `lastPortCode[string]`: Last port of call, coded.The code representing the port immediately previous to the port of arrival, if available. [EMSWe: DE-005-05] [EDIFACT:LOC-3227-92] [IMO:IMO0076]   . Model: [https://schema.org/Text](https://schema.org/Text)- `latitude[number]`: Latitude coordinate of the vessel  - `location[*]`: Geojson reference to the vessel position. It must be a Point where the vessel was placed at observedDate date  - `longitude[number]`: Longitude coordinate of the vessel  - `mmsi[number]`: Marine Mobile Service Identity Number (a temporarily assigned UID, issued by that object's current flag state)  . Model: [https://schema.org/Number](https://schema.org/Number)- `modifiedDate[date-time]`: Date and time of last modification of the entity represented by an ISO 8601 UTC format  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: The name of this item  - `navigationStatus[number]`: Enum:'0=Under way using engine, 1=At anchor, 2=Not under command, 3=Restricted manoeuverability,4=Constrained by her draught, 5=Moored, 6=Aground, 7=Engaged in Fishing, 8=Under way sailing, 9=Reserved for future amendment of Navigational state for HSC, 10=Reserved for future amendment of Navigational Status for WIG, 11=Reserved for future use, 12=Reserved for future use,13=Reserved for future use, 14=AIS-SART is active, 15=Not defined (default)'. Navigation Status. AIVDM/AIVDO data format'  . Model: [https://schema.org/Number](https://schema.org/Number)- `nextPortCode[string]`: Next port of call, coded.The code representing the port immediately previous to the port of arrival, if available.. Related to IALA_S211:nestPortCallCod / IMO. [EMSWe: DE-005-07] [EDIFACT:LOC-3227-61] [IMO:IMO0120]  . Model: [https://schema.org/Text](https://schema.org/Text)- `observedDate[date-time]`: Date and time of this observation represented by an ISO 8601 UTC format  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `portCallNumber[string]`: Port call identifier in MRN format. First element of the NSS should be the 5 character UN/Locode of the port, later the YEAR and finishing with a sequential number in this port [LLLLLYYYY99999] where LLLLL is the UN/LOCODE of the visited port, YYYY is the year, and 99999 is a unique sequential number assigned by port authority unique on each year (i.e. ESHUV202310323). An abbreviation can be used for UN/LOCODE (i.e. H202310323). The portCallNumber is assigned during the initial steps of the visit, but could be null at the beginning. In international standards is also known as [Port Call ID], [Visit ID] or [Port Call Coded]. See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) [EMSWe: DG-004/DG-004-01] [EDIFACT:BGM-1004] [IALA_S211:portCallId] [IMO:IMO108+IMO0153]  . Model: [https://schema.org/Text](https://schema.org/Text)- `portCallRef[uri]`: Reference to parent PortCall entity. [NGSI-MarineTransport.PortCall.id]  - `portCode[string]`: United Nations Code for Trade and Transport Locations. See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) [EMSWe: DE-004-04] [EDIFACT:LOC-3227-153] [IALA_S211:portCode] [IMO:IMO0108]   . Model: [https://schema.org/Text](https://schema.org/Text)- `positionAccuracy[number]`: Enum:'0=Low (> 10 m; autonomous mode of e.g.global navigation satellite system (GNSS) receiver or of other electronic position fixing device; default), 1=High (< 10 m; differential mode of e.g.DGNSS receiver)'. Code for the accuracy of the vessel position flag  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `speedOverGround[number]`: Speed Over Ground (SOG)  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI Entity type. It has to be KeyVessel  - `vesselAtPort[boolean]`: The vessel is in port limits, including waiting outside, at the harbor entrance, awaiting instructions, etc  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `vesselName[string]`: Vessel Name  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselRef[uri]`: Reference to parent MasterVessel entity. [NGSI-MarineTransport.MasterVessel.id]- urn:mrn:<oid>:portcalls:mastervessel:id:9999  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
KeyVessel:    
  description: 'The data model is intended to provide information about key vessels that a port community must focus his work on next days. It allows to represent the properties of each vessel: static and dynamic information'    
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
    callSign:    
      description: Maritime call signs are call signs assigned as unique identifiers to vessels    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    courseOverGround:    
      description: Course Over Ground (COG)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: degree    
    createdDate:    
      description: Date and time of creation of the entity represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      enum:    
        - AIS    
        - AISHUB    
        - ALGORITHM    
        - IA    
        - MARINETRAFFIC    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    deletedDate:    
      description: Date and time of deletion of the entity represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    etaAis:    
      description: Estimated time of arrival, as it is reported by AIS system, represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    etaAlgorithm:    
      description: Estimated time of arrival, computed by an algorithm based on vessel's positions, represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    flagCode:    
      description: Maritime call signs are call signs assigned as unique identifiers to vessels    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    imo:    
      description: International Maritime Organization Number (a global forever UID)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    lastPortCode:    
      description: 'Last port of call, coded.The code representing the port immediately previous to the port of arrival, if available. [EMSWe: DE-005-05] [EDIFACT:LOC-3227-92] [IMO:IMO0076] '    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    latitude:    
      description: Latitude coordinate of the vessel    
      type: number    
      x-ngsi:    
        type: Property    
    location:    
      '@id': http://uri.etsi.org/ngsi-ld/location    
      '@type': https://uri.etsi.org/ngsi-ld/GeoProperty    
      description: Geojson reference to the vessel position. It must be a Point where the vessel was placed at observedDate date    
      x-ngsi:    
        type: GeoProperty    
    longitude:    
      description: Longitude coordinate of the vessel    
      type: number    
      x-ngsi:    
        type: Property    
    mmsi:    
      description: Marine Mobile Service Identity Number (a temporarily assigned UID, issued by that object's current flag state)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    modifiedDate:    
      description: Date and time of last modification of the entity represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    navigationStatus:    
      description: Enum:'0=Under way using engine, 1=At anchor, 2=Not under command, 3=Restricted manoeuverability,4=Constrained by her draught, 5=Moored, 6=Aground, 7=Engaged in Fishing, 8=Under way sailing, 9=Reserved for future amendment of Navigational state for HSC, 10=Reserved for future amendment of Navigational Status for WIG, 11=Reserved for future use, 12=Reserved for future use,13=Reserved for future use, 14=AIS-SART is active, 15=Not defined (default)'. Navigation Status. AIVDM/AIVDO data format'    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
        - 6    
        - 7    
        - 8    
        - 9    
        - 10    
        - 11    
        - 12    
        - 13    
        - 14    
        - 15    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    nextPortCode:    
      description: 'Next port of call, coded.The code representing the port immediately previous to the port of arrival, if available.. Related to IALA_S211:nestPortCallCod / IMO. [EMSWe: DE-005-07] [EDIFACT:LOC-3227-61] [IMO:IMO0120]'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    observedDate:    
      description: Date and time of this observation represented by an ISO 8601 UTC format    
      format: date-time    
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
      description: 'Port call identifier in MRN format. First element of the NSS should be the 5 character UN/Locode of the port, later the YEAR and finishing with a sequential number in this port [LLLLLYYYY99999] where LLLLL is the UN/LOCODE of the visited port, YYYY is the year, and 99999 is a unique sequential number assigned by port authority unique on each year (i.e. ESHUV202310323). An abbreviation can be used for UN/LOCODE (i.e. H202310323). The portCallNumber is assigned during the initial steps of the visit, but could be null at the beginning. In international standards is also known as [Port Call ID], [Visit ID] or [Port Call Coded]. See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) [EMSWe: DG-004/DG-004-01] [EDIFACT:BGM-1004] [IALA_S211:portCallId] [IMO:IMO108+IMO0153]'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    portCallRef:    
      description: Reference to parent PortCall entity. [NGSI-MarineTransport.PortCall.id]    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    portCode:    
      description: 'United Nations Code for Trade and Transport Locations. See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) [EMSWe: DE-004-04] [EDIFACT:LOC-3227-153] [IALA_S211:portCode] [IMO:IMO0108] '    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    positionAccuracy:    
      description: Enum:'0=Low (> 10 m; autonomous mode of e.g.global navigation satellite system (GNSS) receiver or of other electronic position fixing device; default), 1=High (< 10 m; differential mode of e.g.DGNSS receiver)'. Code for the accuracy of the vessel position flag    
      enum:    
        - 0    
        - 1    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    speedOverGround:    
      description: Speed Over Ground (SOG)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meters per second    
    type:    
      description: NGSI Entity type. It has to be KeyVessel    
      enum:    
        - KeyVessel    
      type: string    
      x-ngsi:    
        type: Property    
    vesselAtPort:    
      description: The vessel is in port limits, including waiting outside, at the harbor entrance, awaiting instructions, etc    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    vesselName:    
      description: Vessel Name    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vesselRef:    
      description: Reference to parent MasterVessel entity. [NGSI-MarineTransport.MasterVessel.id]- urn:mrn:<oid>:portcalls:mastervessel:id:9999    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/KeyVessel/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/VesselAtPort/schema.json    
  x-model-tags: I4Trust    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
#### KeyVessel NGSI-v2 key-values Example    
Here is an example of a KeyVessel in JSON format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:portcallvessel:id:1234",  
  "type": "KeyVessel",  
  "vesselRef": "urn:mrn:eshuv:portcalls:mastervessel:imo:9863637",  
  "imo": 9863637,  
  "mmsi": 210049000,  
  "callSign": "5BPC3",  
  "flagCode": "ES",  
  "vesselName": "ELEANOR R.",  
  "portCode":   "ESHUV",  
  "lastPortCode": "ESPMI",  
  "nextPortCode": "ESVLC",  
  "portCallNumber": "ESHUV202401233",  
  "portCallRef": "urn:mrn:eshuv:portcalls:portcall:code:1233",  
  "dataProvider": "AIS",  
  "latitude": 37.2614,  
  "longitude":  -6.9447,  
  "speedOverGround": 11.3,  
  "courseOverGround": 122,  
  "navigationStatus": 4,  
  "observedDate": "2024-07-01T03:11:32Z",  
  "modifiedDate": "2024-07-01T03:07:12Z",  
  "createdDate": "2023-06-03T07:00:00Z",  
  "deletedDate": "2024-07-01T03:07:12Z"  
}  
```  
</details>  
#### KeyVessel NGSI-v2 normalized Example    
Here is an example of a KeyVessel in JSON format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:portcallvessel:id:1234",  
  "type": "KeyVessel",  
  "vesselRef": {  
    "type": "Text",  
    "value": "urn:mrn:eshuv:portcalls:mastervessel:imo:9863637"  
  },  
  "imo": {  
    "type": "Number",  
    "value": 9863637  
  },  
  "mmsi": {  
    "type": "Number",  
    "value": 210049000  
  },  
  "callSign": {  
    "type": "Text",  
    "value": "5BPC3"  
  },  
  "flagCode": {  
    "type": "Text",  
    "value": "ES"  
  },  
  "vesselName": {  
    "type": "Text",  
    "value": "ELEANOR R."  
  },  
  "portCode": {  
    "type": "Text",  
    "value": "ESHUV"  
  },  
  "lastPortCode": {  
    "type": "Text",  
    "value": "ESPMI"  
  },  
  "nextPortCode": {  
    "type": "Text",  
    "value": "ESVLC"  
  },  
  "portCallNumber": {  
    "type": "Text",  
    "value": "ESHUV202401233"  
  },  
  "portCallRef": {  
    "type": "Text",  
    "value": "urn:mrn:eshuv:portcalls:portcall:code:1233"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "AIS"  
  },  
  "latitude": {  
    "type": "Number",  
    "value": 37.2614  
  },  
  "longitude": {  
    "type": "Number",  
    "value": -6.9447  
  },  
  "speedOverGround": {  
    "type": "Number",  
    "value": 11.3  
  },  
  "courseOverGround": {  
    "type": "Number",  
    "value": 122  
  },  
  "navigationStatus": {  
    "type": "Number",  
    "value": 4  
  },  
  "observedDate": {  
    "type": "DateTime",  
    "value": "2024-07-01T03:11:32Z"  
  },  
  "modifiedDate": {  
    "type": "DateTime",  
    "value": "2024-07-01T03:07:12Z"  
  },  
  "createdDate": {  
    "type": "DateTime",  
    "value": "2023-06-03T07:00:00Z"  
  },  
  "deletedDate": {  
    "type": "DateTime",  
    "value": "2024-07-01T03:07:12Z"  
  }  
}  
```  
</details>  
#### KeyVessel NGSI-LD key-values Example    
Here is an example of a KeyVessel in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:KeyVessel:urn:mrn:eshuv:portcalls:portcallvessel:id:1234",  
  "type": "KeyVessel",  
  "vesselRef": "urn:mrn:eshuv:portcalls:mastervessel:imo:9863637",  
  "imo": 9863637,  
  "mmsi": 210049000,  
  "callSign": "5BPC3",  
  "flagCode": "ES",  
  "vesselName": "ELEANOR R.",  
  "portCode": "ESHUV",  
  "lastPortCode": "ESPMI",  
  "nextPortCode": "ESVLC",  
  "portCallNumber": "ESHUV202401233",  
  "portCallRef": "urn:mrn:eshuv:portcalls:portcall:code:1233",  
  "dataProvider": "AIS",  
  "latitude": 37.2614,  
  "longitude": -6.9447,  
  "speedOverGround": 11.3,  
  "courseOverGround": 122,  
  "navigationStatus": 4,  
  "observedDate": "2024-07-01T03:11:32Z",  
  "modifiedDate": "2024-07-01T03:07:12Z",  
  "createdDate": "2023-06-03T07:00:00Z",  
  "deletedDate": "2024-07-01T03:07:12Z",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### KeyVessel NGSI-LD normalized Example    
Here is an example of a KeyVessel in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:KeyVessel:urn:mrn:eshuv:portcalls:portcallvessel:id:1234",  
  "type": "KeyVessel",  
  "vesselRef": {  
    "type": "Property",  
    "value": "urn:mrn:eshuv:portcalls:mastervessel:imo:9863637"  
  },  
  "imo": {  
    "type": "Property",  
    "value": 9863637  
  },  
  "mmsi": {  
    "type": "Property",  
    "value": 210049000  
  },  
  "callSign": {  
    "type": "Property",  
    "value": "5BPC3"  
  },  
  "flagCode": {  
    "type": "Property",  
    "value": "ES"  
  },  
  "vesselName": {  
    "type": "Property",  
    "value": "ELEANOR R."  
  },  
  "portCode": {  
    "type": "Property",  
    "value": "ESHUV"  
  },  
  "lastPortCode": {  
    "type": "Property",  
    "value": "ESPMI"  
  },  
  "nextPortCode": {  
    "type": "Property",  
    "value": "ESVLC"  
  },  
  "portCallNumber": {  
    "type": "Property",  
    "value": "ESHUV202401233"  
  },  
  "portCallRef": {  
    "type": "Property",  
    "value": "urn:mrn:eshuv:portcalls:portcall:code:1233"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "AIS"  
  },  
  "latitude": {  
    "type": "Property",  
    "value": 37.2614  
  },  
  "longitude": {  
    "type": "Property",  
    "value": -6.9447  
  },  
  "speedOverGround": {  
    "type": "Property",  
    "value": 11.3  
  },  
  "courseOverGround": {  
    "type": "Property",  
    "value": 122  
  },  
  "navigationStatus": {  
    "type": "Property",  
    "value": 4  
  },  
  "observedDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-07-01T03:11:32Z"  
    }  
  },  
  "modifiedDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-07-01T03:07:12Z"  
    }  
  },  
  "createdDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2023-06-03T07:00:00Z"  
    }  
  },  
  "deletedDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-07-01T03:07:12Z"  
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
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
