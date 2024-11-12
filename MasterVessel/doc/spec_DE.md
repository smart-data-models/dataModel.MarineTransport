<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: MasterVessel  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/MasterVessel/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Das Datenmodell dient dazu, Informationen über Schiffe bereitzustellen. Es ermöglicht die Darstellung der Eigenschaften der einzelnen Schiffe: statische und dynamische Informationen**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, liegt das daran, dass es mehrere Typen oder unterschiedliche Formate/Muster haben kann</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Lande liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.    
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Nummer zur Identifizierung eines bestimmten Grundstücks an einer öffentlichen Straße    
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `beam[number]`: Breite des Schiffes  . Model: [https://schema.org/Number](https://schema.org/Number)- `buildDate[date]`: Baudatum des Schiffes, dargestellt im Format ISO 8601 UTC  . Model: [https://schema.org/Text](https://schema.org/Text)- `callSign[string]`: Identifizierungssignal eines Schiffes bei der Erstverbindung über Funk [EMSWe: DE-065-05] [EDI: BGM-RFF] [S211: Rufname / Rufzeichen] [IMO: IMO0136]  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `dwt[number]`: Eigengewicht Tonnage (DWT)  . Model: [https://schema.org/Number](https://schema.org/Number)- `financialOwner[string]`: Finanzieller Eigner des Schiffes  . Model: [https://schema.org/Text](https://schema.org/Text)- `flagCode[string]`: Internationaler Flaggencode (ISO 3166-1 alfa-2)  . Model: [https://schema.org/Text](https://schema.org/Text)- `gt[number]`: Bruttoraumzahl (BRZ)  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Eindeutiger Bezeichner der Entität  - `imo[number]`: Nummer der Internationalen Seeschifffahrtsorganisation (eine globale UID für immer) [EMSWe: DE-003-03] [EDIFACT:TDT-8213] [IALA_S211:vesselId] [IMO:IMO0140]  . Model: [https://schema.org/Number](https://schema.org/Number)- `loa[number]`: Länge über das gesamte Schiff  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `manager[string]`: Manager des Schiffes, normalerweise Schiffsgesellschaft  . Model: [https://schema.org/Text](https://schema.org/Text)- `maxDraught[number]`: Maximaler Tiefgang des Schiffes  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxLoadVehicle[number]`: Maximale Kapazität des Schiffes für den Transport von Fahrzeugen  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxPassenger[number]`: Maximale Kapazität des Schiffes für die Beförderung von Passagieren  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVehicle[number]`: Maximal zulässige Abmessungen des Fahrzeugs  . Model: [https://schema.org/Number](https://schema.org/Number)- `minNumOfCrew[number]`: Mindestanzahl der Besatzung für den Betrieb des Schiffes  . Model: [https://schema.org/Number](https://schema.org/Number)- `mmsi[number]`: Marine Mobile Service Identity Number (eine vorübergehend zugewiesene UID, die vom aktuellen Flaggenstaat des Objekts vergeben wird)[EMSWe: DE-068-09] [EDIFACT:TDT-1131] [IALA_S211:vesselId] [IMO:IMO0178]  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `photo[uri]`: Foto-URL des Schiffes  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `sleeve[number]`: Hülse des Schiffes  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der vollständig qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `technicalManager[string]`: Technischer Leiter des Schiffes  . Model: [https://schema.org/Text](https://schema.org/Text)- `toBow[number]`: Dimension zum Bogen  . Model: [http://schema.org/Number](http://schema.org/Number)- `toPort[number]`: Dimension zum Hafen  . Model: [http://schema.org/Number](http://schema.org/Number)- `toStardboard[number]`: Abmessung nach Steuerbord  . Model: [http://schema.org/Number](http://schema.org/Number)- `toStern[number]`: Dimension zum Heck  . Model: [http://schema.org/Number](http://schema.org/Number)- `type[string]`: NGSI-Entitätstyp. Es muss MasterVessel sein  - `vesselClass[string]`: Code für die Schiffsklasse. Enum:'BD=Trockenmassengut; BO=Öltankschiff/Massengutfrachter; BS=Massengutfrachter Entladung; BY=Andere Arten von Massengutfrachtern; FC=Fischereifahrzeug; FO=Schiffsumschlag und/oder Transport; GA=Schiff. RO-RO mit Passagieren; GC=Mrcia allgemein ohne Spezialisierung; GD=Übrige Stückgutschiffe; GE=Buq. transp. kombiniert; GN=Containerschiff; GO=Ro-Ro-Schiff; GP=Passagierschiff; GR=Kühlschiff; OO=Buq. oder Artefakt. schwimmen; OS=Versorgungsschiffe; TC=Transport produkt. Chemikalien; TD=Sonstiges flüssiges Massengut; TL=Transport von Flüssiggas; TO=Öltanker; XD=Bagger; XR=Forschung und Exploration; XT=Schlepper; XX=Sonstige Schiffe und Boote; UR=Schnellpassage; G=Stückgut; T=Flüssigmassengutfrachter (Tanks); S=Festmassengutfrachter; OB=Sonstige Handelsschiffe; UC=Kreuzfahrtschein; OC=Hochseefischereischiffe (Gefrierschiffe);'  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselName[string]`: Name des Schiffes. [EMSWe: DE-003-07] [EDIFACT:TDT-8212] [IMO:IMO0142]  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselOwner[string]`: Eigner des Schiffes  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselSubType[number]`: Enum:0=Nicht verfügbar (Standard),1-19=Reserviert für zukünftige Verwendung,20=Bodenfahrwerk (WIG), alle Schiffe dieses Typs,21=Bodenfahrwerk (WIG), Gefahrenklasse A,22=Bodenfahrwerk (WIG), Gefahrenkategorie B,23=Schiffsflügel in Grund und Boden (WIG), Gefahrenkategorie C,24=Schiffsflügel in Grund und Boden (WIG), Gefahrenkategorie D,25-29=Schiffsflügel in Grund und Boden (WIG), Reserviert für zukünftige Verwendung,30=Fischen,31=Schleppen,32=Schleppen: Länge mehr als 200 m oder Breite mehr als 25 m,33=Baggerarbeiten oder Unterwassereinsätze,34=Taucheinsätze,35=Militärische Einsätze,36=Segeln,37=Sportfahrzeuge,38-39=Reserviert,40=Hochgeschwindigkeitsfahrzeuge (HSC), alle Schiffe dieses Typs,41=Hochgeschwindigkeitsfahrzeuge (HSC), Gefahrenkategorie A,42=Hochgeschwindigkeitsfahrzeuge (HSC), Gefahrenkategorie B,43=Hochgeschwindigkeitsfahrzeuge (HSC), Gefahrenkategorie C,44=Hochgeschwindigkeitsfahrzeuge (HSC), Gefahrenkategorie D,45-48=Hochgeschwindigkeitsfahrzeuge (HSC), reserviert für künftige Verwendung,49=Hochgeschwindigkeitsfahrzeuge (HSC), keine zusätzlichen Angaben,50=Lotsenschiff,51=Such- und Rettungsschiff,52=Schlepper,53=Hafentender,54=Anti-Verschmutzungsausrüstung,55=Gesetzesvollzug,56-57=Ersatz - Lokales Schiff,58=Medizinischer Transport,59=Nichtkämpferschiff gemäß RR Resolution Nr. 18,60=Passagier, alle Schiffe dieses Typs,61=Passagier, Gefahrenkategorie A,62=Passagier, Gefahrenkategorie B,63=Passagier, Gefahrenkategorie C,64=Passagier, Gefahrenkategorie D,65-68=Passagier, reserviert für künftige Verwendung,69=Passagier, keine zusätzlichen Angaben,70=Ladung, alle Schiffe dieses Typs,71=Ladung, Gefahrenkategorie A,72=Ladung, Gefahrenkategorie B,73=Ladung, Gefahrenkategorie C,74=Ladung, Gefahrenkategorie D,75-78=Ladung, für künftige Verwendung reserviert,79=Ladung, keine weiteren Angaben,80=Tanker, alle Schiffe dieses Typs,81=Tankschiff, Gefahrenkategorie A,82=Tankschiff, Gefahrenkategorie B,83=Tankschiff, Gefahrenkategorie C,84=Tankschiff, Gefahrenkategorie D,85-88=Tankschiff, für künftige Verwendung reserviert,89=Tankschiff, keine zusätzlichen Angaben,90=Anderer Typ, alle Schiffe dieses Typs,91=Sonstiger Typ, Gefahrenkategorie A,92=Sonstiger Typ, Gefahrenkategorie B,93=Sonstiger Typ, Gefahrenkategorie C,94=Sonstiger Typ, Gefahrenkategorie D,95-98=Sonstiger Typ, für künftige Verwendung reserviert,99=Sonstiger Typ, keine weiteren Angaben". Code für den Untertyp des Schiffes  . Model: [https://schema.org/Number](https://schema.org/Number)- `vesselType[number]`: Enum:'1=Reserviert,2=Flügel am Boden,3=Sonderkategorie,4=Hochgeschwindigkeitsfahrzeug,5=Sonderkategorie,6=Passagier,7=Fracht,8=Tanker,9=Sonstiges'. Code für den Schiffstyp  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
MasterVessel:    
  description: 'The data model is intended to provide information about vessels. It allows to represent the properties of each vessel: static and dynamic information'    
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
    beam:    
      description: Beam of the Vessel    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meters    
    buildDate:    
      description: Date of building of the vessel represented by an ISO 8601 UTC format    
      format: date    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    callSign:    
      description: 'Identification signal of a vessel when initially connecting by radio [EMSWe: DE-065-05] [EDI: BGM-RFF] [S211: Call Name / Call Sign] [IMO: IMO0136] '    
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
    dwt:    
      description: Dead weight Tonnage (DWT)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: tons    
    financialOwner:    
      description: Financial Owner of the vessel    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    flagCode:    
      description: International Flag Code (ISO 3166-1 alfa-2)    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    gt:    
      description: Gross Tonnage (GT)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: moorson tons    
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
      description: 'International Maritime Organization Number (a global forever UID) [EMSWe: DE-003-03] [EDIFACT:TDT-8213] [IALA_S211:vesselId] [IMO:IMO0140] '    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    loa:    
      description: Length Over All of Vessel    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meters    
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
    manager:    
      description: 'Manager of the Vessel, usually Ship Company'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    maxDraught:    
      description: Maximum Draught of the vessel    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meters    
    maxLoadVehicle:    
      description: Max capacity of vessel to transport vehicles    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maxPassenger:    
      description: Max capacity of vessel to transport passengers    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maxVehicle:    
      description: Max dimensions of vehicle permitted    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    minNumOfCrew:    
      description: Minimum number of crew to operate the vessel    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    mmsi:    
      description: 'Marine Mobile Service Identity Number (a temporarily assigned UID, issued by that object''s current flag state)[EMSWe: DE-068-09] [EDIFACT:TDT-1131] [IALA_S211:vesselId] [IMO:IMO0178]'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    photo:    
      description: Vessel Photo URL    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    sleeve:    
      description: Sleeve of Vessel    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meters    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    technicalManager:    
      description: Technical Manager of the vessel    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    toBow:    
      description: Dimension to Bow    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: meters    
    toPort:    
      description: Dimension to Port    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: meters    
    toStardboard:    
      description: Dimension to Starboard    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: meters    
    toStern:    
      description: Dimension to Stern    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: meters    
    type:    
      description: NGSI Entity type. It has to be MasterVessel    
      enum:    
        - MasterVessel    
      type: string    
      x-ngsi:    
        type: Property    
    vesselClass:    
      description: 'Code for vessel class. Enum:''BD=Dry bulk; BO=Oil tanker / bulk carrier; BS=Bulk carrier unloading; BY=Other types of bulk carriers; FC=Fishing vessel; FO=Vessel. transfer and/or transp.; GA=Vessel. RO-RO with passengers; GC=Mrcia general without specialization; GD=Rest general cargo vessels; GE=Buq. transp. combined; GN=Container ship; GO=Ro-ro vessel; GP=Passenger ship; GR=Refrigerator vessel; OO=Buq. or artefact. float be; OS=Supply ships; TC=Transport product. chemicals; TD=Other liquid bulk; TL=Transportation of liquefied gas; TO=Oil tanker; XD=Dredges; XR=Research and exploration; XT=Tugs / pushers; XX=Other ships and boats; UR=Fast Pass; G=General Cargo; T=Liquid Bulk Carriers (Tanks); S=Solid Bulk Carriers; OB=Other Merchant Vessels; UC=Cruise Ticket; OC=High Sea Fishing Vessels (Freezers);'''    
      enum:    
        - BD    
        - BO    
        - BS    
        - BY    
        - FC    
        - FO    
        - GA    
        - GC    
        - GD    
        - GE    
        - GN    
        - GO    
        - GP    
        - GR    
        - OO    
        - OS    
        - TC    
        - TD    
        - TL    
        - TO    
        - XD    
        - XR    
        - XT    
        - XX    
        - UR    
        - G    
        - T    
        - S    
        - OB    
        - UC    
        - OC    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vesselName:    
      description: 'Name of the Vessel. [EMSWe: DE-003-07] [EDIFACT:TDT-8212] [IMO:IMO0142]'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vesselOwner:    
      description: Owner of the Vessel    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vesselSubType:    
      description: 'Enum:''0=Not available (default),1-19=Reserved for future use,20=Wing in ground (WIG), all ships of this type,21=Wing in ground (WIG), Hazardous category A,22=Wing in ground (WIG), Hazardous category B,23=Wing in ground (WIG), Hazardous category C,24=Wing in ground (WIG), Hazardous category D,25-29=Wing in ground (WIG), Reserved for future use,30=Fishing,31=Towing,32=Towing: length exceeds 200m or breadth exceeds 25m,33=Dredging or underwater ops,34=Diving ops,35=Military ops,36=Sailing,37=Pleasure Craft,38-39=Reserved,40=High speed craft (HSC), all ships of this type,41=High speed craft (HSC), Hazardous category A,42=High speed craft (HSC), Hazardous category B,43=High speed craft (HSC), Hazardous category C,44=High speed craft (HSC), Hazardous category D,45-48=High speed craft (HSC), Reserved for future use,49=High speed craft (HSC), No additional information,50=Pilot Vessel,51=Search and Rescue vessel,52=Tug,53=Port Tender,54=Anti-pollution equipment,55=Law Enforcement,56-57=Spare - Local Vessel,58=Medical Transport,59=Noncombatant ship according to RR Resolution No. 18,60=Passenger, all ships of this type,61=Passenger, Hazardous category A,62=Passenger, Hazardous category B,63=Passenger, Hazardous category C,64=Passenger, Hazardous category D,65-68=Passenger, Reserved for future use,69=Passenger, No additional information,70=Cargo, all ships of this type,71=Cargo, Hazardous category A,72=Cargo, Hazardous category B,73=Cargo, Hazardous category C,74=Cargo, Hazardous category D,75-78=Cargo, Reserved for future use,79=Cargo, No additional information,80=Tanker, all ships of this type,81=Tanker, Hazardous category A,82=Tanker, Hazardous category B,83=Tanker, Hazardous category C,84=Tanker, Hazardous category D,85-88=Tanker, Reserved for future use,89=Tanker, No additional information,90=Other Type, all ships of this type,91=Other Type, Hazardous category A,92=Other Type, Hazardous category B,93=Other Type, Hazardous category C,94=Other Type, Hazardous category D,95-98=Other Type, Reserved for future use,99=Other Type, no additional information''. Code for vessel Sub-Type'    
      enum:    
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
        - 16    
        - 17    
        - 18    
        - 19    
        - 20    
        - 21    
        - 22    
        - 23    
        - 24    
        - 25    
        - 26    
        - 27    
        - 28    
        - 29    
        - 30    
        - 31    
        - 32    
        - 33    
        - 34    
        - 35    
        - 36    
        - 37    
        - 38    
        - 39    
        - 40    
        - 41    
        - 42    
        - 43    
        - 44    
        - 45    
        - 46    
        - 47    
        - 48    
        - 49    
        - 50    
        - 51    
        - 52    
        - 53    
        - 54    
        - 55    
        - 56    
        - 57    
        - 58    
        - 59    
        - 60    
        - 61    
        - 62    
        - 63    
        - 64    
        - 65    
        - 66    
        - 67    
        - 68    
        - 69    
        - 70    
        - 71    
        - 72    
        - 73    
        - 74    
        - 75    
        - 76    
        - 77    
        - 78    
        - 79    
        - 80    
        - 81    
        - 82    
        - 83    
        - 84    
        - 85    
        - 86    
        - 87    
        - 88    
        - 89    
        - 90    
        - 91    
        - 92    
        - 93    
        - 94    
        - 95    
        - 96    
        - 97    
        - 98    
        - 99    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vesselType:    
      description: 'Enum:''1=Reserved,2=Wing In Ground,3=Special Category,4=High-Speed Craft,5=Special Category,6=Passenger,7=Cargo,8=Tanker,9=Other''. Code for vessel type'    
      enum:    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
        - 6    
        - 7    
        - 8    
        - 9    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2024 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/MasterVessel/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/MasterVessel/schema.json    
  x-model-tags: ESHUV    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### MasterVessel NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für ein MasterVessel im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:mastervessel:id:1234",  
  "type": "MasterVessel",  
  "vesselName": "ELEANOR R.",  
  "imo": 9863637,  
  "mmsi": 210049000,  
  "callSign": "5BPC3",  
  "flagCode": "CY",  
  "vesselType": 1,  
  "vesselSubType": 2,  
  "vesselClass": "BO",  
  "gt": 12467,  
  "beam": 7,  
  "loa": 132.22,  
  "sleeve": 25.51,  
  "maxDraught": 5.61,  
  "dwt": 8.10,  
  "buildDate": "2023-06-01",  
  "toBow": 3,  
  "toStern": 20,  
  "toPort": 17,  
  "toStardboard": 4,  
  "photo": "https://acme.com/photos/9863637",  
  "owner": [  
    "urn:ngsi-ld:Acme-OWNER-NAME"  
  ],  
  "vesselOwner": "Acme OWNER NAME",  
  "manager": "Acme MANAGER NAME",  
  "financialOwner": "Acme FINANCIAL ",  
  "technicalManager": "Acme TECHNICAL MANAGER",  
  "dataProvider": "AIS",  
  "maxLoadVehicle": 120,  
  "maxPassenger": 0,  
  "maxVehicle": 16,  
  "minNumOfCrew": 12  
}  
```  
</details>  
#### MasterVessel NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein MasterVessel im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:mastervessel:id:1234",  
  "type": "MasterVessel",  
  "vesselName": {  
    "type": "Text",  
    "value": "ELEANOR R."  
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
    "value": "CY"  
  },  
  "vesselType": {  
    "type": "Boolean",  
    "value": true  
  },  
  "vesselSubType": {  
    "type": "Number",  
    "value": 2  
  },  
  "vesselClass": {  
    "type": "Text",  
    "value": "BO"  
  },  
  "gt": {  
    "type": "Number",  
    "value": 12467  
  },  
  "beam": {  
    "type": "Number",  
    "value": 7  
  },  
  "loa": {  
    "type": "Number",  
    "value": 132.22  
  },  
  "sleeve": {  
    "type": "Number",  
    "value": 25.51  
  },  
  "maxDraught": {  
    "type": "Number",  
    "value": 5.61  
  },  
  "dwt": {  
    "type": "Number",  
    "value": 8.1  
  },  
  "buildDate": {  
    "type": "Date-Time",  
    "value": "2023-06-01"  
  },  
  "toBow": {  
    "type": "Number",  
    "value": 3  
  },  
  "toStern": {  
    "type": "Number",  
    "value": 20  
  },  
  "toPort": {  
    "type": "Number",  
    "value": 17  
  },  
  "toStardboard": {  
    "type": "Number",  
    "value": 4  
  },  
  "photo": {  
    "type": "Text",  
    "value": "https://acme.com/photos/9863637"  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:Acme-OWNER-NAME"  
    ]  
  },  
  "vesselOwner": {  
    "type": "Text",  
    "value": "Acme OWNER NAME"  
  },  
  "manager": {  
    "type": "Text",  
    "value": "Acme MANAGER NAME"  
  },  
  "financialOwner": {  
    "type": "Text",  
    "value": "Acme FINANCIAL "  
  },  
  "technicalManager": {  
    "type": "Text",  
    "value": "Acme TECHNICAL MANAGER"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "AIS"  
  },  
  "maxLoadVehicle": {  
    "type": "Number",  
    "value": 120  
  },  
  "maxPassenger": {  
    "type": "Boolean",  
    "value": false  
  },  
  "maxVehicle": {  
    "type": "Number",  
    "value": 16  
  },  
  "minNumOfCrew": {  
    "type": "Number",  
    "value": 12  
  }  
}  
```  
</details>  
#### MasterVessel NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für ein MasterVessel im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:mastervessel:id:1234",  
  "type": "MasterVessel",  
  "vesselName": "ELEANOR R.",  
  "imo": 9863637,  
  "mmsi": 210049000,  
  "callSign": "5BPC3",  
  "flagCode": "CY",  
  "vesselType": 1,  
  "vesselSubType": 2,  
  "vesselClass": "BO",  
  "gt": 12467,  
  "beam": 7,  
  "loa": 132.22,  
  "sleeve": 25.51,  
  "maxDraught": 5.61,  
  "dwt": 8.10,  
  "buildDate": "2023-06-01",  
  "toBow": 3,  
  "toStern": 20,  
  "toPort": 17,  
  "toStardboard": 4,  
  "photo": "https://acme.com/photos/9863637",  
  "owner": [  
    "urn:ngsi-ld:Acme-OWNER-NAME"  
  ],  
  "vesselOwner": "Acme OWNER NAME",  
  "manager": "Acme MANAGER NAME",  
  "financialOwner": "Acme FINANCIAL ",  
  "technicalManager": "Acme TECHNICAL MANAGER",  
  "dataProvider": "AIS",  
  "maxLoadVehicle": 120,  
  "maxPassenger": 0,  
  "maxVehicle": 16,  
  "minNumOfCrew": 12,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/refs/heads/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### MasterVessel NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein MasterVessel im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:mastervessel:id:1234",  
  "type": "MasterVessel",  
  "vesselName": {  
    "type": "Property",  
    "value": "ELEANOR R."  
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
    "value": "CY"  
  },  
  "vesselType": {  
    "type": "Property",  
    "value": true  
  },  
  "vesselSubType": {  
    "type": "Property",  
    "value": 2  
  },  
  "vesselClass": {  
    "type": "Property",  
    "value": "BO"  
  },  
  "gt": {  
    "type": "Property",  
    "value": 12467  
  },  
  "beam": {  
    "type": "Property",  
    "value": 7  
  },  
  "loa": {  
    "type": "Property",  
    "value": 132.22  
  },  
  "sleeve": {  
    "type": "Property",  
    "value": 25.51  
  },  
  "maxDraught": {  
    "type": "Property",  
    "value": 5.61  
  },  
  "dwt": {  
    "type": "Property",  
    "value": 8.1  
  },  
  "buildDate": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "value": "2023-06-01"  
    }  
  },  
  "toBow": {  
    "type": "Property",  
    "value": 3  
  },  
  "toStern": {  
    "type": "Property",  
    "value": 20  
  },  
  "toPort": {  
    "type": "Property",  
    "value": 17  
  },  
  "toStardboard": {  
    "type": "Property",  
    "value": 4  
  },  
  "photo": {  
    "type": "Property",  
    "value": "https://acme.com/photos/9863637"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Acme-OWNER-NAME"  
    ]  
  },  
  "vesselOwner": {  
    "type": "Property",  
    "value": "Acme OWNER NAME"  
  },  
  "manager": {  
    "type": "Property",  
    "value": "Acme MANAGER NAME"  
  },  
  "financialOwner": {  
    "type": "Property",  
    "value": "Acme FINANCIAL "  
  },  
  "technicalManager": {  
    "type": "Property",  
    "value": "Acme TECHNICAL MANAGER"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "AIS"  
  },  
  "maxLoadVehicle": {  
    "type": "Property",  
    "value": 120  
  },  
  "maxPassenger": {  
    "type": "Property",  
    "value": false  
  },  
  "maxVehicle": {  
    "type": "Property",  
    "value": 16  
  },  
  "minNumOfCrew": {  
    "type": "Property",  
    "value": 12  
  }  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
