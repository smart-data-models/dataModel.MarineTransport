<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: KeyVessel  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/KeyVessel/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Il modello di dati è destinato a fornire informazioni sulle navi chiave su cui la comunità portuale deve concentrare il proprio lavoro nei prossimi giorni. Consente di rappresentare le proprietà di ogni nave: informazioni statiche e dinamiche**  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o formati/pattern diversi</sub></sup>  
- `address[object]`: L'indirizzo di posta  . Modello: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, Spagna  . Modello: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La località in cui si trova l'indirizzo di strada e che si trova nella regione  . Modello: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La regione in cui si trova la località e che si trova nel paese  . Modello: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestito dal governo locale    
	- `postOfficeBoxNumber[string]`: Il numero della casella postale per gli indirizzi di posta  . Ad esempio, 03578  . Modello: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Modello: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'indirizzo di strada  . Modello: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numero che identifica una proprietà specifica in una strada pubblica    
- `alternateName[string]`: Un nome alternativo per questo elemento  - `areaServed[string]`: L'area geografica in cui un servizio o un elemento offerto è fornito  . Modello: [https://schema.org/Text](https://schema.org/Text)- `callSign[string]`: I segnali di chiamata marittimi sono segnali di chiamata assegnati come identificatori univoci alle navi  . Modello: [https://schema.org/Text](https://schema.org/Text)- `courseOverGround[number]`: Corsa sul fondo (COG)  . Modello: [https://schema.org/Number](https://schema.org/Number)- `createdDate[date-time]`: Data e ora di creazione dell'entità rappresentata in formato ISO 8601 UTC  . Modello: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità dei dati armonizzati  . Modello: [https://schema.org/Text](https://schema.org/Text)- `dateCreated[date-time]`: Timestamp di creazione dell'entità. Questo sarà solitamente assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Questo sarà solitamente assegnato dalla piattaforma di archiviazione  - `deletedDate[date-time]`: Data e ora di cancellazione dell'entità rappresentata in formato ISO 8601 UTC  . Modello: [https://schema.org/Text](https://schema.org/Text)- `description[string]`: Una descrizione di questo elemento  - `etaAis[date-time]`: Ora stimata di arrivo, come segnalata dal sistema AIS, rappresentata in formato ISO 8601 UTC  . Modello: [https://schema.org/Text](https://schema.org/Text)- `etaAlgorithm[date-time]`: Ora stimata di arrivo, calcolata da un algoritmo basato sulle posizioni della nave, rappresentata in formato ISO 8601 UTC  . Modello: [https://schema.org/Text](https://schema.org/Text)- `flagCode[string]`: I segnali di chiamata marittimi sono segnali di chiamata assegnati come identificatori univoci alle navi  . Modello: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: Identificatore univoco dell'entità  - `imo[number]`: Numero di identificazione dell'Organizzazione marittima internazionale (un UID globale e permanente)  . Modello: [https://schema.org/Number](https://schema.org/Number)- `lastPortCode[string]`: Ultimo porto di chiamata, codificato. Il codice che rappresenta il porto immediatamente precedente al porto di arrivo, se disponibile. [EMSWe: DE-005-05] [EDIFACT:LOC-3227-92] [IMO:IMO0076]   . Modello: [https://schema.org/Text](https://schema.org/Text)- `latitude[number]`: Coordinate di latitudine della nave  - `location[*]`: Riferimento Geojson alla posizione della nave. Deve essere un punto in cui la nave si trovava alla data observedDate  - `longitude[number]`: Coordinate di longitudine della nave  - `mmsi[number]`: Numero di identità del servizio mobile marittimo (un UID temporaneamente assegnato, rilasciato dallo stato attuale della bandiera dell'oggetto)  . Modello: [https://schema.org/Number](https://schema.org/Number)- `modifiedDate[date-time]`: Data e ora dell'ultima modifica dell'entità rappresentata in formato ISO 8601 UTC  . Modello: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: Il nome di questo elemento  - `navigationStatus[number]`: Enum:'0=In movimento con motore, 1=All'ancora, 2=Non in comando, 3=Manovrabilità limitata, 4=Limitato dalla sua immersione, 5=All'ancora, 6=A terra, 7=Impegnato nella pesca, 8=In movimento a vela, 9=Riservato per future modifiche dello stato di navigazione per HSC, 10=Riservato per future modifiche dello stato di navigazione per WIG, 11=Riservato per uso futuro, 12=Riservato per uso futuro, 13=Riservato per uso futuro, 14=AIS-SART è attivo, 15=Non definito (predefinito)'. Stato di navigazione. Formato dei dati AIVDM/AIVDO'  . Modello: [https://schema.org/Number](https://schema.org/Number)- `nextPortCode[string]`: Prossimo porto di chiamata, codificato. Il codice che rappresenta il porto immediatamente successivo al porto di arrivo, se disponibile. Relativo a IALA_S211:nextPortCallCod / IMO. [EMSWe: DE-005-07] [EDIFACT:LOC-3227-61] [IMO:IMO0120]  . Modello: [https://schema.org/Text](https://schema.org/Text)- `observedDate[date-time]`: Data e ora di questa osservazione rappresentata in formato ISO 8601 UTC  . Modello: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: Un elenco che contiene una sequenza di caratteri in formato JSON che fa riferimento agli ID univoci dei proprietari  - `portCallNumber[string]`: Identificatore di chiamata al porto in formato MRN. Il primo elemento del NSS dovrebbe essere il codice UN/LOCODE di 5 caratteri del porto, seguito dall'anno e terminando con un numero sequenziale univoco nel porto [LLLLLYYYY99999] dove LLLLL è il codice UN/LOCODE del porto visitato, YYYY è l'anno e 99999 è un numero sequenziale univoco assegnato dall'autorità portuale univoco per ogni anno (ad esempio ESHUV202310323). Un abbreviazione può essere utilizzata per il codice UN/LOCODE (ad esempio H202310323). L'identificatore di chiamata al porto è assegnato durante i primi passaggi della visita, ma potrebbe essere nullo all'inizio. Negli standard internazionali è anche noto come [ID di chiamata al porto], [ID di visita] o [Chiamata al porto codificata]. Vedi [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) [EMSWe: DG-004/DG-004-01] [EDIFACT:BGM-1004] [IALA_S211:portCallId] [IMO:IMO108+IMO0153]  . Modello: [https://schema.org/Text](https://schema.org/Text)- `portCallRef[uri]`: Riferimento all'entità PortCall padre. [NGSI-MarineTransport.PortCall.id]  - `portCode[string]`: Codice delle Nazioni Unite per il commercio e i trasporti. Vedi [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) [EMSWe: DE-004-04] [EDIFACT:LOC-3227-153] [IALA_S211:portCode] [IMO:IMO0108]   . Modello: [https://schema.org/Text](https://schema.org/Text)- `positionAccuracy[number]`: Enum:'0=Basso (> 10 m; modalità autonoma di ad esempio ricevitore di sistema di navigazione satellitare globale (GNSS) o di altro dispositivo di fissaggio della posizione elettronica; predefinito), 1=Alto (< 10 m; modalità differenziale di ad esempio ricevitore DGNSS)'. Codice per l'accuratezza della bandiera della posizione della nave  . Modello: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che fornisce la fonte originale dei dati dell'entità come URL. Consigliato di essere il nome di dominio completamente qualificato del fornitore di origine o l'URL dell'oggetto di origine  - `speedOverGround[number]`: Velocità sul fondo (SOG)  . Modello: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Tipo di entità NGSI. Deve essere KeyVessel  - `vesselAtPort[boolean]`: La nave si trova all'interno dei limiti del porto, compreso l'attesa all'esterno, all'ingresso del porto, in attesa di istruzioni, ecc  . Modello: [https://schema.org/Boolean](https://schema.org/Boolean)- `vesselName[string]`: Nome della nave  . Modello: [https://schema.org/Text](https://schema.org/Text)- `vesselRef[uri]`: Riferimento all'entità MasterVessel padre. [NGSI-MarineTransport.MasterVessel.id]- urn:mrn:<oid>:portcalls:mastervessel:id:9999  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Descrizione del modello di dati delle proprietà  
Ordinate alfabeticamente (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>dettagli yaml completi</strong></summary>    
```yaml  
KeyVessel:    
  description: 'The data model is intended to provide information about key vessels that a port community must focus his work on next days. It allows to represent the properties of each vessel: static and dynamic information'    
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
    callSign:    
      description: Maritime call signs are call signs assigned as unique identifiers to vessels    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    courseOverGround:    
      description: Course Over Ground (COG)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: degree    
    createdDate:    
      description: Date and time of creation of the entity represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      enum:    
        - AIS    
        - AISHUB    
        - ALGORITHM    
        - IA    
        - MARINETRAFFIC    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    deletedDate:    
      description: Date and time of deletion of the entity represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    etaAis:    
      description: Estimated time of arrival, as it is reported by AIS system, represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    etaAlgorithm:    
      description: Estimated time of arrival, computed by an algorithm based on vessel's positions, represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    flagCode:    
      description: Maritime call signs are call signs assigned as unique identifiers to vessels    
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
        type: Relationship    
    imo:    
      description: International Maritime Organization Number (a global forever UID)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    lastPortCode:    
      description: 'Last port of call, coded.The code representing the port immediately previous to the port of arrival, if available. [EMSWe: DE-005-05] [EDIFACT:LOC-3227-92] [IMO:IMO0076] '    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    latitude:    
      description: Latitude coordinate of the vessel    
      type: number    
      x-ngsi:    
        type: Property    
    location:    
      '@id': http://uri.etsi.org/ngsi-ld/location    
      '@type': https://uri.etsi.org/ngsi-ld/GeoProperty    
      description: Geojson reference to the vessel position. It must be a Point where the vessel was placed at observedDate date    
      x-ngsi:    
        type: GeoProperty    
    longitude:    
      description: Longitude coordinate of the vessel    
      type: number    
      x-ngsi:    
        type: Property    
    mmsi:    
      description: Marine Mobile Service Identity Number (a temporarily assigned UID, issued by that object's current flag state)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    modifiedDate:    
      description: Date and time of last modification of the entity represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    navigationStatus:    
      description: Enum:'0=Under way using engine, 1=At anchor, 2=Not under command, 3=Restricted manoeuverability,4=Constrained by her draught, 5=Moored, 6=Aground, 7=Engaged in Fishing, 8=Under way sailing, 9=Reserved for future amendment of Navigational state for HSC, 10=Reserved for future amendment of Navigational Status for WIG, 11=Reserved for future use, 12=Reserved for future use,13=Reserved for future use, 14=AIS-SART is active, 15=Not defined (default)'. Navigation Status. AIVDM/AIVDO data format'    
      enum:    
        - 0    
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
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    nextPortCode:    
      description: 'Next port of call, coded.The code representing the port immediately previous to the port of arrival, if available.. Related to IALA_S211:nestPortCallCod / IMO. [EMSWe: DE-005-07] [EDIFACT:LOC-3227-61] [IMO:IMO0120]'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    observedDate:    
      description: Date and time of this observation represented by an ISO 8601 UTC format    
      format: date-time    
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
          type: Relationship    
      type: array    
      x-ngsi:    
        type: Property    
    portCallNumber:    
      description: 'Port call identifier in MRN format. First element of the NSS should be the 5 character UN/Locode of the port, later the YEAR and finishing with a sequential number in this port [LLLLLYYYY99999] where LLLLL is the UN/LOCODE of the visited port, YYYY is the year, and 99999 is a unique sequential number assigned by port authority unique on each year (i.e. ESHUV202310323). An abbreviation can be used for UN/LOCODE (i.e. H202310323). The portCallNumber is assigned during the initial steps of the visit, but could be null at the beginning. In international standards is also known as [Port Call ID], [Visit ID] or [Port Call Coded]. See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) [EMSWe: DG-004/DG-004-01] [EDIFACT:BGM-1004] [IALA_S211:portCallId] [IMO:IMO108+IMO0153]'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    portCallRef:    
      description: Reference to parent PortCall entity. [NGSI-MarineTransport.PortCall.id]    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    portCode:    
      description: 'United Nations Code for Trade and Transport Locations. See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) [EMSWe: DE-004-04] [EDIFACT:LOC-3227-153] [IALA_S211:portCode] [IMO:IMO0108] '    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    positionAccuracy:    
      description: Enum:'0=Low (> 10 m; autonomous mode of e.g.global navigation satellite system (GNSS) receiver or of other electronic position fixing device; default), 1=High (< 10 m; differential mode of e.g.DGNSS receiver)'. Code for the accuracy of the vessel position flag    
      enum:    
        - 0    
        - 1    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    speedOverGround:    
      description: Speed Over Ground (SOG)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meters per second    
    type:    
      description: NGSI Entity type. It has to be KeyVessel    
      enum:    
        - KeyVessel    
      type: string    
      x-ngsi:    
        type: Property    
    vesselAtPort:    
      description: The vessel is in port limits, including waiting outside, at the harbor entrance, awaiting instructions, etc    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    vesselName:    
      description: Vessel Name    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vesselRef:    
      description: Reference to parent MasterVessel entity. [NGSI-MarineTransport.MasterVessel.id]- urn:mrn:<oid>:portcalls:mastervessel:id:9999    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/KeyVessel/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/VesselAtPort/schema.json    
  x-model-tags: I4Trust    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload    
#### Esempio di KeyVessel in formato NGSI-v2 valori chiave    
Ecco un esempio di KeyVessel in formato JSON come valori chiave. Questo è compatibile con NGSI-v2 quando si utilizza `options=keyValues` e restituisce i dati di contesto di un'entità individuale.  
<details><summary><strong>mostra/nascondi esempio</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:portcallvessel:id:1234",  
  "type": "KeyVessel",  
  "vesselRef": "urn:mrn:eshuv:portcalls:mastervessel:imo:9863637",  
  "imo": 9863637,  
  "mmsi": 210049000,  
  "callSign": "5BPC3",  
  "flagCode": "ES",  
  "vesselName": "ELEANOR R.",  
  "portCode":   "ESHUV",  
  "lastPortCode": "ESPMI",  
  "nextPortCode": "ESVLC",  
  "portCallNumber": "ESHUV202401233",  
  "portCallRef": "urn:mrn:eshuv:portcalls:portcall:code:1233",  
  "dataProvider": "AIS",  
  "latitude": 37.2614,  
  "longitude":  -6.9447,  
  "speedOverGround": 11.3,  
  "courseOverGround": 122,  
  "navigationStatus": 4,  
  "observedDate": "2024-07-01T03:11:32Z",  
  "modifiedDate": "2024-07-01T03:07:12Z",  
  "createdDate": "2023-06-03T07:00:00Z",  
  "deletedDate": "2024-07-01T03:07:12Z"  
}  
```  
</details>  
#### Esempio di KeyVessel in formato NGSI-v2 normalizzato    
Ecco un esempio di KeyVessel in formato JSON come normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di un'entità individuale.  
<details><summary><strong>mostra/nascondi esempio</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:portcallvessel:id:1234",  
  "type": "KeyVessel",  
  "vesselRef": {  
    "type": "Text",  
    "value": "urn:mrn:eshuv:portcalls:mastervessel:imo:9863637"  
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
    "value": "ES"  
  },  
  "vesselName": {  
    "type": "Text",  
    "value": "ELEANOR R."  
  },  
  "portCode": {  
    "type": "Text",  
    "value": "ESHUV"  
  },  
  "lastPortCode": {  
    "type": "Text",  
    "value": "ESPMI"  
  },  
  "nextPortCode": {  
    "type": "Text",  
    "value": "ESVLC"  
  },  
  "portCallNumber": {  
    "type": "Text",  
    "value": "ESHUV202401233"  
  },  
  "portCallRef": {  
    "type": "Text",  
    "value": "urn:mrn:eshuv:portcalls:portcall:code:1233"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "AIS"  
  },  
  "latitude": {  
    "type": "Number",  
    "value": 37.2614  
  },  
  "longitude": {  
    "type": "Number",  
    "value": -6.9447  
  },  
  "speedOverGround": {  
    "type": "Number",  
    "value": 11.3  
  },  
  "courseOverGround": {  
    "type": "Number",  
    "value": 122  
  },  
  "navigationStatus": {  
    "type": "Number",  
    "value": 4  
  },  
  "observedDate": {  
    "type": "DateTime",  
    "value": "2024-07-01T03:11:32Z"  
  },  
  "modifiedDate": {  
    "type": "DateTime",  
    "value": "2024-07-01T03:07:12Z"  
  },  
  "createdDate": {  
    "type": "DateTime",  
    "value": "2023-06-03T07:00:00Z"  
  },  
  "deletedDate": {  
    "type": "DateTime",  
    "value": "2024-07-01T03:07:12Z"  
  }  
}  
```  
</details>  
#### Esempio di KeyVessel in formato NGSI-LD valori chiave    
Ecco un esempio di KeyVessel in formato JSON-LD come valori chiave. Questo è compatibile con NGSI-LD quando si utilizza `options=keyValues` e restituisce i dati di contesto di un'entità individuale.  
<details><summary><strong>mostra/nascondi esempio</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:KeyVessel:urn:mrn:eshuv:portcalls:portcallvessel:id:1234",  
  "type": "KeyVessel",  
  "vesselRef": "urn:mrn:eshuv:portcalls:mastervessel:imo:9863637",  
  "imo": 9863637,  
  "mmsi": 210049000,  
  "callSign": "5BPC3",  
  "flagCode": "ES",  
  "vesselName": "ELEANOR R.",  
  "portCode": "ESHUV",  
  "lastPortCode": "ESPMI",  
  "nextPortCode": "ESVLC",  
  "portCallNumber": "ESHUV202401233",  
  "portCallRef": "urn:mrn:eshuv:portcalls:portcall:code:1233",  
  "dataProvider": "AIS",  
  "latitude": 37.2614,  
  "longitude": -6.9447,  
  "speedOverGround": 11.3,  
  "courseOverGround": 122,  
  "navigationStatus": 4,  
  "observedDate": "2024-07-01T03:11:32Z",  
  "modifiedDate": "2024-07-01T03:07:12Z",  
  "createdDate": "2023-06-03T07:00:00Z",  
  "deletedDate": "2024-07-01T03:07:12Z",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Esempio di KeyVessel in formato NGSI-LD normalizzato    
Ecco un esempio di KeyVessel in formato JSON-LD come normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di un'entità individuale.  
<details><summary><strong>mostra/nascondi esempio</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:KeyVessel:urn:mrn:eshuv:portcalls:portcallvessel:id:1234",  
  "type": "KeyVessel",  
  "vesselRef": {  
    "type": "Property",  
    "value": "urn:mrn:eshuv:portcalls:mastervessel:imo:9863637"  
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
    "value": "ES"  
  },  
  "vesselName": {  
    "type": "Property",  
    "value": "ELEANOR R."  
  },  
  "portCode": {  
    "type": "Property",  
    "value": "ESHUV"  
  },  
  "lastPortCode": {  
    "type": "Property",  
    "value": "ESPMI"  
  },  
  "nextPortCode": {  
    "type": "Property",  
    "value": "ESVLC"  
  },  
  "portCallNumber": {  
    "type": "Property",  
    "value": "ESHUV202401233"  
  },  
  "portCallRef": {  
    "type": "Property",  
    "value": "urn:mrn:eshuv:portcalls:portcall:code:1233"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "AIS"  
  },  
  "latitude": {  
    "type": "Property",  
    "value": 37.2614  
  },  
  "longitude": {  
    "type": "Property",  
    "value": -6.9447  
  },  
  "speedOverGround": {  
    "type": "Property",  
    "value": 11.3  
  },  
  "courseOverGround": {  
    "type": "Property",  
    "value": 122  
  },  
  "navigationStatus": {  
    "type": "Property",  
    "value": 4  
  },  
  "observedDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-07-01T03:11:32Z"  
    }  
  },  
  "modifiedDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-07-01T03:07:12Z"  
    }  
  },  
  "createdDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2023-06-03T07:00:00Z"  
    }  
  },  
  "deletedDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-07-01T03:07:12Z"  
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
Vedi [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di misura  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->