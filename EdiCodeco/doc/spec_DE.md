<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: EdiCodeco  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/EdiCodeco/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Eine Meldung, mit der ein Terminal, Depot usw. bestätigt, dass die angegebenen Container vom Binnentransporteur (Straße, Schiene oder Binnenschiff) geliefert oder abgeholt wurden. Diese Nachricht kann auch verwendet werden, um terminalinterne Containerbewegungen zu melden (mit Ausnahme des Be- und Entladens des Schiffes) und um die Änderung des Status von Containern zu melden, ohne dass diese Container physisch bewegt worden sind. Siehe [UN/EDIFACT - CODECO](https://service.unece.org/trade/untdid/d19a/trmd/codeco_c.htm)**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.    
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `ata[date-time]`: Tatsächliche Ankunfts- oder Abfahrtszeit am/vom Terminal. (ISO 8601 UTC-Format). Siehe [UNTDID - D.95B - Segment DTM - C507 (2380)](https://service.unece.org/trade/untdid/d95b/uncl/uncl2380.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `bookingCode[string]`: Buchungsreferenz. Siehe [UNTDID - D.95B - Segment RFF - C506 (1154)](https://service.unece.org/trade/untdid/d95b/uncl/uncl1154.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerCarrierIdentification[string]`: Code zur Identifizierung einer an einer Transaktion beteiligten Partei. Siehe [UNTDID - D.95B - Segment NAD - C082 (3039)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3039.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerClass[string]`: Containerklasse (Angabe der Aktion im Zusammenhang mit dem Equipment). Enum: "Kontinental, Export, Import, Verbleib an Bord, Shifter, Umladung". Siehe [UNTDID - D.95B - Segment EQD - 8249](https://service.unece.org/trade/untdid/d95b/uncl/uncl8249.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerIdentification[string]`: Identifizierung des Behälters. Siehe [UNTDID - D.95B - Segment EQD - C237 (8260)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8260.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerIsoCode[string]`: Codierte Beschreibung der Größe und Art der Ausrüstung. Enum 'Dime coated tank,Epoxy coated tank,IMO1,IMO2,IMO3,Pressurized tank,Refrigerated tank,Semi-refrigerated,Stainless steel tank,Nonworking reefer container 40 ft,Box pallet,Europallet,Scandinavian pallet,Trailer,Nonworking reefer container 20 ft,Exchangeable pallet,Semi-trailer,Tank container 20 ft.,Tankcontainer 30 ft.,Tankcontainer 40 ft.,Container IC 20 ft.,Container IC 30 ft.,Container IC 40 ft.,Kühlschranktank 20 ft.,Kühlschranktank 30 ft.,Kühlschranktank 40 ft.,Tankcontainer IC 20 ft.,Tankcontainer IC 30 ft.,Tankcontainer IC 40 ft.,Kühlschranktank IC 20 ft.,Kühlschranktank IC 40 ft.,Bewegliches Gehäuse: L < 6,15m,Bewegliche Kiste: 6,15m < L < 7,82m,Bewegliche Kiste: 7,82m < L < 9,15m,Bewegliche Kiste: 9,15m < L < 10,90m,Bewegliche Kiste: 10,90m < L < 13,75m,Totebin,Temperaturgesteuerter Container 20 ft,Temperaturgesteuerter Container 40 ft'. Siehe [UNTDID - D.95B - Segment EQD - C224 (8155)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8155.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerSeal[string]`: Die Nummer eines Zollverschlusses oder eines anderen auf den Behältern angebrachten Verschlusses. Siehe [UNTDID - D.95B - Segment SEL - 9308](https://service.unece.org/trade/untdid/d95b/uncl/uncl9308.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerWeight[number]`: Gewicht des Containers. Siehe [UNTDID - D.95B - Segment MEA - C174 (6314)](https://service.unece.org/trade/untdid/d95b/uncl/uncl6314.htm)  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `destination[string]`: Endgültiger Bestimmungsort des Containers (UN/LOCODE: United Nations Code for Trade and Transport Locations). Siehe [UNTDID - D.95B - Segment LOC - C517 (3225)] (https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm) und [UN/LOCODE] (https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)  . Model: [https://schema.org/Text](https://schema.org/Text)- `destinationTransportType[string]`: Code der Beförderungsart (UN/ECE). Siehe [UNTDID - D.95B - Segment TDT - C220 (8067)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8067.htm) und [UN/ECE - Rec 19](https://unece.org/trade/uncefact/cl-recommendations)  . Model: [https://schema.org/Text](https://schema.org/Text)- `dischargingPort[string]`: Hafen, in dem der Container entladen wird (UN/LOCODE: United Nations Code for Trade and Transport Locations). Siehe [UNTDID - D.95B - Segment LOC - C517 (3225)] (https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm) und [UN/LOCODE] (https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)  . Model: [https://schema.org/Text](https://schema.org/Text)- `fileName[string]`: Dateiname der EDI-Codeco-Nachricht  . Model: [https://schema.org/Text](https://schema.org/Text)- `functionCode[string]`: Code, der die Funktion der Nachricht angibt. Enum='Cancellation, Addition, Deletion, Change, Replace, Confirmation, Duplicate, Status, Original, Not found, Response, Not processed, Request, Advance notification, Reminder, Proposal, Cancel, to be reissued, Reissue, Seller initiated change, Replace heading section only, Replace item detail and summary only, Final transmission, Transaction on hold, Delivery instruction, Forecast, Delivery instruction and forecast, Not accepted, Accepted, with amendment in heading section, Accepted without amendment, Angenommen, mit Änderung im Detailbereich, Kopie, Genehmigung, Änderung im Kopfbereich, Angenommen mit Änderung, Rückübermittlung, Änderung im Detailbereich, Stornierung einer Lastschrift, Stornierung einer Gutschrift, Stornierung wegen Stornierung, Antrag auf Löschung, Beendigung/Abschluss eines Auftrags, Bestätigung auf spezielle Weise, Zusätzliche Übermittlung, Angenommen ohne Vorbehalt, Angenommen mit Vorbehalt, Vorläufig, Endgültig, Angenommen, Inhalt abgelehnt, Beilegung eines Streits, Zurückziehen, Genehmigung, Änderungsvorschlag, Test". Siehe [UNTDID - D.95B - BGM - 1225](https://service.unece.org/trade/untdid/d95b/uncl/uncl1225.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[string]`: Eindeutiger Bezeichner der Entität  - `isContainerEmpty[boolean]`: Informationen darüber, ob der Behälter voll oder leer ist. Siehe [UNTDID - D.95B - Segment EQD - 8169](https://service.unece.org/trade/untdid/d95b/uncl/uncl8169.htm)  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `loadingPort[string]`: Hafen, in dem der Container verladen wird (UN/LOCODE: United Nations Code for Trade and Transport Locations). Siehe [UNTDID - D.95B - Segment LOC - C517 (3225)] (https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm) und [UN/LOCODE] (https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `messageRaw[string]`: Rohnachricht des EDI Codeco  . Model: [https://schema.org/Text](https://schema.org/Text)- `messageVersion[string]`: Version des Nachrichtentyps. Siehe [UNTDID - D.95B - UNH - S009 (0052)](https://service.unece.org/trade/untdid/d95b/trmd/codeco_d.htm#DSGI)  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: Der Name dieses Artikels  - `operationType[string]`: Code zur Identifizierung der Funktion eines Ortes. Aufzählung: 'Ort der Lieferbedingungen, Zahlungsort, Wareneingangsort, Abgangsort, Lieferort, Bestimmungsort, Verladeort/-hafen, Annahmeort, Löschort/-hafen, Löschhafen, Umschlagort, Warenort, Ort der Übertragung der Verantwortung, Ort der Eigentumsübertragung, Grenzübergangsort, Lagerhaus, Fabrik/Werk, Ort der endgültigen Bestimmung der Waren, Ort der Verkaufsbedingungen, Abfertigungszollstelle, Übergabehafen, Eingangshafen, Land, Stadt, Ursprungsland, Warenbestimmungsland, Bahnhof, Ursprungsland, Gebäude, Beginn des anrechenbaren Abschnitts, Entladehafen, Verladehafen, Ausfuhr-/Versandland, Endbestimmungsland, Land der letzten Sendung, Land der ersten Bestimmung, Produktionsland, Handelsland, Eingangszollstelle, Ausgangszollstelle, Ort der Zollbeschau, Ort der Beglaubigung des Dokuments, Bestimmungszollstelle (Versand), Versandregion, Bestimmungsregion, Erzeugungsregion, Transitland, Transitzollstelle, Land der ungültigen Transitbürgschaft, Bestimmungsland (Transit), Gebühren- und Frachtschuldner, Herstellungsabteilung, Gebühren- und Frachtschuldner, Ende des gebührenpflichtigen Abschnitts, Zahlungsort, Vollspurige Be- oder Entladung, Ankunftsort, Nächster Anlaufhafen, Nachlaufhafen, Erster fakultativer Entladungsort, Schnellzugsbahnhof, Stückgutbahnhof, Zweiter fakultativer Entladungsort, Nächster nicht entladener Anlaufhafen, Dritter fakultativer Entladeort, Wiedervereinigungspunkt, Vierter fakultativer Entladeort, Konnossement-Freigabestelle, Umladung ohne diesen Ort, Umladung auf diesen Ort beschränkt, Ursprünglicher Verladehafen, Erster Anlaufhafen - nicht entladen, Erster Anlaufhafen - entladen, Ort/Hafen der ersten Einfahrt, Versandort, Fünfter fakultativer Entladeort, Vorlaufhafen, Lieferort (bei Nachlauf), Übernahmeort des Beförderungsvertrags, Bestimmungsort des Beförderungsvertrags, Land der gültigen Transitgarantie, Ort/Hafen der ersten Ankunft des Beförderungsmittels, Ort des Empfangs, Ort der Registrierung, Ort/Ort, an dem besondere Behandlungen stattgefunden haben oder stattfinden müssen, Ort der Ausstellung der Dokumente, Routing, Ort der Anwendung der zusätzlichen Kosten, Ort der Hinterlegung der Dokumente, fakultativer Entladeort, Ort der Versendung der leeren Ausrüstung, Ort der Rückgabe der leeren Ausrüstung, Ort/Hafen des Lagerzugangs, Land des Erstverkaufs, Land des Kaufs, Ort der Verbringung, Ort der Dekonsolidierung, Ort des Verbrauchs, Ursprungsregion, Ort der Konsolidierung, Tarifkombinationspunkt, Ort der Entscheidung über die Verlängerung des Lieferverzugs, Ort der Aufladung, Versandzollstelle, Versandland, Ausfuhrzollstelle, Ausfuhrfreizone, Ausfuhr-/Versandregion, Abgangszollstelle, Zollstelle der Durchfuhrbürgschaft, Umladeland, Verkaufsland, Bestimmungszollstelle, Waggonladebahnhof, Gleisanschluss, Letzter Ort/Anlaufhafen der Beförderung, Land des vorangegangenen Zollverfahrens, Zollstelle für die Registrierung der vorangegangenen Zollanmeldung, Standort des teilnehmenden Absenders, Lohnverhandlungsbezirk, Ort der endgültigen Bestimmung der Beförderung, Ort der Beladung mit leeren Ausrüstungen, Ort der Entladung leerer Ausrüstungen, Liefergebiet, Erdöllager, Ort des Eingangs (Zoll), Ort der Pflege lebender Tiere, Ort der Wiedervereisung, Ort der Verwiegung, Rangierbahnhof, Einkaufsstation, Laderampe, Hafenanschluss, Ort des Verfalls, Verhandlungsort, Ort der fälligen Forderungen, Akkreditiv verfügbar in, Stauzelle, Für den Transport nach, Verladung an Bord/Versand/Übernahme an/von, Privatbox, Nächster Löschhafen, Anlaufhafen, Ort/Ort der Anmietung, Ort/Ort der Abmietung, Terminal anderer Beförderer, Land, in dem die Mehrwertsteuer (MwSt.) anfällt, Kontaktort, Zusätzlicher interner Bestimmungsort, Ausländischer Anlaufhafen, Wartungsort Gegenseitig definiert". Siehe [UNTDID - D.95B - Segment TDT - LOC - 3227](https://service.unece.org/trade/untdid/d95b/uncl/uncl3227.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `originTransportType[string]`: Code der Beförderungsart (UN/ECE). Siehe [UNTDID - D.95B - Segment TDT - C220 (8067)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8067.htm) und [UN/ECE - Rec 19](https://unece.org/trade/uncefact/cl-recommendations)  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `receiverIdentification[string]`: Interchange Recipient Identification. Siehe [UN/EDIFACT - S003](https://unece.org/trade/uncefact/unedifact/part-4-Annex-B)  . Model: [https://schema.org/Text](https://schema.org/Text)- `release[string]`: Versionsnummer innerhalb der aktuellen Versionsnummer. Siehe [UNTDID - D.95B - UNH - S009 (0054)](https://service.unece.org/trade/untdid/d95b/trmd/codeco_d.htm#DSGI)  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `senderIdentification[string]`: Interchange Sender Identification. Siehe [UN/EDIFACT - S002] (https://unece.org/trade/uncefact/unedifact/part-4-Annex-B)  . Model: [https://schema.org/Text](https://schema.org/Text)- `sentAt[date-time]`: Datum und Uhrzeit des Versands der Nachricht im Format ISO 8601 UTC. Siehe [UN/EDIFACT - S004](https://unece.org/trade/uncefact/unedifact/part-4-Annex-B)  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der vollständig qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `travelReference[string]`: Referenznummer der Beförderung. Siehe [UNTDID - D.95B - Segment TDT - 8028](https://service.unece.org/trade/untdid/d95b/uncl/uncl8028.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `truckLicenseCode[string]`: Nummernschild des Lastwagens. Siehe [UNTDID - D.95B - Segment TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI-Entitätstyp. Es muss EdiCodeco sein  - `vesselCallSign[string]`: Maritime Rufzeichen sind Rufzeichen, die Schiffen als eindeutige Identifikatoren zugewiesen werden. Siehe [UNTDID - D.95B - Segment TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselCarrier[string]`: Vessel carrier Identification (Identifizierung der Partei, die den Transport von Gütern zwischen den genannten Punkten durchführt oder organisiert). Siehe [UNTDID - D.95B - Segment TDT - C040 (3127)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3127.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselImo[number]`: Nummer der Internationalen Seeschifffahrtsorganisation (eine globale UID für immer). Siehe [UNTDID - D.95B - Segment TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)  . Model: [https://schema.org/Number](https://schema.org/Number)- `vesselMmsi[number]`: Marine Mobile Service Identity Number (eine vorübergehend zugewiesene UID, die vom aktuellen Flaggenstaat des Objekts vergeben wird). Siehe [UNTDID - D.95B - Segment TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)  . Model: [https://schema.org/Number](https://schema.org/Number)- `vesselName[string]`: Name des Schiffes. Siehe [UNTDID - D.95B - Segment TDT - C222 (8212)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8212.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselVoyage[string]`: Referenznummer der Schiffsreise. Siehe [UNTDID - D.95B - Segment RFF - C506 (1154)](https://service.unece.org/trade/untdid/d95b/uncl/uncl1154.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `containerIdentification`  - `id`  - `type`  - `vesselImo`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
## Beispiel-Nutzlasten  
#### EdiCodeco NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen EdiCodeco im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
#### EdiCodeco NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen EdiCodeco im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
#### EdiCodeco NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für ein EdiCodeco im JSON-LD Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### EdiCodeco NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein EdiCodeco im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
