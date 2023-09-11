<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティエディコデコ  
============<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/EdiCodeco/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述：**ターミナル、デポなどが、指定されたコンテナが内陸輸送業者（道路、鉄道、またははしけ）によって搬入または引き取られたことを確認するためのメッセージ。このメッセージは、ターミナル内のコンテナ移動（船舶への積み込みと積み降ろしを除く）を報告したり、コンテナが物理的に移動していなくてもコンテナのステータスの変更を報告するためにも使用できる。UN/EDIFACT - CODECO](https://service.unece.org/trade/untdid/d19a/trmd/codeco_c.htm)**を参照のこと。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。    
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `ata[date-time]`: ターミナルへの到着またはターミナルからの出発の実際の時刻。(ISO 8601 UTCフォーマット)。UNTDID - D.95B - セグメント DTM - C507 (2380)](https://service.unece.org/trade/untdid/d95b/uncl/uncl2380.htm)を参照。  . Model: [https://schema.org/Text](https://schema.org/Text)- `bookingCode[string]`: 予約参照。UNTDID - D.95B - セグメントRFF - C506 (1154)](https://service.unece.org/trade/untdid/d95b/uncl/uncl1154.htm)を参照のこと。  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerCarrierIdentification[string]`: 取引当事者を識別するコード。UNTDID - D.95B - セグメント NAD - C082 (3039)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3039.htm)を参照のこと。  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerClass[string]`: Container class (コンテナクラス) (コンテナ機器に関連するアクションの表示)。列挙型：「大陸、輸出、輸入、船内残留、シフター、積み替え」。UNTDID - D.95B - セグメント EQD - 8249](https://service.unece.org/trade/untdid/d95b/uncl/uncl8249.htm)を参照。  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerIdentification[string]`: コンテナの識別。UNTDID - D.95B - セグメント EQD - C237 (8260)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8260.htm)を参照のこと。  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerIsoCode[string]`: 装置のサイズとタイプをコード化したもの。Enum 'ダイムコーティングタンク,エポキシコーティングタンク,IMO1,IMO2,IMO3,加圧タンク,冷凍タンク,半冷凍,ステンレスタンク,非稼働冷凍コンテナ40フィート,ボックスパレット,ユーロパレット,スカンジナビアパレット,トレーラー,非稼働冷凍コンテナ20フィート,交換パレット,セミトレーラ,タンクコンテナ20フィート、タンクコンテナ30フィート,タンクコンテナ40フィート,コンテナIC20フィート,コンテナIC30フィート,コンテナIC40フィート,冷蔵庫タンク20フィート,冷蔵庫タンク30フィート,冷蔵庫タンク40フィート,タンクコンテナIC20フィート,タンクコンテナIC30フィート,タンクコンテナIC40フィート,冷蔵庫タンクIC20フィート,冷蔵庫タンクIC40フィート,可動ケース：L < 6,15m,可動ケース：6,15m < L < 7,82m,可動ケース：7,82m < L < 9,15m,可動ケース：9,15m < L < 10,90m,可動ケース：10,90m < L < 13,75m,トートビン,温度調節コンテナ20フィート,温度調節コンテナ40フィート'.UNTDID - D.95B - セグメント EQD - C224 (8155)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8155.htm)を参照。  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerSeal[string]`: 容器に貼付されたカスタムシールまたは他のシールの番号。UNTDID - D.95B - セグメントSEL - 9308](https://service.unece.org/trade/untdid/d95b/uncl/uncl9308.htm)を参照。  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerWeight[number]`: コンテナの重量。UNTDID - D.95B - セグメント MEA - C174 (6314)](https://service.unece.org/trade/untdid/d95b/uncl/uncl6314.htm)を参照のこと。  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `destination[string]`: コンテナの最終仕向地（UN/LOCODE: United Nations Code for Trade and Transport Locations）。UNTDID - D.95B - Segment LOC - C517 (3225)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm)及び[UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)を参照のこと。  . Model: [https://schema.org/Text](https://schema.org/Text)- `destinationTransportType[string]`: 輸送方法コード（UN/ECE）。UNTDID - D.95B - Segment TDT - C220 (8067)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8067.htm)及び[UN/ECE - Rec 19](https://unece.org/trade/uncefact/cl-recommendations)を参照のこと。  . Model: [https://schema.org/Text](https://schema.org/Text)- `dischargingPort[string]`: コンテナが排出される港（UN/LOCODE：United Nations Code for Trade and Transport Locations）。UNTDID - D.95B - Segment LOC - C517 (3225)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm)及び[UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) を参照のこと。  . Model: [https://schema.org/Text](https://schema.org/Text)- `fileName[string]`: EDI Codecoメッセージのファイル名  . Model: [https://schema.org/Text](https://schema.org/Text)- `functionCode[string]`: メッセージの機能を示すコード。Enum='Cancellation, Addition, Deletion, Change, Replace, Confirmation, Duplicate, Status, Original, Not found, Response, Not processed, Request, Advance notification, Reminder, Proposal, Cancel, to be reissue, Reissue, Seller initiated change, Replace heading section only, Replace item detail and summary only, Final transmission, Transaction on hold, Delivery instruction, Forecast, Delivery instruction and forecast, Not accepted, Accepted, with amendment in heading section, Accepted without amendment、詳細部訂正あり、コピー、承認、見出し部変更、訂正あり、再送、詳細部変更、借方取消、貸方取消、取消、削除依頼、注文完了・締切、特定手段による確認、追加送信、引当なし受付、引当あり受付、仮受付、確定、受付、内容否認、紛争解決、取消、承認、訂正案、テスト」。UNTDID - D.95B - BGM - 1225](https://service.unece.org/trade/untdid/d95b/uncl/uncl1225.htm)を参照。  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[string]`: エンティティの一意識別子  - `isContainerEmpty[boolean]`: コンテナが満杯か空かの情報。UNTDID - D.95B - セグメント EQD - 8169](https://service.unece.org/trade/untdid/d95b/uncl/uncl8169.htm)を参照。  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `loadingPort[string]`: コンテナが積み込まれる港(UN/LOCODE: United Nations Code for Trade and Transport Locations)。UNTDID - D.95B - Segment LOC - C517 (3225)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm)及び[UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)を参照のこと。  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `messageRaw[string]`: EDIコデコの生メッセージ  . Model: [https://schema.org/Text](https://schema.org/Text)- `messageVersion[string]`: メッセージタイプのバージョン。UNTDID - D.95B - UNH - S009 (0052)](https://service.unece.org/trade/untdid/d95b/trmd/codeco_d.htm#DSGI)を参照。  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: このアイテムの名前  - `operationType[string]`: 場所の機能を識別するコード。列挙する：'引渡条件地、支払地、商品受取地、出発地、引渡地、仕向地、積地/港、荷受地、荷卸地/港、港、積替地、商品所在地、責任移転地、所有権移転地、国境通過地、倉庫、工場/プラント、商品最終仕向地、販売地、通関事務所、出港地、入港地、国、都市、原産国、仕向国、鉄道駅、原産国、建物、課徴金対象区間の始点、搬出基点、積込基点、輸出・発送国、最終仕向国、最終委託国、第一仕向国、生産国、貿易国、入国税関事務所、出国税関事務所、税関審査場所、書類認証場所、仕向（通過）税関事務所、発送地域、仕向（通過）税関事務所仕向地, 生産地, 通過国, 通過税関事務所, 無効な通過保証の国, 仕向地(通過)国, 使用料及び運賃の支払先, 製造部門, 使用料及び運賃の支払先, 使用料欄の終わり, 支払場所, フルトラックローディングまたはアンローディング, 到着地, 次の寄港地, オンキャリッジ港, 第1の任意の荷降ろし場所, 急行鉄道駅, 混載鉄道駅, 第2の任意の荷降ろし場所、次の非排出寄港地、第3の任意の搬出地、再集積地、第4の任意の搬出地、船荷証券発行所、当地を除く積替地、当地に限定された積替地、最初の積地、最初の非排出寄港地、最初の搬出寄港地、最初の入港地・港、発送地、第5の任意の搬出地、前運送港、引渡地（オンキャリッジによる）、運送契約受入地、運送契約書受領地、運送契約書仕向地、有効な通過保証のある国、運送品初回到着地・港、受領地、登録地、特別な処置が行われた、または行わなければならない地・場所、書類発行地、経路、追加費用適用地、書類寄託地、任意荷揚げ地、空荷装置発送地、空荷装置返送地、入庫地・港、初回販売地、購入地、振替地、混載解除地、消費地、原産地、混載地、運賃合算地、延着決定地、充電地・場所、出港税関支署、出港国、輸出税関支署、輸出自由区域、輸出・出港地域、出港税関支署、通過保証税関支署、積替国、販売国、仕向税関支署、貨車積込鉄道駅、サイディング、輸送の最終寄港地/港、前回の税関手続きの国、前回の税関申告の登録の税関事務所、参加者の送り主の場所、賃金交渉地区、輸送の最終目的地、空の機器の積込み場所、空の機器の排出場所、配達地域、石油倉庫、入国地（税関）、家畜の世話場所、再氷結場所、計量場所、マーシャリングヤード、ショッピングステーション、ローディングドック、港湾接続、期限切れ場所、交渉場所、クレーム支払場所、文書信用供与可能場所、保管場所、輸送先、船積み／出港／引取場所、専用ボックス、次の積出港、寄港地、オンハイヤー場所／場所、オフハイヤー場所／場所、他の輸送会社のターミナル、付加価値税（VAT）管轄国、連絡場所、追加内航目的地、外国寄港地、整備場所 相互に定義される'.UNTDID - D.95B - セグメント TDT - LOC - 3227](https://service.unece.org/trade/untdid/d95b/uncl/uncl3227.htm)を参照のこと。  . Model: [https://schema.org/Text](https://schema.org/Text)- `originTransportType[string]`: 輸送方法コード（UN/ECE）。UNTDID - D.95B - Segment TDT - C220 (8067)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8067.htm)及び[UN/ECE - Rec 19](https://unece.org/trade/uncefact/cl-recommendations)を参照のこと。  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `receiverIdentification[string]`: Interchange Recipient Identification（交換受信者識別）。UN/EDIFACT - S003](https://unece.org/trade/uncefact/unedifact/part-4-Annex-B)を参照のこと。  . Model: [https://schema.org/Text](https://schema.org/Text)- `release[string]`: 現在のバージョン番号内のリリース番号。UNTDID - D.95B - UNH - S009 (0054)](https://service.unece.org/trade/untdid/d95b/trmd/codeco_d.htm#DSGI)を参照。  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `senderIdentification[string]`: Interchange Sender Identification（交換送信者識別）。UN/EDIFACT - S002](https://unece.org/trade/uncefact/unedifact/part-4-Annex-B)を参照のこと。  . Model: [https://schema.org/Text](https://schema.org/Text)- `sentAt[date-time]`: メッセージの送信日時はISO 8601 UTCフォーマットで表される。UN/EDIFACT - S004](https://unece.org/trade/uncefact/unedifact/part-4-Annex-B)を参照。  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `travelReference[string]`: 輸送参照番号。UNTDID - D.95B - セグメント TDT - 8028](https://service.unece.org/trade/untdid/d95b/uncl/uncl8028.htm)を参照のこと。  . Model: [https://schema.org/Text](https://schema.org/Text)- `truckLicenseCode[string]`: トラックのナンバープレート。UNTDID - D.95B - セグメントTDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)を参照。  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSIエンティティタイプ。EdiCodecoでなければならない。  - `vesselCallSign[string]`: 海上コールサインとは、船舶に固有の識別子として割り当てられるコールサインのこと。UNTDID - D.95B - セグメントTDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)を参照のこと。  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselCarrier[string]`: Vessel carrier Identification (指定された地点間の商品の輸送を引き受けまたは手配する当事者の識別)。UNTDID - D.95B - セグメント TDT - C040 (3127)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3127.htm)を参照のこと。  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselImo[number]`: 国際海事機関番号（グローバルな永久UID）。UNTDID - D.95B - セグメントTDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)を参照。  . Model: [https://schema.org/Number](https://schema.org/Number)- `vesselMmsi[number]`: 海上移動サービス識別番号(Marine Mobile Service Identity Number)（そのオブジェクトの現在のフラグ状態によって発行される、一時的に割り当てられたUID）。UNTDID - D.95B - セグメント TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)を参照。  . Model: [https://schema.org/Number](https://schema.org/Number)- `vesselName[string]`: 船舶名。UNTDID - D.95B - セグメント TDT - C222 (8212)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8212.htm)を参照。  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselVoyage[string]`: 航海の参照番号。UNTDID - D.95B - セグメント RFF - C506 (1154)](https://service.unece.org/trade/untdid/d95b/uncl/uncl1154.htm)を参照。  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `containerIdentification`  - `id`  - `type`  - `vesselImo`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
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
## ペイロードの例  
#### EdiCodeco NGSI-v2 キー値の例  
JSON-LD形式のEdiCodecoのkey-valuesの例です。options=keyValues`を使うとNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返す。  
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
#### EdiCodeco NGSI-v2 正規化例  
正規化されたJSON-LD形式のEdiCodecoの例です。これは、オプションを使わない場合はNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### EdiCodeco NGSI-LD キー値の例  
JSON-LD形式のEdiCodecoのkey-valuesの例です。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。  
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
#### エディコデコ NGSI-LD 正規化例  
正規化されたJSON-LD形式のEdiCodecoの例です。これは、オプションを使わない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
