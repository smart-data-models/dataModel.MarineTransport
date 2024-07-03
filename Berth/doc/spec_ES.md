<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: Atracadero  
===================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/Berth/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Este modelo de datos está destinado a proporcionar información sobre Atraques. Definimos "atraque" a cada parada de un buque durante una escala portuaria, tanto para una instalación portuaria (atraque) como para una zona de fondeo. Cada atraque tiene una hora de atraque (estimada, prevista, etc.), un ciclo de vida (estimado, solicitado, aprobado, etc.), una actividad principal durante la parada (operaciones comerciales, reparación mayor, etc.) y una serie de atributos que se describen a continuación. Cuando tengan lugar operaciones comerciales, una entidad Operación definirá los detalles de cada operación comercial**.  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.  
- `activityCode[string]`: Actividad durante la escala en el muelle. Puede tratarse de operaciones de carga o de una serie de actividades relacionadas con las actividades buque-puerto. Enum: ZGR=Reparación mayor; ZPV=Aprovisionamiento; ZCA=Construcción en astillero; ZRA=Reparación mayor en astillero; ZRF=Reparación a flote con personal de la tripulación; ZRT=Reparación fondeado con personal distinto de la tripulación; ZDA=Desguace en astillero; ZTA=Transformación en astillero; ZTF=Transformación; ZVO=Visita oficial; ZAF=Llegada forzosa; ZIN=Inactividad; ZIP=Inactividad pesquera; ZAR=Aprovisionamiento en atraque; ZAO=Aprovisionamiento en fondeo; ZAB=Aprovisionamiento en atraque por gabarra; ZOP=Operaciones portuarias de tráfico comercial; ZCT=Cruceros turísticos; ZTI=Tráfico interno; ZBO=Lanzamiento; ZCO=Construcción; ZRE=Embarcación destinada al servicio de remolque; ZDE=Desguace; ZAP=Embarcaciones pesqueras y artesanales en operaciones de carga y descarga de pescado fresco; ZDR=Embarcación destinada al dragado; ZPB=Paro biológico; ZCL=Sin licencia; ZDJ=Depósito judicial; ZMR=Barco destinado al servicio de amarre; ZPR=Barco destinado al servicio de practicaje; ZRM=Remolque; ZVA=Acceso a grada; ZDS=Barco en dique seco; ZOT=Otros; EST=Estancia; ZSA=Abastecimiento de agua; ZSH=Abastecimiento de hielo; ZSE=Abastecimiento de energía eléctrica; ZSC=Abastecimiento de combustible; ZSV=Vicualización;  . Model: [https://schema.org/Text](https://schema.org/Text)- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección postal, y que está en la región  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, gestiona el gobierno local    
	- `postOfficeBoxNumber[string]`: El número del apartado de correos para las direcciones de apartados postales. Por ejemplo, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: La dirección  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Número que identifica una propiedad específica en una vía pública    
- `agentLegalCode[string]`: Código de identificación legal del agente marítimo de PortCall  . Model: [https://schema.org/Text](https://schema.org/Text)- `agentName[string]`: Nombre del agente marítimo de PortCall  . Model: [https://schema.org/Text](https://schema.org/Text)- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrivalDraught[number]`: Calado en primera línea asegurado para la navegación de llegada  . Model: [https://schema.org/Number](https://schema.org/Number)- `ataBerth[date-time]`: Representado por un formato ISO 8601 UTC, Hora real de llegada al atraque  - `atdBerth[date-time]`: Representado por un formato ISO 8601 UTC. Hora real de salida del atraque  - `authorizationRemarks[string]`: Condiciones de atraque redactadas por la Autoridad Portuaria  . Model: [https://schema.org/Text](https://schema.org/Text)- `authorizedAt[date-time]`: Representado por un formato ISO 8601 UTC, Fecha y hora de autorización por la Autoridad Portuaria y la Autoridad Marítima.  - `berthCode[string]`: Código que identifica el puerto-instalación para esta escala del buque. Formato: <oid>:atraque:99999  . Model: [https://schema.org/Text](https://schema.org/Text)- `berthName[string]`: Nombre de la instalación portuaria para esta escala del buque  . Model: [https://schema.org/Text](https://schema.org/Text)- `berthingTypeCode[string]`: Códigos para identificar el Tipo de atraque/amarre en la interfaz buque-puerto. Enum: ABV=Abarloado de babor a buque; ABX=Abarloado de puerto; AB1=Abarloado de babor por proa; AB2=Abarloado de babor por popa; AEX=Abarloado de estribor; AX1=Abarloado por proa; AEV=Abarloado de estribor a buque; REM=Abarloado de estribor en el muelle; REX=Abarloado de estribor; RE1=Abarloado de estribor por proa; RE2=Abarloado de estribor por popa; RPM=Torsión de puntera a muelle; RPV=Abarloado de punta a barco; RPX=Abarloado de punta; RXM=Amarrar junto a un muelle; RXV=Amarrado a otro barco; RXX=Amarrado ; RX1=Abarloado por proa; AE1=Abarloado a estribor por proa; AE2=Abarloado a estribor por popa; APM=Abarloado al muelle; APV=Abarloado al barco; APX=Acoplado al muelle; AXM=Acoplado al muelle; AXV=Acoplado al buque; AXX=Acoplado; AX2=Acoplado por popa; FBM=Acoplado a babor al muelle; FBV=Acoplado a babor al buque; FBX=Acoplado al muelle; FB1=Acoplado a babor por proa; FB2=Acoplado a babor por popa; FEM=Acoplado a estribor al muelle; FEV=Anclado estribor al barco; FEX=Anclado estribor; FE1=Anclado estribor por proa; FE2=Anclado estribor por popa; FPM=Amarre a muelle; FPV=Anclado punta a barco; FPX=Anclado punta; FP1=Anclado punta por proa; FP2=Anclado punta por popa; FXM=Anclado al muelle; FXV=Anclado al barco; FX1=anclado por proa; FX2=anclado por popa; RBM=anclado a babor en el muelle; RBX=anclado a babor; RB1=anclado a babor por proa; RB2=anclado a babor por popa; RX2=anclado a popa; YBM=anclado a la boya de babor en el muelle; YBV=anclado a la boya de babor del barco; YBX=Atado a la boya de babor; YB1=Atado a la boya de babor por proa; YB2=Atado a la boya de babor por popa; YEM=Atado a la boya de estribor en el muelle; YEV=Atado a la boya de estribor del buque; YEX=Atado a la boya de estribor; YE1=Atado a la boya de estribor por proa; YE2=Atado a la boya de estribor por popa; YPM=Atada a la boya de punta en el muelle; YPV=Atada a la boya de punta al buque; YPX=Atada a la boya de punta; YP1=Atada a la boya de punta por proa; YP2=Atada a la boya de punta por popa; YXM=Atada a la boya en el muelle; YXV=Atada a la boya al buque; YX1=Atada a la boya por proa; YX2=Atado a boya por popa; ABM=Puerto atracado al muelle; AEM=Amurado a estribor al muelle; FXX=Anclado; YXX=Atado a boya sin más indicación; AP1=Boyado punta por proa; AP2=Boyado proa y popa; RBV=Boyado babor al buque; REV=Boyado estribor al buque;.   . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `departureDraught[number]`: Calado en la última línea liberada para la navegación de salida  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: Descripción de este artículo  - `etaBerth[date-time]`: Representado por un formato ISO 8601 UTC, Fecha y hora de la Hora Estimada de Llegada al Atraque prevista por la Autoridad Portuaria (formato ISO 8601 UTC). [EMSWe: DE-005-09] [EDI: DTM-2005-132] [S211: locationState.timeType.ESTIMATED] [OMI: IMO0064].  - `etdBerth[date-time]`: Representado por un formato ISO 8601 UTC, Fecha y hora de la Hora Estimada de Salida del Atraque, prevista por la Autoridad Portuaria. [EMSWe: DE-005-04] [EDI: DTM-2005-133] [S211: locationState.timeType.ESTIMATED] [IMO: IMO0066]  - `firstBollard[string]`: Primer identificador de bolardos en una instalación portuaria  . Model: [https://schema.org/Text](https://schema.org/Text)- `gln[number]`: ISO/IEC 6523:'https://schema.org/Number'. Código opcional de la ubicación. El Global Location Number (GLN) es un número único de 13 dígitos que se asigna a las ubicaciones para permitir su identificación única en todo el mundo, asignado a cualquier ubicación de la cadena de suministro. Estos GLN pueden utilizarse para identificar cualquier ubicación legal, física y funcional  - `id[*]`: Identificador único de la entidad  - `lastBollard[string]`: Último identificador de bolardos en la instalación portuaria  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `mooringLines[number]`: Número de cabos de amarre.  . Model: [https://schema.org/Number](https://schema.org/Number)- `mrn[string]`: Identificador codificado MRN. Tiene que estar relacionado con la entidad de forma que sea conocido por los diferentes organismos el significado y el iniciador de la entidad, y todas las partes siguientes mantendrán en su valor original. Este identificador debe ser un identificador ÚNICO de la entidad PortCall asignado por el sistema que creó en primer lugar la entidad. Este URN debe Conformar MRN & IETF específicamente RFC 2141, RFC 5234, y RFC 8141. El formato propuesto es id::='urn:mrn:<OID>:<ONSS>:portcalls:berth:id:[0-9]+' donde OID:= Organisation UN/LOCODE, OONSS:=Organization Name of Service, 9999999 un identificador único creciente que el emisor de la entidad Berth identificará en sus sistemas (es decir, un SQL row-id), es decir, urn:mrn:eshuv:portcalls:berth:id:2024012. Véase [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory). En las normas internacionales también se conoce como [Ship's Visit].  - `name[string]`: El nombre de este artículo  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `portCallNumber[string]`: Identificador PortCall  . Model: [https://schema.org/Text](https://schema.org/Text)- `portCallRef[*]`: Relación.Referencia a la entidad PortCall matriz.  - `portCode[string]`: Código del puerto de escala  . Model: [https://schema.org/Text](https://schema.org/Text)- `ptaBerth[date-time]`: Representada por un formato ISO 8601 UTC, Hora prevista de llegada al atraque  - `ptdBerth[date-time]`: Representado por un formato ISO 8601 UTC. Hora prevista de salida del atraque  - `remarks[string]`: Observaciones del atraque, por Agente en Puerto u otros  . Model: [https://schema.org/Text](https://schema.org/Text)- `requestedAt[date-time]`: Representado por un formato ISO 8601 UTC, Fecha y hora de la solicitud de atraque por parte del consignatario.  - `rtaBerth[date-time]`: Representado por un formato ISO 8601 UTC, Fecha y hora de la hora de llegada solicitada por el buque-agente (formato ISO 8601 UTC).. [EMSWe: DE-005-09] [EDI: DTM-2005-132] [S211: locationState.timeType.ESTIMATED] [IMO: IMO0064].  - `rtdBerth[date-time]`: Representado por un formato ISO 8601 UTC, Fecha y hora de la hora de salida solicitada por el buque-agente (formato ISO 8601 UTC). [EMSWe: DE-005-09] [EDI: DTM-2005-132] [S211: locationState.timeType.ESTIMATED] [IMO: IMO0064]  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `status[string]`: Estado actual del Atraque en su vida, desde la solicitud hasta la autorización y finalización. Enum:'ACEPTADO, AUTORIZADO, CANCELADO, COMPLETADO, DENEGADO, INICIADO, SOLICITADO, RECHAZADO, FACTURANDO, FACTURADO'. [EMSWe: DE-019-07] [EDI: BGM-1225] [S211: serviceState: timeSequence:VESSEL]  . Model: [https://schema.org/Text](https://schema.org/Text)- `stopRank[number]`: Rango o Número de esta parada en la actividad PortCall ordenada por hora de llegada en la secuencia de paradas (zona de atraque/anclaje).  . Model: [https://schema.org/Number](https://schema.org/Number)- `terminal[string]`: Nombre común de la terminal  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Tipo de entidad NGSI. Tiene que ser Atraque  - `year[number]`: Año de init del atraque  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `id`  - `portCallRef`  - `stopRank`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
modelo de datos extraído de la ontología ERA https://data-interop.era.europa.eu/era-vocabulary (Agencia Ferroviaria de la Unión Europea)  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Descripción de las propiedades del modelo de datos  
Ordenados alfabéticamente (pulse para más detalles)  
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
## Ejemplo de carga útil  
#### Ejemplo de valores clave de NGSI-v2 de amarre  
He aquí un ejemplo de un amarre en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### Atraque NGSI-v2 normalizado Ejemplo  
He aquí un ejemplo de un amarre en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### Ejemplo de valores clave NGSI-LD de amarre  
He aquí un ejemplo de un amarre en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### Atraque NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de un amarre en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
