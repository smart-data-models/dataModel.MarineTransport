<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: EdiCodeco  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/EdiCodeco/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Messaggio con cui un terminal, un deposito, ecc. conferma che i container specificati sono stati consegnati o prelevati dal vettore interno (strada, ferrovia o chiatta). Questo messaggio può essere utilizzato anche per segnalare i movimenti di container interni al terminal (escluso il carico e lo scarico della nave) e per segnalare il cambiamento di stato di uno o più container senza che questi siano stati fisicamente spostati. Vedere [UN/EDIFACT - CODECO](https://service.unece.org/trade/untdid/d19a/trmd/codeco_c.htm)**.  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale.    
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `ata[date-time]`: Ora effettiva di arrivo o partenza da/per il Terminal. (formato ISO 8601 UTC). Vedere [UNTDID - D.95B - Segmento DTM - C507 (2380)](https://service.unece.org/trade/untdid/d95b/uncl/uncl2380.htm).  . Model: [https://schema.org/Text](https://schema.org/Text)- `bookingCode[string]`: Riferimento di prenotazione. Vedi [UNTDID - D.95B - Segmento RFF - C506 (1154)](https://service.unece.org/trade/untdid/d95b/uncl/uncl1154.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerCarrierIdentification[string]`: Codice che identifica una parte coinvolta in una transazione. Vedi [UNTDID - D.95B - Segmento NAD - C082 (3039)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3039.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerClass[string]`: Classe del contenitore (indicazione dell'azione relativa all'apparecchiatura). Enum: "Continentale, Esportazione, Importazione, Rimanere a bordo, Spostamento, Trasbordo". Vedere [UNTDID - D.95B - Segmento EQD - 8249](https://service.unece.org/trade/untdid/d95b/uncl/uncl8249.htm).  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerIdentification[string]`: Identificazione del contenitore. Vedi [UNTDID - D.95B - Segmento EQD - C237 (8260)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8260.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerIsoCode[string]`: Descrizione codificata delle dimensioni e del tipo di attrezzatura. Enum 'Serbatoio rivestito di calce,Serbatoio rivestito di resina epossidica,IMO1,IMO2,IMO3,Serbatoio pressurizzato,Serbatoio refrigerato,Semifrigorifero,Serbatoio in acciaio inox,Contenitore reefer non funzionante 40 ft,Pallet box,Europallet,Pallet scandinavo,Rimorchio,Contenitore reefer non funzionante 20 ft,Pallet intercambiabile,Semirimorchio,Contenitore cisterna 20 ft,Contenitore cisterna 30 ft, Contenitore cisterna 40 ft, Contenitore IC 20 ft, Contenitore IC 30 ft, Contenitore IC 40 ft, Serbatoio frigorifero 20 ft, Serbatoio frigorifero 30 ft, Serbatoio frigorifero 40 ft, Contenitore cisterna IC 20 ft, Contenitore cisterna IC 30 ft, Contenitore cisterna IC 40 ft, Serbatoio frigorifero IC 20 ft, Serbatoio frigorifero IC 40 ft, Cassa mobile: L < 6,15m,Cassa mobile: 6,15m < L < 7,82m,Cassa mobile: 7,82m < L < 9,15m,Cassa mobile: 9,15m < L < 10,90m,Cassa mobile: 10,90m < L < 13,75m,Totebin,Contenitore a temperatura controllata 20 ft,Contenitore a temperatura controllata 40 ft'. Vedi [UNTDID - D.95B - Segmento EQD - C224 (8155)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8155.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerSeal[string]`: Il numero di un sigillo personalizzato o di un altro sigillo apposto sui contenitori. Vedi [UNTDID - D.95B - Segmento SEL - 9308](https://service.unece.org/trade/untdid/d95b/uncl/uncl9308.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerWeight[number]`: Peso del contenitore. Vedi [UNTDID - D.95B - Segmento MEA - C174 (6314)](https://service.unece.org/trade/untdid/d95b/uncl/uncl6314.htm)  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `destination[string]`: Destinazione finale del container (UN/LOCODE: United Nations Code for Trade and Transport Locations). Vedere [UNTDID - D.95B - Segment LOC - C517 (3225)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm) e [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory).  . Model: [https://schema.org/Text](https://schema.org/Text)- `destinationTransportType[string]`: Codice del metodo di trasporto (UN/ECE). Vedere [UNTDID - D.95B - Segmento TDT - C220 (8067)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8067.htm) e [UN/ECE - Rec 19](https://unece.org/trade/uncefact/cl-recommendations).  . Model: [https://schema.org/Text](https://schema.org/Text)- `dischargingPort[string]`: Porto in cui viene scaricato il container (UN/LOCODE: United Nations Code for Trade and Transport Locations). Vedere [UNTDID - D.95B - Segment LOC - C517 (3225)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm) e [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory).  . Model: [https://schema.org/Text](https://schema.org/Text)- `fileName[string]`: Nome del file del messaggio EDI Codeco  . Model: [https://schema.org/Text](https://schema.org/Text)- `functionCode[string]`: Codice che indica la funzione del messaggio. Enum='Annullamento, Aggiunta, Cancellazione, Modifica, Sostituzione, Conferma, Duplicato, Stato, Originale, Non trovato, Risposta, Non elaborato, Richiesta, Notifica anticipata, Promemoria, Proposta, Annullamento, da riemettere, Riemissione, Modifica avviata dal venditore, Sostituire solo la sezione dell'intestazione, Sostituire solo il dettaglio e il riepilogo dell'articolo, Trasmissione finale, Operazione in attesa, Istruzione di consegna, Previsione, Istruzione di consegna e previsione, Non accettato, Accettato, con modifica nella sezione dell'intestazione, Accettato senza modifica, Accettato, con modifica nella sezione di dettaglio, Copia, Approvazione, Modifica della sezione di intestazione, Accettato con modifica, Ritrasmissione, Modifica della sezione di dettaglio, Storno di un addebito, Storno di un accredito, Storno per annullamento, Richiesta di cancellazione, Fine/chiusura ordine, Conferma con modalità specifiche, Trasmissione aggiuntiva, Accettato senza riserve, Accettato con riserve, Provvisorio, Definitivo, Accettato, contenuto rifiutato, Controversia risolta, Ritiro, Autorizzazione, Proposta di modifica, Test". Cfr. [UNTDID - D.95B - BGM - 1225](https://service.unece.org/trade/untdid/d95b/uncl/uncl1225.htm).  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[string]`: Identificatore univoco dell'entità  - `isContainerEmpty[boolean]`: Informazioni sul fatto che il contenitore è pieno o vuoto. Si veda [UNTDID - D.95B - Segmento EQD - 8169](https://service.unece.org/trade/untdid/d95b/uncl/uncl8169.htm).  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `loadingPort[string]`: Porto in cui viene caricato il container (UN/LOCODE: United Nations Code for Trade and Transport Locations). Vedere [UNTDID - D.95B - Segment LOC - C517 (3225)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm) e [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory).  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `messageRaw[string]`: Messaggio grezzo di EDI Codeco  . Model: [https://schema.org/Text](https://schema.org/Text)- `messageVersion[string]`: Versione del tipo di messaggio. Vedi [UNTDID - D.95B - UNH - S009 (0052)](https://service.unece.org/trade/untdid/d95b/trmd/codeco_d.htm#DSGI)  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: Il nome di questo elemento  - `operationType[string]`: Codice che identifica la funzione di una posizione. Enum: Luogo di consegna, Luogo di pagamento, Luogo di ricevimento della merce, Luogo di partenza, Luogo di consegna, Luogo di destinazione, Luogo/porto di carico, Luogo di accettazione, Luogo/porto di scarico, Porto di scarico, Luogo di trasbordo, Ubicazione della merce, Luogo di trasferimento di responsabilità, Luogo di trasferimento di proprietà, Luogo di passaggio di frontiera, Magazzino, Fabbrica/impianto, Luogo di destinazione finale della merce, Luogo di vendita, Ufficio doganale di sdoganamento, Porto di svincolo, Porto di entrata, Paese, Città, Paese di origine, Paese di destinazione delle merci, Stazione ferroviaria, Paese di origine, Edificio, Inizio della sezione imponibile, Base di scarico, Base di carico, Paese di esportazione/spedizione, Paese di destinazione finale, Paese di ultima spedizione, Paese di prima destinazione, Paese di produzione, Paese di commercio, Ufficio doganale di entrata, Ufficio doganale di uscita, Luogo di controllo doganale, Luogo di autenticazione del documento, Ufficio doganale di destinazione (transito), Regione di spedizione, Regione di destinazione, Regione di produzione, Paese di transito, Ufficio doganale di transito, Paese di garanzia di transito non valida, Paese di destinazione (transito), Oneri e noli dovuti da, Reparto di produzione, Oneri e noli dovuti a, Fine della sezione imponibile, Luogo di pagamento, Carico o scarico a raso, Luogo di arrivo, Prossimo porto di scalo, Porto di trasporto, Primo luogo di scarico facoltativo, Stazione ferroviaria per espresso, Stazione ferroviaria per merci miste, Secondo luogo di scarico facoltativo, Prossimo porto di scalo non di scarico, Terzo luogo di scarico facoltativo, Punto di riconsolidamento, Quarto luogo di scarico facoltativo, Ufficio di rilascio della polizza di carico, Trasbordo escluso questo luogo, Trasbordo limitato a questo luogo, Porto di carico originario, Primo porto di scalo - non di scarico, Primo porto di scalo - di scarico, Luogo/porto di primo ingresso, Luogo di spedizione, Quinto luogo di scarico facoltativo, Porto di pre-trasporto, Luogo di consegna (per trasporto), Luogo di accettazione del contratto di trasporto, Luogo di destinazione del contratto di trasporto, Paese in cui è valida la garanzia di transito, Luogo/porto di arrivo iniziale del trasporto, Luogo di ricevimento, Luogo di registrazione, Luogo/luogo in cui sono avvenuti o devono avvenire trattamenti speciali, Luogo di emissione dei documenti, Instradamento, Stazione di applicazione delle spese supplementari, Luogo di deposito dei documenti, Luogo di scarico facoltativo, Luogo di spedizione del materiale vuoto, Luogo di restituzione del materiale vuoto, Luogo/porto di entrata in magazzino, Paese di prima vendita, Paese di acquisto, Luogo di trasferimento, Luogo di deconsolidamento, Luogo di consumo, Regione di origine, Luogo di consolidamento, Punto di combinazione tariffaria, Luogo di proroga della decisione di ritardo nella consegna, Luogo/località di ricarica, Ufficio doganale di spedizione, Paese di spedizione, Ufficio doganale di esportazione, Zona franca di esportazione, Regione di esportazione/spedizione, Ufficio doganale di partenza, Ufficio doganale di transito garantito, Paese di trasbordo, Paese di vendita, Ufficio doganale di destinazione, Stazione ferroviaria di carico dei carri, Luogo di destinazione finale del trasporto, Luogo di carico dell'attrezzatura vuota, Luogo di scarico dell'attrezzatura vuota, Regione di consegna, Deposito di petrolio, Luogo di entrata (Dogana), Luogo di cura degli animali vivi, Luogo di sghiacciamento, Luogo di ponderazione, Stazione di smistamento, Stazione commerciale, Banchina di carico, Collegamento portuale, Luogo di scadenza, Luogo di negoziazione, Luogo di pagamento dei crediti, Credito documentario disponibile in, Cella di stivaggio, Per il trasporto a, Carico a bordo/spedizione/presa in carico a/da, Box privato, Porto di scarico successivo, Porto di scalo, Luogo/località di nolo, Luogo/località di fuori nolo, Terminale di altri vettori, Paese di giurisdizione dell'imposta sul valore aggiunto (IVA), Luogo di contatto, Destinazione interna supplementare, Porto di scalo estero, Luogo di manutenzione Definito reciprocamente". Cfr. [UNTDID - D.95B - Segmento TDT - LOC - 3227](https://service.unece.org/trade/untdid/d95b/uncl/uncl3227.htm).  . Model: [https://schema.org/Text](https://schema.org/Text)- `originTransportType[string]`: Codice del metodo di trasporto (UN/ECE). Vedere [UNTDID - D.95B - Segmento TDT - C220 (8067)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8067.htm) e [UN/ECE - Rec 19](https://unece.org/trade/uncefact/cl-recommendations).  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `receiverIdentification[string]`: Identificazione del destinatario dell'interscambio. Vedi [UN/EDIFACT - S003](https://unece.org/trade/uncefact/unedifact/part-4-Annex-B)  . Model: [https://schema.org/Text](https://schema.org/Text)- `release[string]`: Numero di release all'interno del numero di versione corrente. Vedi [UNTDID - D.95B - UNH - S009 (0054)](https://service.unece.org/trade/untdid/d95b/trmd/codeco_d.htm#DSGI)  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `senderIdentification[string]`: Identificazione del mittente dell'interscambio. Vedi [UN/EDIFACT - S002](https://unece.org/trade/uncefact/unedifact/part-4-Annex-B)  . Model: [https://schema.org/Text](https://schema.org/Text)- `sentAt[date-time]`: Data e ora di invio del messaggio rappresentate da un formato ISO 8601 UTC. Si veda [UN/EDIFACT - S004](https://unece.org/trade/uncefact/unedifact/part-4-Annex-B).  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `travelReference[string]`: Numero di riferimento del trasporto. Vedi [UNTDID - D.95B - Segmento TDT - 8028](https://service.unece.org/trade/untdid/d95b/uncl/uncl8028.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `truckLicenseCode[string]`: Targa del camion. Vedi [UNTDID - D.95B - Segmento TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Tipo di entità NGSI. Deve essere EdiCodeco  - `vesselCallSign[string]`: I nominativi marittimi sono nominativi assegnati come identificatori unici alle navi. Vedi [UNTDID - D.95B - Segmento TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselCarrier[string]`: Identificazione del vettore marittimo (identificazione della parte che effettua o organizza il trasporto di merci tra determinati punti). Vedi [UNTDID - D.95B - Segmento TDT - C040 (3127)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3127.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselImo[number]`: Numero dell'Organizzazione marittima internazionale (un UID globale per sempre). Vedere [UNTDID - D.95B - Segmento TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm).  . Model: [https://schema.org/Number](https://schema.org/Number)- `vesselMmsi[number]`: Marine Mobile Service Identity Number (un UID temporaneamente assegnato, rilasciato dall'attuale stato di bandiera dell'oggetto). Vedere [UNTDID - D.95B - Segmento TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm).  . Model: [https://schema.org/Number](https://schema.org/Number)- `vesselName[string]`: Nome della nave. Vedere [UNTDID - D.95B - Segmento TDT - C222 (8212)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8212.htm).  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselVoyage[string]`: Numero di riferimento del viaggio della nave. Vedi [UNTDID - D.95B - Segmento RFF - C506 (1154)](https://service.unece.org/trade/untdid/d95b/uncl/uncl1154.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `containerIdentification`  - `id`  - `type`  - `vesselImo`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
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
## Esempi di payload  
#### EdiCodeco NGSI-v2 Esempio di valori chiave  
Ecco un esempio di EdiCodeco in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### EdiCodeco NGSI-v2 normalizzato Esempio  
Ecco un esempio di EdiCodeco in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
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
#### EdiCodeco NGSI-LD valori-chiave Esempio  
Ecco un esempio di EdiCodeco in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### EdiCodeco NGSI-LD normalizzato Esempio  
Ecco un esempio di EdiCodeco in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
