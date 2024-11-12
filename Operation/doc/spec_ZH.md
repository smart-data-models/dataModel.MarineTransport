<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：行动  
=====<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/Operation/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**本数据模型旨在提供船舶停靠港口（泊位实体）期间的商业运营信息。操作（Operation）被定义为停泊期间发生的与商业操作有关的活动。每个操作都有一个实体，有些操作可以在同一泊位（停靠或锚地）进行，并通过时间序列号（operationRank）加以区分**。  
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
	- `streetNr[string]`: 标识公共街道上特定房产的编号    
- `alternateName[string]`: 该项目的替代名称  - `amount[number]`: 装载/卸载台数  . Model: [https://schema.org/Number](https://schema.org/Number)- `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `berthRef[uri]`: 引用父级 MarineTransport:Berth 实体  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `etc[date-time]`: 用 ISO 8601 UTC 格式表示，即港务局预计到达泊位的估计时间（ISO 8601 UTC 格式）的日期和时间。如果是第一次靠泊，则 ETA-berth 应与 ETA-PBP 相同。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `ets[date-time]`:   . Model: [https://schema.org/DateTime.Represented by an ISO 8601 UTC format, Date and time of Estimated Time of starting the operation.](https://schema.org/DateTime.Represented by an ISO 8601 UTC format, Date and time of Estimated Time of starting the operation.)- `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `manipulationMeansCode[string]`: 识别操纵手段的代码。枚举：1=船舶自身资源，2=滚上滚下斜坡，3=船坞起重机，4=汽车起重机，5=管道，6=传送带，7=气动泵装置，8=特殊装置，9=其他手段。  . Model: [https://schema.org/Text](https://schema.org/Text)- `manipulationMeansNumber[number]`: 操作手段的数量  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxWeightPerUnit[number]`: 单位装载/卸载最大重量  . Model: [https://schema.org/Number](https://schema.org/Number)- `measureUnit[string]`: 单位负载类型 装载/卸载  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: 该项目的名称  - `operationRank[number]`: 在泊位上进行的所有商业操作（卸货、装货......）中，该操作的等级或编号  . Model: [https://schema.org/Number](https://schema.org/Number)- `operationTypeCode[string]`: 标识商业运营类型的代码。枚举：'ZD=卸载；ZE=登岸；ZT=转运；ZR=废弃物；AV=运输；DT=过境卸载；RE=堆放'。  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `portCallNumber[string]`: 以 urn 格式表示的 PortCall 标识符。MarineTransport:PortCall:portCallNumber  . Model: [https://schema.org/Text](https://schema.org/Text)- `portCallRef[uri]`: 父级 MarineTransport:PortCall 实体的引用  - `portCode[string]`: 停靠港代码  . Model: [https://schema.org/Text](https://schema.org/Text)- `position[string]`: 指定操作发生在港口中的位置的文本  . Model: [https://schema.org/Text](https://schema.org/Text)- `productCode[string]`: 标识此操作的产品类型的代码。枚举：Z01=原油； Z02=燃料油； Z03=天然气； Z04=汽油； Z05=沥青； Z06=其他石油产品； Z07=石油能源气体； Z08=铁矿石； Z09=黄铁矿；Z10=其他矿物； Z11=废铁； Z12=煤炭和石油焦； Z13=钢铁产品； Z14=磷酸盐； Z15=钾盐； Z16=天然和人工肥料；Z17=化学产品； Z18=水泥和熟料； Z19=木材和软木； Z20=建筑材料； Z21=谷物及其面粉； Z22=豆类和豆粉； Z23=水果、蔬菜和豆类； Z24=葡萄酒、酒精饮料及其衍生物； Z25=食盐； Z26=纸张和纸浆； Z27=罐头； Z28=烟草、可可、咖啡和香料；Z29=油脂； Z30=其他食品； Z31=机械、器具、工具及零配件； Z32=汽车及零配件； Z33=冷冻鱼； Z34=其他商品； Z35=天然气； Z36=其他冶金产品； Z37=饲料及饲草； Z38=皮重卡车货台； Z39=集装箱皮重；Z40=过境集装箱内货物； Z41=装满集装箱； Z42=空集装箱； Z43=车辆； Z44=车辆部件； Z91=乘客； Z92=邮轮乘客； 1=鲜鱼； Z51=生物燃料； Z52=其他非金属矿物； ZR1=脏压舱物； ZR2=污泥和沉淀池； ZR3=含油污水池； ZR4=脏水； ZR5=垃圾；  . Model: [https://schema.org/Text](https://schema.org/Text)- `remarks[string]`: 操作说明  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `stevedoreRef[string]`: 装卸工的 ID。格式 urn:mrn:<oid>:portcalls:operation:stevedore:9999  . Model: [https://schema.org/Text](https://schema.org/Text)- `stopRank[number]`: 该停靠站在停靠站（泊位或锚泊区）中的等级或编号，按时间顺序排列  . Model: [https://schema.org/Number](https://schema.org/Number)- `terminal[string]`: 进行操作的终端  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI 实体类型。它必须是 "操作"。在某些国际标准中也被称为[船舶停靠]。  - `year[number]`: 开始停泊的年份  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Operation:    
  description: 'This data model is intended to provide information about commercial operations made in a stop of a ship during a PortCall (Berth entity). An Operation is defined as the activities related to commercial operations that take in place during the berth. Each Operation has an entity and some operations can be made in the same berth (docked or anchorage), and are distinguished by its sequence number on time (operationRank)'    
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
    amount:    
      description: Number of units loading/discharge    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    berthRef:    
      description: 'Reference to parent MarineTransport:Berth entity'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
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
    etc:    
      description: 'Represented by an ISO 8601 UTC format, Date and time of Estimated Time of Arrival to Berth expected by Port Authority  (ISO 8601 UTC format). If this is the first berthing, the ETA-berth should be the same than ETA-PBP'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    ets:    
      description: ""    
      format: date-time    
      type: string    
      x-ngsi:    
        model: 'https://schema.org/DateTime.Represented by an ISO 8601 UTC format, Date and time of Estimated Time of starting the operation.'    
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
    manipulationMeansCode:    
      description: 'Code identifying the manipulation means. Enum: 1=Vessel''s own resources, 2=Roll-on-roll-off ramp, 3=Dock cranes, 4=Automotive cranes, 5=Pipes, 6=Conveyor belts, 7=Pneumatic pumping installations, 8=Special installations, 9=Other means'''    
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
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    manipulationMeansNumber:    
      description: Number of manipulation means    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maxWeightPerUnit:    
      description: Maximum Weight per unit loading/discharge    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Tm    
    measureUnit:    
      description: Unit type of load loading/discharge    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    operationRank:    
      description: 'Rank or Number of this Operation in all the commercial operations made in berth in the sequence of operations (discharge, charge, ...)'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    operationTypeCode:    
      description: 'Code identifying the type of commercial operation. Enum: ''ZD=Disembarkation; ZE=Embarkation; ZT=Transshipment; ZR=Waste; AV=Victualling; DT=Disembarkation in transit; RE=Restow'''    
      enum:    
        - AV    
        - DT    
        - RE    
        - ZD    
        - ZE    
        - ZR    
        - ZT    
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
      description: 'PortCall identifier in urn format. MarineTransport:PortCall:portCallNumber'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    portCallRef:    
      description: 'Reference to parent MarineTransport:PortCall entity'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    portCode:    
      description: Code of the port of the call    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    position:    
      description: Text specifying the position in the port where the operations has place    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    productCode:    
      description: 'Code identifying the type of product of this operation. Enum: Z01=Crude oil; Z02=Fuel oil; Z03=Gas-oil; Z04=Gasoline; Z05=Asphalt; Z06=Other petroleum products; Z07=Petroleum energy gases; Z08=Iron ore; Z09=Pyrites; Z10=Other minerals; Z11=Iron scrap; Z12=Coals and petroleum coke; Z13=Steel products; Z14=Phosphates; Z15=Potasses; Z16=Natural and artificial fertilizers; Z17=Chemical products; Z18=Cement and clinker; Z19=Wood and cork; Z20=Construction materials; Z21=Cereals and their flour; Z22=Beans and soy flour; Z23=Fruits, vegetables and legumes; Z24=Wines, alcoholic beverages and derivatives; Z25=Common salt; Z26=Paper and pulp; Z27=Canned; Z28=Tobacco, cocoa, coffee and spices; Z29=Oils and fats; Z30=Other food products; Z31=Machinery, appliances, tools and spare parts; Z32=Automobiles and parts; Z33=Frozen fish; Z34=Rest of merchandise; Z35=Natural gas; Z36=Other metallurgical products; Z37=Feed and forage; Z38=Tare truck cargo platform; Z39=Container tare; Z40=Merchandise in transit containers; Z41=Containers full; Z42=Empty containers; Z43=Vehicles; Z44=Vehicle parts; Z91=Passengers; Z92=Cruise passengers; 1=Fresh fish; Z51=Biofuels; Z52=Other non-metallic minerals; ZR1=Dirty ballast; ZR2=Sludge and settling tanks; ZR3=Bilge oily water tanks; ZR4=Dirty waters; ZR5=Garbage;'    
      enum:    
        - Z01    
        - Z02    
        - Z03    
        - Z04    
        - Z05    
        - Z06    
        - Z07    
        - Z08    
        - Z09    
        - Z10    
        - Z11    
        - Z12    
        - Z13    
        - Z14    
        - Z15    
        - Z16    
        - Z17    
        - Z18    
        - Z19    
        - Z20    
        - Z21    
        - Z22    
        - Z23    
        - Z24    
        - Z25    
        - Z26    
        - Z27    
        - Z28    
        - Z29    
        - Z30    
        - Z31    
        - Z32    
        - Z33    
        - Z34    
        - Z35    
        - Z36    
        - Z37    
        - Z38    
        - Z39    
        - Z40    
        - Z41    
        - Z42    
        - Z43    
        - Z44    
        - Z91    
        - Z92    
        - Z51    
        - Z52    
        - ZR1    
        - ZR2    
        - ZR3    
        - ZR4    
        - ZR5    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    remarks:    
      description: Remarks of the operation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    stevedoreRef:    
      description: 'Id of the stevedore. Format urn:mrn:<oid>:portcalls:operation:stevedore:9999'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    stopRank:    
      description: Rank or Number of this stop in the stop (berth or anchor area) ordered by time sequence    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    terminal:    
      description: Terminal where the operation takes place    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be Operation. In some international standards is also known as [Ship''s Stop]'    
      enum:    
        - Operation    
      type: string    
      x-ngsi:    
        type: Property    
    year:    
      description: Year of the init of the berthing    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2024 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/Operation/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/Berth/schema.json    
  x-model-tags: ESHUV    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
#### 操作 NGSI-v2 键值示例  
下面是一个以 JSON-LD 格式作为键值的操作示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:activity:id:40923",  
  "type": "Operation",  
  "portCode": "ESHUV",  
  "year": 2023,  
  "portCallNumber": "ESHUV202300123",  
  "portCallRef": "urn:mrn:eshuv:portcalls:activity:id:941",  
  "berthRef": "urn:mrn:eshuv:portcalls:berth:id:1234",  
  "stopRank": 2,  
  "operationRank": 1,  
  "ets": "2023-01-01T07:30:00",  
  "etc": "2023-01-01T07:30:00",  
  "operationTypeCode": "ZE",  
  "productCode": "Z41",  
  "amount": 120,  
  "measureUnit": "TEU",  
  "maxWeightPerUnit": 23.3,  
  "terminal": "Muelle Sur",  
  "position": "Segunda linea granel",  
  "remarks": "Delayed 1h",  
  "manipulationMeansCode": "3",  
  "manipulationMeansNumber": 2,  
  "stevedoreRef": "1234"  
}  
```  
</details>  
#### 操作 NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的操作示例。当不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:activity:id:40923",  
  "type": "Operation",  
  "portCode": {  
    "type": "Text",  
    "value": "ESHUV"  
  },  
  "year": {  
    "type": "Number",  
    "value": 2023  
  },  
  "portCallNumber": {  
    "type": "Text",  
    "value": "ESHUV202300123"  
  },  
  "portCallRef": {  
    "type": "Text",  
    "value": "urn:mrn:eshuv:portcalls:activity:id:941"  
  },  
  "berthRef": {  
    "type": "Text",  
    "value": "urn:mrn:eshuv:portcalls:berth:id:1234"  
  },  
  "stopRank": {  
    "type": "Number",  
    "value": 2  
  },  
  "operationRank": {  
    "type": "Number",  
    "value": 1  
  },  
  "ets": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:30:00"  
  },  
  "etc": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:30:00"  
  },  
  "operationTypeCode": {  
    "type": "Text",  
    "value": "ZE"  
  },  
  "productCode": {  
    "type": "Text",  
    "value": "Z41"  
  },  
  "amount": {  
    "type": "Number",  
    "value": 120  
  },  
  "measureUnit": {  
    "type": "Text",  
    "value": "TEU"  
  },  
  "maxWeightPerUnit": {  
    "type": "Number",  
    "value": 23.3  
  },  
  "terminal": {  
    "type": "Text",  
    "value": "Muelle Sur"  
  },  
  "position": {  
    "type": "Text",  
    "value": "Segunda linea granel"  
  },  
  "remarks": {  
    "type": "Text",  
    "value": "Delayed 1h"  
  },  
  "manipulationMeansCode": {  
    "type": "Text",  
    "value": "3"  
  },  
  "manipulationMeansNumber": {  
    "type": "Number",  
    "value": 2  
  },  
  "stevedoreRef": {  
    "type": "Text",  
    "value": "1234"  
  }  
}  
```  
</details>  
#### 操作 NGSI-LD 键值示例  
下面是一个以 JSON-LD 格式作为键值的操作示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:activity:id:40923",  
  "type": "Operation",  
  "portCode": "ESHUV",  
  "year": 2023,  
  "portCallNumber": "ESHUV202300123",  
  "portCallRef": "urn:mrn:eshuv:portcalls:activity:id:941",  
  "berthRef": "urn:mrn:eshuv:portcalls:berth:id:1234",  
  "stopRank": 2,  
  "operationRank": 1,  
  "ets": "2023-01-01T07:30:00",  
  "etc": "2023-01-01T07:30:00",  
  "operationTypeCode": "ZE",  
  "productCode": "Z41",  
  "amount": 120,  
  "measureUnit": "TEU",  
  "maxWeightPerUnit": 23.3,  
  "terminal": "Muelle Sur",  
  "position": "Segunda linea granel",  
  "remarks": "Delayed 1h",  
  "manipulationMeansCode": "3",  
  "manipulationMeansNumber": 2,  
  "stevedoreRef": "1234",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### NGSI-LD 正常化操作示例  
