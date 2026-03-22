<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : NavigationSector  
========================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/NavigationSector/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Ce modèle de données décrit un secteur de navigation dans un port, y compris les limites géographiques et les détails opérationnels**  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] Si il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modes</sub></sup>  
- `address[object]` : L'adresse postale. Modèle : [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]` : Le pays. Par exemple, l'Espagne. Modèle : [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]` : La localité où se trouve l'adresse de la rue, et qui se trouve dans la région. Modèle : [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]` : La région où se trouve la localité, et qui se trouve dans le pays. Modèle : [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]` : Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local    
	- `postOfficeBoxNumber[string]` : Le numéro de boîte postale pour les adresses de boîte postale. Par exemple, 03578. Modèle : [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]` : Le code postal. Par exemple, 24004. Modèle : [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]` : L'adresse de la rue. Modèle : [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]` : Numéro identifiant une propriété spécifique sur une rue publique    
- `alternateName[string]` : Un nom alternatif pour cet élément  - `areaServed[string]` : La zone géographique où un service ou un élément offert est fourni. Modèle : [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]` : Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisée  - `dateCreated[date-time]` : Horodatage de la création de l'entité. Cela sera généralement alloué par la plate-forme de stockage  - `dateModified[date-time]` : Horodatage de la dernière modification de l'entité. Cela sera généralement alloué par la plate-forme de stockage  - `description[string]` : Une description de cet élément  - `id[*]` : Identifiant unique de l'entité  - `location[*]` : Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un multipoint, d'une multiligne ou d'un multipolygone  - `minProbe[number]` : Profondeur d'eau minimale en mètres dans le secteur  - `minProbeDate[date-time]` : Date à laquelle la profondeur minimale a été enregistrée pour la dernière fois  - `modifiedDate[date-time]` : Date et heure de la dernière modification de l'entité du secteur de navigation  - `mrn[string]` : Identifiant codé MRN. Il doit être lié à l'entité d'une manière qui est bien connue des différents organismes, de la signification et de l'initiateur de l'entité, et toutes les parties suivantes maintiendront sa valeur d'origine. Cet identifiant doit être un identifiant unique de l'entité PortCall attribué par le système qui a créé l'entité pour la première fois. Cette URN doit être conforme à la norme MRN et IETF, en particulier RFC 2141, RFC 5234 et RFC 8141.   
    Le format proposé est   
    id::='urn:mrn:eshuv:<ONSS>:portcalls:navigationsector:id:[0-9]+' ou    
    où OID:= Organisation UN/LOCODE, OONSS:=Nom de l'organisation de service, 2099 l'année au cours de laquelle l'appel au port a été initié, 9999999 un identifiant unique croissant que l'émetteur de l'entité Bollard identifiera sur ses systèmes (par exemple, un ID de ligne SQL),   
    par exemple urn:mrn:eshuv:portcalls:navigationsector:id:16   
     Voir [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) pour obtenir une réponse sur la façon de traiter les unités de magnitude  - `name[string]` : Le nom de cet élément  - `navigationArea[string]` : La zone de navigation plus large où se trouve ce secteur  - `navigationSector[string]` : Identifiant du secteur de navigation dans le port  - `owner[array]` : Une liste contenant une séquence de caractères codés en JSON référençant les ID uniques des propriétaires  - `portCode[string]` : Code du port où se trouve ce secteur de navigation  - `rank[number]` : Niveau de rang ou de priorité du secteur de navigation  - `remarks[string]` : Remarques ou notes supplémentaires sur le secteur de navigation  - `sectorType[string]` : Type de secteur de navigation  - `seeAlso[*]` : liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source[string]` : Une séquence de caractères donnant la source d'origine des données de l'entité sous la forme d'une URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source  - `type[string]` : Type d'entité NGSI. Il doit s'agir de NavigationSector  <!-- /30-PropertiesList -->  
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
NavigationSector:    
  description: This data model describes a navigation sector in a port, including geographic boundaries and operational details    
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
    minProbe:    
      description: Minimum depth of water in meters within the sector    
      type: number    
      x-ngsi:    
        type: Property    
    minProbeDate:    
      description: Date when the minimum depth was last recorded    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    modifiedDate:    
      description: Date and time of last modification of the navigation sector entity    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    mrn:    
      description: "MRN coded identifier. It has to be related to the entity in a way that is well-known by different organisms the meaning and the initiator of the entity, and all next parties will maintain on its origianl value. This identifier must be an UNIQUE identifier of the PortCall entity assigned by the system who created on first the entity. This URN should Conforms MRN & IETF specifically RFC 2141, RFC 5234, and RFC 8141. \n    The propossed format is \n    id::='urn:mrn:eshuv:<ONSS>:portcalls:navigationsector:id:[0-9]+' or  \n    where OID:= Organisation UN/LOCODE, OONSS:=Organization Name of Service, 2099 the year on which the portcall was initiated, 9999999 an increasing, unique identifier that the issuer of the Bollard entity will identify on his sistems (i.e. a SQL row-id), \n    i.e. urn:mrn:eshuv:portcalls:navigationsector:id:16 \n     See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)In international standards is also known as [Ship's Visit]"    
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
    navigationArea:    
      description: The broader navigation area where this sector is situated    
      type: string    
      x-ngsi:    
        type: Property    
    navigationSector:    
      description: Identifier for the navigation sector within the port    
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
      description: Code of the port where this navigation sector is located    
      type: string    
      x-ngsi:    
        type: Property    
    rank:    
      description: Rank or priority level of the navigation sector    
      type: number    
      x-ngsi:    
        type: Property    
    remarks:    
      description: Additional remarks or notes about the navigation sector    
      type: string    
      x-ngsi:    
        type: Property    
    sectorType:    
      description: Type of navigation sector    
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
    type:    
      description: NGSI Entity type. It has to be NavigationSector    
      enum:    
        - NavigationSector    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/NavigationSector/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/NavigationSector/schema.json    
  x-model-tags: ESHUV    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles    
