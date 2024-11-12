<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティマスターベッセル  
==============<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/MasterVessel/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述：**データモデルは船舶に関する情報を提供することを意図している。各船舶の特性を表すことができる：静的情報と動的情報**。  
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
	- `streetNr[string]`: 公道上の特定の物件を特定する番号    
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `beam[number]`: 船幅  . Model: [https://schema.org/Number](https://schema.org/Number)- `buildDate[date]`: ISO 8601 UTCフォーマットで表される本船の建造日  . Model: [https://schema.org/Text](https://schema.org/Text)- `callSign[string]`: 無線で最初に接続する際の船舶の識別信号 [EMSWe: DE-065-05] [EDI: BGM-RFF] [S211: 呼出名/呼出符号] [IMO: IMO0136] 。  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `dwt[number]`: 載貨重量トン数（DWT）  . Model: [https://schema.org/Number](https://schema.org/Number)- `financialOwner[string]`: 本船の財務上の所有者  . Model: [https://schema.org/Text](https://schema.org/Text)- `flagCode[string]`: 国際国旗コード (ISO 3166-1 alfa-2)  . Model: [https://schema.org/Text](https://schema.org/Text)- `gt[number]`: 総トン数（GT）  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: エンティティの一意識別子  - `imo[number]`: 国際海事機関番号（グローバルな永久UID） [EMSWe: DE-003-03] [EDIFACT:TDT-8213] [IALA_S211:vesselId] [IMO:IMO0140] 。  . Model: [https://schema.org/Number](https://schema.org/Number)- `loa[number]`: 全長  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `manager[string]`: 通常船舶会社本船支配人  . Model: [https://schema.org/Text](https://schema.org/Text)- `maxDraught[number]`: 本船の最大喫水  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxLoadVehicle[number]`: 船舶の最大車両輸送能力  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxPassenger[number]`: 旅客輸送船の最大定員  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVehicle[number]`: 車両の最大許容寸法  . Model: [https://schema.org/Number](https://schema.org/Number)- `minNumOfCrew[number]`: 本船を運航するための最低乗組員数  . Model: [https://schema.org/Number](https://schema.org/Number)- `mmsi[number]`: 海上移動サービス識別番号（一時的に割り当てられたUIDで、そのオブジェクトの現在の旗国によって発行される）[EMSWe: DE-068-09] [EDIFACT:TDT-1131] [IALA_S211:vesselId] [IMO:IMO0178] 。  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `photo[uri]`: 船舶写真URL  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `sleeve[number]`: スリーブ  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `technicalManager[string]`: 本船テクニカルマネージャー  . Model: [https://schema.org/Text](https://schema.org/Text)- `toBow[number]`: 船首までの寸法  . Model: [http://schema.org/Number](http://schema.org/Number)- `toPort[number]`: 港までの寸法  . Model: [http://schema.org/Number](http://schema.org/Number)- `toStardboard[number]`: 右舷寸法  . Model: [http://schema.org/Number](http://schema.org/Number)- `toStern[number]`: ディメンション・トゥ・スターン  . Model: [http://schema.org/Number](http://schema.org/Number)- `type[string]`: NGSIエンティティタイプ。MasterVesselでなければならない。  - `vesselClass[string]`: 船級を表すコード。BD=ドライバルク、BO=オイルタンカー・ばら積み貨物船、BS=ばら積み貨物船荷揚げ、BY=その他のばら積み貨物船、FC=漁船、FO=移載・輸送船、GA=旅客を伴うRO-RO船、GC=特化しない一般貨物船、GD=一般貨物船、GE=ばら積み貨物船、GN=コンテナ船。RO-RO船(旅客付き); GC=Mrcia General without specialization; GD=Rest general cargo vessel; GE=Buq. transp. combined; GN=Container ship; GO=Ro-ro ship; GP=Passenger ship; GR=Refrigerator vessel; OO=Buq.化学品; TD=その他の液体バルク; TL=液化ガスの輸送; TO=石油タンカー; XD=浚渫船; XR=調査・探査船; XT=曳船・押船; XX=その他の船舶・ボート; UR=ファストパス; G=一般貨物; T=液体バルク運搬船(タンク); S=固体バルク運搬船; OB=その他の商船; UC=クルーズチケット; OC=公海漁船(冷凍船);'  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselName[string]`: 船舶名[EMSWe: DE-003-07] [EDIFACT:TDT-8212] [IMO:IMO0142].  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselOwner[string]`: 船舶所有者  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselSubType[number]`: 列挙：'0=利用不可(デフォルト),1-19=将来の使用のために予約,20=ウィング・イン・グラウンド(WIG)、このタイプの全船,21=ウィング・イン・グラウンド(WIG)、危険カテゴリA,22=ウィング・イン・グラウンド(WIG)、危険カテゴリB,23=ウィングイングラウンド(WIG),危険カテゴリC,24=ウィングイングラウンド(WIG),危険カテゴリD,25-29=ウィングイングラウンド(WIG),将来の使用のために予約,30=釣り,31=曳航,32=曳航：長さが200mを超えるか、幅が25mを超える,33=浚渫または水中作業,34=潜水作業,35=軍事作業,36=帆走,37=プレジャークラフト,38-39=予約,40=高速船(HSC)、この種の全ての船舶,41=高速船(HSC)、危険分類A,42=高速船(HSC)、危険分類B,43=高速船(HSC)、危険分類C、44=高速船(HSC)、危険カテゴリD,45-48=高速船(HSC)、将来の使用のために予約,49=高速船(HSC)、追加情報なし,50=パイロット船,51=捜索救助船,52=タグ,53=港湾用テンダー,54=汚染防止装置,55=法執行,56-57=予備-地方船,58=医療輸送,59=RR決議No.18,60=Passenger, all ships of this type,61=Passenger, Hazardous category A,62=Passenger, Hazardous category B,63=Passenger, Hazardous category C,64=Passenger, Hazardous category D,65-68=Passenger, reserved for future use,69=Passenger, No additional information、70=貨物、この種の全ての船舶,71=貨物、危険なカテゴリーA,72=貨物、危険なカテゴリーB,73=貨物、危険なカテゴリーC,74=貨物、危険なカテゴリーD,75-78=貨物、将来の使用のために予約,79=貨物、追加情報なし,80=タンカー、この型の全船,81=タンカー,危険等級A,82=タンカー,危険等級B,83=タンカー,危険等級C,84=タンカー,危険等級D,85-88=タンカー,今後の使用のため予約,89=タンカー,追加情報なし,90=その他の型、91=その他型、危険分類A,92=その他型、危険分類B,93=その他型、危険分類C,94=その他型、危険分類D,95-98=その他型、今後の使用予約,99=その他型、追加情報なし」。容器サブタイプのコード  . Model: [https://schema.org/Number](https://schema.org/Number)- `vesselType[number]`: Enum:'1=Reserved,2=Wing In Ground,3=Special Category,4=High-Speed Craft,5=Special Category,6=Passenger,7=Cargo,8=Tanker,9=Other'.船種コード  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
MasterVessel:    
  description: 'The data model is intended to provide information about vessels. It allows to represent the properties of each vessel: static and dynamic information'    
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
    beam:    
      description: Beam of the Vessel    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meters    
    buildDate:    
      description: Date of building of the vessel represented by an ISO 8601 UTC format    
      format: date    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    callSign:    
      description: 'Identification signal of a vessel when initially connecting by radio [EMSWe: DE-065-05] [EDI: BGM-RFF] [S211: Call Name / Call Sign] [IMO: IMO0136] '    
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
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    dwt:    
      description: Dead weight Tonnage (DWT)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: tons    
    financialOwner:    
      description: Financial Owner of the vessel    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    flagCode:    
      description: International Flag Code (ISO 3166-1 alfa-2)    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    gt:    
      description: Gross Tonnage (GT)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: moorson tons    
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
      description: 'International Maritime Organization Number (a global forever UID) [EMSWe: DE-003-03] [EDIFACT:TDT-8213] [IALA_S211:vesselId] [IMO:IMO0140] '    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    loa:    
      description: Length Over All of Vessel    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meters    
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
    manager:    
      description: 'Manager of the Vessel, usually Ship Company'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    maxDraught:    
      description: Maximum Draught of the vessel    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meters    
    maxLoadVehicle:    
      description: Max capacity of vessel to transport vehicles    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maxPassenger:    
      description: Max capacity of vessel to transport passengers    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maxVehicle:    
      description: Max dimensions of vehicle permitted    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    minNumOfCrew:    
      description: Minimum number of crew to operate the vessel    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    mmsi:    
      description: 'Marine Mobile Service Identity Number (a temporarily assigned UID, issued by that object''s current flag state)[EMSWe: DE-068-09] [EDIFACT:TDT-1131] [IALA_S211:vesselId] [IMO:IMO0178]'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
          type: Relationship    
      type: array    
      x-ngsi:    
        type: Property    
    photo:    
      description: Vessel Photo URL    
      format: uri    
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
    sleeve:    
      description: Sleeve of Vessel    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meters    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    technicalManager:    
      description: Technical Manager of the vessel    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    toBow:    
      description: Dimension to Bow    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: meters    
    toPort:    
      description: Dimension to Port    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: meters    
    toStardboard:    
      description: Dimension to Starboard    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: meters    
    toStern:    
      description: Dimension to Stern    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: meters    
    type:    
      description: NGSI Entity type. It has to be MasterVessel    
      enum:    
        - MasterVessel    
      type: string    
      x-ngsi:    
        type: Property    
    vesselClass:    
      description: 'Code for vessel class. Enum:''BD=Dry bulk; BO=Oil tanker / bulk carrier; BS=Bulk carrier unloading; BY=Other types of bulk carriers; FC=Fishing vessel; FO=Vessel. transfer and/or transp.; GA=Vessel. RO-RO with passengers; GC=Mrcia general without specialization; GD=Rest general cargo vessels; GE=Buq. transp. combined; GN=Container ship; GO=Ro-ro vessel; GP=Passenger ship; GR=Refrigerator vessel; OO=Buq. or artefact. float be; OS=Supply ships; TC=Transport product. chemicals; TD=Other liquid bulk; TL=Transportation of liquefied gas; TO=Oil tanker; XD=Dredges; XR=Research and exploration; XT=Tugs / pushers; XX=Other ships and boats; UR=Fast Pass; G=General Cargo; T=Liquid Bulk Carriers (Tanks); S=Solid Bulk Carriers; OB=Other Merchant Vessels; UC=Cruise Ticket; OC=High Sea Fishing Vessels (Freezers);'''    
      enum:    
        - BD    
        - BO    
        - BS    
        - BY    
        - FC    
        - FO    
        - GA    
        - GC    
        - GD    
        - GE    
        - GN    
        - GO    
        - GP    
        - GR    
        - OO    
        - OS    
        - TC    
        - TD    
        - TL    
        - TO    
        - XD    
        - XR    
        - XT    
        - XX    
        - UR    
        - G    
        - T    
        - S    
        - OB    
        - UC    
        - OC    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vesselName:    
      description: 'Name of the Vessel. [EMSWe: DE-003-07] [EDIFACT:TDT-8212] [IMO:IMO0142]'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vesselOwner:    
      description: Owner of the Vessel    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vesselSubType:    
      description: 'Enum:''0=Not available (default),1-19=Reserved for future use,20=Wing in ground (WIG), all ships of this type,21=Wing in ground (WIG), Hazardous category A,22=Wing in ground (WIG), Hazardous category B,23=Wing in ground (WIG), Hazardous category C,24=Wing in ground (WIG), Hazardous category D,25-29=Wing in ground (WIG), Reserved for future use,30=Fishing,31=Towing,32=Towing: length exceeds 200m or breadth exceeds 25m,33=Dredging or underwater ops,34=Diving ops,35=Military ops,36=Sailing,37=Pleasure Craft,38-39=Reserved,40=High speed craft (HSC), all ships of this type,41=High speed craft (HSC), Hazardous category A,42=High speed craft (HSC), Hazardous category B,43=High speed craft (HSC), Hazardous category C,44=High speed craft (HSC), Hazardous category D,45-48=High speed craft (HSC), Reserved for future use,49=High speed craft (HSC), No additional information,50=Pilot Vessel,51=Search and Rescue vessel,52=Tug,53=Port Tender,54=Anti-pollution equipment,55=Law Enforcement,56-57=Spare - Local Vessel,58=Medical Transport,59=Noncombatant ship according to RR Resolution No. 18,60=Passenger, all ships of this type,61=Passenger, Hazardous category A,62=Passenger, Hazardous category B,63=Passenger, Hazardous category C,64=Passenger, Hazardous category D,65-68=Passenger, Reserved for future use,69=Passenger, No additional information,70=Cargo, all ships of this type,71=Cargo, Hazardous category A,72=Cargo, Hazardous category B,73=Cargo, Hazardous category C,74=Cargo, Hazardous category D,75-78=Cargo, Reserved for future use,79=Cargo, No additional information,80=Tanker, all ships of this type,81=Tanker, Hazardous category A,82=Tanker, Hazardous category B,83=Tanker, Hazardous category C,84=Tanker, Hazardous category D,85-88=Tanker, Reserved for future use,89=Tanker, No additional information,90=Other Type, all ships of this type,91=Other Type, Hazardous category A,92=Other Type, Hazardous category B,93=Other Type, Hazardous category C,94=Other Type, Hazardous category D,95-98=Other Type, Reserved for future use,99=Other Type, no additional information''. Code for vessel Sub-Type'    
      enum:    
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
        - 16    
        - 17    
        - 18    
        - 19    
        - 20    
        - 21    
        - 22    
        - 23    
        - 24    
        - 25    
        - 26    
        - 27    
        - 28    
        - 29    
        - 30    
        - 31    
        - 32    
        - 33    
        - 34    
        - 35    
        - 36    
        - 37    
        - 38    
        - 39    
        - 40    
        - 41    
        - 42    
        - 43    
        - 44    
        - 45    
        - 46    
        - 47    
        - 48    
        - 49    
        - 50    
        - 51    
        - 52    
        - 53    
        - 54    
        - 55    
        - 56    
        - 57    
        - 58    
        - 59    
        - 60    
        - 61    
        - 62    
        - 63    
        - 64    
        - 65    
        - 66    
        - 67    
        - 68    
        - 69    
        - 70    
        - 71    
        - 72    
        - 73    
        - 74    
        - 75    
        - 76    
        - 77    
        - 78    
        - 79    
        - 80    
        - 81    
        - 82    
        - 83    
        - 84    
        - 85    
        - 86    
        - 87    
        - 88    
        - 89    
        - 90    
        - 91    
        - 92    
        - 93    
        - 94    
        - 95    
        - 96    
        - 97    
        - 98    
        - 99    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    vesselType:    
      description: 'Enum:''1=Reserved,2=Wing In Ground,3=Special Category,4=High-Speed Craft,5=Special Category,6=Passenger,7=Cargo,8=Tanker,9=Other''. Code for vessel type'    
      enum:    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
        - 6    
        - 7    
        - 8    
        - 9    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2024 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/MasterVessel/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/MasterVessel/schema.json    
  x-model-tags: ESHUV    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### MasterVessel NGSI-v2 キー値の例  
JSON-LD形式のMasterVesselのkey-valuesの例です。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:mastervessel:id:1234",  
  "type": "MasterVessel",  
  "vesselName": "ELEANOR R.",  
  "imo": 9863637,  
  "mmsi": 210049000,  
  "callSign": "5BPC3",  
  "flagCode": "CY",  
  "vesselType": 1,  
  "vesselSubType": 2,  
  "vesselClass": "BO",  
  "gt": 12467,  
  "beam": 7,  
  "loa": 132.22,  
  "sleeve": 25.51,  
  "maxDraught": 5.61,  
  "dwt": 8.10,  
  "buildDate": "2023-06-01",  
  "toBow": 3,  
  "toStern": 20,  
  "toPort": 17,  
  "toStardboard": 4,  
  "photo": "https://acme.com/photos/9863637",  
  "owner": [  
    "urn:ngsi-ld:Acme-OWNER-NAME"  
  ],  
  "vesselOwner": "Acme OWNER NAME",  
  "manager": "Acme MANAGER NAME",  
  "financialOwner": "Acme FINANCIAL ",  
  "technicalManager": "Acme TECHNICAL MANAGER",  
  "dataProvider": "AIS",  
  "maxLoadVehicle": 120,  
  "maxPassenger": 0,  
  "maxVehicle": 16,  
  "minNumOfCrew": 12  
}  
```  
</details>  
#### MasterVessel NGSI-v2 正規化例  
以下は正規化されたJSON-LDフォーマットのMasterVesselの例です。これはNGSI-v2と互換性があり、オプションを使用しない場合、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:mastervessel:id:1234",  
  "type": "MasterVessel",  
  "vesselName": {  
    "type": "Text",  
    "value": "ELEANOR R."  
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
    "value": "CY"  
  },  
  "vesselType": {  
    "type": "Boolean",  
    "value": true  
  },  
  "vesselSubType": {  
    "type": "Number",  
    "value": 2  
  },  
  "vesselClass": {  
    "type": "Text",  
    "value": "BO"  
  },  
  "gt": {  
    "type": "Number",  
    "value": 12467  
  },  
  "beam": {  
    "type": "Number",  
    "value": 7  
  },  
  "loa": {  
    "type": "Number",  
    "value": 132.22  
  },  
  "sleeve": {  
    "type": "Number",  
    "value": 25.51  
  },  
  "maxDraught": {  
    "type": "Number",  
    "value": 5.61  
  },  
  "dwt": {  
    "type": "Number",  
    "value": 8.1  
  },  
  "buildDate": {  
    "type": "Date-Time",  
    "value": "2023-06-01"  
  },  
  "toBow": {  
    "type": "Number",  
    "value": 3  
  },  
  "toStern": {  
    "type": "Number",  
    "value": 20  
  },  
  "toPort": {  
    "type": "Number",  
    "value": 17  
  },  
  "toStardboard": {  
    "type": "Number",  
    "value": 4  
  },  
  "photo": {  
    "type": "Text",  
    "value": "https://acme.com/photos/9863637"  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:Acme-OWNER-NAME"  
    ]  
  },  
  "vesselOwner": {  
    "type": "Text",  
    "value": "Acme OWNER NAME"  
  },  
  "manager": {  
    "type": "Text",  
    "value": "Acme MANAGER NAME"  
  },  
  "financialOwner": {  
    "type": "Text",  
    "value": "Acme FINANCIAL "  
  },  
  "technicalManager": {  
    "type": "Text",  
    "value": "Acme TECHNICAL MANAGER"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "AIS"  
  },  
  "maxLoadVehicle": {  
    "type": "Number",  
    "value": 120  
  },  
  "maxPassenger": {  
    "type": "Boolean",  
    "value": false  
  },  
  "maxVehicle": {  
    "type": "Number",  
    "value": 16  
  },  
  "minNumOfCrew": {  
    "type": "Number",  
    "value": 12  
  }  
}  
```  
</details>  
#### MasterVessel NGSI-LD キー値の例  
JSON-LD形式のMasterVesselのkey-valuesの例です。これはNGSI-LDと互換性があり、`options=keyValues`を使用すると個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:mastervessel:id:1234",  
  "type": "MasterVessel",  
  "vesselName": "ELEANOR R.",  
  "imo": 9863637,  
  "mmsi": 210049000,  
  "callSign": "5BPC3",  
  "flagCode": "CY",  
  "vesselType": 1,  
  "vesselSubType": 2,  
  "vesselClass": "BO",  
  "gt": 12467,  
  "beam": 7,  
  "loa": 132.22,  
  "sleeve": 25.51,  
  "maxDraught": 5.61,  
  "dwt": 8.10,  
  "buildDate": "2023-06-01",  
  "toBow": 3,  
  "toStern": 20,  
  "toPort": 17,  
  "toStardboard": 4,  
  "photo": "https://acme.com/photos/9863637",  
  "owner": [  
    "urn:ngsi-ld:Acme-OWNER-NAME"  
  ],  
  "vesselOwner": "Acme OWNER NAME",  
  "manager": "Acme MANAGER NAME",  
  "financialOwner": "Acme FINANCIAL ",  
  "technicalManager": "Acme TECHNICAL MANAGER",  
  "dataProvider": "AIS",  
  "maxLoadVehicle": 120,  
  "maxPassenger": 0,  
  "maxVehicle": 16,  
  "minNumOfCrew": 12,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/refs/heads/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### マスターベッセル NGSI-LD 正規化例  
