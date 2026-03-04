<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Bollard  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/Bollard/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Ce modèle de données décrit un bollard dans une installation portuaire, utilisé pour l'amarrage des navires.**  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] Si il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modes</sub></sup>  
- `address[object]` : L'adresse postale. Modèle : [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]` : Le pays. Par exemple, Espagne. Modèle : [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]` : La localité où se trouve l'adresse de la rue, et qui se trouve dans la région. Modèle : [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]` : La région où se trouve la localité, et qui se trouve dans le pays. Modèle : [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]` : Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local    
	- `postOfficeBoxNumber[string]` : Le numéro de boîte postale pour les adresses de boîte postale. Par exemple, 03578. Modèle : [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]` : Le code postal. Par exemple, 24004. Modèle : [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]` : L'adresse de la rue. Modèle : [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]` : Numéro identifiant une propriété spécifique sur une rue publique    
- `alternateName[string]` : Un nom alternatif pour cet élément  - `areaServed[string]` : La zone géographique où un service ou un élément proposé est fourni. Modèle : [https://schema.org/Text](https://schema.org/Text)- `bollardIndex[number]` : Numéro d'index du bollard dans l'installation.  - `code[string]` : Code identifiant le bollard.  - `dataProvider[string]` : Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisée  - `dateCreated[date-time]` : Horodatage de la création de l'entité. Cela sera généralement alloué par la plate-forme de stockage  - `dateModified[date-time]` : Horodatage de la dernière modification de l'entité. Cela sera généralement alloué par la plate-forme de stockage  - `description[string]` : Une description de cet élément  - `distanceFromPrevious[number]` : Distance en mètres depuis le bollard précédent.  - `distanceFromStart[number]` : Distance en mètres depuis le début de l'installation.  - `facilityRef[string]` : Référence à l'entité d'installation à laquelle ce bollard appartient.  - `id[*]` : Identifiant unique de l'entité  - `latitude[number]` : Coordonnée de latitude de l'emplacement du bollard.  - `location[*]` : Référence Geojson à l'élément. Il peut s'agir d'un Point, d'une LineString, d'un Polygon, d'un MultiPoint, d'un MultiLineString ou d'un MultiPolygon  - `longitude[number]` : Coordonnée de longitude de l'emplacement du bollard.  - `modifiedDate[date-time]` : Date et heure de la dernière modification de l'entité du bollard.  - `mrn[string]` : Identifiant codé MRN. Il doit être lié à l'entité d'une manière qui est bien connue des différents organismes, de la signification et de l'initiateur de l'entité, et tous les partis suivants maintiendront sa valeur d'origine. Cet identifiant doit être un identifiant UNIQUE de l'entité PortCall attribué par le système qui a créé l'entité pour la première fois. Cette URN doit être conforme à la norme MRN et IETF, en particulier RFC 2141, RFC 5234 et RFC 8141. Le format proposé est     id::='urn:mrn:eshuv:<ONSS>:portcalls:bollard:code:[0-9]+' ou où OID:= Organisation UN/LOCODE, OONSS:=Nom de l'organisation de service, 2099 l'année au cours de laquelle l'appel au port a été initié, 9999999 un identifiant unique croissant que l'émetteur de l'entité Bollard identifiera sur ses systèmes (par exemple, un identifiant de ligne SQL), par exemple urn:mrn:eshuv:portcalls:bollard:id:296 Voir [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) Dans les normes internationales, il est également connu sous le nom de [Visite du navire]  - `name[string]` : Le nom de cet élément  - `outOfOrder[boolean]` : Indique si le bollard est actuellement hors service.  - `owner[array]` : Une liste contenant une séquence de caractères codés en JSON référençant les identifiants uniques des propriétaires  - `portCode[string]` : Code du port où se trouve ce bollard.  - `probe[number]` : Profondeur d'eau à l'emplacement du bollard en mètres.  - `seeAlso[*]` : liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source[string]` : Une séquence de caractères indiquant la source d'origine des données de l'entité sous la forme d'une URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source  - `type[string]` : Type d'entité NGSI. Il doit s'agir d'un Bollard  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `bollardIndex`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Description du modèle de données des propriétés  
Classé par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>détails yaml complets</strong></summary>    
```yaml  
Bollard:    
  description: This data model describes a bollard in a port facility, used for mooring vessels.    
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
    bollardIndex:    
      description: Index number of the bollard within the facility.    
      type: number    
      x-ngsi:    
        type: Property    
    code:    
      description: Code identifying the bollard.    
      type: string    
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
    distanceFromPrevious:    
      description: Distance in meters from the previous bollard.    
      type: number    
      x-ngsi:    
        type: Property    
    distanceFromStart:    
      description: Distance in meters from the start of the facility.    
      type: number    
      x-ngsi:    
        type: Property    
    facilityRef:    
      description: Reference to the facility entity this bollard belongs to.    
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
    latitude:    
      description: Latitude coordinate of the bollard location.    
      type: number    
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
      description: Longitude coordinate of the bollard location.    
      type: number    
      x-ngsi:    
        type: Property    
    modifiedDate:    
      description: Date and time of last modification of the bollard entity.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    mrn:    
      description: MRN coded identifier. It has to be related to the entity in a way that is well-known by different organisms the meaning and the initiator of the entity, and all next parties will maintain on its original value. This identifier must be an UNIQUE identifier of the PortCall entity assigned by the system who created on first the entity. This URN should Conforms MRN & IETF specifically RFC 2141, RFC 5234, and RFC 8141. The propossed format is     id::='urn:mrn:eshuv:<ONSS>:portcalls:bollard:code:[0-9]+' or where OID:= Organisation UN/LOCODE, OONSS:=Organization Name of Service, 2099 the year on which the portcall was initiated, 9999999 an increasing, unique identifier that the issuer of the Bollard entity will identify on his sistems (i.e. a SQL row-id), i.e. urn:mrn:eshuv:portcalls:bollard:id:296 See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)In international standards is also known as [Ship's Visit]    
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
    outOfOrder:    
      description: Indicates if the bollard is currently out of order.    
      type: boolean    
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
    portCode:    
      description: Code of the port where this bollard is located.    
      type: string    
      x-ngsi:    
        type: Property    
    probe:    
      description: Water depth at the bollard location in meters.    
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
    source:    
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be Bollard    
      enum:    
        - Bollard    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - bollardIndex    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/Bollard/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/Bollard/schema.json    
  x-model-tags: ESHUV    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles    
#### Exemple de clés-valeurs Bollard NGSI-v2    
Voici un exemple de Bollard au format JSON en tant que clés-valeurs. Cela est compatible avec NGSI-v2 lors de l'utilisation de `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:facilities:bollard:id:20",  
  "type": "Bollard",  
  "portCode": "ESVLC",  
  "facilityRef": "urn:mrn:eshuv:facilities:facility:code:20",  
  "code": "1",  
  "bollardIndex": 4,  
  "probe": 12.5,  
  "distanceFromPrevious": 15.0,  
  "distanceFromStart": 132.2,  
  "latitude": 37.2614,  
  "longitude":  -6.9447,  
  "outOfOrder": false  
}  
```  
</details>  
#### Exemple de Bollard NGSI-v2 normalisé    
Voici un exemple de Bollard au format JSON en tant que normalisé. Cela est compatible avec NGSI-v2 lorsqu'aucune option n'est utilisée et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:facilities:bollard:id:20",  
  "type": "Bollard",  
  "portCode": {  
    "type": "Text",  
    "value": "ESVLC"  
  },  
  "facilityRef": {  
    "type": "Text",  
    "value": "urn:mrn:eshuv:facilities:facility:code:20"  
  },  
  "code": {  
    "type": "Text",  
    "value": "1"  
  },  
  "bollardIndex": {  
    "type": "Number",  
    "value": 4  
  },  
  "probe": {  
    "type": "Number",  
    "value": 12.5  
  },  
  "distanceFromPrevious": {  
    "type": "Number",  
    "value": 15.0  
  },  
  "distanceFromStart": {  
    "type": "Number",  
    "value": 132.2  
  },  
  "latitude": {  
    "type": "Number",  
    "value": 37.2614  
  },  
  "longitude": {  
    "type": "Number",  
    "value": -6.9447  
  },  
  "outOfOrder": {  
    "type": "Boolean",  
    "value": false  
  }  
}  
```  
</details>  
#### Exemple de clés-valeurs Bollard NGSI-LD    
Voici un exemple de Bollard au format JSON-LD en tant que clés-valeurs. Cela est compatible avec NGSI-LD lors de l'utilisation de `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Bollard:urn:mrn:eshuv:facilities:bollard:id:20",  
  "type": "Bollard",  
  "portCode": "ESVLC",  
  "facilityRef": "urn:mrn:eshuv:facilities:facility:code:20",  
  "code": "1",  
  "bollardIndex": 4,  
  "probe": 12.5,  
  "distanceFromPrevious": 15.0,  
  "distanceFromStart": 132.2,  
  "latitude": 37.2614,  
  "longitude": -6.9447,  
  "outOfOrder": false,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Exemple de Bollard NGSI-LD normalisé    
Voici un exemple de Bollard au format JSON-LD en tant que normalisé. Cela est compatible avec NGSI-LD lorsqu'aucune option n'est utilisée et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Bollard:urn:mrn:eshuv:facilities:bollard:id:20",  
  "type": "Bollard",  
  "portCode": {  
    "type": "Property",  
    "value": "ESVLC"  
  },  
  "facilityRef": {  
    "type": "Property",  
    "value": "urn:mrn:eshuv:facilities:facility:code:20"  
  },  
  "code": {  
    "type": "Property",  
    "value": "1"  
  },  
  "bollardIndex": {  
    "type": "Property",  
    "value": 4  
  },  
  "probe": {  
    "type": "Property",  
    "value": 12.5  
  },  
  "distanceFromPrevious": {  
    "type": "Property",  
    "value": 15.0  
  },  
  "distanceFromStart": {  
    "type": "Property",  
    "value": 132.2  
  },  
  "latitude": {  
    "type": "Property",  
    "value": 37.2614  
  },  
  "longitude": {  
    "type": "Property",  
    "value": -6.9447  
  },  
  "outOfOrder": {  
    "type": "Property",  
    "value": false  
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
