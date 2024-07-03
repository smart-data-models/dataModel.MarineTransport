<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Poste d'amarrage  
=========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/Berth/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Ce modèle de données est destiné à fournir des informations sur les postes d'amarrage. Nous définissons le terme "poste d'amarrage" pour chaque arrêt d'un navire lors d'une escale, à la fois pour une installation portuaire (poste d'amarrage) et pour une zone d'ancrage. Chaque poste d'amarrage a une durée d'accostage (estimée, planifiée, etc.), un cycle de vie (estimé, demandé, approuvé, etc.), une activité principale pendant l'escale (opérations commerciales, réparations majeures, etc.) et un certain nombre d'attributs décrits ci-dessous. Lorsque des opérations commerciales ont lieu, une entité Opération définira les détails de chaque opération commerciale**  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `activityCode[string]`: Activité pendant l'arrêt à quai. Il peut s'agir d'opérations de transport de marchandises ou d'un certain nombre d'activités liées aux activités portuaires du navire. Enum : ZGR=Réparation majeure ; ZPV=Provisionnement ; ZCA=Construction de chantier naval ; ZRA=Réparation majeure de chantier naval ; ZRF=Réparation à flot avec du personnel d'équipage ; ZRT=Réparation au mouillage avec du personnel autre que l'équipage ; ZDA=Mise au rebut de chantier naval ; ZTA=Transformation de chantier naval ; ZTF=Transformation ; ZVO=Visite officielle ; ZAF=Arrivée forcée ; ZIN=Inactif ; ZIP=Inactivité de pêche ; ZAR=Rapprovisionnement à quai ; ZAO=Rapprovisionnement au mouillage ; ZAB=Rapprovisionnement à quai par barge ; ZOP=Opérations portuaires du trafic commercial ; ZCT=Croisières touristiques ; ZTI=Trafic interne ; ZBO=Mise à l'eau ; ZCO=Construction ; ZRE=Navire destiné au remorquage ; ZDE=Dépotoir ; ZAP=Bateaux de pêche et bateaux artisanaux dans les opérations de chargement et de déchargement de poisson frais ; ZDR=Navire destiné au dragage ; ZPB=Arrêt biologique ; ZCL=Pas de permis ; ZDJ=Dépôt judiciaire ; ZMR=Bateau destiné au service d'amarrage ; ZPR=Bateau destiné au service de pilotage ; ZRM=Remorque ; ZVA=Accès à la cale ; ZDS=Bateau en cale sèche ; ZOT=Autre ; EST=Séjour ; ZSA=Approvisionnement en eau ; ZSH=Approvisionnement en glace ; ZSE=Approvisionnement en énergie électrique ; ZSC=Approvisionnement en carburant ; ZSV=Victuariat ;  . Model: [https://schema.org/Text](https://schema.org/Text)- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.    
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numéro identifiant une propriété spécifique sur une voie publique    
- `agentLegalCode[string]`: Code d'identification légale du navire de PortCall Agent  . Model: [https://schema.org/Text](https://schema.org/Text)- `agentName[string]`: Nom de l'agent maritime de PortCall  . Model: [https://schema.org/Text](https://schema.org/Text)- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrivalDraught[number]`: Tirant d'eau en première ligne assuré pour la navigation à l'arrivée  . Model: [https://schema.org/Number](https://schema.org/Number)- `ataBerth[date-time]`: Représentée par un format ISO 8601 UTC, Heure réelle d'arrivée au poste d'amarrage  - `atdBerth[date-time]`: Représentée par un format ISO 8601 UTC. Heure réelle de départ du poste d'amarrage  - `authorizationRemarks[string]`: Conditions d'accostage écrites par l'autorité portuaire  . Model: [https://schema.org/Text](https://schema.org/Text)- `authorizedAt[date-time]`: Représenté par un format ISO 8601 UTC, date et heure de l'autorisation par l'autorité portuaire et l'autorité maritime.  - `berthCode[string]`: Code identifiant l'installation portuaire pour cette escale du navire. Format : <oid>:berth:99999  . Model: [https://schema.org/Text](https://schema.org/Text)- `berthName[string]`: Nom de l'installation portuaire pour cette escale du navire  . Model: [https://schema.org/Text](https://schema.org/Text)- `berthingTypeCode[string]`: Codes permettant d'identifier le type d'accostage ou d'amarrage dans le port maritime de l'interface. Enum : ABV=Accostage de bâbord à navire ; ABX=Accostage de port ; AB1=Accostage de bâbord par l'avant ; AB2=Accostage de bâbord par l'arrière ; AEX=Accostage de tribord ; AX1=Accostage par l'avant ; AEV=Accostage de tribord à navire ; REM=Accostage de tribord au quai ; REX=Accostage de tribord par l'avant ; RE1=Accostage de tribord par l'avant ; RE2=Accostage de tribord par l'arrière ; RPM=Torsion orteil-ressort ; RPV=Abordé de la pointe au navire ; RPX=Point d'amarrage ; RXM=Amarrer le long d'un quai ; RXV=Abandonné à un autre navire ; RXX=Abandonné ; RX1=Enchevêtré par l'avant ; AE1=Bouclé tribord par l'avant ; AE2=Bouclé tribord par l'arrière ; APM=Abordé au quai ; APV=Abordé au navire ; APX=Accostage au point ; AXM=Accostage au quai ; AXV=Accostage au navire ; AXX=Accostage ; AX2=Accostage par l'arrière ; FBM=Accostage bâbord au quai ; FBV=Accostage bâbord au navire ; FBX=Accostage au port ; FB1=Accostage bâbord par l'avant ; FB2=Accostage bâbord par l'arrière ; FEM=Accostage tribord au quai ; FEV=Ancrage tribord au navire ; FEX=Ancrage tribord ; FE1=Ancrage tribord par l'avant ; FE2=Ancrage tribord par l'arrière ; FPM=Amarrage à la jetée ; FPV=Ancrage de la pointe au navire ; FPX=Ancrage au point ; FP1=Ancrage de la pointe par l'avant ; FP2=Ancrage de la pointe par l'arrière ; FXM=Ancrage à la jetée ; FXV=Ancrage au navire ; FX1=Ancrée par l'avant ; FX2=Ancrée par l'arrière ; RBM=Accostée au quai côté bâbord ; RBX=Battue côté bâbord ; RB1=Battue à bâbord par l'avant ; RB2=Battue à bâbord par l'arrière ; RX2=Enchevêtrée par l'arrière ; YBM=Attachée à la bouée bâbord à l'embarcadère ; YBV=Attachée à la bouée sur le côté bâbord du navire ; YBX=Attaché à la bouée bâbord ; YB1=Attaché à la bouée bâbord par l'avant ; YB2=Attaché à la bouée bâbord par l'arrière ; YEM=Attaché à la bouée tribord à l'embarcadère ; YEV=Attaché à la bouée tribord du navire ; YEX=Attaché à la bouée tribord ; YE1=Attaché à la bouée tribord par l'avant ; YE2=Attaché à la bouée tribord par l'arrière ; YPM=Attaché à la bouée d'extrémité à l'embarcadère ; YPV=Attaché à la bouée d'extrémité au navire ; YPX=Attaché à la bouée de pointe ; YP1=Attaché à la bouée de pointe par l'avant ; YP2=Attaché à la bouée de pointe par l'arrière ; YXM=Attaché à la bouée à l'embarcadère ; YXV=Attaché à la bouée au navire ; YX1=Attaché à la bouée par l'avant ; YX2=Attaché à la bouée par l'arrière ; ABM=Port amarré à la jetée ; AEM=Amarré à quai par tribord ; FXX=Ancrage ; YXX=Attaché à la bouée sans autre indication ; AP1=Abordé à la pointe par l'avant ; AP2=Abordé à l'avant et à l'arrière ; RBV=Abordé au navire par bâbord ; REV=Abordé au navire par tribord ;.   . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `departureDraught[number]`: Tirant d'eau à la dernière ligne libérée pour la navigation de départ  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: Une description de l'article  - `etaBerth[date-time]`: Représentées par un format ISO 8601 UTC, la date et l'heure de l'heure d'arrivée prévue au poste d'amarrage par l'autorité portuaire (format ISO 8601 UTC). [EMSWe : DE-005-09] [EDI : DTM-2005-132] [S211 : locationState.timeType.ESTIMATED] [IMO : IMO0064].  - `etdBerth[date-time]`: Représentées par un format ISO 8601 UTC, la date et l'heure de l'heure estimée de départ du poste d'amarrage, attendues par l'autorité portuaire. [EMSWe : DE-005-04] [EDI : DTM-2005-133] [S211 : locationState.timeType.ESTIMATED] [IMO : IMO0066].  - `firstBollard[string]`: Premier identificateur de borne dans une installation portuaire  . Model: [https://schema.org/Text](https://schema.org/Text)- `gln[number]`: ISO/IEC 6523 : "https://schema.org/Number". Code facultatif de l'emplacement. Le Global Location Number (GLN) est un numéro unique de 13 chiffres attribué aux sites pour leur permettre d'être identifiés de manière unique dans le monde entier, et attribué à n'importe quel site de la chaîne d'approvisionnement. Ces GLN peuvent être utilisés pour identifier tous les sites juridiques, physiques et fonctionnels.  - `id[*]`: Identifiant unique de l'entité  - `lastBollard[string]`: Dernier identificateur de borne dans l'installation portuaire  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `mooringLines[number]`: Nombre d'amarres.  . Model: [https://schema.org/Number](https://schema.org/Number)- `mrn[string]`: Identifiant codé MRN. Il doit être lié à l'entité d'une manière bien connue des différents organismes, la signification et l'initiateur de l'entité, et toutes les parties suivantes maintiendront sa valeur originale. Cet identifiant doit être un identifiant UNIQUE de l'entité PortCall attribué par le système qui a créé l'entité en premier. Cet URN doit être conforme au MRN et à l'IETF, en particulier aux RFC 2141, RFC 5234 et RFC 8141. Le format proposé est id::='urn:mrn:<OID>:<ONSS>:portcalls:berth:id :[0-9]+' où OID:= Organisation UN/LOCODE, OONSS:=Organisation Nom du Service, 9999999 un identifiant croissant et unique que l'émetteur de l'entité Berth identifiera sur ses systèmes (i.e. un row-id SQL), i.e. urn:mrn:eshuv:portcalls:berth:id:2024012. Voir [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory). Dans les normes internationales, il est également connu sous le nom de [Ship's Visit].  - `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `portCallNumber[string]`: Identifiant de l'appel de port  . Model: [https://schema.org/Text](https://schema.org/Text)- `portCallRef[*]`: Référence à l'entité parentale PortCall.  - `portCode[string]`: Code du port d'escale  . Model: [https://schema.org/Text](https://schema.org/Text)- `ptaBerth[date-time]`: Représentée par un format ISO 8601 UTC, l'heure prévue d'arrivée au poste d'amarrage  - `ptdBerth[date-time]`: Représentée par un format ISO 8601 UTC. Heure de départ prévue du poste d'amarrage  - `remarks[string]`: Remarques sur l'accostage, par l'agent du port ou d'autres personnes  . Model: [https://schema.org/Text](https://schema.org/Text)- `requestedAt[date-time]`: Représenté par un format ISO 8601 UTC, date et heure de la demande d'accostage par l'agent maritime.  - `rtaBerth[date-time]`: Représentée par un format ISO 8601 UTC, la date et l'heure d'arrivée demandée par l'agent maritime (format ISO 8601 UTC) [EMSWe : DE-005-09] [EDI : DTM-2005-132] [S211 : locationState.timeType.ESTIMATED] [IMO : IMO0064].  - `rtdBerth[date-time]`: Représentée par un format ISO 8601 UTC, date et heure de l'heure de départ demandée par l'agent maritime (format ISO 8601 UTC). [EMSWe : DE-005-09] [EDI : DTM-2005-132] [S211 : locationState.timeType.ESTIMATED] [IMO : IMO0064].  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `status[string]`: Statut actuel de l'accostage au cours de sa durée de vie, de la demande à l'autorisation et à l'achèvement. Enum : "ACCEPTED, AUTHORIZED, CANCELLED, COMPLETED, DENIED, INITIATED, REQUESTED, REJECTED, INVOICING, INVOICED". [EMSWe : DE-019-07] [EDI : BGM-1225] [S211 : serviceState : timeSequence:VESSEL]  . Model: [https://schema.org/Text](https://schema.org/Text)- `stopRank[number]`: Rang ou numéro de cet arrêt dans l'activité PortCall, classé par heure d'arrivée dans la séquence des arrêts (zone d'amarrage)  . Model: [https://schema.org/Number](https://schema.org/Number)- `terminal[string]`: Nom commun du terminal  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Type d'entité NGSI. Il doit s'agir d'un poste d'amarrage  - `year[number]`: Année d'entrée en vigueur de l'accostage  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `portCallRef`  - `stopRank`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
modèle de données mappé à partir de l'ontologie de l'ERA https://data-interop.era.europa.eu/era-vocabulary (Agence de l'Union européenne pour les chemins de fer)  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Berth:    
  description: 'This data model is intended to provide information about Berths. We define ''berth'' to each stop of a ship during a PortCall, both for a port-facility (berth) and as an anchorage area. Each berth has a berthing time (estimated, planned, etc.), a lifecycle (estimated, requested, approved, etc.), an main activity during the stop (commercial operations, major repair, etc.) and a number of attributes described below. When commercial operations take place, an Operation entity will define the details of each commercial operation'    
  properties:    
    activityCode:    
      description: 'Activity during the stop in berth. It can be cargo operations or a number of activities related to the ship-port activities. Enum: ZGR=Major repair; ZPV=Provisioning; ZCA=Shipyard Construction; ZRA=Major shipyard repair; ZRF=Repair afloat with crew personnel; ZRT=Repair at anchor with personnel other than the crew; ZDA=Shipyard scrapping; ZTA=Shipyard Transformation; ZTF=Transformation; ZVO=Official visit; ZAF=Forced arrival; ZIN=Inactive; ZIP=Fishing inactivity; ZAR=Provisioning at docking; ZAO=Provisioning at anchor; ZAB=Provisioning at docking by barge; ZOP=Port operations of commercial traffic; ZCT=Sightseeing cruises; ZTI=Internal traffic; ZBO=Launching; ZCO=Construction; ZRE=Vessel intended for towing service; ZDE=Scrapyard; ZAP=Fishing and artisanal vessels in loading and unloading operations of fresh fish; ZDR=Vessel intended for dredging; ZPB=Biological stoppage; ZCL=No license; ZDJ=Judicial deposit; ZMR=Vessel intended for mooring service; ZPR=Vessel intended for pilotage service; ZRM=Trailer; ZVA=Access to slipway; ZDS=Vessel in dry dock; ZOT=Other; EST=Stay; ZSA=Water Supply; ZSH=Ice Supply; ZSE=Electrical Energy Supply; ZSC=Fuel Supply; ZSV=Victualling;'    
      enum:    
        - ZGR    
        - ZPV    
        - ZCA    
        - ZRA    
        - ZRF    
        - ZRT    
        - ZDA    
        - ZTA    
        - ZTF    
        - ZVO    
        - ZAF    
        - ZIN    
        - ZIP    
        - ZAR    
        - ZAO    
        - ZAB    
        - ZOP    
        - ZCT    
        - ZTI    
        - ZBO    
        - ZCO    
        - ZRE    
        - ZDE    
        - ZAP    
        - ZDR    
        - ZPB    
        - ZCL    
        - ZDJ    
        - ZMR    
        - ZPR    
        - ZRM    
        - ZVA    
        - ZDS    
        - ZOT    
        - EST    
        - ZSA    
        - ZSH    
        - ZSE    
        - ZSC    
        - ZSV    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    agentLegalCode:    
      description: Legal identifier code of the PortCall's ship Agent    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    agentName:    
      description: Name of PortCall's ship Agent    
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
    arrivalDraught:    
      description: Draught at first-line secured for arriving navigation    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ataBerth:    
      description: 'Represented by an ISO 8601 UTC format, Actual time of arrival to Berth'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    atdBerth:    
      description: Represented by an ISO 8601 UTC format. Actual time of departure from Berth    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    authorizationRemarks:    
      description: Conditions to the berthing written by Port Authority    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    authorizedAt:    
      description: 'Represented by an ISO 8601 UTC format, Date and time of authorization by port Authority and Maritime Authority. '    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    berthCode:    
      description: 'Code identifying the port-facility for this stop of the vessel. Format: <oid>:berth:99999'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    berthName:    
      description: Name of the port-facility for this stop of the vessel    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    berthingTypeCode:    
      description: 'Codes for identifying the Type of berthing/mooring in the interface ship-port. Enum: ABV=Board port to ship; ABX=Port berthed; AB1=Bouched port by bow; AB2=Bouched port by stern; AEX=Starboard docked; AX1=Docked by bow; AEV=Board starboard to ship; REM=Boarded starboard at the pier; REX=Starboard bow; RE1=Starboard bow by bow; RE2=Cracked starboard by stern; RPM=Toe-to-spring twisting; RPV=Boarded from tip to ship; RPX=Ringed point; RXM=To moor alongside a dock; RXV=Moored to another vessel; RXX=Moored ; RX1=Tangled by bow; AE1=Bouched starboard by bow; AE2=Bouched starboard by stern; APM=Pocketed to the pier; APV=Pocket to ship; APX=Point docking; AXM=docked at the pier; AXV=Boarded to ship; AXX=docked; AX2=Docked by stern; FBM=Anchored port side at the pier; FBV=Anchored port side to ship; FBX=Port anchored; FB1=Anchored port by bow; FB2=Anchored port by stern; FEM=Anchored starboard to the pier; FEV=Anchored starboard to ship; FEX=Anchored starboard; FE1=Anchored starboard by bow; FE2=Anchored starboard by stern; FPM=Toe-to-pier mooring; FPV=Anchoring tip to ship; FPX=Point anchoring; FP1=Anchoring tip by bow; FP2=Anchoring tip by stern; FXM=Anchored at the pier; FXV=Anchored to ship; FX1=Anchored by bow; FX2=Anchored by stern; RBM=Moored portside to the dock; RBX=Battered port side; RB1=Bulked port by bow; RB2=Bulked on port side by stern; RX2=Tangled by stern; YBM=Tethered to the port buoy at the pier; YBV=Tethered to the buoy on the port side of the ship; YBX=Tethered to port buoy; YB1=Tied to port buoy by bow; YB2=Tied to port buoy by stern; YEM=Tethered to the starboard buoy at the pier; YEV=Tethered to the starboard buoy of the ship; YEX=Tethered to starboard buoy; YE1=Tied to starboard buoy by bow; YE2=Tied to starboard buoy by stern; YPM=Tethered to the end buoy at the pier; YPV=Tethered to the buoy end-to-ship; YPX=Tied to tip buoy; YP1=Tethered to tip buoy by bow; YP2=Tied to the tip buoy by stern; YXM=Tethered to the buoy at the pier; YXV=Tethered to the buoy to the ship; YX1=Tethered to buoy by bow; YX2=Tethered to buoy by stern; ABM=Port berthed to the pier; AEM=Moored starboard to dock; FXX=Anchoring; YXX=Tethered to buoy without further indication; AP1=Boarding tip by bow; AP2=Pocketed fore and aft; RBV=Bulked port to ship; REV=Wheeled starboard to ship;. '    
      enum:    
        - ABV    
        - ABX    
        - AB1    
        - AB2    
        - AEX    
        - AX1    
        - AEV    
        - REM    
        - REX    
        - RE1    
        - RE2    
        - RPM    
        - RPV    
        - RPX    
        - RXM    
        - RXV    
        - RXX    
        - RX1    
        - AE1    
        - AE2    
        - APM    
        - APV    
        - APX    
        - AXM    
        - AXV    
        - AXX    
        - AX2    
        - FBM    
        - FBV    
        - FBX    
        - FB1    
        - FB2    
        - FEM    
        - FEV    
        - FEX    
        - FE1    
        - FE2    
        - FPM    
        - FPV    
        - FPX    
        - FP1    
        - FP2    
        - FXM    
        - FXV    
        - FX1    
        - FX2    
        - RBM    
        - RBX    
        - RB1    
        - RB2    
        - RX2    
        - YBM    
        - YBV    
        - YBX    
        - YB1    
        - YB2    
        - YEM    
        - YEV    
        - YEX    
        - YE1    
        - YE2    
        - YPM    
        - YPV    
        - YPX    
        - YP1    
        - YP2    
        - YXM    
        - YXV    
        - YX1    
        - YX2    
        - ABM    
        - AEM    
        - FXX    
        - YXX    
        - AP1    
        - AP2    
        - RBV    
        - REV    
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
    departureDraught:    
      description: Draught at last-line released for departure navigation    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    etaBerth:    
      description: 'Represented by an ISO 8601 UTC format, Date and time of Estimated Time of Arrival to Berth expected by Port Authority (ISO 8601 UTC format). [EMSWe: DE-005-09] [EDI: DTM-2005-132] [S211: locationState.timeType.ESTIMATED] [IMO: IMO0064]'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    etdBerth:    
      description: 'Represented by an ISO 8601 UTC format, Date and time of Estimated Time of Departure from Berth, expected by Port Authority. [EMSWe: DE-005-04] [EDI: DTM-2005-133] [S211: locationState.timeType.ESTIMATED] [IMO: IMO0066]'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    firstBollard:    
      description: First bollard identifier in port facility    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    gln:    
      description: 'ISO/IEC 6523:''https://schema.org/Number''. Optional code of the location. The Global Location Number (GLN) is a 13 digits-unique number that is assigned to locations to enable them to be identified uniquely worldwide, allocated to any location in the supply chain. These GLNs can be used to identify any legal, physical and functional locations'    
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
        type: Property    
    lastBollard:    
      description: Last bollard identifier in port facility    
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
    mooringLines:    
      description: 'Number of mooring lines. '    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    mrn:    
      description: 'MRN coded identifier. It has to be related to the entity in a way that is well-known by different organisms the meaning and the initiator of the entity, and all next parties will maintain on its original value. This identifier must be an UNIQUE identifier of the PortCall entity assigned by the system who created on first the entity. This URN should Conforms MRN & IETF specifically RFC 2141, RFC 5234, and RFC 8141. The proposed format is id::=''urn:mrn:<OID>:<ONSS>:portcalls:berth:id:[0-9]+'' where OID:= Organisation UN/LOCODE, OONSS:=Organization Name of Service, 9999999 an increasing, unique identifier that the issuer of the Berth entity will identify on his systems (i.e. a SQL row-id), i.e. urn:mrn:eshuv:portcalls:berth:id:2024012. See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory). In international standards is also known as [Ship''s Visit]'    
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
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    portCallNumber:    
      description: PortCall identifier    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    portCallRef:    
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
      description: 'Relationship.Reference to parent PortCall entity. '    
    portCode:    
      description: Code of the port of the call    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    ptaBerth:    
      description: 'Represented by an ISO 8601 UTC format, Planned time of arrival to Berth'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    ptdBerth:    
      description: Represented by an ISO 8601 UTC format. Planned time of departure from Berth    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    remarks:    
      description: 'Remarks of the berthing, by Agent at Port or others'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    requestedAt:    
      description: 'Represented by an ISO 8601 UTC format, Date and time of the berthing request by the ship agent. '    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    rtaBerth:    
      description: 'Represented by an ISO 8601 UTC format, Date and time of Requested Time of Arrival by ship-agent (ISO 8601 UTC format).. [EMSWe: DE-005-09] [EDI: DTM-2005-132] [S211: locationState.timeType.ESTIMATED] [IMO: IMO0064]'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    rtdBerth:    
      description: 'Represented by an ISO 8601 UTC format, Date and time of Requested Time of Departure by ship-agent (ISO 8601 UTC format). [EMSWe: DE-005-09] [EDI: DTM-2005-132] [S211: locationState.timeType.ESTIMATED] [IMO: IMO0064]'    
      format: date-time    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    status:    
      description: 'Current status of the Berthing in its lifetime, from request to authorization and completion. Enum:''ACCEPTED, AUTHORIZED, CANCELLED, COMPLETED, DENIED, INITIATED, REQUESTED, REJECTED, INVOICING, INVOICED''. [EMSWe: DE-019-07] [EDI: BGM-1225] [S211: serviceState: timeSequence:VESSEL] '    
      enum:    
        - ACCEPTED    
        - AUTHORIZED    
        - CANCELLED    
        - COMPLETED    
        - DENIED    
        - INITIATED    
        - REQUESTED    
        - REJECTED    
        - INVOICING    
        - INVOICED    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    stopRank:    
      description: Rank or Number of this stop in the PortCall activity ordered by arrival time in the sequence of stops (berthing/anchor area)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    terminal:    
      description: Common name of the Terminal    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be Berth    
      enum:    
        - Berth    
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
    - portCallRef    
    - stopRank    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2024 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/Berth/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/Berth/schema.json    
  x-model-tags: ESHUV    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### Berth NGSI-v2 key-values Exemple  
Voici un exemple de poste d'amarrage au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "02ce3860-3126-42af-8ac7-c2a661134130",  
  "type": "Berth",  
  "mrn": "urn:mrn:eshuv:portcalls:berth:id:18013",  
  "portCode": "ESHUV",  
  "year": 2023,  
  "portCallNumber": "ESHUV202300123",  
  "portCallRef": "urn:mrn:eshuv:portcalls:portcall:2023:id:941",  
  "stopRank": 2,  
  "terminal": "Muelle Levante",  
  "berthCode": "urn:mrn:eshuv:portcalls:berth:code:10",  
  "berthName": "Levante comercial",  
  "gln": 84332157000139,  
  "firstBollard": "N03",  
  "lastBollard": "N12",  
  "status": "AUTHORIZED",  
  "requestedAt": "2023-01-01T07:30:00",  
  "authorizedAt": "2023-01-01T07:30:00",  
  "berthingTypeCode": "AB1",  
  "mooringLines": 12,  
  "activityCode": "ZOP",  
  "etaBerth": "2023-01-01T07:30:00",  
  "rtaBerth": "2023-01-01T07:30:00",  
  "ptaBerth": "2023-01-01T07:30:00",  
  "ataBerth": "2023-01-01T07:30:00",  
  "etdBerth": "2023-01-01T07:30:00",  
  "rtdBerth": "2023-01-01T07:30:00",  
  "ptdBerth": "2023-01-01T07:30:00",  
  "atdBerth": "2023-01-01T07:30:00",  
  "arrivalDraught": 12.3,  
  "departureDraught": 9.5,  
  "remarks": "FONDEA PARA SUMINISTRO DE COMBUSTIBLE POR GABARRA",  
  "authorizationRemarks": "authorized after departure of ship XX",  
  "agentName": "Acme Huelva S.L.",  
  "agentLegalCode": "A-98345678"  
}  
```  
</details>  
#### Berth NGSI-v2 normalisé Exemple  
Voici un exemple de poste d'amarrage au format JSON-LD tel que normalisé. Ce format est compatible avec les NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "02ce3860-3126-42af-8ac7-c2a661134130",  
  "type": "Berth",  
  "mrn": {  
    "type": "string",  
    "value": "urn:mrn:eshuv:portcalls:berth:id:18013"  
  },  
  "gln": {  
    "type": "number",  
    "value": 84332157000139  
  },  
  "portCode": {  
    "type": "string",  
    "value": "ESHUV"  
  },  
  "year": {  
    "type": "number",  
    "value": 2023  
  },  
  "portCallNumber": {  
    "type": "string",  
    "value": "ESHUV202300123"  
  },  
  "portCallRef": {  
    "type": "string",  
    "value": "urn:mrn:eshuv:portcalls:portcall:2023:id:941"  
  },  
  "stopRank": {  
    "type": "number",  
    "value": 2  
  },  
  "terminal": {  
    "type": "string",  
    "value": "Muelle Levante"  
  },  
  "berthCode": {  
    "type": "string",  
    "value": "urn:mrn:eshuv:portcalls:berth:code:10"  
  },  
  "berthName": {  
    "type": "string",  
    "value": "Levante comercial"  
  },  
  "firstBollard": {  
    "type": "string",  
    "value": "N03"  
  },  
  "lastBollard": {  
    "type": "string",  
    "value": "N12"  
  },  
  "status": {  
    "type": "string",  
    "value": "AUTHORIZED"  
  },  
  "requestedAt": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:30:00"  
  },  
  "authorizedAt": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:30:00"  
  },  
  "berthingTypeCode": {  
    "type": "string",  
    "value": "AB1"  
  },  
  "mooringLines": {  
    "type": "number",  
    "value": 12  
  },  
  "activityCode": {  
    "type": "string",  
    "value": "ZOP"  
  },  
  "etaBerth": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:30:00"  
  },  
  "rtaBerth": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:30:00"  
  },  
  "ptaBerth": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:30:00"  
  },  
  "ataBerth": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:30:00"  
  },  
  "etdBerth": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:30:00"  
  },  
  "rtdBerth": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:30:00"  
  },  
  "ptdBerth": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:30:00"  
  },  
  "atdBerth": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:30:00"  
  },  
  "arrivalDraught": {  
    "type": "number",  
    "value": 12.3  
  },  
  "departureDraught": {  
    "type": "number",  
    "value": 9.5  
  },  
  "remarks": {  
    "type": "string",  
    "value": "FONDEA PARA SUMINISTRO DE COMBUSTIBLE POR GABARRA"  
  },  
  "authorizationRemarks": {  
    "type": "string",  
    "value": "authorized after departure of ship XX"  
  },  
  "agentName": {  
    "type": "string",  
    "value": "Acme Huelva S.L."  
  },  
  "agentLegalCode": {  
    "type": "string",  
    "value": "A-98345678"  
  }  
}  
```  
</details>  
#### Berth NGSI-LD key-values Exemple  
Voici un exemple de poste d'amarrage au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "02ce3860-3126-42af-8ac7-c2a661134130",  
  "type": "Berth",  
  "mrn": "urn:mrn:eshuv:portcalls:berth:id:18013",  
  "gln": 1234567890123,  
  "portCode": "ESHUV",  
  "year": 2023,  
  "portCallNumber": "ESHUV202300123",  
  "portCallRef": "urn:mrn:eshuv:portcalls:portcall:2023:id:941",  
  "stopRank": 2,  
  "terminal": "Muelle Levante",  
  "berthCode": "urn:mrn:eshuv:portcalls:berth:code:10",  
  "berthName": "Levante comercial",  
  "firstBollard": "N03",  
  "lastBollard": "N12",  
  "status": "AUTHORIZED",  
  "requestedAt": "2023-01-01T07:30:00",  
  "authorizedAt": "2023-01-01T07:30:00",  
  "berthingTypeCode": "AB1",  
  "mooringLines": 12,  
  "activityCode": "ZOP",  
  "etaBerth": "2023-01-01T07:30:00",  
  "rtaBerth": "2023-01-01T07:30:00",  
  "ptaBerth": "2023-01-01T07:30:00",  
  "ataBerth": "2023-01-01T07:30:00",  
  "etdBerth": "2023-01-01T07:30:00",  
  "rtdBerth": "2023-01-01T07:30:00",  
  "ptdBerth": "2023-01-01T07:30:00",  
  "atdBerth": "2023-01-01T07:30:00",  
  "arrivalDraught": 12.3,  
  "departureDraught": 9.5,  
  "remarks": "FONDEA PARA SUMINISTRO DE COMBUSTIBLE POR GABARRA",  
  "authorizationRemarks": "authorized after departure of ship XX",  
  "agentName": "Acme Huelva S.L.",  
  "agentLegalCode": "A-98345678",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Berth NGSI-LD normalisé Exemple  
