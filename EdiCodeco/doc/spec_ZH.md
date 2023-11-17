<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：EdiCodeco    
============<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/EdiCodeco/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全球描述：**码头、仓库等确认内陆承运人（公路、铁路或驳船）已交付或提取指定集装箱的报文。该报文也可用于报告码头内部集装箱移动情况（不包括装船和卸船），以及报告集装箱状态的变化，但集装箱并未实际移动。见[UN/EDIFACT - CODECO](https://service.unece.org/trade/untdid/d19a/trmd/codeco_c.htm)**。    
版本： 0.1.0    
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
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `ata[date-time]`: 到达或离开航站楼的实际时间。(ISO 8601 UTC 格式）。见 [UNTDID - D.95B - Segment DTM - C507 (2380)](https://service.unece.org/trade/untdid/d95b/uncl/uncl2380.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `bookingCode[string]`: 预订参考。见 [UNTDID - D.95B - Segment RFF - C506 (1154)](https://service.unece.org/trade/untdid/d95b/uncl/uncl1154.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerCarrierIdentification[string]`: 识别交易中一方的代码。见 [UNTDID - D.95B - Segment NAD - C082 (3039)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3039.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerClass[string]`: 集装箱类别（表示与设备相关的操作）。枚举："大陆、出口、进口、留在船上、转移、转运"。参见 [UNTDID - D.95B - Segment EQD - 8249]（https://service.unece.org/trade/untdid/d95b/uncl/uncl8249.htm）。  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerIdentification[string]`: 容器标识。见 [UNTDID - D.95B - Segment EQD - C237 (8260)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8260.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerIsoCode[string]`: 设备尺寸和类型的编码描述。罐式集装箱 30 英尺,罐式集装箱 40 英尺,集装箱 IC 20 英尺,集装箱 IC 30 英尺,集装箱 IC 40 英尺,冷藏箱 20 英尺,冷藏箱 30 英尺,冷藏箱 40 英尺,罐式集装箱 IC 20 英尺,罐式集装箱 IC 30 英尺,罐式集装箱 IC 40 英尺,冷藏箱 IC 20 英尺,冷藏箱 IC 40 英尺,活动箱：长 < 6,15米,可移动箱子6,15米 < 长 < 7,82米,可移动箱子7,82米 < 长 < 9,15米,可移动箱体9.15米 < 长 < 10.90米,活动箱子10,90米 < 长 < 13,75米,Totebin,温控集装箱20英尺,温控集装箱40英尺'。参见 [UNTDID - D.95B - Segment EQD - C224 (8155)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8155.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerSeal[string]`: 贴在容器上的定制封条或其他封条的编号。见 [UNTDID - D.95B - Segment SEL - 9308](https://service.unece.org/trade/untdid/d95b/uncl/uncl9308.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `containerWeight[number]`: 集装箱重量。见 [UNTDID - D.95B - Segment MEA - C174 (6314)](https://service.unece.org/trade/untdid/d95b/uncl/uncl6314.htm)  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `destination[string]`: 集装箱的最终目的地（UN/LOCODE：联合国贸易和运输地点代码）。见 [UNTDID - D.95B - Segment LOC - C517 (3225)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm) 和 [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)  . Model: [https://schema.org/Text](https://schema.org/Text)- `destinationTransportType[string]`: 运输方法代码（UN/ECE）。见 [UNTDID - D.95B - Segment TDT - C220 (8067)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8067.htm) 和 [UN/ECE - Rec 19](https://unece.org/trade/uncefact/cl-recommendations)。  . Model: [https://schema.org/Text](https://schema.org/Text)- `dischargingPort[string]`: 集装箱卸货港（UN/LOCODE：联合国贸易和运输地点代码）。见 [UNTDID - D.95B - Segment LOC - C517 (3225)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm) 和 [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)  . Model: [https://schema.org/Text](https://schema.org/Text)- `fileName[string]`: EDI Codeco 报文的文件名  . Model: [https://schema.org/Text](https://schema.org/Text)- `functionCode[string]`: 表示信息功能的代码。Enum='取消、添加、删除、更改、替换、确认、重复、状态、原始、未找到、回复、未处理、请求、预先通知、提醒、建议、取消，将重新签发、重新签发、卖方发起的更改、仅替换标题部分、仅替换项目详情和摘要、最终传送、交易搁置、交货指示、预测、交货指示和预测、未接受、接受，标题部分有修改、接受但无修改、接受，在详细部分有修改，复制，批准，标题部分的更改，接受并有修改，重新传送，详细部分的更改，借方逆转，贷方逆转，取消逆转，删除请求，完成/关闭订单，通过特定方式确认，附加传送，无保留地接受，有保留地接受，临时，确定，接受，内容被拒绝，解决争议，撤回，授权，建议修改，测试"。见 [UNTDID - D.95B - BGM - 1225](https://service.unece.org/trade/untdid/d95b/uncl/uncl1225.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: 实体的唯一标识符  - `isContainerEmpty[boolean]`: 容器是满的还是空的信息。参见 [UNTDID - D.95B - Segment EQD - 8169](https://service.unece.org/trade/untdid/d95b/uncl/uncl8169.htm)。  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `loadingPort[string]`: 集装箱装载的港口（UN/LOCODE：联合国贸易和运输地点代码）。见 [UNTDID - D.95B - Segment LOC - C517 (3225)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm) 和 [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `messageRaw[string]`: EDI Codeco 的原始信息  . Model: [https://schema.org/Text](https://schema.org/Text)- `messageVersion[string]`: 信息类型的版本。见 [UNTDID - D.95B - UNH - S009 (0052)](https://service.unece.org/trade/untdid/d95b/trmd/codeco_d.htm#DSGI)  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: 该项目的名称  - `operationType[string]`: 标识位置功能的代码。枚举：交货地点、付款地点、收货地点、出发地点、交货地点、目的地、装货地点/港口、验收地点、卸货地点/港口、卸货港、转运地点、货物地点、责任转移地点、所有权转移地点、过境地点、仓库、工厂、货物最终目的地、销售地点、清关海关、放行港、入境港、国家、城市、原产国、货物目的地国、火车站、来源国、建筑物、收费段起点、卸货港、装货港、出口/发货国、最终目的地国、最后发货国、第一目的地国、生产国、贸易国、入境海关办事处、出境海关办事处、海关检查地点、文件认证地点、目的地（过境）海关办事处、发货地区、转运国、转运海关、无效转运担保国、目的地（转运）国、应收费用和运费、制造部门、应付费用和运费、收费段结束、付款地点、全程装卸、抵达地点、下一停靠港、随车港口、第一个可选卸货地点、特快火车站、混合货物火车站、第二个可选卸货地点、下一个非卸货挂靠港、第三个可选卸货地、重新集结点、第四个可选卸货地、提单放行处、不包括此地的转运、仅限于此地的转运、原装货港、第一个挂靠港--非卸货、第一个挂靠港--卸货、首次入境地/港、发货地、第五个可选卸货地、预运港、交货地（通过随运）、运输合同接收地、运输合同目的地、有效过境担保国、运输工具初次到达地/港、收货地、登记地、已发生或必须发生特殊处理的地点/位置、单证签发地、路线、额外费用申请站、单证存放地、可选卸货地、空设备发运地、空设备返回地、入仓地/港、首次销售国、购买国、转运地、卸货地、消费地、原产地、拼装地、费率组合点、延期交货决定地、装货地/地点、发货海关、发货国、出口海关、出口保税区、出口/发货地区、离境海关、过境担保海关、转运国、销售国、目的地海关、装车火车站、装卸区、运输工具最后停靠地点/港口、前海关手续办理国、前海关申报登记处、参与发运人所在地、工资协商区、运输工具最终目的地、空设备装载地点、空设备卸货地点、交货地区、石油仓库、入境地点（海关）、生活动物看护地点、重新结冰地点、称重地点、卸货场、购物站、装货码头、港口连接、到期地点、交涉地点、应付索赔地点、可提供跟单信用证的地点、积载单元、运往地点、装船/发货/起运地、专用箱、下一个卸货港、停靠港、租用地点/地点、非租用地点/地点、其他承运人码头、增值税（VAT）管辖国、联系地点、额外国内目的地、国外停靠港、维修地点 "相互定义"。见 [UNTDID - D.95B - Segment TDT - LOC - 3227](https://service.unece.org/trade/untdid/d95b/uncl/uncl3227.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `originTransportType[string]`: 运输方法代码（UN/ECE）。见 [UNTDID - D.95B - Segment TDT - C220 (8067)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8067.htm) 和 [UN/ECE - Rec 19](https://unece.org/trade/uncefact/cl-recommendations)。  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `receiverIdentification[string]`: 交换接收方标识。见 [UN/EDIFACT - S003](https://unece.org/trade/uncefact/unedifact/part-4-Annex-B)。  . Model: [https://schema.org/Text](https://schema.org/Text)- `release[string]`: 当前版本号内的版本号。参见 [UNTDID - D.95B - UNH - S009 (0054)](https://service.unece.org/trade/untdid/d95b/trmd/codeco_d.htm#DSGI)  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `senderIdentification[string]`: 交换发件人标识。见 [UN/EDIFACT - S002](https://unece.org/trade/uncefact/unedifact/part-4-Annex-B)。  . Model: [https://schema.org/Text](https://schema.org/Text)- `sentAt[date-time]`: 以 ISO 8601 UTC 格式表示的报文发送日期和时间。见 [UN/EDIFACT - S004](https://unece.org/trade/uncefact/unedifact/part-4-Annex-B)。  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `travelReference[string]`: 转运编号。见 [UNTDID - D.95B - Segment TDT - 8028](https://service.unece.org/trade/untdid/d95b/uncl/uncl8028.htm)。  . Model: [https://schema.org/Text](https://schema.org/Text)- `truckLicenseCode[string]`: 卡车车牌。见 [UNTDID - D.95B - Segment TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI 实体类型。必须是 EdiCodeco  - `vesselCallSign[string]`: 海事呼号是分配给船只作为唯一标识符的呼号。见 [UNTDID - D.95B - Segment TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselCarrier[string]`: 船舶承运人标识（承担或安排指定地点之间货物运输的一方的标识）。见 [UNTDID - D.95B - Segment TDT - C040 (3127)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3127.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselImo[number]`: 国际海事组织编号（全球永久 UID）。参见 [UNTDID - D.95B - Segment TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)  . Model: [https://schema.org/Number](https://schema.org/Number)- `vesselMmsi[number]`: Marine Mobile Service Identity Number（临时分配的 UID，由该对象当前的船旗国颁发）。见 [UNTDID - D.95B - Segment TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)  . Model: [https://schema.org/Number](https://schema.org/Number)- `vesselName[string]`: 船只名称。见 [UNTDID - D.95B - Segment TDT - C222 (8212)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8212.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `vesselVoyage[string]`: 船舶航次参考编号。见 [UNTDID - D.95B - Segment RFF - C506 (1154)](https://service.unece.org/trade/untdid/d95b/uncl/uncl1154.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
所需属性    
- `containerIdentification`  - `id`  - `type`  - `vesselImo`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 属性的数据模型描述    
按字母顺序排列（点击查看详情）    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
EdiCodeco:      
  description: 'A message by which a terminal, depot, etc. confirms that the containers specified have been delivered or picked up by the inland carrier (road, rail or barge). This message can also be used to report internal terminal container movements (excluding loading and discharging the vessel) and to report the change in status of container(s) without those containers having physically been moved. See [UN/EDIFACT - CODECO](https://service.unece.org/trade/untdid/d19a/trmd/codeco_c.htm)'      
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
    ata:      
      description: 'Actual time of arrival or departure to/from Terminal. (ISO 8601 UTC format). See [UNTDID - D.95B - Segment DTM - C507 (2380)](https://service.unece.org/trade/untdid/d95b/uncl/uncl2380.htm)'      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    bookingCode:      
      description: 'Booking Reference. See [UNTDID - D.95B - Segment RFF - C506 (1154)](https://service.unece.org/trade/untdid/d95b/uncl/uncl1154.htm)'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    containerCarrierIdentification:      
      description: 'Code identifying a party involved in a transaction. See [UNTDID - D.95B - Segment NAD - C082 (3039)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3039.htm)'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    containerClass:      
      description: 'Container class (indication of the action related to the equipment). Enum: ''Continental, Export, Import,Remain on board,Shifter,Transhipment''. See [UNTDID - D.95B - Segment EQD - 8249](https://service.unece.org/trade/untdid/d95b/uncl/uncl8249.htm)'      
      enum:      
        - Continental      
        - Export      
        - Import      
        - Remain on board      
        - Shifter      
        - Transhipment      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    containerIdentification:      
      description: 'Containter identification. See [UNTDID - D.95B - Segment EQD - C237 (8260)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8260.htm)'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    containerIsoCode:      
      description: 'Coded description of the size and type of equipment. Enum ''Dime coated tank,Epoxy coated tank,IMO1,IMO2,IMO3,Pressurized tank,Refrigerated tank,Semi-refrigerated,Stainless steel tank,Nonworking reefer container 40 ft,Box pallet,Europallet,Scandinavian pallet,Trailer,Nonworking reefer container 20 ft,Exchangeable pallet,Semi-trailer,Tank container 20 ft.,Tank container 30 ft.,Tank container 40 ft.,Container IC 20 ft.,Container IC 30 ft.,Container IC 40 ft.,Refrigerator tank 20 ft.,Refrigerator tank 30 ft.,Refrigerator tank 40 ft.,Tank container IC 20 ft.,Tank container IC 30 ft.,Tank container IC 40 ft.,Refrigerator tank IC 20 ft.,Refrigerator tank IC 40 ft.,Movable case: L < 6,15m,Movable case: 6,15m < L < 7,82m,Movable case: 7,82m < L < 9,15m,Movable case: 9,15m < L < 10,90m,Movable case: 10,90m < L < 13,75m,Totebin,Temperature controlled container 20 ft,Temperature controlled container 40 ft''. See [UNTDID - D.95B - Segment EQD - C224 (8155)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8155.htm)'      
      enum:      
        - Dime coated tank      
        - Epoxy coated tank      
        - IMO1      
        - IMO2      
        - IMO3      
        - Pressurized tank      
        - Refrigerated tank      
        - Semi-refrigerated      
        - Stainless steel tank      
        - Nonworking reefer container 40 ft      
        - Box pallet      
        - Europallet      
        - Scandinavian pallet      
        - Trailer      
        - Nonworking reefer container 20 ft      
        - Exchangeable pallet      
        - Semi-trailer      
        - Tank container 20 ft.      
        - Tank container 30 ft.      
        - Tank container 40 ft.      
        - Container IC 20 ft.      
        - Container IC 30 ft.      
        - Container IC 40 ft.      
        - Refrigerator tank 20 ft.      
        - Refrigerator tank 30 ft.      
        - Refrigerator tank 40 ft.      
        - Tank container IC 20 ft.      
        - Tank container IC 30 ft.      
        - Tank container IC 40 ft.      
        - Refrigerator tank IC 20 ft.      
        - Refrigerator tank IC 40 ft.      
        - 'Movable case: L < 6,15m'      
        - 'Movable case: 6,15m < L < 7,82m'      
        - 'Movable case: 7,82m < L < 9,15m'      
        - 'Movable case: 9,15m < L < 10,90m'      
        - 'Movable case: 10,90m < L < 13,75m'      
        - Totebin      
        - Temperature controlled container 20 ft      
        - Temperature controlled container 40 ft      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    containerSeal:      
      description: 'The number of a custom seal or another seal affixed to the containers. See [UNTDID - D.95B - Segment SEL - 9308](https://service.unece.org/trade/untdid/d95b/uncl/uncl9308.htm)'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    containerWeight:      
      description: 'Weight of the container. See [UNTDID - D.95B - Segment MEA - C174 (6314)](https://service.unece.org/trade/untdid/d95b/uncl/uncl6314.htm)'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: ' KGM'      
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
    destination:      
      description: 'Final destination of the container (UN/LOCODE: United Nations Code for Trade and Transport Locations). See [UNTDID - D.95B - Segment LOC - C517 (3225)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm) and [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    destinationTransportType:      
      description: 'Method of transport code (UN/ECE). See [UNTDID - D.95B - Segment TDT - C220 (8067)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8067.htm) and [UN/ECE - Rec 19](https://unece.org/trade/uncefact/cl-recommendations)'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    dischargingPort:      
      description: 'Port where the container is discharged (UN/LOCODE: United Nations Code for Trade and Transport Locations). See [UNTDID - D.95B - Segment LOC - C517 (3225)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm) and [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    fileName:      
      description: File name of EDI Codeco message      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    functionCode:      
      description: 'Code indicating the function of the message. Enum=''Cancellation, Addition, Deletion, Change, Replace, Confirmation, Duplicate, Status, Original, Not found, Response, Not processed, Request, Advance notification, Reminder, Proposal, Cancel, to be reissued, Reissue, Seller initiated change, Replace heading section only, Replace item detail and summary only, Final transmission, Transaction on hold, Delivery instruction, Forecast, Delivery instruction and forecast, Not accepted, Accepted, with amendment in heading section, Accepted without amendment, Accepted, with amendment in detail section, Copy, Approval, Change in heading section, Accepted with amendment, Retransmission, Change in detail section, Reversal of a debit, Reversal of a credit, Reversal for cancellation, Request for deletion, Finishing/closing order, Confirmation via specific means, Additional transmission, Accepted without reserves, Accepted with reserves, Provisional, Definitive, Accepted, contents rejected, Settled dispute, Withdraw, Authorisation, Proposed amendment, Test''. See [UNTDID - D.95B - BGM - 1225](https://service.unece.org/trade/untdid/d95b/uncl/uncl1225.htm)'      
      enum:      
        - Cancellation      
        - Addition      
        - Deletion      
        - Change      
        - Replace      
        - Confirmation      
        - Duplicate      
        - Status      
        - Original      
        - Not found      
        - Response      
        - Not processed      
        - Request      
        - Advance notification      
        - Reminder      
        - Proposal      
        - 'Cancel, to be reissued'      
        - Reissue      
        - Seller initiated change      
        - Replace heading section only      
        - Replace item detail and summary only      
        - Final transmission      
        - Transaction on hold      
        - Delivery instruction      
        - Forecast      
        - Delivery instruction and forecast      
        - Not accepted      
        - 'Accepted, with amendment in heading section'      
        - Accepted without amendment      
        - 'Accepted, with amendment in detail section'      
        - Copy      
        - Approval      
        - Change in heading section      
        - Accepted with amendment      
        - Retransmission      
        - Change in detail section      
        - Reversal of a debit      
        - Reversal of a credit      
        - Reversal for cancellation      
        - Request for deletion      
        - Finishing/closing order      
        - Confirmation via specific means      
        - Additional transmission      
        - Accepted without reserves      
        - Accepted with reserves      
        - Provisional      
        - Definitive      
        - 'Accepted, contents rejected'      
        - Settled dispute      
        - Withdraw      
        - Authorisation      
        - Proposed amendment      
        - Test      
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
        type: Property      
    isContainerEmpty:      
      description: 'Information about if the container is full or empty. See [UNTDID - D.95B - Segment EQD - 8169](https://service.unece.org/trade/untdid/d95b/uncl/uncl8169.htm)'      
      type: boolean      
      x-ngsi:      
        model: https://schema.org/Boolean      
        type: Property      
    loadingPort:      
      description: 'Port where the container is loaded (UN/LOCODE: United Nations Code for Trade and Transport Locations). See [UNTDID - D.95B - Segment LOC - C517 (3225)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm) and [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)'      
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
    messageRaw:      
      description: Raw message of the EDI Codeco      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    messageVersion:      
      description: "Version of the message type. See [UNTDID - D.95B - UNH - S009 (0052)](https://service.unece.org/trade/untdid/d95b/trmd/codeco_d.htm#DSGI)"      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    operationType:      
      description: 'Code identifying the function of a location. Enum: ''Place of terms of delivery, Payment place, Goods receipt place, Place of departure, Place of delivery, Place of destination, Place/port of loading, Place of acceptance, Place/port of discharge, Port of discharge, Place of transhipment, Location of goods, Place of transfer responsibility, Place of transfer of ownership, Border crossing place, Warehouse, Factory/plant, Place of ultimate destination of goods, Terms of sale place, Customs office of clearance, Port of release, Port of entry, Country, City, Country of origin, Country of destination of goods, Railway station, Country of source, Building, Beginning of chargeable section, Baseport of discharge, Baseport of loading, Country of exportation/despatch, Country of ultimate destination, Country of last consignment, Country of first destination, Country of production, Country of trading, Customs office of entry, Customs office of exit, Place of Customs examination, Place of authentication of document, Customs office of destination (transit), Region of despatch, Region of destination, Region of production, Country of transit, Customs office of transit, Country of invalid transit guarantee, Country of destination (transit), Charge and freight due from, Manufacturing department, Charges and freight payable to, End of chargeable section, Place of payment, Full track loading or unloading, Place of arrival, Next port of call, On-carriage port, First optional place of discharge, Express railway station, Mixed cargo railway station, Second optional place of discharge, Next non-discharge port of call, Third optional place of discharge, Reconsolidation point, Fourth optional place of discharge, Bill of lading release office, Transhipment excluding this place, Transhipment limited to this place, Original port of loading, First port of call - non-discharging, First port of call - discharging, Place/port of first entry, Place of despatch, Fifth optional place of discharge, Pre-carriage port, Place of delivery (by on carriage), Transport contract place of acceptance, Transport contract place of destination, Country of valid transit guarantee, Place/port of conveyance initial arrival, Place of receipt, Place of registration, Place/location where special treatments have happened or must happen, Place of document issue, Routing, Station of application of additional costs, Place of lodgement of documents, Optional place of discharge, Place of empty equipment despatch, Place of empty equipment return, Place/port of warehouse entry, Country of first sale, Country of purchase, Place of transfer, Place of deconsolidation, Place of consumption, Region of origin, Place of consolidation, Rate combination point, Place of prolongation decision of delivery delay, Recharging place/location, Customs office of despatch, Country of despatch, Customs office of export, Free zone of export, Region of export/despatch, Customs office of departure, Customs office of transit guarantee, Country of transhipment, Country of sale, Customs office of destination, Wagon-load railway station, Siding, Last place/port of call of conveyance, Country of previous Customs procedure, Customs office of registration of previous Customs declaration, Participant sender location, Wage negotiation district, Place of ultimate destination of conveyance, Place of loading of empty equipment, Place of discharge of empty equipment, Region of delivery, Petroleum warehouse, Place of entry (Customs), Living animals care place, Re-icing place, Weighting place, Marshalling yard, Shopping station, Loading dock, Port connection, Place of expiry, Place of negotiation, Claims payable place, Documentary credit available in, Stowage cell, For transportation to, Loading on board/despatch/taking in charge at/from, Private box, Next port of discharge, Port of call, Place/location of on-hire, Place/location of off-hire, Other carriers terminal, Country of Value Added Tax (VAT) jurisdiction, Contact location, Additional internal destination, Foreign port of call, Maintenance location      
        Mutually defined''. See [UNTDID - D.95B - Segment TDT - LOC - 3227](https://service.unece.org/trade/untdid/d95b/uncl/uncl3227.htm)'      
      enum:      
        - Place of terms of delivery      
        - Payment place      
        - Goods receipt place      
        - Place of departure      
        - Place of delivery      
        - Place of destination      
        - Place/port of loading      
        - Place of acceptance      
        - Place/port of discharge      
        - Port of discharge      
        - Place of transhipment      
        - Location of goods      
        - Place of transfer responsibility      
        - Place of transfer of ownership      
        - Border crossing place      
        - Warehouse      
        - Factory/plant      
        - Place of ultimate destination of goods      
        - Terms of sale place      
        - Customs office of clearance      
        - Port of release      
        - Port of entry      
        - Country      
        - City      
        - Country of origin      
        - Country of destination of goods      
        - Railway station      
        - Country of source      
        - Building      
        - Beginning of chargeable section      
        - Baseport of discharge      
        - Baseport of loading      
        - Country of exportation/despatch      
        - Country of ultimate destination      
        - Country of last consignment      
        - Country of first destination      
        - Country of production      
        - Country of trading      
        - Customs office of entry      
        - Customs office of exit      
        - Place of Customs examination      
        - Place of authentication of document      
        - Customs office of destination (transit)      
        - Region of despatch      
        - Region of destination      
        - Region of production      
        - Country of transit      
        - Customs office of transit      
        - Country of invalid transit guarantee      
        - Country of destination (transit)      
        - Charge and freight due from      
        - Manufacturing department      
        - Charges and freight payable to      
        - End of chargeable section      
        - Place of payment      
        - Full track loading or unloading      
        - Place of arrival      
        - Next port of call      
        - On-carriage port      
        - First optional place of discharge      
        - Express railway station      
        - Mixed cargo railway station      
        - Second optional place of discharge      
        - Next non-discharge port of call      
        - Third optional place of discharge      
        - Reconsolidation point      
        - Fourth optional place of discharge      
        - Bill of lading release office      
        - Transhipment excluding this place      
        - Transhipment limited to this place      
        - Original port of loading      
        - First port of call - non-discharging      
        - First port of call - discharging      
        - Place/port of first entry      
        - Place of despatch      
        - Fifth optional place of discharge      
        - Pre-carriage port      
        - Place of delivery (by on carriage)      
        - Transport contract place of acceptance      
        - Transport contract place of destination      
        - Country of valid transit guarantee      
        - Place/port of conveyance initial arrival      
        - Place of receipt      
        - Place of registration      
        - Place/location where special treatments have happened or must happen      
        - Place of document issue      
        - Routing      
        - Station of application of additional costs      
        - Place of lodgement of documents      
        - Optional place of discharge      
        - Place of empty equipment despatch      
        - Place of empty equipment return      
        - Place/port of warehouse entry      
        - Country of first sale      
        - Country of purchase      
        - Place of transfer      
        - Place of deconsolidation      
        - Place of consumption      
        - Region of origin      
        - Place of consolidation      
        - Rate combination point      
        - Place of prolongation decision of delivery delay      
        - Recharging place/location      
        - Customs office of despatch      
        - Country of despatch      
        - Customs office of export      
        - Free zone of export      
        - Region of export/despatch      
        - Customs office of departure      
        - Customs office of transit guarantee      
        - Country of transhipment      
        - Country of sale      
        - Customs office of destination      
        - Wagon-load railway station      
        - Siding      
        - Last place/port of call of conveyance      
        - Country of previous Customs procedure      
        - Customs office of registration of previous Customs declaration      
        - Participant sender location      
        - Wage negotiation district      
        - Place of ultimate destination of conveyance      
        - Place of loading of empty equipment      
        - Place of discharge of empty equipment      
        - Region of delivery      
        - Petroleum warehouse      
        - Place of entry (Customs)      
        - Living animals care place      
        - Re-icing place      
        - Weighting place      
        - Marshalling yard      
        - Shopping station      
        - Loading dock      
        - Port connection      
        - Place of expiry      
        - Place of negotiation      
        - Claims payable place      
        - Documentary credit available in      
        - Stowage cell      
        - For transportation to      
        - Loading on board/despatch/taking in charge at/from      
        - Private box      
        - Next port of discharge      
        - Port of call      
        - Place/location of on-hire      
        - Place/location of off-hire      
        - Other carriers terminal      
        - Country of Value Added Tax (VAT) jurisdiction      
        - Contact location      
        - Additional internal destination      
        - Foreign port of call      
        - Maintenance location      
        - Mutually defined      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    originTransportType:      
      description: 'Method of transport code (UN/ECE). See [UNTDID - D.95B - Segment TDT - C220 (8067)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8067.htm) and [UN/ECE - Rec 19](https://unece.org/trade/uncefact/cl-recommendations)'      
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
    receiverIdentification:      
      description: 'Interchange Recipient Identification. See [UN/EDIFACT - S003](https://unece.org/trade/uncefact/unedifact/part-4-Annex-B)'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    release:      
      description: "Release number within current version number. See [UNTDID - D.95B - UNH - S009 (0054)](https://service.unece.org/trade/untdid/d95b/trmd/codeco_d.htm#DSGI)"      
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
    senderIdentification:      
      description: 'Interchange Sender Identification. See [UN/EDIFACT - S002](https://unece.org/trade/uncefact/unedifact/part-4-Annex-B)'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    sentAt:      
      description: 'Date and time of message has been sent represented by an ISO 8601 UTC format. See [UN/EDIFACT - S004](https://unece.org/trade/uncefact/unedifact/part-4-Annex-B)'      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    travelReference:      
      description: 'Conveyance reference number. See [UNTDID - D.95B - Segment TDT - 8028](https://service.unece.org/trade/untdid/d95b/uncl/uncl8028.htm)'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    truckLicenseCode:      
      description: 'License Plate of the Truck. See [UNTDID - D.95B - Segment TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    type:      
      description: NGSI Entity type. It has to be EdiCodeco      
      enum:      
        - EdiCodeco      
      type: string      
      x-ngsi:      
        type: Property      
    vesselCallSign:      
      description: 'Maritime call signs are call signs assigned as unique identifiers to vessels. See [UNTDID - D.95B - Segment TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    vesselCarrier:      
      description: 'Vessel carrier Identification (identification of party undertaking or arranging transport of goods between named points). See [UNTDID - D.95B - Segment TDT - C040 (3127)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3127.htm)'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    vesselImo:      
      description: 'International Maritime Organization Number (a global forever UID). See [UNTDID - D.95B - Segment TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    vesselMmsi:      
      description: 'Marine Mobile Service Identity Number (a temporarily assigned UID, issued by that object''s current flag state). See [UNTDID - D.95B - Segment TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    vesselName:      
      description: 'Vessel Name. See [UNTDID - D.95B - Segment TDT - C222 (8212)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8212.htm)'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    vesselVoyage:      
      description: 'Reference number of vessel voyage. See [UNTDID - D.95B - Segment RFF - C506 (1154)](https://service.unece.org/trade/untdid/d95b/uncl/uncl1154.htm)'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
  required:      
    - id      
    - type      
    - vesselImo      
    - containerIdentification      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/EdiCodeco/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.MarineTransport/EdiCodeco/schema.json      
  x-model-tags: i4trust      
  x-version: 0.1.0      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 有效载荷示例    
#### EdiCodeco NGSI-v2 键值示例    
下面是一个以 JSON-LD 格式作为键值的 EdiCodeco 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:mrn:eshuv:edi-codeco:1625763902090",  
  "type": "EdiCodeco",  
  "fileName": "file name",  
  "sentAt": "2023-08-11T14:50:00Z",  
  "travelReference": "110823110823CCHRIB",  
  "ata": "2023-08-11T14:47:00Z",  
  "bookingCode": "FUE110823",  
  "containerCarrierIdentification": "ALU",  
  "containerClass": "Export",  
  "containerIdentification": "TESI1120274",  
  "containerIsoCode": "Refrigerated tank",  
  "containerSeal": "28103",  
  "containerWeight": 27000,  
  "destinationTransportType": "Vessel",  
  "dischargingPort": "ESFUE",  
  "functionCode": "Deletion",  
  "isContainerEmpty": false,  
  "loadingPort": "ESHUV",  
  "operationType": "Port of entry",  
  "originTransportType": "Truck",  
  "messageRaw": "UNB+UNOA:1+ESHUV+PA+230811:1450+174749339'UNH+92218+CODECO:D:95B:UN:SMDG16'BGM+34++9'TDT+20+110823110823CCHRIB+1++ALU:172:166:ALUsios+++1111111:146::CHRISTIAN'RFF+ON:110823110823CCHRIB'NAD+CF+ALU:172:166'NAD+MS+ESSCT:160:ZZZ'EQD+CN+TESI1120274+4EG1:102:5++2+5'RFF+BN:FUE110823'RFF+ACA:FUE110823'DTM+7:202308111447:203'LOC+9+ESHUV:139:6'LOC+11+ESFUE:139:6'LOC+165+ESHUV:139:6+CONCHUV:TER:ZZZ'LOC+164+ESFUE:139:6'MEA+AAE+VGM+KGM:27000.0'SEL+88200+SH'TDT+1++3++:172:ZZZ+++993NGR:146'DTM+ACT:202308111447:203'NAD+CA+ALU:172:166'NAD+CF+ALU:172:166'CNT+16:1'UNT+000022+92218'UNZ+1+174749339'",  
  "receiverIdentification": "PA",  
  "release": "95B",  
  "senderIdentification": "ESHUV",  
  "truckLicenseCode": "993NGR",  
  "messageVersion": "D",  
  "vesselCarrier": "ALQ",  
  "vesselImo": 1111111,  
  "vesselName": "Name",  
  "vesselVoyage": "110823110823CCHRIB"  
}  
```  
</details>    
#### EdiCodeco NGSI-v2 标准化示例    
下面是一个规范化 JSON-LD 格式的 EdiCodeco 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:mrn:eshuv:edi-codeco:1625763902090",  
  "type": "EdiCodeco",  
  "fileName": {  
    "type": "Text",  
    "value": "file name"  
  },  
  "sentAt": {  
    "type": "DateTime",  
    "value": "2023-08-11T14:50:00Z"  
  },  
  "travelReference": {  
    "type": "Text",  
    "value": "110823110823CCHRIB"  
  },  
  "ata": {  
    "type": "DateTime",  
    "value": "2023-08-11T14:47:00Z"  
  },  
  "bookingCode": {  
    "type": "Text",  
    "value": "FUE110823"  
  },  
  "containerCarrierIdentification": {  
    "type": "Text",  
    "value": "ALU"  
  },  
  "containerClass": {  
    "type": "Text",  
    "value": "Export"  
  },  
  "containerIdentification": {  
    "type": "Text",  
    "value": "TESI1120274"  
  },  
  "containerIsoCode": {  
    "type": "Text",  
    "value": "Refrigerated tank"  
  },  
  "containerSeal": {  
    "type": "Text",  
    "value": "28103"  
  },  
  "containerWeight": {  
    "type": "Number",  
    "value": 27000  
  },  
  "destinationTransportType": {  
    "type": "Text",  
    "value": "Vessel"  
  },  
  "dischargingPort": {  
    "type": "Text",  
    "value": "ESFUE"  
  },  
  "functionCode": {  
    "type": "Text",  
    "value": "Deletion"  
  },  
  "isContainerEmpty": {  
    "type": "Boolean",  
    "value": false  
  },  
  "loadingPort": {  
    "type": "Text",  
    "value": "ESHUV"  
  },  
  "operationType": {  
    "type": "Text",  
    "value": "Port of entry"  
  },  
  "originTransportType": {  
    "type": "Text",  
    "value": "Truck"  
  },  
  "messageRaw": {  
    "type": "Text",  
    "value": "UNB+UNOA:1+ESHUV+PA+230811:1450+174749339'UNH+92218+CODECO:D:95B:UN:SMDG16'BGM+34++9'TDT+20+110823110823CCHRIB+1++ALU:172:166:ALUsios+++1111111:146::CHRISTIAN'RFF+ON:110823110823CCHRIB'NAD+CF+ALU:172:166'NAD+MS+ESSCT:160:ZZZ'EQD+CN+TESI1120274+4EG1:102:5++2+5'RFF+BN:FUE110823'RFF+ACA:FUE110823'DTM+7:202308111447:203'LOC+9+ESHUV:139:6'LOC+11+ESFUE:139:6'LOC+165+ESHUV:139:6+CONCHUV:TER:ZZZ'LOC+164+ESFUE:139:6'MEA+AAE+VGM+KGM:27000.0'SEL+88200+SH'TDT+1++3++:172:ZZZ+++993NGR:146'DTM+ACT:202308111447:203'NAD+CA+ALU:172:166'NAD+CF+ALU:172:166'CNT+16:1'UNT+000022+92218'UNZ+1+174749339'"  
  },  
  "receiverIdentification": {  
    "type": "Text",  
    "value": "PA"  
  },  
  "release": {  
    "type": "Text",  
    "value": "95B"  
  },  
  "senderIdentification": {  
    "type": "Text",  
    "value": "ESHUV"  
  },  
  "truckLicenseCode": {  
    "type": "Text",  
    "value": "993NGR"  
  },  
  "messageVersion": {  
    "type": "Text",  
    "value": "D"  
  },  
  "vesselCarrier": {  
    "type": "Text",  
    "value": "ALQ"  
  },  
  "vesselImo": {  
    "type": "Number",  
    "value": 1111111  
  },  
  "vesselName": {  
    "type": "Text",  
    "value": "Name"  
  },  
  "vesselVoyage": {  
    "type": "Text",  
    "value": "110823110823CCHRIB"  
  }  
}  
```  
</details>    
#### EdiCodeco NGSI-LD 键值示例    
下面是一个以 JSON-LD 格式作为键值的 EdiCodeco 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:mrn:eshuv:edi-codeco:1625763902090",  
  "type": "EdiCodeco",  
  "fileName": "file name",  
  "sentAt": "2023-08-11T14:50:00Z",  
  "travelReference": "110823110823CCHRIB",  
  "ata": "2023-08-11T14:47:00Z",  
  "bookingCode": "FUE110823",  
  "containerCarrierIdentification": "ALU",  
  "containerClass": "Export",  
  "containerIdentification": "TESI1120274",  
  "containerIsoCode": "Refrigerated tank",  
  "containerSeal": "28103",  
  "containerWeight": 27000,  
  "destinationTransportType": "Vessel",  
  "dischargingPort": "ESFUE",  
  "functionCode": "Deletion",  
  "isContainerEmpty": false,  
  "loadingPort": "ESHUV",  
  "operationType": "Port of entry",  
  "originTransportType": "Truck",  
  "messageRaw": "UNB+UNOA:1+ESHUV+PA+230811:1450+174749339'UNH+92218+CODECO:D:95B:UN:SMDG16'BGM+34++9'TDT+20+110823110823CCHRIB+1++ALU:172:166:ALUsios+++1111111:146::CHRISTIAN'RFF+ON:110823110823CCHRIB'NAD+CF+ALU:172:166'NAD+MS+ESSCT:160:ZZZ'EQD+CN+TESI1120274+4EG1:102:5++2+5'RFF+BN:FUE110823'RFF+ACA:FUE110823'DTM+7:202308111447:203'LOC+9+ESHUV:139:6'LOC+11+ESFUE:139:6'LOC+165+ESHUV:139:6+CONCHUV:TER:ZZZ'LOC+164+ESFUE:139:6'MEA+AAE+VGM+KGM:27000.0'SEL+88200+SH'TDT+1++3++:172:ZZZ+++993NGR:146'DTM+ACT:202308111447:203'NAD+CA+ALU:172:166'NAD+CF+ALU:172:166'CNT+16:1'UNT+000022+92218'UNZ+1+174749339'",  
  "receiverIdentification": "PA",  
  "release": "95B",  
  "senderIdentification": "ESHUV",  
  "truckLicenseCode": "993NGR",  
  "messageVersion": "D",  
  "vesselCarrier": "ALQ",  
  "vesselImo": 1111111,  
  "vesselName": "CHRISTIAN",  
  "vesselVoyage": "110823110823CCHRIB",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### EdiCodeco NGSI-LD 标准化示例    
下面是一个规范化 JSON-LD 格式的 EdiCodeco 示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:mrn:eshuv:edi-codeco:1625763902090",  
    "type": "EdiCodeco",  
    "fileName": {  
        "type": "Property",  
        "value": "file name"  
    },  
    "sentAt": {  
        "type": "Property",  
        "value": {  
            "@value": "2023-08-11T14:50:00Z",  
            "@type": "DateTime"  
        }  
    },  
    "travelReference": {  
        "type": "Property",  
        "value": "110823110823CCHRIB"  
    },  
    "ata": {  
        "type": "Property",  
        "value": {  
            "@value": "2023-08-11T14:47:00Z",  
            "@type": "DateTime"  
        }  
    },  
    "bookingCode": {  
        "type": "Property",  
        "value": "FUE110823"  
    },  
    "containerCarrierIdentification": {  
        "type": "Property",  
        "value": "ALU"  
    },  
    "containerClass": {  
        "type": "Property",  
        "value": "Export"  
    },  
    "containerIdentification": {  
        "type": "Property",  
        "value": "TESI1120274"  
    },  
    "containerIsoCode": {  
        "type": "Property",  
        "value": "Refrigerated tank"  
    },  
    "containerSeal": {  
        "type": "Property",  
        "value": "28103"  
    },  
    "containerWeight": {  
        "type": "Property",  
        "value": 27000  
    },  
    "destinationTransportType": {  
        "type": "Property",  
        "value": "Vessel"  
    },  
    "dischargingPort": {  
        "type": "Property",  
        "value": "ESFUE"  
    },  
    "functionCode": {  
        "type": "Property",  
        "value": "Deletion"  
    },  
    "isContainerEmpty": {  
        "type": "Property",  
        "value": false  
    },  
    "loadingPort": {  
        "type": "Property",  
        "value": "ESHUV"  
    },  
    "operationType": {  
        "type": "Property",  
        "value": "Port of entry"  
    },  
    "originTransportType": {  
        "type": "Property",  
        "value": "Truck"  
    },  
    "messageRaw": {  
        "type": "Property",  
        "value": "UNB+UNOA:1+ESHUV+PA+230811:1450+174749339'UNH+92218+CODECO:D:95B:UN:SMDG16'BGM+34++9'TDT+20+110823110823CCHRIB+1++ALU:172:166:ALUsios+++1111111:146::CHRISTIAN'RFF+ON:110823110823CCHRIB'NAD+CF+ALU:172:166'NAD+MS+ESSCT:160:ZZZ'EQD+CN+TESI1120274+4EG1:102:5++2+5'RFF+BN:FUE110823'RFF+ACA:FUE110823'DTM+7:202308111447:203'LOC+9+ESHUV:139:6'LOC+11+ESFUE:139:6'LOC+165+ESHUV:139:6+CONCHUV:TER:ZZZ'LOC+164+ESFUE:139:6'MEA+AAE+VGM+KGM:27000.0'SEL+88200+SH'TDT+1++3++:172:ZZZ+++993NGR:146'DTM+ACT:202308111447:203'NAD+CA+ALU:172:166'NAD+CF+ALU:172:166'CNT+16:1'UNT+000022+92218'UNZ+1+174749339'"  
    },  
    "receiverIdentification": {  
        "type": "Property",  
        "value": "PA"  
    },  
    "release": {  
        "type": "Property",  
        "value": "95B"  
    },  
    "senderIdentification": {  
        "type": "Property",  
        "value": "ESHUV"  
    },  
    "truckLicenseCode": {  
        "type": "Property",  
        "value": "993NGR"  
    },  
    "messageVersion": {  
        "type": "Property",  
        "value": "D"  
    },  
    "vesselCarrier": {  
        "type": "Property",  
        "value": "ALQ"  
    },  
    "vesselImo": {  
        "type": "Property",  
        "value": 1111111  
    },  
    "vesselName": {  
        "type": "Property",  
        "value": "Name"  
    },  
    "vesselVoyage": {  
        "type": "Property",  
        "value": "110823110823CCHRIB"  
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
