<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: TrackedManeuver  
=======================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/TrackedManeuver/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Entità TrackedManoeuvre proveniente da Tracked (Sistema di tracciamento operativo). Manovra tracciata. L'entityId segue il pattern mrn:urn:eshuv:pdph:Tracked:type:attr:value, dove type=Manoeuvre e attr=manoeuvreCode**  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o formati/pattern diversi</sub></sup>  
- `address[object]`: L'indirizzo di posta  . Modello: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, Spagna  . Modello: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La località in cui si trova l'indirizzo di strada, e che si trova nella regione  . Modello: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Modello: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestito dal governo locale    
	- `postOfficeBoxNumber[string]`: Il numero della casella postale per gli indirizzi di posta  . Modello: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Modello: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'indirizzo di strada  . Modello: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numero che identifica una proprietà specifica in una strada pubblica    
- `alternateName[string]`: Un nome alternativo per questo elemento  - `amendedOnMooringLocation[string]`: Posizione della manovra "fatto veloce accanto / modificato sull'ancoraggio"  - `anchoringAnchorUpDate[date-time]`: Ora di sollevamento dell'ancora (ancora su) per la manovra di ancoraggio  - `anchoringDate[date-time]`: Ora di discesa dell'ancora per la manovra di ancoraggio  - `anchoringLocation[*]`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `anchoringZone[string]`: Zona di ancoraggio per la manovra di ancoraggio  - `areaServed[string]`: L'area geografica in cui un servizio o un elemento offerto è fornito  . Modello: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dei dati dell'entità armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Questo sarà solitamente assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Questo sarà solitamente assegnato dalla piattaforma di archiviazione  - `description[string]`: Una descrizione di questo elemento  - `durationHours[number]`: Durata della manovra in ore  - `endDate[date-time]`: Data di fine della manovra  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `maneuverCode[string]`: Codice della manovra  - `maneuverType[string]`: Tipo di manovra  - `mooringCablesNumber[number]`: Numero di linee per la manovra di ormeggio  - `mooringChangeCablesNumber[number]`: Numero di linee per la manovra di spostamento  - `mooringChangeFirstLandCableDate[date-time]`: Ora della prima linea per la manovra di spostamento  - `mooringChangeInitialLocation[string]`: Posizione iniziale della manovra di spostamento  - `mooringChangeLastCableDate[date-time]`: Ora dell'ultima linea per la manovra di spostamento  - `mooringChangeLastLocation[string]`: Posizione finale della manovra di spostamento  - `mooringChangeNoraysFrom[number]`: Numero di bitta da (manovra di spostamento)  - `mooringChangeNoraysTo[number]`: Numero di bitta a (manovra di spostamento)  - `mooringChangeSide[string]`: Lato di ormeggio per la manovra di spostamento  - `mooringFirstCableDate[date-time]`: Ora della prima linea per la manovra di ormeggio  - `mooringLocation[string]`: Posizione della manovra di ormeggio  - `mooringNoraysFrom[number]`: Numero di bitta da (manovra di ormeggio)  - `mooringNoraysTo[number]`: Numero di bitta a (manovra di ormeggio)  - `mooringSide[string]`: Lato di ormeggio per la manovra di ormeggio  - `name[string]`: Il nome di questo elemento  - `observations[string]`: Osservazioni sulla manovra  - `observedDate[date-time]`: Data dell'ultima modifica dell'entità  - `othersLocation[*]`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `othersType[string]`: Tipo di altra manovra  - `othersZone[string]`: Zona/posizione dell'altra manovra  - `owner[array]`: Una lista che contiene una sequenza di caratteri codificata in JSON che fa riferimento agli ID univoci dei proprietari  - `pilotageDisembarkDate[date-time]`: Ora di sbarco del pilota per la manovra di pilotaggio  - `pilotageDisembarkLocation[string]`: Posizione di sbarco del pilota per la manovra di pilotaggio  - `pilotageEmbarkDate[date-time]`: Ora di imbarco del pilota per la manovra di pilotaggio  - `pilotageEmbarkLocation[string]`: Posizione di imbarco del pilota per la manovra di pilotaggio  - `pilotageExempt[string]`: Esonero dal pilotaggio  - `pilotageObservations[string]`: Osservazioni sulla manovra di pilotaggio  - `pilotagePilots[string]`: Piloti coinvolti nella manovra di pilotaggio  - `portCallCode[string]`: Registro STM della chiamata al porto  - `refPortCallId[string]`: Riferimento alla chiamata al porto  - `refTugServiceId[string]`: Riferimento al servizio di rimorchio  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che fornisce la fonte originale dei dati dell'entità come URL. Consigliato essere il nome di dominio completamente qualificato del fornitore di origine o l'URL dell'oggetto di origine  - `startDate[date-time]`: Data di inizio della manovra  - `tugboatsNumber[number]`: Numero di rimorchiatori per la manovra di servizio di rimorchio  - `tugboatsObservations[string]`: Osservazioni sulla manovra di servizio di rimorchio  - `type[string]`: Tipo di entità NGSI. Deve essere TrackedManoeuvre  - `undockingLastCableDate[date-time]`: Ora dell'ultima linea per la manovra di sdoganamento (sbarco)  - `undockingLocation[string]`: Posizione della manovra di sdoganamento (sbarco)  <!-- /30-PropertiesList -->  
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
TrackedManeuver:    
  description: TrackedManoeuvre entity coming from Tracked (Operation Tracking System). Tracked maneuver. The entityId follows the pattern mrn:urn:eshuv:pdph:Tracked:type:attr:value, where type=Manoeuvre and attr=manoeuvreCode    
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
    amendedOnMooringLocation:    
      description: Location of the 'made fast alongside / amended on mooring' maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    anchoringAnchorUpDate:    
      description: Anchor aweigh (anchor up) time for the anchoring maneuver    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    anchoringDate:    
      description: Anchor down time for the anchoring maneuver    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    anchoringLocation:    
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
    anchoringZone:    
      description: Anchorage zone for the anchoring maneuver    
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
    durationHours:    
      description: Maneuver duration in hours    
      type: number    
      x-ngsi:    
        type: Property    
    endDate:    
      description: Maneuver end date    
      format: date-time    
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
    maneuverCode:    
      description: Maneuver code    
      type: string    
      x-ngsi:    
        type: Property    
    maneuverType:    
      description: Maneuver type    
      type: string    
      x-ngsi:    
        type: Property    
    mooringCablesNumber:    
      description: Number of lines for the mooring maneuver    
      type: number    
      x-ngsi:    
        type: Property    
    mooringChangeCablesNumber:    
      description: Number of lines for the berth-shifting maneuver    
      type: number    
      x-ngsi:    
        type: Property    
    mooringChangeFirstLandCableDate:    
      description: First shore line time for the berth-shifting maneuver    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    mooringChangeInitialLocation:    
      description: Initial location of the berth-shifting maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    mooringChangeLastCableDate:    
      description: Last line time for the berth-shifting maneuver    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    mooringChangeLastLocation:    
      description: Final location of the berth-shifting maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    mooringChangeNoraysFrom:    
      description: Bollard number from (berth-shifting maneuver)    
      type: number    
      x-ngsi:    
        type: Property    
    mooringChangeNoraysTo:    
      description: Bollard number to (berth-shifting maneuver)    
      type: number    
      x-ngsi:    
        type: Property    
    mooringChangeSide:    
      description: Mooring side for the berth-shifting maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    mooringFirstCableDate:    
      description: First line time for the mooring maneuver    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    mooringLocation:    
      description: Location of the mooring maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    mooringNoraysFrom:    
      description: Bollard number from (mooring maneuver)    
      type: number    
      x-ngsi:    
        type: Property    
    mooringNoraysTo:    
      description: Bollard number to (mooring maneuver)    
      type: number    
      x-ngsi:    
        type: Property    
    mooringSide:    
      description: Mooring side for the mooring maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    observations:    
      description: Maneuver observations    
      type: string    
      x-ngsi:    
        type: Property    
    observedDate:    
      description: Last update date of the entity    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    othersLocation:    
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
    othersType:    
      description: Type of other maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    othersZone:    
      description: Zone/location of the other maneuver    
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
    pilotageDisembarkDate:    
      description: Pilot disembarkation time for the pilotage maneuver    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    pilotageDisembarkLocation:    
      description: Pilot disembarkation location for the pilotage maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    pilotageEmbarkDate:    
      description: Pilot embarkation time for the pilotage maneuver    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    pilotageEmbarkLocation:    
      description: Pilot embarkation location for the pilotage maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    pilotageExempt:    
      description: Pilotage exemption    
      type: string    
      x-ngsi:    
        type: Property    
    pilotageObservations:    
      description: Pilotage maneuver observations    
      type: string    
      x-ngsi:    
        type: Property    
    pilotagePilots:    
      description: Pilots involved in the pilotage maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    portCallCode:    
      description: STM register of the port call    
      type: string    
      x-ngsi:    
        type: Property    
    refPortCallId:    
      description: Reference to the port call    
      type: string    
      x-ngsi:    
        type: Property    
    refTugServiceId:    
      description: Reference to the tug service    
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
    startDate:    
      description: Maneuver start date    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    tugboatsNumber:    
      description: Number of tugboats for the tug service maneuver    
      type: number    
      x-ngsi:    
        type: Property    
    tugboatsObservations:    
      description: Tug service maneuver observations    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be TrackedManoeuvre    
      enum:    
        - TrackedManeuver    
      type: string    
      x-ngsi:    
        type: Property    
    undockingLastCableDate:    
      description: Last line time for the unmooring (undocking) maneuver    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    undockingLocation:    
      description: Location of the unmooring (undocking) maneuver    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/TrackedManeuver/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/TrackedManoeuvre/schema.json    
  x-model-tags: ESHUV, i4trust, Tracked    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload    
