<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：端口呼叫  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/PortCall/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述：**靠港是指船只到港口停靠一段时间，以执行某种有用的功能，如装卸货物。  
版本： 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。  
- `UNLOCODE[string]`: 港口的联合国贸易和运输地点代码[UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)  - `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理    
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 在公共街道上标识特定房产的编号    
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrivalDate[date-time]`: 船舶抵达港区的日期/时间  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `arrivalDateScheduled[date-time]`: 船运代理申报的船舶抵达港区的预定日期/时间  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `departureDate[date-time]`: 船舶离开港区的日期/时间  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `departureDateScheduled[date-time]`: 船运代理申报的船舶离开港区的预定日期/时间  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: 项目描述  - `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `regularLine[string]`: 端口呼叫的常规线路  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `status[string]`: 操作状态。枚举："估计、授权、运行、完成"。  - `terminal[string]`: 端口呼叫终端  - `type[string]`: NGSI 实体类型。必须是 PortCall  - `vessel[object]`: 呼叫港口的船只  	- `IMO[number]`: 按照国际海事组织规定的[方案](https://www.imo.org/en/OurWork/IIIS/Pages/IMO-Identification-Number-Schemes.aspx) 确定的国际海事组织船舶识别号。    
	- `shipName[string]`: 船名    
	- `shipTypeCategory[string]`: 船舶类别说明。枚举："集装箱、普通货物（非专用）、散装液体、散装干货、游轮"。    
	- `shipTypeClass[string]`: 船舶类别描述。枚举："多层油轮、化学品油轮、满载油轮、油轮、散装货轮、轻型油轮"。    
- `vesselAgent[string]`: 港口呼叫的船舶代理  - `voyageCode[string]`: 航次代码（航次的唯一 ID）  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `arrivalDate`  - `id`  - `type`  - `vessel`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
数据模型来自 H2020 项目数据端口。  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PortCall:    
  description: 'A Port Call is a vessel''s visit to the port for a period of time, in order to perform some kind of useful function, like the loading or unloading of goods.'    
  properties:    
    UNLOCODE:    
      description: 'United Nations Code for Trade and Transport Locations, [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory), of the port'    
      type: string    
      x-ngsi:    
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
    arrivalDate:    
      description: Date/time of ship arrival at port area    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    arrivalDateScheduled:    
      description: 'Scheduled date/time of ship arrival at port area, as declared by shipping agent'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
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
    departureDate:    
      description: Date/time of ship leaving port area    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    departureDateScheduled:    
      description: 'Scheduled date/time of ship leaving port area, as declared by shipping agent'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
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
    regularLine:    
      description: Regular line of the portcall    
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
      description: 'Status of the operation. Enum: ''Estimated, Authorized, Operational, Completed'''    
      enum:    
        - Estimated    
        - Authorized    
        - Operational    
        - Completed    
      type: string    
      x-ngsi:    
        type: Property    
    terminal:    
      description: Terminal of the portcall    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be PortCall    
      enum:    
        - PortCall    
      type: string    
      x-ngsi:    
        type: Property    
    vessel:    
      description: Calling vessel of the portcall    
      properties:    
        IMO:    
          description: 'IMO ship identification number, following the [scheme](https://www.imo.org/en/OurWork/IIIS/Pages/IMO-Identification-Number-Schemes.aspx) defined by the International Maritime Organization.'    
          type: number    
          x-ngsi:    
            type: Property    
        shipName:    
          description: Name of the vessel    
          type: string    
          x-ngsi:    
            type: Property    
        shipTypeCategory:    
          description: 'Description of vessel category. Enum: ''CONTAINER, GENERAL CARGO NON SPECIALIZED, LIQUID BULK, DRY BULK, CRUISE'''    
          enum:    
            - CONTAINER    
            - GENERAL CARGO NON SPECIALIZED    
            - LIQUID BULK    
            - DRY BULK    
            - CRUISE    
          type: string    
          x-ngsi:    
            type: Property    
        shipTypeClass:    
          description: 'Description of vessel class. Enum: ''MULTI-DECKER, CHEMICAL TANKER, FULL CONTAINER, OIL TANKER, BULK CARRIER, LG TANKER'''    
          enum:    
            - MULTI-DECKER    
            - CHEMICAL TANKER    
            - FULL CONTAINER    
            - OIL TANKER    
            - BULK CARRIER    
            - LG TANKER    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    vesselAgent:    
      description: Vessel Agent of the portcall    
      type: string    
      x-ngsi:    
        type: Property    
    voyageCode:    
      description: Voyage code (unique ID of a voyage)    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - vessel    
    - arrivalDate    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2024 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/PortCall/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/PortCall/schema.json    
  x-model-tags: i4trust    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
#### PortCall NGSI-v2 键值示例  
下面是一个以 JSON-LD 格式作为键值的 PortCall 实例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PortCall:VPF:1202106029",  
  "type": "PortCall",  
  "UNLOCODE": "ESVLC",  
  "arrivalDate": "2021-12-01T00:46:00Z",  
  "arrivalDateScheduled": "2021-12-01T00:46:00Z",  
  "departureDate": "2021-12-01T11:35:00Z",  
  "departureDateScheduled": "2021-12-01T11:35:00Z",  
  "regularLine": "GRIMALDI - SHORT SEA SERVICE B",  
  "status": "Completed",  
  "terminal": "VALENCIA TERMINAL EUROPA, S.A.",  
  "vessel": {  
    "shipName": "ECO BARCELONA",  
    "IMO": 8712345,  
    "shipTypeCategory": "CONTAINER",  
    "shipTypeClass": "FULL CONTAINER"  
  },  
  "vesselAgent": "GRIMALDI LOGISTICA ESPA\u00d1A S.L.",  
  "voyageCode": "1202106029"  
}  
```  
</details>  
#### PortCall NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的 PortCall 示例。当不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PortCall:VPF:1202106029",  
  "type": "PortCall",  
  "UNLOCODE": {  
    "type": "Text",  
    "value": "ESVLC",  
    "metadata": {}  
  },  
  "arrivalDate": {  
    "type": "DateTime",  
    "value": "2021-12-01T00:46:00Z",  
    "metadata": {}  
  },  
  "arrivalDateScheduled": {  
    "type": "DateTime",  
    "value": "2021-12-01T00:46:00Z",  
    "metadata": {}  
  },  
  "departureDate": {  
    "type": "DateTime",  
    "value": "2021-12-01T11:35:00Z",  
    "metadata": {}  
  },  
  "departureDateScheduled": {  
    "type": "DateTime",  
    "value": "2021-12-01T11:35:00Z",  
    "metadata": {}  
  },  
  "regularLine": {  
    "type": "Text",  
    "value": "GRIMALDI - SHORT SEA SERVICE B",  
    "metadata": {}  
  },  
  "status": {  
    "type": "Text",  
    "value": "Completed",  
    "metadata": {}  
  },  
  "terminal": {  
    "type": "Text",  
    "value": "VALENCIA TERMINAL EUROPA, S.A.",  
    "metadata": {}  
  },  
  "vessel": {  
    "type": "StructuredValue",  
    "value": {  
      "shipName": "ECO BARCELONA",  
      "IMO": 8712345,  
      "shipTypeCategory": "CONTAINER",  
      "shipTypeClass": "FULL CONTAINER"  
    },  
    "metadata": {}  
  },  
  "vesselAgent": {  
    "type": "Text",  
    "value": "GRIMALDI LOGISTICA ESPA\u00d1A S.L.",  
    "metadata": {}  
  },  
  "voyageCode": {  
    "type": "Text",  
    "value": "1202106029",  
    "metadata": {}  
  }  
}  
```  
</details>  
#### PortCall NGSI-LD 键值示例  
下面是一个以 JSON-LD 格式作为键值的 PortCall 实例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PortCall:VPF:1202106029",  
  "type": "PortCall",  
  "UNLOCODE": "ESVLC",  
  "arrivalDate": "2021-12-01T00:46:00Z",  
  "arrivalDateScheduled": "2021-12-01T00:46:00Z",  
  "departureDate": "2021-12-01T11:35:00Z",  
  "departureDateScheduled": "2021-12-01T11:35:00Z",  
  "regularLine": "GRIMALDI - SHORT SEA SERVICE B",  
  "status": "Completed",  
  "terminal": "VALENCIA TERMINAL EUROPA, S.A.",  
  "vessel": {  
    "shipName": "ECO BARCELONA",  
    "IMO": 8712345,  
    "shipTypeCategory": "CONTAINER",  
    "shipTypeClass": "FULL CONTAINER"  
  },  
  "vesselAgent": "GRIMALDI LOGISTICA ESPA\u00d1A S.L.",  
  "voyageCode": "1202106029",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### PortCall NGSI-LD 标准化示例  
下面是一个规范化 JSON-LD 格式的 PortCall 示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PortCall:VPF:1202106029",  
  "type": "PortCall",  
  "UNLOCODE": {  
    "type": "Text",  
    "value": "ESVLC"  
  },  
  "arrivalDate": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2021-12-01T00:46:00Z"  
    }  
  },  
  "arrivalDateScheduled": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2021-12-01T00:46:00Z"  
    }  
  },  
  "departureDate": {  
    "type": "Property",  
    "value": "2021-12-01T11:35:00Z",  
    "metadata": {}  
  },  
  "departureDateScheduled": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2021-12-01T11:35:00Z"  
    }  
  },  
  "regularLine": {  
    "type": "Property",  
    "value": "GRIMALDI - SHORT SEA SERVICE B"  
  },  
  "status": {  
    "type": "Property",  
    "value": "Completed"  
  },  
  "terminal": {  
    "type": "Property",  
    "value": "VALENCIA TERMINAL EUROPA, S.A."  
  },  
  "vessel": {  
    "type": "Property",  
    "value": {  
      "shipName": "ECO BARCELONA",  
      "IMO": 8712345,  
      "shipTypeCategory": "CONTAINER",  
      "shipTypeClass": "FULL CONTAINER"  
    }  
  },  
  "vesselAgent": {  
    "type": "Property",  
    "value": "GRIMALDI LOGISTICA ESPAÃ‘A S.L."  
  },  
  "voyageCode": {  
    "type": "Property",  
    "value": "1202106029"  
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
