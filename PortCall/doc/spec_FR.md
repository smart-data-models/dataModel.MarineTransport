<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : PortCall  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/PortCall/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Une escale est la visite d'un navire dans le port pendant un certain temps, afin d'effectuer une fonction utile, comme le chargement ou le déchargement de marchandises**.  
version : 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `UNLOCODE[string]`: Code des Nations unies pour les lieux de commerce et de transport, [UN/LOCODE] (https://unece.org/trade/cefact/unlocode-code-list-country-and-territory), du port  - `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.    
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numéro identifiant une propriété spécifique sur une voie publique    
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrivalDate[date-time]`: Date/heure d'arrivée du navire dans la zone portuaire  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `arrivalDateScheduled[date-time]`: Date/heure prévue d'arrivée du navire dans la zone portuaire, telle que déclarée par l'agent maritime  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `departureDate[date-time]`: Date/heure de la sortie du navire de la zone portuaire  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `departureDateScheduled[date-time]`: Date/heure prévue de sortie du navire de la zone portuaire, telle que déclarée par l'agent maritime  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: Une description de l'article  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `regularLine[string]`: Ligne régulière de l'appel de port  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `status[string]`: Statut de l'opération. Enum : 'Estimé, Autorisé, Opérationnel, Achevé'  - `terminal[string]`: Terminal de l'appel de port  - `type[string]`: Type d'entité NGSI. Il doit s'agir de PortCall  - `vessel[object]`: Navire appelant de l'appel de port  	- `IMO[number]`: Numéro d'identification OMI du navire, selon le [schéma] (https://www.imo.org/en/OurWork/IIIS/Pages/IMO-Identification-Number-Schemes.aspx) défini par l'Organisation maritime internationale.    
	- `shipName[string]`: Nom du navire    
	- `shipTypeCategory[string]`: Description de la catégorie de navire. Enum : "CONTENEUR, CARGAISON GÉNÉRALE NON SPÉCIALISÉE, VRAC LIQUIDE, VRAC SÉCHÉ, CRUISE".    
	- `shipTypeClass[string]`: Description de la classe du navire. Enum : 'MULTI-DECKER, CHEMICAL TANKER, FULL CONTAINER, OIL TANKER, BULK CARRIER, LG TANKER'.    
- `vesselAgent[string]`: Agent maritime de l'appel de port  - `voyageCode[string]`: Code du voyage (identifiant unique d'un voyage)  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `arrivalDate`  - `id`  - `type`  - `vessel`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
Modèle de données du projet H2020 DataPorts. Références pour les termes inclus dans la description. IMO-> https://imocompendium.imo.org/public/IMO-Compendium/Draft/index.htm, S211-IALA -> https://www.iala-aism.org/technical/data-modelling/iala-s-200-development-status/s-211/, EDIFACT-> https://service.unece.org/trade/untdid/d20b/trmd/berman_c.htm, EMSWe -> https://eur-lex.europa.eu/EN/legal-content/summary/european-maritime-single-window-environment-emswe.html / https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32019R1239  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PortCall:    
  description: 'This data model is intended to provide information about PortCalls (the visit of a ship to a port). It allows to represent the properties of each PortCall, including the visiting Vessel (partially loaded and referenced to Vessel entity for more info). On each attribute references related to elements of other well known standards are included. The data model is intended to provide the basic information about a PortCall, that is, the data relative to the arrival and the departure of the ship from the port, but not intermediate activities (berthing, operations, ...) that are defined in other linked entities (Berth, Operation, ...)'    
  properties:    
    UNLOCODE:    
      description: 'United Nations Code for Trade and Transport Locations, [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory), of the port. to be deprecated. Use portCode instead'    
      type: string    
      x-ngsi:    
        type: Property    
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
    agentChangeDate:    
      description: "[EMSWe: -] [EDI: -] [S211: -] [IMO: -] "    
      format: date-time    
      type: string    
      x-ngsi:    
        model: 'https://schema.org/Text represented by an ISO 8601 UTC format, If a change of ship agent occurs during the PortCall, this must be not null, and contains the date and time contract of new agent (secondAgentRef)'    
        type: Property    
    agentLegalCode:    
      description: 'Legal identifier code of the PortCall''s ship Agent. [EMSWe: -] [EDI: -] [S211: -] [IMO: -] '    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    agentName:    
      description: 'The name of the Agent at Port of the ship (aka consignor). [EMSWe: DE-009-01] [EDI: NAD-3035-ZME-CV] [IMO: IMO0002]'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    arrivalDate:    
      description: Date/time of ship arrival at port area. To be deprecated. Use ata instead    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    arrivalDateScheduled:    
      description: 'Scheduled date/time of ship arrival at port area, as declared by shipping agent. To be deprecated. Use eta instead'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    ata:    
      description: 'Date and time of Actual Time of Arrival to Port (ISO 8601 UTC format). [EMSWe: DE-005-02] [IALA_S211:locationState.timeType.ACTUAL] [IMO:IMO0063]'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    atd:    
      description: 'Date and time of Actual Time of Departure  from Port.  (ISO 8601 UTC format). [IALA_S211:timeType=2] [EMSWe: DE-005-03] [IALA_S211:locationState.timeType.ACTUAL] [IMO:IMO0065] '    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    authorizationDate:    
      description: Date and time of authorization represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    authorizedBy:    
      description: 'Codes to identify which authority has approved or denied the visit of the ship. [EMSWe: DE-027-01] [EDIFACT:BGM-4443] [IMO:IMO0010]'    
      enum:    
        - PORT_AUTHORITY    
        - ARMY_AUTHORITY    
        - PORT_ARMY_AUTHORITIES    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    callSign:    
      description: 'Identification signal of a vessel when initially connecting by radio [EMSWe: DE-065-05] [EDI: BGM-RFF] [S211: Call Name / Call Sign] [IMO: IMO0136] '    
      type: string    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    crewArrival:    
      description: 'Number of crew at arrival. [EMSWe: DE-013-03] [EDIFACT:QTY-6063-ZTE] [IMO:IMO0086]'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    crewDeparture:    
      description: 'Number of crew at departure. [EMSWe: DE-013-03] [EDIFACT:QTY-6063-ZTS] [IMO:IMO0086] '    
      type: number    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dangerousGoodsCarried:    
      description: 'A ''yes/no'' indicator whether the ship is carrying any dangerous goods.[EMSWe: DE-018-02] [EDIFACT:FTX-4441-ZCD] [IMO:IMO0046]'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    dangerousGoodsLoading:    
      description: 'A ''yes/no'' indicator whether the ship is loading any dangerous goods in this port. [EMSWe: DE-018-02] [EDIFACT:FTX-4441-ZDD] [IMO:IMO0046]'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    dangerousGoodsUnloading:    
      description: 'A ''yes/no'' indicator whether the ship is unloading any dangerous goods in this port. [EMSWe: DE-018-02] [EDIFACT:FTX-4441-ZBD] [IMO:IMO0046]'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
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
    departureAuthorizationDate:    
      description: Date and time of authorization for the departure by authorities represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    departureDate:    
      description: Date/time of ship leaving port area. To be deprecated. Use atd instead    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    departureDateScheduled:    
      description: 'Scheduled date/time of ship leaving port area, as declared by shipping agent. To be deprecated. Use etd instead'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    eta:    
      description: 'Date and time of Estimated Time of Arrival to Port expected by Port Authority  (ISO 8601 UTC format). [EMSWe: DE-005-09] [EDIFACT:DTM-2005-132] [IALA_S211:locationState.timeType.ESTIMATED] [IMO:IMO0064]'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    etd:    
      description: 'Date and time of Estimated Time of Departure  from Port, expected by Port Authority  (ISO 8601 UTC format). [EMSWe: DE-005-04] [EDIFACT:DTM-2005-133] [IALA_S211:locationState.timeType.ESTIMATED] [IMO:IMO0066]'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
        type: Property    
    imo:    
      description: 'IMO ship identification number, following the [scheme](https://www.imo.org/en/OurWork/IIIS/Pages/IMO-Identification-Number-Schemes.aspx) defined by the International Maritime Organization. [EMSWe: DE-003-03] [EDIFACT:TDT-8213] [IALA_S211:vesselId] [IMO:IMO0140]'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    interiorTraffic:    
      description: ""    
      type: boolean    
      x-ngsi:    
        model: 'https://schema.org/Boolean.Indicator of interior navigation port call'    
        type: Property    
    lastPortCode:    
      description: 'Last port of call, coded.The code representing the port immediately previous to the port of arrival, if available. [EMSWe: DE-005-05] [EDIFACT:LOC-3227-92] [IMO:IMO0076] '    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
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
    manifestActivated:    
      description: ""    
      type: boolean    
      x-ngsi:    
        model: 'https://schema.org/Boolean.Indicator of the Activation of the Manifest of the Cargo, related to [MSWE: DE-036-04:Manifest number]'    
        type: Property    
    manifestActivationDate:    
      description: 'Date and time of approval of the cargo manifest. [MSWE: DE-036-04:Manifest number]'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    masterName:    
      description: 'Name of master [EMSWe: DE-053-01] [EDIFACT:NAD-3035-ZME] [IMO:IMO0083]'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    mmsi:    
      description: 'Marine Mobile Service Identity Number (a temporarily assigned UID, issued by that object''s current flag state)[EMSWe: DE-068-09] [EDIFACT:TDT-1131] [IALA_S211:vesselId] [IMO:IMO0178]'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    mrn:    
      description: 'MRN coded identifier. It has to be related to the entity in a way that is well-known by different organisms the meaning and the initiator of the entity, and all next parties will maintain on its original value. This identifier must be an UNIQUE identifier of the PortCall entity assigned by the system who created on first the entity. This URN should Conforms MRN & IETF specifically RFC 2141, RFC 5234, and RFC 8141. The proposed format is id::=''urn:mrn:<OID>:<ONSS>:portcalls:portcall:id:[0-9]+'' where OID:= Organisation UN/LOCODE, OONSS:=Organization Name of Service, 9999999 an increasing, unique identifier that the issuer of the PortCall entity will identify on his systems (i.e. a SQL row-id), i.e. urn:mrn:eshuv:portcalls:portcall:id:19002. See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)In international standards is also known as [Ship''s Visit]'    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    nextPortCode:    
      description: 'Next port of call, coded.The code representing the port immediately previous to the port of arrival, if available.. Related to IALA_S211:nestPortCallCod / IMO. [EMSWe: DE-005-07] [EDIFACT:LOC-3227-61] [IMO:IMO0120]'    
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
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    passengersArrival:    
      description: 'Number of passengers at arrival. [EMSWe: DE-013-02] [EDIFACT:QTY-6063-ZPE] [IMO:IMO0087].'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    passengersDeparture:    
      description: 'Number of passengers at departure. [EMSWe: DE-013-02] [EDIFACT:QTY-6063-ZPS] [IMO:IMO0087]'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    portCallNumber:    
      description: 'Port call identifier in MRN format. First element of the NSS should be the 5 character UN/Locode of the port, later the YEAR and finishing with a sequential number in this port [LLLLLYYYY99999] where LLLLL is the UN/LOCODE of the visited port, YYYY is the year, and 99999 is a unique sequential number assigned by port authority unique on each year (i.e. ESHUV202310323). An abbreviation can be used for UN/LOCODE (i.e. H202310323).  The portCallNumber is assigned during the initial steps of the visit, but could be null at the beginning. In international standards is also known as [Port Call ID], [Visit ID] or [Port Call Coded]. See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) [EMSWe: DG-004/DG-004-01] [EDIFACT:BGM-1004] [IALA_S211:portCallId] [IMO:IMO108+IMO0153]'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    portCode:    
      description: 'United Nations Code for Trade and Transport Locations. See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) [EMSWe: DE-004-04] [EDIFACT:LOC-3227-153] [IALA_S211:portCode] [IMO:IMO0108]'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    pta:    
      description: 'Date and time of Planned Time of Arrival to Port by Port Authority Berthing Plan  (ISO 8601 UTC format). [EDIFACT:DTM-2005-155] [IALA_S211:locationState.timeType.PLANNED] [IMO:IMO0235]'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    ptd:    
      description: 'Date and time of Planned Time of Departure  from Port, planned by Port Authority Berthing Plan  (ISO 8601 UTC format). [EDI: DTM-2005-156] [S211: locationState.timeType.PLANNED] [IMO: IMO0236]'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    regularLine:    
      description: 'Name of the regular line if any. [EMSWe: DE-004-02] [EDIFACT:-] [IMO:-]'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    remarks:    
      description: 'Comments about this PortCall by the Porth Authority. [EMSWe: DE-038-01] [EDIFACT:FTX-4440-AAI] [IALA_S211:comment] [IMO: IMO0196]'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    rta:    
      description: 'Date and time of Requested Time of Arrival to Port. Requested by Consignee to Port Authority  (ISO 8601 UTC format). [EDIFACT:DTM-2005-178] [IALA_S211:locationState.timeType.REQUIRED] [IMO:IMO0234]'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    rtd:    
      description: 'Date and time of Requested Time of Departure from Port. Requested by Consignee to Port Authority  (ISO 8601 UTC format). [EDIFACT:DTM-2005-189] [IALA_S211:locationState.timeType.REQUIRED] [IMO:IMO0237]'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    secondAgentLegalCode:    
      description: 'Legal identifier code of the PortCall''s ship Agent. [EMSWe: -] [EDI: -] [S211: -] [IMO: -] '    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    secondAgentName:    
      description: 'The name of the new Agent at Port of the Sipping Line and usually the consignor or the load. [EMSWe: DE-009-01] [EDI: NAD-3035-ZME-CV] [IMO: IMO0002] '    
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
    shipName:    
      description: Name of the vessel    
      type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    status:    
      description: 'Current status of the PortCall in its lifetime, from request to authorization by port and civil authorities and completion. [EMSWe: DE-019-07] [EDIFACT:BGM-1225] [IALA_S211:serviceState: timeSequence:VESSEL]. Enum:''ACCEPTED, AUTHORIZED, CANCELLED, COMPLETED, DENIED, ESTIMATED, INITIATED, REQUESTED, REJECTED, INVOICING, INVOICED, OPERATIONAL'''    
      enum:    
        - ACCEPTED    
        - AUTHORIZED    
        - CANCELLED    
        - COMPLETED    
        - DENIED    
        - ESTIMATED    
        - INITIATED    
        - REQUESTED    
        - REJECTED    
        - INVOICING    
        - INVOICED    
        - OPERATIONAL    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    terminal:    
      description: 'Name of the terminal [EMSWe:-] [EDIFACT:-] [IMO:-]'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be PortCall    
      enum:    
        - PortCall    
      type: string    
      x-ngsi:    
        type: Property    
    vessel:    
      description: 'Calling vessel of the portcall. To be deprecated. Use individual attributes IMO, vesselTypeCategory, vesselTypeCategory, vesselName. To be deprecated in this object'    
      properties:    
        imo:    
          description: 'IMO ship identification number, following the [scheme](https://www.imo.org/en/OurWork/IIIS/Pages/IMO-Identification-Number-Schemes.aspx) defined by the International Maritime Organization. [EMSWe: DE-003-03] [EDIFACT:TDT-8213] [IALA_S211:vesselId] [IMO:IMO0140]. To be deprecated in this object'    
          type: number    
          x-ngsi:    
            model: https://schema.org/Number    
            type: Property    
        shipName:    
          description: Name of the vessel. To To be deprecated in this object    
          type: string    
          x-ngsi:    
            type: Property    
        shipTypeCategory:    
          description: 'Description of vessel category. Enum: ''CONTAINER, GENERAL CARGO NON SPECIALIZED, LIQUID BULK, DRY BULK, CRUISE''. To be deprecated in this object'    
          enum:    
            - CONTAINER    
            - GENERAL CARGO NON SPECIALIZED    
            - LIQUID BULK    
            - DRY BULK    
            - CRUISE    
          type: string    
          x-ngsi:    
            type: Property    
        shipTypeClass:    
          description: 'Description of vessel class. Enum: ''MULTI-DECKER, CHEMICAL TANKER, FULL CONTAINER, OIL TANKER, BULK CARRIER, LG TANKER''. To be deprecated in this object'    
          enum:    
            - MULTI-DECKER    
            - CHEMICAL TANKER    
            - FULL CONTAINER    
            - OIL TANKER    
            - BULK CARRIER    
            - LG TANKER    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    vesselAgent:    
      description: Vessel Agent of the portcall. To be deprecated. Use agentName instead    
      type: string    
      x-ngsi:    
        type: Property    
    vesselName:    
      description: 'Name of the Vessel. [EMSWe: DE-003-07] [EDIFACT:TDT-8212] [IMO:IMO0142]'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vesselRef:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: 'Identifier format of any NGSI entity in MRN format [NGSI-MarineTransport.PortCallVessel.id'    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Related PortCallVessel with all fields loaded with further info. Reference to MarineTransport.MasterVessel/schema.json    
      x-ngsi:    
        type: Relationship    
    vesselTypeCategory:    
      description: 'Description of vessel category. Enum: ''CONTAINER, GENERAL CARGO NON SPECIALIZED, LIQUID BULK, DRY BULK, CRUISE'''    
      enum:    
        - CONTAINER    
        - GENERAL CARGO NON SPECIALIZED    
        - LIQUID BULK    
        - DRY BULK    
        - CRUISE    
      type: string    
      x-ngsi:    
        type: Property    
    vesselTypeClass:    
      description: 'Description of vessel class. Enum: ''MULTI-DECKER, CHEMICAL TANKER, FULL CONTAINER, OIL TANKER, BULK CARRIER, LG TANKER'''    
      enum:    
        - MULTI-DECKER    
        - CHEMICAL TANKER    
        - FULL CONTAINER    
        - OIL TANKER    
        - BULK CARRIER    
        - LG TANKER    
      type: string    
      x-ngsi:    
        type: Property    
    voyageCode:    
      description: Voyage code (unique ID of a voyage). To be deprecated. Use voyageNumber instead    
      type: string    
      x-ngsi:    
        type: Property    
    voyageNumber:    
      description: 'Number of voyage. [EMSWe: DE-004-02] [EDIFACT:-] [IMO:-]'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    wasteAgreementExists:    
      description: 'All waste delivery indicator. Waste collection paid indicator. Exists agreement with Port Authority for waste discharge and treatment. [EDIFACT:FTX-4441-ZRS/ZRL] [IALA_S211:locationReferenceObject. SLUDGE_VESSEL]'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
  required:    
    - id    
    - type    
    - eta    
    - status    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2024 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/PortCall/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/PortCall/schema.json    
  x-model-tags: 'ESHUV, i4trust'    
  x-version: 0.1.0    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### PortCall NGSI-v2 valeurs-clés Exemple  
Voici un exemple d'appel de port au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "$af4345f234525$",  
  "mrn": "urn:mrn:eshuv:portcalls:portcall:id:941",  
  "type": "PortCall",  
  "portCode": "ESVLC",  
  "portCallNumber": "ESHUV202301296",  
  "regularLine": "BALE: CITY1 - ISLANDER",  
  "terminal": "TERMINAL ESTE, S.A.",  
  "status": "AUTHORIZED",  
  "authorizedBy": "PORT_ARMY_AUTHORITIES",  
  "authorizationDate": "2023-01-01T08:00:00.00Z",  
  "voyageNumber": "12021060223",  
  "lastPortCode": "ESBCN",  
  "nextPortCode": "NLRTM",  
  "vesselTypeCategory": "CONTAINER",  
  "vesselTypeClass": "FULL CONTAINER",  
  "vesselRef": "URI:NGSI-LD:Portcall:001",  
  "vesselName": "Acme ERC SHIP",  
  "imo": 87123445,  
  "mmsi": 210049000,  
  "callSign": "5BP-*987C3",  
  "masterName": "John Doe",  
  "wasteAgreementExists": true,  
  "dangerousGoodsCarried": true,  
  "dangerousGoodsLoading": true,  
  "dangerousGoodsUnloading": false,  
  "agentName": "Acme Consignors S.L.",  
  "agentLegalCode": "A-43242342",  
  "agentChangeDate": "2023-01-01T08:00:00",  
  "secondAgentName": "John Doe",  
  "secondAgentLegalCode": "31133133-V",  
  "manifestActivated": true,  
  "manifestActivationDate": "2023-01-01T08:00:00",  
  "interiorTraffic": false,  
  "remarks": "Fondeado hasta arreglar avería",  
  "crewArrival": 100,  
  "crewDeparture": 120,  
  "passengersArrival": 20,  
  "passengersDeparture": 25,  
  "eta": "2023-01-01T07:15:00",  
  "rta": "2023-01-01T07:30:00",  
  "pta": "2023-01-01T07:15:00",  
  "ata": "2023-01-01T08:00:00",  
  "etd": "2023-01-02T07:15:00",  
  "rtd": "2023-01-02T07:00:00",  
  "ptd": "2023-01-02T07:00:00",  
  "atd": "2023-01-02T07:00:00"  
}  
```  
</details>  
#### PortCall NGSI-v2 normalisé Exemple  
Voici un exemple d'appel de port au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "$af4345f234525$",  
  "type": "PortCall",  
  "mrn": {  
    "type": "Text",  
    "value": "urn:mrn:eshuv:portcalls:portcall:id:941"  
  },  
  "portCode": {  
    "type": "Text",  
    "value": "ESVLC"  
  },  
  "portCallNumber": {  
    "type": "Text",  
    "value": "ESHUV202301296"  
  },  
  "regularLine": {  
    "type": "Text",  
    "value": "GRIMALDI - SHORT SEA SERVICE B"  
  },  
  "terminal": {  
    "type": "Text",  
    "value": "TERMINAL ESTE, S.A."  
  },  
  "status": {  
    "type": "Text",  
    "value": "AUTHORIZED"  
  },  
  "authorizedBy": {  
    "type": "Text",  
    "value": "PORT_ARMY_AUTHORITIES"  
  },  
  "authorizationDate": {  
    "type": "Date-Time",  
    "value": "2023-01-01T08:00:00.00Z"  
  },  
  "voyageNumber": {  
    "type": "Text",  
    "value": "12021060223"  
  },  
  "lastPortCode": {  
    "type": "Text",  
    "value": "ESBCN"  
  },  
  "nextPortCode": {  
    "type": "Text",  
    "value": "NLRTM"  
  },  
  "vesselTypeCategory": {  
    "type": "Text",  
    "value": "CONTAINER"  
  },  
  "vesselTypeClass": {  
    "type": "Text",  
    "value": "FULL CONTAINER"  
  },  
  "vesselRef": {  
    "type": "Text",  
    "value": "URI:NGSI-LD:Portcall:001"  
  },  
  "vesselName": {  
    "type": "Text",  
    "value": "Acme ERC SHIP"  
  },  
  "imo": {  
    "type": "Number",  
    "value": 87123445  
  },  
  "mmsi": {  
    "type": "Number",  
    "value": 210049000  
  },  
  "callSign": {  
    "type": "Text",  
    "value": "5BP-*987C3"  
  },  
  "masterName": {  
    "type": "Text",  
    "value": "John Doe"  
  },  
  "wasteAgreementExists": {  
    "type": "boolean",  
    "value": true  
  },  
  "dangerousGoodsCarried": {  
    "type": "boolean",  
    "value": true  
  },  
  "dangerousGoodsLoading": {  
    "type": "boolean",  
    "value": true  
  },  
  "dangerousGoodsUnloading": {  
    "type": "boolean",  
    "value": false  
  },  
  "agentName": {  
    "type": "Text",  
    "value": "Acme Consignors S.L."  
  },  
  "agentLegalCode": {  
    "type": "Text",  
    "value": "A-43242342"  
  },  
  "agentChangeDate": {  
    "type": "Text",  
    "value": "2023-01-01T08:00:00"  
  },  
  "secondAgentName": {  
    "type": "Text",  
    "value": "John Doe"  
  },  
  "secondAgentLegalCode": {  
    "type": "Text",  
    "value": "31133133-V"  
  },  
  "manifestActivated": {  
    "type": "boolean",  
    "value": true  
  },  
  "manifestActivationDate": {  
    "type": "Date-Time",  
    "value": "2023-01-01T08:00:00"  
  },  
  "interiorTraffic": {  
    "type": "boolean",  
    "value": false  
  },  
  "remarks": {  
    "type": "Text",  
    "value": "Fondeado hasta arreglar aver\u00eda"  
  },  
  "crewArrival": {  
    "type": "Number",  
    "value": 100  
  },  
  "crewDeparture": {  
    "type": "Number",  
    "value": 120  
  },  
  "passengersArrival": {  
    "type": "Number",  
    "value": 20  
  },  
  "passengersDeparture": {  
    "type": "Number",  
    "value": 25  
  },  
  "eta": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:15:00"  
  },  
  "rta": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:30:00"  
  },  
  "pta": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:15:00"  
  },  
  "ata": {  
    "type": "Date-Time",  
    "value": "2023-01-01T08:00:00"  
  },  
  "etd": {  
    "type": "Date-Time",  
    "value": "2023-01-02T07:15:00"  
  },  
  "rtd": {  
    "type": "Date-Time",  
    "value": "2023-01-02T07:00:00"  
  },  
  "ptd": {  
    "type": "Date-Time",  
    "value": "2023-01-02T07:00:00"  
  },  
  "atd": {  
    "type": "Date-Time",  
    "value": "2023-01-02T07:00:00"  
  }  
}  
```  
</details>  
#### PortCall NGSI-LD key-values Exemple  
Voici un exemple d'appel de port au format JSON-LD sous forme de valeurs clés. Ce format est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:$af4345f234525$",  
  "mrn": "urn:mrn:eshuv:portcalls:portcall:id:941",  
  "type": "PortCall",  
  "portCode": "ESVLC",  
  "portCallNumber": "ESHUV202301296",  
  "regularLine": "BALE: CITY1 - ISLANDER",  
  "terminal": "TERMINAL ESTE, S.A.",  
  "status": "AUTHORIZED",  
  "authorizedBy": "PORT_ARMY_AUTHORITIES",  
  "authorizationDate": "2023-01-01T08:00:00.00Z",  
  "voyageNumber": "12021060223",  
  "lastPortCode": "ESBCN",  
  "nextPortCode": "NLRTM",  
  "vesselTypeCategory": "CONTAINER",  
  "vesselTypeClass": "FULL CONTAINER",  
  "vesselRef": "URI:NGSI-LD:Portcall:001",  
  "vesselName": "Acme ERC SHIP",  
  "imo": 87123445,  
  "mmsi": 210049000,  
  "callSign": "5BP-*987C3",  
  "masterName": "John Doe",  
  "wasteAgreementExists": true,  
  "dangerousGoodsCarried": true,  
  "dangerousGoodsLoading": true,  
  "dangerousGoodsUnloading": false,  
  "agentName": "Acme Consignors S.L.",  
  "agentLegalCode": "A-43242342",  
  "agentChangeDate": "2023-01-01T08:00:00",  
  "secondAgentName": "John Doe",  
  "secondAgentLegalCode": "31133133-V",  
  "manifestActivated": true,  
  "manifestActivationDate": "2023-01-01T08:00:00",  
  "interiorTraffic": false,  
  "remarks": "Fondeado hasta arreglar averÃ­a",  
  "crewArrival": 100,  
  "crewDeparture": 120,  
  "passengersArrival": 20,  
  "passengersDeparture": 25,  
  "eta": "2023-01-01T07:15:00",  
  "rta": "2023-01-01T07:30:00",  
  "pta": "2023-01-01T07:15:00",  
  "ata": "2023-01-01T08:00:00",  
  "etd": "2023-01-02T07:15:00",  
  "rtd": "2023-01-02T07:00:00",  
  "ptd": "2023-01-02T07:00:00",  
  "atd": "2023-01-02T07:00:00",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### PortCall NGSI-LD normalisé Exemple  
Voici un exemple d'appel de port au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:$af4345f234525$",  
  "type": "PortCall",  
  "mrn": {  
    "type": "Property",  
    "value": "urn:mrn:eshuv:portcalls:portcall:id:941"  
  },  
  "portCode": {  
    "type": "Property",  
    "value": "ESVLC"  
  },  
  "portCallNumber": {  
    "type": "Property",  
    "value": "ESHUV202301296"  
  },  
  "regularLine": {  
    "type": "Property",  
    "value": "GRIMALDI - SHORT SEA SERVICE B"  
  },  
  "terminal": {  
    "type": "Property",  
    "value": "TERMINAL ESTE, S.A."  
  },  
  "status": {  
    "type": "Property",  
    "value": "AUTHORIZED"  
  },  
  "authorizedBy": {  
    "type": "Property",  
    "value": "PORT_ARMY_AUTHORITIES"  
  },  
  "authorizationDate": {  
    "type": "Date-Time",  
    "value": "2023-01-01T08:00:00.00Z"  
  },  
  "voyageNumber": {  
    "type": "Property",  
    "value": "12021060223"  
  },  
  "lastPortCode": {  
    "type": "Property",  
    "value": "ESBCN"  
  },  
  "nextPortCode": {  
    "type": "Property",  
    "value": "NLRTM"  
  },  
  "vesselTypeCategory": {  
    "type": "Property",  
    "value": "CONTAINER"  
  },  
  "vesselTypeClass": {  
    "type": "Property",  
    "value": "FULL CONTAINER"  
  },  
  "vesselRef": {  
    "type": "Relationship",  
    "object": "URI:NGSI-LD:Portcall:001"  
  },  
  "vesselName": {  
    "type": "Property",  
    "value": "Acme ERC SHIP"  
  },  
  "imo": {  
    "type": "Property",  
    "value": 87123445  
  },  
  "mmsi": {  
    "type": "Property",  
    "value": 210049000  
  },  
  "callSign": {  
    "type": "Property",  
    "value": "5BP-*987C3"  
  },  
  "masterName": {  
    "type": "Property",  
    "value": "John Doe"  
  },  
  "wasteAgreementExists": {  
    "type": "Property",  
    "value": true  
  },  
  "dangerousGoodsCarried": {  
    "type": "Property",  
    "value": true  
  },  
  "dangerousGoodsLoading": {  
    "type": "Property",  
    "value": true  
  },  
  "dangerousGoodsUnloading": {  
    "type": "Property",  
    "value": false  
  },  
  "agentName": {  
    "type": "Property",  
    "value": "Acme Consignors S.L."  
  },  
  "agentLegalCode": {  
    "type": "Property",  
    "value": "A-43242342"  
  },  
  "agentChangeDate": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T08:00:00"  
    }  
  },  
  "secondAgentName": {  
    "type": "Property",  
    "value": "John Doe"  
  },  
  "secondAgentLegalCode": {  
    "type": "Property",  
    "value": "31133133-V"  
  },  
  "manifestActivated": {  
    "type": "Property",  
    "value": true  
  },  
  "manifestActivationDate": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T08:00:00"  
    }  
  },  
  "interiorTraffic": {  
    "type": "Property",  
    "value": false  
  },  
  "remarks": {  
    "type": "Property",  
    "value": "Fondeado hasta arreglar averia"  
  },  
  "crewArrival": {  
    "type": "Property",  
    "value": 100  
  },  
  "crewDeparture": {  
    "type": "Property",  
    "value": 120  
  },  
  "passengersArrival": {  
    "type": "Property",  
    "value": 20  
  },  
  "passengersDeparture": {  
    "type": "Property",  
    "value": 25  
  },  
  "eta": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:15:00"  
    }  
  },  
  "rta": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:30:00"  
    }  
  },  
  "pta": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:15:00"  
    }  
  },  
  "ata": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T08:00:00"  
    }  
  },  
  "etd": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-02T07:15:00"  
    }  
  },  
  "rtd": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-02T07:00:00"  
    }  
  },  
  "ptd": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-02T07:00:00"  
    }  
  },  
  "atd": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-02T07:00:00"  
    }  
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