Voici un exemple de poste d'amarrage au format JSON-LD tel que normalisé. Ce format est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "02ce3860-3126-42af-8ac7-c2a661134130",  
  "type": "Berth",  
  "mrn": {  
    "type": "Property",  
    "value": "urn:mrn:eshuv:portcalls:berth:id:18013"  
  },  
  "gln": {  
    "type": "Property",  
    "value": 84332157000139  
  },  
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
    "object": "urn:mrn:eshuv:portcalls:portcall:2023:id:941"  
  },  
  "stopRank": {  
    "type": "Property",  
    "value": 2  
  },  
  "terminal": {  
    "type": "Property",  
    "value": "Muelle Levante"  
  },  
  "berthCode": {  
    "type": "Property",  
    "value": "urn:mrn:eshuv:portcalls:berth:code:10"  
  },  
  "berthName": {  
    "type": "Property",  
    "value": "Levante comercial"  
  },  
  "firstBollard": {  
    "type": "Property",  
    "value": "N03"  
  },  
  "lastBollard": {  
    "type": "Property",  
    "value": "N12"  
  },  
  "status": {  
    "type": "Property",  
    "value": "AUTHORIZED"  
  },  
  "requestedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:30:00"  
    }  
  },  
  "authorizedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:30:00"  
    }  
  },  
  "berthingTypeCode": {  
    "type": "Property",  
    "value": "AB1"  
  },  
  "mooringLines": {  
    "type": "Property",  
    "value": 12  
  },  
  "activityCode": {  
    "type": "Property",  
    "value": "ZOP"  
  },  
  "etaBerth": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:30:00"  
    }  
  },  
  "rtaBerth": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:30:00"  
    }  
  },  
  "ptaBerth": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:30:00"  
    }  
  },  
  "ataBerth": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:30:00"  
    }  
  },  
  "etdBerth": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:30:00"  
    }  
  },  
  "rtdBerth": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:30:00"  
    }  
  },  
  "ptdBerth": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:30:00"  
    }  
  },  
  "atdBerth": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:30:00"  
    }  
  },  
  "arrivalDraught": {  
    "type": "Property",  
    "value": 12.3  
  },  
  "departureDraught": {  
    "type": "Property",  
    "value": 9.5  
  },  
  "remarks": {  
    "type": "Property",  
    "value": "FONDEA PARA SUMINISTRO DE COMBUSTIBLE POR GABARRA"  
  },  
  "authorizationRemarks": {  
    "type": "Property",  
    "value": "authorized after departure of ship XX"  
  },  
  "agentName": {  
    "type": "Property",  
    "value": "Acme Huelva S.L."  
  },  
  "agentLegalCode": {  
    "type": "Property",  
    "value": "A-98345678"  
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