下面是一个规范化 JSON-LD 格式的操作示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:activity:id:40923",  
  "type": "Operation",  
  "portCode": {  
    "type": "Property",  
    "value": "ESHUV"  
  },  
  "year": {  
    "type": "Property",  
    "value": 2023  
  },  
  "portCallNumber": {  
    "type": "Property",  
    "value": "ESHUV202300123"  
  },  
  "portCallRef": {  
    "type": "Relationship",  
    "object": "urn:mrn:eshuv:portcalls:activity:id:941"  
  },  
  "berthRef": {  
    "type": "Relationship",  
    "object": "urn:mrn:eshuv:portcalls:berth:id:1234"  
  },  
  "stopRank": {  
    "type": "Property",  
    "value": 2  
  },  
  "operationRank": {  
    "type": "Property",  
    "value": 1  
  },  
  "ets": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:30:00"  
    }  
  },  
  "etc": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:30:00"  
    }  
  },  
  "operationTypeCode": {  
    "type": "Property",  
    "value": "ZE"  
  },  
  "productCode": {  
    "type": "Property",  
    "value": "Z41"  
  },  
  "amount": {  
    "type": "Property",  
    "value": 120  
  },  
  "measureUnit": {  
    "type": "Property",  
    "value": "TEU"  
  },  
  "maxWeightPerUnit": {  
    "type": "Property",  
    "value": 23.3  
  },  
  "terminal": {  
    "type": "Property",  
    "value": "Muelle Sur"  
  },  
  "position": {  
    "type": "Property",  
    "value": "Segunda linea granel"  
  },  
  "remarks": {  
    "type": "Property",  
    "value": "Delayed 1h"  
  },  
  "manipulationMeansCode": {  
    "type": "Property",  
    "value": "3"  
  },  
  "manipulationMeansNumber": {  
    "type": "Property",  
    "value": 2  
  },  
  "stevedoreRef": {  
    "type": "Property",  
    "value": "1234"  
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
