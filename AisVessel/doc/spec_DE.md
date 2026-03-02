<!-- 10-Header -->  
 
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
 
Entity: AisVessel  
================= 
<!-- /10-Header -->  
 
<!-- 15-License -->  
 
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/AisVessel/LICENSE.md)  
 
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
 
<!-- 20-Description -->  
 
Globale Beschreibung: **NGSI-LD-Schema für die Entität AisVessel, das Informationen über Schiffe aus verschiedenen AIS-Datenquellen darstellt**  
 
Version: 0.0.1  
<!-- /20-Description -->  
 
<!-- 30-PropertiesList -->  
 

## Liste der Eigenschaften  

 
<sup><sub>[*] Wenn ein Attribut keinen Typ hat, kann es mehrere Typen oder unterschiedliche Formate/Muster haben</sub></sup>  
- `aisTypeSummary[string]`: Zusammenfassung des AIS-Schiffstyps  
- `alternateName[string]`: Alternativer Name für diesen Eintrag  
- `averageSpeed[number]`: Durchschnittliche Geschwindigkeit auf der letzten Reise  
- `beam[number]`: Breite oder Schiffsbreite  
- `callSign[string]`: Rufzeichen des Schiffes  
- `courseOverGround[number]`: Kurs über Grund (Grad)  
- `createdAt[date-time]`: Erstellungszeit der Aufzeichnung (ISO 8601)  
- `currentPortCountry[string]`: Land des aktuellen Hafens  
- `currentPortId[number]`: ID des aktuellen Hafens  
- `currentPortName[string]`: Name des aktuellen Hafens  
- `currentPortUnlocode[string]`: UN/LOCODE des aktuellen Hafens  
- `dataProvider[string]`: AIS-Datenanbieter  
- `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  
- `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird normalerweise von der Speicherplattform zugewiesen  
- `deletedAt[date-time]`: Logisches Löschdatum (ISO 8601)  
- `description[string]`: Beschreibung dieses Eintrags  
- `destination[string]`: Ziel des Schiffes  
- `distanceToGo[number]`: Verbleibende Entfernung zum Ziel  
- `distanceToPort[number]`: Entfernung zum Hafen  
- `distanceTravelled[number]`: Zurückgelegte Strecke seit dem letzten Hafen  
- `draught[number]`: Tiefgang des Schiffes  
- `dsrc[string]`: AIS-Quelle (TER, SAT, ROAM)  
- `dwt[number]`: Tragfähigkeit  
- `eta[date-time]`: Geschätzte Ankunftszeit (ISO 8601)  
- `etaCalculated[date-time]`: Berechnete ETA (ISO 8601)  
- `etaUpdatedAt[date-time]`: ETA zuletzt aktualisiert (ISO 8601)  
- `expectedArrival[boolean]`: Ist das Schiff erwartet, anzukommen  
- `flagCode[string]`: Ländercode der Flagge  
- `gt[number]`: Bruttoraumzahl  
- `heading[number]`: Steuerbord in Grad  
- `id[*]`: Eindeutige ID der Entität  
- `imo[number]`: IMO-Nummer des Schiffes  
- `lastPortCode[string]`: Vorheriger Hafencode  
- `lastPortCountry[string]`: Land des letzten Hafens  
- `lastPortId[number]`: ID des letzten Hafens  
- `lastPortName[string]`: Name des letzten Hafens  
- `lastPortTime[date-time]`: Abfahrtszeit vom letzten Hafen (ISO 8601)  
- `lastPortUnlocode[string]`: UN/LOCODE des letzten Hafens  
- `latitude[number]`: Breitengrad in Dezimalgrad  
- `lfore[number]`: Entfernung von der AIS-Station zum Bug  
- `loa[number]`: Gesamtlänge  
- `longitude[number]`: Längengrad in Dezimalgrad  
- `market[string]`: Kommerzieller Markt des Schiffes  
- `maxSpeed[number]`: Höchstgeschwindigkeit  
- `mmsi[number]`: MMSI-Nummer des Schiffes  
- `modifiedAt[date-time]`: Letzte Änderungszeit (ISO 8601)  
- `name[string]`: Name dieses Eintrags  
- `navigationStatus[number]`: Navigationsstatus-ID  
- `nextPortCode[string]`: Nächster Hafencode  
- `nextPortCountry[string]`: Land des nächsten Hafens  
- `nextPortId[number]`: ID des nächsten Hafens  
- `nextPortName[string]`: Name des nächsten Hafens  
- `nextPortUnlocode[string]`: UN/LOCODE des nächsten Hafens  
- `observedAt[date-time]`: Zeitstempel der letzten Beobachtung (ISO 8601)  
- `owner[array]`: Liste, die eine JSON-codierte Sequenz von Zeichen enthält, die auf die eindeutigen IDs der Eigentümer verweisen  
- `portCallNumber[string]`: Nummer des Hafenanlaufs  
- `portCode[string]`: Aktueller Hafencode  
- `publishedAt[date-time]`: Zeit, wenn der Datensatz veröffentlicht wurde (ISO 8601)  
- `rot[number]`: Drehgeschwindigkeit  
- `seeAlso[*]`: Liste von URIs, die auf zusätzliche Ressourcen zu diesem Eintrag verweisen  
- `shipClass[string]`: Klasse des Schiffes  
- `shipCountry[string]`: Land des Schiffes  
- `shipType[string]`: Schiffstyp aus AIS  
- `source[string]`: Eine Sequenz von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den vollständigen Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden  
- `speedOverGround[number]`: Geschwindigkeit über Grund (Knoten)  
- `type[string]`: NGSI-Entitätstyp. Muss 'AisVessel' sein  
- `typeName[string]`: Name des Schiffstyps von MarineTraffic  
- `utcSeconds[number]`: UTC-Sekunden des AIS-Zeitslots  
- `vesselInPort[boolean]`: Ist das Schiff derzeit im Hafen  
- `vesselName[string]`: Name des Schiffes  
- `vesselRef[string]`: Eindeutige Master-Schiffsreferenz  
- `wleft[number]`: Entfernung von der AIS-Station zur Backbordseite  
- `yearBuilt[number]`: Jahr, in dem das Schiff gebaut wurde  
<!-- /30-PropertiesList -->  
 
