<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Navire-mère  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/MasterVessel/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Le modèle de données est destiné à fournir des informations sur les navires. Il permet de représenter les propriétés de chaque navire : informations statiques et dynamiques**.  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.    
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numéro identifiant une propriété spécifique sur une voie publique    
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `beam[number]`: Poutre du navire  . Model: [https://schema.org/Number](https://schema.org/Number)- `buildDate[date]`: Date de construction du navire représentée par un format ISO 8601 UTC  . Model: [https://schema.org/Text](https://schema.org/Text)- `callSign[string]`: Signal d'identification d'un navire lors de la première connexion par radio [EMSWe : DE-065-05] [EDI : BGM-RFF] [S211 : Nom d'appel / Indicatif d'appel] [OMI : IMO0136].  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `dwt[number]`: Poids mort Tonnage (DWT)  . Model: [https://schema.org/Number](https://schema.org/Number)- `financialOwner[string]`: Propriétaire financier du navire  . Model: [https://schema.org/Text](https://schema.org/Text)- `flagCode[string]`: Code international des pavillons (ISO 3166-1 alfa-2)  . Model: [https://schema.org/Text](https://schema.org/Text)- `gt[number]`: Tonnage brut (GT)  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identifiant unique de l'entité  - `imo[number]`: Numéro de l'Organisation maritime internationale (un UID global pour toujours) [EMSWe : DE-003-03] [EDIFACT:TDT-8213] [IALA_S211:vesselId] [IMO:IMO0140].  . Model: [https://schema.org/Number](https://schema.org/Number)- `loa[number]`: Longueur sur toute la longueur du navire  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `manager[string]`: Gestionnaire du navire, généralement la compagnie maritime  . Model: [https://schema.org/Text](https://schema.org/Text)- `maxDraught[number]`: Tirant d'eau maximal du navire  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxLoadVehicle[number]`: Capacité maximale du navire à transporter des véhicules  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxPassenger[number]`: Capacité maximale du navire à transporter des passagers  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVehicle[number]`: Dimensions maximales du véhicule autorisées  . Model: [https://schema.org/Number](https://schema.org/Number)- `minNumOfCrew[number]`: Nombre minimum d'équipage pour exploiter le navire  . Model: [https://schema.org/Number](https://schema.org/Number)- `mmsi[number]`: Numéro d'identité du service mobile maritime (un UID temporairement attribué, délivré par l'État du pavillon actuel de cet objet) [EMSWe : DE-068-09] [EDIFACT:TDT-1131] [IALA_S211:vesselId] [IMO:IMO0178]  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `photo[uri]`: URL de la photo du navire  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `sleeve[number]`: Manche du navire  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `technicalManager[string]`: Responsable technique du navire  . Model: [https://schema.org/Text](https://schema.org/Text)- `toBow[number]`: Dimension de l'arc  . Model: [http://schema.org/Number](http://schema.org/Number)- `toPort[number]`: Dimension au port  . Model: [http://schema.org/Number](http://schema.org/Number)- `toStardboard[number]`: Dimension à tribord  . Model: [http://schema.org/Number](http://schema.org/Number)- `toStern[number]`: Dimension à la poupe  . Model: [http://schema.org/Number](http://schema.org/Number)- `type[string]`: Type d'entité NGSI. Il doit s'agir de MasterVessel  - `vesselClass[string]`: Code de la classe du navire. Enum : "BD=Vrac sec ; BO=Huilier / vraquier ; BS=Déchargement du vraquier ; BY=Autres types de vraquiers ; FC=Bateau de pêche ; FO=Navire. transfert et/ou transp. ; GA=Navire. RO-RO avec passagers ; GC=Mrcia général sans spécialisation ; GD=Rest navires de charge générale ; GE=Buq. transp. combiné ; GN=Navire conteneur ; GO=Navire roulier ; GP=Navire à passagers ; GR=Navire frigorifique ; OO=Buq. ou artefact. float be ; OS=Navires de ravitaillement ; TC=Transport de produits. produits chimiques ; TD=autre vrac liquide ; TL=transport de gaz liquéfié ; TO=pétrolier ; XD=dragues ; XR=Recherche et exploration ; XT=pousseurs ; XX=autres navires et bateaux ; UR=Fast Pass ; G=marchandises générales ; T=transporteurs de vrac liquide (citernes) ; S=transporteurs de vrac solide ; OB=autres navires marchands ; UC=billet de croisière ; OC=navires de pêche en haute mer (congélateurs);'  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselName[string]`: Nom du navire. [EMSWe : DE-003-07] [EDIFACT:TDT-8212] [IMO:IMO0142]  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselOwner[string]`: Propriétaire du navire  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselSubType[number]`: Enum :0=Non disponible (par défaut),1-19=Réservé pour une utilisation future,20=Aile au sol (WIG), tous les navires de ce type,21=Aile au sol (WIG), catégorie de danger A,22=Aile au sol (WIG), Catégorie dangereuse B,23=Aile au sol (WIG), Catégorie dangereuse C,24=Aile au sol (WIG), Catégorie dangereuse D,25-29=Aile au sol (WIG), Réservé pour un usage futur,30=Pêche,31=Travailleur,32=Travailleur : longueur supérieure à 200m ou largeur supérieure à 25m,33=Dragage ou opérations sous-marines,34=Opérations de plongée,35=Opérations militaires,36=Voile,37=Bateaux de plaisance,38-39=Réservé,40=Bateaux à grande vitesse (HSC), tous les navires de ce type,41=Bateaux à grande vitesse (HSC), catégorie de danger A,42=Bateaux à grande vitesse (HSC), catégorie de danger B,43=Bateaux à grande vitesse (HSC), catégorie de danger C,44=Bateau à grande vitesse (HSC), Catégorie dangereuse D,45-48=Bateau à grande vitesse (HSC), Réservé pour une utilisation future,49=Bateau à grande vitesse (HSC), Pas d'information supplémentaire,50=Bateau pilote,51=Bateau de recherche et de sauvetage,52=Tug,53=Barge portuaire,54=Équipement anti-pollution,55=Réglementation,56-57=Navire local de rechange,58=Transport médical,59=Navire non-combattant selon la Résolution RR No. 18,60=Passagers, tous les navires de ce type,61=Passagers, catégorie de danger A,62=Passagers, catégorie de danger B,63=Passagers, catégorie de danger C,64=Passagers, catégorie de danger D,65-68=Passagers, Réservé pour une utilisation future,69=Passagers, Pas d'information supplémentaire,70=Cargo, tous les navires de ce type,71=Cargo, catégorie dangereuse A,72=Cargo, catégorie dangereuse B,73=Cargo, catégorie dangereuse C,74=Cargo, catégorie dangereuse D,75-78=Cargo, réservé pour une utilisation future,79=Cargo, pas d'information supplémentaire,80=Tanker, tous les navires de ce type,81=Citerne, catégorie dangereuse A,82=Citerne, catégorie dangereuse B,83=Citerne, catégorie dangereuse C,84=Citerne, catégorie dangereuse D,85-88=Citerne, Réservé pour une utilisation future,89=Citerne, Pas d'information supplémentaire,90=Autre type, tous les navires de ce type,91=autre type, catégorie de danger A,92=autre type, catégorie de danger B,93=autre type, catégorie de danger C,94=autre type, catégorie de danger D,95-98=autre type, réservé pour une utilisation future,99=autre type, pas d'information supplémentaire". Code pour le sous-type de navire  . Model: [https://schema.org/Number](https://schema.org/Number)- `vesselType[number]`: Enum : "1=Réservé,2=Aile au sol,3=Catégorie spéciale,4=Embarcation à grande vitesse,5=Catégorie spéciale,6=Passager,7=Cargo,8=Tanker,9=Autre". Code du type de navire  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
## Exemples de charges utiles  
#### MasterVessel NGSI-v2 key-values Exemple  
Voici un exemple de MasterVessel au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### MasterVessel NGSI-v2 normalisé Exemple  
Voici un exemple de MasterVessel au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec les NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### MasterVessel Valeurs clés de l'INS-LD Exemple  
Voici un exemple de MasterVessel au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### MasterVessel NGSI-LD normalisé Exemple  
Voici un exemple de MasterVessel au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
En attendant de convenir des normes d'identification de chaque champ. Pour la formation des URN, les normes suivantes sont prises en compte - SO 3166-1 - Norme internationale pour les codes de pays et les codes de leurs subdivisions. - RFC 2141 - Syntaxe URN (https://www.ietf.org/rfc/rfc2141.txt) - RFC 8141 - Uniform Resource Names (URN) (https://tools.ietf.org/html/rfc8141) - IALAs MRN Request (https://www.iana.org/assignments/urn-formal/mrn)  
<MRN> ::= "urn" " :" "mrn" " :" <OID> " :" <OSNID> " :" <OSNS> <OID> ::= (alphanum) 0*32(alphanum / "-") (alphanum) ; ID de l'organisation (c'est-à-dire ESHUV) <OSNID> ::= (alphanum) 0*32(alphanum / "-") (alphanum) ; ID de l'espace de noms spécifique à l'organisation (c.-à-d. portcalls) <OSNS> ::= pchar *(pchar / "/") ; Chaîne de l'espace de noms spécifique à l'organisation (c.-à-d. un nom de module ou de microservice). <ID> ::= un identifiant unique pour cet espace de noms (c'est-à-dire un nom d'entité suivi d'un identifiant de ligne dans une base de données SQL).  
Par exemple, urn := "urn:mrn:eshuv:portcalls:portcall:id:343"  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