#### Exemple de clés-valeurs NGSI-v2 pour NavigationSector    
Voici un exemple de NavigationSector au format JSON en tant que clés-valeurs. Cela est compatible avec NGSI-v2 lors de l'utilisation de `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:facilities:navigationsector:id:10",  
  "type": "NavigationSector",  
  "portCode": "ESVLC",  
  "navigationSector": "S95",  
  "navigationArea": "AEXT",  
  "rank": 1,  
  "sectorType": "AEXT",  
  "minProbe": 99.0,  
  "minProbeDate": "2022-01-01T00:00:00",  
  "remarks": "Monoboya de crudo",  
  "location": {  
    "type": "Polygon",  
    "coordinates": [  
      [  
        [  
          -3.703790,  
          40.416775  
        ],  
        [  
          -3.703790,  
          40.426775  
        ],  
        [  
          -3.693790,  
          40.426775  
        ],  
        [  
          -3.693790,  
          40.416775  
        ]  
      ]  
    ]  
  }  
}  
```  
</details>  
#### Exemple de NavigationSector NGSI-v2 normalisé    
Voici un exemple de NavigationSector au format JSON en tant que normalisé. Cela est compatible avec NGSI-v2 lorsqu'aucune option n'est utilisée et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:facilities:navigationsector:id:10",  
  "type": "NavigationSector",  
  "portCode": {  
    "type": "Text",  
    "value": "ESVLC"  
  },  
  "navigationSector": {  
    "type": "Text",  
    "value": "S95"  
  },  
  "navigationArea": {  
    "type": "Text",  
    "value": "AEXT"  
  },  
  "rank": {  
    "type": "Number",  
    "value": 1  
  },  
  "sectorType": {  
    "type": "Text",  
    "value": "AEXT"  
  },  
  "minProbe": {  
    "type": "Number",  
    "value": 99.0  
  },  
  "minProbeDate": {  
    "type": "DateTime",  
    "value": "2022-01-01T00:00:00"  
  },  
  "remarks": {  
    "type": "Text",  
    "value": "Monoboya de crudo"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [  
        [  
          [  
            -3.70379,  
            40.416775  
          ],  
          [  
            -3.70379,  
            40.426775  
          ],  
          [  
            -3.69379,  
            40.426775  
          ],  
          [  
            -3.69379,  
            40.416775  
          ]  
        ]  
      ]  
    }  
  }  
}  
```  
</details>  
#### Exemple de clés-valeurs NGSI-LD pour NavigationSector    
Voici un exemple de NavigationSector au format JSON-LD en tant que clés-valeurs. Cela est compatible avec NGSI-LD lors de l'utilisation de `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:NavigationSector:urn:mrn:eshuv:facilities:navigationsector:id:10",  
  "type": "NavigationSector",  
  "portCode": "ESVLC",  
  "navigationSector": "S95",  
  "navigationArea": "AEXT",  
  "rank": 1,  
  "sectorType": "AEXT",  
  "minProbe": 99.0,  
  "minProbeDate": "2022-01-01T00:00:00",  
  "remarks": "Monoboya de crudo",  
  "location": {  
    "type": "Polygon",  
    "coordinates": [  
      [  
        [  
          -3.703790,  
          40.416775  
        ],  
        [  
          -3.703790,  
          40.426775  
        ],  
        [  
          -3.693790,  
          40.426775  
        ],  
        [  
          -3.693790,  
          40.416775  
        ]  
      ]  
    ]  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Exemple de NavigationSector NGSI-LD normalisé    
Voici un exemple de NavigationSector au format JSON-LD en tant que normalisé. Cela est compatible avec NGSI-LD lorsqu'aucune option n'est utilisée et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:NavigationSector:urn:mrn:eshuv:facilities:navigationsector:id:10",  
  "type": "NavigationSector",  
  "portCode": {  
    "type": "Property",  
    "value": "ESVLC"  
  },  
  "navigationSector": {  
    "type": "Property",  
    "value": "S95"  
  },  
  "navigationArea": {  
    "type": "Property",  
    "value": "AEXT"  
  },  
  "rank": {  
    "type": "Property",  
    "value": 1  
  },  
  "sectorType": {  
    "type": "Property",  
    "value": "AEXT"  
  },  
  "minProbe": {  
    "type": "Property",  
    "value": 99.0  
  },  
  "minProbeDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-01-01T00:00:00"  
    }  
  },  
  "remarks": {  
    "type": "Property",  
    "value": "Monoboya de crudo"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [  
        [  
          [  
            -3.70379,  
            40.416775  
          ],  
          [  
            -3.70379,  
            40.426775  
          ],  
          [  
            -3.69379,  
            40.426775  
          ],  
          [  
            -3.69379,  
            40.416775  
          ]  
        ]  
      ]  
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
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
