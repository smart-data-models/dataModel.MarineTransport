<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティバース  
=========<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/Berth/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述：**このデータモデルはバースに関する情報を提供することを意図している。バース」は、港湾施設（バース）および停泊地として、PortCall中の船舶の各停泊地と定義する。各バースには、停泊時間（予定、計画など）、ライフサイクル（予定、要求、承認など）、停泊中の主な活動（商業運航、大規模修繕など）、および以下に説明するいくつかの属性がある。商業運転が行われる場合、Operationエンティティは各商業運転の詳細を定義する**。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `activityCode[string]`: 停泊中の活動。貨物作業や、船と港の活動に関連するいくつかの活動である。列挙する：ZGR=大修理、ZPV=提供、ZCA=造船所建設、ZRA=造船所大修理、ZRF=乗組員による洋上修理、ZRT=乗組員以外の人員による停泊中修理、ZDA=造船所スクラップ、ZTA=造船所改造、ZTF=改造；ZVO=公式訪問; ZAF=強制到着; ZIN=非活動的; ZIP=漁業非活動的; ZAR=停泊中の提供; ZAO=停泊中の提供; ZAB=はしけによる停泊中の提供; ZOP=商業交通の港湾業務; ZCT=観光クルーズ; ZTI=内部交通；ZBO=進水、ZCO=建造、ZRE=曳船、ZDE=スクラップヤード、ZAP=鮮魚の荷役作業を行う漁船及び職人船、ZDR=浚渫船、ZPB=生物学的停止、ZCL=無免許、ZDJ=司法供託；ZMR=係留サービス目的の船舶、ZPR=水先サービス目的の船舶、ZRM=トレーラー、ZVA=スリップウェイへのアクセス、ZDS=乾ドック内の船舶、ZOT=その他、EST=ステイ、ZSA=水供給、ZSH=氷供給、ZSE=電気エネルギー供給、ZSC=燃料供給、ZSV=ビクタリング；  . Model: [https://schema.org/Text](https://schema.org/Text)- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。    
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 公道上の特定の物件を特定する番号    
- `agentLegalCode[string]`: PortCallの船舶代理店の法的識別子コード  . Model: [https://schema.org/Text](https://schema.org/Text)- `agentName[string]`: PortCallの船舶代理店名  . Model: [https://schema.org/Text](https://schema.org/Text)- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrivalDraught[number]`: 第一線での喫水が確保され、到着航行が可能  . Model: [https://schema.org/Number](https://schema.org/Number)- `ataBerth[date-time]`: ISO 8601 UTCフォーマットで表される、バースへの実際の到着時刻  - `atdBerth[date-time]`: ISO 8601 UTCフォーマットで表される。バース出港時刻  - `authorizationRemarks[string]`: 港湾局による接岸条件  . Model: [https://schema.org/Text](https://schema.org/Text)- `authorizedAt[date-time]`: ISO 8601 UTCフォーマット、港湾局および海事局による認可日時で表される。  - `berthCode[string]`: 本船が停泊する港湾施設を特定するコード。フォーマット<oid>:berth:99999  . Model: [https://schema.org/Text](https://schema.org/Text)- `berthName[string]`: 本船寄港地の港湾施設名  . Model: [https://schema.org/Text](https://schema.org/Text)- `berthingTypeCode[string]`: インターフェース船港における停泊／係留のタイプを識別するためのコード。列挙する：AEX=右舷着岸、AX1=左舷着岸、AEV=右舷着岸、REM=桟橋で右舷着岸、REX=右舷着岸、RE1=左舷着岸、RE2=右舷着岸；RPM=つま先からバネへのねじれ; RPV=先端から船に乗り上げる; RPX=ポイントに乗り上げる; RXM=ドックに横付けする; RXV=他の船に係留する; RXX=係留する; RX1=船首に絡まる; AE1=右舷船首にひびが入る; AE2=右舷船尾にひびが入る; APM=桟橋に横付けする; APV=船に横付けする；APX=ポイントドッキング; AXM=桟橋にドッキング; AXV=船にドッキング; AXX=ドッキング; AX2=船尾にドッキング; FBM=桟橋に左舷にアンカー; FBV=船に左舷にアンカー; FBX=港にアンカー; FB1=船首に左舷にアンカー; FB2=船尾に左舷にアンカー; FEM=桟橋に右舷にアンカー；FEV=右舷から船へ錨泊、FEX=右舷から船へ錨泊、FE1=右舷から船首へ錨泊、FE2=右舷から船尾へ錨泊、FPM=桟橋へ錨泊、FPV=先端から船へ錨泊、FPX=ポイント錨泊、FP1=先端から船首へ錨泊、FP2=先端から船尾へ錨泊、FXM=桟橋へ錨泊、FXV=船へ錨泊；FX1=船首側で錨泊、FX2=船尾側で錨泊、RBM=舷側でドックに係留、RBX=舷側で錨泊、RB1=船首側で舷側で錨泊、RB2=船尾側で舷側で錨泊、RX2=船尾側で錨泊、YBM=桟橋で舷側ブイに係留、YBV=舷側でブイに係留；YBX=左舷ブイに繋留、YB1=船首で左舷ブイに繋留、YB2=船尾で左舷ブイに繋留、YEM=桟橋で右舷ブイに繋留、YEV=船の右舷ブイに繋留、YEX=右舷ブイに繋留、YE1=船首で右舷ブイに繋留、YE2=船尾で右舷ブイに繋留；YPM=桟橋でエンドブイに繋留、YPV=船尾からブイに繋留、YPX=先端ブイに繋留、YP1=船首で先端ブイに繋留、YP2=船尾で先端ブイに繋留、YXM=桟橋でブイに繋留、YXV=船側でブイに繋留、YX1=船首でブイに繋留；YX2=船尾でブイに繋留される; ABM=桟橋に係留される港; AEM=ドックに右舷で係留される; FXX=係留される; YXX=それ以上の指示なしにブイに繋留される; AP1=船首で先端に係留される; AP2=前後にポケットされる; RBV=船に左舷で係留される; REV=船に右舷で係留される; 。  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `departureDraught[number]`: 出発航行のために最終ラインで解放された喫水  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: この商品の説明  - `etaBerth[date-time]`: ISO 8601 UTC フォーマット、港湾局によって予想されるバースへの到着予定日時（ISO 8601 UTC フォーマット）で表される。[EMSWe: DE-005-09] [EDI: DTM-2005-132] [S211: locationState.timeType.ESTIMATED] [IMO: IMO0064] を参照のこと。  - `etdBerth[date-time]`: ISO 8601 UTC フォーマットで表される、港湾局によって予想されるバース出港予定日時。[EMSWe: DE-005-04] [EDI: DTM-2005-133] [S211: locationState.timeType.ESTIMATED] [IMO: IMO0066]。  - `firstBollard[string]`: 港湾施設初のボラード識別装置  . Model: [https://schema.org/Text](https://schema.org/Text)- `gln[number]`: ISO/IEC 6523:'https://schema.org/Number'.ロケーションのオプションコード。グローバル・ロケーション・ナンバー（GLN）は、13桁のユニークな番号であり、サプライチェーン内のあらゆるロケーションに割り当てられ、世界中で一意に識別できるようにするために、ロケーションに割り当てられる。これらのGLNは、法的、物理的、および機能的な所在地を特定するために使用することができます。  - `id[*]`: エンティティの一意識別子  - `lastBollard[string]`: 港湾施設における最後のボラード識別子  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `mooringLines[number]`: 係留線の数  . Model: [https://schema.org/Number](https://schema.org/Number)- `mrn[string]`: MRN コード化された識別子。この識別子は、そのエンティティの意味とイニシエータが異なるオーガナイザによってよく知られる方法で、そのエンティティに関連付けられなければならない。この識別子は、最初に実体を作成したシステムによって割り当てられた PortCall 実体の UNIQUE 識別子でなければならない。このURNは、MRNとIETF（特にRFC 2141、RFC 5234、RFC 8141）に準拠すべきである。提案されているフォーマットは、id::='urn:mrn:<OID>:<ONSS>:portcalls:berth:id:[0-9]+'である。ここで、OID:=Organisation UN/LOCODE、OONSS:=Organization Name of Service、9999999は、バース・エンティティの発行者が自分のシステム上で識別する（つまりSQLのrow-id）増加する一意の識別子である。Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)を参照。国際標準では[Ship's Visit]とも呼ばれる。  - `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `portCallNumber[string]`: ポートコール識別子  . Model: [https://schema.org/Text](https://schema.org/Text)- `portCallRef[*]`: Relationship.親PortCallエンティティへの参照。  - `portCode[string]`: 寄港地コード  . Model: [https://schema.org/Text](https://schema.org/Text)- `ptaBerth[date-time]`: ISO 8601 UTCフォーマットで表されるバース到着予定時刻  - `ptdBerth[date-time]`: ISO 8601 UTCフォーマットで表される。バース出港予定時刻  - `remarks[string]`: 港湾代理店等による停泊の注意事項  . Model: [https://schema.org/Text](https://schema.org/Text)- `requestedAt[date-time]`: ISO 8601 UTCフォーマットで表される、船舶代理店による接岸要求の日時。  - `rtaBerth[date-time]`: ISO 8601 UTC format, Date and time of Requested Time of Arrival by ship-agent (ISO 8601 UTC format)... [EMSWe: DE-005-09] [EDI: DTM-2005-132] [S211: locationState.timeType.ESTIMATED] [IMO: IMO0064] で表される。  - `rtdBerth[date-time]`: ISO 8601 UTC フォーマットで表される、船舶代理店による出港依頼時刻の日付と時刻（ISO 8601 UTC フォーマット）。[EMSWe: DE-005-09] [EDI: DTM-2005-132] [S211: locationState.timeType.ESTIMATED] [IMO: IMO0064] を参照のこと。  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `status[string]`: 要求から承認、完了までの、その生涯におけるバーシングの現在のステータス。Enum:'ACCEPTED, AUTHORIZED, CANCELLED, COMPLETED, DENIED, INITIATED, REQUESTED, REJECTED, INVOICING, INVOICED'.[EMSWe: DE-019-07] [EDI: BGM-1225] [S211: serviceState: timeSequence:VESSEL] を参照のこと。  . Model: [https://schema.org/Text](https://schema.org/Text)- `stopRank[number]`: PortCallアクティビティにおけるこの停留所のランクまたは番号を、停留所（接岸/停泊エリア）のシーケンスにおける到着時刻順に並べたもの。  . Model: [https://schema.org/Number](https://schema.org/Number)- `terminal[string]`: ターミナルの通称  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSIエンティティタイプ。バース  - `year[number]`: 接岸開始年  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `id`  - `portCallRef`  - `stopRank`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
ERAオントロジー https://data-interop.era.europa.eu/era-vocabulary （欧州鉄道庁）からマッピングされたデータモデル。  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
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
## ペイロードの例  
#### バース NGSI-v2 キー値の例  
以下は、JSON-LD形式のバースのキー値の例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。  
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
#### バース NGSI-v2 正規化例  
以下は、正規化された JSON-LD 形式のバースの例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### バース NGSI-LD キー値の例  
バースをJSON-LD形式でkey-valuesとした例である。これはNGSI-LDと互換性があり、`options=keyValues`を使うと個々のエンティティのコンテキストデータを返す。  
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
#### バース NGSI-LD 正規化例  
以下は、正規化された JSON-LD 形式のバースの例である。これは、オプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