<!-- 35-RequiredProperties -->  
 
Erforderliche Eigenschaften  
- `id`  
- `latitude`  
- `longitude`  
- `mmsi`  
- `type`  
<!-- /35-RequiredProperties -->  
 
<!-- 40-NotesYaml -->  
 
<!-- /40-NotesYaml -->  
 
<!-- 50-DataModelHeader -->  
 
## Beschreibung des Datenmodells der Eigenschaften  
 
Alphabetisch sortiert (klicken für Details)  
<!-- /50-DataModelHeader -->  
 
<!-- 60-ModelYaml -->  
 
<details><summary><strong>Vollständige YAML-Details</strong></summary>    
 
```yaml  
AisVessel:    
  description: NGSI-LD schema for AisVessel entity, representing vessel AIS information from different AIS data-sources    
  properties:    
    aisTypeSummary:    
      description: AIS ship type summary    
      type: string    
      x-ngsi:    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    averageSpeed:    
      description: Average speed on last voyage    
      type: number    
      x-ngsi:    
        type: Property    
    beam:    
      description: Beam or width    
      type: number    
      x-ngsi:    
        type: Property    
        units: meters    
    callSign:    
      description: Call sign of the vessel    
      type: string    
      x-ngsi:    
        type: Property    
    courseOverGround:    
      description: Course over ground (degrees)    
      type: number    
      x-ngsi:    
        type: Property    
    createdAt:    
      description: Record creation time (ISO 8601)    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    currentPortCountry:    
      description: Country of current port    
      type: string    
      x-ngsi:    
        type: Property    
    currentPortId:    
      description: Current port ID    
      type: number    
      x-ngsi:    
        type: Property    
    currentPortName:    
      description: Current port name    
      type: string    
      x-ngsi:    
        type: Property    
    currentPortUnlocode:    
      description: UN/LOCODE of current port    
      type: string    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: AIS data provider    
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
    deletedAt:    
      description: Logical deletion time (ISO 8601)    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    destination:    
      description: Destination of the vessel    
      type: string    
      x-ngsi:    
        type: Property    
    distanceToGo:    
      description: Remaining distance to destination    
      type: number    
      x-ngsi:    
        type: Property    
    distanceToPort:    
      description: Distance to the port    
      type: number    
      x-ngsi:    
        type: Property    
    distanceTravelled:    
      description: Distance travelled since last port    
      type: number    
      x-ngsi:    
        type: Property    
    draught:    
      description: Draught of the vessel    
      type: number    
      x-ngsi:    
        type: Property    
        units: meters    
    dsrc:    
      description: AIS source (TER, SAT, ROAM)    
      type: string    
      x-ngsi:    
        type: Property    
    dwt:    
      description: Deadweight tonnage    
      type: number    
      x-ngsi:    
        type: Property    
    eta:    
      description: Estimated Time of Arrival (ISO 8601)    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    etaCalculated:    
      description: Calculated ETA (ISO 8601)    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    etaUpdatedAt:    
      description: ETA last updated (ISO 8601)    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    expectedArrival:    
      description: Is the vessel expected to arrive    
      type: boolean    
      x-ngsi:    
        type: Property    
    flagCode:    
      description: Country flag code    
      type: string    
      x-ngsi:    
        type: Property    
    gt:    
      description: Gross Tonnage    
      type: number    
      x-ngsi:    
        type: Property    
    heading:    
      description: Heading in degrees    
      type: number    
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
    imo:    
      description: IMO number of the vessel    
      type: number    
      x-ngsi:    
        type: Property    
    lastPortCode:    
      description: Previous port code    
      type: string    
      x-ngsi:    
        type: Property    
    lastPortCountry:    
      description: Country of last port    
      type: string    
      x-ngsi:    
        type: Property    
    lastPortId:    
      description: ID of the last port    
      type: number    
      x-ngsi:    
        type: Property    
    lastPortName:    
      description: Name of last port    
      type: string    
      x-ngsi:    
        type: Property    
    lastPortTime:    
      description: Departure time from last port (ISO 8601)    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    lastPortUnlocode:    
      description: UN/LOCODE of last port    
      type: string    
      x-ngsi:    
        type: Property    
    latitude:    
      description: Latitude in decimal degrees    
      type: number    
      x-ngsi:    
        type: Property    
    lfore:    
      description: Distance from AIS station to bow    
      type: number    
      x-ngsi:    
        type: Property    
    loa:    
      description: Length Overall    
      type: number    
      x-ngsi:    
        type: Property    
        units: meters    
    longitude:    
      description: Longitude in decimal degrees    
      type: number    
      x-ngsi:    
        type: Property    
    market:    
      description: Vessel's commercial market    
      type: string    
      x-ngsi:    
        type: Property    
    maxSpeed:    
      description: Maximum speed recorded    
      type: number    
      x-ngsi:    
        type: Property    
    mmsi:    
      description: MMSI number of the vessel    
      type: number    
      x-ngsi:    
        type: Property    
    modifiedAt:    
      description: Last modification time (ISO 8601)    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    navigationStatus:    
      description: Navigation status ID    
      type: number    
      x-ngsi:    
        type: Property    
    nextPortCode:    
      description: Next port code    
      type: string    
      x-ngsi:    
        type: Property    
    nextPortCountry:    
      description: Next port country    
      type: string    
      x-ngsi:    
        type: Property    
    nextPortId:    
      description: Next port ID    
      type: number    
      x-ngsi:    
        type: Property    
    nextPortName:    
      description: Next port name    
      type: string    
      x-ngsi:    
        type: Property    
    nextPortUnlocode:    
      description: UN/LOCODE of next port    
      type: string    
      x-ngsi:    
        type: Property    
    observedAt:    
      description: Timestamp of the last observation (ISO 8601)    
      format: date-time    
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
    portCallNumber:    
      description: Number of the port call    
      type: string    
      x-ngsi:    
        type: Property    
    portCode:    
      description: Current port code    
      type: string    
      x-ngsi:    
        type: Property    
    publishedAt:    
      description: Time when record was published (ISO 8601)    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    rot:    
      description: Rate of Turn    
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
    shipClass:    
      description: Class of the vessel    
      type: string    
      x-ngsi:    
        type: Property    
    shipCountry:    
      description: Country of the ship    
      type: string    
      x-ngsi:    
        type: Property    
    shipType:    
      description: Ship type from AIS    
      type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    speedOverGround:    
      description: Speed over ground (knots)    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. Must be 'AisVessel'    
      enum:    
        - AisVessel    
      type: string    
      x-ngsi:    
        type: Property    
    typeName:    
      description: MarineTraffic ship type name    
      type: string    
      x-ngsi:    
        type: Property    
    utcSeconds:    
      description: UTC seconds of AIS timeslot    
      type: number    
      x-ngsi:    
        type: Property    
    vesselInPort:    
      description: Is the vessel currently in port    
      type: boolean    
      x-ngsi:    
        type: Property    
    vesselName:    
      description: Name of the vessel    
      type: string    
      x-ngsi:    
        type: Property    
    vesselRef:    
      description: Unique Master Vessel Reference    
      type: string    
      x-ngsi:    
        type: Property    
    wleft:    
      description: Distance from AIS station to port side    
      type: number    
      x-ngsi:    
        type: Property    
    yearBuilt:    
      description: Year the vessel was built    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - mmsi    
    - latitude    
    - longitude    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/AisVessel/LICENSE.md    
  x-model-schema: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/AisVessel/schema.json    
  x-model-tags: ''    
  x-version: 0.0.1    
```  
</details>    
 
