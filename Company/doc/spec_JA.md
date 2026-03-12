<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: 会社  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/Company/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバル説明: **このデータモデルは、港にある会社を記述する**  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティの一覧  

<sup><sub>[*] 属性に型がなければ、複数の型または異なる形式/パターンをとることができるためです</sub></sup>  
- `active[boolean]`: 会社またはエンティティのアクティブ化の状態  
- `address[object]`: 郵送先住所。モデル: [https://schema.org/address](https://schema.org/address)  
	- `addressCountry[string]`: 国。例: スペイン。モデル: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 街道の住所が存在する、地域。モデル: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 地域が存在する、国。モデル: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 一部の国では、地方自治体によって管理される行政区分の一種  
	- `postOfficeBoxNumber[string]`: 郵便ポストボックス番号。例: 03578。モデル: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 郵便番号。例: 24004。モデル: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道の住所。モデル: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 公共の通りで特定の物件を識別する番号  
- `admissionDate[date-string]`: 会社がモデルに登録された日付  
- `alias[string]`: 非公式の会社名またはエンティティ名  
- `alternateName[string]`: このアイテムの別名  
- `areaServed[string]`: サービスまたは提供アイテムが提供される地理的なエリア。モデル: [https://schema.org/Text](https://schema.org/Text)  
- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する文字列のシーケンス  
- `dateCreated[date-time]`: エンティティの作成タイムスタンプ。このタイムスタンプは通常、ストレージプラットフォームによって割り当てられます  
- `dateModified[date-time]`: エンティティの最後の変更のタイムスタンプ。このタイムスタンプは通常、ストレージプラットフォームによって割り当てられます  
- `description[string]`: このアイテムの説明  
- `email[idn-email]`: 所有者のメールアドレス  
- `entityType[string]`: 会社またはエンティティの種類  
- `id[*]`: エンティティの一意の識別子  
- `legalCode[string]`: 会社またはエンティティのコード  
- `licenses[array]`: 会社の運用ライセンス。通常、コードと説明のペア  
- `location[*]`: アイテムへのGeojsonリファレンス。Point、LineString、Polygon、MultiPoint、MultiLineString、またはMultiPolygonのいずれかになります  
- `mrn[string]`: MRNコード識別子。このURNは、MRNおよびIETFのRFC 2141、RFC 5234、RFC 8141に準拠する必要があります。提案された形式は、id::='urn:mrn:<PORT>:<ONSS>:community:company:id:[0-9]+'またはPORT := UN/LOCODEの港、OID:= 組織UN/LOCODE、OONSS:= 組織サービス名、9999999は、会社レジストリエンティティの作成者がシステムで識別する一意の識別子（例: SQL行ID）である。例: urn:mrn:eshuv:community:company:id:1296  
- `name[string]`: このアイテムの名前  
- `owner[array]`: 所有者（s）の一意のIDを参照するJSONエンコード文字列のシーケンスを含むリスト  
- `registeredName[string]`: 会社またはエンティティの公式名  
- `seeAlso[*]`: アイテムに関する追加のリソースを指すURIのリスト  
- `source[string]`: エンティティデータの元のソースをURLとして提供する文字列のシーケンス。ソースプロバイダーの完全修飾ドメイン名、またはソースオブジェクトのURLを推奨します  
- `telephone[string]`: この連絡先の電話番号  
- `type[*]`: NGSIエンティティタイプ。会社でなければなりません  
<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## データモデルのプロパティの説明  
アルファベット順に並べた（詳細をクリック）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>完全なYAMLの詳細</strong></summary>    
```yaml  
Company:    
  description: This data model describes a company in a port    
  properties:    
    active:    
      description: Status of activation of the company or entity with activities or responsibility in the port    
      type: boolean    
      x-ngsi:    
        type: Property    
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
    admissionDate:    
      description: Date in which the company was registered in the model    
      format: date-string    
      type: string    
      x-ngsi:    
        type: Property    
    alias:    
      description: Non official Name (nickname) of the company or entity with activities or responsibility in the port    
      type: string    
      x-ngsi:    
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
    email:    
      description: Email address of owner    
      format: idn-email    
      type: string    
      x-ngsi:    
        type: Property    
    entityType:    
      description: Type of the company or entity with activities or responsibility in the port    
      enum:    
        - Agent    
        - Carrier    
        - Consignee    
        - LogisticsOperator    
        - PortAuthority    
        - PortReceptionFacilityOperator    
        - PublicBody    
        - ServiceProvider    
        - Steevedore    
        - TerminalOperator    
        - TransportCompany    
        - WasteManagementCompany    
        - Other    
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
    legalCode:    
      description: Code of the company or entity with activities or responsibility in the port    
      type: string    
      x-ngsi:    
        type: Property    
    licenses:    
      description: Licenses of operation of the Company. Usually in pairs, code and description    
      items:    
        description: Description of an item of the licenses. Usually a pair code and description    
        items:    
          description: Every item in the usual pairs. Can be either the code or the description    
          type: string    
          x-ngsi:    
            type: Property    
        type: array    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
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
    mrn:    
      description: MRN coded identifier. This URN should Conforms MRN & IETF specifically RFC 2141, RFC 5234, and RFC 8141. The proposed format is  id::='urn:mrn:<PORT>:<ONSS>:community:company:id:[0-9]+' or where PORT := UN/LOCODE of port, OID:= Organisation UN/LOCODE, OONSS:=Organization Name of Service, 9999999 an unique identifier that the creator of the company registry entity will identify on his systems (i.e. a SQL row-id), i.e. urn:mrn:eshuv:community:company:id:1296    
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
          type: Relationship    
      type: array    
      x-ngsi:    
        type: Property    
    registeredName:    
      description: official Name of the company or entity with activities or responsibility in the port    
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
    telephone:    
      description: Telephone of this contact    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be Company    
      enum:    
        - Company    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/Company/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/company/schema.json    
  x-model-tags: ESHUV    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例    
#### Company NGSI-v2 キー値の例    
ここは、キー値としてJSON形式の会社の例です。これは、`options=keyValues` を使用してコンテキストデータを個々のエンティティとして返すときに、NGSI-v2 と互換性があります。  
<details><summary><strong>例の表示/非表示</strong></summary>    
```json  
{  
  "type": "Company",  
  "dataProvider": "PCS/other",  
  "id": "urn:mrn:eshuv:pcs:company:cif:B90244585",  
  "legalCode": "B90244585",  
  "registeredName": "BERGE Maritima SL",  
  "alias": "BERGE",  
  "entityType": "Consignee",  
  "address": {  
    "streetAddress": "Avda Sociedad colombina Onubense",  
    "addressLocality": "Huelva",  
    "addressRegion": "Andalucía",  
    "addressCountry": "ES",  
    "postalCode": "21300",  
    "streetNr": "S/N"  
  },  
  "email": "berge@puertohuelva.es",  
  "telephone": "900252526",  
  "active": true,  
  "admissionDate": "2024-12-01T00:00:00",  
  "licenses": [  
    [  
      "Suministro de combustible a buques mediante camión",  
      "SC-013"  
    ],  
    [  
      "SCM-003",  
      "Suministro de combustible a maquinaria mediante camión"  
    ],  
    [  
      "MAR-23",  
      "MarpolAnnex1"  
    ]  
  ]  
}  
```  
</details>  
#### Company NGSI-v2 正規化された例    
ここは、正規化されたJSON形式の会社の例です。これは、オプションを使用しないときに、コンテキストデータを個々のエンティティとして返すときに、NGSI-v2 と互換性があります。  
<details><summary><strong>例の表示/非表示</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:pcs:company:cif:B90244585",  
  "type": "Company",  
  "dataProvider": {  
    "type": "Text",  
    "value": "PCS/other"  
  },  
  "legalCode": {  
    "type": "Text",  
    "value": "B90244585"  
  },  
  "registeredName": {  
    "type": "Text",  
    "value": "BERGE Maritima SL"  
  },  
  "alias": {  
    "type": "Text",  
    "value": "BERGE"  
  },  
  "entityType": {  
    "type": "Text",  
    "value": "Consignee"  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "streetAddress": "Avda Sociedad colombina Onubense",  
      "addressLocality": "Huelva",  
      "addressRegion": "Andalucía",  
      "addressCountry": "ES",  
      "postalCode": "21300",  
      "streetNr": "S/N"  
    }  
  },  
  "email": {  
    "type": "Text",  
    "value": "berge@puertohuelva.es"  
  },  
  "telephone": {  
    "type": "Text",  
    "value": "900252526"  
  },  
  "active": {  
    "type": "Boolean",  
    "value": true  
  },  
  "admissionDate": {  
    "type": "DateTime",  
    "value": "2024-12-01T00:00:00"  
  },  
  "licenses": {  
    "type": "Array",  
    "value": [  
      [  
        "Suministro de combustible a buques mediante camión",  
        "SC-013"  
      ],  
      [  
        "SCM-003",  
        "Suministro de combustible a maquinaria mediante camión"  
      ],  
      [  
        "MAR-23",  
        "MarpolAnnex1"  
      ]  
    ]  
  }  
}  
```  
</details>  
#### Company NGSI-LD キー値の例    
ここは、キー値としてJSON-LD形式の会社の例です。これは、`options=keyValues` を使用してコンテキストデータを個々のエンティティとして返すときに、NGSI-LD と互換性があります。  
<details><summary><strong>例の表示/非表示</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Company:urn:mrn:eshuv:pcs:company:cif:B90244585",  
  "type": "Company",  
  "dataProvider": "PCS/other",  
  "legalCode": "B90244585",  
  "registeredName": "BERGE Maritima SL",  
  "alias": "BERGE",  
  "entityType": "Consignee",  
  "address": {  
    "streetAddress": "Avda Sociedad colombina Onubense",  
    "addressLocality": "Huelva",  
    "addressRegion": "Andalucía",  
    "addressCountry": "ES",  
    "postalCode": "21300",  
    "streetNr": "S/N"  
  },  
  "email": "berge@puertohuelva.es",  
  "telephone": "900252526",  
  "active": true,  
  "admissionDate": "2024-12-01T00:00:00",  
  "licenses": [  
    [  
      "Suministro de combustible a buques mediante camión",  
      "SC-013"  
    ],  
    [  
      "SCM-003",  
      "Suministro de combustible a maquinaria mediante camión"  
    ],  
    [  
      "MAR-23",  
      "MarpolAnnex1"  
    ]  
  ],  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Company NGSI-LD 正規化された例    
ここは、正規化されたJSON-LD形式の会社の例です。これは、オプションを使用しないときに、コンテキストデータを個々のエンティティとして返すときに、NGSI-LD と互換性があります。  
<details><summary><strong>例の表示/非表示</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Company:urn:mrn:eshuv:pcs:company:cif:B90244585",  
  "type": "Company",  
  "dataProvider": {  
    "type": "Property",  
    "value": "PCS/other"  
  },  
  "legalCode": {  
    "type": "Property",  
    "value": "B90244585"  
  },  
  "registeredName": {  
    "type": "Property",  
    "value": "BERGE Maritima SL"  
  },  
  "alias": {  
    "type": "Property",  
    "value": "BERGE"  
  },  
  "entityType": {  
    "type": "Property",  
    "value": "Consignee"  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Avda Sociedad colombina Onubense",  
      "addressLocality": "Huelva",  
      "addressRegion": "Andalucía",  
      "addressCountry": "ES",  
      "postalCode": "21300",  
      "streetNr": "S/N"  
    }  
  },  
  "email": {  
    "type": "Property",  
    "value": "berge@puertohuelva.es"  
  },  
  "telephone": {  
    "type": "Property",  
    "value": "900252526"  
  },  
  "active": {  
    "type": "Property",  
    "value": true  
  },  
  "admissionDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-12-01T00:00:00"  
    }  
  },  
  "licenses": {  
    "type": "Property",  
    "value": [  
      [  
        "Suministro de combustible a buques mediante camión",  
        "SC-013"  
      ],  
      [  
        "SCM-003",  
        "Suministro de combustible a maquinaria mediante camión"  
      ],  
      [  
        "MAR-23",  
        "MarpolAnnex1"  
      ]  
    ]  
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/) を参照して、測定単位を扱う方法についての回答を得てください  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
