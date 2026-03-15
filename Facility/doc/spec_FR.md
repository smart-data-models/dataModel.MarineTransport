<!-- 10-Header -->  
 
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
 
Entité : Installation  
================ 
<!-- /10-Header -->  
 
<!-- 15-License -->  
 
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/Facility/LICENSE.md)  
 
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
 
<!-- 20-Description -->  
 
Description globale : **Ce modèle de données décrit une installation dans un port, qui peut inclure des postes d'amarrage, des terminaux ou d'autres infrastructures portuaires.**  
 
version : 0.0.1  
<!-- /20-Description -->  
 
<!-- 30-PropertiesList -->  
 

## Liste des propriétés  

 
<sup><sub>[*] Si il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modes</sub></sup>  
- `address[object]` : L'adresse postale. Modèle : [https://schema.org/address](https://schema.org/address)  
	- `addressCountry[string]` : Le pays. Par exemple, l'Espagne. Modèle : [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]` : La localité dans laquelle se trouve l'adresse de la rue, et qui se trouve dans la région. Modèle : [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]` : La région dans laquelle se trouve la localité, et qui se trouve dans le pays. Modèle : [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]` : Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local    
	- `postOfficeBoxNumber[string]` : Le numéro de boîte postale pour les adresses de boîte postale. Par exemple, 03578. Modèle : [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]` : Le code postal. Par exemple, 24004. Modèle : [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]` : L'adresse de la rue. Modèle : [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]` : Numéro identifiant une propriété spécifique sur une rue publique    