Es steht noch aus, die Standardidentifikation für jedes Feld zu vereinbaren. Für die Bildung von URNs werden die folgenden Normen berücksichtigt - SO 3166-1 - Internationaler Standard für Ländercodes und Codes für deren Unterteilungen. - RFC 2141 - URN Syntax (https://www.ietf.org/rfc/rfc2141.txt) - RFC 8141 - Uniform Resource Names (URN) (https://tools.ietf.org/html/rfc8141) - IALAs MRN Request (https://www.iana.org/assignments/urn-formal/mrn)  
<MRN> ::= "urn" ":" "mrn" ":" <OID> ":" <OSNID> ":" <OSNS> <OID> ::= (alphanum) 0*32(alphanum / "-") (alphanum) ; Organisations-ID (d.h. ESHUV) <OSNID> ::= (alphanum) 0*32(alphanum / "-") (alphanum) ; Organisationsspezifische Namensraum-ID (z.B. Portcalls) <OSNS> ::= pchar *(pchar / "/") ; Organisationsspezifischer Namensraum-String (z.B. ein Name eines Moduls oder Microservices. <ID> ::= ein eindeutiger Bezeichner für diesen Namensraum (d. h. ein Entitätsname, gefolgt von einer Zeilen-ID in einer SQL-Datenbank)  
d.h. urn := "urn:mrn:eshuv:portcalls:portcall:id:343"  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