<!-- /60-ModelYaml -->  
 
<!-- 70-MiddleNotes -->  
 
<!-- /70-MiddleNotes -->  
 
<!-- 80-Examples -->  
 
## Beispiele für Nutzlasten    
 
#### AisVessel NGSI-v2 Schlüssel-Wert-Beispiel    
 
Hier ist ein Beispiel für ein AisVessel im JSON-Format als Schlüssel-Wert. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und die Kontextdaten einer einzelnen Entität zurückgibt.  
<details><summary><strong>Beispiel anzeigen/verstecken</strong></summary>    
 
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:aisvessel:mtid:11221",  
  "type": "AisVessel",  
  "distanceTravelled": 200,  
  "beam": 17.2,  
  "callSign": "PDSW",  
  "courseOverGround": 48,  
  "destination": "MA MOH > ESHUV",  
  "draught": 47,  
  "dwt": 4995,  
  "eta": "2025-11-08T20:00:00Z",  
  "flagCode": "NL",  
  "gt": 4703,  
  "heading": 322,  
  "imo": 9753832,  
  "latitude": 37.104038,  
  "loa": 108,  
  "longitude": -6.859847,  
  "maxSpeed": 12.3,  
  "mmsi": 244994000,  
  "navigationStatus": 1,  
  "portCallNumber": "ESHUV202501140",  
  "speedOverGround": 0.1,  
  "vesselName": "BITUMA",  
  "vesselRef": "urn:mrn:eshuv:portcalls:mastervessel:id:8028",  
  "dataProvider": "MarineTraffic",  
  "aisTypeSummary": "Tanker",  
  "averageSpeed": 11.2,  
  "currentPortCountry": "ES",  
  "currentPortId": 20645,  
  "currentPortName": "HUELVA ANCH",  
  "currentPortUnlocode": "ESHUV",  
  "distanceToGo": 0,  
  "distanceToPort": 7.86,  
  "dsrc": "TERR",  
  "etaCalculated": "2025-11-08T19:54:00Z",  
  "etaUpdatedAt": "2025-11-08T19:35:00Z",  
  "lastPortCountry": "MA",  
  "lastPortId": 811,  
  "lastPortName": "MOHAMMEDIA",  
  "lastPortTime": "2025-11-08T01:41:00Z",  
  "lastPortUnlocode": "MAMOH",  
  "lfore": 86,  
  "nextPortCountry": "ES",  
  "nextPortId": 1669,  
  "nextPortName": "HUELVA",  
  "nextPortUnlocode": "ESHUV",  
  "rot": 0,  
  "shipClass": "HANDYSIZE",  
  "shipCountry": "Netherlands",  
  "shipType": "80",  
  "utcSeconds": 21,  
  "vesselInPort": true,  
  "wleft": 2,  
  "yearBuilt": 2016,  
  "typeName": "Oil/Chemical Tanker",  
  "market": "WET BULK"  
}  
```  
</details>  
 
#### AisVessel NGSI-v2 normalisiertes Beispiel    
 
Hier ist ein Beispiel für ein AisVessel im JSON-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und die Kontextdaten einer einzelnen Entität zurückgibt.  
<details><summary><strong>Beispiel anzeigen/verstecken</strong></summary>    
 
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:aisvessel:mtid:11221",  
  "type": "AisVessel",  
  "distanceTravelled": {  
    "type": "Number",  
    "value": 200  
  },  
  "beam": {  
    "type": "Number",  
    "value": 17.2  
  },  
  "callSign": {  
    "type": "Text",  
    "value": "PDSW"  
  },  
  "courseOverGround": {  
    "type": "Number",  
    "value": 48  
  },  
  "destination": {  
    "type": "Text",  
    "value": "MA MOH > ESHUV"  
  },  
  "draught": {  
    "type": "Number",  
    "value": 47  
  },  
  "dwt": {  
    "type": "Number",  
    "value": 4995  
  },  
  "eta": {  
    "type": "DateTime",  
    "value": "2025-11-08T20:00:00Z"  
  },  
  "flagCode": {  
    "type": "Text",  
    "value": "NL"  
  },  
  "gt": {  
    "type": "Number",  
    "value": 4703  
  },  
  "heading": {  
    "type": "Number",  
    "value": 322  
  },  
  "imo": {  
    "type": "Number",  
    "value": 9753832  
  },  
  "latitude": {  
    "type": "Number",  
    "value": 37.104038  
  },  
  "loa": {  
    "type": "Number",  
    "value": 108  
  },  
  "longitude": {  
    "type": "Number",  
    "value": -6.859847  
  },  
  "maxSpeed": {  
    "type": "Number",  
    "value": 12.3  
  },  
  "mmsi": {  
    "type": "Number",  
    "value": 244994000  
  },  
  "navigationStatus": {  
    "type": "Number",  
    "value": 1  
  },  
  "portCallNumber": {  
    "type": "Text",  
    "value": "ESHUV202501140"  
  },  
  "speedOverGround": {  
    "type": "Number",  
    "value": 0.1  
  },  
  "vesselName": {  
    "type": "Text",  
    "value": "BITUMA"  
  },  
  "vesselRef": {  
    "type": "Text",  
    "value": "urn:mrn:eshuv:portcalls:mastervessel:id:8028"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "MarineTraffic"  
  },  
  "aisTypeSummary": {  
    "type": "Text",  
    "value": "Tanker"  
  },  
  "averageSpeed": {  
    "type": "Number",  
    "value": 11.2  
  },  
  "currentPortCountry": {  
    "type": "Text",  
    "value": "ES"  
  },  
  "currentPortId": {  
    "type": "Number",  
    "value": 20645  
  },  
  "currentPortName": {  
    "type": "Text",  
    "value": "HUELVA ANCH"  
  },  
  "currentPortUnlocode": {  
    "type": "Text",  
    "value": "ESHUV"  
  },  
  "distanceToGo": {  
    "type": "Number",  
    "value": 0  
  },  
  "distanceToPort": {  
    "type": "Number",  
    "value": 7.86  
  },  
  "dsrc": {  
    "type": "Text",  
    "value": "TERR"  
  },  
  "etaCalculated": {  
    "type": "DateTime",  
    "value": "2025-11-08T19:54:00Z"  
  },  
  "etaUpdatedAt": {  
    "type": "DateTime",  
    "value": "2025-11-08T19:35:00Z"  
  },  
  "lastPortCountry": {  
    "type": "Text",  
    "value": "MA"  
  },  
  "lastPortId": {  
    "type": "Number",  
    "value": 811  
  },  
  "lastPortName": {  
    "type": "Text",  
    "value": "MOHAMMEDIA"  
  },  
  "lastPortTime": {  
    "type": "DateTime",  
    "value": "2025-11-08T01:41:00Z"  
  },  
  "lastPortUnlocode": {  
    "type": "Text",  
    "value": "MAMOH"  
  },  
  "lfore": {  
    "type": "Number",  
    "value": 86  
  },  
  "nextPortCountry": {  
    "type": "Text",  
    "value": "ES"  
  },  
  "nextPortId": {  
    "type": "Number",  
    "value": 1669  
  },  
  "nextPortName": {  
    "type": "Text",  
    "value": "HUELVA"  
  },  
  "nextPortUnlocode": {  
    "type": "Text",  
    "value": "ESHUV"  
  },  
  "rot": {  
    "type": "Number",  
    "value": 0  
  },  
  "shipClass": {  
    "type": "Text",  
    "value": "HANDYSIZE"  
  },  
  "shipCountry": {  
    "type": "Text",  
    "value": "Netherlands"  
  },  
  "shipType": {  
    "type": "Text",  
    "value": "80"  
  },  
  "utcSeconds": {  
    "type": "Number",  
    "value": 21  
  },  
  "vesselInPort": {  
    "type": "Boolean",  
    "value": true  
  },  
  "wleft": {  
    "type": "Number",  
    "value": 2  
  },  
  "yearBuilt": {  
    "type": "Number",  
    "value": 2016  
  },  
  "typeName": {  
    "type": "Text",  
    "value": "Oil/Chemical Tanker"  
  },  
  "market": {  
    "type": "Text",  
    "value": "WET BULK"  
  }  
}  
```  
</details>  
 