正規化されたJSON-LDフォーマットのMasterVesselの例です。これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:mastervessel:id:1234",  
  "type": "MasterVessel",  
  "vesselName": {  
    "type": "Property",  
    "value": "ELEANOR R."  
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
    "value": "CY"  
  },  
  "vesselType": {  
    "type": "Property",  
    "value": true  
  },  
  "vesselSubType": {  
    "type": "Property",  
    "value": 2  
  },  
  "vesselClass": {  
    "type": "Property",  
    "value": "BO"  
  },  
  "gt": {  
    "type": "Property",  
    "value": 12467  
  },  
  "beam": {  
    "type": "Property",  
    "value": 7  
  },  
  "loa": {  
    "type": "Property",  
    "value": 132.22  
  },  
  "sleeve": {  
    "type": "Property",  
    "value": 25.51  
  },  
  "maxDraught": {  
    "type": "Property",  
    "value": 5.61  
  },  
  "dwt": {  
    "type": "Property",  
    "value": 8.1  
  },  
  "buildDate": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "value": "2023-06-01"  
    }  
  },  
  "toBow": {  
    "type": "Property",  
    "value": 3  
  },  
  "toStern": {  
    "type": "Property",  
    "value": 20  
  },  
  "toPort": {  
    "type": "Property",  
    "value": 17  
  },  
  "toStardboard": {  
    "type": "Property",  
    "value": 4  
  },  
  "photo": {  
    "type": "Property",  
    "value": "https://acme.com/photos/9863637"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Acme-OWNER-NAME"  
    ]  
  },  
  "vesselOwner": {  
    "type": "Property",  
    "value": "Acme OWNER NAME"  
  },  
  "manager": {  
    "type": "Property",  
    "value": "Acme MANAGER NAME"  
  },  
  "financialOwner": {  
    "type": "Property",  
    "value": "Acme FINANCIAL "  
  },  
  "technicalManager": {  
    "type": "Property",  
    "value": "Acme TECHNICAL MANAGER"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "AIS"  
  },  
  "maxLoadVehicle": {  
    "type": "Property",  
    "value": 120  
  },  
  "maxPassenger": {  
    "type": "Property",  
    "value": false  
  },  
  "maxVehicle": {  
    "type": "Property",  
    "value": 16  
  },  
  "minNumOfCrew": {  
    "type": "Property",  
    "value": 12  
  }  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
各フィールドの規格識別に合意することが保留されている。SO3166-1-国コードとその下位区分のコードに関する国際標準。- RFC 2141 - URN Syntax (https://www.ietf.org/rfc/rfc2141.txt) - RFC 8141 - Uniform Resource Names (URN) (https://tools.ietf.org/html/rfc8141) - IALAs MRN Request (https://www.iana.org/assignments/urn-formal/mrn)  
<MRN> ::= "urn" ":" "mrn" ":" <OID> ":" <OSNID> ":" <OSNS> <OID> ::= (alphanum) 0*32(alphanum / "-") (alphanum) ;組織ID (すなわち.<OSNID> ::= (alphanum) 0*32(alphanum / "-") (alphanum) ;組織固有の名前空間ID (ポートコールなど) <OSNS> ::= pchar *(pchar / "/") ;組織固有の名前空間文字列 (モジュール名やマイクロサービス名など).<ID> ::= その名前空間上の一意な識別子 (すなわち、エンティティ名の後にSQLデータベースの行IDが続く)  
例："urn:mrn:eshuv:portcalls:portcall:id:343"  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
