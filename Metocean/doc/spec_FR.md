<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Metocean  
================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/Metocean/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Ce modèle de données représente les informations météocéaniques (météorologie + océanographie) pour une période et un emplacement donnés. Il prend en charge à la fois les mesures de séries chronologiques et les prévisions à l'aide de points avec des échantillons de données observés**  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] Si il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modes</sub></sup>  
- `address[object]`: L'adresse postale  . Modèle : [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Modèle : [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse de la rue, et qui se trouve dans la région  . Modèle : [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La région dans laquelle se trouve la localité, et qui se trouve dans le pays  . Modèle : [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local    
	- `postOfficeBoxNumber[string]`: Le numéro de boîte postale pour les adresses de boîte postale. Par exemple, 03578  . Modèle : [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Modèle : [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'adresse de la rue  . Modèle : [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numéro identifiant une propriété spécifique sur une rue publique    
- `alternateName[string]`: Un nom alternatif pour cet élément  - `areaServed[string]`: La zone géographique dans laquelle un service ou un élément proposé est fourni  . Modèle : [https://schema.org/Text](https://schema.org/Text)- `code[string]`: Code ou identifiant de produit/computation météocéanique  . Modèle : [https://schema.org/Text](https://schema.org/Text)- `collectionName[string]`: Nom logique de la collection météocéanique (par exemple, '10-min-metocean-measures', '12hour-daily-forecast')  . Modèle : [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisée  - `dateCreated[date-time]`: Horodatage de création de l'entité. Cela sera généralement alloué par la plate-forme de stockage  - `dateModified[date-time]`: Horodatage de la dernière modification de l'entité. Cela sera généralement alloué par la plate-forme de stockage  - `description[string]`: Une description de cet élément  - `fromDate[date-time]`: Début de la période météocéanique couverte par cette entité, en UTC selon la norme ISO 8601  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Cela peut être un point, une ligne, un polygone, des points multiples, des lignes multiples ou des polygones multiples  - `modifiedAt[date-time]`: Horodatage UTC, selon la norme ISO 8601, de la prévision ou du jeu de données calculé (si applicable)  - `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères codés en JSON référençant les identifiants uniques des propriétaires  - `points[array]`: Tableau de points météocéaniques (capteurs, points de grille, emplacements de prédiction) chacun contenant une série chronologique d'échantillons de données  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source[string]`: Une séquence de caractères donnant la source d'origine des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source  - `toDate[date-time]`: Fin de la période météocéanique couverte par cette entité, en UTC selon la norme ISO 8601  - `type[string]`: Type d'entité NGSI. Il doit s'agir de Metocean  <!-- /30-PropertiesList -->  
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
Metocean:    
  description: This data model represents metocean information (meteorology + oceanography) for a given period and location. It supports both time-series measures and forecasts using points with observed data samples    
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
    code:    
      description: Metocean product/area code or identifier of the computation set    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    collectionName:    
      description: Logical name of the metocean collection (e.g. '10-min-metocean-measures', '12hour-daily-forecast')    
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
    fromDate:    
      description: ISO 8601 UTC start of the metocean period covered by this entity    
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
    modifiedAt:    
      description: ISO 8601 UTC timestamp when the forecast or dataset was computed (if applicable)    
      format: date-time    
      type: string    
      x-ngsi:    
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
    points:    
      description: Array of metocean points (sensors, grid points, prediction locations) each holding a time-series of data samples    
      items:    
        properties:    
          data:    
            description: Time-series of metocean samples for this point    
            items:    
              properties:    
                currentDir:    
                  description: Current direction in degrees (0–360)    
                  maximum: 360    
                  minimum: 0    
                  type: number    
                  x-ngsi:    
                    model: https://schema.org/Number    
                    type: Property    
                currentSpeed:    
                  description: Current speed in m/s    
                  type: number    
                  x-ngsi:    
                    model: https://schema.org/Number    
                    type: Property    
                observedAt:    
                  description: NGSI-LD observedAt timestamp for this data sample (ISO 8601, UTC preferred)    
                  format: date-time    
                  type: string    
                  x-ngsi:    
                    type: Property    
                peakDateTime:    
                  description: If applicable, ISO 8601 time of the nearest related tide peak (high or low)    
                  format: date-time    
                  type: string    
                  x-ngsi:    
                    type: Property    
                peakHeight:    
                  description: Height of the related tide peak in meters    
                  type: number    
                  x-ngsi:    
                    model: https://schema.org/Number    
                    type: Property    
                peakType:    
                  description: Type of tide peak (hightide/lowtide). May be empty when not applicable    
                  enum:    
                    - hightide    
                    - lowtide    
                    - ''    
                  type: string    
                  x-ngsi:    
                    type: Property    
                significantWaveHeight:    
                  description: Significant wave height in meters    
                  type: number    
                  x-ngsi:    
                    model: https://schema.org/Number    
                    type: Property    
                tideHeight:    
                  description: Tide height or water level at this instant, referenced to local datum, in meters    
                  type: number    
                  x-ngsi:    
                    model: https://schema.org/Number    
                    type: Property    
                tideHeight10mValues:    
                  description: Optional intra-hour tide height values (e.g.10-minute steps within the hour around 'observedAt'), in meters    
                  items:    
                    description: Every element in the optional intra-hour tide height values    
                    type: number    
                    x-ngsi:    
                      type: Property    
                  type: array    
                  x-ngsi:    
                    model: https://schema.org/Number    
                    type: Property    
                waveDir:    
                  description: Mean wave direction in degrees (0–360)    
                  maximum: 360    
                  minimum: 0    
                  type: number    
                  x-ngsi:    
                    model: https://schema.org/Number    
                    type: Property    
                waveHeight:    
                  description: Wave height in meters as provided by the source (often total or characteristic wave height)    
                  type: number    
                  x-ngsi:    
                    model: https://schema.org/Number    
                    type: Property    
                wavePeakDir:    
                  description: Peak wave direction in degrees (0–360), if provided by the source    
                  maximum: 360    
                  minimum: 0    
                  type: number    
                  x-ngsi:    
                    model: https://schema.org/Number    
                    type: Property    
                wavePeakPeriod:    
                  description: Peak wave period in seconds    
                  type: number    
                  x-ngsi:    
                    model: https://schema.org/Number    
                    type: Property    
                windDir:    
                  description: Wind direction in degrees (0–360)    
                  maximum: 360    
                  minimum: 0    
                  type: number    
                  x-ngsi:    
                    model: https://schema.org/Number    
                    type: Property    
                windSpeed:    
                  description: Wind speed in m/s    
                  type: number    
                  x-ngsi:    
                    model: https://schema.org/Number    
                    type: Property    
              type: object    
            type: array    
            x-ngsi:    
              type: Property    
          dataNature:    
            description: Nature of the data contained in this entity    
            enum:    
              - forecast    
              - measure    
              - measure-and-forecast    
            type: string    
            x-ngsi:    
              type: Property    
          pointCode:    
            description: Numeric code of the metocean point (sensor, location or prediction point)    
            type: number    
            x-ngsi:    
              model: https://schema.org/Number    
              type: Property    
          pointName:    
            description: Human-readable name of the metocean point    
            type: string    
            x-ngsi:    
              model: https://schema.org/Text    
              type: Property    
          pointType:    
            description: Type of metocean point (e.g. 'current-meter', 'wave-gauge', 'wind-gauge', 'cma-prediction')    
            enum:    
              - cma-prediction    
              - current-meter    
              - ihm-prediction    
              - tide-gauge    
              - wave-gauge    
              - wind-gauge    
              - other    
            type: string    
            x-ngsi:    
              model: https://schema.org/Text    
              type: Property    
          variables:    
            description: Comma-separated list of variable names present in the 'data' array of this point (e.g. 'currentSpeed,currentDir,tideHeight')    
            type: string    
            x-ngsi:    
              model: https://schema.org/Text    
              type: Property    
        type: object    
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
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    toDate:    
      description: ISO 8601 UTC end of the metocean period covered by this entity    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be Metocean    
      enum:    
        - Metocean    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/Metocean/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/Metocean/schema.json    
  x-model-tags: ESHUV, i4trust    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles    
#### Exemple de clés-valeurs Metocean NGSI-v2    
Voici un exemple de Metocean au format JSON en tant que clés-valeurs. Cela est compatible avec NGSI-v2 lors de l'utilisation de `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:iot:measures:20250819",  
  "type": "Metocean",  
  "fromDate": "2025-08-19T13:00:00Z",  
  "toDate": "2025-08-22T13:10:00Z",  
  "source": "PDPH/PCM/...",  
  "collectionName": "10-min-metocean-measures",  
  "modifiedAt": "2025-08-19T13:07:46Z",  
  "points": [  
    {  
      "pointCode": 12,  
      "pointName": "reviroA",  
      "pointType": "current-meter",  
      "variables": "currentSpeed,currentDir,tideHeight",  
      "dataNature": "measure",  
      "data": [  
        {  
          "observedAt": "2024-11-30T01:03:00Z",  
          "currentSpeed": 2.24,  
          "currentDir": 170,  
          "tideHeight": 2.24  
        },  
        {  
          "observedAt": "2024-11-30T02:12:00Z",  
          "currentSpeed": 2.24,  
          "currentDir": 170,  
          "tideHeight": 2.24  
        }  
      ]  
    },  
    {  
      "pointCode": 13,  
      "pointName": "canal-ext",  
      "pointType": "current-meter",  
      "variables": "currentSpeed,currentDir",  
      "dataNature": "measure",  
      "data": [  
        {  
          "observedAt": "2024-11-30T01:03:00Z",  
          "currentSpeed": 2.24,  
          "currentDir": 170,  
          "tideHeight": 2.24  
        },  
        {  
          "observedAt": "2024-11-30T02:12:00Z",  
          "currentSpeed": 2.00,  
          "currentDir": 100,  
          "tideHeight": 2.34  
        }  
      ]  
    },  
    {  
      "pointCode": 301,  
      "pointName": "mareografo-1",  
      "pointType": "wave-gauge",  
      "variables": "waveDir,wavePeakDir,waveHeight,significantWaveHeight,wavePeakPeriod",  
      "dataNature": "measure",  
      "data": [  
        {  
          "observedAt": "2024-11-30T01:00:00Z",  
          "waveDir": 0.0,  
          "wavePeakDir": 0.0,  
          "waveHeight": 0.0,  
          "significantWaveHeight": 0.0,  
          "wavePeakPeriod": 0.0  
        }  
      ]  
    },  
    {  
      "pointCode": 5231001,  
      "pointName": "Muelle Levante",  
      "pointType": "cma-prediction",  
      "variables": "height,peakDate,currentSpeed,peakHeight,peakType,waveHeightM,waveDir,windSpeed",  
      "dataNature": "forecast",  
      "data": [  
        {  
          "observedAt": "2024-11-30T02:00:00",  
          "waveDir": 120,  
          "wavePeakDir": 100,  
          "waveHeight": 1.2,  
          "significantWaveHeight": 0.0,  
          "wavePeakPeriod": 0.0,  
          "windSpeed": 2.16,  
          "windDir": 61,  
          "currentSpeed": 2.53,  
          "currentDir": 122.0,  
          "peakDateTime": "",  
          "peakType": "",  
          "peakHeight": 0.0,  
          "tideHeight": 2.65,  
          "tideHeight10mValues": [  
            2.8984904,  
            2.870916,  
            2.8378513,  
            2.7995095,  
            2.7561383,  
            2.7080173  
          ]  
        },  
        {  
          "observedAt": "2024-11-30T03:00:00",  
          "waveDir": 120,  
          "wavePeakDir": 100,  
          "waveHeight": 1.2,  
          "significantWaveHeight": 0.0,  
          "wavePeakPeriod": 0.0,  
          "windSpeed": 2.16,  
          "windDir": 61,  
          "currentSpeed": 2.53,  
          "currentDir": 122.0,  
          "peakDateTime": "",  
          "peakType": "",  
          "peakHeight": 0.0,  
          "tideHeight": 2.65,  
          "tideHeight10mValues": [  
            2.65,  
            2.59,  
            2.53,  
            2.47,  
            2.40,  
            2.33  
          ]  
        }  
      ]  
    },  
    {  
      "pointCode": 5231003,  
      "pointName": "Muelle Levante",  
      "pointType": "cma-prediction",  
      "variables": "height,peakDate,currentSpeed,peakHeight,peakType,waveHeightM,waveDir,windSpeed",  
      "dataNature": "forecast",  
      "data": [  
        {  
          "observedAt": "2024-11-30T02:00:00",  
          "waveDir": 120,  
          "wavePeakDir": 100,  
          "waveHeight": 1.2,  
          "significantWaveHeight": 0.0,  
          "wavePeakPeriod": 0.0,  
          "windSpeed": 2.16,  
          "windDir": 61,  
          "currentSpeed": 2.53,  
          "currentDir": 122.0,  
          "peakDateTime": "",  
          "peakType": "",  
          "peakHeight": 0.0,  
          "tideHeight": 2.65,  
          "tideHeight10mValues": [  
            2.8984904,  
            2.870916,  
            2.8378513,  
            2.7995095,  
            2.7561383,  
            2.7080173  
          ]  
        },  
        {  
          "observedAt": "2024-11-30T03:00:00",  
          "waveDir": 120,  
          "wavePeakDir": 100,  
          "waveHeight": 1.2,  
          "significantWaveHeight": 0.0,  
          "wavePeakPeriod": 0.0,  
          "windSpeed": 2.16,  
          "windDir": 61,  
          "currentSpeed": 2.53,  
          "currentDir": 122.0,  
          "peakDateTime": "",  
          "peakType": "",  
          "peakHeight": 0.0,  
          "tideHeight": 2.65,  
          "tideHeight10mValues": [  
            2.65,  
            2.59,  
            2.53,  
            2.47,  
            2.40,  
            2.33  
          ]  
        }  
      ]  
    }  
  ]  
}  
```  
</details>  
#### Exemple de Metocean NGSI-v2 normalisé    
Voici un exemple de Metocean au format JSON en tant que normalisé. Cela est compatible avec NGSI-v2 lorsqu'aucune option n'est utilisée et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:iot:measures:20250819",  
  "type": "Metocean",  
  "fromDate": {  
    "type": "DateTime",  
    "value": "2025-08-19T13:00:00Z"  
  },  
  "toDate": {  
    "type": "DateTime",  
    "value": "2025-08-22T13:10:00Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "PDPH/PCM/..."  
  },  
  "collectionName": {  
    "type": "Text",  
    "value": "10-min-metocean-measures"  
  },  
  "modifiedAt": {  
    "type": "DateTime",  
    "value": "2025-08-19T13:07:46Z"  
  },  
  "points": {  
    "type": "Array",  
    "value": [  
      {  
        "pointCode": 12,  
        "pointName": "reviroA",  
        "pointType": "current-meter",  
        "variables": "currentSpeed,currentDir,tideHeight",  
        "dataNature": "measure",  
        "data": [  
          {  
            "observedAt": "2024-11-30T01:03:00Z",  
            "currentSpeed": 2.24,  
            "currentDir": 170,  
            "tideHeight": 2.24  
          },  
          {  
            "observedAt": "2024-11-30T02:12:00Z",  
            "currentSpeed": 2.24,  
            "currentDir": 170,  
            "tideHeight": 2.24  
          }  
        ]  
      },  
      {  
        "pointCode": 13,  
        "pointName": "canal-ext",  
        "pointType": "current-meter",  
        "variables": "currentSpeed,currentDir",  
        "dataNature": "measure",  
        "data": [  
          {  
            "observedAt": "2024-11-30T01:03:00Z",  
            "currentSpeed": 2.24,  
            "currentDir": 170,  
            "tideHeight": 2.24  
          },  
          {  
            "observedAt": "2024-11-30T02:12:00Z",  
            "currentSpeed": 2.0,  
            "currentDir": 100,  
            "tideHeight": 2.34  
          }  
        ]  
      },  
      {  
        "pointCode": 301,  
        "pointName": "mareografo-1",  
        "pointType": "wave-gauge",  
        "variables": "waveDir,wavePeakDir,waveHeight,significantWaveHeight,wavePeakPeriod",  
        "dataNature": "measure",  
        "data": [  
          {  
            "observedAt": "2024-11-30T01:00:00Z",  
            "waveDir": 0.0,  
            "wavePeakDir": 0.0,  
            "waveHeight": 0.0,  
            "significantWaveHeight": 0.0,  
            "wavePeakPeriod": 0.0  
          }  
        ]  
      },  
      {  
        "pointCode": 5231001,  
        "pointName": "Muelle Levante",  
        "pointType": "cma-prediction",  
        "variables": "height,peakDate,currentSpeed,peakHeight,peakType,waveHeightM,waveDir,windSpeed",  
        "dataNature": "forecast",  
        "data": [  
          {  
            "observedAt": "2024-11-30T02:00:00",  
            "waveDir": 120,  
            "wavePeakDir": 100,  
            "waveHeight": 1.2,  
            "significantWaveHeight": 0.0,  
            "wavePeakPeriod": 0.0,  
            "windSpeed": 2.16,  
            "windDir": 61,  
            "currentSpeed": 2.53,  
            "currentDir": 122.0,  
            "peakDateTime": "",  
            "peakType": "",  
            "peakHeight": 0.0,  
            "tideHeight": 2.65,  
            "tideHeight10mValues": [  
              2.8984904,  
              2.870916,  
              2.8378513,  
              2.7995095,  
              2.7561383,  
              2.7080173  
            ]  
          },  
          {  
            "observedAt": "2024-11-30T03:00:00",  
            "waveDir": 120,  
            "wavePeakDir": 100,  
            "waveHeight": 1.2,  
            "significantWaveHeight": 0.0,  
            "wavePeakPeriod": 0.0,  
            "windSpeed": 2.16,  
            "windDir": 61,  
            "currentSpeed": 2.53,  
            "currentDir": 122.0,  
            "peakDateTime": "",  
            "peakType": "",  
            "peakHeight": 0.0,  
            "tideHeight": 2.65,  
            "tideHeight10mValues": [  
              2.65,  
              2.59,  
              2.53,  
              2.47,  
              2.4,  
              2.33  
            ]  
          }  
        ]  
      },  
      {  
        "pointCode": 5231003,  
        "pointName": "Muelle Levante",  
        "pointType": "cma-prediction",  
        "variables": "height,peakDate,currentSpeed,peakHeight,peakType,waveHeightM,waveDir,windSpeed",  
        "dataNature": "forecast",  
        "data": [  
          {  
            "observedAt": "2024-11-30T02:00:00",  
            "waveDir": 120,  
            "wavePeakDir": 100,  
            "waveHeight": 1.2,  
            "significantWaveHeight": 0.0,  
            "wavePeakPeriod": 0.0,  
            "windSpeed": 2.16,  
            "windDir": 61,  
            "currentSpeed": 2.53,  
            "currentDir": 122.0,  
            "peakDateTime": "",  
            "peakType": "",  
            "peakHeight": 0.0,  
            "tideHeight": 2.65,  
            "tideHeight10mValues": [  
              2.8984904,  
              2.870916,  
              2.8378513,  
              2.7995095,  
              2.7561383,  
              2.7080173  
            ]  
          },  
          {  
            "observedAt": "2024-11-30T03:00:00",  
            "waveDir": 120,  
            "wavePeakDir": 100,  
            "waveHeight": 1.2,  
            "significantWaveHeight": 0.0,  
            "wavePeakPeriod": 0.0,  
            "windSpeed": 2.16,  
            "windDir": 61,  
            "currentSpeed": 2.53,  
            "currentDir": 122.0,  
            "peakDateTime": "",  
            "peakType": "",  
            "peakHeight": 0.0,  
            "tideHeight": 2.65,  
            "tideHeight10mValues": [  
              2.65,  
              2.59,  
              2.53,  
              2.47,  
              2.4,  
              2.33  
            ]  
          }  
        ]  
      }  
    ]  
  }  
}  
```  
</details>  
#### Exemple de clés-valeurs Metocean NGSI-LD    
Voici un exemple de Metocean au format JSON-LD en tant que clés-valeurs. Cela est compatible avec NGSI-LD lors de l'utilisation de `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Metocean:urn:mrn:eshuv:iot:measures:20250819",  
  "type": "Metocean",  
  "fromDate": "2025-08-19T13:00:00Z",  
  "toDate": "2025-08-22T13:10:00Z",  
  "source": "PDPH/PCM/...",  
  "collectionName": "10-min-metocean-measures",  
  "modifiedAt": "2025-08-19T13:07:46Z",  
  "points": [  
    {  
      "pointCode": 12,  
      "pointName": "reviroA",  
      "pointType": "current-meter",  
      "variables": "currentSpeed,currentDir,tideHeight",  
      "dataNature": "measure",  
      "data": [  
        {  
          "observedAt": "2024-11-30T01:03:00Z",  
          "currentSpeed": 2.24,  
          "currentDir": 170,  
          "tideHeight": 2.24  
        },  
        {  
          "observedAt": "2024-11-30T02:12:00Z",  
          "currentSpeed": 2.24,  
          "currentDir": 170,  
          "tideHeight": 2.24  
        }  
      ]  
    },  
    {  
      "pointCode": 13,  
      "pointName": "canal-ext",  
      "pointType": "current-meter",  
      "variables": "currentSpeed,currentDir",  
      "dataNature": "measure",  
      "data": [  
        {  
          "observedAt": "2024-11-30T01:03:00Z",  
          "currentSpeed": 2.24,  
          "currentDir": 170,  
          "tideHeight": 2.24  
        },  
        {  
          "observedAt": "2024-11-30T02:12:00Z",  
          "currentSpeed": 2.0,  
          "currentDir": 100,  
          "tideHeight": 2.34  
        }  
      ]  
    },  
    {  
      "pointCode": 301,  
      "pointName": "mareografo-1",  
      "pointType": "wave-gauge",  
      "variables": "waveDir,wavePeakDir,waveHeight,significantWaveHeight,wavePeakPeriod",  
      "dataNature": "measure",  
      "data": [  
        {  
          "observedAt": "2024-11-30T01:00:00Z",  
          "waveDir": 0.0,  
          "wavePeakDir": 0.0,  
          "waveHeight": 0.0,  
          "significantWaveHeight": 0.0,  
          "wavePeakPeriod": 0.0  
        }  
      ]  
    },  
    {  
      "pointCode": 5231001,  
      "pointName": "Muelle Levante",  
      "pointType": "cma-prediction",  
      "variables": "height,peakDate,currentSpeed,peakHeight,peakType,waveHeightM,waveDir,windSpeed",  
      "dataNature": "forecast",  
      "data": [  
        {  
          "observedAt": "2024-11-30T02:00:00",  
          "waveDir": 120,  
          "wavePeakDir": 100,  
          "waveHeight": 1.2,  
          "significantWaveHeight": 0.0,  
          "wavePeakPeriod": 0.0,  
          "windSpeed": 2.16,  
          "windDir": 61,  
          "currentSpeed": 2.53,  
          "currentDir": 122.0,  
          "peakDateTime": "",  
          "peakType": "",  
          "peakHeight": 0.0,  
          "tideHeight": 2.65,  
          "tideHeight10mValues": [  
            2.8984904,  
            2.870916,  
            2.8378513,  
            2.7995095,  
            2.7561383,  
            2.7080173  
          ]  
        },  
        {  
          "observedAt": "2024-11-30T03:00:00",  
          "waveDir": 120,  
          "wavePeakDir": 100,  
          "waveHeight": 1.2,  
          "significantWaveHeight": 0.0,  
          "wavePeakPeriod": 0.0,  
          "windSpeed": 2.16,  
          "windDir": 61,  
          "currentSpeed": 2.53,  
          "currentDir": 122.0,  
          "peakDateTime": "",  
          "peakType": "",  
          "peakHeight": 0.0,  
          "tideHeight": 2.65,  
          "tideHeight10mValues": [  
            2.65,  
            2.59,  
            2.53,  
            2.47,  
            2.4,  
            2.33  
          ]  
        }  
      ]  
    },  
    {  
      "pointCode": 5231003,  
      "pointName": "Muelle Levante",  
      "pointType": "cma-prediction",  
      "variables": "height,peakDate,currentSpeed,peakHeight,peakType,waveHeightM,waveDir,windSpeed",  
      "dataNature": "forecast",  
      "data": [  
        {  
          "observedAt": "2024-11-30T02:00:00",  
          "waveDir": 120,  
          "wavePeakDir": 100,  
          "waveHeight": 1.2,  
          "significantWaveHeight": 0.0,  
          "wavePeakPeriod": 0.0,  
          "windSpeed": 2.16,  
          "windDir": 61,  
          "currentSpeed": 2.53,  
          "currentDir": 122.0,  
          "peakDateTime": "",  
          "peakType": "",  
          "peakHeight": 0.0,  
          "tideHeight": 2.65,  
          "tideHeight10mValues": [  
            2.8984904,  
            2.870916,  
            2.8378513,  
            2.7995095,  
            2.7561383,  
            2.7080173  
          ]  
        },  
        {  
          "observedAt": "2024-11-30T03:00:00",  
          "waveDir": 120,  
          "wavePeakDir": 100,  
          "waveHeight": 1.2,  
          "significantWaveHeight": 0.0,  
          "wavePeakPeriod": 0.0,  
          "windSpeed": 2.16,  
          "windDir": 61,  
          "tideHeight": 7.78,  
          "currentSpeed": 2.53,  
          "currentDir": 122.0,  
          "peakDateTime": "",  
          "peakType": "",  
          "peakHeight": 0.0,  
          "tideHeight": 2.65,  
          "tideHeight10mValues": [  
            2.65,  
            2.59,  
            2.53,  
            2.47,  
            2.4,  
            2.33  
          ]  
        }  
      ]  
    }  
  ],  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Exemple de Metocean NGSI-LD normalisé    
Voici un exemple de Metocean au format JSON-LD en tant que normalisé. Cela est compatible avec NGSI-LD lorsqu'aucune option n'est utilisée et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Metocean:urn:mrn:eshuv:iot:measures:20250819",  
  "type": "Metocean",  
  "fromDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2025-08-19T13:00:00Z"  
    }  
  },  
  "toDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2025-08-22T13:10:00Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "PDPH/PCM/..."  
  },  
  "collectionName": {  
    "type": "Property",  
    "value": "10-min-metocean-measures"  
  },  
  "modifiedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2025-08-19T13:07:46Z"  
    }  
  },  
  "points": {  
    "type": "Property",  
    "value": [  
      {  
        "pointCode": 12,  
        "pointName": "reviroA",  
        "pointType": "current-meter",  
        "variables": "currentSpeed,currentDir,tideHeight",  
        "dataNature": "measure",  
        "data": [  
          {  
            "observedAt": "2024-11-30T01:03:00Z",  
            "currentSpeed": 2.24,  
            "currentDir": 170,  
            "tideHeight": 2.24  
          },  
          {  
            "observedAt": "2024-11-30T02:12:00Z",  
            "currentSpeed": 2.24,  
            "currentDir": 170,  
            "tideHeight": 2.24  
          }  
        ]  
      },  
      {  
        "pointCode": 13,  
        "pointName": "canal-ext",  
        "pointType": "current-meter",  
        "variables": "currentSpeed,currentDir",  
        "dataNature": "measure",  
        "data": [  
          {  
            "observedAt": "2024-11-30T01:03:00Z",  
            "currentSpeed": 2.24,  
            "currentDir": 170,  
            "tideHeight": 2.24  
          },  
          {  
            "observedAt": "2024-11-30T02:12:00Z",  
            "currentSpeed": 2.0,  
            "currentDir": 100,  
            "tideHeight": 2.34  
          }  
        ]  
      },  
      {  
        "pointCode": 301,  
        "pointName": "mareografo-1",  
        "pointType": "wave-gauge",  
        "variables": "waveDir,wavePeakDir,waveHeight,significantWaveHeight,wavePeakPeriod",  
        "dataNature": "measure",  
        "data": [  
          {  
            "observedAt": "2024-11-30T01:00:00Z",  
            "waveDir": 0.0,  
            "wavePeakDir": 0.0,  
            "waveHeight": 0.0,  
            "significantWaveHeight": 0.0,  
            "wavePeakPeriod": 0.0  
          }  
        ]  
      },  
      {  
        "pointCode": 5231001,  
        "pointName": "Muelle Levante",  
        "pointType": "cma-prediction",  
        "variables": "height,peakDate,currentSpeed,peakHeight,peakType,waveHeightM,waveDir,windSpeed",  
        "dataNature": "forecast",  
        "data": [  
          {  
            "observedAt": "2024-11-30T02:00:00",  
            "waveDir": 120,  
            "wavePeakDir": 100,  
            "waveHeight": 1.2,  
            "significantWaveHeight": 0.0,  
            "wavePeakPeriod": 0.0,  
            "windSpeed": 2.16,  
            "windDir": 61,  
            "currentSpeed": 2.53,  
            "currentDir": 122.0,  
            "peakDateTime": "",  
            "peakType": "",  
            "peakHeight": 0.0,  
            "tideHeight": 2.65,  
            "tideHeight10mValues": [  
              2.8984904,  
              2.870916,  
              2.8378513,  
              2.7995095,  
              2.7561383,  
              2.7080173  
            ]  
          },  
          {  
            "observedAt": "2024-11-30T03:00:00",  
            "waveDir": 120,  
            "wavePeakDir": 100,  
            "waveHeight": 1.2,  
            "significantWaveHeight": 0.0,  
            "wavePeakPeriod": 0.0,  
            "windSpeed": 2.16,  
            "windDir": 61,  
            "currentSpeed": 2.53,  
            "currentDir": 122.0,  
            "peakDateTime": "",  
            "peakType": "",  
            "peakHeight": 0.0,  
            "tideHeight": 2.65,  
            "tideHeight10mValues": [  
              2.65,  
              2.59,  
              2.53,  
              2.47,  
              2.4,  
              2.33  
            ]  
          }  
        ]  
      },  
      {  
        "pointCode": 5231003,  
        "pointName": "Muelle Levante",  
        "pointType": "cma-prediction",  
        "variables": "height,peakDate,currentSpeed,peakHeight,peakType,waveHeightM,waveDir,windSpeed",  
        "dataType": "forecast",  
        "data": [  
          {  
            "observedAt": "2024-11-30T02:00:00",  
            "waveDir": 120,  
            "wavePeakDir": 100,  
            "waveHeight": 1.2,  
            "significantWaveHeight": 0.0,  
            "wavePeakPeriod": 0.0,  
            "windSpeed": 2.16,  
            "windDir": 61,  
            "currentSpeed": 2.53,  
            "currentDir": 122.0,  
            "peakDateTime": "",  
            "peakType": "",  
            "peakHeight": 0.0,  
            "tideHeight": 2.65,  
            "tideHeight10mValues": [  
              2.8984904,  
              2.870916,  
              2.8378513,  
              2.7995095,  
              2.7561383,  
              2.7080173  
            ]  
          },  
          {  
            "observedAt": "2024-11-30T03:00:00",  
            "waveDir": 120,  
            "wavePeakDir": 100,  
            "waveHeight": 1.2,  
            "significantWaveHeight": 0.0,  
            "wavePeakPeriod": 0.0,  
            "windSpeed": 2.16,  
            "windDir": 61,  
            "currentSpeed": 2.53,  
            "currentDir": 122.0,  
            "peakDateTime": "",  
            "peakType": "",  
            "peakHeight": 0.0,  
            "tideHeight": 2.65,  
            "tideHeight10mValues": [  
              2.65,  
              2.59,  
              2.53,  
              2.47,  
              2.4,  
              2.33  
            ]  
          }  
        ]  
      }  
    ]  
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