#### AisVessel NGSI-LD Schlüssel-Wert-Beispiel    
 
Hier ist ein Beispiel für ein AisVessel im JSON-LD-Format als Schlüssel-Wert. Dies ist kompatibel mit NGSI-LD, wenn `options=keyValues` verwendet wird und die Kontextdaten einer einzelnen Entität zurückgibt.  
<details><summary><strong>Beispiel anzeigen/verstecken</strong></summary>    
 
```json  
{  
  "id": "urn:ngsi-ld:AisVessel:urn:mrn:eshuv:portcalls:aisvessel:mtid:11221",  
  "type": "AisVessel",  
  "distanceTravelled": 200,  
  "beam": 17.2,  
  "callSign": "PDSW",  
  "courseOverGround": 48,  
  "destination": "MA MOH > ESHUV",  
  "draught": 47,  
  "dwt": 4995,  
  "eta": "2025-11-08T20:00:00Z",  
  "flagCode": "NL",  
  "gt": 4703,  
  "heading": 322,  
  "imo": 9753832,  
  "latitude": 37.104038,  
  "loa": 108,  
  "longitude": -6.859847,  
  "maxSpeed": 12.3,  
  "mmsi": 244994000,  
  "navigationStatus": 1,  
  "portCallNumber": "ESHUV202501140",  
  "speedOverGround": 0.1,  
  "vesselName": "BITUMA",  
  "vesselRef": "urn:mrn:eshuv:portcalls:mastervessel:id:8028",  
  "dataProvider": "MarineTraffic",  
  "aisTypeSummary": "Tanker",  
  "averageSpeed": 11.2,  
  "currentPortCountry": "ES",  
  "currentPortId": 20645,  
  "currentPortName": "HUELVA ANCH",  
  "currentPortUnlocode": "ESHUV",  
  "distanceToGo": 0,  
  "distanceToPort": 7.86,  
  "dsrc": "TERR",  
  "etaCalculated": "2025-11-08T19:54:00Z",  
  "etaUpdatedAt": "2025-11-08T19:35:00Z",  
  "lastPortCountry": "MA",  
  "lastPortId": 811,  
  "lastPortName": "MOHAMMEDIA",  
  "lastPortTime": "2025-11-08T01:41:00Z",  
  "lastPortUnlocode": "MAMOH",  
  "lfore": 86,  
  "nextPortCountry": "ES",  
  "nextPortId": 1669,  
  "nextPortName": "HUELVA",  
  "nextPortUnlocode": "ESHUV",  
  "rot": 0,  
  "shipClass": "HANDYSIZE",  
  "shipCountry": "Netherlands",  
  "shipType": "80",  
  "utcSeconds": 21,  
  "vesselInPort": true,  
  "wleft": 2,  
  "yearBuilt": 2016,  
  "typeName": "Oil/Chemical Tanker",  
  "market": "WET BULK",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```  
