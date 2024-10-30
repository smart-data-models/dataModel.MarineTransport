<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：泊位  
=====<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/Berth/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**本数据模型旨在提供有关泊位的信息。我们将 "泊位 "定义为船舶在港口呼叫（PortCall）期间的每次停靠，既包括港口设施（泊位），也包括锚地。每个泊位都有一个停泊时间（预计、计划等）、一个生命周期（预计、申请、批准等）、停靠期间的主要活动（商业运营、大修等）和下面描述的一些属性。当商业运营发生时，运营实体将定义每个商业运营的细节**。  
版本： 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。  
- `activityCode[string]`: 停泊期间的活动。它可以是货物操作，也可以是与船舶-港口活动有关的一系列活动。枚举：ZGR=大修； ZPV=供应； ZCA=船厂建造； ZRA=船厂大修； ZRF=船员在海上修理； ZRT=船员以外人员在锚地修理； ZDA=船厂报废； ZTA=船厂改造； ZTF=改造；ZAO=正式访问；ZAF=强行抵达；ZAIN=不活动；ZAIP=不活动捕鱼；ZAR=停靠供应；ZAO=锚地供应；ZAB=驳船停靠供应；ZAP=商业运输的港口作业；ZACT=观光游船；ZAI=内部运输；ZBO=下水；ZCO=施工；ZRE=用于拖曳服务的船舶；ZDE=废料场；ZAP=从事鲜鱼装卸作业的渔船和手工船；ZDR=用于疏浚的船舶；ZPB=生物停航；ZCL=无许可证；ZDJ=司法押金；ZMR=用于系泊服务的船舶； ZPR=用于引航服务的船舶； ZRM=拖车； ZVA=进入船台； ZDS=干船坞中的船舶； ZOT=其他； EST=停留； ZSA=供水； ZSH=供冰； ZSE=电能供应； ZSC=燃料供应； ZSV=运输；  . Model: [https://schema.org/Text](https://schema.org/Text)- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理    
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 标识公共街道上特定房产的编号    
- `agentLegalCode[string]`: PortCall 船舶代理的法定识别代码  . Model: [https://schema.org/Text](https://schema.org/Text)- `agentName[string]`: PortCall 船舶代理名称  . Model: [https://schema.org/Text](https://schema.org/Text)- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrivalDraught[number]`: 确保抵达航道的一线吃水  . Model: [https://schema.org/Number](https://schema.org/Number)- `ataBerth[date-time]`: 以 ISO 8601 UTC 格式表示，实际抵达泊位时间  - `atdBerth[date-time]`: 以 ISO 8601 UTC 格式表示。离开泊位的实际时间  - `authorizationRemarks[string]`: 港务局所写的停泊条件  . Model: [https://schema.org/Text](https://schema.org/Text)- `authorizedAt[date-time]`: 以 ISO 8601 UTC 格式表示，港务局和海事局授权的日期和时间。  - `berthCode[string]`: 船舶停靠港口设施的代码。格式为<oid>:berth:99999  . Model: [https://schema.org/Text](https://schema.org/Text)- `berthName[string]`: 船舶此次停靠的港口设施名称  . Model: [https://schema.org/Text](https://schema.org/Text)- `berthingTypeCode[string]`: 用于识别接口船港停泊/停泊类型的代码。枚举：ABV=左舷靠泊；ABX=港口靠泊；AB1=船首靠泊左舷；AB2=船尾靠泊左舷；AEX=右舷靠泊；AX1=船首靠泊；AEV=右舷靠泊；REM=码头右舷靠泊；REX=船首靠泊；RE1=船首靠泊右舷；RE2=船尾靠泊右舷；RPM=船头至弹簧扭转； RPV=船头至船舷； RPX=锚定点； RXM=停泊在码头旁； RXV=停泊在另一艘船上； RXX=停泊； RX1=船头缠绕； AE1=船头撞击右舷； AE2=船尾撞击右舷； APM=停泊在码头； APV=停泊在船上；APX=点靠岸； AXM=靠码头； AXV=靠船舷； AXX=靠岸； AX2=靠船尾； FBM=靠码头锚定左舷； FBV=靠船舷锚定左舷； FBX=靠码头锚定左舷； FB1=靠船首锚定左舷； FB2=靠船尾锚定左舷； FEM=靠码头锚定右舷；FEV=右舷锚定至船舶； FEX=右舷锚定； FE1=船首锚定右舷； FE2=船尾锚定右舷； FPM=舣舟； FPV=船头锚定至船舶； FPX=点锚定； FP1=船首锚定船头； FP2=船尾锚定船头； FXM=锚定在码头； FXV=锚定至船舶；FX1=锚泊在船首；FX2=锚泊在船尾；RBM=锚泊在码头左舷；RBX=锚泊在左舷；RB1=锚泊在船首左舷；RB2=锚泊在船尾左舷；RX2=锚泊在船尾；YBM=锚泊在码头左舷浮标上；YBV=锚泊在船左舷浮标上；YBX=系在左舷浮标上；YB1=系在船首的左舷浮标上；YB2=系在船尾的左舷浮标上；YEM=系在码头的右舷浮标上；YEV=系在船上的右舷浮标上；YEX=系在右舷浮标上；YE1=系在船首的右舷浮标上；YE2=系在船尾的右舷浮标上；YPM=系在码头端部浮标上； YPV=系在船尾浮标上； YPX=系在船首浮标上； YP1=系在船首浮标上； YP2=系在船尾浮标上； YXM=系在码头浮标上； YXV=系在船尾浮标上； YX1=系在船首浮标上；YX2=拴在船尾的浮标上；ABM=靠泊在码头的港口；AEM=靠泊在码头的右舷；FXX=锚定；YXX=拴在浮标上，无进一步指示；AP1=靠船头的尖端；AP2=前后袋装；RBV=靠船头的港口；REV=靠船尾的右舷；。  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `departureDraught[number]`: 在最后一线释放的吃水，用于离港航行  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: 项目描述  - `etaBerth[date-time]`: 用 ISO 8601 UTC 格式表示，即港务局预计到达泊位的估计时间的日期和时间（ISO 8601 UTC 格式）。[EMSWe：DE-005-09] [EDI：DTM-2005-132] [S211：locationState.timeType.ESTIMATED] [IMO：IMO0064]  - `etdBerth[date-time]`: 以 ISO 8601 UTC 格式表示，港务局预计的估计离泊时间的日期和时间。[EMSWe：DE-005-04] [EDI：DTM-2005-133] [S211：locationState.timeType.ESTIMATED] [IMO：IMO0066]  - `firstBollard[string]`: 港口设施中的首个系缆桩识别器  . Model: [https://schema.org/Text](https://schema.org/Text)- `gln[number]`: ISO/IEC 6523:'https://schema.org/Number'。地点的可选代码。全球位置编号（GLN）是一个 13 位数的唯一编号，分配给位置后，可在全球范围内对其进行唯一标识，并分配给供应链中的任何位置。这些 GLN 可用于识别任何法律、物理和功能地点  - `id[*]`: 实体的唯一标识符  - `lastBollard[string]`: 港口设施中最后一个系缆桩标识符  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `mooringLines[number]`: 缆绳数量。  . Model: [https://schema.org/Number](https://schema.org/Number)- `mrn[string]`: MRN 编码标识符。该标识符必须与实体相关，其含义和实体的发起者必须为不同的机构所熟知，并且所有下一个机构都将保持其原始值。该标识符必须是由创建该实体的系统分配的 PortCall 实体的唯一标识符。该 URN 应符合 MRN 和 IETF，特别是 RFC 2141、RFC 5234 和 RFC 8141。建议格式为 id::='urn:mrn:<OID>:<ONSS>:portcalls:berth:id:[0-9]+'，其中 OID:= Organisation UN/LOCODE，OONSS:=Organization Name of Service，99999999 是一个递增的唯一标识符，泊位实体的发行者将在其系统中识别该标识符（即 SQL 行标识符），即 urn:mrn:eshuv:portcalls:berth:id:2024012。参见 [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)。在国际标准中也称为 [船舶访问]。  - `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `portCallNumber[string]`: 端口呼叫标识符  . Model: [https://schema.org/Text](https://schema.org/Text)- `portCallRef[*]`: 关系.父 PortCall 实体的引用。  - `portCode[string]`: 停靠港代码  . Model: [https://schema.org/Text](https://schema.org/Text)- `ptaBerth[date-time]`: 用 ISO 8601 UTC 格式表示，计划抵达泊位的时间  - `ptdBerth[date-time]`: 以 ISO 8601 UTC 格式表示。计划离开泊位的时间  - `remarks[string]`: 港口代理或其他人对停泊情况的说明  . Model: [https://schema.org/Text](https://schema.org/Text)- `requestedAt[date-time]`: 以 ISO 8601 UTC 格式表示，船舶代理申请停泊的日期和时间。  - `rtaBerth[date-time]`: 由 ISO 8601 UTC 格式表示，船舶代理请求到达时间的日期和时间（ISO 8601 UTC 格式）... [EMSWe: DE-005-09] [EDI: DTM-2005-132] [S211: locationState.timeType.ESTIMATED] [IMO: IMO0064].  - `rtdBerth[date-time]`: 以 ISO 8601 UTC 格式表示，船舶代理要求的离港时间日期和时间（ISO 8601 UTC 格式）。[EMSWe: DE-005-09] [EDI: DTM-2005-132] [S211: locationState.timeType.ESTIMATED] [IMO: IMO0064]  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `status[string]`: 停泊从申请到授权和完成的整个过程中的当前状态。枚举：'ACCEPTED、AUTHORIZED、CANCELLED、COMPLETED、DENIED、INITIATED、REQUESTED、REJECTED、INVOICING、INVOICED'。[EMSWe：DE-019-07] [EDI：BGM-1225] [S211：serviceState：timeSequence：VESSEL] [S211：serviceState：timeSequence：VESSEL  . Model: [https://schema.org/Text](https://schema.org/Text)- `stopRank[number]`: 该停靠站在 PortCall 活动中的等级或编号，按停靠站（泊位/锚地）序列中的到达时间排序  . Model: [https://schema.org/Number](https://schema.org/Number)- `terminal[string]`: 航站楼的通用名称  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI 实体类型。必须是泊位  - `year[number]`: 开始停泊的年份  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `portCallRef`  - `stopRank`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
从 ERA 本体映射的数据模型 https://data-interop.era.europa.eu/era-vocabulary（欧盟铁路局）  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Berth:    
  description: 'This data model is intended to provide information about Berths. We define ''berth'' to each stop of a ship during a PortCall, both for a port-facility (berth) and as an anchorage area. Each berth has a berthing time (estimated, planned, etc.), a lifecycle (estimated, requested, approved, etc.), an main activity during the stop (commercial operations, major repair, etc.) and a number of attributes described below. When commercial operations take place, an Operation entity will define the details of each commercial operation'    
  properties:    
    activityCode:    
      description: 'Activity during the stop in berth. It can be cargo operations or a number of activities related to the ship-port activities. Enum: ZGR=Major repair; ZPV=Provisioning; ZCA=Shipyard Construction; ZRA=Major shipyard repair; ZRF=Repair afloat with crew personnel; ZRT=Repair at anchor with personnel other than the crew; ZDA=Shipyard scrapping; ZTA=Shipyard Transformation; ZTF=Transformation; ZVO=Official visit; ZAF=Forced arrival; ZIN=Inactive; ZIP=Fishing inactivity; ZAR=Provisioning at docking; ZAO=Provisioning at anchor; ZAB=Provisioning at docking by barge; ZOP=Port operations of commercial traffic; ZCT=Sightseeing cruises; ZTI=Internal traffic; ZBO=Launching; ZCO=Construction; ZRE=Vessel intended for towing service; ZDE=Scrapyard; ZAP=Fishing and artisanal vessels in loading and unloading operations of fresh fish; ZDR=Vessel intended for dredging; ZPB=Biological stoppage; ZCL=No license; ZDJ=Judicial deposit; ZMR=Vessel intended for mooring service; ZPR=Vessel intended for pilotage service; ZRM=Trailer; ZVA=Access to slipway; ZDS=Vessel in dry dock; ZOT=Other; EST=Stay; ZSA=Water Supply; ZSH=Ice Supply; ZSE=Electrical Energy Supply; ZSC=Fuel Supply; ZSV=Victualling;'    
      enum:    
        - ZGR    
        - ZPV    
        - ZCA    
        - ZRA    
        - ZRF    
        - ZRT    
        - ZDA    
        - ZTA    
        - ZTF    
        - ZVO    
        - ZAF    
        - ZIN    
        - ZIP    
        - ZAR    
        - ZAO    
        - ZAB    
        - ZOP    
        - ZCT    
        - ZTI    
        - ZBO    
        - ZCO    
        - ZRE    
        - ZDE    
        - ZAP    
        - ZDR    
        - ZPB    
        - ZCL    
        - ZDJ    
        - ZMR    
        - ZPR    
        - ZRM    
        - ZVA    
        - ZDS    
        - ZOT    
        - EST    
        - ZSA    
        - ZSH    
        - ZSE    
        - ZSC    
        - ZSV    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    agentLegalCode:    
      description: Legal identifier code of the PortCall's ship Agent    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    agentName:    
      description: Name of PortCall's ship Agent    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    arrivalDraught:    
      description: Draught at first-line secured for arriving navigation    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ataBerth:    
      description: 'Represented by an ISO 8601 UTC format, Actual time of arrival to Berth'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    atdBerth:    
      description: Represented by an ISO 8601 UTC format. Actual time of departure from Berth    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    authorizationRemarks:    
      description: Conditions to the berthing written by Port Authority    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    authorizedAt:    
      description: 'Represented by an ISO 8601 UTC format, Date and time of authorization by port Authority and Maritime Authority. '    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    berthCode:    
      description: 'Code identifying the port-facility for this stop of the vessel. Format: <oid>:berth:99999'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    berthName:    
      description: Name of the port-facility for this stop of the vessel    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    berthingTypeCode:    
      description: 'Codes for identifying the Type of berthing/mooring in the interface ship-port. Enum: ABV=Board port to ship; ABX=Port berthed; AB1=Bouched port by bow; AB2=Bouched port by stern; AEX=Starboard docked; AX1=Docked by bow; AEV=Board starboard to ship; REM=Boarded starboard at the pier; REX=Starboard bow; RE1=Starboard bow by bow; RE2=Cracked starboard by stern; RPM=Toe-to-spring twisting; RPV=Boarded from tip to ship; RPX=Ringed point; RXM=To moor alongside a dock; RXV=Moored to another vessel; RXX=Moored ; RX1=Tangled by bow; AE1=Bouched starboard by bow; AE2=Bouched starboard by stern; APM=Pocketed to the pier; APV=Pocket to ship; APX=Point docking; AXM=docked at the pier; AXV=Boarded to ship; AXX=docked; AX2=Docked by stern; FBM=Anchored port side at the pier; FBV=Anchored port side to ship; FBX=Port anchored; FB1=Anchored port by bow; FB2=Anchored port by stern; FEM=Anchored starboard to the pier; FEV=Anchored starboard to ship; FEX=Anchored starboard; FE1=Anchored starboard by bow; FE2=Anchored starboard by stern; FPM=Toe-to-pier mooring; FPV=Anchoring tip to ship; FPX=Point anchoring; FP1=Anchoring tip by bow; FP2=Anchoring tip by stern; FXM=Anchored at the pier; FXV=Anchored to ship; FX1=Anchored by bow; FX2=Anchored by stern; RBM=Moored portside to the dock; RBX=Battered port side; RB1=Bulked port by bow; RB2=Bulked on port side by stern; RX2=Tangled by stern; YBM=Tethered to the port buoy at the pier; YBV=Tethered to the buoy on the port side of the ship; YBX=Tethered to port buoy; YB1=Tied to port buoy by bow; YB2=Tied to port buoy by stern; YEM=Tethered to the starboard buoy at the pier; YEV=Tethered to the starboard buoy of the ship; YEX=Tethered to starboard buoy; YE1=Tied to starboard buoy by bow; YE2=Tied to starboard buoy by stern; YPM=Tethered to the end buoy at the pier; YPV=Tethered to the buoy end-to-ship; YPX=Tied to tip buoy; YP1=Tethered to tip buoy by bow; YP2=Tied to the tip buoy by stern; YXM=Tethered to the buoy at the pier; YXV=Tethered to the buoy to the ship; YX1=Tethered to buoy by bow; YX2=Tethered to buoy by stern; ABM=Port berthed to the pier; AEM=Moored starboard to dock; FXX=Anchoring; YXX=Tethered to buoy without further indication; AP1=Boarding tip by bow; AP2=Pocketed fore and aft; RBV=Bulked port to ship; REV=Wheeled starboard to ship;. '    
      enum:    
        - ABV    
        - ABX    
        - AB1    
        - AB2    
        - AEX    
        - AX1    
        - AEV    
        - REM    
        - REX    
        - RE1    
        - RE2    
        - RPM    
        - RPV    
        - RPX    
        - RXM    
        - RXV    
        - RXX    
        - RX1    
        - AE1    
        - AE2    
        - APM    
        - APV    
        - APX    
        - AXM    
        - AXV    
        - AXX    
        - AX2    
        - FBM    
        - FBV    
        - FBX    
        - FB1    
        - FB2    
        - FEM    
        - FEV    
        - FEX    
        - FE1    
        - FE2    
        - FPM    
        - FPV    
        - FPX    
        - FP1    
        - FP2    
        - FXM    
        - FXV    
        - FX1    
        - FX2    
        - RBM    
        - RBX    
        - RB1    
        - RB2    
        - RX2    
        - YBM    
        - YBV    
        - YBX    
        - YB1    
        - YB2    
        - YEM    
        - YEV    
        - YEX    
        - YE1    
        - YE2    
        - YPM    
        - YPV    
        - YPX    
        - YP1    
        - YP2    
        - YXM    
        - YXV    
        - YX1    
        - YX2    
        - ABM    
        - AEM    
        - FXX    
        - YXX    
        - AP1    
        - AP2    
        - RBV    
        - REV    
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
    departureDraught:    
      description: Draught at last-line released for departure navigation    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    etaBerth:    
      description: 'Represented by an ISO 8601 UTC format, Date and time of Estimated Time of Arrival to Berth expected by Port Authority (ISO 8601 UTC format). [EMSWe: DE-005-09] [EDI: DTM-2005-132] [S211: locationState.timeType.ESTIMATED] [IMO: IMO0064]'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    etdBerth:    
      description: 'Represented by an ISO 8601 UTC format, Date and time of Estimated Time of Departure from Berth, expected by Port Authority. [EMSWe: DE-005-04] [EDI: DTM-2005-133] [S211: locationState.timeType.ESTIMATED] [IMO: IMO0066]'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    firstBollard:    
      description: First bollard identifier in port facility    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    gln:    
      description: 'ISO/IEC 6523:''https://schema.org/Number''. Optional code of the location. The Global Location Number (GLN) is a 13 digits-unique number that is assigned to locations to enable them to be identified uniquely worldwide, allocated to any location in the supply chain. These GLNs can be used to identify any legal, physical and functional locations'    
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
        type: Property    
    lastBollard:    
      description: Last bollard identifier in port facility    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    mooringLines:    
      description: 'Number of mooring lines. '    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    mrn:    
      description: 'MRN coded identifier. It has to be related to the entity in a way that is well-known by different organisms the meaning and the initiator of the entity, and all next parties will maintain on its original value. This identifier must be an UNIQUE identifier of the PortCall entity assigned by the system who created on first the entity. This URN should Conforms MRN & IETF specifically RFC 2141, RFC 5234, and RFC 8141. The proposed format is id::=''urn:mrn:<OID>:<ONSS>:portcalls:berth:id:[0-9]+'' where OID:= Organisation UN/LOCODE, OONSS:=Organization Name of Service, 9999999 an increasing, unique identifier that the issuer of the Berth entity will identify on his systems (i.e. a SQL row-id), i.e. urn:mrn:eshuv:portcalls:berth:id:2024012. See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory). In international standards is also known as [Ship''s Visit]'    
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
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    portCallNumber:    
      description: PortCall identifier    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    portCallRef:    
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
      description: 'Relationship.Reference to parent PortCall entity. '    
    portCode:    
      description: Code of the port of the call    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    ptaBerth:    
      description: 'Represented by an ISO 8601 UTC format, Planned time of arrival to Berth'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    ptdBerth:    
      description: Represented by an ISO 8601 UTC format. Planned time of departure from Berth    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    remarks:    
      description: 'Remarks of the berthing, by Agent at Port or others'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    requestedAt:    
      description: 'Represented by an ISO 8601 UTC format, Date and time of the berthing request by the ship agent. '    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    rtaBerth:    
      description: 'Represented by an ISO 8601 UTC format, Date and time of Requested Time of Arrival by ship-agent (ISO 8601 UTC format).. [EMSWe: DE-005-09] [EDI: DTM-2005-132] [S211: locationState.timeType.ESTIMATED] [IMO: IMO0064]'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    rtdBerth:    
      description: 'Represented by an ISO 8601 UTC format, Date and time of Requested Time of Departure by ship-agent (ISO 8601 UTC format). [EMSWe: DE-005-09] [EDI: DTM-2005-132] [S211: locationState.timeType.ESTIMATED] [IMO: IMO0064]'    
      format: date-time    
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
      description: 'Current status of the Berthing in its lifetime, from request to authorization and completion. Enum:''ACCEPTED, AUTHORIZED, CANCELLED, COMPLETED, DENIED, INITIATED, REQUESTED, REJECTED, INVOICING, INVOICED''. [EMSWe: DE-019-07] [EDI: BGM-1225] [S211: serviceState: timeSequence:VESSEL] '    
      enum:    
        - ACCEPTED    
        - AUTHORIZED    
        - CANCELLED    
        - COMPLETED    
        - DENIED    
        - INITIATED    
        - REQUESTED    
        - REJECTED    
        - INVOICING    
        - INVOICED    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    stopRank:    
      description: Rank or Number of this stop in the PortCall activity ordered by arrival time in the sequence of stops (berthing/anchor area)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    terminal:    
      description: Common name of the Terminal    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be Berth    
      enum:    
        - Berth    
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
    - portCallRef    
    - stopRank    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2024 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/Berth/LICENSE.md    
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
#### 泊位 NGSI-v2 关键值示例  
下面是一个以 JSON-LD 格式作为键值的泊位示例。当使用 "options=keyValues "时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "02ce3860-3126-42af-8ac7-c2a661134130",  
  "type": "Berth",  
  "mrn": "urn:mrn:eshuv:portcalls:berth:id:18013",  
  "portCode": "ESHUV",  
  "year": 2023,  
  "portCallNumber": "ESHUV202300123",  
  "portCallRef": "urn:mrn:eshuv:portcalls:portcall:2023:id:941",  
  "stopRank": 2,  
  "terminal": "Muelle Levante",  
  "berthCode": "urn:mrn:eshuv:portcalls:berth:code:10",  
  "berthName": "Levante comercial",  
  "gln": 84332157000139,  
  "firstBollard": "N03",  
  "lastBollard": "N12",  
  "status": "AUTHORIZED",  
  "requestedAt": "2023-01-01T07:30:00",  
  "authorizedAt": "2023-01-01T07:30:00",  
  "berthingTypeCode": "AB1",  
  "mooringLines": 12,  
  "activityCode": "ZOP",  
  "etaBerth": "2023-01-01T07:30:00",  
  "rtaBerth": "2023-01-01T07:30:00",  
  "ptaBerth": "2023-01-01T07:30:00",  
  "ataBerth": "2023-01-01T07:30:00",  
  "etdBerth": "2023-01-01T07:30:00",  
  "rtdBerth": "2023-01-01T07:30:00",  
  "ptdBerth": "2023-01-01T07:30:00",  
  "atdBerth": "2023-01-01T07:30:00",  
  "arrivalDraught": 12.3,  
  "departureDraught": 9.5,  
  "remarks": "FONDEA PARA SUMINISTRO DE COMBUSTIBLE POR GABARRA",  
  "authorizationRemarks": "authorized after departure of ship XX",  
  "agentName": "Acme Huelva S.L.",  
  "agentLegalCode": "A-98345678"  
}  
```  
</details>  
#### 泊位 NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的泊位示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "02ce3860-3126-42af-8ac7-c2a661134130",  
  "type": "Berth",  
  "mrn": {  
    "type": "string",  
    "value": "urn:mrn:eshuv:portcalls:berth:id:18013"  
  },  
  "gln": {  
    "type": "number",  
    "value": 84332157000139  
  },  
  "portCode": {  
    "type": "string",  
    "value": "ESHUV"  
  },  
  "year": {  
    "type": "number",  
    "value": 2023  
  },  
  "portCallNumber": {  
    "type": "string",  
    "value": "ESHUV202300123"  
  },  
  "portCallRef": {  
    "type": "string",  
    "value": "urn:mrn:eshuv:portcalls:portcall:2023:id:941"  
  },  
  "stopRank": {  
    "type": "number",  
    "value": 2  
  },  
  "terminal": {  
    "type": "string",  
    "value": "Muelle Levante"  
  },  
  "berthCode": {  
    "type": "string",  
    "value": "urn:mrn:eshuv:portcalls:berth:code:10"  
  },  
  "berthName": {  
    "type": "string",  
    "value": "Levante comercial"  
  },  
  "firstBollard": {  
    "type": "string",  
    "value": "N03"  
  },  
  "lastBollard": {  
    "type": "string",  
    "value": "N12"  
  },  
  "status": {  
    "type": "string",  
    "value": "AUTHORIZED"  
  },  
  "requestedAt": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:30:00"  
  },  
  "authorizedAt": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:30:00"  
  },  
  "berthingTypeCode": {  
    "type": "string",  
    "value": "AB1"  
  },  
  "mooringLines": {  
    "type": "number",  
    "value": 12  
  },  
  "activityCode": {  
    "type": "string",  
    "value": "ZOP"  
  },  
  "etaBerth": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:30:00"  
  },  
  "rtaBerth": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:30:00"  
  },  
  "ptaBerth": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:30:00"  
  },  
  "ataBerth": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:30:00"  
  },  
  "etdBerth": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:30:00"  
  },  
  "rtdBerth": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:30:00"  
  },  
  "ptdBerth": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:30:00"  
  },  
  "atdBerth": {  
    "type": "Date-Time",  
    "value": "2023-01-01T07:30:00"  
  },  
  "arrivalDraught": {  
    "type": "number",  
    "value": 12.3  
  },  
  "departureDraught": {  
    "type": "number",  
    "value": 9.5  
  },  
  "remarks": {  
    "type": "string",  
    "value": "FONDEA PARA SUMINISTRO DE COMBUSTIBLE POR GABARRA"  
  },  
  "authorizationRemarks": {  
    "type": "string",  
    "value": "authorized after departure of ship XX"  
  },  
  "agentName": {  
    "type": "string",  
    "value": "Acme Huelva S.L."  
  },  
  "agentLegalCode": {  
    "type": "string",  
    "value": "A-98345678"  
  }  
}  
```  
</details>  
#### 泊位 NGSI-LD 键值示例  
下面是一个以 JSON-LD 格式作为键值的泊位示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "02ce3860-3126-42af-8ac7-c2a661134130",  
  "type": "Berth",  
  "mrn": "urn:mrn:eshuv:portcalls:berth:id:18013",  
  "gln": 1234567890123,  
  "portCode": "ESHUV",  
  "year": 2023,  
  "portCallNumber": "ESHUV202300123",  
  "portCallRef": "urn:mrn:eshuv:portcalls:portcall:2023:id:941",  
  "stopRank": 2,  
  "terminal": "Muelle Levante",  
  "berthCode": "urn:mrn:eshuv:portcalls:berth:code:10",  
  "berthName": "Levante comercial",  
  "firstBollard": "N03",  
  "lastBollard": "N12",  
  "status": "AUTHORIZED",  
  "requestedAt": "2023-01-01T07:30:00",  
  "authorizedAt": "2023-01-01T07:30:00",  
  "berthingTypeCode": "AB1",  
  "mooringLines": 12,  
  "activityCode": "ZOP",  
  "etaBerth": "2023-01-01T07:30:00",  
  "rtaBerth": "2023-01-01T07:30:00",  
  "ptaBerth": "2023-01-01T07:30:00",  
  "ataBerth": "2023-01-01T07:30:00",  
  "etdBerth": "2023-01-01T07:30:00",  
  "rtdBerth": "2023-01-01T07:30:00",  
  "ptdBerth": "2023-01-01T07:30:00",  
  "atdBerth": "2023-01-01T07:30:00",  
  "arrivalDraught": 12.3,  
  "departureDraught": 9.5,  
  "remarks": "FONDEA PARA SUMINISTRO DE COMBUSTIBLE POR GABARRA",  
  "authorizationRemarks": "authorized after departure of ship XX",  
  "agentName": "Acme Huelva S.L.",  
  "agentLegalCode": "A-98345678",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### 泊位 NGSI-LD 归一化示例  
下面是一个规范化 JSON-LD 格式的泊位示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "02ce3860-3126-42af-8ac7-c2a661134130",  
  "type": "Berth",  
  "mrn": {  
    "type": "Property",  
    "value": "urn:mrn:eshuv:portcalls:berth:id:18013"  
  },  
  "gln": {  
    "type": "Property",  
    "value": 84332157000139  
  },  
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
    "object": "urn:mrn:eshuv:portcalls:portcall:2023:id:941"  
  },  
  "stopRank": {  
    "type": "Property",  
    "value": 2  
  },  
  "terminal": {  
    "type": "Property",  
    "value": "Muelle Levante"  
  },  
  "berthCode": {  
    "type": "Property",  
    "value": "urn:mrn:eshuv:portcalls:berth:code:10"  
  },  
  "berthName": {  
    "type": "Property",  
    "value": "Levante comercial"  
  },  
  "firstBollard": {  
    "type": "Property",  
    "value": "N03"  
  },  
  "lastBollard": {  
    "type": "Property",  
    "value": "N12"  
  },  
  "status": {  
    "type": "Property",  
    "value": "AUTHORIZED"  
  },  
  "requestedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:30:00"  
    }  
  },  
  "authorizedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:30:00"  
    }  
  },  
  "berthingTypeCode": {  
    "type": "Property",  
    "value": "AB1"  
  },  
  "mooringLines": {  
    "type": "Property",  
    "value": 12  
  },  
  "activityCode": {  
    "type": "Property",  
    "value": "ZOP"  
  },  
  "etaBerth": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:30:00"  
    }  
  },  
  "rtaBerth": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:30:00"  
    }  
  },  
  "ptaBerth": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:30:00"  
    }  
  },  
  "ataBerth": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:30:00"  
    }  
  },  
  "etdBerth": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:30:00"  
    }  
  },  
  "rtdBerth": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:30:00"  
    }  
  },  
  "ptdBerth": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:30:00"  
    }  
  },  
  "atdBerth": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-01T07:30:00"  
    }  
  },  
  "arrivalDraught": {  
    "type": "Property",  
    "value": 12.3  
  },  
  "departureDraught": {  
    "type": "Property",  
    "value": 9.5  
  },  
  "remarks": {  
    "type": "Property",  
    "value": "FONDEA PARA SUMINISTRO DE COMBUSTIBLE POR GABARRA"  
  },  
  "authorizationRemarks": {  
    "type": "Property",  
    "value": "authorized after departure of ship XX"  
  },  
  "agentName": {  
    "type": "Property",  
    "value": "Acme Huelva S.L."  
  },  
  "agentLegalCode": {  
    "type": "Property",  
    "value": "A-98345678"  
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