#### Esempio di TrackedManeuver NGSI-v2 chiave-valore    
Ecco un esempio di TrackedManeuver in formato JSON come chiave-valore. Questo è compatibile con NGSI-v2 quando si utilizza `options=keyValues` e restituisce i dati di contesto di un'entità individuale.  
<details><summary><strong>mostra/nascondi esempio</strong></summary>    
```json  
{  
  "id": "mrn:urn:eshuv:pdph:sigo:sigomanoeuvre:manoeuvrecode:E11:22-M2",  
  "type": "TrackedManeuver",  
  "observedDate": "2024-06-14T08:30:00Z",  
  "refPortCallId": "mrn:urn:eshuv:pdph:sigo:sigoportcall:stmregister:E36:24",  
  "refTugServiceId": "mrn:urn:eshuv:pdph:sigo:sigotugboat:name:examplename",  
  "portCallCode": "E36/24",  
  "maneuverCode": "E11/22-M2",  
  "maneuverType": "Atraque",  
  "startDate": "2024-06-14T08:30:00Z",  
  "endDate": "2024-06-14T08:30:00Z",  
  "durationHours": 0.33,  
  "observations": "Observaciones de Maniobra ejemplo",  
  "mooringFirstCableDate": "2024-06-14T08:30:00Z",  
  "mooringLocation": "PANTALAN ERCROSS-ARAGONESAS",  
  "mooringCablesNumber": 3,  
  "mooringNoraysFrom": 4,  
  "mooringNoraysTo": 6,  
  "mooringSide": "Babor",  
  "mooringChangeLastCableDate": "2024-06-14T08:30:00Z",  
  "mooringChangeInitialLocation": "REINA SOFIA",  
  "mooringChangeFirstLandCableDate": "2024-06-14T08:30:00Z",  
  "mooringChangeLastLocation": "MUELLE SUR",  
  "mooringChangeCablesNumber": 2,  
  "mooringChangeNoraysFrom": 1,  
  "mooringChangeNoraysTo": 3,  
  "mooringChangeSide": "string",  
  "undockingLastCableDate": "2024-06-14T08:30:00Z",  
  "undockingLocation": "REINA SOFIA",  
  "amendedOnMooringLocation": "REINA SOFIA",  
  "anchoringZone": "string",  
  "anchoringLocation": {  
    "type": "Point",  
    "coordinates": [-6.3872, 36.02]  
  },  
  "anchoringDate": "2024-06-14T08:30:00Z",  
  "anchoringAnchorUpDate": "2024-06-14T08:30:00Z",  
  "othersType": "string",  
  "othersZone": "string",  
  "othersLocation": {  
    "type": "Point",  
    "coordinates": [-6.3872, 36.02]  
  },  
  "pilotageEmbarkLocation": "LEVANTE NORTE",  
  "pilotageEmbarkDate": "2024-06-14T08:30:00Z",  
  "pilotageDisembarkLocation": "LEVANTE SUR",  
  "pilotageDisembarkDate": "2024-06-14T08:30:00Z",  
  "pilotagePilots": "Carlos Bernal",  
  "pilotageExempt": "No",  
  "pilotageObservations": "Observaciones de practicaje",  
  "tugboatsNumber": 1,  
  "tugboatsObservations": "Observaciones de remolque"  
}  
```  
</details>  
#### Esempio di TrackedManeuver NGSI-v2 normalizzato    
Ecco un esempio di TrackedManeuver in formato JSON come normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di un'entità individuale.  
<details><summary><strong>mostra/nascondi esempio</strong></summary>    
```json  
{  
  "id": "mrn:urn:eshuv:pdph:sigo:sigomanoeuvre:manoeuvrecode:E11:22-M2",  
  "type": "TrackedManeuver",  
  "observedDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "refPortCallId": {  
    "type": "Text",  
    "value": "mrn:urn:eshuv:pdph:sigo:sigoportcall:stmregister:E36:24"  
  },  
  "refTugServiceId": {  
    "type": "Text",  
    "value": "mrn:urn:eshuv:pdph:sigo:sigotugboat:name:examplename"  
  },  
  "portCallCode": {  
    "type": "Text",  
    "value": "E36/24"  
  },  
  "maneuverCode": {  
    "type": "Text",  
    "value": "E11/22-M2"  
  },  
  "maneuverType": {  
    "type": "Text",  
    "value": "Atraque"  
  },  
  "startDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "endDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "durationHours": {  
    "type": "Number",  
    "value": 0.33  
  },  
  "observations": {  
    "type": "Text",  
    "value": "Observaciones de Maniobra ejemplo"  
  },  
  "mooringFirstCableDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "mooringLocation": {  
    "type": "Text",  
    "value": "PANTALAN ERCROSS-ARAGONESAS"  
  },  
  "mooringCablesNumber": {  
    "type": "Number",  
    "value": 3  
  },  
  "mooringNoraysFrom": {  
    "type": "Number",  
    "value": 4  
  },  
  "mooringNoraysTo": {  
    "type": "Number",  
    "value": 6  
  },  
  "mooringSide": {  
    "type": "Text",  
    "value": "Babor"  
  },  
  "mooringChangeLastCableDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "mooringChangeInitialLocation": {  
    "type": "Text",  
    "value": "REINA SOFIA"  
  },  
  "mooringChangeFirstLandCableDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "mooringChangeLastLocation": {  
    "type": "Text",  
    "value": "MUELLE SUR"  
  },  
  "mooringChangeCablesNumber": {  
    "type": "Number",  
    "value": 2  
  },  
  "mooringChangeNoraysFrom": {  
    "type": "Number",  
    "value": 1  
  },  
  "mooringChangeNoraysTo": {  
    "type": "Number",  
    "value": 3  
  },  
  "mooringChangeSide": {  
    "type": "Text",  
    "value": "string"  
  },  
  "undockingLastCableDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "undockingLocation": {  
    "type": "Text",  
    "value": "REINA SOFIA"  
  },  
  "amendedOnMooringLocation": {  
    "type": "Text",  
    "value": "REINA SOFIA"  
  },  
  "anchoringZone": {  
    "type": "Text",  
    "value": "string"  
  },  
  "anchoringLocation": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -6.3872,  
        36.02  
      ]  
    }  
  },  
  "anchoringDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "anchoringAnchorUpDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "othersType": {  
    "type": "Text",  
    "value": "string"  
  },  
  "othersZone": {  
    "type": "Text",  
    "value": "string"  
  },  
  "othersLocation": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -6.3872,  
        36.02  
      ]  
    }  
  },  
  "pilotageEmbarkLocation": {  
    "type": "Text",  
    "value": "LEVANTE NORTE"  
  },  
  "pilotageEmbarkDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "pilotageDisembarkLocation": {  
    "type": "Text",  
    "value": "LEVANTE SUR"  
  },  
  "pilotageDisembarkDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "pilotagePilots": {  
    "type": "Text",  
    "value": "Carlos Bernal"  
  },  
  "pilotageExempt": {  
    "type": "Text",  
    "value": "No"  
  },  
  "pilotageObservations": {  
    "type": "Text",  
    "value": "Observaciones de practicaje"  
  },  
  "tugboatsNumber": {  
    "type": "Number",  
    "value": 1  
  },  
  "tugboatsObservations": {  
    "type": "Text",  
    "value": "Observaciones de remolque"  
  }  
}  
```  
</details>  
#### Esempio di TrackedManeuver NGSI-LD chiave-valore    
Ecco un esempio di TrackedManeuver in formato JSON-LD come chiave-valore. Questo è compatibile con NGSI-LD quando si utilizza `options=keyValues` e restituisce i dati di contesto di un'entità individuale.  
<details><summary><strong>mostra/nascondi esempio</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:TrackedManeuver:mrn:urn:eshuv:pdph:sigo:sigomanoeuvre:manoeuvrecode:E11:22-M2",  
  "type": "TrackedManeuver",  
  "observedDate": "2024-06-14T08:30:00Z",  
  "refPortCallId": "urn:ngsi-ld:PortCallId:mrn:urn:eshuv:pdph:sigo:sigoportcall:stmregister:E36:24",  
  "refTugServiceId": "urn:ngsi-ld:TugServiceId:mrn:urn:eshuv:pdph:sigo:sigotugboat:name:examplename",  
  "portCallCode": "E36/24",  
  "maneuverCode": "E11/22-M2",  
  "maneuverType": "Atraque",  
  "startDate": "2024-06-14T08:30:00Z",  
  "endDate": "2024-06-14T08:30:00Z",  
  "durationHours": 0.33,  
  "observations": "Observaciones de Maniobra ejemplo",  
  "mooringFirstCableDate": "2024-06-14T08:30:00Z",  
  "mooringLocation": "PANTALAN ERCROSS-ARAGONESAS",  
  "mooringCablesNumber": 3,  
  "mooringNoraysFrom": 4,  
  "mooringNoraysTo": 6,  
  "mooringSide": "Babor",  
  "mooringChangeLastCableDate": "2024-06-14T08:30:00Z",  
  "mooringChangeInitialLocation": "REINA SOFIA",  
  "mooringChangeFirstLandCableDate": "2024-06-14T08:30:00Z",  
  "mooringChangeLastLocation": "MUELLE SUR",  
  "mooringChangeCablesNumber": 2,  
  "mooringChangeNoraysFrom": 1,  
  "mooringChangeNoraysTo": 3,  
  "mooringChangeSide": "string",  
  "undockingLastCableDate": "2024-06-14T08:30:00Z",  
  "undockingLocation": "REINA SOFIA",  
  "amendedOnMooringLocation": "REINA SOFIA",  
  "anchoringZone": "string",  
  "anchoringLocation": {  
    "type": "Point",  
    "coordinates": [  
      -6.3872,  
      36.02  
    ]  
  },  
  "anchoringDate": "2024-06-14T08:30:00Z",  
  "anchoringAnchorUpDate": "2024-06-14T08:30:00Z",  
  "othersType": "string",  
  "othersZone": "string",  
  "othersLocation": {  
    "type": "Point",  
    "coordinates": [  
      -6.3872,  
      36.02  
    ]  
  },  
  "pilotageEmbarkLocation": "LEVANTE NORTE",  
  "pilotageEmbarkDate": "2024-06-14T08:30:00Z",  
  "pilotageDisembarkLocation": "LEVANTE SUR",  
  "pilotageDisembarkDate": "2024-06-14T08:30:00Z",  
  "pilotagePilots": "Carlos Bernal",  
  "pilotageExempt": "No",  
  "pilotageObservations": "Observaciones de practicaje",  
  "tugboatsNumber": 1,  
  "tugboatsObservations": "Observaciones de remolque",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Esempio di TrackedManeuver NGSI-LD normalizzato    
