<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：船长  
=====<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/MasterVessel/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**数据模型旨在提供有关船只的信息。它可以表示每艘船只的属性：静态和动态信息**。  
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
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `beam[number]`: 船宽  . Model: [https://schema.org/Number](https://schema.org/Number)- `buildDate[date]`: 以 ISO 8601 UTC 格式表示的船舶建造日期  . Model: [https://schema.org/Text](https://schema.org/Text)- `callSign[string]`: 无线电初始连接时的船舶识别信号 [EMSWe: DE-065-05] [EDI: BGM-RFF] [S211: Call Name / Call Sign] [IMO: IMO0136]  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `dwt[number]`: 载重吨（DWT）  . Model: [https://schema.org/Number](https://schema.org/Number)- `financialOwner[string]`: 船东  . Model: [https://schema.org/Text](https://schema.org/Text)- `flagCode[string]`: 国际旗帜代码（ISO 3166-1 alfa-2）  . Model: [https://schema.org/Text](https://schema.org/Text)- `gt[number]`: 总吨位（GT）  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 实体的唯一标识符  - `imo[number]`: 国际海事组织编号（全球永久 UID） [EMSWe: DE-003-03] [EDIFACT:TDT-8213] [IALA_S211:vesselId] [IMO:IMO0140]  . Model: [https://schema.org/Number](https://schema.org/Number)- `loa[number]`: 全船长度  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: 项目的 Geojson 引用。可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `manager[string]`: 船舶经理，通常是船舶公司  . Model: [https://schema.org/Text](https://schema.org/Text)- `maxDraught[number]`: 船舶最大吃水  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxLoadVehicle[number]`: 船舶运输车辆的最大能力  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxPassenger[number]`: 船只最大载客量  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVehicle[number]`: 允许的最大车辆尺寸  . Model: [https://schema.org/Number](https://schema.org/Number)- `minNumOfCrew[number]`: 操作船只的最低船员人数  . Model: [https://schema.org/Number](https://schema.org/Number)- `mmsi[number]`: 海事移动服务身份号（临时分配的 UID，由该对象当前船旗国颁发）[EMSWe: DE-068-09] [EDIFACT:TDT-1131] [IALA_S211:vesselId] [IMO:IMO0178]  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `photo[uri]`: 船只照片 URL  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `sleeve[number]`: 容器套筒  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `technicalManager[string]`: 船舶技术经理  . Model: [https://schema.org/Text](https://schema.org/Text)- `toBow[number]`: 弓形尺寸  . Model: [http://schema.org/Number](http://schema.org/Number)- `toPort[number]`: 端口尺寸  . Model: [http://schema.org/Number](http://schema.org/Number)- `toStardboard[number]`: 右舷尺寸  . Model: [http://schema.org/Number](http://schema.org/Number)- `toStern[number]`: 船尾尺寸  . Model: [http://schema.org/Number](http://schema.org/Number)- `type[string]`: NGSI 实体类型。必须是 MasterVessel  - `vesselClass[string]`: 船舶类别代码。枚举：'BD=干散货船；BO=油轮/散货船；BS=卸货散货船；BY=其他类型的散货船；FC=渔船；FO=中转船和/或运输船；GA=载客 RO-RO 船；GC=无专业的杂货船；GD=其他杂货船；GE=综合运输船；GN=集装箱船。GD=Rest General cargo vessels; GE=Buq.transport.combined;GN=Container ship; GO=Ro-ro vessel; GP=Passenger ship; GR=Refrigerator vessel; OO=Buq.or artefact.float be; OS=Supply ships; TC=Transport product.化学品；TD=其他散装液体；TL=运输液化气；TO=油轮；XD=挖泥船；XR=研究和勘探船；XT=拖船/推船；XX=其他船舶和船只；UR=快速通道；G=一般货物；T=散装液体运输船（储罐）；S=散装固体运输船；OB=其他商船；UC=巡航票；OC=公海渔船（冷冻船）；'  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselName[string]`: 船名。[EMSWe: DE-003-07] [EDIFACT:TDT-8212] [IMO:IMO0142]  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselOwner[string]`: 船主  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselSubType[number]`: 枚举：0=不可用（默认值）,1-19=保留供将来使用,20=地面机翼（WIG），所有此类舰船,21=地面机翼（WIG），危险类别 A,22=地面机翼（WIG），危险类别 B,23=地面机翼（WIG），危险类别 C,24=地面机翼（WIG），危险类别 D,25-29=地面机翼（WIG）、危险类别 B,23=Wing in ground (WIG)，危险类别 C,24=Wing in ground (WIG)，危险类别 D,25-29=Wing in ground (WIG)，保留给将来使用,30=Fishing,31=Towing,32=Towing：长度超过 200 米或宽度超过 25 米,33=挖泥或水下作业,34=潜水作业,35=军事作业,36=航行,37=游艇,38-39=保留,40=高速船（HSC），所有此类船只,41=高速船（HSC），危险类别 A,42=高速船（HSC），危险类别 B,43=高速船（HSC），危险类别 C、44=高速船（HSC），危险类别 D,45-48=高速船（HSC），保留供将来使用,49=高速船（HSC），无其他信息,50=引航船,51=搜索和救援船,52=拖船,53=港口补给船,54=防污染设备,55=执法船,56-57=备用-本地船,58=医疗运输船,59=根据 RR Resolution No.18,60=乘客，所有此类船舶,61=乘客，危险类别 A,62=乘客，危险类别 B,63=乘客，危险类别 C,64=乘客，危险类别 D,65-68=乘客，留待将来使用,69=乘客，无其他信息、70=货物，所有此类船舶,71=货物，危险类别 A,72=货物，危险类别 B,73=货物，危险类别 C,74=货物，危险类别 D,75-78=货物，保留供将来使用,79=货物，无附加信息,80=油轮、所有此类船舶,81=油轮，危险类别 A,82=油轮，危险类别 B,83=油轮，危险类别 C,84=油轮，危险类别 D,85-88=油轮，保留将来使用,89=油轮，无其他信息,90=其他类型、所有此类船舶,91=其他类型，危险类别 A,92=其他类型，危险类别 B,93=其他类型，危险类别 C,94=其他类型，危险类别 D,95-98=其他类型，保留将来使用,99=其他类型，无其他信息'。容器子类型代码  . Model: [https://schema.org/Number](https://schema.org/Number)- `vesselType[number]`: 枚举：'1=保留,2=机翼着地,3=特殊类别,4=高速船,5=特殊类别,6=客运,7=货运,8=油轮,9=其他'。船舶类型代码  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
MasterVessel:    
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
      description: Beam of the Vessel    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meters    
    buildDate:    
      description: Date of building of the vessel represented by an ISO 8601 UTC format    
      format: date    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    callSign:    
      description: 'Identification signal of a vessel when initially connecting by radio [EMSWe: DE-065-05] [EDI: BGM-RFF] [S211: Call Name / Call Sign] [IMO: IMO0136] '    
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
    dwt:    
      description: Dead weight Tonnage (DWT)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: tons    
    financialOwner:    
      description: Financial Owner of the vessel    
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
    gt:    
      description: Gross Tonnage (GT)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: moorson tons    
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
      description: 'International Maritime Organization Number (a global forever UID) [EMSWe: DE-003-03] [EDIFACT:TDT-8213] [IALA_S211:vesselId] [IMO:IMO0140] '    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    loa:    
      description: Length Over All of Vessel    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meters    
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
      description: 'Manager of the Vessel, usually Ship Company'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    maxDraught:    
      description: Maximum Draught of the vessel    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meters    
    maxLoadVehicle:    
      description: Max capacity of vessel to transport vehicles    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maxPassenger:    
      description: Max capacity of vessel to transport passengers    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maxVehicle:    
      description: Max dimensions of vehicle permitted    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    minNumOfCrew:    
      description: Minimum number of crew to operate the vessel    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    mmsi:    
      description: 'Marine Mobile Service Identity Number (a temporarily assigned UID, issued by that object''s current flag state)[EMSWe: DE-068-09] [EDIFACT:TDT-1131] [IALA_S211:vesselId] [IMO:IMO0178]'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    photo:    
      description: Vessel Photo URL    
      format: uri    
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
    sleeve:    
      description: Sleeve of Vessel    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meters    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    technicalManager:    
      description: Technical Manager of the vessel    
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
        units: meters    
    toPort:    
      description: Dimension to Port    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: meters    
    toStardboard:    
      description: Dimension to Starboard    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: meters    
    toStern:    
      description: Dimension to Stern    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: meters    
    type:    
      description: NGSI Entity type. It has to be MasterVessel    
      enum:    
        - MasterVessel    
      type: string    
      x-ngsi:    
        type: Property    
    vesselClass:    
      description: 'Code for vessel class. Enum:''BD=Dry bulk; BO=Oil tanker / bulk carrier; BS=Bulk carrier unloading; BY=Other types of bulk carriers; FC=Fishing vessel; FO=Vessel. transfer and/or transp.; GA=Vessel. RO-RO with passengers; GC=Mrcia general without specialization; GD=Rest general cargo vessels; GE=Buq. transp. combined; GN=Container ship; GO=Ro-ro vessel; GP=Passenger ship; GR=Refrigerator vessel; OO=Buq. or artefact. float be; OS=Supply ships; TC=Transport product. chemicals; TD=Other liquid bulk; TL=Transportation of liquefied gas; TO=Oil tanker; XD=Dredges; XR=Research and exploration; XT=Tugs / pushers; XX=Other ships and boats; UR=Fast Pass; G=General Cargo; T=Liquid Bulk Carriers (Tanks); S=Solid Bulk Carriers; OB=Other Merchant Vessels; UC=Cruise Ticket; OC=High Sea Fishing Vessels (Freezers);'''    
      enum:    
        - BD    
        - BO    
        - BS    
        - BY    
        - FC    
        - FO    
        - GA    
        - GC    
        - GD    
        - GE    
        - GN    
        - GO    
        - GP    
        - GR    
        - OO    
        - OS    
        - TC    
        - TD    
        - TL    
        - TO    
        - XD    
        - XR    
        - XT    
        - XX    
        - UR    
        - G    
        - T    
        - S    
        - OB    
        - UC    
        - OC    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vesselName:    
      description: 'Name of the Vessel. [EMSWe: DE-003-07] [EDIFACT:TDT-8212] [IMO:IMO0142]'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vesselOwner:    
      description: Owner of the Vessel    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vesselSubType:    
      description: 'Enum:''0=Not available (default),1-19=Reserved for future use,20=Wing in ground (WIG), all ships of this type,21=Wing in ground (WIG), Hazardous category A,22=Wing in ground (WIG), Hazardous category B,23=Wing in ground (WIG), Hazardous category C,24=Wing in ground (WIG), Hazardous category D,25-29=Wing in ground (WIG), Reserved for future use,30=Fishing,31=Towing,32=Towing: length exceeds 200m or breadth exceeds 25m,33=Dredging or underwater ops,34=Diving ops,35=Military ops,36=Sailing,37=Pleasure Craft,38-39=Reserved,40=High speed craft (HSC), all ships of this type,41=High speed craft (HSC), Hazardous category A,42=High speed craft (HSC), Hazardous category B,43=High speed craft (HSC), Hazardous category C,44=High speed craft (HSC), Hazardous category D,45-48=High speed craft (HSC), Reserved for future use,49=High speed craft (HSC), No additional information,50=Pilot Vessel,51=Search and Rescue vessel,52=Tug,53=Port Tender,54=Anti-pollution equipment,55=Law Enforcement,56-57=Spare - Local Vessel,58=Medical Transport,59=Noncombatant ship according to RR Resolution No. 18,60=Passenger, all ships of this type,61=Passenger, Hazardous category A,62=Passenger, Hazardous category B,63=Passenger, Hazardous category C,64=Passenger, Hazardous category D,65-68=Passenger, Reserved for future use,69=Passenger, No additional information,70=Cargo, all ships of this type,71=Cargo, Hazardous category A,72=Cargo, Hazardous category B,73=Cargo, Hazardous category C,74=Cargo, Hazardous category D,75-78=Cargo, Reserved for future use,79=Cargo, No additional information,80=Tanker, all ships of this type,81=Tanker, Hazardous category A,82=Tanker, Hazardous category B,83=Tanker, Hazardous category C,84=Tanker, Hazardous category D,85-88=Tanker, Reserved for future use,89=Tanker, No additional information,90=Other Type, all ships of this type,91=Other Type, Hazardous category A,92=Other Type, Hazardous category B,93=Other Type, Hazardous category C,94=Other Type, Hazardous category D,95-98=Other Type, Reserved for future use,99=Other Type, no additional information''. Code for vessel Sub-Type'    
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
      description: 'Enum:''1=Reserved,2=Wing In Ground,3=Special Category,4=High-Speed Craft,5=Special Category,6=Passenger,7=Cargo,8=Tanker,9=Other''. Code for vessel type'    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2024 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/MasterVessel/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/MasterVessel/schema.json    
  x-model-tags: ESHUV    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
#### MasterVessel NGSI-v2 键值示例  
下面是一个以 JSON-LD 格式作为键值的 MasterVessel 示例。当使用 "options=keyValues "时，这与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:mastervessel:id:1234",  
  "type": "MasterVessel",  
  "vesselName": "ELEANOR R.",  
  "imo": 9863637,  
  "mmsi": 210049000,  
  "callSign": "5BPC3",  
  "flagCode": "CY",  
  "vesselType": 1,  
  "vesselSubType": 2,  
  "vesselClass": "BO",  
  "gt": 12467,  
  "beam": 7,  
  "loa": 132.22,  
  "sleeve": 25.51,  
  "maxDraught": 5.61,  
  "dwt": 8.10,  
  "buildDate": "2023-06-01",  
  "toBow": 3,  
  "toStern": 20,  
  "toPort": 17,  
  "toStardboard": 4,  
  "photo": "https://acme.com/photos/9863637",  
  "owner": [  
    "urn:ngsi-ld:Acme-OWNER-NAME"  
  ],  
  "vesselOwner": "Acme OWNER NAME",  
  "manager": "Acme MANAGER NAME",  
  "financialOwner": "Acme FINANCIAL ",  
  "technicalManager": "Acme TECHNICAL MANAGER",  
  "dataProvider": "AIS",  
  "maxLoadVehicle": 120,  
  "maxPassenger": 0,  
  "maxVehicle": 16,  
  "minNumOfCrew": 12  
}  
```  
</details>  
#### MasterVessel NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的 MasterVessel 示例。在不使用选项的情况下，这与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:mastervessel:id:1234",  
  "type": "MasterVessel",  
  "vesselName": {  
    "type": "Text",  
    "value": "ELEANOR R."  
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
  "vesselClass": {  
    "type": "Text",  
    "value": "BO"  
  },  
  "gt": {  
    "type": "Number",  
    "value": 12467  
  },  
  "beam": {  
    "type": "Number",  
    "value": 7  
  },  
  "loa": {  
    "type": "Number",  
    "value": 132.22  
  },  
  "sleeve": {  
    "type": "Number",  
    "value": 25.51  
  },  
  "maxDraught": {  
    "type": "Number",  
    "value": 5.61  
  },  
  "dwt": {  
    "type": "Number",  
    "value": 8.1  
  },  
  "buildDate": {  
    "type": "Date-Time",  
    "value": "2023-06-01"  
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
  "photo": {  
    "type": "Text",  
    "value": "https://acme.com/photos/9863637"  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:Acme-OWNER-NAME"  
    ]  
  },  
  "vesselOwner": {  
    "type": "Text",  
    "value": "Acme OWNER NAME"  
  },  
  "manager": {  
    "type": "Text",  
    "value": "Acme MANAGER NAME"  
  },  
  "financialOwner": {  
    "type": "Text",  
    "value": "Acme FINANCIAL "  
  },  
  "technicalManager": {  
    "type": "Text",  
    "value": "Acme TECHNICAL MANAGER"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "AIS"  
  },  
  "maxLoadVehicle": {  
    "type": "Number",  
    "value": 120  
  },  
  "maxPassenger": {  
    "type": "Boolean",  
    "value": false  
  },  
  "maxVehicle": {  
    "type": "Number",  
    "value": 16  
  },  
  "minNumOfCrew": {  
    "type": "Number",  
    "value": 12  
  }  
}  
```  
</details>  
#### MasterVessel NGSI-LD 键值示例  
下面是一个以 JSON-LD 格式作为键值的 MasterVessel 示例。当使用 `options=keyValues` 时，这与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:mastervessel:id:1234",  
  "type": "MasterVessel",  
  "vesselName": "ELEANOR R.",  
  "imo": 9863637,  
  "mmsi": 210049000,  
  "callSign": "5BPC3",  
  "flagCode": "CY",  
  "vesselType": 1,  
  "vesselSubType": 2,  
  "vesselClass": "BO",  
  "gt": 12467,  
  "beam": 7,  
  "loa": 132.22,  
  "sleeve": 25.51,  
  "maxDraught": 5.61,  
  "dwt": 8.10,  
  "buildDate": "2023-06-01",  
  "toBow": 3,  
  "toStern": 20,  
  "toPort": 17,  
  "toStardboard": 4,  
  "photo": "https://acme.com/photos/9863637",  
  "owner": [  
    "urn:ngsi-ld:Acme-OWNER-NAME"  
  ],  
  "vesselOwner": "Acme OWNER NAME",  
  "manager": "Acme MANAGER NAME",  
  "financialOwner": "Acme FINANCIAL ",  
  "technicalManager": "Acme TECHNICAL MANAGER",  
  "dataProvider": "AIS",  
  "maxLoadVehicle": 120,  
  "maxPassenger": 0,  
  "maxVehicle": 16,  
  "minNumOfCrew": 12,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/refs/heads/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### MasterVessel NGSI-LD 归一化示例  
