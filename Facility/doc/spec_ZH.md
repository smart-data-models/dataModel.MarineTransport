---
BEGIN 文档 ---
<!-- 10-Header -->  
 
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
 
实体：设施  
================ 
<!-- /10-Header -->  
 
<!-- 15-License -->  
 
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/Facility/LICENSE.md)  
 
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
 
<!-- 20-Description -->  
 
全局描述：**此数据模型描述了港口中的一个设施，可能包括泊位、终端或其他港口基础设施。**  
版本：0.0.1  
<!-- /20-Description -->  
 
<!-- 30-PropertiesList -->  
 
 
## 属性列表  
 
<sup><sub>[*] 如果属性中没有类型，是因为它可以有多种类型或不同的格式/模式</sub></sup>  
- `address[object]`：邮寄地址。模型：[https://schema.org/address](https://schema.org/address)  
	- `addressCountry[string]`：国家。例如，西班牙。模型：[https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`：街道地址所在的地区，并且在该地区。模型：[https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`：地区所在的地区，并且在该国家。模型：[https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`：区是一个类型的行政区划，在一些国家，由地方政府管理    
	- `postOfficeBoxNumber[string]`：邮政信箱地址的邮政信箱号码。例如，03578。模型：[https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`：邮政编码。例如，24004。模型：[https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`：街道地址。模型：[https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`：公众街道上特定属性的编号    
- `alternateName[string]`：此项的替代名称   
- `areaServed[string]`：服务或提供的项目所提供的的地理区域。模型：[https://schema.org/Text](https://schema.org/Text)  
- `bollardCodes[array]`：设施中可用的系泊柱代码列表。   
- `closed[boolean]`：指示设施是否当前关闭。   
- `dataProvider[string]`：一系列字符，用于识别和谐数据实体的提供者   
- `dateCreated[date-time]`：实体创建时间戳。这通常由存储平台分配   
- `dateModified[date-time]`：实体最后修改的时间戳。这通常由存储平台分配   
- `deadweight[number]`：允许在设施中停靠的船舶的最大死重量。   
- `description[string]`：此项的描述   
- `displacement[number]`：允许在设施中停靠的最大排水量。   
- `facilityCode[string]`：设施的代码。   
- `facilityName[string]`：设施的名称。   
- `facilityType[string]`：设施的类型，例如泊位、终端等。   
- `firstBollard[number]`：设施中的第一个系泊柱标识符。   
- `id[*]`：实体的唯一标识符   
- `lastBollard[number]`：设施中的最后一个系泊柱标识符。   
- `latitude[['number', 'null']]`：设施位置的纬度坐标。   
- `location[*]`：Geojson 引用项。它可以是点、线、多边形、多点、多线或多多边形   
- `longitude[number]`：设施位置的经度坐标。   
- `maxBeam[number]`：允许在设施中停靠的船舶的最大宽度（以米为单位）。   
- `maxDraught[number]`：允许在设施中停靠的最大吃水深度（以米为单位）。   
- `maxLoa[number]`：允许在设施中停靠的船舶的最大长度（以米为单位）。   
- `minimumProbe[number]`：设施的最小深度（以米为单位）。   
- `minimumProbeDate[date-time]`：最后记录最小深度的日期。   
- `modifiedDate[date-time]`：设施实体最后修改的日期和时间。   
- `mrn[string]`：MRN 编码标识符。它必须以一种众所周知的方式与实体相关联，所有后续方都将保持其原始值。此标识符必须是分配给 PortCall 实体的系统的唯一标识符。该 URN 应符合 MRN 和 IETF，特别是 RFC 2141、RFC 5234 和 RFC 8141。   
    提出的格式是   
    id::='urn:mrn:eshuv:<ONSS>:portcalls:facility:code:[0-9]+' 或    
    其中 OID:= 组织 UN/LOCODE，OONSS:= 服务组织名称，2099 是港口呼叫启动的年份，9999999 是发行方 Facility 实体在其系统中识别的唯一标识符（例如 SQL 行 ID），   
    例如 urn:mrn:eshuv:portcalls:facility:id:196   
    参见 [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) 以了解如何处理大小单位   
- `name[string]`：此项的名称   
- `navigationSector[string]`：与此设施相关的导航部门。   
- `owner[array]`：包含 JSON 编码序列的列表，引用所有者（s）的唯一 ID   
- `planningGroup[string]`：设施所属的规划组。   
- `portCode[string]`：设施所在港口的代码。   
- `remarks[string]`：关于设施的其他备注或说明。   
- `seeAlso[*]`：指向有关此项的其他资源的 URI 列表   
- `source[string]`：一个字符序列，用于给出实体数据的原始来源作为 URL。建议使用完全合格的域名或源对象的 URL   
- `terminal[string]`：与此设施相关的终端名称。   
- `terminalRef[string]`：与此设施相关的终端实体的引用。   
- `type[string]`：NGSI 实体类型。它必须是 Facility   
<!-- /30-PropertiesList -->  
 
<!-- 35-RequiredProperties -->  
 
必需属性  
- `id`   
- `portCode`   
- `type`   
<!-- /35-RequiredProperties -->  
 
<!-- 40-NotesYaml -->  
 
<!-- /40-NotesYaml -->  
 
<!-- 50-DataModelHeader -->  
 
## 属性的数据模型描述  
 
按字母顺序排序（单击以查看详细信息）  
<!-- /50-DataModelHeader -->  
 
<!-- 60-ModelYaml -->  
 
<details><summary><strong>完整的 yaml 详细信息</strong></summary>    
 
```yaml  
Facility:    
  description: This data model describes a facility in a port, which may include berths, terminals, or other port infrastructure.    
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
    bollardCodes:    
      description: List of bollard codes available at the facility.    
      items:    
        description: Any element in the list of bollard codes available at the facility.    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    closed:    
      description: Indicates if the facility is currently closed.    
      type: boolean    
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
    deadweight:    
      description: Maximum deadweight of vessels allowed in the facility.    
      type: number    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    displacement:    
      description: Maximum displacement allowed in the facility.    
      type: number    
      x-ngsi:    
        type: Property    
    facilityCode:    
      description: Code identifying the facility.    
      type: string    
      x-ngsi:    
        type: Property    
    facilityName:    
      description: Name of the facility.    
      type: string    
      x-ngsi:    
        type: Property    
    facilityType:    
      description: Type of facility, such as BERTH, TERMINAL, etc.    
      enum:    
        - BERTH    
        - TERMINAL    
        - ANCHORAGE    
        - OTHER    
      type: string    
      x-ngsi:    
        type: Property    
    firstBollard:    
      description: First bollard identifier in the facility.    
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
        type: Relationship    
    lastBollard:    
      description: Last bollard identifier in the facility.    
      type: number    
      x-ngsi:    
        type: Property    
    latitude:    
      description: Latitude coordinate of the facility location.    
      type:    
        - number    
        - 'null'    
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
      description: Longitude coordinate of the facility location.    
      type: number    
      x-ngsi:    
        type: Property    
    maxBeam:    
      description: Maximum beam width of vessels allowed in meters.    
      type: number    
      x-ngsi:    
        type: Property    
    maxDraught:    
      description: Maximum draught allowed in meters.    
      type: number    
      x-ngsi:    
        type: Property    
    maxLoa:    
      description: Maximum length overall (LOA) of vessels allowed in meters.    
      type: number    
      x-ngsi:    
        type: Property    
    minimumProbe:    
      description: Minimum depth of the facility in meters.    
      type: number    
      x-ngsi:    
        type: Property    
    minimumProbeDate:    
      description: Date when the minimum depth was last recorded.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    modifiedDate:    
      description: Date and time of last modification of the facility entity.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    mrn:    
      description: "MRN coded identifier. It has to be related to the entity in a way that is well-known by different organisms the meaning and the initiator of the entity, and all next parties will maintain on its origianl value. This identifier must be an UNIQUE identifier of the PortCall entity assigned by the system who created on first the entity. This URN should Conforms MRN & IETF specifically RFC 2141, RFC 5234, and RFC 8141. \n    The propossed format is \n    id::='urn:mrn:eshuv:<ONSS>:portcalls:facility:code:[0-9]+' or  \n    where OID:= Organisation UN/LOCODE, OONSS:=Organization Name of Service, 2099 the year on which the portcall was initiated, 9999999 an increasing, unique identifier that the issuer of the Facility entity will identify on his sistems (i.e. a SQL row-id), \n    i.e. urn:mrn:eshuv:portcalls:facility:id:196 \n     See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)In international standards is also known as [Ship's Visit]"    
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
    navigationSector:    
      description: Navigation sector associated with this facility.    
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
    planningGroup:    
      description: Planning group to which the facility belongs.    
      type: string    
      x-ngsi:    
        type: Property    
    portCode:    
      description: Code of the port where this facility is located.    
      type: string    
      x-ngsi:    
        type: Property    
    remarks:    
      description: Additional remarks or notes about the facility.    
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
    terminal:    
      description: Name of the terminal associated with this facility.    
      type: string    
      x-ngsi:    
        type: Property    
    terminalRef:    
      description: Reference to the terminal entity associated with this facility.    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be Facility    
      enum:    
        - Facility    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - portCode    
    - type    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/Facility/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/Facility/schema.json    
  x-model-tags: ESHUV    
  x-version: 0.0.1    
```  
</details>    
 
<!-- /60-ModelYaml -->  
 
<!-- 70-MiddleNotes -->  
 
<!-- /70-MiddleNotes -->  
 
<!-- 80-Examples -->  
 
## 示例有效载荷    
 
#### Facility NGSI-v2 键值示例    
 
这是一个 Facility 的 JSON 格式示例，作为键值。它与 NGSI-v2 兼容，当使用 `options=keyValues` 时，返回个别实体的上下文数据。  
<details><summary><strong>显示/隐藏示例</strong></summary>    
 
```json  
{  
  "id": "urn:mrn:eshuv:facilities:facility:code:20",  
  "type": "Facility",  
  "portCode": "ESVLC",  
  "facilityName": "Levante pesquero",  
  "facilityCode": "0011",  
  "facilityType": "BERTH",  
  "terminal": "Levante",  
  "terminalRef": "urn:mrn:eshuv:infrastructure:terminal:code:20",  
  "planningGroup": "Levante",  
  "navigationSector": "CINT",  
  "minimumProbe": 2.4,  
  "minimumProbeDate": "2024-12-01T00:00:00",  
  "displacement": 103500.00,  
  "latitude": 37.252290,  
  "longitude": -6.958843,  
  "deadweight": 35000.00,  
  "maxDraught": 4.0,  
  "maxLoa": 240.0,  
  "maxBeam": 36.50,  
  "remarks": "Levante pesquero",  
  "firstBollard": 1,  
  "lastBollard": 34,  
  "closed": false,  
  "bollardCodes" : [ "1", "2", "3", "4", "5" ]  
}  
```  
</details>  
 
#### Facility NGSI-v2 规范化示例    
 
这是一个 Facility 的 JSON 格式示例，作为规范化。它与 NGSI-v2 兼容，当不使用选项时，返回个别实体的上下文数据。  
<details><summary><strong>显示/隐藏示例</strong></summary>    
 
```json  
{  
  "id": "urn:mrn:eshuv:facilities:facility:code:20",  
  "type": "Facility",  
  "portCode": {  
    "type": "Text",  
    "value": "ESVLC"  
  },  
  "facilityName": {  
    "type": "Text",  
    "value": "Levante pesquero"  
  },  
  "facilityCode": {  
    "type": "Text",  
    "value": "0011"  
  },  
  "facilityType": {  
    "type": "Text",  
    "value": "BERTH"  
  },  
  "terminal": {  
    "type": "Text",  
    "value": "Levante"  
  },  
  "terminalRef": {  
    "type": "Text",  
    "value": "urn:mrn:eshuv:infrastructure:terminal:code:20"  
  },  
  "planningGroup": {  
    "type": "Text",  
    "value": "Levante"  
  },  
  "navigationSector": {  
    "type": "Text",  
    "value": "CINT"  
  },  
  "minimumProbe": {  
    "type": "Number",  
    "value": 2.4  
  },  
  "minimumProbeDate": {  
    "type": "DateTime",  
    "value": "2024-12-01T00:00:00"  
  },  
  "displacement": {  
    "type": "Number",  
    "value": 103500.0  
  },  
  "latitude": {  
    "type": "Number",  
    "value": 37.25229  
  },  
  "longitude": {  
    "type": "Number",  
    "value": -6.958843  
  },  
  "deadweight": {  
    "type": "Number",  
    "value": 35000.0  
  },  
  "maxDraught": {  
    "type": "Number",  
    "value": 4.0  
  },  
  "maxLoa": {  
    "type": "Number",  
    "value": 240.0  
  },  
  "maxBeam": {  
    "type": "Number",  
    "value": 36.5  
  },  
  "remarks": {  
    "type": "Text",  
    "value": "Levante pesquero"  
  },  
  "firstBollard": {  
    "type": "Number",  
    "value": 1  
  },  
  "lastBollard": {  
    "type": "Number",  
    "value": 34  
  },  
  "closed": {  
    "type": "Boolean",  
    "value": false  
  },  
  "bollardCodes": {  
    "type": "Array",  
    "value": [  
      "1",  
      "2",  
      "3",  
      "4",  
      "5"  
    ]  
  }  
}  
```  
</details>  
 
#### Facility NGSI-LD 键值示例    
 
这是一个 Facility 的 JSON-LD 格式示例，作为键值。它与 NGSI-LD 兼容，当使用 `options=keyValues` 时，返回个别实体的上下文数据。  
<details><summary><strong>显示/隐藏示例</strong></summary>    
 
```json  
{  
  "id": "urn:ngsi-ld:Facility:urn:mrn:eshuv:facilities:facility:code:20",  
  "type": "Facility",  
  "portCode": "ESVLC",  
  "facilityName": "Levante pesquero",  
  "facilityCode": "0011",  
  "facilityType": "BERTH",  
  "terminal": "Levante",  
  "terminalRef": "urn:mrn:eshuv:infrastructure:terminal:code:20",  
  "planningGroup": "Levante",  
  "navigationSector": "CINT",  
  "minimumProbe": 2.4,  
  "minimumProbeDate": "2024-12-01T00:00:00",  
  "displacement": 103500.0,  
  "latitude": 37.25229,  
  "longitude": -6.958843,  
  "deadweight": 35000.0,  
  "maxDraught": 4.0,  
  "maxLoa": 240.0,  
  "maxBeam": 36.5,  
  "remarks": "Levante pesquero",  
  "firstBollard": 1,  
  "lastBollard": 34,  
  "closed": false,  
  "bollardCodes": [  
    "1",  
    "2",  
    "3",  
    "4",  
    "5"  
  ],  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```  
</details>  
 
#### Facility NGSI-LD 规范化示例    
 
这是一个 Facility 的 JSON-LD 格式示例，作为规范化。它与 NGSI-LD 兼容，当不使用选项时，返回个别实体的上下文数据。  
<details><summary><strong>显示/隐藏示例</strong></summary>    
 
```json  
{  
  "id": "urn:ngsi-ld:Facility:urn:mrn:eshuv:facilities:facility:code:20",  
  "type": "Facility",  
  "portCode": {  
    "type": "Property",  
    "value": "ESVLC"  
  },  
  "facilityName": {  
    "type": "Property",  
    "value": "Levante pesquero"  
  },  
  "facilityCode": {  
    "type": "Property",  
    "value": "0011"  
  },  
  "facilityType": {  
    "type": "Property",  
    "value": "BERTH"  
  },  
  "terminal": {  
    "type": "Property",  
    "value": "Levante"  
  },  
  "terminalRef": {  
    "type": "Property",  
    "value": "urn:mrn:eshuv:infrastructure:terminal:code:20"  
  },  
  "planningGroup": {  
    "type": "Property",  
    "value": "Levante"  
  },  
  "navigationSector": {  
    "type": "Property",  
    "value": "CINT"  
  },  
  "minimumProbe": {  
    "type": "Property",  
    "value": 2.4  
  },  
  "minimumProbeDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-12-01T00:00:00"  
    }  
  },  
  "displacement": {  
    "type": "Property",  
    "value": 103500.0  
  },  
  "latitude": {  
    "type": "Property",  
    "value": 37.25229  
  },  
  "longitude": {  
    "type": "Property",  
    "value": -6.958843  
  },  
  "deadweight": {  
    "type": "Property",  
    "value": 35000.0  
  },  
  "maxDraught": {  
    "type": "Property",  
    "value": 4.0  
  },  
  "maxLoa": {  
    "type": "Property",  
    "value": 240.0  
  },  
  "maxBeam": {  
    "type": "Property",  
    "value": 36.5  
  },  
  "remarks": {  
    "type": "Property",  
    "value": "Levante pesquero"  
  },  
  "firstBollard": {  
    "type": "Property",  
    "value": 1  
  },  
  "lastBollard": {  
    "type": "Property",  
    "value": 34  
  },  
  "closed": {  
    "type": "Property",  
    "value": false  
  },  
  "bollardCodes": {  
    "type": "Property",  
    "value": [  
      "1",  
      "2",  
      "3",  
      "4",  
      "5"  
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
 
参见 [FAQ 10](https://smartdatamodels.org/index.php/faqs/) 以了解如何处理大小单位  
<!-- /95-Units -->  
 
<!-- 97-LastFooter -->  
 
---  
 
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
 
--- END 文档 ---