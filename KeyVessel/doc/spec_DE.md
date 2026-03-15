<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: KeyVessel  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/KeyVessel/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Das Datenmodell soll Informationen über die wichtigsten Schiffe liefern, auf die sich die Hafencommunity in den nächsten Tagen konzentrieren muss. Es ermöglicht die Darstellung der Eigenschaften jedes Schiffes: statische und dynamische Informationen**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn in einem Attribut kein Typ angegeben ist, liegt dies daran, dass es mehrere Typen oder unterschiedliche Formate/Muster haben kann</sub></sup>  
- `address[object]`: Die Postanschrift. Modell: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel Spanien. Modell: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: Die Ortschaft, in der die Straßenadresse liegt und die in der Region liegt. Modell: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: Die Region, in der die Ortschaft liegt und die im Land liegt. Modell: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird    
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel 03578. Modell: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel 24004. Modell: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: Die Straßenadresse. Modell: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Eine Nummer, die ein bestimmtes Grundstück auf einer öffentlichen Straße identifiziert    
- `alternateName[string]`: Ein alternativer Name für dieses Element  - `areaServed[string]`: Das geografische Gebiet, in dem ein Dienst oder ein angebotenes Element bereitgestellt wird. Modell: [https://schema.org/Text](https://schema.org/Text)- `callSign[string]`: Seefunkrufzeichen sind Rufzeichen, die als eindeutige Identifikatoren für Schiffe zugewiesen werden. Modell: [https://schema.org/Text](https://schema.org/Text)- `courseOverGround[number]`: Kurs über Grund (COG). Modell: [https://schema.org/Number](https://schema.org/Number)- `createdDate[date-time]`: Datum und Uhrzeit der Erstellung der durch ein ISO 8601-UTC-Format dargestellten Entität. Modell: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Datenentität identifiziert. Modell: [https://schema.org/Text](https://schema.org/Text)- `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `deletedDate[date-time]`: Datum und Uhrzeit der Löschung der durch ein ISO 8601-UTC-Format dargestellten Entität. Modell: [https://schema.org/Text](https://schema.org/Text)- `description[string]`: Eine Beschreibung dieses Elements  - `etaAis[date-time]`: Geschätzte Ankunftszeit, wie sie vom AIS-System gemeldet wird, dargestellt in einem ISO 8601-UTC-Format. Modell: [https://schema.org/Text](https://schema.org/Text)- `etaAlgorithm[date-time]`: Geschätzte Ankunftszeit, berechnet durch einen Algorithmus auf der Grundlage der Schiffpositionen, dargestellt in einem ISO 8601-UTC-Format. Modell: [https://schema.org/Text](https://schema.org/Text)- `flagCode[string]`: Seefunkrufzeichen sind Rufzeichen, die als eindeutige Identifikatoren für Schiffe zugewiesen werden. Modell: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: Eindeutiger Identifikator der Entität  - `imo[number]`: Internationale Seeschifffahrts-Organisation-Nummer (eine global eindeutige UID) . Modell: [https://schema.org/Number](https://schema.org/Number)- `lastPortCode[string]`: Letzter Hafen, kodiert. Der Code, der den Hafen unmittelbar vor dem Ankunftshafen darstellt, wenn verfügbar. [EMSWe: DE-005-05] [EDIFACT:LOC-3227-92] [IMO:IMO0076] . Modell: [https://schema.org/Text](https://schema.org/Text)- `latitude[number]`: Breitenkoordinate des Schiffes  - `location[*]`: Geojson-Verweis auf die Schiffposition. Es muss ein Punkt sein, an dem sich das Schiff zum Zeitpunkt der Beobachtung befand.    
- `longitude[number]`: Längenkoordinate des Schiffes  - `mmsi[number]`: Marine Mobile Service Identity Number (eine vorübergehend zugewiesene UID, die von dem Flaggenstaat des Objekts ausgegeben wird) . Modell: [https://schema.org/Number](https://schema.org/Number)- `modifiedDate[date-time]`: Datum und Uhrzeit der letzten Änderung der durch ein ISO 8601-UTC-Format dargestellten Entität. Modell: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: Der Name dieses Elements  - `navigationStatus[number]`: Enum:'0=Unterwegs mit Motor, 1=Vor Anker, 2=Nicht unter Kommando, 3=Eingeschränkte Manövrierfähigkeit, 4=Durch den Tiefgang eingeschränkt, 5=Vertäut, 6=Auf Grund gelaufen, 7=Beim Fischen beschäftigt, 8=Unterwegs segelnd, 9=Reserviert für zukünftige Änderungen des Navigationszustands für HSC, 10=Reserviert für zukünftige Änderungen des Navigationsstatus für WIG, 11=Reserviert für zukünftige Verwendung, 12=Reserviert für zukünftige Verwendung, 13=Reserviert für zukünftige Verwendung, 14=AIS-SART ist aktiv, 15=Nicht definiert (Standard)'. Navigationsstatus. AIVDM/AIVDO-Datenformat' . Modell: [https://schema.org/Number](https://schema.org/Number)- `nextPortCode[string]`: Nächster Hafen, kodiert. Der Code, der den Hafen unmittelbar vor dem Ankunftshafen darstellt, wenn verfügbar. Im Zusammenhang mit IALA_S211:nestPortCallCod / IMO. [EMSWe: DE-005-07] [EDIFACT:LOC-3227-61] [IMO:IMO0120] . Modell: [https://schema.org/Text](https://schema.org/Text)- `observedDate[date-time]`: Datum und Uhrzeit dieser Beobachtung, dargestellt in einem ISO 8601-UTC-Format. Modell: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: Eine Liste, die eine JSON-kodierte Folge von Zeichen enthält, die auf die eindeutigen IDs der Eigentümer verweisen  - `portCallNumber[string]`: Hafenanrufkennung im MRN-Format. Das erste Element des NSS sollte der 5-stellige UN/LOCODE des Hafens sein, gefolgt vom Jahr und abschließend mit einer eindeutigen laufenden Nummer in diesem Hafen [LLLLLYYYY99999], wobei LLLLL der UN/LOCODE des besuchten Hafens, YYYY das Jahr und 99999 eine eindeutige laufende Nummer ist, die von der Hafenbehörde zugewiesen wird und jedes Jahr eindeutig ist (z. B. ESHUV202310323). Eine Abkürzung kann für den UN/LOCODE verwendet werden (z. B. H202310323). Die Hafenanrufnummer wird während der ersten Schritte des Besuchs zugewiesen, kann jedoch am Anfang null sein. In internationalen Standards wird dies auch als [Hafenanruf-ID], [Besuchs-ID] oder [Hafenanrufkennung] bezeichnet. Siehe [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) [EMSWe: DG-004/DG-004-01] [EDIFACT:BGM-1004] [IALA_S211:portCallId] [IMO:IMO108+IMO0153] . Modell: [https://schema.org/Text](https://schema.org/Text)- `portCallRef[uri]`: Verweis auf die übergeordnete PortCall-Entität. [NGSI-MarineTransport.PortCall.id]  - `portCode[string]`: Vereinte Nationen-Code für Handel und Transportstandorte. Siehe [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) [EMSWe: DE-004-04] [EDIFACT:LOC-3227-153] [IALA_S211:portCode] [IMO:IMO0108] . Modell: [https://schema.org/Text](https://schema.org/Text)- `positionAccuracy[number]`: Enum:'0=Niedrig (> 10 m; autonomer Modus eines z. B. globalen Navigationssatellitensystems (GNSS)-Empfängers oder eines anderen elektronischen Positionsbestimmungsgeräts; Standard), 1=Hoch (< 10 m; differentieller Modus eines z. B. DGNSS-Empfängers)'. Code für die Genauigkeit der Schiffpositionskennung . Modell: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: Liste von URIs, die auf zusätzliche Ressourcen zu diesem Element verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `speedOverGround[number]`: Geschwindigkeit über Grund (SOG). Modell: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI-Entitätstyp. Es muss KeyVessel sein  - `vesselAtPort[boolean]`: Das Schiff befindet sich innerhalb der Hafengrenzen, einschließlich des Wartens außerhalb, am Hafeneingang, wartet auf Anweisungen usw. . Modell: [https://schema.org/Boolean](https://schema.org/Boolean)- `vesselName[string]`: Schiffname . Modell: [https://schema.org/Text](https://schema.org/Text)- `vesselRef[uri]`: Verweis auf die übergeordnete MasterVessel-Entität. [NGSI-MarineTransport.MasterVessel.id]- urn:mrn:<oid>:portcalls:mastervessel:id:9999  <!-- /30-PropertiesList -->  
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
## Beispiel-Payloads    
#### KeyVessel NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für ein KeyVessel im JSON-Format als key-values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und die Kontextdaten einer einzelnen Entität zurückgibt.  
<details><summary><strong>Beispiel ein-/ausblenden</strong></summary>    
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
#### KeyVessel NGSI-v2 normalisiertes Beispiel    
Hier ist ein Beispiel für ein KeyVessel im JSON-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und die Kontextdaten einer einzelnen Entität zurückgibt.  
<details><summary><strong>Beispiel ein-/ausblenden</strong></summary>    
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
#### KeyVessel NGSI-LD key-values Beispiel    
Hier ist ein Beispiel für ein KeyVessel im JSON-LD-Format als key-values. Dies ist kompatibel mit NGSI-LD, wenn `options=keyValues` verwendet wird und die Kontextdaten einer einzelnen Entität zurückgibt.  
<details><summary><strong>Beispiel ein-/ausblenden</strong></summary>    
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
#### KeyVessel NGSI-LD normalisiertes Beispiel    
Hier ist ein Beispiel für ein KeyVessel im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und die Kontextdaten einer einzelnen Entität zurückgibt.  
<details><summary><strong>Beispiel ein-/ausblenden</strong></summary>    
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
Siehe [FAQ 10](https://smartdatamodels.org/index.php/faqs/), um eine Antwort darauf zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
