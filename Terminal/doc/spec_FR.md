<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Terminal  
================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/Terminal/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Ce modèle de données décrit un terminal dans un port comme une jonction d'installations et de terrains, qui peut être utilisé pour diverses opérations maritimes.**  
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
- `alternateName[string]`: Un nom alternatif pour cet élément  - `areaServed[string]`: La zone géographique où un service ou un élément proposé est fourni  . Modèle : [https://schema.org/Text](https://schema.org/Text)- `code[string]`: Code identifiant le terminal  - `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisée  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Cela sera généralement alloué par la plate-forme de stockage  - `dateModified[date-time]`: Horodatage de la dernière modification de l'entité. Cela sera généralement alloué par la plate-forme de stockage  - `description[string]`: Une description de cet élément  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un multipoint, d'une multiligne ou d'un multipolygone  - `mrn[string]`: Identifiant codé MRN. Il doit être lié à l'entité d'une manière bien connue des différents organismes, de la signification et de l'initiateur de l'entité, et toutes les parties suivantes conserveront sa valeur d'origine. Cet identifiant doit être un identifiant UNIQUE de l'entité PortCall attribué par le système qui l'a créé en premier. Cette URN doit être conforme aux normes MRN et IETF, en particulier RFC 2141, RFC 5234 et RFC 8141. Le format proposé est id::='urn:mrn:eshuv:<ONSS>:portcalls:terminal:code:[A-Z0-9]+' ou  . où OID:= Organisation UN/LOCODE, OONSS:=Nom de l'organisation de service, 2099 l'année au cours de laquelle l'appel au port a été initié, 9999999 un identifiant unique croissant que l'émetteur de l'entité Terminal identifiera sur ses systèmes (par exemple, un identifiant de ligne SQL), . par exemple urn:mrn:eshuv:portcalls:terminal:id:4 . Voir [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)Dans les normes internationales, il est également connu sous le nom de [Visite du navire]  - `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères codés en JSON référençant les identifiants uniques des propriétaires  - `portCode[string]`: Code du port où se trouve ce terminal  - `remarks[string]`: Remarques ou notes supplémentaires sur le terminal  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source[string]`: Une séquence de caractères donnant la source d'origine des données de l'entité sous la forme d'une URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source  - `tafTsiLocationCode[string]`: Code d'emplacement TAF-TSI pour l'identification secondaire du terminal  - `terminal[string]`: Nom du terminal  - `type[string]`: Type d'entité NGSI. Il doit s'agir d'un terminal  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `code`  - `id`  - `portCode`  - `terminal`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Description du modèle de données des propriétés  
Classées par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>détails yaml complets</strong></summary>    
```yaml  
Terminal:    
  description: This data model describes a terminal in a port as a join of facilities and ground, which can be used for various maritime operations.    
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
      description: Code identifying the terminal    
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
    mrn:    
      description: MRN coded identifier. It has to be related to the entity in a way that is well-known by different organisms the meaning and the initiator of the entity, and all next parties will maintain on its original value. This identifier must be an UNIQUE identifier of the PortCall entity assigned by the system who created on first the entity. This URN should Conforms MRN & IETF specifically RFC 2141, RFC 5234, and RFC 8141. The proposed format is id::='urn:mrn:eshuv:<ONSS>:portcalls:terminal:code:[A-Z0-9]+' or  . where OID:= Organisation UN/LOCODE, OONSS:=Organization Name of Service, 2099 the year on which the portcall was initiated, 9999999 an increasing, unique identifier that the issuer of the Terminal entity will identify on his systems (i.e. a SQL row-id), . i.e. urn:mrn:eshuv:portcalls:terminal:id:4 . See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)In international standards is also known as [Ship's Visit]    
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
    portCode:    
      description: Code of the port where this terminal is located    
      type: string    
      x-ngsi:    
        type: Property    
    remarks:    
      description: Additional remarks or notes about the terminal    
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
    tafTsiLocationCode:    
      description: TAF-TSI location code for secondary identification of the terminal    
      type: string    
      x-ngsi:    
        type: Property    
    terminal:    
      description: Name of the terminal    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be Terminal    
      enum:    
        - Terminal    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - portCode    
    - terminal    
    - code    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/Terminal/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/Terminal/schema.json    
  x-model-tags: ESHUV    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles    
#### Exemple de Terminal NGSI-v2 en valeurs clés    
Voici un exemple d'un Terminal au format JSON en valeurs clés. Cela est compatible avec NGSI-v2 lors de l'utilisation de `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:facilities:terminal:id:20",  
  "type": "Terminal",  
  "mrn": "urn:mrn:eshuv:facilities:terminal:id:20",  
  "portCode": "ESVLC",  
  "terminal": "Levante Pesquero",  
  "code": "LEV",  
  "remarks": "Fishing terminal",  
  "tafTsiLocationCode": "XXXxxxx TAF-TSI label localizacion secundaria de la terminal"  
}  
```  
</details>  
#### Exemple de Terminal NGSI-v2 normalisé    
Voici un exemple d'un Terminal au format JSON normalisé. Cela est compatible avec NGSI-v2 lors de l'utilisation sans options et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:facilities:terminal:id:20",  
  "type": "Terminal",  
  "mrn": {  
    "type": "Text",  
    "value": "urn:mrn:eshuv:facilities:terminal:id:20"  
  },  
  "portCode": {  
    "type": "Text",  
    "value": "ESVLC"  
  },  
  "terminal": {  
    "type": "Text",  
    "value": "Levante Pesquero"  
  },  
  "code": {  
    "type": "Text",  
    "value": "LEV"  
  },  
  "remarks": {  
    "type": "Text",  
    "value": "Fishing terminal"  
  },  
  "tafTsiLocationCode": {  
    "type": "Text",  
    "value": "XXXxxxx TAF-TSI label localizacion secundaria de la terminal"  
  }  
}  
```  
</details>  
#### Exemple de Terminal NGSI-LD en valeurs clés    
Voici un exemple d'un Terminal au format JSON-LD en valeurs clés. Cela est compatible avec NGSI-LD lors de l'utilisation de `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Terminal:urn:mrn:eshuv:facilities:terminal:id:20",  
  "type": "Terminal",  
  "mrn": "urn:mrn:eshuv:facilities:terminal:id:20",  
  "portCode": "ESVLC",  
  "terminal": "Levante Pesquero",  
  "code": "LEV",  
  "remarks": "Fishing terminal",  
  "tafTsiLocationCode": "XXXxxxx TAF-TSI label localizacion secundaria de la terminal",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Exemple de Terminal NGSI-LD normalisé    
Voici un exemple d'un Terminal au format JSON-LD normalisé. Cela est compatible avec NGSI-LD lors de l'utilisation sans options et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Terminal:urn:mrn:eshuv:facilities:terminal:id:20",  
  "type": "Terminal",  
  "mrn": {  
    "type": "Property",  
    "value": "urn:mrn:eshuv:facilities:terminal:id:20"  
  },  
  "portCode": {  
    "type": "Property",  
    "value": "ESVLC"  
  },  
  "terminal": {  
    "type": "Property",  
    "value": "Levante Pesquero"  
  },  
  "code": {  
    "type": "Property",  
    "value": "LEV"  
  },  
  "remarks": {  
    "type": "Property",  
    "value": "Fishing terminal"  
  },  
  "tafTsiLocationCode": {  
    "type": "Property",  
    "value": "XXXxxxx TAF-TSI label localizacion secundaria de la terminal"  
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
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
