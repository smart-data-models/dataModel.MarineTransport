<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: Liegeplatz  
===================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/Berth/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Dieses Datenmodell dient der Bereitstellung von Informationen über Liegeplätze. Wir definieren "Liegeplatz" für jeden Aufenthalt eines Schiffes während eines PortCalls, sowohl für eine Hafenanlage (Liegeplatz) als auch für einen Ankerplatz. Jeder Liegeplatz hat eine Liegezeit (geschätzt, geplant usw.), einen Lebenszyklus (geschätzt, beantragt, genehmigt usw.), eine Hauptaktivität während des Aufenthalts (kommerzielle Tätigkeiten, größere Reparaturen usw.) und eine Reihe von Attributen, die im Folgenden beschrieben werden. Wenn ein kommerzieller Betrieb stattfindet, definiert eine Entität Operation die Details jedes kommerziellen Betriebs**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `activityCode[string]`: Aktivität während des Aufenthalts am Liegeplatz. Dabei kann es sich um Ladungsvorgänge oder eine Reihe von Aktivitäten im Zusammenhang mit den Schiffs-Hafen-Aktivitäten handeln. Aufzählung: ZGR=Große Reparatur; ZPV=Bereitstellung; ZCA=Werftbau; ZRA=Große Werftreparatur; ZRF=Reparatur auf See mit Besatzungspersonal; ZRT=Reparatur vor Anker mit anderem Personal als der Besatzung; ZDA=Werftabwrackung; ZTA=Werftumbau; ZTF=Umbau; ZVO=Offizieller Besuch; ZAF=Zwangsankunft; ZIN=Inaktiv; ZIP=Inaktivität der Fischerei; ZAR=Bereitstellung am Liegeplatz; ZAO=Bereitstellung am Ankerplatz; ZAB=Bereitstellung am Liegeplatz durch Binnenschiff; ZOP=Hafenbetrieb des gewerblichen Verkehrs; ZCT=Sightseeing Cruises; ZTI=Interner Verkehr; ZBO=Launching; ZCO=Bau; ZRE=Schleppdienst; ZDE=Abwrackwerft; ZAP=Fischereifahrzeuge und handwerkliche Fischereifahrzeuge beim Be- und Entladen von Frischfisch; ZDR=Schiff für Baggerarbeiten; ZPB=Biologischer Stillstand; ZCL=Keine Lizenz; ZDJ=Gerichtsverwahrung; ZMR=Schiff zum Festmachen; ZPR=Schiff zum Lotsendienst; ZRM=Anhänger; ZVA=Zugang zur Helling; ZDS=Schiff im Trockendock; ZOT=Sonstiges; EST=Aufenthalt; ZSA=Wasserversorgung; ZSH=Eisversorgung; ZSE=Elektrizitätsversorgung; ZSC=Kraftstoffversorgung; ZSV=Verkehr;  . Model: [https://schema.org/Text](https://schema.org/Text)- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.    
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Nummer zur Identifizierung eines bestimmten Grundstücks an einer öffentlichen Straße    
- `agentLegalCode[string]`: Rechtlicher Identifizierungscode des PortCall-Schiffsagenten  . Model: [https://schema.org/Text](https://schema.org/Text)- `agentName[string]`: Name des Schiffsagenten von PortCall  . Model: [https://schema.org/Text](https://schema.org/Text)- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrivalDraught[number]`: Tiefgang an der ersten Linie für die ankommende Schifffahrt gesichert  . Model: [https://schema.org/Number](https://schema.org/Number)- `ataBerth[date-time]`: Dargestellt durch ein ISO 8601 UTC-Format, tatsächliche Ankunftszeit am Liegeplatz  - `atdBerth[date-time]`: Dargestellt durch ein ISO 8601 UTC-Format. Tatsächliche Zeit der Abfahrt vom Liegeplatz  - `authorizationRemarks[string]`: Von der Hafenbehörde aufgestellte Bedingungen für das Anlegen  . Model: [https://schema.org/Text](https://schema.org/Text)- `authorizedAt[date-time]`: Dargestellt durch ein ISO 8601 UTC-Format, Datum und Uhrzeit der Genehmigung durch die Hafenbehörde und die Schifffahrtsbehörde.  - `berthCode[string]`: Code zur Identifizierung der Hafenanlage für diesen Stopp des Schiffes. Format: <oid>:Liegeplatz:99999  . Model: [https://schema.org/Text](https://schema.org/Text)- `berthName[string]`: Name der Hafenanlage für diesen Aufenthalt des Schiffes  . Model: [https://schema.org/Text](https://schema.org/Text)- `berthingTypeCode[string]`: Codes zur Identifizierung der Art des Liegeplatzes/Liegeplatzes in der Schnittstelle Schiff-Hafen. Aufzählung: ABV=Angelegt von Backbord an Schiff; ABX=Angelegt von Backbord an Schiff; AB1=Angelegt von Backbord an Bug; AB2=Angelegt von Backbord an Heck; AEX=Angelegt von Steuerbord an Schiff; AX1=Angelegt von Bug; AEV=Angelegt von Steuerbord an Schiff; REM=Angelegt von Steuerbord an der Pier; REX=Angelegt von Steuerbord an Bug; RE1=Angelegt von Steuerbord an Bug; RE2=Angelegt von Steuerbord an Heck; RPM=Verdrehung von der Spitze zum Schiff; RPV=Verdrehung von der Spitze zum Schiff; RPX=Verdrehung von der Spitze zum Schiff; RXM=Längsseits an einem Dock festmachen; RXV=An einem anderen Schiff festgemacht; RXX=Festgemacht; RX1=Verdrehung vom Bug; AE1=Verdrehung von Steuerbord durch den Bug; AE2=Verdrehung von Steuerbord durch das Heck; APM=Verdrehung an der Pier; APV=Verdrehung zum Schiff; APX=Punktankerung; AXM=An der Pier festgemacht; AXV=Auf dem Schiff festgemacht; AXX=Auf dem Schiff festgemacht; AX2=Auf dem Schiff festgemacht; FBM=Backbord an der Pier verankert; FBV=Backbord auf dem Schiff verankert; FBX=Hafen verankert; FB1=Bugbord an Bug verankert; FB2=Bugbord an Heck verankert; FEM=Steuerbord an der Pier verankert; FEV=Steuerbord zum Schiff verankert; FEX=Steuerbord verankert; FE1=Steuerbord mit dem Bug verankert; FE2=Steuerbord mit dem Heck verankert; FPM=An der Pier verankert; FPV=An der Spitze zum Schiff verankert; FPX=Punktverankerung; FP1=An der Spitze mit dem Bug verankert; FP2=An der Spitze mit dem Heck verankert; FXM=An der Pier verankert; FXV=Am Schiff verankert; FX1=Mit dem Bug verankert; FX2=Mit dem Heck verankert; RBM=An der Backbordseite des Docks festgemacht; RBX=An der Backbordseite festgemacht; RB1=Mit dem Bug an Backbord festgemacht; RB2=Mit dem Heck an Backbord festgemacht; RX2=Mit dem Heck festgemacht; YBM=An der Backbordboje an der Pier festgemacht; YBV=An der Boje an der Backbordseite des Schiffs festgemacht; YBX=An der Backbordboje angebunden; YB1=Mit dem Bug an der Backbordboje angebunden; YB2=Mit dem Heck an der Backbordboje angebunden; YEM=An der Steuerbordboje an der Pier angebunden; YEV=Mit der Steuerbordboje des Schiffes angebunden; YEX=Mit der Steuerbordboje angebunden; YE1=Mit dem Bug an der Steuerbordboje angebunden; YE2=Mit dem Heck an der Steuerbordboje angebunden; YPM=An der Endboje am Pier angebunden; YPV=An der Boje Ende-Schiff angebunden; YPX=An der Spitzentonne angebunden; YP1=Mit dem Bug an der Spitzentonne angebunden; YP2=Mit dem Heck an der Spitzentonne angebunden; YXM=Mit der Boje am Pier angebunden; YXV=Mit der Boje am Schiff angebunden; YX1=Mit dem Bug an der Boje angebunden; YX2=Mit dem Heck an der Boje festgemacht; ABM=Hafen an der Pier festgemacht; AEM=Steuerbord am Dock festgemacht; FXX=Ankerung; YXX=An der Boje festgemacht ohne weitere Angabe; AP1=Bordspitze mit dem Bug; AP2=Vorschiffs und achtern festgemacht; RBV=Bord zum Schiff; REV=Steuerbord zum Schiff gerollt;.   . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `departureDraught[number]`: Tiefgang an der letzten Linie für die Abfahrtsnavigation freigegeben  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: Eine Beschreibung dieses Artikels  - `etaBerth[date-time]`: Dargestellt durch ein ISO 8601 UTC-Format, Datum und Uhrzeit der von der Hafenbehörde erwarteten geschätzten Ankunftszeit am Liegeplatz (ISO 8601 UTC-Format). [EMSWe: DE-005-09] [EDI: DTM-2005-132] [S211: locationState.timeType.ESTIMATED] [IMO: IMO0064]  - `etdBerth[date-time]`: Dargestellt durch ein ISO 8601 UTC-Format, Datum und Uhrzeit der von der Hafenbehörde erwarteten geschätzten Zeit des Verlassens des Liegeplatzes. [EMSWe: DE-005-04] [EDI: DTM-2005-133] [S211: locationState.timeType.ESTIMATED] [IMO: IMO0066]  - `firstBollard[string]`: Erste Pollerkennzeichnung in einer Hafenanlage  . Model: [https://schema.org/Text](https://schema.org/Text)- `gln[number]`: ISO/IEC 6523:'https://schema.org/Number'. Optionaler Code des Standorts. Die Global Location Number (GLN) ist eine 13-stellige eindeutige Nummer, die Standorten zugewiesen wird, um sie weltweit eindeutig identifizieren zu können, und die jedem Standort in der Lieferkette zugeordnet wird. Diese GLNs können zur Identifizierung aller rechtlichen, physischen und funktionalen Standorte verwendet werden.  - `id[*]`: Eindeutiger Bezeichner der Entität  - `lastBollard[string]`: Letzte Poller-Kennung in der Hafenanlage  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `mooringLines[number]`: Anzahl der Festmacherleinen.  . Model: [https://schema.org/Number](https://schema.org/Number)- `mrn[string]`: MRN kodierter Bezeichner. Er muss mit der Entität in einer Weise verknüpft sein, die den verschiedenen Organismen die Bedeutung und dem Initiator der Entität bekannt ist, und alle nachfolgenden Parteien werden seinen ursprünglichen Wert beibehalten. Dieser Bezeichner muss ein eindeutiger Bezeichner der PortCall-Einheit sein, der von dem System zugewiesen wird, das die Einheit zuerst erstellt hat. Diese URN sollte MRN- und IETF-konform sein, insbesondere RFC 2141, RFC 5234 und RFC 8141. Das vorgeschlagene Format ist id::='urn:mrn:<OID>:<ONSS>:portcalls:berth:id:[0-9]+', wobei OID:=Organisations-UN/LOCODE, OONSS:=Organisationsname des Dienstes, 9999999 ein zunehmender, eindeutiger Bezeichner, den der Aussteller der Berth-Entität auf seinen Systemen identifiziert (d. h. eine SQL-Zeilen-ID), z. B. urn:mrn:eshuv:portcalls:berth:id:2024012. Siehe [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory). In internationalen Standards auch bekannt als [Ship's Visit]  - `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `portCallNumber[string]`: PortCall-Bezeichnung  . Model: [https://schema.org/Text](https://schema.org/Text)- `portCallRef[*]`: Beziehung: Verweis auf die übergeordnete PortCall-Entität.  - `portCode[string]`: Code des angelaufenen Hafens  . Model: [https://schema.org/Text](https://schema.org/Text)- `ptaBerth[date-time]`: Geplante Ankunftszeit am Liegeplatz, dargestellt im ISO 8601 UTC-Format  - `ptdBerth[date-time]`: Dargestellt durch ein ISO 8601 UTC-Format. Geplante Zeit der Abfahrt vom Liegeplatz  - `remarks[string]`: Bemerkungen zum Liegeplatz, durch den Agenten im Hafen oder andere  . Model: [https://schema.org/Text](https://schema.org/Text)- `requestedAt[date-time]`: Dargestellt durch ein ISO 8601 UTC-Format, Datum und Uhrzeit der Liegeplatzanfrage durch den Schiffsagenten.  - `rtaBerth[date-time]`: Dargestellt durch ein ISO 8601 UTC-Format, Datum und Uhrzeit der angeforderten Ankunftszeit des Schiffsagenten (ISO 8601 UTC-Format) [EMSWe: DE-005-09] [EDI: DTM-2005-132] [S211: locationState.timeType.ESTIMATED] [IMO: IMO0064]  - `rtdBerth[date-time]`: Dargestellt durch ein ISO 8601 UTC-Format, Datum und Uhrzeit der vom Schiffsagenten angeforderten Abfahrtszeit (ISO 8601 UTC-Format). [EMSWe: DE-005-09] [EDI: DTM-2005-132] [S211: locationState.timeType.ESTIMATED] [IMO: IMO0064]  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `status[string]`: Aktueller Status des Liegeplatzes in seiner Lebensdauer, von der Anfrage bis zur Genehmigung und Fertigstellung. Enum:'ACCEPTED, AUTHORIZED, CANCELLED, COMPLETED, DENIED, INITIATED, REQUESTED, REJECTED, INVOICING, INVOICED'. [EMSWe: DE-019-07] [EDI: BGM-1225] [S211: serviceState: timeSequence:VESSEL]  . Model: [https://schema.org/Text](https://schema.org/Text)- `stopRank[number]`: Rang oder Nummer dieser Haltestelle in der PortCall-Aktivität, geordnet nach Ankunftszeit in der Abfolge der Haltestellen (Liegeplatz/Ankerbereich)  . Model: [https://schema.org/Number](https://schema.org/Number)- `terminal[string]`: Allgemeiner Name des Terminals  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI-Entitätstyp. Es muss Liegeplatz sein  - `year[number]`: Jahr der Inbetriebnahme des Liegeplatzes  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `portCallRef`  - `stopRank`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
Datenmodell, das von der ERA-Ontologie https://data-interop.era.europa.eu/era-vocabulary (European Union Agency for Railways) übernommen wurde  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
## Beispiel-Nutzlasten  
#### Liegeplatz NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen Liegeplatz im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### Liegeplatz NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen Liegeplatz im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
#### Liegeplatz NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen Liegeplatz im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### Liegeplatz NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen Liegeplatz im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
