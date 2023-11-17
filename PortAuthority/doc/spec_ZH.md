<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：港口管理局    
========<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/PortAuthority/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全局描述：**该数据模型旨在提供有关港务局的信息**。    
版本： 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 属性列表    
<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。    
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理      
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `contactPoint[object]`: 与物品联系的详细信息  . Model: [https://schema.org/ContactPoint](https://schema.org/ContactPoint)	- `areaServed[string]`: 提供服务或所提供项目的地理区域。取代服务区域      
	- `availabilityRestriction[*]`: 该属性将一个联络点与该联络点不在时的信息联系起来。详细信息通过 "开放时间规范 "类提供  . Model: [http://schema.org/hoursAvailable](http://schema.org/hoursAvailable)    
	- `availableLanguage[*]`: 某人在使用物品、服务或场所时可能使用的语言。请使用 IETF BCP 47 标准中的一种语言代码。可使用 "文本 "选项，但也可以使用 "语言 "选项。  . Model: [http://schema.org/availableLanguage](http://schema.org/availableLanguage)    
	- `contactOption[*]`: 该联络点的可用选项（如免费电话号码或对听力受损来电者的支持）  . Model: [http://schema.org/contactOption](http://schema.org/contactOption)    
	- `contactType[string]`: 此项目的联系类型      
	- `email[idn-email]`: 所有者的电子邮件地址      
	- `faxNumber[string]`: 传真号码  . Model: [http://schema.org/Text](http://schema.org/Text)    
	- `name[string]`: 该项目的名称      
	- `productSupported[string]`: 该支持联络点所涉及的产品或服务（如特定产品系列的产品支持）。可以是特定产品或产品系列（如 "iPhone"），也可以是产品或服务的一般类别（如 "智能手机）  . Model: [http://schema.org/Text](http://schema.org/Text)    
	- `telephone[string]`: 联系人电话      
- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `timezone[string]`: 所提供的值应为 IANA 时区数据库中列出的值。参见 [时区数据库](https://timezonedb.com/time-zones)  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI 实体类型。必须是 PortAuthority  - `unlocode[string]`: 联合国贸易和运输地点代码。参见 [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
所需属性    
- `id`  - `location`  - `type`  - `unlocode`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 属性的数据模型描述    
按字母顺序排列（点击查看详情）    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
PortAuthority:      
  description: The data model is intended to provide information about Port Authorities      
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
    contactPoint:      
      description: The details to contact with the item      
      properties:      
        areaServed:      
          description: The geographic area where a service or offered item is provided. Supersedes serviceArea      
          type: string      
          x-ngsi:      
            type: Property      
        availabilityRestriction:      
          anyOf:      
            - description: Array of identifiers format of any NGSI entity      
              items:      
                maxLength: 256      
                minLength: 1      
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
                type: string      
              type: array      
              x-ngsi:      
                type: Property      
            - description: Array of identifiers format of any NGSI entity      
              items:      
                format: uri      
                type: string      
              type: array      
              x-ngsi:      
                type: Property      
          description: This property links a contact point to information about when the contact point is not available. The details are provided using the Opening Hours Specification class      
          x-ngsi:      
            model: http://schema.org/hoursAvailable      
            type: Relationship      
        availableLanguage:      
          anyOf:      
            - anyOf:      
                - type: string      
                - items:      
                    type: string      
                  type: array      
          description: 'A language someone may use with or at the item, service or place. Please use one of the language codes from the IETF BCP 47 standard. It is implemented the Text option but it could be also Language'      
          x-ngsi:      
            model: http://schema.org/availableLanguage      
            type: Property      
        contactOption:      
          anyOf:      
            - type: string      
            - items:      
                type: string      
              type: array      
          description: An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers)      
          x-ngsi:      
            model: http://schema.org/contactOption      
            type: Property      
        contactType:      
          description: Contact type of this item      
          type: string      
          x-ngsi:      
            type: Property      
        email:      
          description: Email address of owner      
          format: idn-email      
          type: string      
          x-ngsi:      
            type: Property      
        faxNumber:      
          description: The fax number      
          type: string      
          x-ngsi:      
            model: http://schema.org/Text      
            type: Property      
        name:      
          description: The name of this item      
          type: string      
          x-ngsi:      
            type: Property      
        productSupported:      
          description: The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. 'iPhone') or a general category of products or services (e.g. 'smartphones')      
          type: string      
          x-ngsi:      
            model: http://schema.org/Text      
            type: Property      
        telephone:      
          description: Telephone of this contact      
          type: string      
          x-ngsi:      
            type: Property      
        url:      
          description: URL which provides a description or further information about this item      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/ContactPoint      
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
    timezone:      
      description: 'The value provided should be among those listed in the IANA Time Zone Database. See [Time Zone Database](https://timezonedb.com/time-zones)'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    type:      
      description: NGSI Entity type. It has to be PortAuthority      
      enum:      
        - PortAuthority      
      type: string      
      x-ngsi:      
        type: Property      
    unlocode:      
      description: 'United Nations Code for Trade and Transport Locations. See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
  required:      
    - id      
    - type      
    - location      
    - unlocode      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/PortAuthority/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Ports/PortAuthority/schema.json      
  x-model-tags: ""      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 有效载荷示例    
#### PortAuthority NGSI-v2 密钥值示例    
下面是一个以 JSON-LD 格式作为键值的 PortAuthority 的示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:mrn:amura:port-authority:UNLOCODE",  
  "type": "PortAuthority",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -0.3048254137983776,  
      39.431348987126704  
    ]  
  },  
  "name": "Port Authoriy name",  
  "unlocode": "Unlocode",  
  "description": "Port Authoriy description",  
  "timezone": "Europe/London",  
  "address": {  
    "streetAddress": "Avda. Example",  
    "addressCountry": "ES",  
    "addressLocality": "Locality",  
    "postalCode": "1234"  
  },  
  "contactPoint": {  
    "telephone": "+34 12 34 56 78",  
    "email": "example@portauthority.com",  
    "availableLanguage": [  
      "en-EN",  
      "es-ES"  
    ],  
    "faxNumber": "12 345 67 89",  
    "name": "Port Authoriy name",  
    "url": "https://URL"  
  }  
}  
```  
</details>    
#### PortAuthority NGSI-v2 标准化示例    
下面是一个规范化的 JSON-LD 格式的 PortAuthority 示例。当不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:mrn:amura:port-authority:UNLOCODE",  
  "type": "PortAuthority",  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -0.3048254137983776,  
        39.431348987126704  
      ]  
    }  
  },  
  "name": {  
    "type": "Text",  
    "value": "Port Authoriy name"  
  },  
  "unlocode": {  
    "type": "Text",  
    "value": "Unlocode"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Port Authoriy description"  
  },  
  "timezone": {  
    "type": "Text",  
    "value": "Europe/London"  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Avda. Example",  
      "addressCountry": "ES",  
      "addressLocality": "Locality",  
      "postalCode": "1234"  
    }  
  },  
  "contactPoint": {  
    "type": "StructuredValue",  
    "value": {  
      "telephone": "+34 12 34 56 78",  
      "email": "example@port.com",  
      "availableLanguage": [  
        "en-EN",  
        "es-ES"  
      ],  
      "faxNumber": "12 345 67 89",  
      "name": "Portname",  
      "url": "https://URL"  
    }  
  }  
}  
```  
</details>    
#### PortAuthority NGSI-LD 密钥值 示例    
下面是一个以 JSON-LD 格式作为键值的 PortAuthority 的示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:mrn:amura:port-authority:UNLOCODE",  
  "type": "PortAuthority",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -0.3048254137983776,  
      39.431348987126704  
    ]  
  },  
  "name": "Port Authoriy name",  
  "unlocode": "Unlocode",  
  "description": "Port Authoriy description",  
  "timezone": "Europe/London",  
  "address": {  
    "streetAddress": "Avda. Example",  
    "addressCountry": "ES",  
    "addressLocality": "Locality",  
    "postalCode": "1234"  
  },  
  "contactPoint": {  
    "telephone": "+34 12 34 56 78",  
    "email": "example@portauthority.com",  
    "availableLanguage": [  
      "en-EN",  
      "es-ES"  
    ],  
    "faxNumber": "12 345 67 89",  
    "name": "Port Authoriy name",  
    "url": "https://URL"  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/context.jsonld",  
    "https://gitlab.com/hiades/fiware/smart-data-models/-/raw/main/context.jsonld"  
  ]  
}  
```  
</details>    
#### PortAuthority NGSI-LD 标准化示例    
下面是一个规范化的 JSON-LD 格式的 PortAuthority 示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:mrn:amura:port-authority:UNLOCODE",  
  "type": "PortAuthority",  
  "location": {  
      "type": "GeoProperty",  
      "value": {  
          "type": "Point",  
          "coordinates": [  
              -0.3048254137983776,  
              39.431348987126704  
          ]  
      }  
  },  
  "name": {  
    "type": "Property",  
    "value": "Port Authoriy name"  
  },  
  "unlocode": {  
    "type": "Property",  
    "value": "Unlocode"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Port Authoriy description"  
  },  
  "timezone": {  
    "type": "Property",  
    "value": "Europe/London"  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Avda. Example",  
      "addressCountry": "ES",  
      "addressLocality": "Locality",  
      "postalCode": "1234"  
    }  
  },  
  "contactPoint": {  
    "type": "Property",  
    "value": {  
      "telephone": "+34 12 34 56 78",  
      "email": "example@port.com",  
      "availableLanguage": [  
        "en-EN",  
        "es-ES"  
      ],  
      "faxNumber": "12 345 67 89",  
      "name": "Portname",  
      "url": "https://URL"  
    }  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/context.jsonld",  
    "https://gitlab.com/hiades/fiware/smart-data-models/-/raw/main/context.jsonld"  
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