下面是一个规范化 JSON-LD 格式的 MasterVessel 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:mastervessel:id:1234",  
  "type": "MasterVessel",  
  "vesselName": {  
    "type": "Property",  
    "value": "ELEANOR R."  
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
    "value": "CY"  
  },  
  "vesselType": {  
    "type": "Property",  
    "value": true  
  },  
  "vesselSubType": {  
    "type": "Property",  
    "value": 2  
  },  
  "vesselClass": {  
    "type": "Property",  
    "value": "BO"  
  },  
  "gt": {  
    "type": "Property",  
    "value": 12467  
  },  
  "beam": {  
    "type": "Property",  
    "value": 7  
  },  
  "loa": {  
    "type": "Property",  
    "value": 132.22  
  },  
  "sleeve": {  
    "type": "Property",  
    "value": 25.51  
  },  
  "maxDraught": {  
    "type": "Property",  
    "value": 5.61  
  },  
  "dwt": {  
    "type": "Property",  
    "value": 8.1  
  },  
  "buildDate": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "value": "2023-06-01"  
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
  "photo": {  
    "type": "Property",  
    "value": "https://acme.com/photos/9863637"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Acme-OWNER-NAME"  
    ]  
  },  
  "vesselOwner": {  
    "type": "Property",  
    "value": "Acme OWNER NAME"  
  },  
  "manager": {  
    "type": "Property",  
    "value": "Acme MANAGER NAME"  
  },  
  "financialOwner": {  
    "type": "Property",  
    "value": "Acme FINANCIAL "  
  },  
  "technicalManager": {  
    "type": "Property",  
    "value": "Acme TECHNICAL MANAGER"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "AIS"  
  },  
  "maxLoadVehicle": {  
    "type": "Property",  
    "value": 120  
  },  
  "maxPassenger": {  
    "type": "Property",  
    "value": false  
  },  
  "maxVehicle": {  
    "type": "Property",  
    "value": 16  
  },  
  "minNumOfCrew": {  
    "type": "Property",  
    "value": 12  
  }  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
有待商定每个字段的标准标识。对于 URN 的形成，将考虑以下标准 - SO 3166-1 - 国家代码及其分支代码的国际标准。- RFC 2141 - URN 语法 (https://www.ietf.org/rfc/rfc2141.txt) - RFC 8141 - 统一资源名称 (URN) (https://tools.ietf.org/html/rfc8141) - IALAs MRN 请求 (https://www.iana.org/assignments/urn-formal/mrn)  
<MRN> ::= "urn" ":" "mrn" ":" <OID> ":" <OSNID> ":" <OSNS> <OID> ::= (alphanum) 0*32(alphanum / "-") (alphanum) ; 组织 ID（即 ESHUV<OSNID> ::= (alphanum) 0*32(alphanum / "-") (alphanum) ; 特定于组织的命名空间 ID（即端口调用） <OSNS> ::= pchar *(pchar / "/") ; 特定于组织的命名空间字符串（即模块或微服务的名称。<ID> ::= 该命名空间的唯一标识符（即 SQL 数据库中实体名称后的行标识符）  
例如 urn := "urn:mrn:eshuv:portcalls:portcall:id:343"  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