</details>  
 
#### AisVessel NGSI-LD normalisiertes Beispiel    
 
Hier ist ein Beispiel für ein AisVessel im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und die Kontextdaten einer einzelnen Entität zurückgibt.  
<details><summary><strong>Beispiel anzeigen/verstecken</strong></summary>    
 
```json  
{  
  "id": "urn:ngsi-ld:AisVessel:urn:mrn:eshuv:portcalls:aisvessel:mtid:11221",  
  "type": "AisVessel",  
  "distanceTravelled": {  
    "type": "Property",  
    "value": 200  
  },  
  "beam": {  
    "type": "Property",  
    "value": 17.2  
  },  
  "callSign": {  
    "type": "Property",  
    "value": "PDSW"  
  },  
  "courseOverGround": {  
    "type": "Property",  
    "value": 48  
  },  
  "destination": {  
    "type": "Property",  
    "value": "MA MOH > ESHUV"  
  },  
  "draught": {  
    "type": "Property",  
    "value": 47  
  },  
  "dwt": {  
    "type": "Property",  
    "value": 4995  
  },  
  "eta": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2025-11-08T20:00:00Z"  
    }  
  },  
  "flagCode": {  
    "type": "Property",  
    "value": "NL"  
  },  
  "gt": {  
    "type": "Property",  
    "value": 4703  
  },  
  "heading": {  
    "type": "Property",  
    "value": 322  
  },  
  "imo": {  
    "type": "Property",  
    "value": 9753832  
  },  
  "latitude": {  
    "type": "Property",  
    "value": 37.104038  
  },  
  "loa": {  
    "type": "Property",  
    "value": 108  
  },  
  "longitude": {  
    "type": "Property",  
    "value": -6.859847  
  },  
  "maxSpeed": {  
    "type": "Property",  
    "value": 12.3  
  },  
  "mmsi": {  
    "type": "Property",  
    "value": 244994000  
  },  
  "navigationStatus": {  
    "type": "Property",  
    "value": 1  
  },  
  "portCallNumber": {  
    "type": "Property",  
    "value": "ESHUV202501140"  
  },  
  "speedOverGround": {  
    "type": "Property",  
    "value": 0.1  
  },  
  "vesselName": {  
    "type": "Property",  
    "value": "BITUMA"  
  },  
  "vesselRef": {  
    "type": "Property",  
    "value": "urn:mrn:eshuv:portcalls:mastervessel:id:8028"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "MarineTraffic"  
  },  
  "aisTypeSummary": {  
    "type": "Property",  
    "value": "Tanker"  
  },  
  "averageSpeed": {  
    "type": "Property",  
    "value": 11.2  
  },  
  "currentPortCountry": {  
    "type": "Property",  
    "value": "ES"  
  },  
  "currentPortId": {  
    "type": "Property",  
    "value": 20645  
  },  
  "currentPortName": {  
    "type": "Property",  
    "value": "HUELVA ANCH"  
  },  
  "currentPortUnlocode": {  
    "type": "Property",  
    "value": "ESHUV"  
  },  
  "distanceToGo": {  
    "type": "Property",  
    "value": 0  
  },  
  "distanceToPort": {  
    "type": "Property",  
    "value": 7.86  
  },  
  "dsrc": {  
    "type": "Property",  
    "value": "TERR"  
  },  
  "etaCalculated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2025-11-08T19:54:00Z"  
    }  
  },  
  "etaUpdatedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2025-11-08T19:35:00Z"  
    }  
  },  
  "lastPortCountry": {  
    "type": "Property",  
    "value": "MA"  
  },  
  "lastPortId": {  
    "type": "Property",  
    "value": 811  
  },  
  "lastPortName": {  
    "type": "Property",  
    "value": "MOHAMMEDIA"  
  },  
  "lastPortTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2025-11-08T01:41:00Z"  
    }  
  },  
  "lastPortUnlocode": {  
    "type": "Property",  
    "value": "MAMOH"  
  },  
  "lfore": {  
    "type": "Property",  
    "value": 86  
  },  
  "nextPortCountry": {  
    "type": "Property",  
    "value": "ES"  
  },  
  "nextPortId": {  
    "type": "Property",  
    "value": 1669  
  },  
  "nextPortName": {  
    "type": "Property",  
    "value": "HUELVA"  
  },  
  "nextPortUnlocode": {  
    "type": "Property",  
    "value": "ESHUV"  
  },  
  "rot": {  
    "type": "Property",  
    "value": 0  
  },  
  "shipClass": {  
    "type": "Property",  
    "value": "HANDYSIZE"  
  },  
  "shipCountry": {  
    "type": "Property",  
    "value": "Netherlands"  
  },  
  "shipType": {  
    "type": "Property",  
    "value": "80"  
  },  
  "utcSeconds": {  
    "type": "Property",  
    "value": 21  
  },  
  "vesselInPort": {  
    "type": "Property",  
    "value": true  
  },  
  "wleft": {  
    "type": "Property",  
    "value": 2  
  },  
  "yearBuilt": {  
    "type": "Property",  
    "value": 2016  
  },  
  "typeName": {  
    "type": "Property",  
    "value": "Oil/Chemical Tanker"  
  },  
  "market": {  
    "type": "Property",  
    "value": "WET BULK"  
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
 
