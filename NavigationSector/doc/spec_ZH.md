<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：导航区  
========================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/NavigationSector/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**此数据模型描述了港口中的导航区，包括地理边界和操作细节**  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，则可能有多种类型或不同的格式/模式</sub></sup>  
- `address[object]`：邮寄地址。模型：[https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`：国家。例如，西班牙。模型：[https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`：街道地址所在的地区，并且位于该地区。模型：[https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`：地区所在的地区，并且位于该国家。模型：[https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`：区是一个类型的行政区划，在某些国家，由地方政府管理    
	- `postOfficeBoxNumber[string]`：邮政信箱地址的邮政信箱号码。例如，03578。模型：[https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`：邮政编码。例如，24004。模型：[https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`：街道地址。模型：[https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`：公众街道上特定属性的标识符    
- `alternateName[string]`：此项的替代名称  - `areaServed[string]`：服务或提供的项目所提供的地理区域。模型：[https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`：一个序列的字符，标识和谐数据实体的提供者  - `dateCreated[date-time]`：实体创建时间戳。这通常由存储平台分配  - `dateModified[date-time]`：实体最后修改的时间戳。这通常由存储平台分配  - `description[string]`：此项的描述  - `id[*]`：实体的唯一标识符  - `location[*]`：Geojson 引用项。它可以是点、线字符串、多边形、多点、多线字符串或多多边形  - `minProbe[number]`：该区域内的最小水深（以米为单位）  - `minProbeDate[date-time]`：最后记录最小水深的日期  - `modifiedDate[date-time]`：导航区实体最后修改的日期和时间  - `mrn[string]`：MRN 编码标识符。它必须以一种众所周知的方式与实体相关联，并且所有后续方都将保持其原始值。该标识符必须是系统创建的实体的唯一标识符。该URN应符合MRN和IETF，特别是RFC 2141、RFC 5234和RFC 8141。   
    提出的格式是   
    id::='urn:mrn:eshuv:<ONSS>:portcalls:navigationsector:id:[0-9]+' 或    
    其中 OID:= 组织 UN/LOCODE，OONSS:= 服务组织名称，2099 是港口呼叫启动的年份，9999999 是发行方的唯一标识符（例如SQL行ID）   
    例如urn:mrn:eshuv:portcalls:navigationsector:id:16   
     参见 [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) 在国际标准中也称为 [船舶访问]  - `name[string]`：此项的名称  - `navigationArea[string]`：此导航区所在的更广泛的导航区域  - `navigationSector[string]`：导航区在港口中的标识符  - `owner[array]`：包含对所有者（s）唯一 ID 的 JSON 编码序列的列表  - `portCode[string]`：此导航区所在港口的代码  - `rank[number]`：导航区的等级或优先级  - `remarks[string]`：关于导航区的其他备注或说明  - `sectorType[string]`：导航区的类型  - `seeAlso[*]`：指向有关此项的其他资源的 URI 列表  - `source[string]`：实体数据的原始来源的字符序列，以 URL 形式给出。建议使用完全合格的域名或源对象的 URL  - `type[string]`：NGSI 实体类型。必须是 NavigationSector  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排序（单击查看详细信息）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>完整的 yaml 详细信息</strong></summary>    
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
## 示例有效载荷    
#### 导航区 NGSI-v2 键值示例    
这是导航区在 JSON 格式中的键值示例。它与 NGSI-v2 兼容，当使用 `options=keyValues` 时，返回个别实体的上下文数据。  
<details><summary><strong>显示/隐藏示例</strong></summary>    
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
#### 导航区 NGSI-v2 规范示例    
这是导航区在 JSON 格式中的规范示例。它与 NGSI-v2 兼容，当不使用选项时，返回个别实体的上下文数据。  
<details><summary><strong>显示/隐藏示例</strong></summary>    
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
#### 导航区 NGSI-LD 键值示例    
这是导航区在 JSON-LD 格式中的键值示例。它与 NGSI-LD 兼容，当使用 `options=keyValues` 时，返回个别实体的上下文数据。  
<details><summary><strong>显示/隐藏示例</strong></summary>    
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
#### 导航区 NGSI-LD 规范示例    
这是导航区在 JSON-LD 格式中的规范示例。它与 NGSI-LD 兼容，当不使用选项时，返回个别实体的上下文数据。  
<details><summary><strong>显示/隐藏示例</strong></summary>    
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
参见 [FAQ 10](https://smartdatamodels.org/index.php/faqs/) 以获取有关如何处理数量单位的答案  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
