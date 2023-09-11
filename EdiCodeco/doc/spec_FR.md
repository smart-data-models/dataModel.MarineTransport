<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : EdiCodeco  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/EdiCodeco/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Message par lequel un terminal, un dépôt, etc. confirme que les conteneurs spécifiés ont été livrés ou enlevés par le transporteur terrestre (route, rail ou péniche). Ce message peut également être utilisé pour signaler les mouvements de conteneurs internes au terminal (à l'exclusion du chargement et du déchargement du navire) et pour signaler le changement d'état d'un ou de plusieurs conteneurs sans que ceux-ci aient été physiquement déplacés. Voir [UN/EDIFACT - CODECO](https://service.unece.org/trade/untdid/d19a/trmd/codeco_c.htm)**.  
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
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `ata[date-time]`: Heure réelle d'arrivée ou de départ du terminal. (format ISO 8601 UTC). Voir [UNTDID - D.95B - Segment DTM - C507 (2380)](https://service.unece.org/trade/untdid/d95b/uncl/uncl2380.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `bookingCode[string]`: Référence de réservation. Voir [UNTDID - D.95B - Segment RFF - C506 (1154)](https://service.unece.org/trade/untdid/d95b/uncl/uncl1154.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerCarrierIdentification[string]`: Code identifiant une partie impliquée dans une transaction. Voir [UNTDID - D.95B - Segment NAD - C082 (3039)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3039.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerClass[string]`: Classe de conteneur (indication de l'action liée à l'équipement). Enum : "Continental, Export, Import, Remain on board, Shifter, Transhipment". Voir [UNTDID - D.95B - Segment EQD - 8249] (https://service.unece.org/trade/untdid/d95b/uncl/uncl8249.htm).  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerIdentification[string]`: Identification du conteneur. Voir [UNTDID - D.95B - Segment EQD - C237 (8260)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8260.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerIsoCode[string]`: Description codée de la taille et du type d'équipement. Enum 'Réservoir enduit de chaux,Réservoir enduit d'époxy,IMO1,IMO2,IMO3,Réservoir pressurisé,Réservoir réfrigéré,Semi-réfrigéré,Réservoir en acier inoxydable,Conteneur frigorifique non ouvrable de 40 pieds,Caisse-palette,Europalette,Palette scandinave,Remorque,Conteneur frigorifique non ouvrable de 20 pieds,Palette interchangeable,Semi-remorque,Conteneur-citerne de 20 pieds,Conteneur-citerne 30 ft.,Conteneur-citerne 40 ft.,Conteneur IC 20 ft.,Conteneur IC 30 ft.,Conteneur IC 40 ft.,Citerne frigorifique 20 ft.,Citerne frigorifique 30 ft.,Citerne frigorifique 40 ft.,Conteneur-citerne IC 20 ft.,Conteneur-citerne IC 30 ft.,Conteneur-citerne IC 40 ft.,Citerne frigorifique IC 20 ft.,Citerne frigorifique IC 40 ft.,Caisson déplaçable : L < 6,15m,Caisse mobile : 6,15m < L < 7,82m,Caisse mobile : 7,82m < L < 9,15m,Caisse mobile : 9,15m < L < 10,90m,Caisse mobile : 10,90m < L < 13,75m,Totebin,Conteneur à température contrôlée 20 ft,Conteneur à température contrôlée 40 ft'. Voir [UNTDID - D.95B - Segment EQD - C224 (8155)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8155.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerSeal[string]`: Le numéro d'un scellé personnalisé ou d'un autre scellé apposé sur les conteneurs. Voir [UNTDID - D.95B - Segment SEL - 9308](https://service.unece.org/trade/untdid/d95b/uncl/uncl9308.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerWeight[number]`: Poids du conteneur. Voir [UNTDID - D.95B - Segment MEA - C174 (6314)](https://service.unece.org/trade/untdid/d95b/uncl/uncl6314.htm)  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `destination[string]`: Destination finale du conteneur (UN/LOCODE : Code des Nations Unies pour les lieux de commerce et de transport). Voir [UNTDID - D.95B - Segment LOC - C517 (3225)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm) et [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)  . Model: [https://schema.org/Text](https://schema.org/Text)- `destinationTransportType[string]`: Code de la méthode de transport (CEE/ONU). Voir [UNTDID - D.95B - Segment TDT - C220 (8067)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8067.htm) et [UN/ECE - Rec 19](https://unece.org/trade/uncefact/cl-recommendations)  . Model: [https://schema.org/Text](https://schema.org/Text)- `dischargingPort[string]`: Port où le conteneur est déchargé (UN/LOCODE : Code des Nations Unies pour les lieux de commerce et de transport). Voir [UNTDID - D.95B - Segment LOC - C517 (3225)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm) et [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)  . Model: [https://schema.org/Text](https://schema.org/Text)- `fileName[string]`: Nom de fichier du message EDI Codeco  . Model: [https://schema.org/Text](https://schema.org/Text)- `functionCode[string]`: Code indiquant la fonction du message. Enum='Annulation, Ajout, Suppression, Modification, Remplacement, Confirmation, Duplicata, Statut, Original, Non trouvé, Réponse, Non traité, Demande, Notification préalable, Rappel, Proposition, Annulation, à réémettre, Réémission, Modification à l'initiative du vendeur, Remplacement de la section d'en-tête uniquement, Remplacement du détail de l'article et du résumé uniquement, Transmission finale, Transaction en attente, Instruction de livraison, Prévision, Instruction de livraison et prévision, Non accepté, Accepté, avec modification dans la section d'en-tête, Accepté sans modification, Accepté, avec modification dans la section détaillée, Copie, Approbation, Modification dans la section du titre, Accepté avec modification, Retransmission, Modification dans la section détaillée, Annulation d'un débit, Annulation d'un crédit, Annulation pour annulation, Demande de suppression, Finir/fermer l'ordre, Confirmation par des moyens spécifiques, Transmission supplémentaire, Accepté sans réserves, Accepté avec réserves, Provisoire, Définitif, Accepté, contenu rejeté, Litige réglé, Retrait, Autorisation, Proposition de modification, Test". Voir [UNTDID - D.95B - BGM - 1225] (https://service.unece.org/trade/untdid/d95b/uncl/uncl1225.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[string]`: Identifiant unique de l'entité  - `isContainerEmpty[boolean]`: Information indiquant si le conteneur est plein ou vide. Voir [UNTDID - D.95B - Segment EQD - 8169](https://service.unece.org/trade/untdid/d95b/uncl/uncl8169.htm)  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `loadingPort[string]`: Port où le conteneur est chargé (UN/LOCODE : Code des Nations Unies pour les lieux de commerce et de transport). Voir [UNTDID - D.95B - Segment LOC - C517 (3225)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm) et [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `messageRaw[string]`: Message brut de l'EDI Codeco  . Model: [https://schema.org/Text](https://schema.org/Text)- `messageVersion[string]`: Version du type de message. Voir [UNTDID - D.95B - UNH - S009 (0052)] (https://service.unece.org/trade/untdid/d95b/trmd/codeco_d.htm#DSGI)  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: Le nom de cet élément  - `operationType[string]`: Code identifiant la fonction d'un lieu. Enum : 'Lieu des conditions de livraison, Lieu de paiement, Lieu de réception des marchandises, Lieu de départ, Lieu de livraison, Lieu de destination, Lieu/port de chargement, Lieu d'acceptation, Lieu/port de déchargement, Port de déchargement, Lieu de transbordement, Emplacement des marchandises, Lieu de transfert de responsabilité, Lieu de transfert de propriété, Lieu de passage de la frontière, Entrepôt, Usine/usine, Lieu de destination finale des marchandises, Lieu des conditions de vente, Bureau de douane de dédouanement, Port de mainlevée, Port d'entrée, Pays, Ville, Pays d'origine, Pays de destination des marchandises, Gare ferroviaire, Pays de provenance, Bâtiment, Début de la section taxable, Port de base du déchargement, Port de base du chargement, Pays d'exportation/d'expédition, Pays de destination finale, Pays de dernier envoi, Pays de première destination, Pays de production, Pays de commerce, Bureau de douane d'entrée, Bureau de douane de sortie, Lieu d'examen douanier, Lieu d'authentification du document, Bureau de douane de destination (transit), Région d'expédition, Région de destination, Région de production, Pays de transit, Bureau de douane de transit, Pays de garantie de transit non valable, Pays de destination (transit), Frais et fret dus par, Département de fabrication, Frais et fret dus à, Fin de la section imposable, Lieu de paiement, Chargement ou déchargement en pleine voie, Lieu d'arrivée, Port d'escale suivant, Port d'embarquement, Premier lieu de déchargement facultatif, Gare ferroviaire express, Gare ferroviaire pour cargaisons mixtes, Deuxième lieu de déchargement facultatif, Port d'escale suivant sans déchargement, Troisième lieu de déchargement facultatif, Point de regroupement, Quatrième lieu de déchargement facultatif, Bureau de libération du connaissement, Transbordement excluant ce lieu, Transbordement limité à ce lieu, Port de chargement initial, Premier port d'escale sans déchargement, Premier port d'escale avec déchargement, Lieu/port de première entrée, Lieu d'expédition, Cinquième lieu de déchargement facultatif, Port de préacheminement, Lieu de livraison (par transport sur wagon), Lieu d'acceptation du contrat de transport, Lieu de destination du contrat de transport, Pays de garantie de transit valable, Lieu/port d'arrivée initiale du moyen de transport, Lieu de réception, Lieu d'enregistrement, Lieu/emplacement où des traitements spéciaux ont eu lieu ou doivent avoir lieu, Lieu de délivrance des documents, Acheminement, Station d'application des frais supplémentaires, Lieu de dépôt des documents, Lieu de déchargement facultatif, Lieu d'expédition de l'équipement vide, Lieu de retour de l'équipement vide, Lieu/port d'entrée de l'entrepôt, Pays de la première vente, Pays de l'achat, Lieu de transfert, lieu de dégroupement, lieu de consommation, région d'origine, lieu de groupage, point de combinaison des taux, lieu de décision de prolongation du retard de livraison, lieu/emplacement de rechargement, bureau de douane d'expédition, pays d'expédition, bureau de douane d'exportation, zone franche d'exportation, région d'exportation/d'expédition, bureau de douane de départ, bureau de douane de garantie de transit, pays de transbordement, pays de vente, bureau de douane de destination, gare ferroviaire de wagons isolés, Voie d'évitement, dernier lieu/port d'escale du moyen de transport, pays du régime douanier précédent, bureau de douane d'enregistrement de la déclaration en douane précédente, lieu de l'expéditeur participant, district de négociation salariale, lieu de destination finale du moyen de transport, lieu de chargement de l'équipement vide, lieu de déchargement de l'équipement vide, région de livraison, entrepôt de produits pétroliers, lieu d'entrée (douane), lieu de soins aux animaux vivants, lieu de reglaçage, lieu de pesage, gare de triage, station de magasinage, quai de chargement, Connexion portuaire, Lieu d'expiration, Lieu de négociation, Lieu de paiement des créances, Crédit documentaire disponible dans, Cellule d'arrimage, Pour le transport vers, Chargement à bord/expédition/prise en charge à/depuis, Box privé, Port de déchargement suivant, Port d'escale, Lieu/emplacement d'embarquement, Lieu/emplacement de débarquement, Terminal d'autres transporteurs, Pays de la juridiction de la taxe sur la valeur ajoutée (TVA), Lieu de contact, Destination interne supplémentaire, Port d'escale étranger, Lieu d'entretien Défini mutuellement". Voir [UNTDID - D.95B - Segment TDT - LOC - 3227] (https://service.unece.org/trade/untdid/d95b/uncl/uncl3227.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `originTransportType[string]`: Code de la méthode de transport (CEE/ONU). Voir [UNTDID - D.95B - Segment TDT - C220 (8067)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8067.htm) et [UN/ECE - Rec 19](https://unece.org/trade/uncefact/cl-recommendations)  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `receiverIdentification[string]`: Identification du destinataire de l'échange. Voir [UN/EDIFACT - S003] (https://unece.org/trade/uncefact/unedifact/part-4-Annex-B)  . Model: [https://schema.org/Text](https://schema.org/Text)- `release[string]`: Numéro de version dans le numéro de version actuel. Voir [UNTDID - D.95B - UNH - S009 (0054)] (https://service.unece.org/trade/untdid/d95b/trmd/codeco_d.htm#DSGI)  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `senderIdentification[string]`: Interchange Sender Identification (identification de l'expéditeur de l'échange). Voir [UN/EDIFACT - S002] (https://unece.org/trade/uncefact/unedifact/part-4-Annex-B)  . Model: [https://schema.org/Text](https://schema.org/Text)- `sentAt[date-time]`: Date et heure d'envoi du message représentées par un format ISO 8601 UTC. Voir [UN/EDIFACT - S004] (https://unece.org/trade/uncefact/unedifact/part-4-Annex-B)  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `travelReference[string]`: Numéro de référence du moyen de transport. Voir [UNTDID - D.95B - Segment TDT - 8028] (https://service.unece.org/trade/untdid/d95b/uncl/uncl8028.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `truckLicenseCode[string]`: Plaque d'immatriculation du camion. Voir [UNTDID - D.95B - Segment TDT - C222 (8213)] (https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Type d'entité NGSI. Il doit s'agir d'EdiCodeco  - `vesselCallSign[string]`: Les indicatifs d'appel maritimes sont des indicatifs d'appel attribués comme identificateurs uniques aux navires. Voir [UNTDID - D.95B - Segment TDT - C222 (8213)] (https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselCarrier[string]`: Identification du transporteur maritime (identification de la partie qui entreprend ou organise le transport de marchandises entre des points désignés). Voir [UNTDID - D.95B - Segment TDT - C040 (3127)] (https://service.unece.org/trade/untdid/d95b/uncl/uncl3127.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselImo[number]`: Numéro de l'Organisation maritime internationale (un UID mondial pour toujours). Voir [UNTDID - D.95B - Segment TDT - C222 (8213)] (https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)  . Model: [https://schema.org/Number](https://schema.org/Number)- `vesselMmsi[number]`: Numéro d'identité du service mobile maritime (UID attribué temporairement, délivré par l'État du pavillon actuel de l'objet). Voir [UNTDID - D.95B - Segment TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)  . Model: [https://schema.org/Number](https://schema.org/Number)- `vesselName[string]`: Nom du navire. Voir [UNTDID - D.95B - Segment TDT - C222 (8212)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8212.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselVoyage[string]`: Numéro de référence du voyage du navire. Voir [UNTDID - D.95B - Segment RFF - C506 (1154)](https://service.unece.org/trade/untdid/d95b/uncl/uncl1154.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `containerIdentification`  - `id`  - `type`  - `vesselImo`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EdiCodeco:    
  description: 'A message by which a terminal, depot, etc. confirms that the containers specified have been delivered or picked up by the inland carrier (road, rail or barge). This message can also be used to report internal terminal container movements (excluding loading and discharging the vessel) and to report the change in status of container(s) without those containers having physically been moved. See [UN/EDIFACT - CODECO](https://service.unece.org/trade/untdid/d19a/trmd/codeco_c.htm)'    
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
    ata:    
      description: 'Actual time of arrival or departure to/from Terminal. (ISO 8601 UTC format). See [UNTDID - D.95B - Segment DTM - C507 (2380)](https://service.unece.org/trade/untdid/d95b/uncl/uncl2380.htm)'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    bookingCode:    
      description: 'Booking Reference. See [UNTDID - D.95B - Segment RFF - C506 (1154)](https://service.unece.org/trade/untdid/d95b/uncl/uncl1154.htm)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    containerCarrierIdentification:    
      description: 'Code identifying a party involved in a transaction. See [UNTDID - D.95B - Segment NAD - C082 (3039)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3039.htm)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    containerClass:    
      description: 'Container class (indication of the action related to the equipment). Enum: ''Continental, Export, Import,Remain on board,Shifter,Transhipment''. See [UNTDID - D.95B - Segment EQD - 8249](https://service.unece.org/trade/untdid/d95b/uncl/uncl8249.htm)'    
      enum:    
        - Continental    
        - Export    
        - Import    
        - Remain on board    
        - Shifter    
        - Transhipment    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    containerIdentification:    
      description: 'Containter identification. See [UNTDID - D.95B - Segment EQD - C237 (8260)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8260.htm)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    containerIsoCode:    
      description: 'Coded description of the size and type of equipment. Enum ''Dime coated tank,Epoxy coated tank,IMO1,IMO2,IMO3,Pressurized tank,Refrigerated tank,Semi-refrigerated,Stainless steel tank,Nonworking reefer container 40 ft,Box pallet,Europallet,Scandinavian pallet,Trailer,Nonworking reefer container 20 ft,Exchangeable pallet,Semi-trailer,Tank container 20 ft.,Tank container 30 ft.,Tank container 40 ft.,Container IC 20 ft.,Container IC 30 ft.,Container IC 40 ft.,Refrigerator tank 20 ft.,Refrigerator tank 30 ft.,Refrigerator tank 40 ft.,Tank container IC 20 ft.,Tank container IC 30 ft.,Tank container IC 40 ft.,Refrigerator tank IC 20 ft.,Refrigerator tank IC 40 ft.,Movable case: L < 6,15m,Movable case: 6,15m < L < 7,82m,Movable case: 7,82m < L < 9,15m,Movable case: 9,15m < L < 10,90m,Movable case: 10,90m < L < 13,75m,Totebin,Temperature controlled container 20 ft,Temperature controlled container 40 ft''. See [UNTDID - D.95B - Segment EQD - C224 (8155)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8155.htm)'    
      enum:    
        - Dime coated tank    
        - Epoxy coated tank    
        - IMO1    
        - IMO2    
        - IMO3    
        - Pressurized tank    
        - Refrigerated tank    
        - Semi-refrigerated    
        - Stainless steel tank    
        - Nonworking reefer container 40 ft    
        - Box pallet    
        - Europallet    
        - Scandinavian pallet    
        - Trailer    
        - Nonworking reefer container 20 ft    
        - Exchangeable pallet    
        - Semi-trailer    
        - Tank container 20 ft.    
        - Tank container 30 ft.    
        - Tank container 40 ft.    
        - Container IC 20 ft.    
        - Container IC 30 ft.    
        - Container IC 40 ft.    
        - Refrigerator tank 20 ft.    
        - Refrigerator tank 30 ft.    
        - Refrigerator tank 40 ft.    
        - Tank container IC 20 ft.    
        - Tank container IC 30 ft.    
        - Tank container IC 40 ft.    
        - Refrigerator tank IC 20 ft.    
        - Refrigerator tank IC 40 ft.    
        - 'Movable case: L < 6,15m'    
        - 'Movable case: 6,15m < L < 7,82m'    
        - 'Movable case: 7,82m < L < 9,15m'    
        - 'Movable case: 9,15m < L < 10,90m'    
        - 'Movable case: 10,90m < L < 13,75m'    
        - Totebin    
        - Temperature controlled container 20 ft    
        - Temperature controlled container 40 ft    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    containerSeal:    
      description: 'The number of a custom seal or another seal affixed to the containers. See [UNTDID - D.95B - Segment SEL - 9308](https://service.unece.org/trade/untdid/d95b/uncl/uncl9308.htm)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    containerWeight:    
      description: 'Weight of the container. See [UNTDID - D.95B - Segment MEA - C174 (6314)](https://service.unece.org/trade/untdid/d95b/uncl/uncl6314.htm)'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: ' KGM'    
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
    destination:    
      description: 'Final destination of the container (UN/LOCODE: United Nations Code for Trade and Transport Locations). See [UNTDID - D.95B - Segment LOC - C517 (3225)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm) and [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    destinationTransportType:    
      description: 'Method of transport code (UN/ECE). See [UNTDID - D.95B - Segment TDT - C220 (8067)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8067.htm) and [UN/ECE - Rec 19](https://unece.org/trade/uncefact/cl-recommendations)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dischargingPort:    
      description: 'Port where the container is discharged (UN/LOCODE: United Nations Code for Trade and Transport Locations). See [UNTDID - D.95B - Segment LOC - C517 (3225)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm) and [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    fileName:    
      description: File name of EDI Codeco message    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    functionCode:    
      description: 'Code indicating the function of the message. Enum=''Cancellation, Addition, Deletion, Change, Replace, Confirmation, Duplicate, Status, Original, Not found, Response, Not processed, Request, Advance notification, Reminder, Proposal, Cancel, to be reissued, Reissue, Seller initiated change, Replace heading section only, Replace item detail and summary only, Final transmission, Transaction on hold, Delivery instruction, Forecast, Delivery instruction and forecast, Not accepted, Accepted, with amendment in heading section, Accepted without amendment, Accepted, with amendment in detail section, Copy, Approval, Change in heading section, Accepted with amendment, Retransmission, Change in detail section, Reversal of a debit, Reversal of a credit, Reversal for cancellation, Request for deletion, Finishing/closing order, Confirmation via specific means, Additional transmission, Accepted without reserves, Accepted with reserves, Provisional, Definitive, Accepted, contents rejected, Settled dispute, Withdraw, Authorisation, Proposed amendment, Test''. See [UNTDID - D.95B - BGM - 1225](https://service.unece.org/trade/untdid/d95b/uncl/uncl1225.htm)'    
      enum:    
        - Cancellation    
        - Addition    
        - Deletion    
        - Change    
        - Replace    
        - Confirmation    
        - Duplicate    
        - Status    
        - Original    
        - Not found    
        - Response    
        - Not processed    
        - Request    
        - Advance notification    
        - Reminder    
        - Proposal    
        - 'Cancel, to be reissued'    
        - Reissue    
        - Seller initiated change    
        - Replace heading section only    
        - Replace item detail and summary only    
        - Final transmission    
        - Transaction on hold    
        - Delivery instruction    
        - Forecast    
        - Delivery instruction and forecast    
        - Not accepted    
        - 'Accepted, with amendment in heading section'    
        - Accepted without amendment    
        - 'Accepted, with amendment in detail section'    
        - Copy    
        - Approval    
        - Change in heading section    
        - Accepted with amendment    
        - Retransmission    
        - Change in detail section    
        - Reversal of a debit    
        - Reversal of a credit    
        - Reversal for cancellation    
        - Request for deletion    
        - Finishing/closing order    
        - Confirmation via specific means    
        - Additional transmission    
        - Accepted without reserves    
        - Accepted with reserves    
        - Provisional    
        - Definitive    
        - 'Accepted, contents rejected'    
        - Settled dispute    
        - Withdraw    
        - Authorisation    
        - Proposed amendment    
        - Test    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    id:    
      description: Unique identifier of the entity    
      type: string    
      x-ngsi:    
        type: Property    
    isContainerEmpty:    
      description: 'Information about if the container is full or empty. See [UNTDID - D.95B - Segment EQD - 8169](https://service.unece.org/trade/untdid/d95b/uncl/uncl8169.htm)'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    loadingPort:    
      description: 'Port where the container is loaded (UN/LOCODE: United Nations Code for Trade and Transport Locations). See [UNTDID - D.95B - Segment LOC - C517 (3225)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm) and [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)'    
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
    messageRaw:    
      description: Raw message of the EDI Codeco    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    messageVersion:    
      description: "Version of the message type. See [UNTDID - D.95B - UNH - S009 (0052)](https://service.unece.org/trade/untdid/d95b/trmd/codeco_d.htm#DSGI)"    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    operationType:    
      description: 'Code identifying the function of a location. Enum: ''Place of terms of delivery, Payment place, Goods receipt place, Place of departure, Place of delivery, Place of destination, Place/port of loading, Place of acceptance, Place/port of discharge, Port of discharge, Place of transhipment, Location of goods, Place of transfer responsibility, Place of transfer of ownership, Border crossing place, Warehouse, Factory/plant, Place of ultimate destination of goods, Terms of sale place, Customs office of clearance, Port of release, Port of entry, Country, City, Country of origin, Country of destination of goods, Railway station, Country of source, Building, Beginning of chargeable section, Baseport of discharge, Baseport of loading, Country of exportation/despatch, Country of ultimate destination, Country of last consignment, Country of first destination, Country of production, Country of trading, Customs office of entry, Customs office of exit, Place of Customs examination, Place of authentication of document, Customs office of destination (transit), Region of despatch, Region of destination, Region of production, Country of transit, Customs office of transit, Country of invalid transit guarantee, Country of destination (transit), Charge and freight due from, Manufacturing department, Charges and freight payable to, End of chargeable section, Place of payment, Full track loading or unloading, Place of arrival, Next port of call, On-carriage port, First optional place of discharge, Express railway station, Mixed cargo railway station, Second optional place of discharge, Next non-discharge port of call, Third optional place of discharge, Reconsolidation point, Fourth optional place of discharge, Bill of lading release office, Transhipment excluding this place, Transhipment limited to this place, Original port of loading, First port of call - non-discharging, First port of call - discharging, Place/port of first entry, Place of despatch, Fifth optional place of discharge, Pre-carriage port, Place of delivery (by on carriage), Transport contract place of acceptance, Transport contract place of destination, Country of valid transit guarantee, Place/port of conveyance initial arrival, Place of receipt, Place of registration, Place/location where special treatments have happened or must happen, Place of document issue, Routing, Station of application of additional costs, Place of lodgement of documents, Optional place of discharge, Place of empty equipment despatch, Place of empty equipment return, Place/port of warehouse entry, Country of first sale, Country of purchase, Place of transfer, Place of deconsolidation, Place of consumption, Region of origin, Place of consolidation, Rate combination point, Place of prolongation decision of delivery delay, Recharging place/location, Customs office of despatch, Country of despatch, Customs office of export, Free zone of export, Region of export/despatch, Customs office of departure, Customs office of transit guarantee, Country of transhipment, Country of sale, Customs office of destination, Wagon-load railway station, Siding, Last place/port of call of conveyance, Country of previous Customs procedure, Customs office of registration of previous Customs declaration, Participant sender location, Wage negotiation district, Place of ultimate destination of conveyance, Place of loading of empty equipment, Place of discharge of empty equipment, Region of delivery, Petroleum warehouse, Place of entry (Customs), Living animals care place, Re-icing place, Weighting place, Marshalling yard, Shopping station, Loading dock, Port connection, Place of expiry, Place of negotiation, Claims payable place, Documentary credit available in, Stowage cell, For transportation to, Loading on board/despatch/taking in charge at/from, Private box, Next port of discharge, Port of call, Place/location of on-hire, Place/location of off-hire, Other carriers terminal, Country of Value Added Tax (VAT) jurisdiction, Contact location, Additional internal destination, Foreign port of call, Maintenance location    
        Mutually defined''. See [UNTDID - D.95B - Segment TDT - LOC - 3227](https://service.unece.org/trade/untdid/d95b/uncl/uncl3227.htm)'    
      enum:    
        - Place of terms of delivery    
        - Payment place    
        - Goods receipt place    
        - Place of departure    
        - Place of delivery    
        - Place of destination    
        - Place/port of loading    
        - Place of acceptance    
        - Place/port of discharge    
        - Port of discharge    
        - Place of transhipment    
        - Location of goods    
        - Place of transfer responsibility    
        - Place of transfer of ownership    
        - Border crossing place    
        - Warehouse    
        - Factory/plant    
        - Place of ultimate destination of goods    
        - Terms of sale place    
        - Customs office of clearance    
        - Port of release    
        - Port of entry    
        - Country    
        - City    
        - Country of origin    
        - Country of destination of goods    
        - Railway station    
        - Country of source    
        - Building    
        - Beginning of chargeable section    
        - Baseport of discharge    
        - Baseport of loading    
        - Country of exportation/despatch    
        - Country of ultimate destination    
        - Country of last consignment    
        - Country of first destination    
        - Country of production    
        - Country of trading    
        - Customs office of entry    
        - Customs office of exit    
        - Place of Customs examination    
        - Place of authentication of document    
        - Customs office of destination (transit)    
        - Region of despatch    
        - Region of destination    
        - Region of production    
        - Country of transit    
        - Customs office of transit    
        - Country of invalid transit guarantee    
        - Country of destination (transit)    
        - Charge and freight due from    
        - Manufacturing department    
        - Charges and freight payable to    
        - End of chargeable section    
        - Place of payment    
        - Full track loading or unloading    
        - Place of arrival    
        - Next port of call    
        - On-carriage port    
        - First optional place of discharge    
        - Express railway station    
        - Mixed cargo railway station    
        - Second optional place of discharge    
        - Next non-discharge port of call    
        - Third optional place of discharge    
        - Reconsolidation point    
        - Fourth optional place of discharge    
        - Bill of lading release office    
        - Transhipment excluding this place    
        - Transhipment limited to this place    
        - Original port of loading    
        - First port of call - non-discharging    
        - First port of call - discharging    
        - Place/port of first entry    
        - Place of despatch    
        - Fifth optional place of discharge    
        - Pre-carriage port    
        - Place of delivery (by on carriage)    
        - Transport contract place of acceptance    
        - Transport contract place of destination    
        - Country of valid transit guarantee    
        - Place/port of conveyance initial arrival    
        - Place of receipt    
        - Place of registration    
        - Place/location where special treatments have happened or must happen    
        - Place of document issue    
        - Routing    
        - Station of application of additional costs    
        - Place of lodgement of documents    
        - Optional place of discharge    
        - Place of empty equipment despatch    
        - Place of empty equipment return    
        - Place/port of warehouse entry    
        - Country of first sale    
        - Country of purchase    
        - Place of transfer    
        - Place of deconsolidation    
        - Place of consumption    
        - Region of origin    
        - Place of consolidation    
        - Rate combination point    
        - Place of prolongation decision of delivery delay    
        - Recharging place/location    
        - Customs office of despatch    
        - Country of despatch    
        - Customs office of export    
        - Free zone of export    
        - Region of export/despatch    
        - Customs office of departure    
        - Customs office of transit guarantee    
        - Country of transhipment    
        - Country of sale    
        - Customs office of destination    
        - Wagon-load railway station    
        - Siding    
        - Last place/port of call of conveyance    
        - Country of previous Customs procedure    
        - Customs office of registration of previous Customs declaration    
        - Participant sender location    
        - Wage negotiation district    
        - Place of ultimate destination of conveyance    
        - Place of loading of empty equipment    
        - Place of discharge of empty equipment    
        - Region of delivery    
        - Petroleum warehouse    
        - Place of entry (Customs)    
        - Living animals care place    
        - Re-icing place    
        - Weighting place    
        - Marshalling yard    
        - Shopping station    
        - Loading dock    
        - Port connection    
        - Place of expiry    
        - Place of negotiation    
        - Claims payable place    
        - Documentary credit available in    
        - Stowage cell    
        - For transportation to    
        - Loading on board/despatch/taking in charge at/from    
        - Private box    
        - Next port of discharge    
        - Port of call    
        - Place/location of on-hire    
        - Place/location of off-hire    
        - Other carriers terminal    
        - Country of Value Added Tax (VAT) jurisdiction    
        - Contact location    
        - Additional internal destination    
        - Foreign port of call    
        - Maintenance location    
        - Mutually defined    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    originTransportType:    
      description: 'Method of transport code (UN/ECE). See [UNTDID - D.95B - Segment TDT - C220 (8067)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8067.htm) and [UN/ECE - Rec 19](https://unece.org/trade/uncefact/cl-recommendations)'    
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
    receiverIdentification:    
      description: 'Interchange Recipient Identification. See [UN/EDIFACT - S003](https://unece.org/trade/uncefact/unedifact/part-4-Annex-B)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    release:    
      description: "Release number within current version number. See [UNTDID - D.95B - UNH - S009 (0054)](https://service.unece.org/trade/untdid/d95b/trmd/codeco_d.htm#DSGI)"    
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
    senderIdentification:    
      description: 'Interchange Sender Identification. See [UN/EDIFACT - S002](https://unece.org/trade/uncefact/unedifact/part-4-Annex-B)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    sentAt:    
      description: 'Date and time of message has been sent represented by an ISO 8601 UTC format. See [UN/EDIFACT - S004](https://unece.org/trade/uncefact/unedifact/part-4-Annex-B)'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    travelReference:    
      description: 'Conveyance reference number. See [UNTDID - D.95B - Segment TDT - 8028](https://service.unece.org/trade/untdid/d95b/uncl/uncl8028.htm)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    truckLicenseCode:    
      description: 'License Plate of the Truck. See [UNTDID - D.95B - Segment TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be EdiCodeco    
      enum:    
        - EdiCodeco    
      type: string    
      x-ngsi:    
        type: Property    
    vesselCallSign:    
      description: 'Maritime call signs are call signs assigned as unique identifiers to vessels. See [UNTDID - D.95B - Segment TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vesselCarrier:    
      description: 'Vessel carrier Identification (identification of party undertaking or arranging transport of goods between named points). See [UNTDID - D.95B - Segment TDT - C040 (3127)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3127.htm)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vesselImo:    
      description: 'International Maritime Organization Number (a global forever UID). See [UNTDID - D.95B - Segment TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vesselMmsi:    
      description: 'Marine Mobile Service Identity Number (a temporarily assigned UID, issued by that object''s current flag state). See [UNTDID - D.95B - Segment TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vesselName:    
      description: 'Vessel Name. See [UNTDID - D.95B - Segment TDT - C222 (8212)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8212.htm)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vesselVoyage:    
      description: 'Reference number of vessel voyage. See [UNTDID - D.95B - Segment RFF - C506 (1154)](https://service.unece.org/trade/untdid/d95b/uncl/uncl1154.htm)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
    - vesselImo    
    - containerIdentification    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/EdiCodeco/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.MarineTransport/EdiCodeco/schema.json    
  x-model-tags: i4trust    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### EdiCodeco NGSI-v2 key-values Exemple  
Voici un exemple d'EdiCodeco au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:mrn:eshuv:edi-codeco:1625763902090",  
    "type": "EdiCodeco",  
    "fileName": "file name",  
    "sentAt": "2023-08-11T14:50:00Z",  
    "travelReference": "110823110823CCHRIB",  
    "ata": "2023-08-11T14:47:00Z",  
    "bookingCode": "FUE110823",  
    "containerCarrierIdentification": "ALU",  
    "containerClass": "Export",  
    "containerIdentification": "TESI1120274",  
    "containerIsoCode": "Refrigerated tank",  
    "containerSeal": "28103",  
    "containerWeight": 27000,  
    "destinationTransportType": "Vessel",  
    "dischargingPort": "ESFUE",  
    "functionCode": "Deletion",  
    "isContainerEmpty": false,  
    "loadingPort": "ESHUV",  
    "operationType": "Port of entry",  
    "originTransportType": "Truck",  
    "messageRaw": "UNB+UNOA:1+ESHUV+PA+230811:1450+174749339'UNH+92218+CODECO:D:95B:UN:SMDG16'BGM+34++9'TDT+20+110823110823CCHRIB+1++ALU:172:166:ALUsios+++1111111:146::CHRISTIAN'RFF+ON:110823110823CCHRIB'NAD+CF+ALU:172:166'NAD+MS+ESSCT:160:ZZZ'EQD+CN+TESI1120274+4EG1:102:5++2+5'RFF+BN:FUE110823'RFF+ACA:FUE110823'DTM+7:202308111447:203'LOC+9+ESHUV:139:6'LOC+11+ESFUE:139:6'LOC+165+ESHUV:139:6+CONCHUV:TER:ZZZ'LOC+164+ESFUE:139:6'MEA+AAE+VGM+KGM:27000.0'SEL+88200+SH'TDT+1++3++:172:ZZZ+++993NGR:146'DTM+ACT:202308111447:203'NAD+CA+ALU:172:166'NAD+CF+ALU:172:166'CNT+16:1'UNT+000022+92218'UNZ+1+174749339'",  
    "receiverIdentification": "PA",  
    "release": "95B",  
    "senderIdentification": "ESHUV",  
    "truckLicenseCode": "993NGR",  
    "messageVersion": "D",  
    "vesselCarrier": "ALQ",  
    "vesselImo": 1111111,  
    "vesselName": "Name",  
    "vesselVoyage": "110823110823CCHRIB"  
}  
```  
</details>  
#### EdiCodeco NGSI-v2 normalisé Exemple  
Voici un exemple d'EdiCodeco au format JSON-LD tel que normalisé. Ce format est compatible avec les NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:mrn:eshuv:edi-codeco:1625763902090",  
    "type": "EdiCodeco",  
    "fileName": {  
        "type": "Text",  
        "value": "file name"  
    },  
    "sentAt": {  
        "type": "DateTime",  
        "value": "2023-08-11T14:50:00Z"  
    },  
    "travelReference": {  
        "type": "Text",  
        "value": "110823110823CCHRIB"  
    },  
    "ata": {  
        "type": "DateTime",  
        "value": "2023-08-11T14:47:00Z"  
    },  
    "bookingCode": {  
        "type": "Text",  
        "value": "FUE110823"  
    },  
    "containerCarrierIdentification": {  
        "type": "Text",  
        "value": "ALU"  
    },  
    "containerClass": {  
        "type": "Text",  
        "value": "Export"  
    },  
    "containerIdentification": {  
        "type": "Text",  
        "value": "TESI1120274"  
    },  
    "containerIsoCode": {  
        "type": "Text",  
        "value": "Refrigerated tank"  
    },  
    "containerSeal": {  
        "type": "Text",  
        "value": "28103"  
    },  
    "containerWeight": {  
        "type": "Number",  
        "value": 27000  
    },  
    "destinationTransportType": {  
        "type": "Text",  
        "value": "Vessel"  
    },  
    "dischargingPort": {  
        "type": "Text",  
        "value": "ESFUE"  
    },  
    "functionCode": {  
        "type": "Text",  
        "value": "Deletion"  
    },  
    "isContainerEmpty": {  
        "type": "Boolean",  
        "value": false  
    },  
    "loadingPort": {  
        "type": "Text",  
        "value": "ESHUV"  
    },  
    "operationType": {  
        "type": "Text",  
        "value": "Port of entry"  
    },  
    "originTransportType": {  
        "type": "Text",  
        "value": "Truck"  
    },  
    "messageRaw": {  
        "type": "Text",  
        "value": "UNB+UNOA:1+ESHUV+PA+230811:1450+174749339'UNH+92218+CODECO:D:95B:UN:SMDG16'BGM+34++9'TDT+20+110823110823CCHRIB+1++ALU:172:166:ALUsios+++1111111:146::CHRISTIAN'RFF+ON:110823110823CCHRIB'NAD+CF+ALU:172:166'NAD+MS+ESSCT:160:ZZZ'EQD+CN+TESI1120274+4EG1:102:5++2+5'RFF+BN:FUE110823'RFF+ACA:FUE110823'DTM+7:202308111447:203'LOC+9+ESHUV:139:6'LOC+11+ESFUE:139:6'LOC+165+ESHUV:139:6+CONCHUV:TER:ZZZ'LOC+164+ESFUE:139:6'MEA+AAE+VGM+KGM:27000.0'SEL+88200+SH'TDT+1++3++:172:ZZZ+++993NGR:146'DTM+ACT:202308111447:203'NAD+CA+ALU:172:166'NAD+CF+ALU:172:166'CNT+16:1'UNT+000022+92218'UNZ+1+174749339'"  
    },  
    "receiverIdentification": {  
        "type": "Text",  
        "value": "PA"  
    },  
    "release": {  
        "type": "Text",  
        "value": "95B"  
    },  
    "senderIdentification": {  
        "type": "Text",  
        "value": "ESHUV"  
    },  
    "truckLicenseCode": {  
        "type": "Text",  
        "value": "993NGR"  
    },  
    "messageVersion": {  
        "type": "Text",  
        "value": "D"  
    },  
    "vesselCarrier": {  
        "type": "Text",  
        "value": "ALQ"  
    },  
    "vesselImo": {  
        "type": "Number",  
        "value": 1111111  
    },  
    "vesselName": {  
        "type": "Text",  
        "value": "Name"  
    },  
    "vesselVoyage": {  
        "type": "Text",  
        "value": "110823110823CCHRIB"  
    }  
}  
```  
</details>  
#### Valeurs clés NGSI-LD d'EdiCodeco Exemple  
Voici un exemple d'EdiCodeco au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:mrn:eshuv:edi-codeco:1625763902090",  
    "type": "EdiCodeco",  
    "fileName": "file name",  
    "sentAt": "2023-08-11T14:50:00Z",  
    "travelReference": "110823110823CCHRIB",  
    "ata": "2023-08-11T14:47:00Z",  
    "bookingCode": "FUE110823",  
    "containerCarrierIdentification": "ALU",  
    "containerClass": "Export",  
    "containerIdentification": "TESI1120274",  
    "containerIsoCode": "Refrigerated tank",  
    "containerSeal": "28103",  
    "containerWeight": 27000,  
    "destinationTransportType": "Vessel",  
    "dischargingPort": "ESFUE",  
    "functionCode": "Deletion",  
    "isContainerEmpty": false,  
    "loadingPort": "ESHUV",  
    "operationType": "Port of entry",  
    "originTransportType": "Truck",  
    "messageRaw": "UNB+UNOA:1+ESHUV+PA+230811:1450+174749339'UNH+92218+CODECO:D:95B:UN:SMDG16'BGM+34++9'TDT+20+110823110823CCHRIB+1++ALU:172:166:ALUsios+++1111111:146::CHRISTIAN'RFF+ON:110823110823CCHRIB'NAD+CF+ALU:172:166'NAD+MS+ESSCT:160:ZZZ'EQD+CN+TESI1120274+4EG1:102:5++2+5'RFF+BN:FUE110823'RFF+ACA:FUE110823'DTM+7:202308111447:203'LOC+9+ESHUV:139:6'LOC+11+ESFUE:139:6'LOC+165+ESHUV:139:6+CONCHUV:TER:ZZZ'LOC+164+ESFUE:139:6'MEA+AAE+VGM+KGM:27000.0'SEL+88200+SH'TDT+1++3++:172:ZZZ+++993NGR:146'DTM+ACT:202308111447:203'NAD+CA+ALU:172:166'NAD+CF+ALU:172:166'CNT+16:1'UNT+000022+92218'UNZ+1+174749339'",  
    "receiverIdentification": "PA",  
    "release": "95B",  
    "senderIdentification": "ESHUV",  
    "truckLicenseCode": "993NGR",  
    "messageVersion": "D",  
    "vesselCarrier": "ALQ",  
    "vesselImo": 1111111,  
    "vesselName": "CHRISTIAN",  
    "vesselVoyage": "110823110823CCHRIB",  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### EdiCodeco NGSI-LD normalisé Exemple  
Voici un exemple d'EdiCodeco au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:mrn:eshuv:edi-codeco:1625763902090",  
    "type": "EdiCodeco",  
    "fileName": {  
        "type": "Property",  
        "value": "file name"  
    },  
    "sentAt": {  
        "type": "Property",  
        "value": {  
            "@value": "2023-08-11T14:50:00Z",  
            "@type": "DateTime"  
        }  
    },  
    "travelReference": {  
        "type": "Property",  
        "value": "110823110823CCHRIB"  
    },  
    "ata": {  
        "type": "Property",  
        "value": {  
            "@value": "2023-08-11T14:47:00Z",  
            "@type": "DateTime"  
        }  
    },  
    "bookingCode": {  
        "type": "Property",  
        "value": "FUE110823"  
    },  
    "containerCarrierIdentification": {  
        "type": "Property",  
        "value": "ALU"  
    },  
    "containerClass": {  
        "type": "Property",  
        "value": "Export"  
    },  
    "containerIdentification": {  
        "type": "Property",  
        "value": "TESI1120274"  
    },  
    "containerIsoCode": {  
        "type": "Property",  
        "value": "Refrigerated tank"  
    },  
    "containerSeal": {  
        "type": "Property",  
        "value": "28103"  
    },  
    "containerWeight": {  
        "type": "Property",  
        "value": 27000  
    },  
    "destinationTransportType": {  
        "type": "Property",  
        "value": "Vessel"  
    },  
    "dischargingPort": {  
        "type": "Property",  
        "value": "ESFUE"  
    },  
    "functionCode": {  
        "type": "Property",  
        "value": "Deletion"  
    },  
    "isContainerEmpty": {  
        "type": "Property",  
        "value": false  
    },  
    "loadingPort": {  
        "type": "Property",  
        "value": "ESHUV"  
    },  
    "operationType": {  
        "type": "Property",  
        "value": "Port of entry"  
    },  
    "originTransportType": {  
        "type": "Property",  
        "value": "Truck"  
    },  
    "messageRaw": {  
        "type": "Property",  
        "value": "UNB+UNOA:1+ESHUV+PA+230811:1450+174749339'UNH+92218+CODECO:D:95B:UN:SMDG16'BGM+34++9'TDT+20+110823110823CCHRIB+1++ALU:172:166:ALUsios+++1111111:146::CHRISTIAN'RFF+ON:110823110823CCHRIB'NAD+CF+ALU:172:166'NAD+MS+ESSCT:160:ZZZ'EQD+CN+TESI1120274+4EG1:102:5++2+5'RFF+BN:FUE110823'RFF+ACA:FUE110823'DTM+7:202308111447:203'LOC+9+ESHUV:139:6'LOC+11+ESFUE:139:6'LOC+165+ESHUV:139:6+CONCHUV:TER:ZZZ'LOC+164+ESFUE:139:6'MEA+AAE+VGM+KGM:27000.0'SEL+88200+SH'TDT+1++3++:172:ZZZ+++993NGR:146'DTM+ACT:202308111447:203'NAD+CA+ALU:172:166'NAD+CF+ALU:172:166'CNT+16:1'UNT+000022+92218'UNZ+1+174749339'"  
    },  
    "receiverIdentification": {  
        "type": "Property",  
        "value": "PA"  
    },  
    "release": {  
        "type": "Property",  
        "value": "95B"  
    },  
    "senderIdentification": {  
        "type": "Property",  
        "value": "ESHUV"  
    },  
    "truckLicenseCode": {  
        "type": "Property",  
        "value": "993NGR"  
    },  
    "messageVersion": {  
        "type": "Property",  
        "value": "D"  
    },  
    "vesselCarrier": {  
        "type": "Property",  
        "value": "ALQ"  
    },  
    "vesselImo": {  
        "type": "Property",  
        "value": 1111111  
    },  
    "vesselName": {  
        "type": "Property",  
        "value": "Name"  
    },  
    "vesselVoyage": {  
        "type": "Property",  
        "value": "110823110823CCHRIB"  
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
