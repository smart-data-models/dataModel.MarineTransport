---
 
<!-- 10-Header --> 
 
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
 
实体：KeyVessel 
================= 
<!-- /10-Header --> 
 
<!-- 15-License --> 
 
 
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/KeyVessel/LICENSE.md)  
 
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60) 
<!-- /15-License --> 
 
<!-- 20-Description --> 
 
 
全局描述：**数据模型旨在提供有关港口社区必须在接下来的几天内关注的关键船舶的信息。它允许表示每艘船舶的属性：静态和动态信息** 
 
版本：0.0.1 
<!-- /20-Description --> 
 
<!-- 30-PropertiesList -->  
 
 
## 属性列表 
 
 
<sup><sub>[*] 如果属性中没有类型，则可能有多种类型或不同的格式/模式</sub></sup> 
- `address[object]`：邮寄地址。模型：[https://schema.org/address](https://schema.org/address) 
    - `addressCountry[string]`：国家。例如，西班牙。模型：[https://schema.org/addressCountry](https://schema.org/addressCountry) 
    - `addressLocality[string]`：街道地址所在的地区，并且该地区在该地区。模型：[https://schema.org/addressLocality](https://schema.org/addressLocality) 
    - `addressRegion[string]`：该地区所在的地区，并且该地区在该国家。模型：[https://schema.org/addressRegion](https://schema.org/addressRegion) 
    - `district[string]`：区是一种行政区划，在一些国家，由地方政府管理 
    - `postOfficeBoxNumber[string]`：邮政信箱地址的邮政信箱号码。例如，03578。模型：[https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber) 
    - `postalCode[string]`：邮政编码。例如，24004。模型：[https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode) 
    - `streetAddress[string]`：街道地址。模型：[https://schema.org/streetAddress](https://schema.org/streetAddress) 
    - `streetNr[string]`：在公共街道上标识特定属性的编号 
- `alternateName[string]`：此项的替代名称 
- `areaServed[string]`：服务或提供的项目所提供的的地理区域。模型：[https://schema.org/Text](https://schema.org/Text) 
- `callSign[string]`：海事呼号是分配给船舶的唯一标识符。模型：[https://schema.org/Text](https://schema.org/Text) 
- `courseOverGround[number]`：地面航向（COG）。模型：[https://schema.org/Number](https://schema.org/Number) 
- `createdDate[date-time]`：实体创建的日期和时间，以ISO 8601 UTC格式表示。模型：[https://schema.org/Text](https://schema.org/Text) 
- `dataProvider[string]`：一串字符，标识提供的数据实体的提供者。模型：[https://schema.org/Text](https://schema.org/Text) 
- `dateCreated[date-time]`：实体创建的时间戳。这通常由存储平台分配 
- `dateModified[date-time]`：实体最后修改的时间戳。这通常由存储平台分配 
- `deletedDate[date-time]`：实体删除的日期和时间，以ISO 8601 UTC格式表示。模型：[https://schema.org/Text](https://schema.org/Text) 
- `description[string]`：此项的描述 
- `etaAis[date-time]`：预计到达时间，如AIS系统报告，以ISO 8601 UTC格式表示。模型：[https://schema.org/Text](https://schema.org/Text) 
- `etaAlgorithm[date-time]`：预计到达时间，根据船舶位置计算，以ISO 8601 UTC格式表示。模型：[https://schema.org/Text](https://schema.org/Text) 
- `flagCode[string]`：海事呼号是分配给船舶的唯一标识符。模型：[https://schema.org/Text](https://schema.org/Text) 
- `id[*]`：实体的唯一标识符 
- `imo[number]`：国际海事组织编号（全球永久UID）。模型：[https://schema.org/Number](https://schema.org/Number) 
- `lastPortCode[string]`：最后一个港口，编码。代表港口的代码，即到达港口之前的港口，如果有的话。[EMSWe：DE-005-05] [EDIFACT：LOC-3227-92] [IMO：IMO0076]。模型：[https://schema.org/Text](https://schema.org/Text) 
- `latitude[number]`：船舶的纬度坐标 
- `location[*]`：Geojson引用到船舶位置。它必须是一个点，即船舶在观察日期所在的位置 
- `longitude[number]`：船舶的经度坐标 
- `mmsi[number]`：移动海事服务身份编号（一个暂时分配的UID，由该对象的当前国旗状态颁发）。模型：[https://schema.org/Number](https://schema.org/Number) 
- `modifiedDate[date-time]`：实体最后修改的日期和时间，以ISO 8601 UTC格式表示。模型：[https://schema.org/Text](https://schema.org/Text) 
- `name[string]`：此项的名称 
- `navigationStatus[number]`：枚举：'0=使用发动机行驶，1=锚泊，2=不受控制，3=机动性受限，4=受制于其吃水，5=系泊，6=搁浅，7=从事捕鱼，8=使用帆行驶，9=为未来修订航行状态保留，10=为未来修订航行状态保留，11=为未来使用保留，12=为未来使用保留，13=为未来使用保留，14=AIS-SART处于活动状态，15=未定义（默认）'。导航状态。AIVDM/AIVDO数据格式。模型：[https://schema.org/Number](https://schema.org/Number) 
- `nextPortCode[string]`：下一个港口，编码。代表港口的代码，即到达港口之前的港口，如果有的话。与IALA_S211：nestPortCallCod / IMO相关。[EMSWe：DE-005-07] [EDIFACT：LOC-3227-61] [IMO：IMO0120]。模型：[https://schema.org/Text](https://schema.org/Text) 
- `observedDate[date-time]`：此观察的日期和时间，以ISO 8601 UTC格式表示。模型：[https://schema.org/Text](https://schema.org/Text) 
- `owner[array]`：包含JSON编码序列的列表，引用所有者（s）的唯一ID 
- `portCallNumber[string]`：港口呼叫标识符，以MRN格式表示。第一个元素应该是港口的5个字符UN/LOCODE，后面是年份，最后是港口内的唯一顺序号[LLLLLYYYY99999]，其中LLLLL是访问港口的UN/LOCODE，YYYY是年份，99999是港口当局在每年内分配的唯一顺序号（例如ES HUV202310323）。可以使用UN/LOCODE的缩写（例如H202310323）。在访问的初始步骤中分配港口呼叫号码，但可能在开始时为空。在国际标准中，也称为[Port Call ID]，[Visit ID]或[Port Call Coded]。请参阅[Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) [EMSWe：DG-004/DG-004-01] [EDIFACT：BGM-1004] [IALA_S211：portCallId] [IMO：IMO108+IMO0153]。模型：[https://schema.org/Text](https://schema.org/Text) 
- `portCallRef[uri]`：引用父级PortCall实体。[NGSI-MarineTransport.PortCall.id] 
- `portCode[string]`：贸易和运输位置的联合国代码。请参阅[Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) [EMSWe：DE-004-04] [EDIFACT：LOC-3227-153] [IALA_S211：portCode] [IMO：IMO0108]。模型：[https://schema.org/Text](https://schema.org/Text) 
- `positionAccuracy[number]`：枚举：'0=低（> 10米；例如全球导航卫星系统（GNSS）接收器或其他电子定位设备的自主模式；默认），1=高（< 10米；例如DGNSS接收器的差分模式）'。船舶位置准确性代码的标志。模型：[https://schema.org/Number](https://schema.org/Number) 
- `seeAlso[*]`：指向项目的其他资源的URI列表 
- `source[string]`：一串字符，给出实体数据的原始来源作为URL。建议为提供者的全限定域名，或源对象的URL 
- `speedOverGround[number]`：地面速度（SOG）。模型：[https://schema.org/Number](https://schema.org/Number) 
- `type[string]`：NGSI实体类型。必须是KeyVessel 
- `vesselAtPort[boolean]`：船舶在港口范围内，包括在港口入口外等待、等待指令等。模型：[https://schema.org/Boolean](https://schema.org/Boolean) 
- `vesselName[string]`：船舶名称。模型：[https://schema.org/Text](https://schema.org/Text) 
- `vesselRef[uri]`：引用父级MasterVessel实体。[NGSI-MarineTransport.MasterVessel.id]- urn：mrn：<oid>：portcalls：mastervessel：id：9999 
<!-- /30-PropertiesList --> 
 
<!-- 35-RequiredProperties --> 
 
 
必需属性 
- `id` 
- `type` 
<!-- /35-RequiredProperties --> 
 
<!-- 40-NotesYaml --> 
 
<!-- /40-NotesYaml --> 
 
<!-- 50-DataModelHeader --> 
 
 
## 数据模型属性描述 
 
按字母顺序排序（点击查看详细信息） 
<!-- /50-DataModelHeader --> 
 
<!-- 60-ModelYaml --> 
 
<details><summary><strong>完整的YAML详细信息</strong></summary> 
 
 
```yaml  
KeyVessel:    
  description: 'The data model is intended to provide information about key vessels that a port community must focus his work on next days. It allows to represent the properties of each vessel: static and dynamic information'    
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
    callSign:    
      description: Maritime call signs are call signs assigned as unique identifiers to vessels    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    courseOverGround:    
      description: Course Over Ground (COG)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: degree    
    createdDate:    
      description: Date and time of creation of the entity represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      enum:    
        - AIS    
        - AISHUB    
        - ALGORITHM    
        - IA    
        - MARINETRAFFIC    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    deletedDate:    
      description: Date and time of deletion of the entity represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    etaAis:    
      description: Estimated time of arrival, as it is reported by AIS system, represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    etaAlgorithm:    
      description: Estimated time of arrival, computed by an algorithm based on vessel's positions, represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    flagCode:    
      description: Maritime call signs are call signs assigned as unique identifiers to vessels    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    imo:    
      description: International Maritime Organization Number (a global forever UID)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    lastPortCode:    
      description: 'Last port of call, coded.The code representing the port immediately previous to the port of arrival, if available. [EMSWe: DE-005-05] [EDIFACT:LOC-3227-92] [IMO:IMO0076] '    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    latitude:    
      description: Latitude coordinate of the vessel    
      type: number    
      x-ngsi:    
        type: Property    
    location:    
      '@id': http://uri.etsi.org/ngsi-ld/location    
      '@type': https://uri.etsi.org/ngsi-ld/GeoProperty    
      description: Geojson reference to the vessel position. It must be a Point where the vessel was placed at observedDate date    
      x-ngsi:    
        type: GeoProperty    
    longitude:    
      description: Longitude coordinate of the vessel    
      type: number    
      x-ngsi:    
        type: Property    
    mmsi:    
      description: Marine Mobile Service Identity Number (a temporarily assigned UID, issued by that object's current flag state)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    modifiedDate:    
      description: Date and time of last modification of the entity represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    navigationStatus:    
      description: Enum:'0=Under way using engine, 1=At anchor, 2=Not under command, 3=Restricted manoeuverability,4=Constrained by her draught, 5=Moored, 6=Aground, 7=Engaged in Fishing, 8=Under way sailing, 9=Reserved for future amendment of Navigational state for HSC, 10=Reserved for future amendment of Navigational Status for WIG, 11=Reserved for future use, 12=Reserved for future use,13=Reserved for future use, 14=AIS-SART is active, 15=Not defined (default)'. Navigation Status. AIVDM/AIVDO data format'    
      enum:    
        - 0    
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
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    nextPortCode:    
      description: 'Next port of call, coded.The code representing the port immediately previous to the port of arrival, if available.. Related to IALA_S211:nestPortCallCod / IMO. [EMSWe: DE-005-07] [EDIFACT:LOC-3227-61] [IMO:IMO0120]'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    observedDate:    
      description: Date and time of this observation represented by an ISO 8601 UTC format    
      format: date-time    
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
          type: Relationship    
      type: array    
      x-ngsi:    
        type: Property    
    portCallNumber:    
      description: 'Port call identifier in MRN format. First element of the NSS should be the 5 character UN/Locode of the port, later the YEAR and finishing with a sequential number in this port [LLLLLYYYY99999] where LLLLL is the UN/LOCODE of the visited port, YYYY is the year, and 99999 is a unique sequential number assigned by port authority unique on each year (i.e. ESHUV202310323). An abbreviation can be used for UN/LOCODE (i.e. H202310323). The portCallNumber is assigned during the initial steps of the visit, but could be null at the beginning. In international standards is also known as [Port Call ID], [Visit ID] or [Port Call Coded]. See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) [EMSWe: DG-004/DG-004-01] [EDIFACT:BGM-1004] [IALA_S211:portCallId] [IMO:IMO108+IMO0153]'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    portCallRef:    
      description: Reference to parent PortCall entity. [NGSI-MarineTransport.PortCall.id]    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    portCode:    
      description: 'United Nations Code for Trade and Transport Locations. See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) [EMSWe: DE-004-04] [EDIFACT:LOC-3227-153] [IALA_S211:portCode] [IMO:IMO0108] '    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    positionAccuracy:    
      description: Enum:'0=Low (> 10 m; autonomous mode of e.g.global navigation satellite system (GNSS) receiver or of other electronic position fixing device; default), 1=High (< 10 m; differential mode of e.g.DGNSS receiver)'. Code for the accuracy of the vessel position flag    
      enum:    
        - 0    
        - 1    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    speedOverGround:    
      description: Speed Over Ground (SOG)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meters per second    
    type:    
      description: NGSI Entity type. It has to be KeyVessel    
      enum:    
        - KeyVessel    
      type: string    
      x-ngsi:    
        type: Property    
    vesselAtPort:    
      description: The vessel is in port limits, including waiting outside, at the harbor entrance, awaiting instructions, etc    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    vesselName:    
      description: Vessel Name    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vesselRef:    
      description: Reference to parent MasterVessel entity. [NGSI-MarineTransport.MasterVessel.id]- urn:mrn:<oid>:portcalls:mastervessel:id:9999    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/KeyVessel/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/VesselAtPort/schema.json    
  x-model-tags: I4Trust    
  x-version: 0.0.1    
``` 
</details> 
 
<!-- /60-ModelYaml --> 
 
<!-- 70-MiddleNotes --> 
 
<!-- /70-MiddleNotes --> 
 
<!-- 80-Examples --> 
 
 
## 示例有效载荷 
     
#### KeyVessel NGSI-v2 键值示例 
     
这是一个KeyVessel在JSON格式中的示例，作为键值。它与NGSI-v2兼容，当使用`options=keyValues`并返回个别实体的上下文数据时。 
<details><summary><strong>显示/隐藏示例</strong></summary> 
 
 
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:portcallvessel:id:1234",  
  "type": "KeyVessel",  
  "vesselRef": "urn:mrn:eshuv:portcalls:mastervessel:imo:9863637",  
  "imo": 9863637,  
  "mmsi": 210049000,  
  "callSign": "5BPC3",  
  "flagCode": "ES",  
  "vesselName": "ELEANOR R.",  
  "portCode":   "ESHUV",  
  "lastPortCode": "ESPMI",  
  "nextPortCode": "ESVLC",  
  "portCallNumber": "ESHUV202401233",  
  "portCallRef": "urn:mrn:eshuv:portcalls:portcall:code:1233",  
  "dataProvider": "AIS",  
  "latitude": 37.2614,  
  "longitude":  -6.9447,  
  "speedOverGround": 11.3,  
  "courseOverGround": 122,  
  "navigationStatus": 4,  
  "observedDate": "2024-07-01T03:11:32Z",  
  "modifiedDate": "2024-07-01T03:07:12Z",  
  "createdDate": "2023-06-03T07:00:00Z",  
  "deletedDate": "2024-07-01T03:07:12Z"  
}  
``` 
</details> 
 
 
#### KeyVessel NGSI-v2 规范化示例 
     
这是一个KeyVessel在JSON格式中的示例，作为规范化。它与NGSI-v2兼容，当不使用选项并返回个别实体的上下文数据时。 
<details><summary><strong>显示/隐藏示例</strong></summary> 
 
 
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:portcallvessel:id:1234",  
  "type": "KeyVessel",  
  "vesselRef": {  
    "type": "Text",  
    "value": "urn:mrn:eshuv:portcalls:mastervessel:imo:9863637"  
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
    "value": "ES"  
  },  
  "vesselName": {  
    "type": "Text",  
    "value": "ELEANOR R."  
  },  
  "portCode": {  
    "type": "Text",  
    "value": "ESHUV"  
  },  
  "lastPortCode": {  
    "type": "Text",  
    "value": "ESPMI"  
  },  
  "nextPortCode": {  
    "type": "Text",  
    "value": "ESVLC"  
  },  
  "portCallNumber": {  
    "type": "Text",  
    "value": "ESHUV202401233"  
  },  
  "portCallRef": {  
    "type": "Text",  
    "value": "urn:mrn:eshuv:portcalls:portcall:code:1233"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "AIS"  
  },  
  "latitude": {  
    "type": "Number",  
    "value": 37.2614  
  },  
  "longitude": {  
    "type": "Number",  
    "value": -6.9447  
  },  
  "speedOverGround": {  
    "type": "Number",  
    "value": 11.3  
  },  
  "courseOverGround": {  
    "type": "Number",  
    "value": 122  
  },  
  "navigationStatus": {  
    "type": "Number",  
    "value": 4  
  },  
  "observedDate": {  
    "type": "DateTime",  
    "value": "2024-07-01T03:11:32Z"  
  },  
  "modifiedDate": {  
    "type": "DateTime",  
    "value": "2024-07-01T03:07:12Z"  
  },  
  "createdDate": {  
    "type": "DateTime",  
    "value": "2023-06-03T07:00:00Z"  
  },  
  "deletedDate": {  
    "type": "DateTime",  
    "value": "2024-07-01T03:07:12Z"  
  }  
}  
``` 
</details> 
 
 
#### KeyVessel NGSI-LD 键值示例 
     
这是一个KeyVessel在JSON-LD格式中的示例，作为键值。它与NGSI-LD兼容，当使用`options=keyValues`并返回个别实体的上下文数据时。 
<details><summary><strong>显示/隐藏示例</strong></summary> 
 
 
```json  
{  
  "id": "urn:ngsi-ld:KeyVessel:urn:mrn:eshuv:portcalls:portcallvessel:id:1234",  
  "type": "KeyVessel",  
  "vesselRef": "urn:mrn:eshuv:portcalls:mastervessel:imo:9863637",  
  "imo": 9863637,  
  "mmsi": 210049000,  
  "callSign": "5BPC3",  
  "flagCode": "ES",  
  "vesselName": "ELEANOR R.",  
  "portCode": "ESHUV",  
  "lastPortCode": "ESPMI",  
  "nextPortCode": "ESVLC",  
  "portCallNumber": "ESHUV202401233",  
  "portCallRef": "urn:mrn:eshuv:portcalls:portcall:code:1233",  
  "dataProvider": "AIS",  
  "latitude": 37.2614,  
  "longitude": -6.9447,  
  "speedOverGround": 11.3,  
  "courseOverGround": 122,  
  "navigationStatus": 4,  
  "observedDate": "2024-07-01T03:11:32Z",  
  "modifiedDate": "2024-07-01T03:07:12Z",  
  "createdDate": "2023-06-03T07:00:00Z",  
  "deletedDate": "2024-07-01T03:07:12Z",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
``` 
</details> 
 
 
#### KeyVessel NGSI-LD 规范化示例 
     
这是一个KeyVessel在JSON-LD格式中的示例，作为规范化。它与NGSI-LD兼容，当不使用选项并返回个别实体的上下文数据时。 
<details><summary><strong>显示/隐藏示例</strong></summary> 
 
 
```json  
{  
  "id": "urn:ngsi-ld:KeyVessel:urn:mrn:eshuv:portcalls:portcallvessel:id:1234",  
  "type": "KeyVessel",  
  "vesselRef": {  
    "type": "Property",  
    "value": "urn:mrn:eshuv:portcalls:mastervessel:imo:9863637"  
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
    "value": "ES"  
  },  
  "vesselName": {  
    "type": "Property",  
    "value": "ELEANOR R."  
  },  
  "portCode": {  
    "type": "Property",  
    "value": "ESHUV"  
  },  
  "lastPortCode": {  
    "type": "Property",  
    "value": "ESPMI"  
  },  
  "nextPortCode": {  
    "type": "Property",  
    "value": "ESVLC"  
  },  
  "portCallNumber": {  
    "type": "Property",  
    "value": "ESHUV202401233"  
  },  
  "portCallRef": {  
    "type": "Property",  
    "value": "urn:mrn:eshuv:portcalls:portcall:code:1233"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "AIS"  
  },  
  "latitude": {  
    "type": "Property",  
    "value": 37.2614  
  },  
  "longitude": {  
    "type": "Property",  
    "value": -6.9447  
  },  
  "speedOverGround": {  
    "type": "Property",  
    "value": 11.3  
  },  
  "courseOverGround": {  
    "type": "Property",  
    "value": 122  
  },  
  "navigationStatus": {  
    "type": "Property",  
    "value": 4  
  },  
  "observedDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-07-01T03:11:32Z"  
    }  
  },  
  "modifiedDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-07-01T03:07:12Z"  
    }  
  },  
  "createdDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2023-06-03T07:00:00Z"  
    }  
  },  
  "deletedDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-07-01T03:07:12Z"  
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
 
 
请参阅[FAQ 10](https://smartdatamodels.org/index.php/faqs/)，了解如何处理数量单位 
<!-- /95-Units --> 
 
<!-- 97-LastFooter --> 
 
--- 
 
 
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter --> 
 
---