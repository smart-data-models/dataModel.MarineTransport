<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : TrackedManeuver  
=======================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/TrackedManeuver/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Entité TrackedManoeuvre issue de Tracked (Système de suivi des opérations). Manœuvre suivie. L'identifiant d'entité suit le modèle mrn:urn:eshuv:pdph:Tracked:type:attr:value, où type=Manoeuvre et attr=manoeuvreCode**  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] Si il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>  
- `address[object]` : L'adresse postale  . Modèle : [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]` : Le pays. Par exemple, l'Espagne  . Modèle : [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]` : La localité dans laquelle se trouve l'adresse de la rue, et qui se trouve dans la région  . Modèle : [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]` : La région dans laquelle se trouve la localité, et qui se trouve dans le pays  . Modèle : [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]` : Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local    
	- `postOfficeBoxNumber[string]` : Le numéro de boîte postale pour les adresses de boîte postale. Par exemple, 03578  . Modèle : [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]` : Le code postal. Par exemple, 24004  . Modèle : [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]` : L'adresse de la rue  . Modèle : [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]` : Numéro identifiant une propriété spécifique sur une rue publique    
- `alternateName[string]` : Un nom alternatif pour cet élément  - `amendedOnMooringLocation[string]` : Emplacement de la manœuvre « amarré le long / modifié sur l'amarrage »  - `anchoringAnchorUpDate[date-time]` : Heure de levage de l'ancre (ancre levée) pour la manœuvre d'ancre  - `anchoringDate[date-time]` : Heure de descente de l'ancre pour la manœuvre d'ancre  - `anchoringLocation[*]` : Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, de plusieurs points, de plusieurs lignes ou de plusieurs polygones  - `anchoringZone[string]` : Zone d'ancre pour la manœuvre d'ancre  - `areaServed[string]` : La zone géographique où un service ou un élément est proposé  . Modèle : [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]` : Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]` : Horodatage de la création de l'entité. Cela sera généralement alloué par la plate-forme de stockage  - `dateModified[date-time]` : Horodatage de la dernière modification de l'entité. Cela sera généralement alloué par la plate-forme de stockage  - `description[string]` : Une description de cet élément  - `durationHours[number]` : Durée de la manœuvre en heures  - `endDate[date-time]` : Date de fin de la manœuvre  - `id[*]` : Identifiant unique de l'entité  - `location[*]` : Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, de plusieurs points, de plusieurs lignes ou de plusieurs polygones  - `maneuverCode[string]` : Code de manœuvre  - `maneuverType[string]` : Type de manœuvre  - `mooringCablesNumber[number]` : Nombre de lignes pour la manœuvre d'amarrage  - `mooringChangeCablesNumber[number]` : Nombre de lignes pour la manœuvre de déplacement de quai  - `mooringChangeFirstLandCableDate[date-time]` : Heure de la première ligne pour la manœuvre de déplacement de quai  - `mooringChangeInitialLocation[string]` : Emplacement initial de la manœuvre de déplacement de quai  - `mooringChangeLastCableDate[date-time]` : Heure de la dernière ligne pour la manœuvre de déplacement de quai  - `mooringChangeLastLocation[string]` : Emplacement final de la manœuvre de déplacement de quai  - `mooringChangeNoraysFrom[number]` : Numéro de bollard depuis (manœuvre de déplacement de quai)  - `mooringChangeNoraysTo[number]` : Numéro de bollard vers (manœuvre de déplacement de quai)  - `mooringChangeSide[string]` : Côté d'amarrage pour la manœuvre de déplacement de quai  - `mooringFirstCableDate[date-time]` : Heure de la première ligne pour la manœuvre d'amarrage  - `mooringLocation[string]` : Emplacement de la manœuvre d'amarrage  - `mooringNoraysFrom[number]` : Numéro de bollard depuis (manœuvre d'amarrage)  - `mooringNoraysTo[number]` : Numéro de bollard vers (manœuvre d'amarrage)  - `mooringSide[string]` : Côté d'amarrage pour la manœuvre d'amarrage  - `name[string]` : Le nom de cet élément  - `observations[string]` : Observations de manœuvre  - `observedDate[date-time]` : Date de dernière mise à jour de l'entité  - `othersLocation[*]` : Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, de plusieurs points, de plusieurs lignes ou de plusieurs polygones  - `othersType[string]` : Type d'autre manœuvre  - `othersZone[string]` : Zone/emplacement de l'autre manœuvre  - `owner[array]` : Une liste contenant une séquence de caractères codés en JSON référençant les identifiants uniques des propriétaires  - `pilotageDisembarkDate[date-time]` : Heure de débarquement du pilote pour la manœuvre de pilotage  - `pilotageDisembarkLocation[string]` : Emplacement de débarquement du pilote pour la manœuvre de pilotage  - `pilotageEmbarkDate[date-time]` : Heure d'embarquement du pilote pour la manœuvre de pilotage  - `pilotageEmbarkLocation[string]` : Emplacement d'embarquement du pilote pour la manœuvre de pilotage  - `pilotageExempt[string]` : Exemption de pilotage  - `pilotageObservations[string]` : Observations de la manœuvre de pilotage  - `pilotagePilots[string]` : Pilotes impliqués dans la manœuvre de pilotage  - `portCallCode[string]` : Registre STM de l'appel au port  - `refPortCallId[string]` : Référence à l'appel au port  - `refTugServiceId[string]` : Référence au service de remorquage  - `seeAlso[*]` : liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source[string]` : Une séquence de caractères indiquant la source originale des données d'entité sous la forme d'une URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source  - `startDate[date-time]` : Date de début de la manœuvre  - `tugboatsNumber[number]` : Nombre de remorqueurs pour la manœuvre de service de remorquage  - `tugboatsObservations[string]` : Observations de la manœuvre de service de remorquage  - `type[string]` : Type d'entité NGSI. Il doit s'agir de TrackedManoeuvre  - `undockingLastCableDate[date-time]` : Heure de la dernière ligne pour la manœuvre de déamarrage (désamarrage)  - `undockingLocation[string]` : Emplacement de la manœuvre de déamarrage (désamarrage)  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Description du modèle de données des propriétés  
Classées par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>détails yaml complets</strong></summary>    
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
## Exemples de charges utiles    
#### Exemple de TrackedManeuver NGSI-v2 en valeurs clés    
Voici un exemple de TrackedManeuver au format JSON en valeurs clés. Cela est compatible avec NGSI-v2 lors de l'utilisation de `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    
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
#### Exemple de TrackedManeuver NGSI-v2 normalisé    
Voici un exemple de TrackedManeuver au format JSON en normalisé. Cela est compatible avec NGSI-v2 lorsqu'aucune option n'est utilisée et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    
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
#### Exemple de TrackedManeuver NGSI-LD en valeurs clés    
Voici un exemple de TrackedManeuver au format JSON-LD en valeurs clés. Cela est compatible avec NGSI-LD lors de l'utilisation de `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    
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
#### Exemple de TrackedManeuver NGSI-LD normalisé    
Voici un exemple de TrackedManeuver au format JSON-LD en normalisé. Cela est compatible avec NGSI-LD lorsqu'aucune option n'est utilisée et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    
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
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de gérer les unités de magnitude  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->