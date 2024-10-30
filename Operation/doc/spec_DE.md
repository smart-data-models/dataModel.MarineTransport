<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: Operation  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/Operation/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Dieses Datenmodell dient der Bereitstellung von Informationen über kommerzielle Vorgänge bei einem Schiffsstopp während eines Hafenanlaufs (Entität Liegeplatz). Ein Vorgang ist definiert als die Aktivitäten im Zusammenhang mit kommerziellen Vorgängen, die während des Liegeplatzes stattfinden. Jeder Vorgang hat eine Entität, und einige Vorgänge können am selben Liegeplatz (angedockt oder verankert) durchgeführt werden und werden durch ihre zeitliche Sequenznummer (operationRank)** unterschieden.  
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
	- `streetNr[string]`: Nummer zur Identifizierung eines bestimmten Grundstücks an einer öffentlichen Straße    
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `amount[number]`: Anzahl der Einheiten beim Laden/Entladen  . Model: [https://schema.org/Number](https://schema.org/Number)- `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `berthRef[uri]`: Verweis auf die übergeordnete Entität MarineTransport:Liegeplatz  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `etc[date-time]`: Datum und Uhrzeit der geschätzten Ankunftszeit am Liegeplatz, die von der Hafenbehörde erwartet wird (ISO 8601 UTC-Format), dargestellt durch ein ISO 8601 UTC-Format. Wenn es sich um den ersten Liegeplatz handelt, sollte die ETA-Liegezeit mit der ETA-PBP identisch sein.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `ets[date-time]`:   . Model: [https://schema.org/DateTime.Represented by an ISO 8601 UTC format, Date and time of Estimated Time of starting the operation.](https://schema.org/DateTime.Represented by an ISO 8601 UTC format, Date and time of Estimated Time of starting the operation.)- `id[*]`: Eindeutiger Bezeichner der Entität  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `manipulationMeansCode[string]`: Code zur Identifizierung des Manipulationsmittels. Aufzählung: 1=Schiffseigene Mittel, 2=Roll-on-Roll-off-Rampe, 3=Dockkräne, 4=Autokräne, 5=Rohre, 6=Förderbänder, 7=Pneumatische Pumpanlagen, 8=Spezialanlagen, 9=Sonstige Mittel'  . Model: [https://schema.org/Text](https://schema.org/Text)- `manipulationMeansNumber[number]`: Anzahl der Manipulationsmittel  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxWeightPerUnit[number]`: Maximales Gewicht pro Lade-/Entladeeinheit  . Model: [https://schema.org/Number](https://schema.org/Number)- `measureUnit[string]`: Art der Belastung/Entlastung der Einheit  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: Der Name dieses Artikels  - `operationRank[number]`: Rang oder Nummer dieses Vorgangs bei allen kommerziellen Vorgängen am Liegeplatz in der Reihenfolge der Vorgänge (Löschen, Laden, ...)  . Model: [https://schema.org/Number](https://schema.org/Number)- `operationTypeCode[string]`: Code zur Identifizierung der Art des Handelsgeschäfts. Enum: 'ZD=Entladung; ZE=Einschiffung; ZT=Umschlag; ZR=Abfall; AV=Victualling; DT=Entladung im Transit; RE=Restau'  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `portCallNumber[string]`: PortCall-Bezeichner im Urnenformat. MarineTransport:PortCall:portCallNumber  . Model: [https://schema.org/Text](https://schema.org/Text)- `portCallRef[uri]`: Verweis auf die übergeordnete Entität MarineTransport:PortCall  - `portCode[string]`: Code des angelaufenen Hafens  . Model: [https://schema.org/Text](https://schema.org/Text)- `position[string]`: Text, der die Position im Hafen angibt, an der der Vorgang stattgefunden hat  . Model: [https://schema.org/Text](https://schema.org/Text)- `productCode[string]`: Code, der die Art des Produkts dieser Operation identifiziert. Aufzählung: Z01=Rohöl; Z02=Heizöl; Z03=Gasöl; Z04=Benzin; Z05=Asphalt; Z06=Andere Erdölprodukte; Z07=Erdöl-Energiegase; Z08=Eisenerz; Z09=Pyrit; Z10=Andere Mineralien; Z11=Eisenschrott; Z12=Kohlen und Petrolkoks; Z13=Stahlerzeugnisse; Z14=Phosphate; Z15=Kalke; Z16=Natürliche und künstliche Düngemittel; Z17=Chemische Erzeugnisse; Z18=Zement und Klinker; Z19=Holz und Kork; Z20=Baustoffe; Z21=Getreide und Getreidemehl; Z22=Bohnen und Sojamehl; Z23=Früchte, Gemüse und Hülsenfrüchte; Z24=Wein, alkoholische Getränke und daraus hergestellte Erzeugnisse; Z25=Speisesalz; Z26=Papier und Zellstoff; Z27=Konserven; Z28=Tabak, Kakao, Kaffee und Gewürze; Z29=Öle und Fette; Z30=Sonstige Nahrungsmittel; Z31=Maschinen, Apparate, Werkzeuge und Ersatzteile; Z32=Kraftfahrzeuge und Kraftfahrzeugteile; Z33=Tiefkühlfisch; Z34=Restliche Waren; Z35=Erdgas; Z36=Sonstige Hüttenerzeugnisse; Z37=Futtermittel und Futtermittel; Z38=Tara-LKW-Ladefläche; Z39=Containertara; Z40=Waren in Transitcontainern; Z41=Container voll; Z42=Leere Container; Z43=Fahrzeuge; Z44=Fahrzeugteile; Z91=Passagiere; Z92=Kreuzfahrtpassagiere; 1=Frischer Fisch; Z51=Biokraftstoffe; Z52=Sonstige nichtmetallische Mineralien; ZR1=Schmutziger Ballast; ZR2=Schlamm- und Absetzbecken; ZR3=Tanks für ölhaltiges Wasser; ZR4=Schmutzwasser; ZR5=Müll;  . Model: [https://schema.org/Text](https://schema.org/Text)- `remarks[string]`: Bemerkungen zur Operation  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der vollständig qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `stevedoreRef[string]`: Kennung des Stauers. Format urn:mrn:<oid>:portcalls:operation:stevedore:9999  . Model: [https://schema.org/Text](https://schema.org/Text)- `stopRank[number]`: Rang oder Nummer dieser Haltestelle in der Haltestelle (Liegeplatz oder Ankerplatz), geordnet nach Zeitfolge  . Model: [https://schema.org/Number](https://schema.org/Number)- `terminal[string]`: Terminal, an dem der Vorgang stattfindet  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI-Entitätstyp. Es muss Operation sein. In einigen internationalen Standards auch als [Ship's Stop] bekannt.  - `year[number]`: Jahr der Inbetriebnahme des Liegeplatzes  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
Operation:    
  description: 'This data model is intended to provide information about commercial operations made in a stop of a ship during a PortCall (Berth entity). An Operation is defined as the activities related to commercial operations that take in place during the berth. Each Operation has an entity and some operations can be made in the same berth (docked or anchorage), and are distinguished by its sequence number on time (operationRank)'    
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
    amount:    
      description: Number of units loading/discharge    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    berthRef:    
      description: 'Reference to parent MarineTransport:Berth entity'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
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
    etc:    
      description: 'Represented by an ISO 8601 UTC format, Date and time of Estimated Time of Arrival to Berth expected by Port Authority  (ISO 8601 UTC format). If this is the first berthing, the ETA-berth should be the same than ETA-PBP'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    ets:    
      description: ""    
      format: date-time    
      type: string    
      x-ngsi:    
        model: 'https://schema.org/DateTime.Represented by an ISO 8601 UTC format, Date and time of Estimated Time of starting the operation.'    
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
    manipulationMeansCode:    
      description: 'Code identifying the manipulation means. Enum: 1=Vessel''s own resources, 2=Roll-on-roll-off ramp, 3=Dock cranes, 4=Automotive cranes, 5=Pipes, 6=Conveyor belts, 7=Pneumatic pumping installations, 8=Special installations, 9=Other means'''    
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
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    manipulationMeansNumber:    
      description: Number of manipulation means    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maxWeightPerUnit:    
      description: Maximum Weight per unit loading/discharge    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Tm    
    measureUnit:    
      description: Unit type of load loading/discharge    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    operationRank:    
      description: 'Rank or Number of this Operation in all the commercial operations made in berth in the sequence of operations (discharge, charge, ...)'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    operationTypeCode:    
      description: 'Code identifying the type of commercial operation. Enum: ''ZD=Disembarkation; ZE=Embarkation; ZT=Transshipment; ZR=Waste; AV=Victualling; DT=Disembarkation in transit; RE=Restow'''    
      enum:    
        - AV    
        - DT    
        - RE    
        - ZD    
        - ZE    
        - ZR    
        - ZT    
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
      description: 'PortCall identifier in urn format. MarineTransport:PortCall:portCallNumber'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    portCallRef:    
      description: 'Reference to parent MarineTransport:PortCall entity'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    portCode:    
      description: Code of the port of the call    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    position:    
      description: Text specifying the position in the port where the operations has place    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    productCode:    
      description: 'Code identifying the type of product of this operation. Enum: Z01=Crude oil; Z02=Fuel oil; Z03=Gas-oil; Z04=Gasoline; Z05=Asphalt; Z06=Other petroleum products; Z07=Petroleum energy gases; Z08=Iron ore; Z09=Pyrites; Z10=Other minerals; Z11=Iron scrap; Z12=Coals and petroleum coke; Z13=Steel products; Z14=Phosphates; Z15=Potasses; Z16=Natural and artificial fertilizers; Z17=Chemical products; Z18=Cement and clinker; Z19=Wood and cork; Z20=Construction materials; Z21=Cereals and their flour; Z22=Beans and soy flour; Z23=Fruits, vegetables and legumes; Z24=Wines, alcoholic beverages and derivatives; Z25=Common salt; Z26=Paper and pulp; Z27=Canned; Z28=Tobacco, cocoa, coffee and spices; Z29=Oils and fats; Z30=Other food products; Z31=Machinery, appliances, tools and spare parts; Z32=Automobiles and parts; Z33=Frozen fish; Z34=Rest of merchandise; Z35=Natural gas; Z36=Other metallurgical products; Z37=Feed and forage; Z38=Tare truck cargo platform; Z39=Container tare; Z40=Merchandise in transit containers; Z41=Containers full; Z42=Empty containers; Z43=Vehicles; Z44=Vehicle parts; Z91=Passengers; Z92=Cruise passengers; 1=Fresh fish; Z51=Biofuels; Z52=Other non-metallic minerals; ZR1=Dirty ballast; ZR2=Sludge and settling tanks; ZR3=Bilge oily water tanks; ZR4=Dirty waters; ZR5=Garbage;'    
      enum:    
        - Z01    
        - Z02    
        - Z03    
        - Z04    
        - Z05    
        - Z06    
        - Z07    
        - Z08    
        - Z09    
        - Z10    
        - Z11    
        - Z12    
        - Z13    
        - Z14    
        - Z15    
        - Z16    
        - Z17    
        - Z18    
        - Z19    
        - Z20    
        - Z21    
        - Z22    
        - Z23    
        - Z24    
        - Z25    
        - Z26    
        - Z27    
        - Z28    
        - Z29    
        - Z30    
        - Z31    
        - Z32    
        - Z33    
        - Z34    
        - Z35    
        - Z36    
        - Z37    
        - Z38    
        - Z39    
        - Z40    
        - Z41    
        - Z42    
        - Z43    
        - Z44    
        - Z91    
        - Z92    
        - Z51    
        - Z52    
        - ZR1    
        - ZR2    
        - ZR3    
        - ZR4    
        - ZR5    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    remarks:    
      description: Remarks of the operation    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    stevedoreRef:    
      description: 'Id of the stevedore. Format urn:mrn:<oid>:portcalls:operation:stevedore:9999'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    stopRank:    
      description: Rank or Number of this stop in the stop (berth or anchor area) ordered by time sequence    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    terminal:    
      description: Terminal where the operation takes place    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be Operation. In some international standards is also known as [Ship''s Stop]'    
      enum:    
        - Operation    
      type: string    
      x-ngsi:    
        type: Property    
    year:    
      description: Year of the init of the berthing    
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
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/Operation/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/Berth/schema.json    
  x-model-tags: ESHUV    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### Betrieb NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für eine Operation im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:activity:id:40923",  
  "type": "Operation",  
  "portCode": "ESHUV",  
  "year": 2023,  
  "portCallNumber": "ESHUV202300123",  
  "portCallRef": "urn:mrn:eshuv:portcalls:activity:id:941",  
  "berthRef": "urn:mrn:eshuv:portcalls:berth:id:1234",  
  "stopRank": 2,  
  "operationRank": 1,  
  "ets": "2023-01-01T07:30:00",  
  "etc": "2023-01-01T07:30:00",  
  "operationTypeCode": "ZE",  
  "productCode": "Z41",  
  "amount": 120,  
  "measureUnit": "TEU",  
  "maxWeightPerUnit": 23.3,  
  "terminal": "Muelle Sur",  
  "position": "Segunda linea granel",  
  "remarks": "Delayed 1h",  
  "manipulationMeansCode": "3",  
  "manipulationMeansNumber": 2,  
  "stevedoreRef": "1234"  
}  
```  
</details>  
#### Betrieb NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine Operation im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:activity:id:40923",  
  "type": "Operation",  
  "portCode": {  
    "type": "Text",  
    "value": "ESHUV"  
  },  
  "year": {  
    "type": "Number",  
    "value": 2023  
  },  
  "portCallNumber": {  
    "type": "Text",  
    "value": "ESHUV202300123"  
  },  
  "portCallRef": {  
    "type": "Text",  
    "value": "urn:mrn:eshuv:portcalls:activity:id:941"  
  },  
  "berthRef": {  
    "type": "Text",  
    "value": "urn:mrn:eshuv:portcalls:berth:id:1234"  
  },  
  "stopRank": {  
    "type": "Number",  
    "value": 2  
  },  
  "operationRank": {  
    "type": "Number",  
    "value": 1  
  },  
  "ets": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:30:00"  
  },  
  "etc": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:30:00"  
  },  
  "operationTypeCode": {  
    "type": "Text",  
    "value": "ZE"  
  },  
  "productCode": {  
    "type": "Text",  
    "value": "Z41"  
  },  
  "amount": {  
    "type": "Number",  
    "value": 120  
  },  
  "measureUnit": {  
    "type": "Text",  
    "value": "TEU"  
  },  
  "maxWeightPerUnit": {  
    "type": "Number",  
    "value": 23.3  
  },  
  "terminal": {  
    "type": "Text",  
    "value": "Muelle Sur"  
  },  
  "position": {  
    "type": "Text",  
    "value": "Segunda linea granel"  
  },  
  "remarks": {  
    "type": "Text",  
    "value": "Delayed 1h"  
  },  
  "manipulationMeansCode": {  
    "type": "Text",  
    "value": "3"  
  },  
  "manipulationMeansNumber": {  
    "type": "Number",  
    "value": 2  
  },  
  "stevedoreRef": {  
    "type": "Text",  
    "value": "1234"  
  }  
}  
```  
</details>  
#### Betrieb NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für eine Operation im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:activity:id:40923",  
  "type": "Operation",  
  "portCode": "ESHUV",  
  "year": 2023,  
  "portCallNumber": "ESHUV202300123",  
  "portCallRef": "urn:mrn:eshuv:portcalls:activity:id:941",  
  "berthRef": "urn:mrn:eshuv:portcalls:berth:id:1234",  
  "stopRank": 2,  
  "operationRank": 1,  
  "ets": "2023-01-01T07:30:00",  
  "etc": "2023-01-01T07:30:00",  
  "operationTypeCode": "ZE",  
  "productCode": "Z41",  
  "amount": 120,  
  "measureUnit": "TEU",  
  "maxWeightPerUnit": 23.3,  
  "terminal": "Muelle Sur",  
  "position": "Segunda linea granel",  
  "remarks": "Delayed 1h",  
  "manipulationMeansCode": "3",  
  "manipulationMeansNumber": 2,  
  "stevedoreRef": "1234",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Betrieb NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine Operation im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:activity:id:40923",  
  "type": "Operation",  
  "portCode": {  
    "type": "Property",  
    "value": "ESHUV"  
  },  
  "year": {  
    "type": "Property",  
    "value": 2023  
  },  
  "portCallNumber": {  
    "type": "Property",  
    "value": "ESHUV202300123"  
  },  
  "portCallRef": {  
    "type": "Relationship",  
    "object": "urn:mrn:eshuv:portcalls:activity:id:941"  
  },  
  "berthRef": {  
    "type": "Relationship",  
    "object": "urn:mrn:eshuv:portcalls:berth:id:1234"  
  },  
  "stopRank": {  
    "type": "Property",  
    "value": 2  
  },  
  "operationRank": {  
    "type": "Property",  
    "value": 1  
  },  
  "ets": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:30:00"  
    }  
  },  
  "etc": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:30:00"  
    }  
  },  
  "operationTypeCode": {  
    "type": "Property",  
    "value": "ZE"  
  },  
  "productCode": {  
    "type": "Property",  
    "value": "Z41"  
  },  
  "amount": {  
    "type": "Property",  
    "value": 120  
  },  
  "measureUnit": {  
    "type": "Property",  
    "value": "TEU"  
  },  
  "maxWeightPerUnit": {  
    "type": "Property",  
    "value": 23.3  
  },  
  "terminal": {  
    "type": "Property",  
    "value": "Muelle Sur"  
  },  
  "position": {  
    "type": "Property",  
    "value": "Segunda linea granel"  
  },  
  "remarks": {  
    "type": "Property",  
    "value": "Delayed 1h"  
  },  
  "manipulationMeansCode": {  
    "type": "Property",  
    "value": "3"  
  },  
  "manipulationMeansNumber": {  
    "type": "Property",  
    "value": 2  
  },  
  "stevedoreRef": {  
    "type": "Property",  
    "value": "1234"  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
