<!-- 10-Header -->  
 
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
 
エンティティ: NavigationSector  
======================== 
<!-- /10-Header -->  
 
<!-- 15-License -->  
 
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/NavigationSector/LICENSE.md)  
 
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
 
<!-- 20-Description -->  
 
グローバル説明: **このデータモデルは、港内のナビゲーションセクターを、地理的境界と運用の詳細を含めて記述する**  
 
バージョン: 0.0.1  
<!-- /20-Description -->  
 
<!-- 30-PropertiesList -->  
 

## プロパティのリスト  
 
<sup><sub>[*] 属性に型がない場合は、複数の型または異なる形式/パターンをとる可能性がある</sub></sup>  
- `address[object]`: 郵送先住所。モデル: [https://schema.org/address](https://schema.org/address)  
	- `addressCountry[string]`: 国。例: スペイン。モデル: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 街道住所が存在し、地域内にある自治体。モデル: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 自治体が存在し、国内にある地域。モデル: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 一部の国では、地方自治体によって管理される行政区分の一種  
	- `postOfficeBoxNumber[string]`: 郵便ポストボックス番号。例: 03578。モデル: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 郵便番号。例: 24004。モデル: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道住所。モデル: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 公共の通り上的特定の物件を識別する番号  
- `alternateName[string]`: このアイテムの別名  
- `areaServed[string]`: サービスまたは提供アイテムが提供される地理的なエリア。モデル: [https://schema.org/Text](https://schema.org/Text)  
- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する文字シーケンス  
- `dateCreated[date-time]`: エンティティの作成タイムスタンプ。この場合は通常、ストレージプラットフォームによって割り当てられる  
- `dateModified[date-time]`: エンティティの最後の変更のタイムスタンプ。この場合は通常、ストレージプラットフォームによって割り当てられる  
- `description[string]`: このアイテムの説明  
- `id[*]`: エンティティの一意の識別子  
- `location[*]`: アイテムへのGeojson参照。ポイント、ラインストリング、ポリゴン、マルチポイント、マルチラインストリング、マルチポリゴンのいずれかになる  
- `minProbe[number]`: セクター内の水の最小深度（メートル）  
- `minProbeDate[date-time]`: 最小深度が最後に記録された日付  
- `modifiedDate[date-time]`: ナビゲーションセクターのエンティティの最後の変更の日時  
- `mrn[string]`: MRNコード識別子。これは、エンティティの意味とエンティティの起源を知ることができるように、さまざまな組織によって共通の方法で識別される必要があります。エンティティを作成したシステムによって割り当てられた、PortCallエンティティの一意の識別子でなければなりません。このURNは、MRNとIETF、特にRFC 2141、RFC 5234、およびRFC 8141に準拠している必要があります。  
    提案された形式は  
    id::='urn:mrn:eshuv:<ONSS>:portcalls:navigationsector:id:[0-9]+' または  
    ここで、OID:= 組織のUN / LOCODE、OONSS:= サービスの組織名、2099は、ポートコールが開始された年、9999999は、ボラードエンティティの発行者がシステムで識別する、一意の増加識別子（例: SQL行ID）  
    例: urn:mrn:eshuv:portcalls:navigationsector:id:16  
    国際標準では、[Ship's Visit] としても知られている[Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)  
- `name[string]`: このアイテムの名前  
- `navigationArea[string]`: このセクターが位置するより広いナビゲーションエリア  
- `navigationSector[string]`: 港内でのナビゲーションセクターの識別子  
- `owner[array]`: 所有者の一意のIDを参照するJSONエンコード文字シーケンスを含むリスト  
- `portCode[string]`: このナビゲーションセクターが位置する港のコード  
- `rank[number]`: ナビゲーションセクターのランクまたは優先度レベル  
- `remarks[string]`: ナビゲーションセクターに関する追加の備考またはノート  
- `sectorType[string]`: ナビゲーションセクターの種類  
- `seeAlso[*]`: アイテムに関する追加のリソースを指すURIのリスト  
- `source[string]`: エンティティデータの元のソースをURLとして示す文字シーケンス。ソースプロバイダーの完全修飾ドメイン名、またはソースオブジェクトへのURLであることをお勧めします。  
- `type[string]`: NGSIエンティティタイプ。これは、NavigationSectorでなければなりません  
<!-- /30-PropertiesList -->  
 
<!-- 35-RequiredProperties -->  
 
必要なプロパティ  
- `id`  
- `type`  
<!-- /35-RequiredProperties -->  
 
<!-- 40-NotesYaml -->  
 
<!-- /40-NotesYaml -->  
 
<!-- 50-DataModelHeader -->  
 
## プロパティのデータモデル説明  
 
アルファベット順（詳細をクリック）  
<!-- /50-DataModelHeader -->  
 
<!-- 60-ModelYaml -->  
 
<details><summary><strong>フルヤムルの詳細</strong></summary>    
 
```yaml  
NavigationSector:    
  description: This data model describes a navigation sector in a port, including geographic boundaries and operational details    
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
    location:    
      description: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              description: BBox of the  Point    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Point    
              items:    
                type: number    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the LineString    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the Polygon    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Polygon    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MulitPoint    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MultiLineString    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: Coordinates of the MultiPolygon    
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
              x-ngsi:    
                type: Property    
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
    minProbe:    
      description: Minimum depth of water in meters within the sector    
      type: number    
      x-ngsi:    
        type: Property    
    minProbeDate:    
      description: Date when the minimum depth was last recorded    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    modifiedDate:    
      description: Date and time of last modification of the navigation sector entity    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    mrn:    
      description: "MRN coded identifier. It has to be related to the entity in a way that is well-known by different organisms the meaning and the initiator of the entity, and all next parties will maintain on its origianl value. This identifier must be an UNIQUE identifier of the PortCall entity assigned by the system who created on first the entity. This URN should Conforms MRN & IETF specifically RFC 2141, RFC 5234, and RFC 8141. \n    The propossed format is \n    id::='urn:mrn:eshuv:<ONSS>:portcalls:navigationsector:id:[0-9]+' or  \n    where OID:= Organisation UN/LOCODE, OONSS:=Organization Name of Service, 2099 the year on which the portcall was initiated, 9999999 an increasing, unique identifier that the issuer of the Bollard entity will identify on his sistems (i.e. a SQL row-id), \n    i.e. urn:mrn:eshuv:portcalls:navigationsector:id:16 \n     See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)In international standards is also known as [Ship's Visit]"    
      enum:    
        - PortCall    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    navigationArea:    
      description: The broader navigation area where this sector is situated    
      type: string    
      x-ngsi:    
        type: Property    
    navigationSector:    
      description: Identifier for the navigation sector within the port    
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
    portCode:    
      description: Code of the port where this navigation sector is located    
      type: string    
      x-ngsi:    
        type: Property    
    rank:    
      description: Rank or priority level of the navigation sector    
      type: number    
      x-ngsi:    
        type: Property    
    remarks:    
      description: Additional remarks or notes about the navigation sector    
      type: string    
      x-ngsi:    
        type: Property    
    sectorType:    
      description: Type of navigation sector    
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
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be NavigationSector    
      enum:    
        - NavigationSector    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/NavigationSector/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/NavigationSector/schema.json    
  x-model-tags: ESHUV    
  x-version: 0.0.1    
```  
</details>    
 
<!-- /60-ModelYaml -->  
 
<!-- 70-MiddleNotes -->  
 
<!-- /70-MiddleNotes -->  
 
<!-- 80-Examples -->  
 
## ペイロードの例    
 
#### NavigationSector NGSI-v2 キー値の例    
 
ここでは、キー値としてJSON形式のNavigationSectorの例を示します。これは、`options=keyValues` を使用してコンテキストデータを個々のエンティティとして返す場合に、NGSI-v2 と互換性があります。  
<details><summary><strong>例の表示/非表示</strong></summary>    
 
```json  
{  
  "id": "urn:mrn:eshuv:facilities:navigationsector:id:10",  
  "type": "NavigationSector",  
  "portCode": "ESVLC",  
  "navigationSector": "S95",  
  "navigationArea": "AEXT",  
  "rank": 1,  
  "sectorType": "AEXT",  
  "minProbe": 99.0,  
  "minProbeDate": "2022-01-01T00:00:00",  
  "remarks": "Monoboya de crudo",  
  "location": {  
    "type": "Polygon",  
    "coordinates": [  
      [  
        [  
          -3.703790,  
          40.416775  
        ],  
        [  
          -3.703790,  
          40.426775  
        ],  
        [  
          -3.693790,  
          40.426775  
        ],  
        [  
          -3.693790,  
          40.416775  
        ]  
      ]  
    ]  
  }  
}  
```  
</details>  
 
#### NavigationSector NGSI-v2 正規化された例    
 
ここでは、正規化されたJSON形式のNavigationSectorの例を示します。これは、オプションを使用しない場合に、NGSI-v2 と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>例の表示/非表示</strong></summary>    
 
```json  
{  
  "id": "urn:mrn:eshuv:facilities:navigationsector:id:10",  
  "type": "NavigationSector",  
  "portCode": {  
    "type": "Text",  
    "value": "ESVLC"  
  },  
  "navigationSector": {  
    "type": "Text",  
    "value": "S95"  
  },  
  "navigationArea": {  
    "type": "Text",  
    "value": "AEXT"  
  },  
  "rank": {  
    "type": "Number",  
    "value": 1  
  },  
  "sectorType": {  
    "type": "Text",  
    "value": "AEXT"  
  },  
  "minProbe": {  
    "type": "Number",  
    "value": 99.0  
  },  
  "minProbeDate": {  
    "type": "DateTime",  
    "value": "2022-01-01T00:00:00"  
  },  
  "remarks": {  
    "type": "Text",  
    "value": "Monoboya de crudo"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [  
        [  
          [  
            -3.70379,  
            40.416775  
          ],  
          [  
            -3.70379,  
            40.426775  
          ],  
          [  
            -3.69379,  
            40.426775  
          ],  
          [  
            -3.69379,  
            40.416775  
          ]  
        ]  
      ]  
    }  
  }  
}  
```  
</details>  
 
#### NavigationSector NGSI-LD キー値の例    
 
ここでは、キー値としてJSON-LD形式のNavigationSectorの例を示します。これは、`options=keyValues` を使用してコンテキストデータを個々のエンティティとして返す場合に、NGSI-LD と互換性があります。  
<details><summary><strong>例の表示/非表示</strong></summary>    
 
```json  
{  
  "id": "urn:ngsi-ld:NavigationSector:urn:mrn:eshuv:facilities:navigationsector:id:10",  
  "type": "NavigationSector",  
  "portCode": "ESVLC",  
  "navigationSector": "S95",  
  "navigationArea": "AEXT",  
  "rank": 1,  
  "sectorType": "AEXT",  
  "minProbe": 99.0,  
  "minProbeDate": "2022-01-01T00:00:00",  
  "remarks": "Monoboya de crudo",  
  "location": {  
    "type": "Polygon",  
    "coordinates": [  
      [  
        [  
          -3.703790,  
          40.416775  
        ],  
        [  
          -3.703790,  
          40.426775  
        ],  
        [  
          -3.693790,  
          40.426775  
        ],  
        [  
          -3.693790,  
          40.416775  
        ]  
      ]  
    ]  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```  
</details>  
 
#### NavigationSector NGSI-LD 正規化された例    
 
ここでは、正規化されたJSON-LD形式のNavigationSectorの例を示します。これは、オプションを使用しない場合に、NGSI-LD と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>例の表示/非表示</strong></summary>    
 
```json  
{  
  "id": "urn:ngsi-ld:NavigationSector:urn:mrn:eshuv:facilities:navigationsector:id:10",  
  "type": "NavigationSector",  
  "portCode": {  
    "type": "Property",  
    "value": "ESVLC"  
  },  
  "navigationSector": {  
    "type": "Property",  
    "value": "S95"  
  },  
  "navigationArea": {  
    "type": "Property",  
    "value": "AEXT"  
  },  
  "rank": {  
    "type": "Property",  
    "value": 1  
  },  
  "sectorType": {  
    "type": "Property",  
    "value": "AEXT"  
  },  
  "minProbe": {  
    "type": "Property",  
    "value": 99.0  
  },  
  "minProbeDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-01-01T00:00:00"  
    }  
  },  
  "remarks": {  
    "type": "Property",  
    "value": "Monoboya de crudo"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [  
        [  
          [  
            -3.70379,  
            40.416775  
          ],  
          [  
            -3.70379,  
            40.426775  
          ],  
          [  
            -3.69379,  
            40.426775  
          ],  
          [  
            -3.69379,  
            40.416775  
          ]  
        ]  
      ]  
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
 
[FAQ 10](https://smartdatamodels.org/index.php/faqs/) を参照して、量の単位を扱う方法についての回答を得る  
<!-- /95-Units -->  
 
<!-- 97-LastFooter -->  
 
---  
 
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
 