Ecco un esempio di TrackedManeuver in formato JSON-LD come normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di un'entità individuale.  
<details><summary><strong>mostra/nascondi esempio</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:TrackedManeuver:mrn:urn:eshuv:pdph:sigo:sigomanoeuvre:manoeuvrecode:E11:22-M2",  
  "type": "TrackedManeuver",  
  "observedDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "refPortCallId": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PortCallId:mrn:urn:eshuv:pdph:sigo:sigoportcall:stmregister:E36:24"  
  },  
  "refTugServiceId": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:TugServiceId:mrn:urn:eshuv:pdph:sigo:sigotugboat:name:examplename"  
  },  
  "portCallCode": {  
    "type": "Property",  
    "value": "E36/24"  
  },  
  "maneuverCode": {  
    "type": "Property",  
    "value": "E11/22-M2"  
  },  
  "maneuverType": {  
    "type": "Property",  
    "value": "Atraque"  
  },  
  "startDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "endDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "durationHours": {  
    "type": "Property",  
    "value": 0.33  
  },  
  "observations": {  
    "type": "Property",  
    "value": "Observaciones de Maniobra ejemplo"  
  },  
  "mooringFirstCableDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "mooringLocation": {  
    "type": "Property",  
    "value": "PANTALAN ERCROSS-ARAGONESAS"  
  },  
  "mooringCablesNumber": {  
    "type": "Property",  
    "value": 3  
  },  
  "mooringNoraysFrom": {  
    "type": "Property",  
    "value": 4  
  },  
  "mooringNoraysTo": {  
    "type": "Property",  
    "value": 6  
  },  
  "mooringSide": {  
    "type": "Property",  
    "value": "Babor"  
  },  
  "mooringChangeLastCableDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "mooringChangeInitialLocation": {  
    "type": "Property",  
    "value": "REINA SOFIA"  
  },  
  "mooringChangeFirstLandCableDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "mooringChangeLastLocation": {  
    "type": "Property",  
    "value": "MUELLE SUR"  
  },  
  "mooringChangeCablesNumber": {  
    "type": "Property",  
    "value": 2  
  },  
  "mooringChangeNoraysFrom": {  
    "type": "Property",  
    "value": 1  
  },  
  "mooringChangeNoraysTo": {  
    "type": "Property",  
    "value": 3  
  },  
  "mooringChangeSide": {  
    "type": "Property",  
    "value": "string"  
  },  
  "undockingLastCableDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "undockingLocation": {  
    "type": "Property",  
    "value": "REINA SOFIA"  
  },  
  "amendedOnMooringLocation": {  
    "type": "Property",  
    "value": "REINA SOFIA"  
  },  
  "anchoringZone": {  
    "type": "Property",  
    "value": "string"  
  },  
  "anchoringLocation": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -6.3872,  
        36.02  
      ]  
    }  
  },  
  "anchoringDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "anchoringAnchorUpDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "othersType": {  
    "type": "Property",  
    "value": "string"  
  },  
  "othersZone": {  
    "type": "Property",  
    "value": "string"  
  },  
  "othersLocation": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -6.3872,  
        36.02  
      ]  
    }  
  },  
  "pilotageEmbarkLocation": {  
    "type": "Property",  
    "value": "LEVANTE NORTE"  
  },  
  "pilotageEmbarkDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "pilotageDisembarkLocation": {  
    "type": "Property",  
    "value": "LEVANTE SUR"  
  },  
  "pilotageDisembarkDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "pilotagePilots": {  
    "type": "Property",  
    "value": "Carlos Bernal"  
  },  
  "pilotageExempt": {  
    "type": "Property",  
    "value": "No"  
  },  
  "pilotageObservations": {  
    "type": "Property",  
    "value": "Observaciones de practicaje"  
  },  
  "tugboatsNumber": {  
    "type": "Property",  
    "value": 1  
  },  
  "tugboatsObservations": {  
    "type": "Property",  
    "value": "Observaciones de remolque"  
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
Vedi [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->