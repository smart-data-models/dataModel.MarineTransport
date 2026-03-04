<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：公司  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/Company/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**该数据模型描述了港口中的公司**  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可以有多种类型或不同的格式/模式</sub></sup>  
- `active[boolean]`：公司或实体在港口中的活动或责任的激活状态  - `address[object]`：邮寄地址。 模型：[https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`：国家。 例如，西班牙。 模型：[https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`：街道地址所在的地区，并且该地区位于区域内。 模型：[https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`：地区所在的区域，并且该区域位于国家内。 模型：[https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`：一个地区是一种行政区划，在某些国家，由地方政府管理    
	- `postOfficeBoxNumber[string]`：邮政信箱地址的邮政信箱号码。 例如，03578。 模型：[https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`：邮政编码。 例如，24004。 模型：[https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`：街道地址。 模型：[https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`：公共街道上特定属性的标识号    
- `admissionDate[date-string]`：公司在模型中注册的日期  - `alias[string]`：公司或实体在港口中的非官方名称（昵称）  - `alternateName[string]`：该项的另一个名称  - `areaServed[string]`：服务或提供的项目所提供的的地理区域。 模型：[https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`：一个字符序列，用于标识和谐数据实体的提供者  - `dateCreated[date-time]`：实体创建的时间戳。 这通常由存储平台分配  - `dateModified[date-time]`：实体最后修改的时间戳。 这通常由存储平台分配  - `description[string]`：对该项的描述  - `email[idn-email]`：所有者的电子邮件地址  - `entityType[string]`：公司或实体在港口中的类型  - `id[*]`：实体的唯一标识符  - `legalCode[string]`：公司或实体在港口中的代码  - `licenses[array]`：公司的营业许可。 通常成对出现，代码和描述  - `location[*]`：项目的Geojson引用。 可以是Point、LineString、Polygon、MultiPoint、MultiLineString或MultiPolygon  - `mrn[string]`：MRN编码标识符。 这个URN应该符合MRN和IETF，特别是RFC 2141、RFC 5234和RFC 8141。 提出的格式是 id::='urn:mrn:<PORT>:<ONSS>:community:company:id:[0-9]+' 或 PORT := UN/LOCODE港口，OID:= 组织UN/LOCODE，OONSS:= 服务组织名称，9999999是一个唯一标识符，公司注册实体的创建者将在其系统中识别（例如，SQL行ID），即urn:mrn:eshuv:community:company:id:1296  - `name[string]`：该项的名称  - `owner[array]`：包含JSON编码序列的列表，引用所有者（s）的唯一ID  - `registeredName[string]`：公司或实体在港口中的官方名称  - `seeAlso[*]`：指向该项的其他资源的URI列表  - `source[string]`：一个字符序列，给出实体数据的原始来源作为URL。 推荐使用完全合格的域名或源对象的URL  - `telephone[string]`：此联系人的电话  - `type[*]`：NGSI实体类型。 必须是公司  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 数据模型属性描述  
按字母顺序排序（点击查看详细信息）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>完整的YAML详细信息</strong></summary>    
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
## 示例有效载荷    
#### 公司NGSI-v2键值示例    
这是一个公司在JSON格式中的键值示例。 这与NGSI-v2兼容，当使用`options=keyValues`时，返回个别实体的上下文数据。  
<details><summary><strong>显示/隐藏示例</strong></summary>    
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
#### 公司NGSI-v2规范示例    
这是一个公司在JSON格式中的规范示例。 这与NGSI-v2兼容，当不使用选项时，返回个别实体的上下文数据。  
<details><summary><strong>显示/隐藏示例</strong></summary>    
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
#### 公司NGSI-LD键值示例    
这是一个公司在JSON-LD格式中的键值示例。 这与NGSI-LD兼容，当使用`options=keyValues`时，返回个别实体的上下文数据。  
<details><summary><strong>显示/隐藏示例</strong></summary>    
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
#### 公司NGSI-LD规范示例    
这是一个公司在JSON-LD格式中的规范示例。 这与NGSI-LD兼容，当不使用选项时，返回个别实体的上下文数据。  
<details><summary><strong>显示/隐藏示例</strong></summary>    
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
请参阅[FAQ 10](https://smartdatamodels.org/index.php/faqs/)以了解如何处理数量单位  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