- `alternateName[string]` : Un nom alternatif pour cet élément   
- `areaServed[string]` : La zone géographique où un service ou un élément proposé est fourni. Modèle : [https://schema.org/Text](https://schema.org/Text)  
- `bollardCodes[array]` : Liste des codes de bollard disponibles dans l'installation.   
- `closed[boolean]` : Indique si l'installation est actuellement fermée.   
- `dataProvider[string]` : Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisée   
- `dateCreated[date-time]` : Horodatage de la création de l'entité. Cela sera généralement alloué par la plate-forme de stockage   
- `dateModified[date-time]` : Horodatage de la dernière modification de l'entité. Cela sera généralement alloué par la plate-forme de stockage   
- `deadweight[number]` : Port en lourd maximum des navires autorisés dans l'installation.   
- `description[string]` : Une description de cet élément   
- `displacement[number]` : Déplacement maximum autorisé dans l'installation.   
- `facilityCode[string]` : Code identifiant l'installation.   
- `facilityName[string]` : Nom de l'installation.   
- `facilityType[string]` : Type d'installation, tel que POSTE D'AMARRAGE, TERMINAL, etc.   
- `firstBollard[number]` : Premier identifiant de bollard dans l'installation.   
- `id[*]` : Identifiant unique de l'entité   
- `lastBollard[number]` : Dernier identifiant de bollard dans l'installation.   
- `latitude[['number', 'null']]` : Coordonnée de latitude de l'emplacement de l'installation.   
- `location[*]` : Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un multi-point, d'un multi-ligne ou d'un multi-polygone   
- `longitude[number]` : Coordonnée de longitude de l'emplacement de l'installation.   
- `maxBeam[number]` : Largeur de la coque maximale des navires autorisés en mètres.   
- `maxDraught[number]` : Tirant d'eau maximum autorisé en mètres.   
- `maxLoa[number]` : Longueur hors tout (LHT) maximale des navires autorisés en mètres.   
- `minimumProbe[number]` : Profondeur minimale de l'installation en mètres.   
- `minimumProbeDate[date-time]` : Date à laquelle la profondeur minimale a été enregistrée pour la dernière fois.   
- `modifiedDate[date-time]` : Date et heure de la dernière modification de l'entité d'installation.   
- `mrn[string]` : Identifiant codé MRN. Il doit être lié à l'entité d'une manière qui est bien connue des différents organismes, de la signification et de l'initiateur de l'entité, et toutes les parties suivantes maintiendront sa valeur d'origine. Cet identifiant doit être un identifiant UNIQUE de l'entité d'appel de port attribué par le système qui a créé l'entité pour la première fois. Cette URN doit être conforme à la norme MRN et à l'IETF, en particulier aux RFC 2141, RFC 5234 et RFC 8141.   
    Le format proposé est   
    id::='urn:mrn:eshuv:<ONSS>:portcalls:facility:code:[0-9]+' ou    
    où OID:= Organisation UN/LOCODE, OONSS:=Nom de l'organisation de service, 2099 l'année au cours de laquelle l'appel de port a été initié, 9999999 un identifiant unique croissant que l'émetteur de l'entité d'installation identifiera sur ses systèmes (par exemple, un identifiant de ligne SQL),   
    par exemple urn:mrn:eshuv:portcalls:facility:id:196   
     Voir [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) Dans les normes internationales, il est également connu sous le nom de [Visite du navire]   
- `name[string]` : Le nom de cet élément   
- `navigationSector[string]` : Secteur de navigation associé à cette installation.   
- `owner[array]` : Une liste contenant une séquence de caractères codés en JSON référençant les identifiants uniques des propriétaires   
- `planningGroup[string]` : Groupe de planification auquel appartient l'installation.   
- `portCode[string]` : Code du port où se trouve cette installation.   
- `remarks[string]` : Remarques ou notes supplémentaires sur l'installation.   
- `seeAlso[*]` : liste d'uri pointant vers des ressources supplémentaires sur l'élément   
- `source[string]` : Une séquence de caractères indiquant la source d'origine des données de l'entité sous la forme d'une URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source   
- `terminal[string]` : Nom du terminal associé à cette installation.   
- `terminalRef[string]` : Référence à l'entité de terminal associée à cette installation.   
- `type[string]` : Type d'entité NGSI. Il doit s'agir d'une installation   
<!-- /30-PropertiesList -->  
 
<!-- 35-RequiredProperties -->  
 
Propriétés requises  
- `id`   
- `portCode`   
- `type`   
<!-- /35-RequiredProperties -->  
 
<!-- 40-NotesYaml -->  
 
<!-- /40-NotesYaml -->  
 
<!-- 50-DataModelHeader -->  
 
## Description du modèle de données des propriétés  
 
Classées par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
 
<!-- 60-ModelYaml -->  
 
<details><summary><strong>détails yaml complets</strong></summary>    
 
```yaml  
Facility:    
  description: This data model describes a facility in a port, which may include berths, terminals, or other port infrastructure.    
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
    bollardCodes:    
      description: List of bollard codes available at the facility.    
      items:    
        description: Any element in the list of bollard codes available at the facility.    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    closed:    
      description: Indicates if the facility is currently closed.    
      type: boolean    
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
    deadweight:    
      description: Maximum deadweight of vessels allowed in the facility.    
      type: number    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    displacement:    
      description: Maximum displacement allowed in the facility.    
      type: number    
      x-ngsi:    
        type: Property    
    facilityCode:    
      description: Code identifying the facility.    
      type: string    
      x-ngsi:    
        type: Property    
    facilityName:    
      description: Name of the facility.    
      type: string    
      x-ngsi:    
        type: Property    
    facilityType:    
      description: Type of facility, such as BERTH, TERMINAL, etc.    
      enum:    
        - BERTH    
        - TERMINAL    
        - ANCHORAGE    
        - OTHER    
      type: string    
      x-ngsi:    
        type: Property    
    firstBollard:    
      description: First bollard identifier in the facility.    
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
    lastBollard:    
      description: Last bollard identifier in the facility.    
      type: number    
      x-ngsi:    
        type: Property    
    latitude:    
      description: Latitude coordinate of the facility location.    
      type:    
        - number    
        - 'null'    
      x-ngsi:    
        type: Property    
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
    longitude:    
      description: Longitude coordinate of the facility location.    
      type: number    
      x-ngsi:    
        type: Property    
    maxBeam:    
      description: Maximum beam width of vessels allowed in meters.    
      type: number    
      x-ngsi:    
        type: Property    
    maxDraught:    
      description: Maximum draught allowed in meters.    
      type: number    
      x-ngsi:    
        type: Property    
    maxLoa:    
      description: Maximum length overall (LOA) of vessels allowed in meters.    
      type: number    
      x-ngsi:    
        type: Property    
    minimumProbe:    
      description: Minimum depth of the facility in meters.    
      type: number    
      x-ngsi:    
        type: Property    
    minimumProbeDate:    
      description: Date when the minimum depth was last recorded.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    modifiedDate:    
      description: Date and time of last modification of the facility entity.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    mrn:    
      description: "MRN coded identifier. It has to be related to the entity in a way that is well-known by different organisms the meaning and the initiator of the entity, and all next parties will maintain on its origianl value. This identifier must be an UNIQUE identifier of the PortCall entity assigned by the system who created on first the entity. This URN should Conforms MRN & IETF specifically RFC 2141, RFC 5234, and RFC 8141. \n    The propossed format is \n    id::='urn:mrn:eshuv:<ONSS>:portcalls:facility:code:[0-9]+' or  \n    where OID:= Organisation UN/LOCODE, OONSS:=Organization Name of Service, 2099 the year on which the portcall was initiated, 9999999 an increasing, unique identifier that the issuer of the Facility entity will identify on his sistems (i.e. a SQL row-id), \n    i.e. urn:mrn:eshuv:portcalls:facility:id:196 \n     See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)In international standards is also known as [Ship's Visit]"    
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
    navigationSector:    
      description: Navigation sector associated with this facility.    
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
    planningGroup:    
      description: Planning group to which the facility belongs.    
      type: string    
      x-ngsi:    
        type: Property    
    portCode:    
      description: Code of the port where this facility is located.    
      type: string    
      x-ngsi:    
        type: Property    
    remarks:    
      description: Additional remarks or notes about the facility.    
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
    terminal:    
      description: Name of the terminal associated with this facility.    
      type: string    
      x-ngsi:    
        type: Property    
    terminalRef:    
      description: Reference to the terminal entity associated with this facility.    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be Facility    
      enum:    
        - Facility    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - portCode    
    - type    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/Facility/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/Facility/schema.json    
  x-model-tags: ESHUV    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
 
<!-- 70-MiddleNotes -->  
 
<!-- /70-MiddleNotes -->  
 
<!-- 80-Examples -->  
 
## Exemples de charges utiles    
 
#### Exemple de clés-valeurs de l'installation NGSI-v2    
 
Voici un exemple d'une installation au format JSON en tant que clés-valeurs. Cela est compatible avec NGSI-v2 lors de l'utilisation de `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    
 
```json  
{  
  "id": "urn:mrn:eshuv:facilities:facility:code:20",  
  "type": "Facility",  
  "portCode": "ESVLC",  
  "facilityName": "Levante pesquero",  
  "facilityCode": "0011",  
  "facilityType": "BERTH",  
  "terminal": "Levante",  
  "terminalRef": "urn:mrn:eshuv:infrastructure:terminal:code:20",  
  "planningGroup": "Levante",  
  "navigationSector": "CINT",  
  "minimumProbe": 2.4,  
  "minimumProbeDate": "2024-12-01T00:00:00",  
  "displacement": 103500.00,  
  "latitude": 37.252290,  
  "longitude": -6.958843,  
  "deadweight": 35000.00,  
  "maxDraught": 4.0,  
  "maxLoa": 240.0,  
  "maxBeam": 36.50,  
  "remarks": "Levante pesquero",  
  "firstBollard": 1,  
  "lastBollard": 34,  
  "closed": false,  
  "bollardCodes" : [ "1", "2", "3", "4", "5" ]  
}  
```  
</details>  
 
#### Exemple de l'installation NGSI-v2 normalisé    
 
Voici un exemple d'une installation au format JSON en tant que normalisé. Cela est compatible avec NGSI-v2 lorsqu'aucune option n'est utilisée et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    
 
```json  
{  
  "id": "urn:mrn:eshuv:facilities:facility:code:20",  
  "type": "Facility",  
  "portCode": {  
    "type": "Text",  
    "value": "ESVLC"  
  },  
  "facilityName": {  
    "type": "Text",  
    "value": "Levante pesquero"  
  },  
  "facilityCode": {  
    "type": "Text",  
    "value": "0011"  
  },  
  "facilityType": {  
    "type": "Text",  
    "value": "BERTH"  
  },  
  "terminal": {  
    "type": "Text",  
    "value": "Levante"  
  },  
  "terminalRef": {  
    "type": "Text",  
    "value": "urn:mrn:eshuv:infrastructure:terminal:code:20"  
  },  
  "planningGroup": {  
    "type": "Text",  
    "value": "Levante"  
  },  
  "navigationSector": {  
    "type": "Text",  
    "value": "CINT"  
  },  
  "minimumProbe": {  
    "type": "Number",  
    "value": 2.4  
  },  
  "minimumProbeDate": {  
    "type": "DateTime",  
    "value": "2024-12-01T00:00:00"  
  },  
  "displacement": {  
    "type": "Number",  
    "value": 103500.0  
  },  
  "latitude": {  
    "type": "Number",  
    "value": 37.25229  
  },  
  "longitude": {  
    "type": "Number",  
    "value": -6.958843  
  },  
  "deadweight": {  
    "type": "Number",  
    "value": 35000.0  
  },  
  "maxDraught": {  
    "type": "Number",  
    "value": 4.0  
  },  
  "maxLoa": {  
    "type": "Number",  
    "value": 240.0  
  },  
  "maxBeam": {  
    "type": "Number",  
    "value": 36.5  
  },  
  "remarks": {  
    "type": "Text",  
    "value": "Levante pesquero"  
  },  
  "firstBollard": {  
    "type": "Number",  
    "value": 1  
  },  
  "lastBollard": {  
    "type": "Number",  
    "value": 34  
  },  
  "closed": {  
    "type": "Boolean",  
    "value": false  
  },  
  "bollardCodes": {  
    "type": "Array",  
    "value": [  
      "1",  
      "2",  
      "3",  
      "4",  
      "5"  
    ]  
  }  
}  
```  
</details>  
 
#### Exemple de clés-valeurs de l'installation NGSI-LD    
 
Voici un exemple d'une installation au format JSON-LD en tant que clés-valeurs. Cela est compatible avec NGSI-LD lors de l'utilisation de `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    
 
```json  
{  
  "id": "urn:ngsi-ld:Facility:urn:mrn:eshuv:facilities:facility:code:20",  
  "type": "Facility",  
  "portCode": "ESVLC",  
  "facilityName": "Levante pesquero",  
  "facilityCode": "0011",  
  "facilityType": "BERTH",  
  "terminal": "Levante",  
  "terminalRef": "urn:mrn:eshuv:infrastructure:terminal:code:20",  
  "planningGroup": "Levante",  
  "navigationSector": "CINT",  
  "minimumProbe": 2.4,  
  "minimumProbeDate": "2024-12-01T00:00:00",  
  "displacement": 103500.0,  
  "latitude": 37.25229,  
  "longitude": -6.958843,  
  "deadweight": 35000.0,  
  "maxDraught": 4.0,  
  "maxLoa": 240.0,  
  "maxBeam": 36.5,  
  "remarks": "Levante pesquero",  
  "firstBollard": 1,  
  "lastBollard": 34,  
  "closed": false,  
  "bollardCodes": [  
    "1",  
    "2",  
    "3",  
    "4",  
    "5"  
  ],  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```  
</details>  
 
#### Exemple de l'installation NGSI-LD normalisé    
 
Voici un exemple d'une installation au format JSON-LD en tant que normalisé. Cela est compatible avec NGSI-LD lorsqu'aucune option n'est utilisée et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    
 
```json  
{  
  "id": "urn:ngsi-ld:Facility:urn:mrn:eshuv:facilities:facility:code:20",  
  "type": "Facility",  
  "portCode": {  
    "type": "Property",  
    "value": "ESVLC"  
  },  
  "facilityName": {  
    "type": "Property",  
    "value": "Levante pesquero"  
  },  
  "facilityCode": {  
    "type": "Property",  
    "value": "0011"  
  },  
  "facilityType": {  
    "type": "Property",  
    "value": "BERTH"  
  },  
  "terminal": {  
    "type": "Property",  
    "value": "Levante"  
  },  
  "terminalRef": {  
    "type": "Property",  
    "value": "urn:mrn:eshuv:infrastructure:terminal:code:20"  
  },  
  "planningGroup": {  
    "type": "Property",  
    "value": "Levante"  
  },  
  "navigationSector": {  
    "type": "Property",  
    "value": "CINT"  
  },  
  "minimumProbe": {  
    "type": "Property",  
    "value": 2.4  
  },  
  "minimumProbeDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-12-01T00:00:00"  
    }  
  },  
  "displacement": {  
    "type": "Property",  
    "value": 103500.0  
  },  
  "latitude": {  
    "type": "Property",  
    "value": 37.25229  
  },  
  "longitude": {  
    "type": "Property",  
    "value": -6.958843  
  },  
  "deadweight": {  
    "type": "Property",  
    "value": 35000.0  
  },  
  "maxDraught": {  
    "type": "Property",  
    "value": 4.0  
  },  
  "maxLoa": {  
    "type": "Property",  
    "value": 240.0  
  },  
  "maxBeam": {  
    "type": "Property",  
    "value": 36.5  
  },  
  "remarks": {  
    "type": "Property",  
    "value": "Levante pesquero"  
  },  
  "firstBollard": {  
    "type": "Property",  
    "value": 1  
  },  
  "lastBollard": {  
    "type": "Property",  
    "value": 34  
  },  
  "closed": {  
    "type": "Property",  
    "value": false  
  },  
  "bollardCodes": {  
    "type": "Property",  
    "value": [  
      "1",  
      "2",  
      "3",  
      "4",  
      "5"  
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
 
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la manière de traiter les unités de magnitude  
<!-- /95-Units -->  
 
<!-- 97-LastFooter -->  
 
---  
 
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
 
--- FIN DU DOCUMENT ---