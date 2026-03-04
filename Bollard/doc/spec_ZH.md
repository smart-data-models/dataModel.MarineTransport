<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：防撞柱  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/Bollard/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**此数据模型描述了港口设施中的防撞柱，用于系泊船只。**  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，则可能有多种类型或不同的格式/模式</sub></sup>  
- `address[object]`：邮寄地址。模型：[https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`：国家。例如，西班牙。模型：[https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`：街道地址所在的地区，并且在该地区。模型：[https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`：地区所在的地区，并且在国家。模型：[https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`：区是一个类型的行政区划，在一些国家，由地方政府管理    
	- `postOfficeBoxNumber[string]`：邮政信箱地址的邮政信箱编号。例如，03578。模型：[https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`：邮政编码。例如，24004。模型：[https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`：街道地址。模型：[https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`：标识特定属性的公用街道编号    
- `alternateName[string]`：此项的替代名称  - `areaServed[string]`：服务或提供的项目所提供的的地理区域。模型：[https://schema.org/Text](https://schema.org/Text)- `bollardIndex[number]`：设施内防撞柱的索引号。  - `code[string]`：标识防撞柱的代码。  - `dataProvider[string]`：一系列字符，标识和谐数据实体的提供者  - `dateCreated[date-time]`：实体创建时间戳。这通常由存储平台分配  - `dateModified[date-time]`：实体最后修改的时间戳。这通常由存储平台分配  - `description[string]`：此项的描述  - `distanceFromPrevious[number]`：从前一个防撞柱到此防撞柱的距离（以米为单位）。  - `distanceFromStart[number]`：从设施开始到此防撞柱的距离（以米为单位）。  - `facilityRef[string]`：指向此防撞柱所属的设施实体的引用。  - `id[*]`：实体的唯一标识符  - `latitude[number]`：防撞柱位置的纬度坐标。  - `location[*]`：Geojson 引用此项。它可以是 Point、LineString、Polygon、MultiPoint、MultiLineString 或 MultiPolygon  - `longitude[number]`：防撞柱位置的经度坐标。  - `modifiedDate[date-time]`：防撞柱实体的最后修改日期和时间。  - `mrn[string]`：MRN 编码标识符。它必须以一种众所周知的方式与实体相关联，并且所有后续方都将保持其原始值。该标识符必须是系统创建的实体的唯一标识符，必须符合 MRN 和 IETF 的特定要求（RFC 2141、RFC 5234 和 RFC 8141）。建议的格式是     id::='urn:mrn:eshuv:<ONSS>:portcalls:bollard:code:[0-9]+' 或 OID:= 组织 UN/LOCODE，OONSS:= 服务组织名称，2099 是港口呼叫开始的年份，9999999 是发行者分配的唯一标识符（例如 SQL 行 ID），例如 urn:mrn:eshuv:portcalls:bollard:id:296 参见 [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) 在国际标准中也称为 [船舶访问]  - `name[string]`：此项的名称  - `outOfOrder[boolean]`：指示防撞柱当前是否损坏。  - `owner[array]`：包含 JSON 编码序列的列表，引用所有者（s）的唯一 ID  - `portCode[string]`：防撞柱所在港口的代码。  - `probe[number]`：防撞柱位置的水深（以米为单位）。  - `seeAlso[*]`：指向此项的其他资源的 URI 列表  - `source[string]`：实体数据的原始来源的字符序列，作为 URL。建议使用完全限定域名或源对象的 URL  - `type[string]`：NGSI 实体类型。必须是 Bollard  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必需属性  
- `bollardIndex`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 数据模型属性描述  
按字母顺序排序（单击查看详细信息）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>完整的 yaml 详细信息</strong></summary>    
```yaml  
Bollard:    
  description: This data model describes a bollard in a port facility, used for mooring vessels.    
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
    bollardIndex:    
      description: Index number of the bollard within the facility.    
      type: number    
      x-ngsi:    
        type: Property    
    code:    
      description: Code identifying the bollard.    
      type: string    
      x-ngsi:    
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
    distanceFromPrevious:    
      description: Distance in meters from the previous bollard.    
      type: number    
      x-ngsi:    
        type: Property    
    distanceFromStart:    
      description: Distance in meters from the start of the facility.    
      type: number    
      x-ngsi:    
        type: Property    
    facilityRef:    
      description: Reference to the facility entity this bollard belongs to.    
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
    latitude:    
      description: Latitude coordinate of the bollard location.    
      type: number    
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
    longitude:    
      description: Longitude coordinate of the bollard location.    
      type: number    
      x-ngsi:    
        type: Property    
    modifiedDate:    
      description: Date and time of last modification of the bollard entity.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    mrn:    
      description: MRN coded identifier. It has to be related to the entity in a way that is well-known by different organisms the meaning and the initiator of the entity, and all next parties will maintain on its original value. This identifier must be an UNIQUE identifier of the PortCall entity assigned by the system who created on first the entity. This URN should Conforms MRN & IETF specifically RFC 2141, RFC 5234, and RFC 8141. The propossed format is     id::='urn:mrn:eshuv:<ONSS>:portcalls:bollard:code:[0-9]+' or where OID:= Organisation UN/LOCODE, OONSS:=Organization Name of Service, 2099 the year on which the portcall was initiated, 9999999 an increasing, unique identifier that the issuer of the Bollard entity will identify on his sistems (i.e. a SQL row-id), i.e. urn:mrn:eshuv:portcalls:bollard:id:296 See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)In international standards is also known as [Ship's Visit]    
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
    outOfOrder:    
      description: Indicates if the bollard is currently out of order.    
      type: boolean    
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
      description: Code of the port where this bollard is located.    
      type: string    
      x-ngsi:    
        type: Property    
    probe:    
      description: Water depth at the bollard location in meters.    
      type: number    
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
      description: NGSI Entity type. It has to be Bollard    
      enum:    
        - Bollard    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - bollardIndex    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/Bollard/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/Bollard/schema.json    
  x-model-tags: ESHUV    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 示例有效载荷    
#### Bollard NGSI-v2 键值示例    
这是 Bollard 以 JSON 格式表示的键值示例。它与 NGSI-v2 兼容，当使用 `options=keyValues` 时，返回单个实体的上下文数据。  
<details><summary><strong>显示/隐藏示例</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:facilities:bollard:id:20",  
  "type": "Bollard",  
  "portCode": "ESVLC",  
  "facilityRef": "urn:mrn:eshuv:facilities:facility:code:20",  
  "code": "1",  
  "bollardIndex": 4,  
  "probe": 12.5,  
  "distanceFromPrevious": 15.0,  
  "distanceFromStart": 132.2,  
  "latitude": 37.2614,  
  "longitude":  -6.9447,  
  "outOfOrder": false  
}  
```  
</details>  
#### Bollard NGSI-v2 规范化示例    
这是 Bollard 以 JSON 格式表示的规范化示例。它与 NGSI-v2 兼容，当不使用选项时，返回单个实体的上下文数据。  
<details><summary><strong>显示/隐藏示例</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:facilities:bollard:id:20",  
  "type": "Bollard",  
  "portCode": {  
    "type": "Text",  
    "value": "ESVLC"  
  },  
  "facilityRef": {  
    "type": "Text",  
    "value": "urn:mrn:eshuv:facilities:facility:code:20"  
  },  
  "code": {  
    "type": "Text",  
    "value": "1"  
  },  
  "bollardIndex": {  
    "type": "Number",  
    "value": 4  
  },  
  "probe": {  
    "type": "Number",  
    "value": 12.5  
  },  
  "distanceFromPrevious": {  
    "type": "Number",  
    "value": 15.0  
  },  
  "distanceFromStart": {  
    "type": "Number",  
    "value": 132.2  
  },  
  "latitude": {  
    "type": "Number",  
    "value": 37.2614  
  },  
  "longitude": {  
    "type": "Number",  
    "value": -6.9447  
  },  
  "outOfOrder": {  
    "type": "Boolean",  
    "value": false  
  }  
}  
```  
</details>  
#### Bollard NGSI-LD 键值示例    
这是 Bollard 以 JSON-LD 格式表示的键值示例。它与 NGSI-LD 兼容，当使用 `options=keyValues` 时，返回单个实体的上下文数据。  
<details><summary><strong>显示/隐藏示例</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Bollard:urn:mrn:eshuv:facilities:bollard:id:20",  
  "type": "Bollard",  
  "portCode": "ESVLC",  
  "facilityRef": "urn:mrn:eshuv:facilities:facility:code:20",  
  "code": "1",  
  "bollardIndex": 4,  
  "probe": 12.5,  
  "distanceFromPrevious": 15.0,  
  "distanceFromStart": 132.2,  
  "latitude": 37.2614,  
  "longitude": -6.9447,  
  "outOfOrder": false,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Bollard NGSI-LD 规范化示例    
这是 Bollard 以 JSON-LD 格式表示的规范化示例。它与 NGSI-LD 兼容，当不使用选项时，返回单个实体的上下文数据。  
<details><summary><strong>显示/隐藏示例</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Bollard:urn:mrn:eshuv:facilities:bollard:id:20",  
  "type": "Bollard",  
  "portCode": {  
    "type": "Property",  
    "value": "ESVLC"  
  },  
  "facilityRef": {  
    "type": "Property",  
    "value": "urn:mrn:eshuv:facilities:facility:code:20"  
  },  
  "code": {  
    "type": "Property",  
    "value": "1"  
  },  
  "bollardIndex": {  
    "type": "Property",  
    "value": 4  
  },  
  "probe": {  
    "type": "Property",  
    "value": 12.5  
  },  
  "distanceFromPrevious": {  
    "type": "Property",  
    "value": 15.0  
  },  
  "distanceFromStart": {  
    "type": "Property",  
    "value": 132.2  
  },  
  "latitude": {  
    "type": "Property",  
    "value": 37.2614  
  },  
  "longitude": {  
    "type": "Property",  
    "value": -6.9447  
  },  
  "outOfOrder": {  
    "type": "Property",  
    "value": false  
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
参见 [FAQ 10](https://smartdatamodels.org/index.php/faqs/) 以获取有关如何处理量级单位的答案  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
