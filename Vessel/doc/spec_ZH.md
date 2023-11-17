<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：船只    
=====<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/Vessel/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全局描述：**数据模型旨在提供有关船只的信息。它可以表示每艘船只的属性：静态和动态信息**。    
版本： 0.0.2    
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
	- `streetNr[string]`: 标识公共街道上特定房产的编号      
- `airDraught[number]`: 空气吃水（船只最高点到水线的距离）  . Model: [http://schema.org/Number](http://schema.org/Number)- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `beam[number]`: 船宽  . Model: [https://schema.org/Number](https://schema.org/Number)- `buildingAt[date-time]`: 以 ISO 8601 UTC 格式表示的船舶建造日期和时间  . Model: [https://schema.org/Text](https://schema.org/Text)- `callSign[string]`: 海事呼号是指分配给船只作为唯一标识的呼号  . Model: [https://schema.org/Text](https://schema.org/Text)- `courseOverGround[number]`: 地面航线（COG）  . Model: [https://schema.org/Number](https://schema.org/Number)- `createdAt[date-time]`: 以 ISO 8601 UTC 格式表示的实体创建日期和时间  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  . Model: [https://schema.org/Text](https://schema.org/Text)- `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `deadweightTonnage[number]`: 载重吨（DWT）  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: 项目描述  - `destinationPort[string]`: 目的港（地理编码方案 UN/LOCODE（联合国贸易和运输地点代码）。https://unece.org/trade/publications/recommendation-ndeg16-united-nations-code-trade-and-transport-locations)  . Model: [https://schema.org/Text](https://schema.org/Text)- `draught[number]`: 吃水（水线与船体底部（龙骨）之间的垂直距离）  . Model: [http://schema.org/Number](http://schema.org/Number)- `estimatedTimeOfArrival[date-time]`: 托运人最初计划和输入的预计到达时间，以 ISO 8601 UTC 格式表示  . Model: [https://schema.org/Text](https://schema.org/Text)- `financialOwner[string]`: 财务负责人  . Model: [https://schema.org/Text](https://schema.org/Text)- `flagCode[string]`: 国际旗帜代码（ISO 3166-1 alfa-2）  . Model: [https://schema.org/Text](https://schema.org/Text)- `grossTonnage[number]`: 总吨位（GT）  . Model: [https://schema.org/Number](https://schema.org/Number)- `heading[number]`: 船舶航向 (HDG)  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[string]`: 实体的唯一标识符  - `imo[number]`: 国际海事组织编号（全球永久 UID）  . Model: [https://schema.org/Number](https://schema.org/Number)- `length[number]`: 船只长度  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[object]`: 项目的 Geojson 引用。可以是点、线条字符串、多边形、多点、多线条字符串或多多边形属性  	- `coordinates`:       
	- `type`:       
- `manager[string]`: 管理船只  . Model: [https://schema.org/Text](https://schema.org/Text)- `maximumDraught[number]`: 最大吃水  . Model: [https://schema.org/Number](https://schema.org/Number)- `mmsi[number]`: 海事移动服务身份号（临时分配的 UID，由该对象的当前船旗国颁发）  . Model: [https://schema.org/Number](https://schema.org/Number)- `modifiedAt[date-time]`: 以 ISO 8601 UTC 格式表示的实体最后一次修改的日期和时间  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: 船只名称  . Model: [https://schema.org/Text](https://schema.org/Text)- `navigationStatus[number]`: 枚举：0=使用发动机航行中,1=抛锚,2=未受指挥,3=操纵能力受限,4=受吃水限制,5=停泊,6=搁浅,7=从事捕鱼,8=航行中,9=保留用于将来修改 HSC 的航行状态、10=为将来修改 WIG 的航行状态而保留，11=为将来使用而保留，12=为将来使用而保留，13=为将来使用而保留，14=AIS-SART 已激活，15=未定义（默认）'。导航状态。AIVDM/AIVDO 数据格式  . Model: [http://schema.org/Number](http://schema.org/Number)- `observedAt[date-time]`: 以 ISO 8601 UTC 格式表示的观测日期和时间  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `ownerVessel[string]`: 船主船只  . Model: [https://schema.org/Text](https://schema.org/Text)- `photo[string]`: 船只照片 URL  . Model: [https://schema.org/Text](https://schema.org/Text)- `positionAccuracy[number]`: 全球导航卫星系统（GNSS）接收器或其他电子定位装置；默认值），1=高（< 10 米；例如 DGNSS 接收器的差分模式）'。船位旗精度代码  . Model: [https://schema.org/Number.Enum: 0=Low (> 10 m; autonomous mode of e.g](https://schema.org/Number.Enum: 0=Low (> 10 m; autonomous mode of e.g)- `previousPort[string]`: 上一个港口（地理编码方案 UN/LOCODE（联合国贸易和运输地点代码）。https://unece.org/trade/publications/recommendation-ndeg16-united-nations-code-trade-and-transport-locations)  . Model: [https://schema.org/Text](https://schema.org/Text)- `rateOfTurn[number]`: 转动速率 (ROT)  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `specialManeuverIndicator[number]`: 枚举："0=不可用（默认），1=未参与特殊演习，2=参与特殊演习"。特殊演习标志代码  . Model: [https://schema.org/Number](https://schema.org/Number)- `speedOverGround[number]`: 地面速度（SOG）  . Model: [https://schema.org/Number](https://schema.org/Number)- `technicalManager[string]`: 技术经理  . Model: [https://schema.org/Text](https://schema.org/Text)- `toBow[number]`: 弓形尺寸  . Model: [http://schema.org/Number](http://schema.org/Number)- `toPort[number]`: 端口尺寸  . Model: [http://schema.org/Number](http://schema.org/Number)- `toStardboard[number]`: 右舷尺寸  . Model: [http://schema.org/Number](http://schema.org/Number)- `toStern[number]`: 船尾尺寸  . Model: [http://schema.org/Number](http://schema.org/Number)- `type[string]`: NGSI 实体类型。必须是船只  - `vesselSubType[number]`: 枚举：0=不可用（默认值）,1-19=保留供将来使用,20=地面机翼（WIG），所有此类舰船,21=地面机翼（WIG），危险类别 A,22=地面机翼（WIG），危险类别 B,23=地面机翼（WIG），危险类别 C,24=地面机翼（WIG），危险类别 D,25-29=地面机翼（WIG）、危险类别 B,23=Wing in ground (WIG)，危险类别 C,24=Wing in ground (WIG)，危险类别 D,25-29=Wing in ground (WIG)，保留给将来使用,30=Fishing,31=Towing,32=Towing：长度超过 200 米或宽度超过 25 米,33=挖泥或水下作业,34=潜水作业,35=军事作业,36=航行,37=游艇,38-39=保留,40=高速船（HSC），所有此类船只,41=高速船（HSC），危险类别 A,42=高速船（HSC），危险类别 B,43=高速船（HSC），危险类别 C、44=高速船（HSC），危险类别 D,45-48=高速船（HSC），保留供将来使用,49=高速船（HSC），无其他信息,50=引航船,51=搜索和救援船,52=拖船,53=港口补给船,54=防污染设备,55=执法船,56-57=备用-本地船,58=医疗运输船,59=根据 RR Resolution No.18,60=乘客，所有此类船舶,61=乘客，危险类别 A,62=乘客，危险类别 B,63=乘客，危险类别 C,64=乘客，危险类别 D,65-68=乘客，保留供将来使用,69=乘客，无其他信息、70=货物，所有此类船舶,71=货物，危险类别 A,72=货物，危险类别 B,73=货物，危险类别 C,74=货物，危险类别 D,75-78=货物，留待将来使用,79=货物，无附加信息,80=油轮、所有此类船舶,81=油轮，危险类别 A,82=油轮，危险类别 B,83=油轮，危险类别 C,84=油轮，危险类别 D,85-88=油轮，保留将来使用,89=油轮，无其他信息,90=其他类型、所有此类船舶,91=其他类型，危险类别 A,92=其他类型，危险类别 B,93=其他类型，危险类别 C,94=其他类型，危险类别 D,95-98=其他类型，保留将来使用,99=其他类型，无其他信息'。容器子类型代码  . Model: [https://schema.org/Number](https://schema.org/Number)- `vesselType[number]`: 枚举：'1=保留，2=机翼着地，3=特殊类别，4=高速船，5=特殊类别，6=客运，7=货运，8=油轮，9=其他'。船舶类型代码  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
所需属性    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 属性的数据模型描述    
按字母顺序排列（点击查看详情）    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
Vessel:      
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
    airDraught:      
      description: Air Draught (distance from the top of a vessel''s highest point to its waterline)      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
        units: ' meters'      
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
      description: Beam of Vessel      
      maximum: 1000      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: ' meters'      
    buildingAt:      
      description: Date and time of building of the vessel represented by an ISO 8601 UTC format      
      format: date-time      
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
        units: ' degree'      
    createdAt:      
      description: Date and time of creation of the entity represented by an ISO 8601 UTC format      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
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
    deadweightTonnage:      
      description: Deadweight Tonnage (DWT)      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: ' tons'      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    destinationPort:      
      description: 'Destination Port (Geographic coding scheme UN/LOCODE (United Nations Code for Trade and Transport Locations). https://unece.org/trade/publications/recommendation-ndeg16-united-nations-code-trade-and-transport-locations)'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    draught:      
      description: Draught (vertical distance between the waterline and the bottom of the hull (keel))      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
        units: ' meters'      
    estimatedTimeOfArrival:      
      description: 'Estimated time of arrival, as it was originally planned and entered by the shipper, represented by an ISO 8601 UTC format'      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    financialOwner:      
      description: Financial Owner      
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
    grossTonnage:      
      description: Gross Tonnage (GT)      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: ' moorson tons'      
    heading:      
      description: Heading of the Vessel (HDG)      
      maximum: 511      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: ' degree'      
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
    imo:      
      description: International Maritime Organization Number (a global forever UID)      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    length:      
      description: Length of Vessel      
      maximum: 8000      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: ' meters'      
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
      description: Manager Vessel      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    maximumDraught:      
      description: Maximum Draught      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: ' meters'      
    mmsi:      
      description: 'Marine Mobile Service Identity Number (a temporarily assigned UID, issued by that object''s current flag state)'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    modifiedAt:      
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
      description: 'Enum: ''0=Under way using engine,1=At anchor,2=Not under command,3=Restricted manoeuverability,4=Constrained by her draught,5=Moored,6=Aground,7=Engaged in Fishing,8=Under way sailing,9=Reserved for future amendment of Navigational Status for HSC,10=Reserved for future amendment of Navigational Status for WIG,11=Reserved for future use,12=Reserved for future use,13=Reserved for future use,14=AIS-SART is active,15=Not defined (default)''. Navigation Status. AIVDM/AIVDO data format'      
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
        model: http://schema.org/Number      
        type: Property      
    observedAt:      
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
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    ownerVessel:      
      description: Owner Vessel      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    photo:      
      description: Vessel Photo URL      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    positionAccuracy:      
      description: 'global navigation satellite system (GNSS) receiver or of other electronic position fixing device; default),1=High (< 10 m; differential mode of e.g. DGNSS receiver)''. Code for the accuracy of the vessel position flag'      
      enum:      
        - 0      
        - 1      
      type: number      
      x-ngsi:      
        model: 'https://schema.org/Number.Enum: 0=Low (> 10 m; autonomous mode of e.g'      
        type: Property      
    previousPort:      
      description: 'Previous Port (Geographic coding scheme UN/LOCODE (United Nations Code for Trade and Transport Locations). https://unece.org/trade/publications/recommendation-ndeg16-united-nations-code-trade-and-transport-locations)'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    rateOfTurn:      
      description: Rate of Turn (ROT)      
      maximum: 708      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: ' degree'      
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
    specialManeuverIndicator:      
      description: 'Enum: ''0=Not available (default),1=Not engaged in special maneuver,2=Engaged in special maneuver''. Code for the special maneuver flag'      
      enum:      
        - 0      
        - 1      
        - 2      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    speedOverGround:      
      description: Speed Over Ground (SOG)      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: ' meters per second'      
    technicalManager:      
      description: Technical Manager      
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
        units: ' meters'      
    toPort:      
      description: Dimension to Port      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
        units: ' meters'      
    toStardboard:      
      description: Dimension to Starboard      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
        units: ' meters'      
    toStern:      
      description: Dimension to Stern      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
        units: ' meters'      
    type:      
      description: NGSI Entity type. It has to be Vessel      
      enum:      
        - Vessel      
      type: string      
      x-ngsi:      
        type: Property      
    vesselSubType:      
      description: 'Enum: ''0=Not available (default),1-19=Reserved for future use,20=Wing in ground (WIG), all ships of this type,21=Wing in ground (WIG), Hazardous category A,22=Wing in ground (WIG), Hazardous category B,23=Wing in ground (WIG), Hazardous category C,24=Wing in ground (WIG), Hazardous category D,25-29=Wing in ground (WIG), Reserved for future use,30=Fishing,31=Towing,32=Towing: length exceeds 200m or breadth exceeds 25m,33=Dredging or underwater ops,34=Diving ops,35=Military ops,36=Sailing,37=Pleasure Craft,38-39=Reserved,40=High speed craft (HSC), all ships of this type,41=High speed craft (HSC), Hazardous category A,42=High speed craft (HSC), Hazardous category B,43=High speed craft (HSC), Hazardous category C,44=High speed craft (HSC), Hazardous category D,45-48=High speed craft (HSC), Reserved for future use,49=High speed craft (HSC), No additional information,50=Pilot Vessel,51=Search and Rescue vessel,52=Tug,53=Port Tender,54=Anti-pollution equipment,55=Law Enforcement,56-57=Spare - Local Vessel,58=Medical Transport,59=Noncombatant ship according to RR Resolution No. 18,60=Passenger, all ships of this type,61=Passenger, Hazardous category A,62=Passenger, Hazardous category B,63=Passenger, Hazardous category C,64=Passenger, Hazardous category D,65-68=Passenger, Reserved for future use,69=Passenger, No additional information,70=Cargo, all ships of this type,71=Cargo, Hazardous category A,72=Cargo, Hazardous category B,73=Cargo, Hazardous category C,74=Cargo, Hazardous category D,75-78=Cargo, Reserved for future use,79=Cargo, No additional information,80=Tanker, all ships of this type,81=Tanker, Hazardous category A,82=Tanker, Hazardous category B,83=Tanker, Hazardous category C,84=Tanker, Hazardous category D,85-88=Tanker, Reserved for future use,89=Tanker, No additional information,90=Other Type, all ships of this type,91=Other Type, Hazardous category A,92=Other Type, Hazardous category B,93=Other Type, Hazardous category C,94=Other Type, Hazardous category D,95-98=Other Type, Reserved for future use,99=Other Type, no additional information''. Code for vessel Sub-Type'      
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
      description: 'Enum: ''1=Reserved,2=Wing In Ground,3=Special Category,4=High-Speed Craft,5=Special Category,6=Passenger,7=Cargo,8=Tanker,9=Other''. Code for vessel type'      
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/Vessel/LICENSE.md      
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/Vessel/schema.json      
  x-model-tags: I4Trust      
  x-version: 0.1.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 有效载荷示例    
#### 船只 NGSI-v2 键值示例    
下面是一个以 JSON-LD 格式作为键值的船只示例。当使用 `options=keyValues` 时，这与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:mrn:amura:vessel:test",  
  "type": "Vessel",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -5.993307,  
      37.362882  
    ]  
  },  
  "imo": 9863637,  
  "mmsi": 210049000,  
  "callSign": "5BPC5",  
  "name": "ELEANOR ROOSEVELT",  
  "speedOverGround": 1,  
  "courseOverGround": 1,  
  "heading": 1,  
  "rateOfTurn": 1,  
  "createdAt": "2022-06-01T07:00:00.00Z",  
  "modifiedAt": "2022-06-01T07:00:00.00Z",  
  "observedAt": "2022-06-01T07:00:00.00Z",  
  "flagCode": "CY",  
  "vesselType": 1,  
  "vesselSubType": 2,  
  "grossTonnage": 12467,  
  "beam": 7,  
  "length": 32,  
  "maximumDraught": 5,  
  "deadweightTonnage": 8,  
  "buildingAt": "2021-01-01T07:00:00.00Z",  
  "toBow": 3,  
  "toStern": 20,  
  "toPort": 17,  
  "toStardboard": 4,  
  "navigationStatus": 4,  
  "airDraught": 4,  
  "draught": 4,  
  "photo": "PHOTO URL",  
  "ownerVessel": "OWNER NAME",  
  "manager": "MANAGER NAME",  
  "financialOwner": "FINANCIAL OWNER NAME",  
  "technicalManager": "TECHNICAL MANAGER NAME",  
  "dataProvider": "AIS",  
  "destinationPort": "ESVLC",  
  "previousPort": "ESPMI",  
  "estimatedTimeOfArrival": "2023-03-01T07:00:00.00Z",  
  "calculatedTimeOfArrival": "2023-03-02T07:00:00.00Z",  
  "positionAccuracy": 0,  
  "specialManeuverIndicator": 1  
}  
```  
</details>    
#### 船舶 NGSI-v2 标准化示例    
下面是一个以 JSON-LD 格式规范化的船只示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:mrn:amura:vessel:test",  
  "type": "Vessel",  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -5.993307,  
        37.362882  
      ]  
    }  
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
    "value": "5BPC5"  
  },  
  "name": {  
    "type": "Text",  
    "value": "ELEANOR ROOSEVELT"  
  },  
  "speedOverGround": {  
    "type": "Boolean",  
    "value": true  
  },  
  "courseOverGround": {  
    "type": "Boolean",  
    "value": true  
  },  
  "heading": {  
    "type": "Boolean",  
    "value": true  
  },  
  "rateOfTurn": {  
    "type": "Boolean",  
    "value": true  
  },  
  "createdAt": {  
    "type": "DateTime",  
    "value": "2022-06-01T07:00:00.00Z"  
  },  
  "modifiedAt": {  
    "type": "DateTime",  
    "value": "2022-06-01T07:00:00.00Z"  
  },  
  "observedAt": {  
    "type": "DateTime",  
    "value": "2022-06-01T07:00:00.00Z"  
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
  "grossTonnage": {  
    "type": "Number",  
    "value": 12467  
  },  
  "beam": {  
    "type": "Number",  
    "value": 7  
  },  
  "length": {  
    "type": "Number",  
    "value": 32  
  },  
  "maximumDraught": {  
    "type": "Number",  
    "value": 5  
  },  
  "deadweightTonnage": {  
    "type": "Number",  
    "value": 8  
  },  
  "buildingAt": {  
    "type": "DateTime",  
    "value": "2021-01-01T07:00:00.00Z1"  
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
  "navigationStatus": {  
    "type": "Number",  
    "value": 4  
  },  
  "airDraught": {  
    "type": "Number",  
    "value": 4  
  },  
  "draught": {  
    "type": "Number",  
    "value": 4  
  },  
  "photo": {  
    "type": "Text",  
    "value": "URL PHOTO"  
  },  
  "ownerVessel": {  
    "type": "Text",  
    "value": "OWNER NAME"  
  },  
  "manager": {  
    "type": "Text",  
    "value": "MANAGER NAME"  
  },  
  "financialOwner": {  
    "type": "Text",  
    "value": "FINANCIAL OWNER NAME"  
  },  
  "technicalManager": {  
    "type": "Text",  
    "value": "TECHNICAL MANAGER NAME"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "AIS"  
  },  
  "destinationPort": {  
    "type": "Text",  
    "value": "ESVLC"  
  },  
  "previousPort": {  
    "type": "Text",  
    "value": "ESPMI"  
  },  
  "estimatedTimeOfArrival": {  
    "type": "DateTime",  
    "value": "2023-03-01T07:00:00.00Z"  
  },  
  "positionAccuracy": {  
    "type": "Boolean",  
    "value": false  
  },  
  "specialManeuverIndicator": {  
    "type": "Boolean",  
    "value": true  
  }  
}  
```  
</details>    
#### 船只 NGSI-LD 键值示例    
下面是一个以 JSON-LD 格式作为键值的船只示例。当使用 `options=keyValues` 时，这与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:mrn:amura:vessel:test",  
  "type": "Vessel",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -5.993307,  
      37.362882  
    ]  
  },  
  "imo": 9863637,  
  "mmsi": 210049000,  
  "callSign": "5BPC5",  
  "name": "ELEANOR ROOSEVELT",  
  "speedOverGround": 1,  
  "courseOverGround": 1,  
  "heading": 1,  
  "rateOfTurn": 1,  
  "createdAt": "2022-06-01T07:00:00.00Z",  
  "modifiedAt": "2022-06-01T07:00:00.00Z",  
  "observedAt": "2022-06-01T07:00:00.00Z",  
  "flagCode": "CY",  
  "vesselType": 1,  
  "vesselSubType": 2,  
  "grossTonnage": 12467,  
  "beam": 7,  
  "length": 32,  
  "maximumDraught": 5,  
  "deadweightTonnage": 8,  
  "buildingAt": "2021-01-01T07:00:00.00Z",  
  "toBow": 3,  
  "toStern": 20,  
  "toPort": 17,  
  "toStardboard": 4,  
  "navigationStatus": 4,  
  "airDraught": 4,  
  "draught": 4,  
  "photo": "PHOTO URL",  
  "ownerVessel": "OWNER NAME",  
  "manager": "MANAGER NAME",  
  "financialOwner": "FINANCIAL OWNER NAME",  
  "technicalManager": "TECHNICAL MANAGER NAME",  
  "dataProvider": "AIS",  
  "destinationPort": "ESVLC",  
  "previousPort": "ESPMI",  
  "estimatedTimeOfArrival": "2023-03-01T07:00:00.00Z",  
  "positionAccuracy": 0,  
  "specialManeuverIndicator": 1,  
  "@context": [  
    "https://gitlab.com/hiades/fiware/smart-data-models/-/raw/main/context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### 船舶 NGSI-LD 归一化示例    
下面是一个以 JSON-LD 格式规范化的船只示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:mrn:amura:vessel:test",  
    "type": "Vessel",  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -5.993307,  
                37.362882  
            ]  
        }  
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
        "value": "5BPC5"  
    },  
    "name": {  
        "type": "Property",  
        "value": "ELEANOR ROOSEVELT"  
    },  
    "speedOverGround": {  
        "type": "Property",  
        "value": 1  
    },  
    "courseOverGround": {  
        "type": "Property",  
        "value": 1  
    },  
    "heading": {  
        "type": "Property",  
        "value": 1  
    },  
    "rateOfTurn": {  
        "type": "Property",  
        "value": 1  
    },  
    "createdAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2022-06-01T07:00:00.00Z"  
        }  
    },  
    "modifiedAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2022-06-01T07:00:00.00Z"  
        }  
    },  
    "observedAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2022-06-01T07:00:00.00Z"  
        }  
    },  
    "flagCode": {  
        "type": "Property",  
        "value": "CY"  
    },  
    "vesselType": {  
        "type": "Property",  
        "value": 1  
    },  
    "vesselSubType": {  
        "type": "Property",  
        "value": 2  
    },  
    "grossTonnage": {  
        "type": "Property",  
        "value": 12467  
    },  
    "beam": {  
        "type": "Property",  
        "value": 7  
    },  
    "length": {  
        "type": "Property",  
        "value": 32  
    },  
    "maximumDraught": {  
        "type": "Property",  
        "value": 5  
    },  
    "deadweightTonnage": {  
        "type": "Property",  
        "value": 8  
    },  
    "buildingAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-01-01T07:00:00.00Z1"  
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
    "navigationStatus": {  
        "type": "Property",  
        "value": 4  
    },  
    "airDraught": {  
        "type": "Property",  
        "value": 4  
    },  
    "draught": {  
        "type": "Property",  
        "value": 4  
    },  
    "photo": {  
        "type": "Property",  
        "value": "URL PHOTO"  
    },  
    "ownerVessel": {  
        "type": "Property",  
        "value": "OWNER NAME"  
    },  
    "manager": {  
        "type": "Property",  
        "value": "MANAGER NAME"  
    },  
    "financialOwner": {  
        "type": "Property",  
        "value": "FINANCIAL OWNER NAME"  
    },  
    "technicalManager": {  
        "type": "Property",  
        "value": "TECHNICAL MANAGER NAME"  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "AIS"  
    },  
    "destinationPort": {  
        "type": "Property",  
        "value": "ESVLC"  
    },  
    "previousPort": {  
        "type": "Property",  
        "value": "ESPMI"  
    },  
    "estimatedTimeOfArrival": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2023-03-01T07:00:00.00Z"  
        }  
    },  
    "positionAccuracy": {  
        "type": "Property",  
        "value": 0  
    },  
    "specialManeuverIndicator": {  
        "type": "Property",  
        "value": 1  
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
